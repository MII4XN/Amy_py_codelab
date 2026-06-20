item=["shirt","pants","toothbrush","toothpaste","bag","water","snack","hat","sunscreen","food"]

item.remove("hat") # ["shirt","pants","toothbrush","toothpaste","bag","water","snack","sunscreen","food"]
item.remove("sunscreen")#["shirt","pants","toothbrush","toothpaste","bag","water","snack","food"]
item.remove("snack")#["shirt","pants","toothbrush","toothpaste","bag","water","food"]
item.append("food2")#["shirt","pants","toothbrush","toothpaste","bag","water","snack","food",food2]
item.pop()#["shirt","pants","toothbrush","toothpaste","bag","water","food"]
x=len(item)#8
print("bag" in item)

print(item)
print(x)

y="Skibidy"
print(y[5])
#d

print(item[5]) #

print(item[-1]) #

trigo = ["sin", "cos", "tan", "sec", "cot"]

print(trigo[3])	# sec

print(trigo[1])	# cos

print(trigo[0])	# sin

print(trigo[-1])	# cot

string = "codelabrama2"
letters = list(string)

print(letters)

print(letters[1:])
# odelabrama2
print(letters[:3])
# cod
print(letters[7:])
# rama2
print(letters[::3])
#cebm


menu=["salmon","pizza","water","rice","egg","milk","bread"]

print(len(menu))
if "egg" in menu :
    print("we have egg in menu")
print(menu[2])
menu.remove("water")
menu.append("water")
print(menu[2])
print(menu[5:7])

my_list=[1,2,3]
print(my_list[1:10]) # 2 3
subject=[["Phonic","computer","math","lang",],["sci","art,","insight","thai"],["art","com","math","phonic"],
["lang","sci","thai","insight"],["art","insight","math","sci"]]
print(subject)
print(subject[1][3]) #thai
print(subject[3][1])#sci
print(subject[2][1:4])#com math phonic
print(subject[4][0:3])#art insight math sci
print(subject[0][0:3:2])#phonic math
print(subject[2][0:3:2])#art math
print(subject[4][0:3:2])#art math
print(subject[-1][-1])#sci
print(subject[4][::-1])#sci math insight art





