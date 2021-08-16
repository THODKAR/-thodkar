num=int(input("enter the number"))
if num<0:
    print("{} is a negative number".format(num))
elif(num>0):
        print("{} is a positive number".format(num))
        if(num%2==0):
            print("{} is even number".format(num))
        else:
            print("{} is odd number".format(num))

        def fact(num):
            if(num==0):
                return 1
            return num*fact(num-1)
        result=fact(num)
        print("{} is the factorial of {}".format(result,num))
        def isprime(num):
            for i in range(2,num):
                if(num%i==0):
                    print("{} is not a prime number".format(num))
                    break
            else:
                print("{} is a prime number".format(num))
        isprime(num)

else:
    print("{} is zero".format(num))

print(bin(num),"in binary")
print(oct(num),"in octal")
print(hex(num),"in hexadecimal")
