from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as DT
import pandas as pd

stage = 'https://stage2.co.fi/register'
crm_stage = 'https://crm.stage2.co.fi/'

crm_login = ''
crm_pass = ''
file_1 = 'C:/cover.png'
file_2 = 'C:/selenium-csharp.jpg'

driver = webdriver.Chrome()
driver.get(stage)
driver.maximize_window()
time.sleep(1)

# Открытие mailinator, создание почты!
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://www.mailinator.com/site/verified-pro-plan/')

# Функция рандомных значений email
random_email = (''.join(random.choice(string.ascii_lowercase) for i in range(12)))

# Ввод в mailinator рандомных данных
mailinator_mail = driver.find_element(By.XPATH, '/html/body/div[1]/header[1]/div[1]/div/div/div[1]/div/input')
mailinator_mail.send_keys(random_email)
mailinator_go = driver.find_element(By.XPATH, '/html/body/div[1]/header[1]/div[1]/div/div/div[1]/div/button').click()
time.sleep(1)

# Копирование email
copy_email = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/div[5]/input')
actionchains = ActionChains(driver)
actionchains.double_click(copy_email).perform()
copy_email.send_keys(Keys.CONTROL + 'C')
driver.switch_to.window(driver.window_handles[0])

# Клик по радио-кнопке "Инвестор"
radio_button_investor = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[1]/label[2]/div[2]')
radio_button_investor.click()

# Ввод в поле Email
email_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/div/div/input')
email_input.send_keys(Keys.CONTROL + 'V')
email_input.send_keys('@mailinator.com')

# Ввод в поле пароль
password_input = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[3]/div/div/input')
password_input.send_keys('Password1')

# Ввод в поле повторите пароль
password_input = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[4]/div/div/input')
password_input.send_keys('Password1')

# Клик на чек-бокс Я ознакомлен с правилами
check_box_1 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[5]/div[1]/label/div[1]')
check_box_1.click()

# Клик на чек-бокс Я согласен на обработку
check_box_2 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[5]/div[2]/label/div[1]')
check_box_2.click()

# Клик на чек-бокс Я согласен на получение
check_box_3 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[5]/div[3]/label/div[1]')
check_box_3.click()

# Клик по кнопке Зарегестрироваться
register_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[1]/form/button')
register_1.click()

# Подтверждение почты в mailinator
driver.switch_to.window(driver.window_handles[1])

wait = WebDriverWait(driver, 20)
register_latter = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div[3]/div/div[4]/div/div/table/tbody/tr/td[2]')))
register_latter.click()
time.sleep(0.3)
tab_links = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div[3]/ul/li[5]/a')
tab_links.click()
register_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '/auth/verification' and '/email/verify')))
register_link.click()

# Переключение на вкладку регистрации
driver.switch_to.window(driver.window_handles[2])

# Клик по кнопке Заполнить
filling = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/main/div/div/div[1]/div/div/button')))
filling.click()

# Клик по чек боксу "ФЛ"
check_box_FL = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[1]/form/div/label[1]/div[1]')))
check_box_FL.click()

# Отключение стиля display в инпутах пасспортов
driver.execute_script(
    "document.querySelectorAll('.file-input__field input').forEach(field => {field.style.display = 'block'});")

# Добавление фото в инпут 1
input_passport1 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/div[1]/div[2]/label/input')))
input_passport1.send_keys(file_1)

# Добавление фото в инпут 2
input_passport2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/div[2]/div[2]/label/input')))
input_passport2.send_keys(file_2)
time.sleep(1)

# Функция рандома номера телефона
random_phone_number = [random.randint(100000000, 999999999) for i in range(1)]

# Ввод номера телефона
input_number = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/div[3]/div/div/input')
input_number.send_keys('9', str(random_phone_number))

# Чек бокс Я не являюсь публичным
check_box_4 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/div[4]/div[1]/label/div[1]')
check_box_4.click()

# Чек бокс Я не являюсь иностранным
check_box_5 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/div[4]/div[2]/label/div[1]')
check_box_5.click()

# Скролл
driver.execute_script("window.scrollTo(0, 500)")

# Кнопка отправить
send = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[1]/form/div[2]/button')
send.click()

# СМС подтверждение
sms_check_1 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[1]')))
sms_check_2 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[2]')
sms_check_3 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[3]')
sms_check_4 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[4]')

sms_check_1.send_keys(1)
sms_check_2.send_keys(1)
sms_check_3.send_keys(1)
sms_check_4.send_keys(1)

# Переключение на вкладку CRM
driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get(crm_stage)

