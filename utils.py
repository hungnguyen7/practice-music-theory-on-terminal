from termcolor import colored
from constants import NOTE_COLORS


def pretty_time(seconds):
    """Format the time taken in seconds to a human-readable format."""
    minutes, seconds = divmod(seconds, 60)
    return f"{colored(int(minutes), 'green')} minutes and {colored(round(seconds, 2), 'green')} seconds"


def display_note_reminders():
    """Display the note names to remind the user."""
    print("Let's remember all the basic notes first:")
    for note in ["C", "D", "E", "F", "G", "A", "B"]:
        print(color_note(note), end=" ")
    print()


def color_note(note):
    """Return the note colored based on its value."""
    padded_note = note.ljust(2)
    color = NOTE_COLORS.get(note.strip())
    return colored(padded_note, color)
