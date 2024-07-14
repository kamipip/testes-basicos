from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver
driver = webdriver.Firefox()

try:
    # Abre o navegador 
    driver.get('http://the-internet.herokuapp.com/login')
    
    # Encontra o campo de nome de usuário e insere um valor
    username = driver.find_element(By.ID, 'username')
    username.send_keys('tomsmith')
    
    # Encontra o campo de senha e insere um valor
    password = driver.find_element(By.ID, 'password')
    password.send_keys('SuperSecretPassword!')
    
    # Encontrar o botão de login e clicar nele
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
    login_button.click()
    
    # Aguarda o carregamento da página
    time.sleep(60)
    
    # Verificar se o login foi bem-sucedido
    success_message = driver.find_element(By.CSS_SELECTOR, 'div.flash.success')
    assert 'You logged into a secure area!' in success_message.text
    
    print("Teste de login bem-sucedido!")
    
except Exception as e:
    print(f"Teste falhou: {e}")

finally:
    # Fechar o navegador
    driver.quit()
