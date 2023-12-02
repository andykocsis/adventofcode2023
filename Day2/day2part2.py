import re

rawdata = []
powertotal = 0

file_path = "c:/Users/eagle/Documents/AdventOfCode/Day2/day2.txt"

#Read in input file
with open(file_path, "r") as f:
	for line in f:
		line = line.strip()
		rawdata.append(line)

for x in rawdata:
	game_data = re.split(r':|,|;', x)
	green_int = []
	red_int = []
	blue_int = []
	
	#Separate input string into 4 separate lists, based on the color and another with the game 
	for x in game_data:
		color = 'green'
		greenvalues = [i for i in game_data if color in i]
		color = 'red'
		redvalues = [i for i in game_data if color in i]
		color = 'blue'
		bluevalues = [i for i in game_data if color in i]
		color = 'Game'
		gamevalues = [i for i in game_data if color in i]

	#Convert list from strings to ints, store the highest number
	for y in greenvalues:
		green = re.search('\d+', y)
		green_int.append(int(green.group()))
	high_green = max(green_int)

	for y in redvalues:
		red = re.search('\d+', y)
		red_int.append(int(red.group()))
	high_red = max(red_int)

	for y in bluevalues:
		blue = re.search('\d+', y)
		blue_int.append(int(blue.group()))
	high_blue = max(blue_int)

	game = re.search('\d+', gamevalues[0])
	game_int = int(game.group())

	#Multiply highest numbers found previously to get power
	power = high_green*high_red*high_blue
	powertotal += power

print(powertotal)