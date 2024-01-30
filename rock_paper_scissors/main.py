"""Rock Paper Scissors Lizard Spoc
An international Rock Paper Scissors Lizard Spock tournament is organized, all players receive a number when they register.

Each player chooses a sign that he will keep throughout the tournament among:
Rock (R)
Paper (P)
sCissors (C)
Lizard (L)
Spock (S)

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
and in case of a tie, the player with the lowest number wins (it's scandalous but it's the rule).

Example
4 R \
      1 P \
1 P /      \
             1 P
8 P \      /     \
      8 P /       \
3 R /              \
                     2 L
7 C \              /
      5 S \       /
5 S /      \     /
             2 L
6 L \      /
      2 L /
2 L /
The winner of the tournament is player 2. Before winning, he faced player 6, then player 5 and finally player 1.

Input
Line 1: an integer N representing the number of participants in the competition
Lines 2 to N+1: an integer NUMPLAYER indicating the player number (players have distinct numbers between 1 and N) followed by a letter 'R', 'P', 'C', 'L' or 'S' indicating the chosen sign SIGNPLAYER

Output
Line 1: the number of the winner
Line 2: the list of its opponents separated by spaces

Constraints
N is a 2^k value (2, 4, 8, 16, ..., 1024)
2 ≤ N ≤ 1024

https://www.codingame.com/ide/puzzle/rock-paper-scissors-lizard-spock

Author: Dominique Reese
"""

GAME_MAP = {
    'R': ['L', 'C'],
    'P': ['R', 'S'],
    'C': ['P', 'L'],
    'L': ['S', 'P'],
    'S': ['R', 'C']
}


def process_players(n):
    players = []
    for i in range(n):
        inputs = input().split()
        numplayer = int(inputs[0])
        signplayer = inputs[1]
        player = {
            "sign": signplayer,
            "number": numplayer,
            "matches": []
        }
        players.append(player)
    return players


def play(match):
    winner = None
    player_one = match[0]
    player_two = match[1]

    player_one["matches"].append(player_two["number"])
    player_two["matches"].append(player_one["number"])

    if player_one["sign"] == player_two["sign"]:
        winner = player_one if player_one["number"] < player_two["number"] else player_two
    else:
        player_one_sign_wins = player_two["sign"] in GAME_MAP[player_one["sign"]]
        winner = player_one if player_one_sign_wins else player_two

    return winner


def main():
    n = int(input())
    players = process_players(n)
    while len(players) > 1:
        matches = ((players[i], players[i+1])
                   for i in range(0, len(players), 2))
        winners = [play(match) for match in matches]
        players = winners
    winner = players[0]
    print(winner["number"])
    print(" ".join(map(str, winner["matches"])))


if __name__ == "__main__":
    main()
