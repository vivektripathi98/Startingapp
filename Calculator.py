import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("250x400")

        # Create the display widget
        self.display = tk.Entry(self, font=("Arial", 20), bg="#eee", bd=0, justify="right")
        self.display.pack(fill="x", pady=10)

        # Create the buttons
        self.create_buttons()

    def create_buttons(self):
        # Create a frame to hold the buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(fill="x")

        # Create the buttons using a grid layout
        buttons = [
            "7", "8", "9", "*", "C",
            "4", "5", "6", "/", "sqrt",
            "1", "2", "3", "-", "^",
            "0", ".", "=", "+"
        ]
        for index, button in enumerate(buttons):
            tk.Button(buttons_frame, text=button, font=("Arial", 20), bg="#fff", bd=0, padx=10, pady=10,
                      command=lambda b=button: self.button_pressed(b)).grid(row=index // 5, column=index % 5)

    def button_pressed(self, button):
        # Handle button presses
        if button == "C":
            # Clear the display
            self.display.delete(0, "end")
        elif button == "=":
            # Calculate and display the result
            result = eval(self.display.get())
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        elif button == "sqrt":
            # Calculate and display the square root of the current value
            result = eval(self.display.get()) ** 0.5
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        elif button == "^":
            # Calculate and display the square of the current value
            result = eval(self.display.get()) ** 2
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        else:
            # Append the button text to the display
            self.display.insert("end", button)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
