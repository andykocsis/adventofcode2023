import re

rawdata = []
total = 0

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

    #Get game number as int
	game = re.search('\d+', gamevalues[0])
	game_int = int(game.group())

	print(game_int, high_green, high_red, high_blue)

    #Find if the amount of cubes gives a valid result and then add the game number to total
	if high_green <= 13 and high_red <= 12 and high_blue <= 14:
		total += game_int

print(total)