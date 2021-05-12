num_1 = int(input("Please enter a number: "))
k = 2

while k < num_1:
    if num_1%k == 0:
        print(f"{num_1} is not a prime number")
        break
    else:
        k += 1
        
if k == num_1:
    print(f"{num_1} is a prime number")              
