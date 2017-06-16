CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
INTERVAL_PATTERN = [2, 2, 1, 2, 2, 2, 1]

def construct_major_scale(unison_note):
    norm_note = unison_note.upper()
    note_index = CHROMATIC_SCALE.index(norm_note)
    major_scale = [norm_note]

    for step in INTERVAL_PATTERN:
        note_index = (note_index + step) % len(CHROMATIC_SCALE)
        major_scale.append(CHROMATIC_SCALE[note_index])

    return major_scale
