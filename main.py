from browser.Navegador import Navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select

import time


instance = Navegador()  

info_login_oficial = {
    'user': "ramonss.bque@gmail.com",
    'senha': "Ramon@@1995"
} 

def faca_login_nerdin():
    url = "https://www.nerdin.com.br/login"
    instance.open_window_maximized(url)
    
    input_email = '//*[@id="cEmail"]'
    elemento_email = instance.driver.find_element(By.XPATH, input_email)
    elemento_email.send_keys(info_login_oficial['user'])
    
    input_senha = '//*[@id="cSenha"]'
    elemento_senha = instance.driver.find_element(By.XPATH, input_senha)
    elemento_senha.send_keys(info_login_oficial['senha'])

    botao = '//*[@id="btnContinuar"]'
    botao_login = instance.driver.find_element(By.XPATH, botao)
    botao_login.click()
    time.sleep(10)
    
def vai_para_tela_vagas():
    url = "https://www.nerdin.com.br/vagas"
    instance.open_window(url)

def search_jobs():
    time.sleep(2)
    input_search_jobs = instance.driver.find_element(By.XPATH, '//*[@id="PalavraChave"]')
    input_search_jobs.send_keys(".Net")
    input_search_jobs.send_keys(Keys.ENTER)
    
    time.sleep(3)
    
def select_jobs():
    elementos = instance.driver.find_elements(By.XPATH, "//*[contains(@id, 'divVagaConteudo')]")
    for elemento in elementos:
        
        print(elemento.text)
        elemento.click()
        time.sleep(3)
        
        #verificaElementoVagaIndisponível()
            
        botao_vaga = instance.driver.find_element(By.XPATH, '//*[@id="divListaVagas"]/div[2]/button')
        botao_vaga.click()
        
        time.sleep(3)
        
        input_nome = instance.driver.find_element(By.ID, "NomeCandidato")
        input_nome.clear()
        input_nome.send_keys("Ramon da Silva Santos")
            
        input_funcao = instance.driver.find_element(By.ID, "FuncaoCandidato")
        input_funcao.clear()
        input_funcao.send_keys("Dev Full Stack")    
        
        input_telefone = instance.driver.find_element(By.ID, "TelefoneCandidato")
        input_telefone.clear()
        input_telefone.send_keys("63981311589")    
        
        input_email = instance.driver.find_element(By.ID, "EmailCandidato")
        input_email.clear()
        input_email.send_keys("ramonss.bque@gmail.com")    
        
        input_cidade = instance.driver.find_element(By.ID, "CidadeCandidato")
        input_cidade.clear()
        input_cidade.send_keys("Palmas - TO")    
        
        input_disponibilidade_inicio = instance.driver.find_element(By.ID, "DisponibilidadeInicio")
        input_disponibilidade_inicio.clear()
        input_disponibilidade_inicio.send_keys("15")    
        
        input_pretensao_clt = instance.driver.find_element(By.ID, "ValorPretensaoSalarial")
        input_pretensao_clt.clear()
        input_pretensao_clt.send_keys("16000,00")    
        
        input_pretensao_pj_hora = instance.driver.find_element(By.ID, "ValorPretensaoSalarialPJ")
        input_pretensao_pj_hora.clear()
        input_pretensao_pj_hora.send_keys("120,00")    
        
        combo_possui_empresa = instance.driver.find_element(By.ID, "PossuiPJ")
        combo_possui_empresa = Select(combo_possui_empresa)
        combo_possui_empresa.select_by_visible_text("Sim")    
        
        combo_idioma = instance.driver.find_element(By.ID, "NivelIngles")
        combo_idioma = Select(combo_idioma)
        combo_idioma.select_by_visible_text("Advanced")   
        
        combo_atuacao_CSharp = instance.driver.find_element(By.ID, "VagaPalavraChave1")
        combo_atuacao_CSharp = Select(combo_atuacao_CSharp)
        combo_atuacao_CSharp.select_by_visible_text("Acima de 5 anos") 
        
        combo_atuacao_CSharp = instance.driver.find_element(By.ID, "VagaPalavraChave2")
        combo_atuacao_CSharp = Select(combo_atuacao_CSharp)
        combo_atuacao_CSharp.select_by_visible_text("Acima de 5 anos") 
        
        time.sleep(5)
        
        botao_enviar = instance.driver.find_element(By.ID, "btnSolicitar2")
        botao_enviar.click()
        
        instance.driver.back()
        
        time.sleep(1)
        instance.driver.back()
        time.sleep(5)
        # Executar o código
        
def verificaElementoVagaIndisponível():
    try:
        #verifica se a vaga está indisponível
        el_vaga_indisponivel = instance.driver.find_element(By.XPATH ,"//*[contains(text(), 'vaga indisponível')]")
        if el_vaga_indisponivel is not None:
            instance.driver.back()
    except (NoSuchElementException, ElementNotInteractableException):
        print("Elemento 'vaga indisponível ou não interável' não encontrado.")
        
try:
    faca_login_nerdin()
    vai_para_tela_vagas()
    
    search_jobs()
    
    select_jobs()
    time.sleep(10)
    
except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fechar o navegador
    instance.driver.quit()
    
    
