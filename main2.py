from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()  # Usando FloatLayout para permitir o posicionamento flexível

        # Adiciona a logomarca e faz com que ela ocupe todo o espaço
        try:
            logo = Image(source='C:\\Users\\tceno\\OneDrive\\Área de Trabalho\\MEUS-TRABALHOS\\FOTUS\FOTUS\\home.png',
                          allow_stretch=True,
                          keep_ratio=False,
                          size_hint=(1, 1))
            layout.add_widget(logo)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

        # Adiciona um botão para carregar pratos
        btn_carregar = Button(text='Carregar Pratos', size_hint=(0.8, 0.1),
                               background_color=(1.0, 0.34, 0.20, 1),
                               background_normal='',
                               pos_hint={'x': 0.1, 'y': 0.1})
        layout.add_widget(btn_carregar)

        # Adiciona um botão para abrir o cardápio
        btn_cardapio = Button(text='Abrir Cardápio', size_hint=(0.8, 0.1),
                               background_color=(0.2, 0.7, 0.3, 1),
                               background_normal='',
                               pos_hint={'x': 0.1, 'y': 0.2})
        btn_cardapio.bind(on_press=self.abrir_cardapio)  # Bind para abrir cardápio
        layout.add_widget(btn_cardapio)

        self.add_widget(layout)

    def abrir_cardapio(self, instance):
        self.manager.current = 'cardapio'  # Muda para a tela do cardápio

class CardapioScreen(Screen):
    def __init__(self, **kwargs):
        super(CardapioScreen, self).__init__(**kwargs)

        # Criando um ScrollView
        scroll_view = ScrollView(do_scroll_x=False)
        layout = GridLayout(cols=1, size_hint_y=None, padding=[10, 10, 10, 10], spacing=10)  # GridLayout para armazenar os botões
        layout.bind(minimum_height=layout.setter('height'))  # Ajusta a altura do layout

        # Botões para diferentes categorias de pratos
        categorias = [
            'À La Carte', 'Churrascos', 'Tira-Gosto',
            'Cerveja 600ml', 'Cervejas Long Neck',
            'Pratos Executivos', 'Torres', 'Combos', 'Salgados'
        ]

        for categoria in categorias:
            btn_categoria = Button(text=categoria, size_hint=(1, None),
                                    height=50,
                                    background_color=(0.1, 0.5, 0.8, 1),
                                    font_size=18,
                                    color=(1, 1, 1, 1),
                                    background_normal='',
                                    background_down='')
            btn_categoria.bind(on_press=self.abrir_categoria)  # Bind para abrir categoria
            layout.add_widget(btn_categoria)

        # Botão para voltar
        btn_voltar = Button(text='Voltar', size_hint=(1, None),
                             height=50,
                             background_color=(1, 0.34, 0.20, 1),
                             font_size=18,
                             color=(1, 1, 1, 1),
                             background_normal='',
                             background_down='')
        btn_voltar.bind(on_press=self.voltar)  # Bind para voltar
        layout.add_widget(btn_voltar)

        scroll_view.add_widget(layout)  # Adiciona o layout ao ScrollView
        self.add_widget(scroll_view)  # Adiciona o ScrollView à tela

    def abrir_categoria(self, instance):
        # Vamos adicionar uma lógica simples para identificar a categoria e trocar para a tela correta
        categoria = instance.text.lower().replace(' ', '_')
        self.manager.current = categoria

    def voltar(self, instance):
        self.manager.current = 'main'  # Volta para a tela principal

class CategoriaScreen(Screen):
    def __init__(self, **kwargs):
        super(CategoriaScreen, self).__init__(**kwargs)
        layout = FloatLayout()  # Usando FloatLayout para posicionamento

        # Exemplo de imagem e descrição
        img_produto = Image(source='C:\\Users\\tceno\\OneDrive\\Área de Trabalho\\MEUS-TRABALHOS\\FOTUS\\produtos\\bebida.jpg',
                            size_hint=(0.5, 0.5),
                            pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(img_produto)

        descricao_produto = Label(text='Descrição da bebida aqui.',
                                  size_hint=(0.8, 0.2),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(descricao_produto)

        # Botão para voltar ao cardápio
        btn_voltar = Button(text='Voltar', size_hint=(0.8, 0.1),
                             background_color=(1.0, 0.34, 0.20, 1),
                             pos_hint={'center_x': 0.5, 'y': 0.05})
        btn_voltar.bind(on_press=self.voltar)
        layout.add_widget(btn_voltar)

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'cardapio'  # Volta para a tela do cardápio

class MyApp(App):
    def build(self):
        # Adiciona a transição Fade ao ScreenManager
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name='main'))  # Tela principal
        sm.add_widget(CardapioScreen(name='cardapio'))  # Tela do cardápio
        # Adiciona telas para cada categoria
        categorias = [
            'à_la_carte', 'churrascos', 'tira_gosto', 'cerveja_600ml',
            'cervejas_long_neck', 'pratos_executivos', 'torres', 'combos', 'salgados'
        ]
        for categoria in categorias:
            sm.add_widget(CategoriaScreen(name=categoria))
        return sm

if __name__ == '__main__':
    MyApp().run()
