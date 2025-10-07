"""
Terminal Menu Module

This module provides a TerminalMenu class for creating interactive terminal menus
using the prompt_toolkit library. Users can navigate with arrow keys and select options.
"""

from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
import sys

class TerminalMenu:
    """
    A class for creating interactive terminal menus with keyboard navigation.
    
    Attributes:
        options (list): List of menu options to display
        title (str): Title displayed at the top of the menu
        current_index (int): Index of the currently selected option
        selected_option (str): The option selected by the user
        kb (KeyBindings): Keyboard bindings for menu navigation
    """
    
    def __init__(self, options, title="Menu"):
        """
        Initialize the TerminalMenu with options and title.
        
        Args:
            options (list): List of menu option strings
            title (str): Menu title (default: "Menu")
        """
        self.options = options
        self.title = title
        self.current_index = 0
        self.selected_option = None
        self.kb = KeyBindings()
        
        # Key binding for moving up in the menu
        @self.kb.add('up')
        def move_up(event):
            # Use modulo to wrap around to the bottom when at the top
            self.current_index = (self.current_index - 1) % len(self.options)
            event.app.invalidate()  # Refresh the display
        
        # Key binding for moving down in the menu
        @self.kb.add('down')
        def move_down(event):
            # Use modulo to wrap around to the top when at the bottom
            self.current_index = (self.current_index + 1) % len(self.options)
            event.app.invalidate()  # Refresh the display
        
        # Key binding for selecting the current option
        @self.kb.add('enter')
        def select_option(event):
            self.selected_option = self.options[self.current_index]
            event.app.exit()  # Exit the application
        
        # Key binding for exiting with Ctrl+C
        @self.kb.add('c-c')
        def exit_app(event):
            event.app.exit()
    
    def get_menu_text(self):
        """
        Generate formatted text for the menu display.
        
        Returns:
            list: List of tuples containing (style, text) for each menu line
        """
        # Add the menu title with bold and underline styling
        lines = [('bold underline', f'{self.title}\n')]
        
        # Add each menu option with appropriate styling
        for idx, option in enumerate(self.options):
            if idx == self.current_index:
                # Highlight the currently selected option with green background
                lines.append(('bg:#00aa00 #ffffff bold', f'  > {option}\n'))
            else:
                # Display non-selected options with plain styling
                lines.append(('', f'    {option}\n'))
        return lines
    
    def run(self):
        """
        Display the menu and wait for user selection.
        
        Returns:
            str: The selected option, or None if no selection was made
        """
        style = None
        
        # Create the layout with the menu content
        layout = Layout(
            HSplit([
                Window(
                    content=FormattedTextControl(
                        text=self.get_menu_text
                    ),
                    height=len(self.options) + 2
                )
            ])
        )
        
        # Create the application with the layout and key bindings
        app = Application(
            layout=layout,
            key_bindings=self.kb,
            style=style,
            full_screen=False
        )
        
        # Run the application (blocks until selection is made)
        app.run()
        
        # Return the selected option
        return self.selected_option


# Example usage when run as a standalone script
if __name__ == "__main__":
    # Define menu options
    options = [
        "Convert Image to ASCII",
        "View Image Gallery", 
        "Settings",
        "Exit"
    ]
    
    # Create and display the menu
    menu = TerminalMenu(options, title="=== ASCII Art Converter ===")
    choice = menu.run()
    
    # Handle the user's choice
    if choice == "Convert Image to ASCII":
        print("Converting image...")
    elif choice == "View Image Gallery":
        print("Viewing gallery...")
    elif choice == "Settings":
        print("Opening settings...")
    elif choice == "Exit":
        print("Goodbye!")
        sys.exit(0)
