from termcolor import colored
import random

# Each note is associated with different colors
NOTE_COLORS = {
    "E": "black",
    "F": "magenta",
    "F#": "light_magenta",
    "G": "red",
    "G#": "light_red",
    "A": "green",
    "A#": "light_green",
    "C": "yellow",
    "C#": "light_yellow",
    "D": "blue",
    "D#": "light_blue",
    "B": "white",
}

GUITAR_NOTES = {
    6: ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
    5: ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"],
    4: ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"],
    3: ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"],
    2: ["B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    1: ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"]
}

GUITAR_FRETS = 12


def color_note(note):
    """Return the note colored based on its value."""
    padded_note = note.ljust(2)
    color = NOTE_COLORS.get(note.strip())
    return colored(padded_note, color)


def print_fret_numbers():
    """Print the fret numbers with frets 5, 7, and 9 colored red."""
    frets = []

    # Loop through fret numbers 1 to 12
    for i in range(1, 13):
        if i in [5, 7, 9]:
            # Frets 5, 7, and 9 are colored red
            frets.append(colored(str(i).rjust(2), "red", "on_blue"))
        else:
            # Standard white on blue color for other frets
            frets.append(colored(str(i).rjust(2), "white", "on_blue"))

    # Join the frets into a line with separators, colored white on blue
    fret_line = colored(" | ", "white", "on_blue").join(frets)

    print(colored("Fret |", "black", "on_light_magenta") + " " + fret_line)


def display_notes_on_strings(guitar_strings, hidden_notes):
    """Display the guitar notes, hiding specific ones based on the hidden notes list."""
    print_fret_numbers()
    for string, notes in guitar_strings.items():
        colored_notes = [
            "__" if (string, idx) in hidden_notes else color_note(note)
            for idx, note in enumerate(notes)
        ]
        print(colored(f"Str {string}|", "black", "on_light_magenta") + " " + ' | '.join(colored_notes[1:]))
    print_fret_numbers()
    print()


def guess_notes(hidden_notes, guitar_strings):
    """Prompt the user to guess the hidden notes and provide feedback."""
    correct_notes = 0
    wrong_notes = 0
    for string, idx in hidden_notes:
        print(f"######################### *Question {correct_notes + wrong_notes + 1}* #########################")
        display_notes_on_strings(guitar_strings, hidden_notes)
        user_input = input(f"Guess the note for string {string}, fret {idx}: ").strip().upper()
        correct_note = guitar_strings[string][idx]
        if user_input == correct_note:
            print(colored(f"Correct! It's {correct_note}.", "green"))
            correct_notes += 1
        else:
            print(colored(f"Wrong! The correct note was {correct_note}.", "red"))
            wrong_notes += 1
        print("-" * 65)

    return correct_notes, wrong_notes


def display_note_reminders():
    """Display the note names to remind the user."""
    print("Let's remember all the basic notes first:")
    for note in ["C", "D", "E", "F", "G", "A", "B"]:
        print(color_note(note), end=" ")
    print()


def get_number_of_hidden_notes():
    """Get the number of hidden notes from the user."""
    try:
        num_hidden = int(input("How many notes would you like to guess? "))
        if num_hidden > 72:
            print("There are only 72 notes on the guitar. Please try again.")
        else:
            return num_hidden
    except ValueError:
        print("Please enter a valid number.")


def generate_hidden_notes(num_hidden):
    """Generate unique random hidden notes based on the number specified."""
    unique_notes = set()

    while len(unique_notes) < num_hidden:
        note = (random.randint(1, 6), random.randint(1, 12))  # Randomly generate a note
        unique_notes.add(note)  # Add to set, duplicates are ignored

    return list(unique_notes)  # Convert the set back to a list


def main():
    """Main function to run the guitar note guessing game."""
    print("Welcome to Guitar Note Practice 🎼🎵🎶🎸!")
    display_note_reminders()

    while True:
        num_hidden = get_number_of_hidden_notes()
        hidden_notes = generate_hidden_notes(num_hidden)
        correct_notes, wrong_notes = guess_notes(hidden_notes, GUITAR_NOTES)
        print(f"You got {colored(correct_notes, 'green')} correct notes and {colored(wrong_notes, 'red')} wrong notes.")
        print("Practice makes perfect! Let's try again.")


if __name__ == "__main__":
    main()
