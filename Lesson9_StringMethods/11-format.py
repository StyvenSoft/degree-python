def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana"

def poem_title_card(poet, title):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc

print(poem_title_card("I Hear America Singing", "Walt Whitman"))