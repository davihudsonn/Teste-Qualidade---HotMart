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
    print("[INFO] Login")

    print("[AÇÃO] Faça login manual...")
    time.sleep(40)

    if "login" in driver.current_url:
        raise Exception("Login falhou")

    driver.get("https://hotmart.com/pt-br/marketplace")

    curso = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[href*='/marketplace/produtos/']")
        )
    )
    driver.execute_script("arguments[0].click();", curso)

    botao = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='btn-buy']"))
    )

    if botao:
        print("[OK] CT_006 PASSOU")
    else:
        print("[FAIL] CT_006 FALHOU")

except Exception as e:
    print("[ERROR]", e)

finally:
    time.sleep(5)
    driver.quit()