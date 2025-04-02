import requests
response = requests.get("http://localhost:8080/api/fibonaci/")
print(response.status_code)

#the fib sequence
sequence = [0]
#placeholder
items = []

#sequence calculator (WORKS! :D)
def calculate():
    global items
    total_numbers = items[1]
    place = 2
    if total_numbers > 1:
        sequence.append(1)
        while place != total_numbers:
            sequence.append(sequence[-1] + sequence[-2])
            place += 1

#checks for each specific command and reacts accordingly
def commands():
    global items
    items = input1.split(" ")
    #switches numbers in list to ints
    for item in items:
        if item.isnumeric():
            items.remove(item)
            items.insert(1, int(item))
    calculate()

    #checks for numbering cmd
    if " --numbering" in input1:
        place = 1
        for number in sequence:
            sequence[place - 1] = f"{place}:{number}"
            place += 1

    #prints last digit only
    if "--last-only" in input1:
        print('"{\n  sequence:"', f'"{sequence[-1]}"', "\n }")
    
    #checks for oneline cmd
    elif "--one-line" in input1:
        string = ""
        for each in (sequence):
            string += f"{str(each)}, "
        #prints without last space or comma
        print(string[:-2])

    #prints normally (\n)
    else:
        for num in sequence:
            print('"{\n  sequence:"', f'"{sequence[-1]}"', "\n }")

#invalid format message
def invalid():
    print("Invalid formatting.")

#main loop
while True:
    #starting input
    input1 = input("./Fibonacci-gen ")
    #help command
    if input1 == "--help":
        print("--count|-c: Calculate to (c) places.\n--one-line: Print all the numbers on one line, separated by commas.\n--numbering: Prefaces each number in the sequence with it's placement.\n--last-only: Only prints the last number in the sequence.")
    #generator
    else:
        #makes sure input is correct for count
        if input1.startswith("--count"):
            if input1[8].isdigit():
                commands()
                break
            else:
                invalid()
                break

        #checks for -c instead of count
        elif input1.startswith("-c"):
            if input1[3].isdigit():
                commands()
                break
            else:
                invalid()
                break
        #if it doesn't start with those, it ends the program    
        else:
            invalid()
            break