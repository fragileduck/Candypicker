# last updated 1/15/2024

def main():
  print("Welcome to the Candy Store!")

  print("Choose your number my candy Queen.:")

  while True:
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
      print("You picked Junior Mints. Enjoy your candy!")
      break
    elif choice == '2':
      print("You picked Gum Drops. NOT THE GUMDROP BUTTONS!")
      break
    elif choice == '3':
      print("You picked Cow Tails. Enjoy your candy!")
      break
    elif choice == '4':
      print("You picked Reeses. Enjoy your candy!")
      break
    elif choice == '5':
      print("You picked Ice Cream. Enjoy frozen milk and sugar!")
      break
    elif choice == '6':
      print("You picked peanut M&M's. Enjoy your candy!")
      break
    elif choice == '7':
      print("you picked Donuts. Enjoy your Donuts!")
    else:
      print("Invalid choice.")


if __name__ == "__main__":
  main()
