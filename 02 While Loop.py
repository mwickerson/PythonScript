#Loop through lists of information

#Create a list
list = ['slab1','slab2','slab3']

#Cycle through the list and print the index number and  
#the data that is stored at that position
for i in range(len(list)):
    print i, list[i]

#Create a variable and assign data to it
nocolumns = 10

#Create a 'while loop'
#While the number of columns is greater than zero, continue running the loop
#The loop stops when the condition does not exist anymore or turns false
while nocolumns>0:

#Print the number of columns and text (string text must be in apostrophes)
    print nocolumns, "I have placed a column"

#Reduce the number of columns by 1
    nocolumns = nocolumns-1

