from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import prompt
from prompt_toolkit.keys import Keys

class Menu:
    def __init__(self, option_list):
        self.option_list = option_list
        self.index = 0

    def draw_menu(self):
        for i, (value, label) in enumerate(self.option_list):
            prefix = ">" if i == self.index else "  "
            print(f"{prefix} {label}")

    def move_up(self):
        self.index = (self.index - 1) % len(self.option_list) # Using % makes sure you cant go out of bounds of the list

    def move_down(self):
        self.index = (self.index + 1) % len(self.option_list)

    def get_key_input(self):
        # Create key bindings
        kb = KeyBindings()
        
        @kb.add('up')
        def _(event):
            event.app.exit(result='up')
        
        @kb.add('down')
        def _(event):
            event.app.exit(result='down')
        
        @kb.add('enter')
        def _(event):
            event.app.exit(result='enter')
        
        # Use prompt with key bindings
        result = prompt('', key_bindings=kb, return_as_string=True)
        return result

    def run(self):
        while True:
            self.draw_menu()
            key = self.get_key_input()

            if key == "up":
                self.move_up()
            elif key == "down":
                self.move_down()
            elif key == "enter":
                return self.option_list[self.index][0]
