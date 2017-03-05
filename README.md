# python-mendel

This is a simple python implementation of Gregor Mendel's heredity rule

# Instructions :

First you need to import the lib in your script, like so :

```
from mendel import *
```
## Filial()

To create a Filial() object just type :

```
f = Filial("f1", "Tt", "TT")
```

For the Filial() object you need to pass in the name of your filial and then your allels, you don't need to 
hardcode them, you can import them from a JSON file like so :

```
f = Filial("f1")
i = f.load("filials.json")
```

Make sure that the name that you used in your Filial object is actually in the file you pass.
For more information about the formatting of the JSON file you can check filials.json.

### Functions of a Filial() object :

```
n = f.getName() #Will return the name of your filial
g = f.getAllels() #Will return your allels in an array
l = f.load("filials.json") #Used to load the allels from a JSON file
```

## Allels()

To create a Allels() object just type :

```
a = Alles("TT", "Tt")
```

For the Allels() object you need to pass two allels, or you can pass a Filial() object that contains two allels.
If you've loaded the Filial() from a JSON file, the Allels() object will take only the first two allels of it.

```
f = Filial("f1")
l = f.load("filials.json")
a = Allels(l) #Create a Allels() object passing a Filial() object
```

### Functions of a Allels() object :

```
a = Allels("TT", "tt")
r = a.combine() #Comine your two allels to create a new filial
a.save("f2", "output.json", r) #It saves you new filial in a JSON file
```

For the function <b>save()</b> you need to pass in the name of your new filial, the JSON file for the output and the variable
that contains your new filial ( the one you've created with <b>combine()</b> )

<b>For more info about the usage make sure to check the <i>test.py</i> file</b>

# Soon :

More functions will be added ; )

<b><a href="https://github.com/Splinter0">Splinter</a></b>
