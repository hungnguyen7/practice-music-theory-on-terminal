import random
from termcolor import colored
import time
from constants import NOTES_ON_SHEET, POSITION_MAP, SECTION_BREAK
from utils import pretty_time, display_note_reminders


# * Define a template for an empty staff
def create_empty_staff():
    return [
        " _______ ",  # * Line 5 (Top line)
        "|       |",  # * Space 4
        "|_______|",  # * Line 4
        "|       |",  # * Space 3
        "|_______|",  # * Line 3 (Middle line)
        "|       |",  # * Space 2
        "|_______|",  # * Line 2
        "|       |",  # * Space 1
        "|_______|"   # * Line 1 (Bottom line)
    ]


def place_notes_on_staff(staff):
    """Place all notes on the staff."""
    for note in NOTES_ON_SHEET:
        pos = POSITION_MAP[(note["on"], note["position"])]
        staff[pos] = staff[pos][:4] + "♪" + \
            staff[pos][5:]  # * Replace with whole note '♪'


def hide_random_note(staff):
    """Randomly hide a note on the staff."""
    hidden_note_index = random.randint(0, len(NOTES_ON_SHEET) - 1)
    hidden_note = NOTES_ON_SHEET[hidden_note_index]

    pos = POSITION_MAP[(hidden_note["on"], hidden_note["position"])]
    staff[pos] = staff[pos][:4] + " " + \
        staff[pos][5:]  # * Remove the note representation
    return hidden_note


def sheet_music_practice():
    print("Welcome to Sheet Music Practice 🎼🎵🎶!")
    display_note_reminders()
    while True:
        staff = create_empty_staff()  # * Reset the staff for each round
        place_notes_on_staff(staff)    # * Place notes on the staff

        hidden_note = hide_random_note(staff)  # * Hide a note

        start = time.time()
        print("Identify the hidden note on the staff:")
        for line in staff:
            print(line)

        user_answer = ""
        while user_answer != hidden_note["note"]:
            user_answer = input(
                "What note is hidden? (E, F, G, A, B, C, D): ").strip().upper()

            if user_answer == hidden_note["note"]:
                print(
                    f"Correct! The hidden note is {colored(user_answer, 'green')}")
            else:
                print("Incorrect. Try again.")
        end = time.time()

        print(f"Time taken: {pretty_time(end - start)}")
        print(SECTION_BREAK)
