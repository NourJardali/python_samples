def pos(list):
    posList = []
    for num in list:
        if num >= 0:
            posList.append(num)
    return posList

def even_count(list):
    count = 0
    for num in list:
        if num%2 == 0:
            count += 1
    return count

def next_number(list):
    for num in range(len(list)):
        if num > 0:
            if not num in list:
                return num

print("positive numbers:")
posList = pos([-1.2,1.3,0.5,-0.7,0.0])
print(*posList)

print("number of even numbers:")
eventListNb = even_count([3,5,4,-1,0])
print(eventListNb)

print("next number:")
list = [5,3,1]
flag = 0
for i in range(len(list)):
    for j in range(len(list)):
        if i != j:
            if list[i] == list[j]:
                flag = 1
    if list[i] < 1:
        flag = 1

if(not flag):
    x = next_number(list)
    print(x)