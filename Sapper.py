from tkinter import *
from tkinter.messagebox import showinfo
from random import randint


def CellClicked(cell):
    global G_digged
    if cell in G_bombs_cells:
        [cell_.config(state="disabled") for cell_ in G_field]
        [cell_.config(bg="red", state="disabled", text="*") for cell_ in G_bombs_cells]
        showinfo("Restart the game looser", "Sike, that's the wrong choice!")
    else:
        cell.config(bg="brown", state="disabled", relief="ridge")
        G_digged += 1
        s = 0
        for cell_ in G_bombs_cells:
            for cell__ in ((cell.x - 1, cell.y - 1), (cell.x - 1, cell.y), (cell.x - 1, cell.y + 1),
                           (cell.x, cell.y - 1), (cell.x, cell.y + 1),
                           (cell.x + 1, cell.y - 1), (cell.x + 1, cell.y), (cell.x + 1, cell.y + 1)):
                if (cell_.x, cell_.y) == cell__:
                    s += 1
                    # cell_.config(bg="blue")
                    break
        if s != 0:
            cell.config(text=f"{s}")
        if G_digged == G_empty_cells:
            showinfo("The end", "Hey, that's pretty good!")


def Flag(event, cell):
    if cell["state"] != "disabled":
        cell.config(text="F", bg="blue") if cell["text"] == "" else cell.config(text="", bg="green")


if __name__ == "__main__":
    root = Tk()
    root.resizable(0, 0)
    G_ROW, G_COLUMN = 10, 10
    G_BOMBS = 25
    G_empty_cells = G_ROW * G_COLUMN - G_BOMBS
    G_bombs_cells = []
    G_bombs_cells_pos = []
    G_field = []
    G_digged = 0
    for y in range(G_COLUMN):
        for x in range(G_ROW):
            cell = Button(root, width=2, activebackground="brown", bg="green")
            cell.x = x
            cell.y = y
            # Left click - mine cell in field
            cell.config(command=lambda cell=cell: CellClicked(cell))
            # Right click - set flag over a cell
            cell.bind("<Button-3>", lambda e, cell=cell: Flag(e, cell))
            cell.grid(row=x, column=y)
            G_field.append(cell)
    # Generates random placed bomb cells
    for i in range(G_BOMBS):
        x, y = randint(0, G_ROW - 1), randint(0, G_COLUMN - 1)
        while (x, y) in G_bombs_cells_pos:
            x, y = randint(0, G_ROW - 1), randint(0, G_COLUMN - 1)
        for cell in G_field:
            if (x, y) == (cell.x, cell.y):
                G_bombs_cells.append(cell)
                G_bombs_cells_pos.append((x, y))
                break
    cell.grid(row=x, column=y)
    root.mainloop()
