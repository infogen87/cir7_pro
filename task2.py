def sum():
    numbers = []
    total = 0
    user_input = input("enter some digits ")
    for value in user_input:
        try:
            numbers.append(int(value))
        except ValueError:
            print("sorry only input digits!")
            break
    for val in numbers:
        total += val
    print(f"the total sum is {total}")


sum()