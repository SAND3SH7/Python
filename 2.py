# course = "python \n\"programming"
# print(course[:3])
# print(course)

# first = 'sandes'
# last = "shrestha"
# full = f"{first}  {last}"
# print(full)

# course = ('    Python programming')
# print(course.upper())
# print(course.title())
# print(course.strip())
# print(course.find('pro'))
# print(course.replace('p', 'j'))
# print('pro' in course)
# print('swift' not in course)


# age = 22
# if age >= 18:
#     print('eligible')
# else:
#     print('not eligible')

# message = "eligible" if age >= 18 else "not eigible"
# print(message)

# highIncome = True
# goodCredit = True
# student = True
# if highIncome and goodCredit:
#     print('Eligible')
# else:
#     print("not eligible")
# if not student:
#     print('eligible')
# else:
#     print("not eligible")

# age = 22
# if age>=18 and age<65:
# if 18 <= age < 65:
#     print('eligible')

print('sending a message')
successful = False
for number in range(3):
    # print("attemp", number+1, (number+1)*".")
    print('attemp')
    if successful:
        print("successful")
        break
else:
    print('attempted 3 time and failed')
