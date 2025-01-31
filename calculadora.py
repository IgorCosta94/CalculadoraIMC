from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color


class IMCApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        with main_layout.canvas.before:
            Color(0, 1,0.80, 0.80)
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)

        main_layout.bind(size=self.update_rect, pos=self.update_rect)

        main_layout.add_widget(
            Label(text="Calculadora de IMC", font_size=30, bold=True, color=(1, 0.80, 0.5, 1)))

        height_layout = BoxLayout(orientation="horizontal", padding= 20 ,spacing=10)
        height_layout.add_widget(Label(text="Altura (m):", font_size=20, size_hint=(0.4, 1),color=(0, 0, 0, 1)))
        self.height_input = TextInput(multiline=False, font_size=20)
        height_layout.add_widget(self.height_input)
        main_layout.add_widget(height_layout)

        weight_layout = BoxLayout(orientation="horizontal",padding= 20 ,spacing=10)
        weight_layout.add_widget(Label(text="Peso (kg):", font_size=20, size_hint=(0.4, 1),color=(0, 0, 0, 1)))
        self.weight_input = TextInput(multiline=False, font_size=20)
        weight_layout.add_widget(self.weight_input)
        main_layout.add_widget(weight_layout)

        calculate_button = Button(text="Calcular IMC", font_size=22, size_hint=(0.3, 0.5), pos_hint={"center_x": 0.60, "center_y": 0.60},color=(0, 0, 0, 1),background_color=(0.8, 0, 8, 0.5))
        calculate_button.bind(on_press=self.calculate_imc)
        main_layout.add_widget(calculate_button)

        result_layout = BoxLayout(orientation="horizontal", padding= 20,spacing=10)
        result_layout.add_widget(Label(text="IMC:", font_size=20, size_hint=(0.4, 1),color=(0, 0, 0, 1)))
        self.result_input = TextInput(multiline=False, readonly=True, font_size=20)
        result_layout.add_widget(self.result_input)
        main_layout.add_widget(result_layout)

        category_layout = BoxLayout(orientation="horizontal", padding= 20,spacing=10)
        category_layout.add_widget(Label(text="Categoria:", font_size=20, size_hint=(0.4, 1),color=(0, 0, 0, 1)))
        self.classificacao_input = TextInput(multiline=False, readonly=True, font_size=20)
        category_layout.add_widget(self.classificacao_input)
        main_layout.add_widget(category_layout)

        return main_layout

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def calculate_imc(self, instance):
        try:
            altura = float(self.height_input.text)
            peso = float(self.weight_input.text)

            if altura > 0 and peso > 0:
                imc = peso / (altura ** 2)
                self.result_input.text = f"{imc:.2f}"

                categoria = self.classificacao_category(imc)
                self.classificacao_input.text = categoria

            else:
                self.result_input.text = "Erro"
        except ValueError:
            self.result_input.text = "Inválido"

    def classificacao_category(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"

if __name__ == "__main__":
    IMCApp().run()
