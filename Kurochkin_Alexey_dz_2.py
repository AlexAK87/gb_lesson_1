
numbers = []
numbers_for_sum = []

for i in range(0, 1000):
    if i%2 != 0:
        numbers.append(i**3)

for number in numbers:
    sum = 0
    number_process = number
    while number_process > 0:
        num = number_process % 10
        sum += num
        number_process = number_process // 10
    if sum % 7 == 0:
        numbers_for_sum.append(number)

total1 = 0
total2 = 0
sum_number = 0

for nums in numbers_for_sum:
    total1 += nums
    number_process = nums
    number_process += 17
    while number_process > 0:
        num = number_process % 10
        sum_number += num
        number_process = number_process // 10
    if sum_number % 7 == 0:
        total2 += nums

print(numbers)
print(numbers_for_sum)
print(total1)
print(total2)
