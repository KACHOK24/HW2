# juft = []
# toq = []

# for i in range(10):
#     son = int(input("Son kiriting: "))

#     if son % 2 == 0:
#         juft.append(son)
#     else:
#         toq.append(son)

# print("Juft sonlar:", juft)
# print("Toq sonlar:", toq)


# parol = ("py1234")

# for i in range(3):
#   kiriting = (input("parol kiriting:"))
#   if kiriting == parol:
#    print("xush kelipsiz")
#   else:
#    print("parol notg'ri")
son = int(input("Son kiriting: "))

for i in range(1, son + 1):
    if son % i == 0:
        print(i)
