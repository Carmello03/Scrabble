letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters: points for letters, points in zip(letters, points)}
letter_to_points[" "] = 0


def main():
    play_again = "y"
    print("Hi welcome to Scrabble")
    player = players()
    while play_again == "y":
        word_choice = word()
        play_word(player, word_choice)
        while True:
            play_again = input("Would you like to play again? (y/n)")
            if play_again in ["y", "n"]:
                break
    print("Thanks for playing")
    update_point_totals()
    print(player_to_words)


def score_word(word1):
    point_total = 0
    for letter in word1:
        point_total += letter_to_points.get(letter, 0)
    return point_total


def play_word(player, word2):
    player_to_words[player].append(word2)


player_to_words = {"player1": ["BLUE"], "player2": ["BLUE"],
                   "player3": ["BLUE"], "player4": ["BLUE"]}
player_to_points = {}


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for w in words:
            player_points += score_word(w)
        player_to_words[player] = player_points


def players():
    player_input = int(input("Please choose your player \n -> 1\n -> 2\n -> 3\n -> 4\n ---> "))
    if player_input == 1:
        return "player1"
    elif player_input == 2:
        return "player2"
    elif player_input == 3:
        return "player3"
    elif player_input == 4:
        return "player4"


def word():
    word_input = input("Enter a word: ")
    return word_input


main()
