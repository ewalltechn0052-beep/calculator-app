%%writefile main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (360, 600)

class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.display = TextInput(
            text='0', font_size=50, readonly=True, halign='right',
            multiline=False, size_hint=(1, 0.2),
            background_color=(0.95, 0.95, 0.95, 1)
        )
        main_layout.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=5, size_hint=(1, 0.8))
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]
        for row in buttons:
            for text in row:
                btn = Button(text=text, font_size=35)
                btn.bind(on_press=self.on_press)
                if text == 'C':
                    btn.background_color = (0.9, 0.2, 0.2, 1)
                elif text in ['=', '+', '-', '*', '/']:
                    btn.background_color = (0.2, 0.6, 0.9, 1)
                else:
                    btn.background_color = (0.9, 0.9, 0.9, 1)
                grid.add_widget(btn)

        main_layout.add_widget(grid)
        return main_layout

    def on_press(self, instance):
        text = instance.text
        current = self.display.text
        if text == 'C':
            self.display.text = '0'
        elif text == '=':
            try:
                result = eval(current.replace('×', '*').replace('÷', '/'))
                self.display.text = str(result)
            except Exception:
                self.display.text = 'Error'
        else:
            if current in ('0', 'Error'):
                self.display.text = text
            else:
                self.display.text = current + text

if __name__ == '__main__':
    CalculatorApp().run()
