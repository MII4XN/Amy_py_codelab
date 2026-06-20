# coins=[10,25,5,50,1,100,20,5,10,50]
# total=0
# biggest=0
# for i in range(len(coins)):
#     x=coins[i]
#     total+=x
#     if x>biggest:
#         biggest=x
# print(total)
# print(biggest)
# print(sum(coins))
# print(max(coins))
from empire_week2 import celsius


# target_sum = int(input("Enter the target sum: "))
#
# current_sum = 0
#
# num = 1
#
# while current_sum <target_sum:
#     current_sum+=num
#     print((f" current sum up to {num} is {current_sum}. "))
#     num +=1
# print((f" The sum of number up to {num-1} is {current_sum}. "))

#
# rate=float(input("Enter the rate value: "))
# initial=int(input("Enter the initial value: "))
# target=int(input("Enter the target value: "))
# year=1
#
# while initial<target:
#     bonus=initial*rate/100
#     initial = initial+bonus
#     print((f" After year {year},current value {initial}. "))
#     year+=1
# print((f" it will take {year-1}. "))


# t1=15*2
# t2=80*2
# t3=50*3
# print(t1)
# print(t2)
# print(t3)
# def calc(price ,qty):
#     return price*qty
#
# print(calc(15,2))
# print(calc(80,2))
# print(calc(46,2))






# def calc_price(name ,qty):
#     return name * qty
#
#
# print(calc_price(cola, 20))

# ═══════════════════════════════════════════════════════════
# 🖥️ W1 · Calc Price — เฉลยความเหนื่อยของ S7!
# F2 Session 08 · Functions
# ═══════════════════════════════════════════════════════════
#
# 🎯 หน้าที่ของเด็ก: เติมโค้ดตรง  # TODO
# จำร้านขายน้ำ 5 รายการของ S7 ได้มั้ย? ที่เขียนซ้ำจนเหนื่อย?
# วันนี้เราจะทำให้มันเหลือ function เดียว!
# ───────────────────────────────────────────────────────────

# 😩 แบบ S7 (เขียนซ้ำ) — ดูไว้เป็นตัวอย่างความเหนื่อย:
# total1 = 15 * 2
# print("โค้ก = " + str(total1))
# total2 = 80 * 1
# print("ผัดไทย = " + str(total2))
# ... ทำซ้ำ 5 รอบ = 40 บรรทัด!


# ✨ แบบ S8 (function เดียว):
# def calc_price(name, price, qty):
#     # TODO 1: คำนวณราคารวม (price คูณ qty) เก็บในตัวแปร total
#     total = price*qty # 👈 แก้ตรงนี้
#
#     # TODO 2: ส่งข้อความกลับออกไป เช่น "โค้ก = 30 บาท"
#     return name + " = " + str(total) + " บาท"
#
#
# # ───────────────────────────────────────────────────────────
# # เรียกใช้ function 5 ครั้ง (แทน copy-paste 40 บรรทัด!)
# print(calc_price("โค้ก", 15, 2))
# print(calc_price("ผัดไทย", 80, 1))
# print(calc_price("ส้มตำ", 50, 3))
# print(calc_price("ต้มยำ", 120, 1))
# print(calc_price("ชาเย็น", 35, 4))
#
# # ✅ เสร็จแล้ว: เห็นมั้ยว่า 5 บรรทัด แทน 40 บรรทัด!

# def get_grade(x):
#     if x>=80:
#         return "A"
#     elif x>=70:
#         return "B"
#     elif x>=60:
#         return"C"
#     elif x>=50:
#         return"D"
#     else:
#         return"F"
#
# print("คะแนน 85 ได้เกรด:", get_grade(85))   # ควรได้ B
# print("คะแนน 95 ได้เกรด:", get_grade(95))   # ควรได้ A
# print("คะแนน 45 ได้เกรด:", get_grade(45))   # ควรได้ F
# print("คะแนน 45 ได้เกรด:", get_grade(70))   # ควรได้ F
# print("คะแนน 45 ได้เกรด:", get_grade(60))   # ควรได้ F
# print("คะแนน 45 ได้เกรด:", get_grade(55))   # ควรได้ F


# ═══════════════════════════════════════════════════════════
# 🎨 Mini · Unit Converter (°C ↔ °F) — CustomTkinter Template
# F2 Session 08 · Functions
# ═══════════════════════════════════════════════════════════
#
# 🎯 หน้าที่ของเด็ก: เติมแค่ 2 function ตรง # TODO
# ❌ ห้ามแตะส่วน UI ด้านล่าง (ครูเตรียมไว้ให้แล้ว)
# ───────────────────────────────────────────────────────────

# ─── ส่วนที่เด็กต้องแก้ (FUNCTIONS) ─────────────────────────
def c_to_f(c):
    # TODO 1: แปลง Celsius เป็น Fahrenheit
    # สูตร: c * 9/5 + 32
    return   c * 9/5 + 32# 👈 แก้ตรงนี้

def f_to_c(f):
    # TODO 2: แปลง Fahrenheit เป็น Celsius
    # สูตร: (f - 32) * 5/9
    return (f - 32) * 5/9 # 👈 แก้ตรงนี้
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (UI — ครูจะอธิบายภายหลัง)
import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("เครื่องแปลงอุณหภูมิ")
app.geometry("360x260")

entry = ctk.CTkEntry(app, placeholder_text="ใส่ตัวเลข", width=200)
entry.pack(pady=20)
result = ctk.CTkLabel(app, text="ผลลัพธ์จะขึ้นตรงนี้", font=("IBM Plex Sans Thai", 18))
result.pack(pady=10)

def do_c_to_f():
    val = float(entry.get())
    result.configure(text=str(val) + "°C = " + str(c_to_f(val)) + "°F")

def do_f_to_c():
    val = float(entry.get())
    result.configure(text=str(val) + "°F = " + str(round(f_to_c(val), 1)) + "°C")

ctk.CTkButton(app, text="°C → °F", command=do_c_to_f).pack(pady=6)
ctk.CTkButton(app, text="°F → °C", command=do_f_to_c).pack(pady=6)

app.mainloop()
