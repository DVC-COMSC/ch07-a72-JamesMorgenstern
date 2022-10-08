
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
count = 0

for i in range(len(num2)):
    for j in range(len(num1)):
        if(num2[i] == num1[j]):
            count += 1

if(count >= len(num2)):
    print("True")
else:
    print("False")
# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
