import re

rawdata = []
corrected_data = []
combined_num = []

#Read data from day1.txt into list rawdata
with open("day1.txt") as day1:
	for line in day1:
		line = line.strip()
		rawdata.append(line)
		
for x in rawdata:

	# Compensate for edge cases
	x = x.replace("twone", "21" )
	x = x.replace("oneight", "18" )
	x = x.replace("eightwo", "82" )

	#Standard replacement after edge cases
	x = x.replace("one", "1")
	x = x.replace("two", "2")
	x = x.replace("three", "3")
	x = x.replace("four", "4")
	x = x.replace("five", "5")
	x = x.replace("six", "6")
	x = x.replace("seven", "7")
	x = x.replace("eight", "8")
	x = x.replace("nine", "9")

	corrected_data.append(x)
	
	
#Search for first digit
for y in corrected_data:
	match = re.search('\d', y)
	first_digit = int(match.group())
	
	
	#Search for last digit 
	backmatch = re.search('\d', y [::-1])
	second_digit = int(backmatch.group())
	
	
	#Combine first and last digits
	combined_num.append(first_digit*10+second_digit)
	

total = sum(combined_num)
print(total)

	

	

	
