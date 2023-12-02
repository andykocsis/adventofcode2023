import re

rawdata = []
combined_num = []

#Read data from day1.txt into list rawdata
with open("day1.txt") as day1:
	for line in day1:
		line = line.strip()
		rawdata.append(line)
		
for x in rawdata:
	
#Search for first digit
	match = re.search('\d', x)
	first_digit = int(match.group())
	
	
#Search for last digit in original string
	backmatch = re.search('\d', x [::-1])
	second_digit = int(backmatch.group())
	
	
#Combine first and last digits
	combined_num.append(first_digit*10+second_digit)

total = sum(combined_num)
print(total)

	

	

	
