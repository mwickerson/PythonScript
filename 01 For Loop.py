#Loop through lists of information

#There is an ability to script structures that
#perform repetitive tasks. These are called loops.
#Some loops perform a set of instructions for a finite time.
#Other loops check a rule, and continue if true

#Create a list
list = ['slab1','slab2','slab3']

#Print the list with a range from zero to the end of the list 
print range(len(list))

#For each item in the range, associate that individual item to the variable 'i'
#Add a semicolon and press enter to add sub-instructions inside the 'for loop'
#The sub-instructions are automatically indented
for i in range(len(list)):
    print i

#Cycle through the list and print the index number and what data is stored at that position 
for i in range(len(list)):
    print i, list[i]