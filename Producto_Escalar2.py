a = list(map(int, input("Lista A: ").split()))
b = list(map(int, input("Lista B: ").split()))
producto = 0
for i in range(len(a)):
    producto += a[i] * b[i]
print("Producto escalar =", producto)