import json

""" Software created by Splinter, GitHub : https://github.com/Splinter0
    You'll find the explaination of every function in this file, for more info check
    README.md and test.py to see a quick overview of the usage
"""

global filial
filial = ""

class Filial(object):

    """ Here you can create a Filial object, you can load the first two allels
        of your filial with a JSON file ( check filials.json ).
        Or you can manually give two allels.
        To create a Filial object you need to specify the name of your filial,
        if you load from a JSON file ( with .load() ) you need to make sure that the name
        you give to Filial() is actually in your JSON file.
        Then if you're not loading it from a JSON files you need to pass two allels to Filial()

        REMEMBER : The Filial object is gonna take only two allels, so if you pass in a different number than two
                   You're gonna get an error. If you're loading from a JSON file the program will automatically
                   take ONLY the first two allels

        Functions :
                    getName() = It's just gonna return the name of your filial
                    load() = It's the function that allows you to load allels from a JSON file
                    getAllels() = Returns two allels you've created in this filial
    """

    def __init__(self, fil, *kwargs):
        self.fil = fil
        if kwargs :
            self.first = kwargs[0]
            self.second = kwargs[1]


    def getName(self):
        return self.fil

    def getAllels(self):
        global filial
        if self.first and self.second:
            allels = [self.first, self.second]
            return allels
        elif filial == "":
            print("No allels created")
            exit()
        else :
            first, second = filial[0][0], filial[0][1]
            return first, second
    def load(self, place):
        with open(place, "r") as fils:
            fils = json.load(fils)
            load = {}
            found = False
            for key, value in fils.iteritems():
                if key == self.fil:
                    load.update({key:value})
                    found = True
            if found :
                global filial
                filial = load.values()
                return filial
            print("No filial named as "+self.fil+" in "+place)

class Allels(object):

    """ Here is where you create your Allels object, you can pass two allels like this : a = Allels("TT", "Tt")
       or you can direcly pass in your Filial object like so :
       j = Filial("f2", "TT", "Tt"); b = j.getAllels(); a = Allels(b)
       Once you have an Allels object you can combine your two allels to create a new generation using the function
       combine().
       After you have your new 4 allels created by the combination of the previous two you can keep them in a variable
       or you can also save them in a JSON file using the function save() this way:
       a = Allels("TT", "Tt"); c = a.combine(); a.save(c)
    """

    def __init__(self, *kwargs):
        if not kwargs :
            print("No allels passed")
            exit()
        if type(kwargs[0]) is list:
            try :
                error = kwargs[1]
                print("You can't pass more than one filial!")
                exit()
            except IndexError :
                try :
                    self.first = kwargs[0][0]
                    self.second = kwargs[0][1]
                except IndexError :
                    self.first = kwargs[0][0][0]
                    self.second = kwargs[0][0][1]
        else :
            try :
                self.first = kwargs[0]
                self.second = kwargs[1]
            except IndexError :
                print("You need to pass two allels")
                exit()
        if len(self.first) != 2 or len(self.second) != 2 :
            print("An allel is formed by two characters ")
            exit()

    def combine(self):
        self.first = [self.first[:1], self.first[1:]]
        self.second = [self.second[:1], self.second[1:]]
        combo = []
        for x in range(len(self.first)):
            if self.first[x].islower():
                combo.append(self.second[x] + self.first[x])
                combo.append(self.second[x] + self.first[1])
            else:
                combo.append(self.first[x] + self.second[x])
                combo.append(self.first[x] + self.second[1])

        return combo

    def save(self, filName, place, *kwargs):
        f = open(place, "w")
        if not kwargs :
            print("No allels passed")
            exit()
        try :
            error = kwargs[2]
            print("You can pass only one filial or two allels")
            exit()
        except IndexError:
            pass

        als = []
        for arg in kwargs[0]:
            als.append(arg)

        fil = {filName:als}
        place = open(place, 'wb')
        json.dump(fil, place, sort_keys=False,
                  indent=4, separators=(',', ': '))

        return filName



"""TODO : SAVE FUNCTION"""
