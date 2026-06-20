from empire_week9 import lowest, average

a = "abcdfg"
list1 = list(a)
print(list)

for item in list1:
    print(item)



#easy
friends=["alex","bob","cat","dan" ,"amy","kitty","moo","nam","yuki","shi"]
for friend in friends :
    print(f"hi {friend}!")
print (f"total student is {len(friends)}")

color = ["red","blue","green"]
for c in color:
    print(c)

# #hard
# for i in range(len(friends)):
#     name = friends[i]
#     print(f"Hi {name}")


amy=["a","b","c","d","e","f"]
for i ,name in enumerate(amy):
    print (i,name)

for i in range (len(amy)):
    print(i)
for name in amy:
    print(name)

friends = ["alex", "bob", "cat", "dan", "amy", "kitty", "moo", "nam", "yuki", "shi"]
for i ,name in enumerate(friends):
    print (i,name)






color = ["red","blue","green"]
for i ,name in enumerate(color):
    print (i,name)

num = [1,2,4,5,3,5,3,1,7,3,9,8,3,5,9,7,8,3,5,8,5,9,3,5,6,8,3,9,1,5]
print(num)
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))








sub=["math","eng","sci","lang","thai"]
score=[67,76,99,87,90]
print("-"*35)
for i, sub1 in enumerate(sub):
    print((f"{i+1}. {sub1:10} : {score[i]}"))
print("-"*35)
total=sum(score)
highest=max(score)
lowest=min(score)
average=sum(score)/len(score)



# higest_indx= score.index(highest)h
# print(highest_indx)
print(f"Total     : {total}")
print(f"Highest  : {highest}")
print(f"Lowest    : {lowest}")
print(f"Average   : {average}")
print("-"*35)
higest_index= score.index(highest)
print(f" The highest subject score is  : {sub[higest_index]}")