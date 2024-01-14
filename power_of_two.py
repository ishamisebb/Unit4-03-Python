# created by me on december 12 2024

def main():
    try:
        #input
        counter = 0
        user_number = int(input("please enter positive integer:"))
        print("")
        #calculate power
        for counter in range(user_number + 1):
         power_of_two = counter ** 2
         print("{}^2 = {}".format(counter,power_of_two))

    except ValueError:
        print("invalid input enter positive number")
   
        
if __name__ == "__main__":
    main()