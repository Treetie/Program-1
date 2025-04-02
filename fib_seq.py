#the sequence that will get printed
sequence = [0]

#sequence calculator
def calculate():
    total_numbers = items[1]
    place = 2
    if total_numbers > 1:
        sequence.append(1)
        while place != total_numbers:
            sequence.append(sequence[-1] + sequence[-2])
            place += 1
    print(sequence)

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
                #splits inputs into separate items in a list
                items = input1.split(" ")
                #switches numbers to ints
                for item in items:
                    if item.isnumeric():
                        items.remove(item)
                        items.insert(1, int(item))
                        #checks for --last-only
                calculate()
                if "--last-only" in input1:
                    print("h")

            else:
                print("Invalid format.")

        elif input1.startswith("-c"):
            if input1[3].isdigit():
                print("yay")



            