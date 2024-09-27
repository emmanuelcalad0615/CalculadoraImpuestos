from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)
from Logi.Calculadora import CalcularCouta

class CalculadoraApp(App):
    def build(self):
        """Builds the user interface for the calculator application."""
        self.scroll_view = ScrollView()
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Change background color
        with self.layout.canvas.before:
            Color(0, 0, 0)  # Background color
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Styles
        label_color = (1, 1, 1)  # White
        input_color = (0.95, 0.95, 0.95, 1)  # Light color for inputs
        button_color = (0.5, 0.5, 0.5)  # Button color

        # Inputs
        self.inputs = {}
        fields = [
            "Ingresos laborales",
            "Otros ingresos",
            "Retenciones de fuente",
            "Pagos a Seguridad Social",
            "Aportes a pensión",
            "Pagos hipotecarios",
            "Donaciones",
            "Gastos educativos"
        ]

        for field in fields:
            label = Label(text=field, size_hint_y=None, height=40, color=label_color)
            self.layout.add_widget(label)
            input_field = TextInput(
                multiline=False,
                size_hint_y=None,
                height=40,
                background_color=input_color,
                hint_text="Ingrese correctamente todos los campos: " + field.lower(),
                hint_text_color=(0,0,0)  
            )
            self.layout.add_widget(input_field)
            self.inputs[field] = input_field

        # Calculate button
        self.calc_button = Button(text='Calcular', size_hint_y=None, height=50)
        self.calc_button.bind(on_press=self.calculate)
        self.calc_button.background_color = button_color
        self.calc_button.color = (1, 1, 1)  # White text on button
        self.layout.add_widget(self.calc_button)

        # Result label
        self.result_label = Label(text="", size_hint_y=None, height=40, color=(1, 1, 1))
        self.layout.add_widget(self.result_label)

        self.scroll_view.add_widget(self.layout)
        return self.scroll_view

    def _update_rect(self, instance, value):
        """Updates the position and size of the background rectangle."""
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def calculate(self, instance):
        """Calculates the tax based on user inputs and displays the result."""
        try:
            values = {field: int(self.inputs[field].text) for field in self.inputs}
            result = CalcularCouta(
                values["Ingresos laborales"],
                values["Otros ingresos"],
                values["Retenciones de fuente"],
                values["Pagos a Seguridad Social"],
                values["Aportes a pensión"],
                values["Pagos hipotecarios"],
                values["Donaciones"],
                values["Gastos educativos"]
            )
            self.result_label.text = f"Total a pagar: {result}"
        except Exception as el_error:
            self.result_label.text = f"Valor Ingresado Erroneo: {str(el_error)}"  # Display error message

if __name__ == '__main__':
    CalculadoraApp().run()  # Run the application
