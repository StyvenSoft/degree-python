letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: value
    for key, value in zip(letters, points)
}

letter_to_points[" "] = 0

print(letter_to_points)

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

brownie_points = score_word("BROWNIE")
print("Total ", brownie_points)

# {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}
# Total 15

# player1	wordNerd	Lexi Con	Prof Reader
###############################################
# BLUE	    EARTH	    ERASER	    ZAP
# TENNIS	EYES	    BELLY	    COMA
# EXIT  	MACHINE	    HUSKY	    PERIOD


player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}

def update_points_total():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

update_points_total()
print(player_to_points)

def play_word(player, word):
    player_to_words[player].append(word)
    update_points_total()

play_word("player1", "CODE")
print(player_to_words)
print(player_to_points)

# {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}
# {'player1': ['BLUE', 'TENNIS', 'EXIT', 'CODE'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
# {'player1': 36, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}