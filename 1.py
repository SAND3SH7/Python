# name="sandesh"
# print(f"name")

# name='sandesh'
# age=25
# height=5.6
# is_student=True
# print(name,'is',age,'years old')
# print(type(height))

# score=90
# if score>=90:
#     print('Grade:A')
# elif score >=70:
#     print('Grade: B')
# else:
#     print("Grade :F")

# fruits=['apple','banana','cherry','sandesh']
# for fruit in fruits:
#     print(fruit)

# for i in range(5):
#     print(i)

# count=0
# while count<3:
#     print('count:',count)
#     count+=1

# nums=[3,2,5,1,7,90]
# nums.sort()
# print(nums)

# student={
#     'name':'sandesh',
#     'age':25,
#     'is_student':True
# }
# print(student["name"])
# print(student["age"])
# print(student["is_student"])

# student['height']=5.6
# print(student['height'])
# student['age']=90
# print(student)

# for key, value in student.items():
#     print(key, value)
# print(student.keys())
# print(student.values())
# print(student.items())

# print('fuck you dg randiko ban' * 5)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
eqn=input("Enter equation in numpy format: ")
try: 
    def f(x):
        return eval(eqn)
except Exception as e:
    print(f"Error due to {e}")
    exit(0)
a,b=map(float,input("Enter 2 initial guesses: ").split())
fa,fb=f(a),f(b)
if fa*fb>0:
    print("Roots not bracketed.")
    exit(0)
elif abs(fb-fa)<1e-10:
    print("Divisiono by zero. Choose new guesses")
    exit(0)
else:
    E=float(input("Enter tolerable error: "))
    N=int(input("ENter max no of iteration: "))
    ite=1
    t=[]
    m=[]
    while ite<=N:
        num=(a*fb-b*fa)
        den=(fb-fa)
        c=num/den
        fc=f(c)
        t.append([ite,a,b,c,fa,fb,fc,abs(a-b)])
        m.append(c)
        if abs(fc)<1e-10:
            break
        elif fa*fc<0:
            b=c
        else:
            a=c
        if abs(fa-fc)<1e-10:
            print("Division bu zero occured ")
            exit(0)
        elif abs(a-b)<E:
            break
        else:
            ite+=1
    if ite>N:
        print(f'soulution does not converges in {ite-1} iteraions')
    else:
        table=pd.DataFrame(t,columns=['iterations','a','b','c','F(a)','F(b)','F(c)','Error'])
        print(table.to_string(index=False))
        print(f"The approx root is {c} in {ite} iterations")

x=np.linspace(-5,5,1000)
roots=np.array(m)
plt.figure(figsize=(8,6))
plt.plot(x,f(x),linestyle="dotted",color="red",label="Graph")
plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.scatter(roots,np.zeros_like(m),color="blue",marker="*",label="root approximation")
for j in range(len(roots)):
    plt.text(roots[j],0,str(j+1))
plt.title(f"Graph of {eqn}")
plt.grid(True)
plt.legend(loc="upper right")
plt.show()
