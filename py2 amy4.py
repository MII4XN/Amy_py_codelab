# import time
# a=int(input("what time you want to count down: "))
# x=0
# z=0
# step = 0
# if a>0:
#     step = -1
# else:
#     step=1
# for i in range(a,0,step):
#     print(i)
#     x+=i
#     if i%5==0 and i>-20:
#         z+=1
#         print("lab:",z)
#     time.sleep(1)
#     # if i ==0:
#     #     break
# print("end")

# x=0
# for i in range(0,102,2):
#     print(i)
#     x+=i
# print(x)

# list1=[]
# list2=[]
# list3=[]
# for i in range (10,0,-1):
#     list1.append(i)
# print(list1)
#
# for n in range (2,21,2):
#     list2.append(n)
# print(list2)
# for m in range (5,101,5):
#     list3.append(m)
# print(list3)

# import customtkinter as ctk
#
#
# # ----- Window setup -----
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")
#
# app = ctk.CTk()
# app.title("âœ–ï¸ Times Table App")
# app.geometry("360x520")
# app.configure(fg_color="#1a1a1a")
#
#
# # ----- Header -----
# header = ctk.CTkLabel(
#     app, text="âœ–ï¸ TIMES TABLE",
#     font=("IBM Plex Sans Thai", 12, "bold"),
#     text_color="#888"
# )
# header.pack(pady=(20, 4))
#
# base_label = ctk.CTkLabel(
#     app, text="Table of 2",
#     font=("IBM Plex Sans Thai", 24, "bold"),
#     text_color="#fff"
# )
# base_label.pack(pady=4)
#
#
# # ----- Table display -----
# table_label = ctk.CTkLabel(
#     app, text="(drag the slider to choose a number)",
#     font=("JetBrains Mono", 14),
#     text_color="#50FA7B",
#     justify="left"
# )
# table_label.pack(pady=(10, 20))
#
#
# # ----- The main function (EDIT THIS!) -----
# def show_table(value):
#     """Called when slider moves â€” value is the chosen number"""
#     base = int(value)
#     base_label.configure(text=f"Table of {base}")
#
#     # Build the times table text
#     result = ""
#     for i in range(1, 13):
#         # ðŸ“ TODO: Fix the ___ to calculate base Ã— i
#         answer = base*i
#         result += f"{base} x {i:2d} = {answer}\n"
#
#     table_label.configure(text=result)
#
#
# # ----- Slider -----
# slider_label = ctk.CTkLabel(
#     app, text="â† drag to change table â†’",
#     font=("IBM Plex Sans Thai", 11),
#     text_color="#666"
# )
# slider_label.pack(pady=(10, 4))
#
# slider = ctk.CTkSlider(
#     app, from_=2, to=12,
#     number_of_steps=10,
#     width=280,
#     button_color="#C8102E",
#     button_hover_color="#8B0000",
#     progress_color="#E53935",
#     command=show_table,
# )
# slider.set(2)
# slider.pack(pady=8)
#
#
# # ----- Footer -----
# footer = ctk.CTkLabel(
#     app, text="CodeLab Â· Python F2 Â· Session 3",
#     font=("IBM Plex Sans Thai", 10),
#     text_color="#444"
# )
# footer.pack(side="bottom", pady=12)
#
#
# # Initial call to show table of 2
# show_table(2)
#
#
# app.mainloop()


# print("ðŸŽ‚ Birthday Party Budget Calculator")
# print("=" * 40)
#
# # 5 items to buy for the party
# items = ["ðŸŽ‚ Cake", "ðŸ­ Candy", "ðŸ¥¤ Drinks", "ðŸŽˆ Balloons", "ðŸŽ Gifts"]
# total = 0
#
# # ðŸ“ TODO 1: Loop through each item â†’ ask price â†’ add to total
# for item in items:
#     price = int(input(f"{item} price: "))
#     total = total + price
#
#
# # ðŸ“ TODO 2: Print the grand total
# print()
# print("=" * 40)
# print(f"ðŸ’° Grand Total: {total} baht")
#
#
# # ðŸ“ TODO 3: Check if over budget (set budget limit)
# #    If total > 1000 â†’ warn the user
# if total > 2000:
#     print("âš ï¸  Over budget! What can you cut?")
# else:
#     print("âœ… Within budget â€” good planning!")
#
#
# # =====================================================
# # ðŸ“‹ EXAMPLE INTERACTION:
# # =====================================================
# # ðŸŽ‚ Cake price: 500
# # ðŸ­ Candy price: 200
# # ðŸ¥¤ Drinks price: 100
# # ðŸŽˆ Balloons price: 150
# # ðŸŽ Gifts price: 300
# #
# # ðŸ’° Grand Total: 1250 baht
# # âš ï¸  Over budget! What can you cut?
# # =====================================================
#
#
# # =====================================================
# # ðŸŽ BONUS 1: Track prices in a list, find the most expensive
# # =====================================================
# # prices = []
# # for item in items:
# #     price = int(input(f"{item} price: "))
# #     prices.append(price)
# #     total += price
# #
# # max_price = max(prices)
# # max_item = items[prices.index(max_price)]
# # print(f"ðŸ˜± Most expensive: {max_item} ({max_price} baht)")
#
#
# # =====================================================
# # ðŸŽ BONUS 2: Ask parents for their real budget
# # =====================================================
# # budget = int(input("\nWhat's your parents' budget? "))
# # remaining = budget - total
# # if remaining >= 0:
# #     print(f"ðŸ’š {remaining} baht remaining")
# # else:
# #     print(f"ðŸ’” Over by {abs(remaining)} baht")
# # =====================================================
#
#
#
# price = []
# sun=0
# most=0
# cake=int(input("what cake price: "))
# price.append(cake)
# water=int(input("what water price: "))
# price.append(water)
# gift=int(input("what gift price: "))
# price.append(gift)
# candy=int(input("what candy price: "))
# price.append(candy)
# ballon=int(input("what ballon price: "))
# price.append(ballon)
#
# for i in range(0,len(price)):
#     sun+=price[i]
#     if price[i]>most:
#         most=price[i]
# print ("total price is ",sun)
# if sun >1000:
#     print("over budget")
# print("the most expendsive item is price",most)
x=0
row=int(input("how much rows: "))
for i in range (1,row+1):
    print(i," "*(row-i),end="")
    for j in range(1,row+1):
        print(j,end=" ")
    print()








