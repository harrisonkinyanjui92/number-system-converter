from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.metrics import dp
from kivy.core.window import Window

# Main window background
Window.clearcolor = (0.05, 0.25, 0.1, 1)


class NumberConverterApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20)
        )

        # TITLE
        title = Label(
            text="NUMBER SYSTEM CONVERTER",
            font_size=dp(26),
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(60)
        )
        layout.add_widget(title)

        # NUMBER INPUT
        self.number_input = TextInput(
            hint_text="Enter your number",
            multiline=False,
            font_size=dp(22),
            foreground_color=(0, 0, 0, 1),
            background_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(55),
            halign="center"
        )
        layout.add_widget(self.number_input)

        # FROM SYSTEM - YELLOW
        self.from_system = Spinner(
            text="Binary(2)",
            values=(
                "Binary(2)",
                "Decimal(10)",
                "Octal(8)",
                "Hexadecimal(16)"
            ),
            font_size=dp(20),
            color=(0, 0, 0, 1),
            background_color=(1, 1, 0, 1),
            size_hint_y=None,
            height=dp(55)
        )
        layout.add_widget(self.from_system)

        # CONVERT - BLACK
        convert_button = Button(
            text="CONVERT",
            font_size=dp(20),
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(60)
        )
        convert_button.bind(on_press=self.convert_number)
        layout.add_widget(convert_button)

        # TO SYSTEM - YELLOW
        self.to_system = Spinner(
            text="Decimal(10)",
            values=(
                "Binary(2)",
                "Decimal(10)",
                "Octal(8)",
                "Hexadecimal(16)"
            ),
            font_size=dp(20),
            color=(0, 0, 0, 1),
            background_color=(1, 1, 0, 1),
            size_hint_y=None,
            height=dp(55)
        )
        layout.add_widget(self.to_system)

        # SWAP - GREEN
        swap_button = Button(
            text="SWAP",
            font_size=dp(20),
            color=(1, 1, 1, 1),
            background_color=(0, 0.6, 0.3, 1),
            size_hint_y=None,
            height=dp(55)
        )
        swap_button.bind(on_press=self.swap_systems)
        layout.add_widget(swap_button)

        # CLEAR - RED
        clear_button = Button(
            text="CLEAR",
            font_size=dp(20),
            color=(1, 1, 1, 1),
            background_color=(0.8, 0.1, 0.1, 1),
            size_hint_y=None,
            height=dp(55)
        )
        clear_button.bind(on_press=self.clear_fields)
        layout.add_widget(clear_button)

        # RESULT - BLUE
        self.result = Label(
            text="Final Result:",
            font_size=dp(23),
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(70)
        )
        layout.add_widget(self.result)

        return layout

    # CONVERT
    def convert_number(self, instance):

        number = self.number_input.text.strip()
        from_system = self.from_system.text
        to_system = self.to_system.text

        bases = {
            "Binary(2)": 2,
            "Decimal(10)": 10,
            "Octal(8)": 8,
            "Hexadecimal(16)": 16
        }

        try:

            if number == "":
                self.result.text = "Please enter a number!"
                return

            decimal_number = int(
                number,
                bases[from_system]
            )

            if to_system == "Binary(2)":
                result = format(decimal_number, "b")

            elif to_system == "Octal(8)":
                result = format(decimal_number, "o")

            elif to_system == "Hexadecimal(16)":
                result = format(decimal_number, "X")

            elif to_system == "Decimal(10)":
                result = str(decimal_number)

            self.result.text = f"Final Result: {result}"

        except ValueError:
            self.result.text = "Invalid number!"

        except KeyError:
            self.result.text = "Invalid system!"

    # SWAP
    def swap_systems(self, instance):

        old_from = self.from_system.text
        old_to = self.to_system.text

        self.from_system.text = old_to
        self.to_system.text = old_from

    # CLEAR
    def clear_fields(self, instance):

        self.number_input.text = ""

        self.from_system.text = "Binary(2)"

        self.to_system.text = "Decimal(10)"

        self.result.text = "Final Result:"


NumberConverterApp().run()