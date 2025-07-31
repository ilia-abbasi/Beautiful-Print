def main() -> None :
    print("Welcome to ~Beautiful Print~ !")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something went wrong. Info on what happened: {e}")