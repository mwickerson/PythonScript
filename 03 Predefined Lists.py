#Predefined Lists

#Make predefined lists of data in advance
#There are different options for the range of data that you want to receive
#from the list (Start, Start stop, Start stop step)

#Create a list from 0 to 10 with a step of 2
nums = range(0,10,2)
print nums

#Create a list from 0 to 10 with a step with no step
nums = range(0,10)
print nums

#Create a list from 0 to 20
#If you are starting at zero you can type in the end number only and it 
#will automatically create a range until that number is reached
nums = range(20)
print nums