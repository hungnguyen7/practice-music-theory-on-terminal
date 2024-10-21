from guitar_note_practice import guitar_note_practice
from sheet_music_practice import sheet_music_practice


def main():
    print("Welcome to the Music Practice App!")
    options = [
        "Guitar Note Practice 🎸",
        "Sheet Music Practice 🎼",
    ]

    actions = [
        guitar_note_practice,
        sheet_music_practice,
    ]

    print("Please choose an option:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Enter the number of your choice: ")

    if choice.isdigit() and 1 <= int(choice) <= len(actions):
        actions[int(choice) - 1]()

    else:
        print("Invalid choice. Please try again.")
        main()


if __name__ == "__main__":
    main()
