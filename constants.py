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

NOTES_ON_SHEET = [
    {"note": "A", "on": "line", "position": -2},
    {"note": "B", "on": "space", "position": -2},
    {"note": "C", "on": "line", "position": -1},
    {"note": "D", "on": "space", "position": -1},
    {"note": "E", "on": "line", "position": 0},
    {"note": "F", "on": "space", "position": 0},
    {"note": "G", "on": "line", "position": 1},
    {"note": "A", "on": "space", "position": 1},
    {"note": "B", "on": "line", "position": 2},
    {"note": "C", "on": "space", "position": 2},
    {"note": "D", "on": "line", "position": 3},
    {"note": "E", "on": "space", "position": 3},
    {"note": "F", "on": "line", "position": 4},
    {"note": "G", "on": "space", "position": 4},
    {"note": "A", "on": "line", "position": 5},
]

# Map positions to the index in the staff
POSITION_MAP = {
    ("line", -2): 14,
    ("space", -2): 13,
    ("line", -1): 12,
    ("space", -1): 11,
    ("line", 0): 10,
    ("space", 0): 9,
    ("line", 1): 8,
    ("space", 1): 7,
    ("line", 2): 6,
    ("space", 2): 5,
    ("line", 3): 4,
    ("space", 3): 3,
    ("line", 4): 2,
    ("space", 4): 1,
    ("line", 5): 0,
}

GUITAR_FRETS = 12

NUMBER_OF_GUITAR_STRINGS = 6

SECTION_BREAK = "-" * 65

EXTRA_LINE = "┆"
TAB_LINE = "|"
TAB_CORNER = {
    "TOP_LEFT": "┍",
    "TOP_RIGHT": "┑",
    "BOTTOM_LEFT": "┕",
    "BOTTOM_RIGHT": "┙"
}
STAFF_LINE = "......."
STAFF_SPACE = "       "
SYMBOL_FOR_NOTE = "♪"
UNKNOWN_NOTE = "?"
