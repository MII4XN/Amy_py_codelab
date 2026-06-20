# text="code lab th"
#
# for char in text :
#     print(char)
#
# print(text.upper())
# print( text.split())
# print(text.replace("a","@"))
from empire_week3 import result


# x=0
# s=["a","e","i","o","u"]
# name=str(input("What your name: "))
# for i in range(len(name)):
#     if  name[i] in s:
#         x+=1
# print(x)
# def reverse (word):
#     result= ""
#     for i in word :
#         result+=i
#
# print(reverse("hello"))     # ควรได้ "olleh"
# print(reverse("codelab"))   # ควรได้ "baledoc"
#
# secret = input("\nพิมพ์คำลับ แล้วให้เพื่อนทาย: ")
# print("คำกลับหลังคือ:", reverse(secret))
def reverse (word):
    result=""
    for i in range(len(word)):
        result = word[i] + result
    return result
print(reverse("hello"))     # ควรได้ "olleh"
print(reverse("codelab"))   # ควรได้ "baledoc"

secret = input("\nพิมพ์คำลับ แล้วให้เพื่อนทาย: ")
print("คำกลับหลังคือ:", reverse(secret))

