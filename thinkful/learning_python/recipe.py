# Ingredients are stored as a dictionary of tuples. Each tuple contains the name
# of the ingredients and the amount in milliliters (unless otherwise specified)
# Why a dictionary of tuples? Because it is kinda convenient, and shows off how to
# combine multiple data structures.

ingredients = {"butter" : ("butter", 118.3),
					"sugar" : ("sugar", 236.6), 
					"vanilla" : ("vanilla", 4.929), 
					"eggs" : ("eggs", 2), #whole eggs
					"cocoa" : ("cocoa", 118.3), 
					"flour" : ("flour", 118.3)
}

# The butter was refrigerated, so it's not soft yet.
butter_soft = False

bowl = []

# To make the cake, we'll need the following functions
def melt(this):
	print("Melting {0}.".format(this))

def bake(this, temp):
	print("Baking at {0} at {1}.".format(this, temp))

def mix(this):
	print("Mixing {0}.".format(this))

def add_to_bowl(ingredient):
	print("Adding {0} to the bowl.".format(ingredient))
	return bowl.append(ingredient)

if butter_soft != True:
	melt(ingredients["butter"][0])
	butter_soft = True

add_to_bowl(ingredients["butter"][0])
add_to_bowl(ingredients["sugar"][0])

mixing_time = 0
mixture_creamy = False

while mixture_creamy == False:
	mix(bowl)
	mixing_time += 1
	if mixing_time == 3:
		mixture_creamy = True

add_to_bowl(ingredients["vanilla"][0])
add_to_bowl(ingredients["eggs"][0])

mix(bowl)

add_to_bowl(ingredients["cocoa"][0])
add_to_bowl(ingredients["flour"][0])

mixing_time = 0
well_blended = False

while well_blended == False:
	mix(bowl)
	mixing_time += 1
	if mixing_time == 4:
		well_blended = True

cake_pan = bowl

cooking_temp = 350
cooking_time = 30

for minute in range(0, cooking_time):
	bake(cake_pan, cooking_temp)

print "Cake is done!"

























