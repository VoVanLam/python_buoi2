tong13 = 0
n = int(input("Nhap N:"))
for i in range (n+1):
    if (i < 14):
     tong13 = tong13 + i
    else:
     break
print("Tong 13 so dau la:", tong13)