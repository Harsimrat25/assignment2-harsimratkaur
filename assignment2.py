#q1
txt='Python is a case sensitive language'
print(len(txt))
print(txt[::-1])
name=txt[10:]
print(name)
print(txt.replace('a case sensitive','object oriented'))
print(txt.index('a'))
print(txt.replace(' ',''))

#q2
name='Harsimrat Kaur'
SID=21104115
dep='Electrical Engineering'
CGPA=9.9
print('Hey,%s Here!'%(name))
print('My SID is %d'%(SID))
print('I am from %s department and my CGPA is %s'%(dep,CGPA))

#q3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)

#q4
a=int(input("Enter number in a: "))
b=int(input("Enter number in b: "))
c=int(input("Enter number in c: "))
print('Largest number is:',max(a,b,c))

#q5
string=input('Enter a sentence:')
if 'name' in string:
 print('Yes')
else:
 print('No')

#q6
side1=int(input('Length of 1st side:'))
side2=int(input('Length of 2nd side:'))
side3=int(input('Length of 3rd side:'))
#A triangle is formed only when the sum of any two sides is greater than or equal to the third one
if side1>=(side2+side3) and side2>=(side1+side3) and side3>=(side1+side2):
 print('No, Triangle cannot be formed')
else:
 print('Yes,Triangle can be formed')
 


























