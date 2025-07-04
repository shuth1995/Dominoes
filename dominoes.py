import random
from collections import Counter

# Generate a full set of unique dominos (28 pieces, each combination without duplicates)
def generate_unique_dominos():
    return [[x, y] for x in range(7) for y in range(x, 7)]

# Shuffle and allocate dominos to stock, player, and computer ensuring at least one double in player or computer hand
def allocate_dominos(unique_dominos):
    while True:
        random.shuffle(unique_dominos)
        stock, player, computer = unique_dominos[:14], unique_dominos[14:21], unique_dominos[21:28]
        doubles_player = find_doubles(player)
        doubles_computer = find_doubles(computer)
        if doubles_player or doubles_computer:
            return stock, player, computer, doubles_player, doubles_computer

# Find and return sorted list of doubles (pieces with identical numbers) from a set of dominos
def find_doubles(pieces):
    return sorted([piece for piece in pieces if piece[0] == piece[1]], reverse=True)

# Print the current game state: sizes of stock and computer pieces, domino snake, player's hand, and current status
def print_game_state(stock, player, computer, domino_snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")  # Number of dominos left in stock
    print(f"Computer pieces: {len(computer)}\n")  # Number of dominos in computer's hand
    display_domino_snake(domino_snake)  # Show the current domino snake on the board
    print("\nYour pieces:")
    for index, value in enumerate(player):
        print(f"{index + 1}:{value}")  # List player's dominos with numbering
    print("")

    # Display appropriate status message based on whose turn or game outcome
    if status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
    elif status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    elif status == "draw":
        print("Status: The game is over. It's a draw!")
    elif status == "player_won":
        print("Status: The game is over. You won!")
    elif status == "computer_won":
        print("Status: The game is over. The computer won!")

# Display the domino snake on the board, truncating middle if too long for readability
def display_domino_snake(domino_snake):
    if len(domino_snake) > 6:
        # Show first 3 and last 3 pieces with ellipsis in between
        start = ''.join(str(piece) for piece in domino_snake[:3])
        end = ''.join(str(piece) for piece in domino_snake[-3:])
        print(f"{start}...{end}")
    else:
        # Show entire snake if short enough
        print(''.join(str(piece) for piece in domino_snake))

# Check the current game status to determine if there's a winner, draw, or game continues
def check_game_status(domino_snake, player, computer, stock):
    # Flatten all numbers at both ends of the domino snake to count occurrences
    flat_numbers = [num for piece in domino_snake for num in piece]
    counts = Counter(flat_numbers)

    # Condition 1: Draw if any number appears 8 times and the ends of the snake have the same number
    if any(count == 8 for count in counts.values()) and domino_snake[0][0] == domino_snake[-1][1]:
        return "draw"

    # Condition 2: Player or computer wins if they have no dominos left
    if not player:
        return "player_won"
    if not computer:
        return "computer_won"

    # Condition 3: Check if both players cannot move and no dominos left in stock -> draw
    left_end = domino_snake[0][0]
    right_end = domino_snake[-1][1]
    player_can_move = any(left_end in d or right_end in d for d in player)
    computer_can_move = any(left_end in d or right_end in d for d in computer)

    if not player_can_move and not computer_can_move and not stock:
        return "draw"

    # No end condition met, game continues
    return None

# Handle the player's turn: input move, validate, rotate domino if needed, or draw from stock
def player_turn(player, domino_snake, stock):
    left_end = domino_snake[0][0]   # Number on left end of snake
    right_end = domino_snake[-1][1] # Number on right end of snake

    while True:
        try:
            user_turn = int(input())  # Read player's move input
            if user_turn == 0:
                # Player chooses to draw from stock if available
                if stock:
                    player.append(stock.pop(random.randint(0, len(stock) - 1)))
                break
            elif -len(player) <= user_turn <= len(player):
                index = abs(user_turn) - 1
                chosen_domino = player[index]

                if user_turn < 0:
                    # Player wants to place domino on left side of snake
                    if left_end in chosen_domino:
                        # Rotate domino if its second number matches left end, so first number aligns
                        if chosen_domino[1] == left_end:
                            domino_snake.insert(0, chosen_domino)
                        else:
                            # Flip domino to align left end correctly
                            chosen_domino = [chosen_domino[1], chosen_domino[0]]
                            domino_snake.insert(0, chosen_domino)
                        player.pop(index)  # Remove placed domino from player's hand
                        break
                    else:
                        print("Illegal move. Please try again.")
                elif user_turn > 0:
                    # Player wants to place domino on right side of snake
                    if right_end in chosen_domino:
                        # Rotate domino if its first number matches right end, so second number aligns
                        if chosen_domino[0] == right_end:
                            domino_snake.append(chosen_domino)
                        else:
                            # Flip domino to align right end correctly
                            chosen_domino = [chosen_domino[1], chosen_domino[0]]
                            domino_snake.append(chosen_domino)
                        player.pop(index)  # Remove placed domino from player's hand
                        break
                    else:
                        print("Illegal move. Please try again.")
            else:
                print("Invalid input. Please try again.")
        except (ValueError, IndexError):
            # Handle non-integer input or invalid index
            print("Invalid input. Please enter a valid number.")

# Handle the computer's turn: find all valid moves, choose one randomly, rotate if needed, or draw from stock
def computer_turn(computer, domino_snake, stock):

    def _place_domino(domino, side):
        """
        Insert the domino on the specified side ('left' or 'right') of the domino_snake,
        flipping it if necessary to align with the snake's end number.
        """
        if side == "left":
            left_end = domino_snake[0][0]
            if domino[1] == left_end:
                domino_snake.insert(0, domino)
            else:
                domino_snake.insert(0, [domino[1], domino[0]])
        else:  # side == "right"
            right_end = domino_snake[-1][1]
            if domino[0] == right_end:
                domino_snake.append(domino)
            else:
                domino_snake.append([domino[1], domino[0]])

    # Combine computer pieces and domino snake to count occurrences of each number for scoring
    combined_list = computer + domino_snake
    flat_list = [num for piece in combined_list for num in piece]
    counts = Counter(flat_list)

    # Score each domino based on the frequency of its numbers in combined list
    scores = {tuple(domino): counts[domino[0]] + counts[domino[1]] for domino in computer}
    # Sort dominos by score descending
    sorted_score = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

    left_end = domino_snake[0][0]
    right_end = domino_snake[-1][1]
    move_made = False

    # Attempt to place the highest scoring dominos first
    for domino_tuple in sorted_score:
        domino = list(domino_tuple)
        if left_end in domino or right_end in domino:
            # Determine possible sides to place the domino
            can_place_left = left_end in domino
            can_place_right = right_end in domino

            if can_place_left and can_place_right:
                # Randomly choose side if both ends are possible
                side = random.choice(["left", "right"])
            elif can_place_left:
                side = "left"
            else:
                side = "right"

            _place_domino(domino, side)

            # Remove the placed domino from computer's hand
            for d in computer:
                if sorted(d) == sorted(domino):
                    computer.remove(d)
                    break

            move_made = True
            break

    # If no move was made, draw from stock if available
    if not move_made and stock:
        computer.append(stock.pop(random.randint(0, len(stock) - 1)))

# Main function to initialize game, determine starting player, and run game loop
def main():
    unique_dominos = generate_unique_dominos()
    stock, player, computer, doubles_player, doubles_computer = allocate_dominos(unique_dominos)

    # Determine starting player based on highest double; starting player places that double on the board
    if doubles_player and doubles_computer:
        if doubles_player[0] > doubles_computer[0]:
            domino_snake, status = [doubles_player.pop(0)], "computer"  # Player starts, computer moves next
            player.remove(domino_snake[0])
        else:
            domino_snake, status = [doubles_computer.pop(0)], "player"  # Computer starts, player moves next
            computer.remove(domino_snake[0])
    elif doubles_player:
        domino_snake, status = [doubles_player.pop(0)], "computer"
        player.remove(domino_snake[0])
    elif doubles_computer:
        domino_snake, status = [doubles_computer.pop(0)], "player"
        computer.remove(domino_snake[0])

    # Main game loop continues until a win/draw condition is met
    while True:
        game_result = check_game_status(domino_snake, player, computer, stock)
        if game_result is not None:
            status = game_result
            print_game_state(stock, player, computer, domino_snake, status)
            break  # End game loop
        print_game_state(stock, player, computer, domino_snake, status)
        if status == "player":
            player_turn(player, domino_snake, stock)  # Player makes a move
            status = "computer"  # Next turn is computer's
        else:
            computer_turn(computer, domino_snake, stock)  # Computer makes a move
            status = "player"  # Next turn is player's

# Run the game if this script is executed directly
if __name__ == "__main__":
    main()
