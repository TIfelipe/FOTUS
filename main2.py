from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()  # Usando FloatLayout para permitir o posicionamento flexível
        
        # Adiciona a logomarca e faz com que ela ocupe todo o espaço
        logo = Image(source='C:\\Users\\tceno\\OneDrive\\Área de Trabalho\\MEUS-TRABALHOS\\FOTUS\\logomarca.jpg', 
                     allow_stretch=True,  
                     keep_ratio=False,    
                     size_hint=(1, 1))    
        layout.add_widget(logo)
        
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
        layout = GridLayout(cols=1, size_hint_y=None)  # GridLayout para armazenar os botões
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
                                   background_color=(0.1, 0.5, 0.8, 1))
            layout.add_widget(btn_categoria)

        # Botão para voltar
        btn_voltar = Button(text='Voltar', size_hint=(1, None), 
                            height=50, 
                            background_color=(1, 0.34, 0.20, 1))
        btn_voltar.bind(on_press=self.voltar)  # Bind para voltar
        layout.add_widget(btn_voltar)

        scroll_view.add_widget(layout)  # Adiciona o layout ao ScrollView
        self.add_widget(scroll_view)  # Adiciona o ScrollView à tela

    def voltar(self, instance):
        self.manager.current = 'main'  # Volta para a tela principal

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))  # Tela principal
        sm.add_widget(CardapioScreen(name='cardapio'))  # Tela do cardápio
        return sm

if __name__ == '__main__':
    MyApp().run()
