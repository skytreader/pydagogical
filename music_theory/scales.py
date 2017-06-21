CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NO_SHARPS = [note for note in CHROMATIC_SCALE if len(note) == 1]
INTERVAL_PATTERN = [2, 2, 1, 2, 2, 2, 1]

INTERVAL_NAMES = [
    "unison", "minor 2nd", "major 2nd", "minor 3rd", "major 3rd", "perfect 4th",
    "tritone", "perfect 5th", "minor 6th", "major 6th", "minor 7th", "major 7th",
    "octave"
]

def add_interval(note, interval_name):
    norm_name = interval_name.lower()
    norm_note = note.upper()
    add_offset = INTERVAL_NAMES.index(norm_name)
    new_note_index = (CHROMATIC_SCALE.index(norm_note) + add_offset) % len(CHROMATIC_SCALE)
    return CHROMATIC_SCALE[new_note_index]

def construct_major_scale(unison_note):
    norm_note = unison_note.upper()
    note_index = CHROMATIC_SCALE.index(norm_note)
    major_scale = [norm_note]

    for step in INTERVAL_PATTERN:
        note_index = (note_index + step) % len(CHROMATIC_SCALE)
        major_scale.append(CHROMATIC_SCALE[note_index])

    return major_scale

def eval_flat(note):
    if len(note) == 2 and note[1] == "b":
        norm_note = note[0].upper()
        note_index = CHROMATIC_SCALE.index(norm_note)
        return CHROMATIC_SCALE[note_index - 1]
    else:
        raise ValueError("Call only on flat-notated notes.")

def interval_quality(note1, note2):
    # FIXME This assumes it won't be fed flats.
    # TODO Work this in terms of minor and major intervals.
    norm_note1 = note1.upper()
    norm_note2 = note2.upper()
    index1 = CHROMATIC_SCALE.index(norm_note1)
    index2 = CHROMATIC_SCALE.index(norm_note2)

    if index2 >= index1:
        return index2 - index1 + 1
    else:
        index2 += len(CHROMATIC_SCALE)
        return index2 - index1 + 1

def interval_quantity(note1, note2):
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
