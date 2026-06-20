# import random
#
# number = random.randint(1, 100)
# guess = 0
# count = 0
#
# while guess != number:
#     guess = int(input("Guess: "))
#     count += 1
#
#     if guess > number:
#         print("Too high")
#     elif guess < number:
#         print("Too low")
#
# print("Correct!")
# print("Guesses =", count)

# answer = ""
#
# while answer.lower() != "bangkok":
#     answer = input("What's the capital of Thailand? ")
#
#     if answer.lower() != "bangkok":
#         print("Try again!")
#
# print("Correct!")

# import random
#
# choices = ["rock", "paper", "scissors"]
#
# rounds = 1
# win = 0
# lose = 0
# tie = 0
#
# while rounds <= 5:
#     user = input("rock / paper / scissors : ")
#     cpu = random.choice(choices)
#
#     print("CPU:", cpu)
#
#     if user == cpu:
#         print("Tie")
#         tie += 1
#     elif (user == "rock" and cpu == "scissors") or \
#          (user == "paper" and cpu == "rock") or \
#          (user == "scissors" and cpu == "paper"):
#         print("You win")
#         win += 1
#     else:
#         print("CPU win")
#         lose += 1
#
#     rounds += 1
#
# print("Final")
# print("Win =", win)
# print("Lose =", lose)
# print("Tie =", tie)
# =====================================================
# 🎵 Stage 1 — Playlist Mayhem
# Python Foundation 2 · Session 6 · Survival Challenge
# =====================================================
# 🎯 GOAL: ทบทวน list operations จาก S1-S2
#         (append, remove, slicing, in)
# ⏱️  TIME: 15 นาที
# 🔑 SKILL: list methods · slicing · for loop
# =====================================================

# 📝 SETUP: playlist เริ่มต้น (มีเพลงปนกัน 8 เพลง)
# playlist = [
#     "ดอกไม้ใจ (เศร้า)",
#     "rock anthem",
#     "เหงาทั้งคืน (เศร้า)",
#     "pump it up",
#     "tears in rain (เศร้า)",
#     "feeling alive",
#     "energy boost",
#     "ฝันร้าย (เศร้า)",
# ]
#
# print("─── Playlist เริ่มต้น ───")
# for song in playlist:
#     print(f"  🎵 {song}")
# print(f"รวม: {len(playlist)} เพลง\n")


# =====================================================
# 📝 TASK 1: เพิ่มเพลงปลุกใจ 3 เพลง (append)
# Hint: ใช้ .append() 3 ครั้ง — เพลงอะไรก็ได้!
# =====================================================
# playlist.append("AA")
# playlist.append("AA")
# playlist.append("AA")
# =====================================================
# 📝 TASK 2: ลบเพลงที่มีคำว่า "เศร้า" ออกทั้งหมด
# Hint: วน loop ผ่าน list สร้างใหม่ที่ไม่มี "เศร้า"
#       (ห้าม remove ตรงๆ เพราะ list จะรวน)
# =====================================================
# playlist_happy = []
# for i in range(len(playlist)):
#     if "เศร้า" not in playlist[i]:
#         playlist_happy.append(playlist[i])
#
# playlist=playlist_happy
# print(playlist)
# =====================================================
# 📝 TASK 3: print Top 5 ออกมา (slicing)
# Hint: ใช้ [:3]
# =====================================================
# a=[]
# a=playlist[-1:-4:-1]
# print(a)
# =====================================================
# 📝 TASK 4 (BONUS): เช็คว่า "เพลงโปรด" ของคุณอยู่ใน playlist มั้ย
# =====================================================
# my_favorite="pump it up"
# if my_favorite in playlist:
#     print("it have ",my_favorite," in playlist")
# else:
#     print("it dont have ",my_favorite," in playlist")



# =====================================================
# 📋 EXPECTED OUTPUT (ตัวอย่าง):
# =====================================================
# ─── Playlist เริ่มต้น ───
#   🎵 ดอกไม้ใจ (เศร้า)
#   🎵 rock anthem
#   ... (8 เพลง)
# รวม: 8 เพลง
#
# ─── Top 5 หลังจัด ───
#   1. rock anthem
#   2. pump it up
#   3. feeling alive
#   4. energy boost
#   5. [เพลงปลุกใจ #1]
#
# 💚 พบเพลงโปรด 'xxx' ใน playlist!
# =====================================================


# =====================================================
# 💡 KEY IDEAS ที่ทบทวน
# =====================================================
# • .append(x)         เพิ่ม x ท้าย list
# • .remove(x)         ลบ x ตัวแรกที่เจอ
# • list[a:b]          slicing — ตั้งแต่ index a ถึง b-1
# • list[:5]           ตั้งแต่ต้นถึง 5 ตัวแรก
# • for x in list      วนทุก item
# • x in list          เช็คว่ามี x มั้ย (True/False)
# • not in             ตรงข้ามของ in
# =====================================================


score=[67,45,58,89,30,78,79,92,56,48]
name=["amy","skibidi","67","pa","wee","oum","nk","shyi","yuki","moo"]
avg=sum(score)/10
top=sorted(score,reverse=True)
print(avg)
print(top)
top3=top[0:3]
print(top3)
lower=(top)[6:9]
print(lower)