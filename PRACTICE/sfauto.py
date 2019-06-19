import subprocess, sys

def callps1():
	powerShellPath = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'
	powerShellCmd = r"C:\Python\democall.ps1"
	arg1 = 5
 
	p = subprocess.Popen([powerShellPath, '-ExecutionPolicy', 'Unrestricted', powerShellCmd, str(arg1)] , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	rc = p.returncode
	print(rc)
	#print "Return code given to Python script is: ".format(str(rc))
	print(output)
	print(error)
 
#Test
def main():
	print('Calling Main()')
	#ReadCSV()
	callps1()
main()
