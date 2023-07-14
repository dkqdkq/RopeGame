from rule import rule_A, rule_B
import random
#a = 분자 b = 분모
a = random.randint(1,10000000)
b = random.randint(1,10000000)

arr = []
i=0
print(f"{a}/{b}")
print("\n\n")
while True:
#    print(f"{a}/{b}")
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
