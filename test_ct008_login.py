from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 40)

EMAIL = "zibteste01@gmail.com"

def preencher_se_existir(xpath, valor, nome):
    try:
        campo = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        campo.clear()
        campo.send_keys(valor)
        print(f"[INFO] {nome} preenchido")
    except:
        print(f"[INFO] {nome} não solicitado nesse checkout")

try:
    # 1. Login
    driver.get("https://sso.hotmart.com/login")
    print("[INFO] Página de login carregada")

    print("[AÇÃO NECESSÁRIA] Faça login manual e resolva o captcha...")
    time.sleep(40)

    if "login" in driver.current_url:
        raise Exception("Login não foi concluído")

    print("[INFO] Login realizado com sucesso")

    # 2. Marketplace
    driver.get("https://hotmart.com/pt-br/marketplace")
    print("[INFO] Marketplace carregado")

    # 3. Abrir curso
    curso = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href*='/marketplace/produtos/']")
        )
    )
    driver.execute_script("arguments[0].click();", curso)
    print("[INFO] Curso aberto")

    # 4. Botão carrinho
    botao_carrinho = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='btn-buy']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", botao_carrinho)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", botao_carrinho)

    print("[INFO] Clique no botão 'Ir para o carrinho'")

    # 5. Esperar checkout
    wait.until(EC.presence_of_element_located((By.XPATH, "//input")))
    print("[INFO] Checkout carregado")

    time.sleep(3)

    # 6. EMAIL
    campos_email = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@placeholder,'email')]")
        )
    )

    campos_email[0].send_keys(EMAIL)
    campos_email[1].send_keys(EMAIL)
    print("[INFO] Emails preenchidos")

    # 7. CAMPOS DINÂMICOS
    preencher_se_existir("//input[contains(@placeholder,'nome')]", "Davi Hudson Frazao", "Nome")
    preencher_se_existir("//input[contains(@placeholder,'CPF')]", "61706253338", "CPF")
    preencher_se_existir("//input[@id='PHONE']", "98984390654", "Telefone")

    # CAMPOS VARIÁVEIS
    preencher_se_existir("//input[contains(@placeholder,'CEP')]", "65000000", "CEP")
    preencher_se_existir("//input[contains(@placeholder,'Instagram')]", "@davi.teste", "Instagram")

    print("[INFO] Dados pessoais tratados")

    # =========================
    # IFRAME DO CARTÃO
    # =========================
    iframe = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[src*='credit-card-form']")
        )
    )

    driver.switch_to.frame(iframe)
    print("[INFO] Entrou no iframe do cartão")

    # 🔥 8. CARTÃO INVÁLIDO (CT_008)
    wait.until(EC.element_to_be_clickable((By.ID, "CARD_NUMBER"))).send_keys("1234567890123456")
    driver.find_element(By.ID, "CARD_EXPIRY_MONTH_YEAR").send_keys("00/00")
    driver.find_element(By.ID, "CARD_CVV").send_keys("000")
    driver.find_element(By.ID, "CARD_HOLDER").send_keys("Teste Invalido")

    print("[INFO] Cartão inválido preenchido")

    # sair do iframe
    driver.switch_to.default_content()

    # 9. COMPRAR
    botao_comprar = wait.until(
        EC.element_to_be_clickable((By.ID, "payment-button"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", botao_comprar)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", botao_comprar)

    print("[INFO] Clique em 'Comprar agora'")

    # 10. VALIDAÇÃO REAL (CT_008)
    time.sleep(5)

    erros = driver.find_elements(
        By.XPATH,
        "//*[contains(text(),'inválido') or contains(text(),'erro') or contains(text(),'recusado')]"
    )

    if len(erros) > 0:
        print("[OK] CT_008 PASSOU: pagamento recusado corretamente")
    else:
        print("[FAIL] CT_008 FALHOU: sistema não bloqueou pagamento inválido")

except Exception as e:
    print("[ERROR] Falha no teste")
    print("[ERROR] Detalhes:", e)

finally:
    time.sleep(10)
    driver.quit()