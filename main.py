##actual code//

food_bank = {  # dict with all foods : qty

}

all_foods = []  # list of all foods, for later in view()
all_qty = []  #


def main():
    print("Welcome to Loggr. Select an option from the list below: ")

    while True:
        print(" Log - logs new food  \n View - view all logs and quantities \n Help - details how to use Loggr")

        my_choice_1 = input(" $type...").lower()

        if my_choice_1 == "log":
            log()
        elif my_choice_1 == "view":
            view()
        elif my_choice_1 == "help":
            print("Help - Loggr is designed to remind you what you DO  and DO NOT  already have in your pantry.  \n")
        else:
            print("Entry not recognized")


def log():
    try:
        while True:
            food = input("Enter a food item that you'd like to log: \n"
                         "(enter 'q' at anytime to quit log) ").lower()
            if food == 'q':
                main()
                break

            qty = input(f"How much do you have left of {food}? Enter:  \n  "
                        f" 'none'  'little'  'average'   or   'full' or a number \n"
                        f"(enter 'q' at anytime to quit log) ").lower()
            if qty == None:
                log()

            print(f" {food} has been added to databse. Qnty: {qty}")
            all_foods.append(food)

            food_bank[food] = qty

            with open('dbase.txt', 'w+') as f:  # Opens file and writes food and qty:
                f.write("")
                for food in food_bank:
                    f.write(food + ", " + qty)
                    f.write('\n')

    except ValueError:
        "Invalid Response"


# def oepn_database():
# file = open('dbase.txt', 'a')

# for food in food_start:
#   file.write(food) #O Open database.txt file code

def view():
    # newvar = log()
    print(" View command provides a list of all food items matched with their quantities...")
    print(" Foods | Qty: ")
    # print(food_bank)

    with open('dbase.txt', 'r') as f:
        for line in f:
            # contents = f.read()
            print(line, end='')

    f.close()

    input2 = input("To view only your foods, type 'f' ")
    if input2 == 'f':
        print(all_foods)
        # return all_foods
    elif input2 == "log":
        log()
    else:
        print("Entry not allowed. ")
        main()


main()

# def open_write_db():

# file = open('dbase.txt', "r")
# content = file.read()

# print("content type: " + type(content).__name__ + "\n")

# for line in content:
#   print(line.strip())

# print(content)


# file.close()


# Menu Code / UX
