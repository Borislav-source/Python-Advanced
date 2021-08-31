from selenium import webdriver as wd

driver = wd.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
url = 'https://www.emag.bg/laptopi/promo/filter/vid-laptop-f7882,gaming-v-17788/c?ref=dep_banner_2_1'

driver.get(url)

driver.maximize_window()

driver.implicitly_wait(5)

click = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[7]/div[4]/div[2]/div/div[3]/div[3]/form/button')
click.click()



url = 'https://www.emag.bg/laptopi/promo/filter/vid-laptop-f7882,gaming-v-17788/c?ref=dep_banner_2_1'

driver.get(url)

button2 = driver.find_element_by_xpath('/html/body/div[3]/nav[1]/div/div/div[3]/div/div[4]/a')
button2.click()


# url = 'https://www.emag.bg/cart/products?ref=cart'
#
# driver.get(url)

button3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[3]/a')
button3.click()