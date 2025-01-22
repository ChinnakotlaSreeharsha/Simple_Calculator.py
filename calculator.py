import customtkinter as ctk

# Configure the theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"

# Main application
class TechWinz_Adventures(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TechWinz Adventures")
        self.geometry("400x600")
        self.configure(padx=10, pady=10)
        
        # Display frame
        self.display_var = ctk.StringVar()
        self.display = ctk.CTkEntry(self, textvariable=self.display_var, font=("Arial", 24), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")
        
        # Button configurations
        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        
        # Create buttons dynamically
        for text, row, col in self.buttons:
            button = ctk.CTkButton(self, text=text, font=("Arial", 20), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        # Grid configuration
        for i in range(5):  # Rows
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):  # Columns
            self.grid_columnconfigure(j, weight=1)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.display_var.set("")  # Clear the display
        elif button_text == "=":
            try:
                # Evaluate the expression
                result = eval(self.display_var.get())
                self.display_var.set(result)
            except Exception:
                self.display_var.set("Error")
        else:
            # Append the button text to the display
            current_text = self.display_var.get()
            self.display_var.set(current_text + button_text)

# Run the application
if __name__ == "__main__":
    app = TechWinz_Adventures()
    app.mainloop()
