from termcolor import colored

# Each note is associated with different color
note_colors = {
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

guitar_notes_on_string = {
    6: ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
    5: ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"],
    4: ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"],
    3: ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"],
    2: ["B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    1: ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"]
}

def color_note(note):
    # Pad the note to be 2 characters before applying color
    padded_note = note.ljust(2)
    color = note_colors.get(note.strip())
    return colored(padded_note, color)

def draw_guitar_strings(guitar_strings):
    for string, notes in guitar_strings.items():
        colored_notes = [color_note(note) for note in notes]
        print(f"Str {string}: " + ' | '.join(colored_notes[1:]))

if __name__ == "__main__":
    draw_guitar_strings(guitar_notes_on_string)
