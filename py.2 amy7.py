# for i in range (1,21):
#     if i == 13:
#         break
#     print(i)
#
# for i in range (1,21):
#     if i == 13:
#         continue
#     print(i)


# print ("--- task 3: break atfrist miltiple of 7 ---")
# for i in range(1, 51):
#     if i%7 == 0:
#         print(f"found {i} - stopping!")
#         break
#
# print()


# print ("--- task 4 ---")
# for i in range(1, 21):
#     if i%3 == 0:
#
#         continue
#     print(i)


class_list=[
    "aim","bar","tang","mai","nut",
    "ohm","pim","que","run","som",
    "top","mk","amy","shiyi","yuki",
    "otto","ford","gina","titan","pat"]
target=input("find a friend (type a name): ")
found=False
for i, name in enumerate(class_list):
    if name ==target:
        print (f"found '{name}' at position {i+1} of {len (class_list)}")
        found = True
        break

if not found :
    print(f"'{target}'is not in the class list")

target2=input ("find another friend : ")
for i, name in enumerate(class_list):
    if name ==target2:
        print (f"found '{name}' at position {i+1} ")
        break
else:
    print (f"'{target2}' is not in the class list")


