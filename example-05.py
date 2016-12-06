from musical.theory import Note, Scale, Chord

# generate a random major key
root = Note('c')
scale = Scale(root, 'major')

# generate a I-V-vi-IV progression
progression = Chord.progression(Scale(root, (7, 2, -4, -5)), 3)
for chord in progression:
    print chord
