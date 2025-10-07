from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
import sys

class TerminalMenu:
    def __init__(self, options, title="Menu"):
        self.options = options
        self.title = title
        self.current_index = 0
        self.selected_option = None
        self.kb = KeyBindings()
        
        @self.kb.add('up')
        def move_up(event):
            self.current_index = (self.current_index - 1) % len(self.options)
            event.app.invalidate()
        
        @self.kb.add('down')
        def move_down(event):
            self.current_index = (self.current_index + 1) % len(self.options)
            event.app.invalidate()
        
        @self.kb.add('enter')
        def select_option(event):
            self.selected_option = self.options[self.current_index]
            event.app.exit()
        
        @self.kb.add('c-c')
        def exit_app(event):
            event.app.exit()
    
    def get_menu_text(self):
        lines = [('bold underline', f'{self.title}\n')]
        for idx, option in enumerate(self.options):
            if idx == self.current_index:
                lines.append(('bg:#00aa00 #ffffff bold', f'  > {option}\n'))
            else:
                lines.append(('', f'    {option}\n'))
        return lines
    
    def run(self):
        style = None
        
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
        
        app = Application(
            layout=layout,
            key_bindings=self.kb,
            style=style,
            full_screen=False
        )
        
        app.run()
        
        return self.selected_option


if __name__ == "__main__":
    options = [
        "Convert Image to ASCII",
        "View Image Gallery", 
        "Settings",
        "Exit"
    ]
    
    menu = TerminalMenu(options, title="=== ASCII Art Converter ===")
    choice = menu.run()
    
    if choice == "Convert Image to ASCII":
        print("Converting image...")
    elif choice == "View Image Gallery":
        print("Viewing gallery...")
    elif choice == "Settings":
        print("Opening settings...")
    elif choice == "Exit":
        print("Goodbye!")
        sys.exit(0)
