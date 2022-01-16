numbers = [1,2,3,4,5,6]
odd_numbers = []
squared_odd_numbers = []
total = 0
# filter for odd numbers
for number in numbers:
   if number % 2 == 1:
      odd_numbers.append(number)
# square all odd numbers
for number in odd_numbers:
   squared_odd_numbers.append(number * number)
# calculate total
for number in squared_odd_numbers:
   total += number
# calculate average