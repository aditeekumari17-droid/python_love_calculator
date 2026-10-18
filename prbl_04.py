#love calculator
name = input("Enter your full name: ")
partner_name = input("Enter your partner name: ")
combine_string = name + partner_name
lower_case = combine_string.lower()

t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')
true = t+r+u+e

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')
love = l+o+v+e

score = int(str(true) + str(love))


if score<10 or score>90:
    print(f"Your love score is {score} and you go together like coke and mentos")
elif score>=40 and score<=50:
    print(f"Your love score is {score} and you  are alright together :)")
else:
    print(f"your love score is {score}")
