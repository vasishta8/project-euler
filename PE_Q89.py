def roman(x):
	value = 0
	roman_preds = ["IV", "IX", "XL", "XC", "CD", "CM"]
	value_preds = [4, 9, 40, 90, 400, 900]
	roman_nums = ["I", "V", "X", "L", "C", "D", "M"]
	value_nums = [1, 5, 10, 50, 100, 500, 1000]
	for roman_pred in roman_preds:
		if x.find(roman_pred) != -1:
			x = x[0:x.find(roman_pred)]+x[x.find(roman_pred)+2:len(x)]
			value += value_preds[roman_preds.index(roman_pred)]
		else:
			value += 0
	for letter in x:
		c = x.count(letter)
		value += value_nums[roman_nums.index(letter)]

	roman_value = ""
	while value > 0:
		counter = 0
		while value >= 1000 and counter < 4:
			roman_value += "M"
			value -= 1000
			counter += 1
		if value >= 900:
			roman_value += "CM"
			value -= 900
		if value >= 500:
			roman_value += "D"
			value -= 500
		if value >= 400:
			roman_value += "CD"
			value -= 400
		counter = 0
		while value >= 100 and counter < 4:
			roman_value += "C"
			value -= 100
			counter = 0
		if value >= 90:
			roman_value += "XC"
			value -= 90
		if value >= 50:
			roman_value += "L"
			value -= 50
		if value >= 40:
			roman_value += "XL"
			value -= 40
		counter = 0
		while value >= 10 and counter < 4:
			roman_value += "X"
			value -= 10
			counter += 1
		if value >= 9:
			roman_value += "IX"
			value -= 9
		if value >= 5:
			roman_value += "V"
			value -= 5
		if value >= 4:
			roman_value += "IV"
			value -= 4
		counter = 0
		if value >= 1 and counter < 4:
			roman_value += "I"
			value -= 1
			counter += 1

	return roman_value

roman_file = open("0089_roman.txt","r")
roman_text = roman_file.read()
total_chars = 0
new_total_chars = 0
roman_numerals = roman_text.splitlines()
for roman_numeral in roman_numerals:
	total_chars += len(roman_numeral)
	new_total_chars += len(roman(roman_numeral))
print(total_chars-new_total_chars)
