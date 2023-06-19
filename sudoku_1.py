
import tkinter as tk


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.board = [
            [0, 6, 0, 4, 0, 3, 8, 0, 0],
            [0, 0, 7, 0, 0, 6, 0, 4, 0],
            [3, 0, 0, 0, 5, 0, 0, 0, 6],
            [1, 2, 3, 0, 0, 5, 4, 0, 9],
            [5, 8, 9, 7, 0, 0, 0, 6, 0],
            [7, 0, 0, 2, 1, 0, 5, 0, 0],
            [4, 0, 0, 0, 0, 8, 0, 1, 3],
            [6, 0, 0, 1, 9, 0, 2, 0, 4],
            [0, 5, 0, 3, 0, 2, 6, 0, 0]
        ]
        self.user_board = [[self.board[row][col] for col in range(9)] for row in range(9)]

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.cells = [[None for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                frame_index = (row // 3) * 3 + col // 3  # Determine the index of the 3x3 frame
                cell_bg = "white" if frame_index % 2 == 0 else "#f0f0f0"  # Alternating frame colors
                ipadx, ipady, padx, pady = 5, 5, 1, 1
                if row % 3 == 0 and row != 0:
                    pady = (0, 3)
                if col % 3 == 0 and col != 0:
                    padx = (0, 3)
                self.cells[row][col] = tk.Entry(
                    self.frame,
                    width=4,
                    font=("Arial", 20, "bold"),
                    justify="center",
                    bg=cell_bg,
                    relief="solid"
                )
                self.cells[row][col].grid(row=row, column=col, ipadx=ipadx, ipady=ipady, padx=padx, pady=pady)
                if self.user_board[row][col] != 0:
                    self.cells[row][col].insert(0, str(self.user_board[row][col]))
                    self.cells[row][col].config(state="disabled")

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        self.solve_button.pack(pady=10)

    def is_valid_move(self, row, col, num):
        # Check if the number already exists in the same row or column
        for i in range(9):
            if self.user_board[row][i] == num or self.user_board[i][col] == num:
                return False

        # Check if the number already exists in the same 3x3 box
        box_row = row // 3
        box_col = col // 3
        for i in range(3):
            for j in range(3):
                if self.user_board[box_row * 3 + i][box_col * 3 + j] == num:
                    return False

        return True

    def solve_sudoku(self):
        if self.solve_sudoku_helper():
            for row in range(9):
                for col in range(9):
                    self.cells[row][col].config(state="normal")
                    self.cells[row][col].delete(0, "end")
                    self.cells[row][col].insert(0, str(self.user_board[row][col]))
                    self.cells[row][col].config(state="disabled")
        else:
            print("No solution exists.")

    def solve_sudoku_helper(self):
        for row in range(9):
            for col in range(9):
                if self.user_board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.user_board[row][col] = num
                            if self.solve_sudoku_helper():
                                return True
                            self.user_board[row][col] = 0
                    return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
