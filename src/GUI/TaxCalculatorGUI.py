from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.popup import Popup

import sys
sys.path.append("src")
from TaxCalculator.IncomeDeclaration import NaturalPerson, IncomeDeclaration

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        contenedor = BoxLayout(orientation="vertical", padding=50, spacing=20)
        
        with contenedor.canvas.before:
            Color(1, 1, 1)
            self.rect = RoundedRectangle(size=contenedor.size, pos=contenedor.pos)
            contenedor.bind(size=self._update_rect, pos=self._update_rect)

        welcome_label = Label(text="Welcome to the Tax Calculator", font_size='24sp', halign="center", bold=True, color=(0, 0, 0))
        contenedor.add_widget(welcome_label)

        #img = Image(source='TaxCalculator.png')
        #contenedor.add_widget(img)

        instructions_label = Label(text="Please enter all fields correctly to calculate your Tax. \n \n If you don't have [b]other incomes[/b] or [b]donations[/b], let it empty or put zero.", font_size='20sp', halign="center", color=(0, 0, 0), markup=True)
        contenedor.add_widget(instructions_label)


        button = Button(text='Go to Calculator', size=(200, 50), size_hint_y=None, background_color=(0.37, 0.75, 0.96), background_normal='', color=(1, 1, 1), font_size='20sp', bold=True)
        button.bind(on_press=self.change_screen)
        contenedor.add_widget(button)
        
        self.add_widget(contenedor)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos
    
    def change_screen(self, instance):
        self.manager.current = "questions_screen"


class QuestionsScreen(Screen):
    def __init__(self, **kwargs):
        super(QuestionsScreen, self).__init__(**kwargs)
        contenedor = BoxLayout(orientation="vertical", padding=50, spacing=20)
        
        with contenedor.canvas.before:
            Color(1, 1, 1)
            self.rect = RoundedRectangle(size=contenedor.size, pos=contenedor.pos)
            contenedor.bind(size=self._update_rect, pos=self._update_rect)

        instruction_label = Label(text="Please answer the following questions before proceeding:", font_size='20sp', halign="center", color=(0, 0, 0))
        contenedor.add_widget(instruction_label)

        self.inputs = {}

        fields = ["Name", "ID", "Occupation"]
        for field in fields:
            label = Label(text=field, size_hint_y=None, height=40, color=(0, 0, 0, 1), halign="left", valign="middle", font_size='20', bold=True)
            contenedor.add_widget(label)

            input_field = TextInput(multiline=False, size_hint_y=None, height=40, font_size='20sp', hint_text="Enter your " + field)
            contenedor.add_widget(input_field)
            self.inputs[field] = input_field

        next_button = Button(text='Next', size=(200, 50), size_hint_y=None, background_color=(0.37, 0.75, 0.96), background_normal='', color=(1, 1, 1), font_size='20sp', bold=True)
        next_button.bind(on_press=self.go_to_calculator)
        contenedor.add_widget(next_button)

        self.add_widget(contenedor)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def go_to_calculator(self, instance):
        self.manager.current = "calculator_screen"


class CalculadoraScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculadoraScreen, self).__init__(**kwargs)
        self.build() 

    def build(self):
        layout_back = BoxLayout(orientation='horizontal')  # Layout principal para toda la pantalla

        # Botón de regreso en la parte izquierda
        back_button = Button(text="Back", size_hint=(0.1, 1), color=(1, 1, 1), font_size='20sp', bold=True, background_color=(0.37, 0.75, 0.96), background_normal='')
        back_button.bind(on_press=self.go_back)
        layout_back.add_widget(back_button)

        scroll_view = ScrollView(size_hint=(0.9, 1), bar_width=5, bar_color=(1, 1, 1, 1))
        scroll_view.effect_cls = "ScrollEffect"
        
        contenedor = GridLayout(cols=2, padding=80, spacing=20, size_hint_y=None)
        contenedor.bind(minimum_height=contenedor.setter('height'))

        with contenedor.canvas.before:
            Color(1, 1, 1)
            self.rect = RoundedRectangle(size=contenedor.size, pos=contenedor.pos)
            contenedor.bind(size=self._update_rect, pos=self._update_rect)

        title_label = Label(text="Tax Calculator", font_size='24sp', color=(0, 0, 0, 1), size_hint_y=None, height=50, bold=True)
        contenedor.add_widget(Label(text=""))
        contenedor.add_widget(title_label)

        self.inputs = {}
        fields = [
            "Labor Income", 
            "Other Incomes", 
            "Withholding sources",
            "Social Security Payments", 
            "Pension Contributions",
            "Mortgage Payments", 
            "Donations", 
            "Educational Expenses"
        ]

        for field in fields:
            label = Label(text=field, size_hint_y=None, height=40, color=(0, 0, 0, 1), halign="left", valign="middle", font_size='20', bold=True)
            contenedor.add_widget(label)

            input_field = TextInput(multiline=False, size_hint_y=None, height=40, hint_text="$",font_size='20sp')
            contenedor.add_widget(input_field)
            self.inputs[field] = input_field

        calculate_button = Button(text='Calculate', size_hint_y=None, height=50, background_color=(0.37, 0.75, 0.96), background_normal='', color=(1, 1, 1), font_size='20sp', bold=True)
        calculate_button.bind(on_press=self.calculate)
        contenedor.add_widget(Label(text=""))
        contenedor.add_widget(calculate_button)

        scroll_view.add_widget(contenedor)
        layout_back.add_widget(scroll_view)
        
        self.add_widget(layout_back)


    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def calculate(self, instance):
        try:
            inputs = {
                "Labor Income": "labor_income",
                "Other Incomes": "other_income",
                "Withholding sources": "withholding_source",
                "Social Security Payments": "social_security_payments",
                "Pension Contributions": "pension_contributions",
                "Mortgage Payments": "mortgage_payments",
                "Donations": "donations",
                "Educational Expenses": "educational_expenses"}

            values = {inputs[field]: int(self.inputs[field].text) if self.inputs[field].text else 0 for field in inputs}

            person = NaturalPerson(
                values["labor_income"],
                values["other_income"],
                values["withholding_source"],
                values["social_security_payments"],
                values["pension_contributions"],
                values["mortgage_payments"],
                values["donations"],
                values["educational_expenses"]
            )
            
            declaration = IncomeDeclaration(person)
            tax_value = declaration.calcular_valor_impuesto()


            contenedor = BoxLayout(orientation='vertical', padding=10, spacing=10)
            result_label = Label(text=f"Total Tax: ${tax_value:,.2f}", font_size='20sp', halign="center", color=(0.37, 0.75, 0.96))
            close_button = Button(text="Close", size_hint_y=None, background_color=(0.37, 0.75, 0.96), height=50, on_press=lambda x: popup.dismiss())

            contenedor.add_widget(result_label)
            contenedor.add_widget(close_button)

            popup = Popup(title='Result', content=contenedor, size_hint=(0.8, 0.5), auto_dismiss=False)

            popup.open()

        except Exception as el_error:
            print(el_error)

            contenedor = BoxLayout(orientation='vertical', padding=10, spacing=10)
            error_label = Label(text=f"¡ERROR! Incorrect Value Entered: \n {str(el_error)}", font_size='20sp', halign="center", color=(1, 0, 0))
            close_button = Button(text="Close", size_hint_y=None, background_color=(0.37, 0.75, 0.96), height=50, on_press=lambda x: popup.dismiss())

            contenedor.add_widget(error_label)
            contenedor.add_widget(close_button)

            popup = Popup(title='Error', content=contenedor, size_hint=(0.8, 0.5), auto_dismiss=False)

            popup.open()

    def go_back(self, instance):
        self.clear_fields()
        self.manager.current = "questions_screen"
        
    
    def clear_fields(self):
        for field in self.inputs:
            self.inputs[field].text = ""

class CalculadoraApp(App):
    def build(self):
        contenedor = ScreenManager()

        contenedor.add_widget(MainScreen(name="main_screen"))
        contenedor.add_widget(QuestionsScreen(name="questions_screen"))  
        contenedor.add_widget(CalculadoraScreen(name="calculator_screen"))

        return contenedor

if __name__ == '__main__':
    CalculadoraApp().run()
