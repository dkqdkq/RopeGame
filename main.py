from rule import rule_A, rule_B
# a = 분자 b = 분모
a = int(input("분자: "))
b = int(input("분모: "))

arr = []
i=0
print(f"{a}/{b}")
while True:
    if(a > 0):
        a, b = rule_B(a,b)
        print(f"B: {a}/{b}")
        arr.append("B")
        i += 1
    if(a < 0):
        a, b = rule_A(a,b)
        print(f"A: {a}/{b}")
        arr.append('A')
        i += 1
    if(a == 0):
        break

print(i)
print(''.join(arr))