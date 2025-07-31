def simple_wrap(text : str, chars : str, include_spaces : bool = False) -> str:
    result = ""

    if include_spaces:
        text = " " + text + " "
    
    result = chars + text + chars
    
    if include_spaces:
        result = " " + result + " "

    return result

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