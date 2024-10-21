from termcolor import colored
import random
import time
from constants import GUITAR_NOTES, NOTE_COLORS, GUITAR_FRETS, NUMBER_OF_GUITAR_STRINGS, SECTION_BREAK


def color_note(note):
    """Return the note colored based on its value."""
    padded_note = note.ljust(2)
    color = NOTE_COLORS.get(note.strip())
    return colored(padded_note, color)


def print_fret_numbers():
    """Print the fret numbers with frets 5, 7, and 9 colored red."""
    frets = []

    # * Loop through fret numbers 1 to 12
    for i in range(1, 13):
        if i in [5, 7, 9]:
            # * Frets 5, 7, and 9 are colored red
            frets.append(colored(str(i).rjust(2), "red", "on_blue"))
        else:
            # * Standard white on blue color for other frets
            frets.append(colored(str(i).rjust(2), "white", "on_blue"))

    # * Join the frets into a line with separators, colored white on blue
    fret_line = colored(" | ", "white", "on_blue").join(frets)

    print(colored("Fret |", "black", "on_light_magenta") + " " + fret_line)


def display_notes_on_strings(hidden_notes):
    """Display the guitar notes, hiding specific ones based on the hidden notes list."""
    print_fret_numbers()
    for string, notes in GUITAR_NOTES.items():
        colored_notes = [
            "__" if (string, idx) in hidden_notes else color_note(note)
            for idx, note in enumerate(notes)
        ]
        print(colored(f"Str {string}|", "black",
              "on_light_magenta") + " " + ' | '.join(colored_notes[1:]))
    print_fret_numbers()
    print()


def guess_notes(hidden_notes):
    """Prompt the user to guess the hidden notes and provide feedback."""
    correct_count = 0
    guessed_notes = set()

    total_questions = len(hidden_notes)

    for question_number, (string, idx) in enumerate(hidden_notes, start=1):
        print(
            f"######################### *Question {question_number} of {total_questions}* #########################")

        # * Display only the remaining hidden notes that haven't been guessed
        remaining_hidden_notes = [(s, i) for (
            s, i) in hidden_notes if (s, i) not in guessed_notes]
        display_notes_on_strings(remaining_hidden_notes)

        user_input = input(
            f"Guess the note for string {string}, fret {idx}: ").strip().upper()
        correct_note = GUITAR_NOTES[string][idx]

        if user_input == correct_note:
            print(colored(f"Correct! It's {correct_note}.", "green"))
            correct_count += 1
        else:
            print(
                colored(f"Wrong! The correct note was {correct_note}.", "red"))

        guessed_notes.add((string, idx))
        print(SECTION_BREAK)

    # * Return the number of correct and wrong answers
    return correct_count, total_questions - correct_count


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
        total_notes = NUMBER_OF_GUITAR_STRINGS * GUITAR_FRETS
        if num_hidden > total_notes:
            print(colored(
                f"There are only {total_notes} notes on the guitar. Please try again.", "red"))
        else:
            return num_hidden
    except ValueError:
        print("Please enter a valid number.")


def generate_hidden_notes(num_hidden):
    """Generate unique random hidden notes based on the number specified."""
    # * Generate all possible notes (1-6 for the first value, 1-12 for the second)
    all_notes = [(x, y) for x in range(1, 7) for y in range(1, 13)]

    random.shuffle(all_notes)

    return all_notes[:num_hidden]


def pretty_time(seconds):
    """Format the time taken in seconds to a human-readable format."""
    minutes, seconds = divmod(seconds, 60)
    return f"{colored(int(minutes), 'green')} minutes and {colored(round(seconds, 2), 'green')} seconds"


def main():
    """Main function to run the guitar note guessing game."""
    print("Welcome to Guitar Note Practice 🎼🎵🎶🎸!")
    display_note_reminders()

    while True:
        num_hidden = get_number_of_hidden_notes()
        if not num_hidden:
            continue
        hidden_notes = generate_hidden_notes(num_hidden)

        start = time.time()
        correct_notes, wrong_notes = guess_notes(hidden_notes)
        end = time.time()
        print(
            f"You got {colored(correct_notes, 'green')} correct notes and {colored(wrong_notes, 'red')} wrong notes.")
        print(f"Time taken: {pretty_time(end - start)}")
        print(SECTION_BREAK)
        print("Practice makes perfect! Let's try again.")


if __name__ == "__main__":
    main()
