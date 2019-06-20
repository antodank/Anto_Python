import requests
import zipfile
import shutil
import os
import pandas as pd
import json

urls = {
    2017: 'https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM',
    2016: 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsrV0VldnVIT1hyb0E',
    2015: 'https://drive.google.com/uc?export=download&id=0B0DL28AqnGsra1psanV1MEdxZk0',
}

filenames = {
    2017: 'survey_results_public.csv', 
    2016: '2016 Stack Overflow Survey Results/2016 Stack Overflow Survey Responses.csv',
    2015: '2015 Stack Overflow Developer Survey Responses.csv',
}

question_names = {
    2017: 'HaveWorkedLanguage',
    2016: 'tech_do',
    2015: 'Select all that apply',
}

def survey_csvname(year):
    return 'survey{}.csv'.format(year)

def download_survey(year):
    print(f"Downloading {year}")
    request = requests.get(urls[year])
    with open("survey.zip", "wb") as file:
        file.write(request.content) 

    with zipfile.ZipFile("survey.zip", "r") as file:
        file.extractall("data")

    shutil.move("data/" + filenames[year], survey_csvname(year))
    shutil.rmtree("data", ignore_errors=True)
    os.remove("survey.zip")

def languages_breakdown(year):
    if not os.path.exists(survey_csvname(year)):
        download_survey(year)

    print(f"Processing {year}")
    data=pd.read_csv(survey_csvname(year), encoding='latin1')

    if year >= 2016:
        # Languages are semicolon separated list in a single column
        languages = data[question_names[year]].str.split(';', expand=True)
    else:
        # Languages are a set of columns, one column per language + other
        # First get a list of column names that represent the set of languages/technology
        current = 0
        columnNames = []

        # Iterate through columns until we get to the language/tech question       
        while data.columns[current] != question_names[year]:
            current += 1

        # Add all columns except for other (which is the last one)
        while data.columns[current + 1].startswith('Unnamed'):
            columnNames.append(data.columns[current])
            current += 1

        # Filter the survey to just the language column names
        languages = data[columnNames]
        languages = languages.drop(0)

    summary = languages.apply(pd.Series.value_counts)
    summary = pd.DataFrame({'count': summary.sum(axis=1).groupby(lambda x: x.strip()).sum()})

    total = data[data[question_names[year]].notnull()].shape[0]
    summary['percent'] = summary['count']/total*100

    return summary

if __name__ == "__main__":
    totals = {}
    for year in range(2011, 2018):
        totals[year] = languages_breakdown(year).to_dict()

    with open('data.json', 'w') as file:
        file.write(json.dumps(totals, indent=4, separators=(',', ': ')))