# Ввод логин/пароль
email_input = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div/main/div/div/div[1]/div/form/div[1]/div/div[1]/div/input')))
pass_input = driver.find_element(By.XPATH,
                                 '/html/body/div/div/main/div/div/div[1]/div/form/div[2]/div/div[1]/div/input')
email_input.send_keys(crm_login)
pass_input.send_keys(crm_pass)

# Кнопка войти
login = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div[1]/div/form/button')
login.click()

# Открытие меню
menu = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/header/div/div/div[1]/button')))
menu.click()

# Клик по кнопке "Модерация"
moderation = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[1]/nav/div[1]/div/div/div[1]/div[1]')))
moderation.click()

# Клик по кнопке "Пользователи"
user_moderation = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[1]/nav/div[1]/div/div/div[1]/div[2]/a[1]')))
user_moderation.click()

# Клик по дропдауну "Статус"
select_status = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       '//*[@id="app"]/div/div[1]/main/div/div/div[2]/div/div/div/div/form/div[1]/div[4]/div/div/div/div/div[1]/div[1]')))
select_status.click()

# Клик по статусу "На модерации"
status_on_modarate = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]')))
status_on_modarate.click()

# Клик по кнопке "Поиск"
search = driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[1]/main/div/div/div[2]/div/div/div/div/form/div[1]/div[7]/div/button')
search.submit()

# Клик по фильтру "Поступление на модерацию"
moderation_time = driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[1]/main/div/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[5]/span')
moderation_time.click()
time.sleep(1)
moderation_time.click()

# Клик по первому юзеру в таблице
first_user = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div/div/div[1]/table/tbody/tr[1]/td[7]/span/span')))
first_user.click()

#############  **ФУНКЦИИ РАНДОМНЫХ ДАННЫХ**  ##################################
# Рандом имени
list_name = ["Андрей", "Алексей", "Игорь", "Илья", "Вадим", "Бенджамин", "Валентин", "Василий", "Аркадий", "Артем",
             "Вячеслав", "Влад", "Анатолий", "Артур", "Владислав", "Данил", "Джонатан", "Дмитрий", "Дамир", "Евгений",
             "Иван"]
random_name_index = random.randint(0, len(list_name) - 1)

# Рандом фамилии
list_surname = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Козлов",
                "Новиков", "Морозов", "Волков", "Соловьёв", "Васильев", "Зайцев", "Павлов", "Семёнов", "Голубев",
                "Виноградов", "Богданов", "Воробьёв", "Фёдоров", "Михайлов", "Беляев"]
random_surname_index = random.randint(0, len(list_surname) - 1)
##########################################################################


# Ввод в поле "Фамилия"
surname_input = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       '/html/body/div/div/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[1]/div[1]/div/div[1]/div/input')))
time.sleep(1)
surname_input.send_keys(list_surname[random_surname_index])

# Ввод в поле "Имя"
name_input = driver.find_element(By.XPATH,
                                 '/html/body/div/div/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[2]/div[1]/div/div[1]/div/input')
name_input.send_keys(list_name[random_name_index])

# Выбор пола
choice_sex = driver.find_element(By.XPATH,
                                 '//*[@id="personal_information_block"]/div/div/form/div[1]/div[4]/div/div/div[1]/div[1]/div[2]/div/i')
choice_sex.click()
time.sleep(0.2)
male = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]')
male.click()

############# **ФУНКЦИЯ РАНДОМА ДАТЫ РОЖДЕНИЯ** ###############################
start_birth_date = DT.datetime(1935, 8, 5)
end_birth_date = DT.datetime(2002, 7, 28)

random_date = pd.date_range(
    min(start_birth_date, end_birth_date),
    max(start_birth_date, end_birth_date)
).strftime('%d%m%Y').tolist()
random_birth_date = random.choice(random_date)
###############################################################################


# Ввод даты рождения
birth_date = driver.find_element(By.XPATH,
                                 '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[5]/div[1]/div/div[1]/div/input')
birth_date.send_keys(random_birth_date)

# Ввод серии/номера паспорта
passport_ser_num = driver.find_element(By.XPATH,
                                       '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div[1]/div/div/div[1]/div/input')
passport_ser_num.send_keys('1111111111')

# Ввод кода подразделения
code_of_state = driver.find_element(By.XPATH,
                                    '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div[2]/div[1]/div/div[1]/div/input')
code_of_state.send_keys(random.randint(1, 85))

show_states = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="personal_information_block"]/div/div/form/div[3]/div[2]/div[1]')))
show_states.click()

choice_state = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div/div[1]')))
choice_state.click()

##################### **ФУНКЦИЯ РАНДОМА ДАТЫ ВЫДАЧИ ПАСПОРТА**#############################################
start_date_of_issue = DT.datetime(2000, 8, 5)
end_date_of_issue = DT.datetime(2022, 2, 28)

random_passport_issue_date = pd.date_range(
    min(start_date_of_issue, end_date_of_issue),
    max(start_date_of_issue, end_date_of_issue)
).strftime('%d%m%Y').tolist()
random_issue_date = random.choice(random_passport_issue_date)
############################################################################################################

# Ввод даты выдачи паспорта
date_issue = driver.find_element(By.XPATH,
                                 '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div[3]/div[1]/div/div[1]/div/input')
date_issue.send_keys(random_issue_date)

# Ввод в поле место рождения
place_of_birth = driver.find_element(By.XPATH,
                                     '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div[4]/div/div/div[1]/div/input')
cities = ['Москва', 'Санкт-Петербург', 'Тверь', 'Ростов', 'Новосибирск', 'Екатеринбург', 'Калининград', 'Мурманск',
          'Самара', 'Тольятти']
random_city = random.randint(0, len(cities) - 1)
place_of_birth.send_keys(cities[random_city])

# Ввод в поле адрес регистрации
registration_address = driver.find_element(By.XPATH,
                                           '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div[6]/div[1]/div/div[1]/div/input')
addresses = ['Москва', 'Санкт-Петербург', 'Тверь', 'Ростов', 'Новосибирск', 'Екатеринбург', 'Калининград', 'Мурманск',
             'Самара', 'Тольятти']
random_address = random.randint(0, len(addresses) - 1)
registration_address.send_keys(addresses[random_address])

# Ввод в поле фактический адресс
fact_address = driver.find_element(By.XPATH,
                                   '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div[7]/div[1]/div/div[1]/div/input')
fact_address.send_keys(addresses[random_address])

# Скролл
driver.execute_script("window.scrollTo(0, 500)")

# Открытие генератора ИНН, КОПИРОВАНИЕ ИНН
driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get('https://www.random1.ru/generator-inn-snils-oms-ogrn-kpp')
copy_inn = driver.find_element(By.XPATH, '//*[@id="inn_fiz"]')
actionchains = ActionChains(driver)
actionchains.double_click(copy_inn).perform()
copy_inn.send_keys(Keys.CONTROL + 'C')
driver.switch_to.window(driver.window_handles[3])

# ВВОД В ПОЛЕ ИНН
inn_input = driver.find_element(By.XPATH,
                                '/html/body/div/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/form/div[4]/div[1]/div/div/div[1]/div/input')
inn_input.send_keys(Keys.CONTROL + 'V')

# РАДИОКНОПКА ПАССПОРТ ДЕЙСТВИТЕЛЕН
radio_button_passport = driver.find_element(By.XPATH,
                                            '//*[@id="personal_information_block"]/div/div/form/div[6]/div[2]/div/div/div[1]/div/div[1]/div/div')
radio_button_passport.click()

# Скролл
driver.execute_script("window.scrollTo(0, 1500)")

# ВЫБОР СТАТУСА
user_status_change = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div/div/div[1]/div[1]/div[1]')
user_status_change.click()
user_status_checked = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/div/div[3]/div')))
user_status_checked.click()

# КНОПКА ПРИМЕНИТЬ
confirm_button = driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[1]/main/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/div[3]/div[2]/div/div/button[2]')
confirm_button.click()
time.sleep(1.5)

# Преключение на стейдж
driver.switch_to.window(driver.window_handles[2])
time.sleep(3)
driver.refresh()

# Клик по чек боксу
check_box_6 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[3]/div[3]/div/div[1]/div/div/label/div[1]')))
check_box_6.click()

# Клик по кнопке Подписать
sign_dec = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'declaration__button')))
sign_dec.click()

# СМС подтверждение декларации
sms_check_5 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[1]')))
sms_check_6 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[2]')
sms_check_7 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[3]')
sms_check_8 = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div[4]/form/div[2]/input[4]')

sms_check_5.send_keys(1)
sms_check_6.send_keys(1)
sms_check_7.send_keys(1)
sms_check_8.send_keys(1)
time.sleep(5)

menu_title = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/header/div/div/nav/div/div'))).click()
show_email = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/div/header/div/div/nav/div/div/div[3]/div[1]/div[2]')
time.sleep(1)
print_email = show_email.text
print_password = 'Password1'
print(print_email)
print(print_password)
time.sleep(5)
driver.quit()
