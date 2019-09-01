
#!/usr/bin/env python
import os
import subprocess

def autoGrade():
	result = "";
	subprocess.call("rm -f ./a.out", shell=True)
	retcode = subprocess.call("/usr/bin/g++ walk.cc", shell=True) 
	if retcode:
	 return("failed to compile walk.cc")
	 exit

	subprocess.call("rm -f ./output", shell=True) 
	if(not os.access('test.sh', os.X_OK)):
		return("test script no exe rights")
		exit
	
	retcode = subprocess.call("./test.sh", shell=True)

	result = "Score: " + str(retcode) + " out of 2 correct.";
	#print ("Score: " + str(retcode) + " out of 2 correct.")
	print("*************Original submission*************")
	with open('walk.cc','r') as fs:
 	 print(fs.read())
	return result