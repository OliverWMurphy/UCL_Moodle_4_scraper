from scrapy.selector import Selector
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import  argparse


######################################
#Functions to run main
def get_elements_by_xpath(html,xpath):
    sel = Selector(text = html)
    elements_sel = sel.xpath(xpath)
    elements = elements_sel.extract()
    return elements

def get_html(browser,url):
    browser.set_page_load_timeout(60)
    browser.get(url)
    html = browser.page_source
    
    return browser,html

def start_firefox(options):
    
    if options == 'default':
        options = Options()
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # Specify the MIME type for PDF files
        options.set_preference("pdfjs.disabled", True)  # Disable the built-in PDF viewer
    
    elif type(options) != type(Options()):
        raise TypeError('options argument must be either "default" or an instance of a selenium.webdriver.firefox.options.Options object')
    
    browser = webdriver.Firefox(options=options)
    
    return browser

def moodle_login(browser , email , password ):
    EMAILFIELD = (By.ID, "i0116")
    PASSWORDFIELD = (By.ID, "i0118")
    NEXTBUTTON = (By.ID, "idSIButton9")
    LOGIN = (By.XPATH,'//a[@href="https://moodle.ucl.ac.uk/auth/oidc/"]/button[@class="loginbtn btn btn-secondary btn-block"]')
    
    browser.get("https://moodle.ucl.ac.uk/login/index.php")
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(LOGIN)).click()
    except:
        pass
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
    
    # Click Next  
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
     
    # wait for password field and enter password
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(password)
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    
    return browser
    

    
def get_surface_content(browser,url):
    
    browser,html = get_html(browser, url)
    
    xpath = '//a[contains(@href,"resource")]/@href'

    links = get_elements_by_xpath(html,xpath)
    #print(links)

    if len(links) == 0:
        print('Nothing to take')

    ###
    ### Download links
    browser.set_page_load_timeout(2)
       
    for link in links:
        try:
            browser.get(link)
        except:
            continue

def get_subfolder_content(browser,url):
    browser,html = get_html(browser, url)

    
    xpath = '//a[contains(@href,"folder")]/@href'
    DOWNLOAD = (By.XPATH,'//form[@action="https://moodle.ucl.ac.uk/mod/folder/download_folder.php"]/button')
 
    links = get_elements_by_xpath(html,xpath)
    print(links)

    for folder in links:
        browser.get(folder)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(DOWNLOAD)).click()
    return browser  

##############################    
       


def main():
    global args
    parser = argparse.ArgumentParser(description='Moodle 4 Scraper')
    parser.add_argument('url', nargs=1, help='url of the page')
    parser.add_argument('email', nargs=1, help='login email')
    parser.add_argument('password', nargs=1, help='login password')
    args = parser.parse_args()    
    
    url = args.url[0]
    email = args.email[0]
    password = args.password[0]
    options = 'default'

    browser = start_firefox(options)
    browser = moodle_login(browser,email,password)

    get_surface_content(browser, url)
    get_subfolder_content(browser, url)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass