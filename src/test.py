from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/b.kravchenko/Desktop/CoursePython/chromedriver_win32/chromedriver.exe")

driver.get("https://www.wikipedia.org/")

search_field = driver.find_element(By.ID,"searchInput") # .send_keys("Test Automation") можно написать и тут а не отдельно
search_button = driver.find_element(By.XPATH,"//form[@id = 'search-form']/fieldset/button")

search_field.send_keys("Test Automation")  # ввести эти данные в поле
search_button.click()                      # команда нажатия на кнопку

# Верхними шагами мы перешли на нужную страницу, а теперь сделаем проверки, например проверим тайтл

assert "Test automation" in driver.title  # это означает (проверь что такое название в тайтл) метод ASSERT
driver.quit()






