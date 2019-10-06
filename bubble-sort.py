# list1 = [10,15,4,23,0]
list1 =[]
print("Enter size of the list:")
size=int(input())

for i in range(size):
    print("Enter the", i+1, "st Element:")
    item = input()
    list1.append(item)

print("Input List:", list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            print(list1)
        else:
            print(list1)
    print()

print("Sorted:",list1)
