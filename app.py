# Desafio da confirmação de dados + salvar em bloco de notas
import pyautogui

# Qual o email do usuário
email = pyautogui.prompt(text='Digite seu e-mail:', title='Confirmação de Login')
print(email)
# Qual a senha do usuário
senha = pyautogui.password(text='Digite sua senha:', title='Confirmação de Login',mask='*')
print(senha)
# Clicar no bloco e colar senha e email
pyautogui.click(1234,323,duration=2)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)