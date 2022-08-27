from selenium import webdriver


#structura link
produs = 'samsung'
pagina = 1
baseLink = 'https://www.emag.ro/search/'

link = baseLink + produs+'/' +'p'+ str(pagina)

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver', chrome_options = options)

def get_chrome_web_options():
    return webdriver.ChromeOptions()

def get_chrome_web_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    return options

def get_chrome_web_icognito(options):
    options.add_argument('--incognito')
    return options 