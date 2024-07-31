from sortedcontainers import SortedDict

def main():
    rbt = SortedDict()

    while True:
        print("Enter a number to insert into the Red-Black Tree (or 'q' to quit):")
        user_input = input()
        if user_input == 'q':
            break
        try:
            value = int(user_input)
            rbt[value] = None
            print("Red-Black Tree:")
            for key in rbt.keys():
                print(key)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

if __name__ == "__main__":
   main()
