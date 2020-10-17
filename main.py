print("Enter three-digit number: ", end="")
a=int(input())

a_h=a//100
a_d=(a%100)//10
a_n=(a%100)%10

b=a_h*100+a_d*10+a_n
print(b)
a1=a_h*100+a_n*10+a_d
print(a1)
a2=a_n*100+a_h*10+a_d
print(a2)
a3=a_n*100+a_d*10+a_n
print(a3)
a4=a_d*100+a_h*10+a_n
print(a4)
a5=a_d*100+a_n*10+a_h
print(a5)