#1-misol
matn = input("Matn kiriting: ")
teskari = matn[::-1]
print("Teskari matn:", teskari)

#2-misol
n = input("Ism kiriting: ")
b = input("Familya kiriting: ")

print(n + b)

#3-misol
n = input("Matn kiriting va python so'zi bor yoki yo'qligini tekshiring: ")
if "python" in n.lower():
    print("Matnda python so'zi bor")
else:
    print("Matnda python so'zi yoq!")
