#%d operator converts numbe
# %s operator converts whatever it sees into a string
# %r string representation of the object inclues "" , '

print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))


print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))


print('This is my ten-character, two-decimal number:%10.2f' %13.579)

name = 'Fred'
print(f"He said his name is {name}.")


num = 23.45678
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

i,j,k,l = 5,6,7,8
print(f"Number - {i} {j} {k} {l}")