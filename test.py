from mendel import *

"""Here you can find an example of how to use the library"""

f = Filial("f1", "Tt", "TT") #Create our firts filial
n = f.getName() #Get the name of our filial
g = f.getAllels() #Get our allels in a variable
a = Allels(g) #Create an allels object using our g variable
combo = a.combine() #Combine our allels to get a new filial formed by 4 new allels
output = "fil.json"
new = a.save("f2", output, combo) #Output our new filial in a JSON file getting the name of the new filial in a variable

print("Our first filial : "+n+" contains :\n\t "+str(g)+"\n")
print("Lets combine those two allels in a new filial\n")
print("Our new filial : "+new+" contains : \n\t "+str(combo)+"\n")
print("Our new filian is saved in '"+output+"'")
print("\n"+"-"*40+"\n")

"""In this example you'll see that when you pass a filial from a JSON file that has more than 2 allels,
    the program will automatically combine only the first two"""

print("In this example you'll see that when you pass a filial\nfrom a JSON file that has more than 2 allels, the program")
print("will combine only the first two\n")

f = Filial("f1") #Create the filial
fil = f.getName() #Get the name of the filial
l = f.load("filials.json") #Load the allels from a JSON file
a = Allels(l) #Create an allels object
c = a.combine() #Combine the allels

print("The filial : "+fil+" contains : \n\t"+str(l)+"\n\nBut only the first two will be considered :")
print("\t"+str(l[0][0])+", "+str(l[0][1])+"\n")
print("In fact the combination is only between the first two, here the combination :")
print("\t"+str(c))
