from selenium import webdriver
import chromedriver_autoinstall
import time

class Navegador:
    def __init__(self) -> None:
        print('Configuração iniciada')
        
        chromedriver_autoinstall.install()
        self.driver = webdriver.Chrome()
        
        
    def configura_browser(self):
        print ("configura_browser")
        
    def open_window(self, url):
        try:
            self.driver.get(url)

        except Exception as e:
            print(f"Erro ao abrir a janela maximizada: {e}")
        finally:
            # Fechar o navegador ao finalizar
            #self.driver.quit()
            print('Terminou')
    
    def open_window_maximized(self, url):
        try:
            # Abrir uma URL qualquer
            self.driver.get(url)
            print("Abriu navegador")

            # Maximizar a janela
            self.driver.maximize_window()
            time.sleep(3)  # Aguarda por 15 segundos (você pode ajustar conforme necessário)
        except Exception as e:
            print(f"Erro ao abrir a janela maximizada: {e}")
        finally:
            # Fechar o navegador ao finalizar
            #self.driver.quit()
            print('Terminou')
            