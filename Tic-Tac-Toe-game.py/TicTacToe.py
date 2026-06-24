import sys

class TicTacToe:
    """A minimal, interview-ready Tic-Tac-Toe with an O(1) winner check."""

    def __init__(self, n: int):
        if n < 3:
            print("❌ Board size must be 3 or more.")
            sys.exit()
        
        # Core game state
        self.n = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.current_player = 'X'
        self.winner = None
        self.moves_made = 0

        # The key data structures for O(1) winner detection
        self._player_map = {'X': 1, 'O': -1}
        self._rows = [0] * n
        self._cols = [0] * n
        self._diagonal = 0
        self._anti_diagonal = 0

    def _print_board(self):
        """Helper to display the current board state."""
        print()
        for i, row in enumerate(self.board):
            print(f"  {' | '.join(cell for cell in row)}")
            if i < self.n - 1:
                print(" " + "---" * self.n)
        print()

    def _make_move(self, row: int, col: int) -> bool:
        """
        Places a mark, updates counters, and checks for a winner in O(1) time.
        Returns True if the move was successful, False otherwise.
        """
        if not (0 <= row < self.n and 0 <= col < self.n and self.board[row][col] == ' '):
            return False

        # Update board and state
        self.board[row][col] = self.current_player
        self.moves_made += 1
        player_value = self._player_map[self.current_player]

        # Update the O(1) counters
        self._rows[row] += player_value
        self._cols[col] += player_value
        if row == col:
            self._diagonal += player_value
        if row + col == self.n - 1:
            self._anti_diagonal += player_value

        # Check for a winner by seeing if any counter sum equals +/- n
        if abs(self._rows[row]) == self.n or \
           abs(self._cols[col]) == self.n or \
           abs(self._diagonal) == self.n or \
           abs(self._anti_diagonal) == self.n:
            self.winner = self.current_player
        
        return True

    def play(self):
        """The main game loop."""
        while not self.winner and self.moves_made < self.n * self.n:
            self._print_board()
            print(f"Player '{self.current_player}', it's your turn.")
            
            try:
                move = input(f"Enter your move as row,col (0-{self.n-1}): ")
                row, col = map(int, move.split(','))
                
                if not self._make_move(row, col):
                    print("🔴 Invalid move! That spot is taken or out of bounds. Try again.")
                    continue
                    
            except (ValueError, IndexError):
                print("🔴 Invalid format. Please enter as row,col (e.g., 1,2).")
                continue

            # Switch player only after a successful move
            if not self.winner:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

        # Announce the final result
        self._print_board()
        if self.winner:
            print(f"🎉 Congratulations Player '{self.winner}', you win!")
        else:
            print("🤝 It's a draw!")


# --- Main Entrypoint ---
if __name__ == "__main__":
    try:
        board_size = int(input("Enter the board size (e.g., 3 for 3x3): "))
        game = TicTacToe(n=board_size)
        game.play()
    except ValueError:
        print("🔴 Please enter a valid number for the board size.")