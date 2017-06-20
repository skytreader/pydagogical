CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NO_SHARPS = [note for note in CHROMATIC_SCALE if len(note) == 1]
INTERVAL_PATTERN = [2, 2, 1, 2, 2, 2, 1]

def construct_major_scale(unison_note):
    norm_note = unison_note.upper()
    note_index = CHROMATIC_SCALE.index(norm_note)
    major_scale = [norm_note]

    for step in INTERVAL_PATTERN:
        note_index = (note_index + step) % len(CHROMATIC_SCALE)
        major_scale.append(CHROMATIC_SCALE[note_index])

    return major_scale

def interval_quantity(note1, note2):
    plain_note1 = note1[0].upper()
    plain_note2 = note2[0].upper()
    index1 = NO_SHARPS.index(plain_note1)
    index2 = NO_SHARPS.index(plain_note2)
    return abs(index1 - index2) + 1
