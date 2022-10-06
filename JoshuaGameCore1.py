#this runs its a shadow of the final product in which each game will actually open a simple version of that game 10-5-22
money = 50
shopping_cart = []
games = {"Solitaire": 5, "Checkers": 10, "Minesweeper": 20, "Backgammon": 25, "Go Fish": 30, "Chess": 35, "Global Thermonuclear War": 100}

while True:
    if money<=0:
        print("GAME OVER")
        break
    else:
            player_choice = input(f"Select a game{games}:").title()
            if player_choice in games:
                if money >= games[player_choice]:
                    shopping_cart.append(player_choice)
                    money -= games[player_choice]
                    print(f"Shopping cart: {shopping_cart} \nMoney left: {money}")
                else:
                    print("Interesting game...the only winning move is not to play.")
