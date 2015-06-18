import json
import os

write = 1
workspace = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(workspace + "/workspace"):
	os.makedirs("workspace")
fVersion = open("version.json","r")
version = json.load(fVersion)
print("Nova v" + version['nova.version'])
fVersion.close()
print("")
fileName = raw_input("File Name: ")
print("")
project = open(workspace + r"/workspace/" + fileName, "w")
while write == 1:
	l  = raw_input()
	if l == "e_o_f":
		write = 0
		project.close()
	else:
		project.write(l + "\n")
