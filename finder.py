import sys
import re
import string
import datetime
import os

#This Python Script will read an input text file with a list of strings and search a second input file for the string from the first input file.
#Running this script from a command line requires the following.
#finder.py -c [debug] infile1 infile2 outfile1
#
#
y=0 #rline1 counter
x=0 #rline2 counter
z=1000000 #maximum counter limit
chrTab = chr(9)

ddebug = sys.argv[2]
#change the value of debug to turn it off yes turns it on!
debug = "no"
if ddebug == "yes":
	debug = "yes"
#change debug value and max limit of z from 1m to 10
if ddebug == "yes10":
	debug = "yes"
	z=10
if ddebug == "yes1":
	debug = "yes"
if ddebug == "yes2":
	debug = "yes"
#Input Files
fileI1=sys.argv[3]	
fi1 = open(fileI1)
fileI2=sys.argv[4]	

#Output File - Overwritten **
fileO1=sys.argv[5]	
fo1 = open(fileO1, 'w')
fo1.write("#Checking Files for Content\n")
#initiate first values for rline1 and rline2
rline1 = fi1.readline()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#Scan through the lines of the input file.
if debug == "yes":
	print("pre loop")

while rline1:
	if debug == "yes":
		print("Checking for: " + rline1)
		os.system("pause")
	if debug == "yes1":
		print("Checking for: " + rline1)
	y = y + 1
	if y > z: 
		break
	fi2 = open(fileI2)
	rline2 = fi2.readline()
	while rline2:
		rline1 = rline1.upper()
		rline1 = rline1.strip()
		rline2 = rline2.upper()
		if ddebug == "yes2":
			print("in loop")
			print(rline2)
			print(rline1)
		s1 = re.search(rline1, rline2)
		if s1: 
			#found a match!
			fo1.write(rline1 + "\n") 
			fo1.write(rline2)
			#break
		rline2 = fi2.readline()
		x = x + 1
	fi2.close()	
	rline1 = fi1.readline()

print("Input File 1: Lines processed: "  + str(y))
print("Input File 2: Lines processed: "  + str(x))

fi1.close()
fi2.close()
fo1.close() 
