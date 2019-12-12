#Dictionaries

#Create a dictionary using curly brackets {} 
#Add within the brackets 'keys' and add value to the keys with a semicolon and data
mydict = {"nopanels":10,"xspacing":5,"yspacing":5}

#You can refer to and print data by their name/state rather than their value
print mydict["nopanels"]
print mydict["xspacing"]

#To find out what is in the dictionary, print the keys
print mydict.keys()

#To find out what the values are within the dictionary
print mydict.values()

#Add to the dictionary
mydict["nopanelsY"]=20
print mydict

#Check if something is in the dictionary
#This will tell you a true or false answer
#If it is in the dictionary it will be true
print "nopanels" in mydict

#If it is not in the dictionary it will be false
print "nopanelsx" in mydict


