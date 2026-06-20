import random
#
# dice = 0
# count = 0
# while dice != 4 :
#     dice = random.randint(2,12)
#     count = count + 1
#
#     print(f"roll{count}:{dice}")
#
# print(f" got 6 after {count} roll!")



# x=0
# while True:
#     print(x)
#     x = x+1
#     break


# for i in range (10,0,-1):
#    print(i)


# amy=10
# while amy >=0:
#     print(amy)
#     amy-=1


# for i in range(1,13):
#     w = i * 7
#     print(w)
#
# word=54321
# x=0
# while word != x:
#     x = int(input("what is your password: "))
# print("Pass")





# money=10000
# x=0
# z=0
# while z<money:
#     z += random.randint(100, 1000)
#     print(f"random,{x}:{z}")
#     x+=1
#
# print(f" got 10000 after {x} money!")\


num= random.randint(1, 100)
x=0
while num != x:

    x = int(input("what is your number: "))
    if x <num:
        print ("too low")
    if x >num:
        print("too hight")
print("corret")