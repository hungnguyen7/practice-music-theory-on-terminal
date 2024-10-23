import random
from termcolor import colored
import time
from constants import NOTES_ON_SHEET, POSITION_MAP, SECTION_BREAK, TAB_CORNER, TAB_LINE, STAFF_LINE, STAFF_SPACE, EXTRA_LINE, SYMBOL_FOR_NOTE, UNKNOWN_NOTE
from utils import pretty_time, display_note_reminders
import sys


def create_empty_staff():
    """Create an empty staff."""
    return [
        f"{EXTRA_LINE}{STAFF_LINE}{EXTRA_LINE}",
        f"{EXTRA_LINE}{STAFF_SPACE}{EXTRA_LINE}",
        # * Top of the musical tablature, above are the extra lines
        f"{TAB_CORNER['TOP_LEFT']}{STAFF_LINE}{TAB_CORNER['TOP_RIGHT']}",
        f"{TAB_LINE}{STAFF_SPACE}{TAB_LINE}",
        f"{TAB_LINE}{STAFF_LINE}{TAB_LINE}",
        f"{TAB_LINE}{STAFF_SPACE}{TAB_LINE}",
        f"{TAB_LINE}{STAFF_LINE}{TAB_LINE}",
        f"{TAB_LINE}{STAFF_SPACE}{TAB_LINE}",
        f"{TAB_LINE}{STAFF_LINE}{TAB_LINE}",
        f"{TAB_LINE}{STAFF_SPACE}{TAB_LINE}",
        f"{TAB_CORNER['BOTTOM_LEFT']}{STAFF_LINE}{TAB_CORNER['BOTTOM_RIGHT']}",
        # * Bottom of musical tablature, below are the extra lines
        f"{EXTRA_LINE}{STAFF_SPACE}{EXTRA_LINE}",
        f"{EXTRA_LINE}{STAFF_LINE}{EXTRA_LINE}",
        f"{EXTRA_LINE}{STAFF_SPACE}{EXTRA_LINE}",
        f"{EXTRA_LINE}{STAFF_LINE}{EXTRA_LINE}",
    ]


def place_notes_on_staff(staff):
    """Place all notes on the staff."""
    for note in NOTES_ON_SHEET:
        pos = POSITION_MAP[(note["on"], note["position"])]
        # * Replace the space with the note representation
        staff[pos] = staff[pos][:4] + SYMBOL_FOR_NOTE + \
            staff[pos][5:]


def hide_random_note(staff):
    """Randomly hide a note on the staff."""
    hidden_note_index = random.randint(0, len(NOTES_ON_SHEET) - 1)
    hidden_note = NOTES_ON_SHEET[hidden_note_index]

    pos = POSITION_MAP[(hidden_note["on"], hidden_note["position"])]
    staff[pos] = staff[pos][:4] + UNKNOWN_NOTE + \
        staff[pos][5:]  # * Remove the note representation
    return hidden_note


def pretty_staff(staff):
    """Pretty print the staff."""
    for line in staff:
        if EXTRA_LINE in line:
            if UNKNOWN_NOTE in line:
                # * Print the question mark in red, and the rest in blue
                question_mark_index = line.index(UNKNOWN_NOTE)
                pre_question_mark = colored(line[:question_mark_index], "blue")
                post_question_mark = colored(
                    line[question_mark_index + 1:], "blue")
                colored_question = colored(UNKNOWN_NOTE, "green")
                print(pre_question_mark + colored_question + post_question_mark)
            else:
                print(colored(line, "blue"))
        elif UNKNOWN_NOTE in line:
            print(line.replace(UNKNOWN_NOTE, colored(UNKNOWN_NOTE, "green")))
        else:
            print(line)


def practice_identifying_hidden_note(staff, hidden_note):
    """Practice identifying the hidden note."""
    print("Identify the hidden note on the staff:")
    pretty_staff(staff)

    user_answer = ""
    start_time = time.time()

    while user_answer != hidden_note["note"]:
        user_answer = input(
            "What note is hidden? (E, F, G, A, B, C, D): ").strip().upper()

        if user_answer == hidden_note["note"]:
            print(
                f"Correct! The hidden note is {colored(user_answer, 'green')}")
        else:
            print(
                colored("Incorrect! Try again.", "red"))

    end_time = time.time()
    return end_time - start_time


def sheet_music_practice():
    """Main function to practice sheet music."""
    print("Welcome to Sheet Music Practice 🎼🎵🎶!")
    display_note_reminders()

    time_records = []

    while True:
        try:
            staff = create_empty_staff()  # Reset the staff for each round

            place_notes_on_staff(staff)    # Place notes on the staff
            hidden_note = hide_random_note(staff)  # Hide a note

            time_taken = practice_identifying_hidden_note(staff, hidden_note)

            time_records.append(time_taken)
            print(f"Time taken: {pretty_time(time_taken)}")
            print(SECTION_BREAK)
        except KeyboardInterrupt:
            if time_records:
                print(
                    f"\nAverage time taken: {pretty_time(sum(time_records) / len(time_records))}")
            print("\nHope you had fun practicing sheet music! Goodbye! 😊")
            sys.exit(0)
