TBC = 0
sum = 0
n = int(input("Nhap N:"))
for i in range (1,n+1):
 sum = sum + i
 TBC = sum
print("Tong la:", str(sum))
print("TBC la:", TBC/n)