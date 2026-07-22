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

try:
    driver.get("https://sso.hotmart.com/login")
    print("[AÇÃO] Login manual...")
    time.sleep(40)

    driver.get("https://hotmart.com/pt-br/marketplace")

    curso = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/marketplace/produtos/']"))
    )
    driver.execute_script("arguments[0].click();", curso)

    botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='btn-buy']")))
    driver.execute_script("arguments[0].click();", botao)

    wait.until(EC.presence_of_element_located((By.XPATH, "//input")))

    # NÃO PREENCHE NADA
    botao = wait.until(EC.element_to_be_clickable((By.ID, "payment-button")))
    botao.click()

    time.sleep(3)

    if "obrigatório" in driver.page_source.lower() or "preencha" in driver.page_source.lower():
        print("[OK] CT_009 PASSOU")
    else:
        print("[FAIL] CT_009 FALHOU")

except Exception as e:
    print("[ERROR]", e)

finally:
    time.sleep(5)
    driver.quit()