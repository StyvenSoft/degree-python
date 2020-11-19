def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("Hello There!")

print(the_scream, the_whisper)

# HELLO THERE! hello there!