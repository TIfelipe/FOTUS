from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

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
        layout = FloatLayout()  # Usando FloatLayout para a tela do cardápio
        
        # Aqui você pode adicionar widgets para os tipos de pratos
        # Por exemplo, adicionar botões ou labels para diferentes categorias
        categoria_entrada = Button(text='Entradas', size_hint=(0.8, 0.1), 
                                   background_color=(0.1, 0.5, 0.8, 1), 
                                   pos_hint={'center_x': 0.5, 'center_y': 0.8})
        layout.add_widget(categoria_entrada)

        categoria_principal = Button(text='Pratos Principais', size_hint=(0.8, 0.1), 
                                     background_color=(0.1, 0.5, 0.8, 1), 
                                     pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(categoria_principal)

        categoria_sobremesa = Button(text='Sobremesas', size_hint=(0.8, 0.1), 
                                     background_color=(0.1, 0.5, 0.8, 1), 
                                     pos_hint={'center_x': 0.5, 'center_y': 0.4})
        layout.add_widget(categoria_sobremesa)

        # Botão para voltar
        btn_voltar = Button(text='Voltar', size_hint=(0.8, 0.1), 
                            background_color=(1, 0.34, 0.20, 1), 
                            pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_voltar.bind(on_press=self.voltar)  # Bind para voltar
        layout.add_widget(btn_voltar)

        self.add_widget(layout)

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
