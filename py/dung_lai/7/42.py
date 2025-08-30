# with open("data.txt","w") as file:
#     for i in range(5,0,-1):
#         file.write(f"{i}\n")

# with open("data.txt","r") as file:
#     for data in file:
#         print(data.strip())


user_input = int(input("Enter an integer: "))

with open("data.txt","w") as file:
    for i in range(user_input):
        file.write(str(user_input - i)+ "\n")


with open("data.txt","r") as file:
    numbers = file.read().split("\n")
    numbers.pop()
    print(numbers)

for i in range(len(numbers)):
    print(f"Line {i+1}: {numbers[i]}")