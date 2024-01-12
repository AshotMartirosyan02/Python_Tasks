from tkinter import Text, Menu, filedialog, font, BOTH, END


class TextEditor:
    def __init__(self, root) -> None:
        self.root = root
        root.title("My Text Editor")
        self.current_file_path = ''

        self.current_font = font.Font(family="Arial", size=12)

        self.text = Text(root, font=self.current_font, undo=True)
        self.text.pack(expand=True, fill=BOTH)

        self.menu = Menu(root)
        root.config(menu=self.menu)

        file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)

        edit_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text.edit_redo)

    def open_file(self) -> None:
        file_path = filedialog.askopenfilename(initialdir='~/Desktop', filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_file_path = file_path
            with open(file_path, "r") as file:
                content = file.read()
            self.text.delete(1.0, END)
            self.text.insert(END, content)

    def save_file(self) -> None:
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                content = self.text.get(1.0, END)
                file.write(content)
        else:
            self.save_as()

    def save_as(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.current_file_path = file_path
            self.save_file()

    def exit_editor(self) -> None:
        self.root.quit()
