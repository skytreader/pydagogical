from typing import Optional, Tuple

ScaleType = Tuple[str, str, str, str, str, str, str, str, str, str, str, str]
IntervalPatternType = Tuple[int, int, int, int, int, int, int]

CHROMATIC_SCALE: ScaleType = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")
NO_SHARPS: Tuple[str, ...] = tuple(note for note in CHROMATIC_SCALE if len(note) == 1)
INTERVAL_PATTERN: IntervalPatternType = (2, 2, 1, 2, 2, 2, 1)

INTERVAL_NAMES: Tuple[str, ...] = (
    "unison", "minor 2nd", "major 2nd", "minor 3rd", "major 3rd", "perfect 4th",
    "tritone", "perfect 5th", "minor 6th", "major 6th", "minor 7th", "major 7th",
    "octave"
)

def add_interval(note: str, interval_name: str) -> str:
    norm_name = interval_name.lower()
    norm_note = note.upper()
    add_offset = INTERVAL_NAMES.index(norm_name)
    new_note_index = (CHROMATIC_SCALE.index(norm_note) + add_offset) % len(CHROMATIC_SCALE)
    return CHROMATIC_SCALE[new_note_index]

def construct_major_scale(unison_note: str, interval_reps: int = 1) -> Tuple[str, ...]:
    norm_note = unison_note.upper()
    note_index = CHROMATIC_SCALE.index(norm_note)
    major_scale = [norm_note]

    for _ in range(interval_reps):
        for step in INTERVAL_PATTERN:
            note_index = (note_index + step) % len(CHROMATIC_SCALE)
            major_scale.append(CHROMATIC_SCALE[note_index])

    return tuple(major_scale)

def construct_natural_minor_scale(unison_note: str) -> Tuple[str, ...]:
    """
    AKA The Aeolian Mode.
    """
    major_scale = construct_major_scale(unison_note)
    minor_scale = list(major_scale[5:7])
    minor_scale.extend(major_scale[0:5])
    return tuple(minor_scale)

def construct_relative_minor_scale(unison_note: str) -> Tuple[str, ...]:
    """
    Alias for construct_natural_minor_scale.
    """
    return construct_natural_minor_scale(unison_note)

def norm_flat(note: str) -> str:
    if len(note) == 2 and note[1] == "b":
        norm_note = note[0].upper()
        note_index = CHROMATIC_SCALE.index(norm_note)
        return CHROMATIC_SCALE[note_index - 1]
    else:
        return note

def __normalize_note(note: str) -> str:
    return norm_flat(note) if len(note) == 2 and note[1] == "b" else note.upper()

def flatten_note(note: str) -> str:
    normalized = __normalize_note(note)
    return CHROMATIC_SCALE[CHROMATIC_SCALE.index(normalized) - 1]

def interval_quality(note1: str, note2: str) -> str:
    # FIXME This assumes it won't be fed flats.
    # TODO Work this in terms of minor and major intervals.
    norm_note1 = __normalize_note(note1)
    norm_note2 = __normalize_note(note2)
    index1 = CHROMATIC_SCALE.index(norm_note1)
    index2 = CHROMATIC_SCALE.index(norm_note2)

    if index2 >= index1:
        quality = index2 - index1
    else:
        index2 += len(CHROMATIC_SCALE)
        quality = index2 - index1
    
    return INTERVAL_NAMES[quality]

def interval_quantity(note1: str, note2: str) -> int:
    # TODO Work this in terms of minor and major intervals.
    plain_note1 = note1[0].upper()
    plain_note2 = note2[0].upper()
    index1 = NO_SHARPS.index(plain_note1)
    index2 = NO_SHARPS.index(plain_note2)

    if index2 >= index1:
        return index2 - index1 + 1
    else:
        index2 += len(NO_SHARPS)
        return index2 - index1 + 1

def get_major_chord(note: str) -> Tuple[str, str, str]:
    major_scale = construct_major_scale(note)
    return (major_scale[0], major_scale[2], major_scale[4])

def get_minor_chord(note: str) -> Tuple[str, str, str]:
    major_chord = get_major_chord(note)
    return (major_chord[0], flatten_note(major_chord[1]), major_chord[2])

def determine_chord(n1: str, n2: str, n3: str) -> Optional[str]:
    note_tuple = (__normalize_note(n) for n in (n1, n2, n3))
    note_set = set(note_tuple)
    for note in note_tuple:
        if set(get_major_chord(note)) == note_set:
            return "%s major" % note
        elif set(get_minor_chord(note)) == note_set:
            return "%s minor" % note

    return None
