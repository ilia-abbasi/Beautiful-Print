def simple_wrap(text : str, chars : str, add_spaces : bool = True) -> str:
    if add_spaces:
        text = " " + text + " "
    return chars + text + chars

def main() -> None :
    while True:
        print("Welcome to ~Beautiful Print~ !")
        print("==============================")
        print()
        print("1) Exit")
        print()
        print()
        choice = input("Your choice: ")

        if choice == "1":
            return
        
        print("\nInvalid choice!\n\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nYou 'Ctrl-C'ed out of this place!")
    except Exception as e:
        print(f"Something went wrong. Info on what happened: {e}")