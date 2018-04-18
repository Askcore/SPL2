n = input("Bitte n eingeben: ")
n = int(n)

print("Alle Zahlen")
for i in range(1, n+1):
    if (i < n):
        print(i, end= ", ")
    else:
        print(i)

print("\nAlle Geraden")
for i in range (1, n+1):
    if(i%2 == 0):
        if(i < n):
            print(i, end=", ")
        else:
            print(i)

print("\nAlle Ungeraden")
for i in range (1,n+1):
    if(i%2 != 0):
        if(i+1 != n):
            print(i, end=", ")
        else:
            print(i)

print("\nAlle durch 9 teilbare Zahlen")
for i in range (1,n+1):
    if(i%9 == 0):
        if(i+1 != n):
            print(i, end=", ")
        else:
            print(i)