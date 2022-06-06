from .scales import CHROMATIC_SCALE

def construct_fretting(tuning: str, fret_limit: int = 12):
    """
    `tuning` is a string describing the notes sounded by the guitar string when
    played in open. No length restrictions are imposed because, hey, whatever
    set-up floats your guitar. :)
    """
    fretting = []

    for open_note in tuning:
        string = []
        open_norm = open_note.upper()
        initial_index = CHROMATIC_SCALE.index(open_norm)

        for i in range(fret_limit + 1):
            string.append(CHROMATIC_SCALE[(initial_index + i) % len(CHROMATIC_SCALE)])

        fretting.append(string)

    return fretting
