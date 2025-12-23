from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
import pyautogui
from pathlib import Path
import os, time, datetime
from dotenv import load_dotenv
import subprocess; 

class InstaFollow:
    def __init__(self):
        """using selenium: build an object, we could work on it with selenium on Instagram.com"""
        load_dotenv()
        subprocess.call('cls', shell=True)
        self.INSTAGRAM_URL = "https://www.instagram.com/"
        self.INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
        self.INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')
        self.TARGET_URL = os.environ.get("SIMILAR_ACCOUNT")
        ## BUILD A DRIVER FOR FIREFOX 
        self.driver = Firefox(options=FirefoxOptions())
        self.driver.maximize_window()
        self.install_veepn()
        self.login_instagram()
        self.find_followers(target_url=self.TARGET_URL)
        self.follow_procedure()

    def highlight(self, element):
        """get an element as arg, and put a red border on it in web browser to see it visualy. after 2s removes it"""
        driver = element._parent
        ## STORE CURRENT STYLE TO RESTORE IT LATER
        original_style = element.get_attribute('style')
        
        ## ADD A RED BORDER ON THAT SPECIFIC ELEMENT
        driver.execute_script("arguments[0].setAttribute('style', 'border: 2px solid red;padding:5px;');", element)
        
        ## FREEZ CODE FOR 2 SECOND TO SEE IT IN WEB BROWSER
        time.sleep(1)
        
        ## GET BACK TO ORIGIN STYLE
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)

#TODO: replace every switch code with this method
    def switch_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def install_veepn(self):
        """installs 'Veepn' extension to firefox driver from files exist in main profile of user."""
        self.veepn_ID = r'{94ed9bbf-a1e2-4e58-81ae-cd16dad818d8}'
        self.extention_veepn_fp = Path(
            fr"C://Users/{os.environ.get("USERNAME")}/AppData/Roaming/Mozilla/Firefox/Profiles/vx6mst7r.default-release/extensions/{self.veepn_ID}.xpi"
            ).resolve()
        self.driver.install_addon(
            path= self.extention_veepn_fp
        )
        #add wait to load
        WebDriverWait(driver= self.driver, timeout=30, poll_frequency=1).until(
            EC.new_window_is_opened(self.driver.window_handles)
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(driver= self.driver, timeout=30, poll_frequency=1).until(
            EC.all_of( 
                ## 1.wait for first tick 
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.app__container")
                ),
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "span.checkbox__box")
                ),          
                ## 2.wait for accept btn
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "app__accept")
                )
            )
        )

        ## FILL THE TICKS FOR VEEPN
        self.checkboxs = self.driver.find_elements(By.CSS_SELECTOR, "span.checkbox__box") 
        for i in self.checkboxs: ##tick all 
            i.click()
        ## CLICK ON 'ACCEPT' BTN
        self.driver.find_element(By.CLASS_NAME, "app__accept").click()

        ## use 'pyautogui' library and automate clicking and enabling veepn
        img_dir = (Path(__file__).parent/'img').resolve()
        confidence_level = 0.8

        ## find and click on 'puzzle_logo.img'
        puzzle_btn_fp = img_dir/'1.puzzle_logo.png'
        puzzle_btn_generator = pyautogui.locateAllOnScreen(
            puzzle_btn_fp.resolve()._str,
            confidence= confidence_level,
            grayscale= False,
        )
        puzzle_btns = list(puzzle_btn_generator)
        pyautogui.click(
            pyautogui.center(puzzle_btns[0])
        )

        ## find and click on '2.disabled_extension_click.png'
        disabled_extension_click_fp = img_dir/'2.disabled_extension_click.png'
        disabled_extension_click_generator = pyautogui.locateAllOnScreen(
            disabled_extension_click_fp.resolve()._str,
            confidence= confidence_level,
            grayscale= False,
        )
        disabled_extension_click_btn = list(disabled_extension_click_generator)
        pyautogui.click(
            pyautogui.center(disabled_extension_click_btn[0])
        )

        ##wait 3 seconds to open...
        time.sleep(3)

        ## find and click on '3.continue_btn.png'
        continue_btn_fp = img_dir/'3.continue_btn.png'
        continue_btn_generator = pyautogui.locateAllOnScreen(
            continue_btn_fp.resolve()._str,
            confidence= confidence_level,
            grayscale= False,
        )
        continue_btn = list(continue_btn_generator)
        pyautogui.click(
            pyautogui.center(continue_btn[0])
        )
        ##repeat click for '4.start_btn.png'
        time.sleep(0.1)
        pyautogui.click(
            pyautogui.center(continue_btn[0])
        )

        ##find and click on '5.login_btn.png'
        login_btn_fp = img_dir/'5.login_btn.png'
        login_btn_generator = pyautogui.locateAllOnScreen(
            login_btn_fp.resolve()._str,
            confidence= confidence_level,
            grayscale=False,
        )
        login_btn = list(login_btn_generator)
        pyautogui.click(
            pyautogui.center(login_btn[0])
        )

        ##find and click on '6.tick_btn.png'
        tick_btn_fp = img_dir/'6.tick_btn.png'
        tick_btn_generator = pyautogui.locateAllOnScreen(
            tick_btn_fp.resolve()._str,
            confidence= confidence_level,
            grayscale=False,
        )
        tick_btn = list(tick_btn_generator)
        pyautogui.click(
            pyautogui.center(tick_btn[0])
        )
        
        time.sleep(1)

        ##find and click on '7.select_server_btn.png'
        select_server_btn_fp = img_dir/'7.select_server_btn.png'
        select_server_btn_generator = pyautogui.locateAllOnScreen(
            select_server_btn_fp.resolve()._str,
            confidence= 0.5,
            grayscale=False,
        )
        select_server_btn = list(select_server_btn_generator)
        pyautogui.click(
            pyautogui.center(select_server_btn[0])
        )

        time.sleep(1)

        ##find and click on '8.UK_server_btn.png'
        UK_server_btn_fp = img_dir/'8.UK_server_btn.png'
        UK_server_btn_generator = pyautogui.locateAllOnScreen(
            UK_server_btn_fp.resolve()._str,
            confidence= confidence_level,
            grayscale=False,
        )
        UK_server_btn = list(UK_server_btn_generator)

        pyautogui.click(
            pyautogui.center(UK_server_btn[0])
        )

        time.sleep(1)

        ##find and click on '9.connect_btn.png'
        connect_btn_fp = img_dir/'9.connect_btn.png'
        connect_btn_generator = pyautogui.locateAllOnScreen(
            connect_btn_fp.resolve()._str,
            confidence= confidence_level,
            grayscale=False,
        )
        connect_btn = list(connect_btn_generator)
        pyautogui.click(
            pyautogui.center(connect_btn[0])
        )

        ## CHECK WITH PYAUTOGUI VEEPN CONNECTED OR NOT
        # img_dir = (Path(__file__).parent/'img').resolve()
        connected_img_fp = img_dir/'10.check_connect.png'
        is_connected = False
        while not is_connected:
            if bool(pyautogui.locateOnScreen(
                image= connected_img_fp.resolve()._str,
                grayscale=False,
                confidence=0.8,)
                ):
                is_connected = True
                time.sleep(2)
            else: 
                time.sleep(2)  
        self.driver.switch_to.window(self.driver.window_handles[-1])        

    def login_instagram(self):
        """login to instagram"""
        ## LOAD INSTAGRAM PAGE
        try:
            self.driver.get(self.INSTAGRAM_URL)
        except WebDriverException:
            time.sleep(5)
            self.driver.get(self.INSTAGRAM_URL)
        self.switch_last_window()
        ## WAIT FOR PAGE TO LOAD
        WebDriverWait(driver= self.driver, timeout= 30, poll_frequency= 2).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "_a9--")
            )
        )

        ## CLICK ON DECLINE COOKIES
        self.driver.find_element(by= By.CLASS_NAME, value= "_a9--").click()
        time.sleep(3)

        ### FILL INFORMATIONS
        ## CHECK WHAT KIND OF LOGIN FORM WE HAVE, USE THAT ONE
        try: # check for #login_form
            self.driver.find_element(by= By.CSS_SELECTOR, value= "#login_form")
            value_to_get_login_form = "#login_form"
            value_to_get_username_input = 'Mobile number, username or email'
        except NoSuchElementException: 
            value_to_get_login_form = "#loginForm"
            value_to_get_username_input ='Phone number, username, or email'

        ## GET LOGIN FORM DIV FIRST TO GET ANOTHERs WITH IT
        instagram_login_form = self.driver.find_element(by= By.CSS_SELECTOR, value= f"{value_to_get_login_form}")
            # instagram_login_form = self.driver.find_element(by= By.CSS_SELECTOR, value= "#loginForm").find_elements(By.CSS_SELECTOR, "div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")[0]
        
        ## GET username_input FROM instagram_login_form
        username_input = instagram_login_form.find_element(By.XPATH, fr"//*[contains(text(),'{value_to_get_username_input}')]").find_element(By.XPATH, "..").find_element(By.CSS_SELECTOR, "input") # first get a label tag with given string, then get parent of that tag, then looking for an input in it.
            # username_input = instagram_login_form.find_elements(
            #     by= By.CSS_SELECTOR,
            #     value= "._aa4b"
            # )[0]

        ## GET password_input FROM instagram_login_form
        password_input = instagram_login_form.find_element(By.XPATH, "//*[contains(text(),'Password')]").find_element(By.XPATH, "..").find_element(By.CSS_SELECTOR, "input")
            # password_input = instagram_login_form.find_elements(
            #     by= By.CSS_SELECTOR,
            #     value= "._aa4b"
            # )[1]

        ## GET login_btn FROM instagram_login_form 
        all_logins_in_form = instagram_login_form.find_elements(By.XPATH, "//*[contains(text(),'Log in')]")
        for log_in in all_logins_in_form:
            ## LOOP IN ALL LOGINS WHICH IS IN instagram_login_form AND GET THAT ONE IS EQUAL TO 'LOG IN'
            if log_in.get_attribute('innerHTML').lower() == 'log in':
                login_btn = log_in 
            # login_btn = None
            # for div in instagram_login_form.find_elements(By.CSS_SELECTOR,"div"):
            #     if div.get_attribute('innerHTML').lower() == "log in":
            #         login_btn = div
            #     else: 
            #         pass

        # FILL USERNAME INTO username_input
        username_input.send_keys(self.INSTAGRAM_USERNAME)

        # FILL PASSWORD INTO password_input
        password_input.send_keys(self.INSTAGRAM_PASSWORD)

        ## PUSH 'LOGIN' BTN
        time.sleep(1)
        login_btn.click()
        time.sleep(7)
        try:
            if self.driver.find_element(By.XPATH, "//*[contains(text(), 'There was a problem logging you into Instagram. Please try again soon.')]"):
                time.sleep(5)
                login_btn.click()
        except:
            pass
        # TODO : figure out for try again soon error codes function right
                # try:
                #     self.driver.find_element(By.XPATH, "//*[contains(text(), 'There was a problem logging you into Instagram. Please try again soon.')]")
                # except:
                #     pass
                # else: 
                #     time.sleep(5)
                #     login_btn.click()
                
        ## WAIT 5SEC FOR ERROR, AND IF OCCURED: BREAK AND RUN AGAIN
        time.sleep(5)
        self.switch_last_window()
        # TODO: check this 2 try-except function right
        try: # for recaptcha
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'Help us confirm it's you')]")
            input("RECAPTCHA CHECK! DO IT MANUALY THE COME BACK AND HIT ANY BUTTON...")
        except: 
            pass
        
        try: # for reload page and login failed or something 
            self.driver.find_element(
                By.XPATH, "//*[contains(text(), 'Something went wrong')]"
            )
            return self.login_instagram()
        except:
            pass

        ## wait to load page which ask for 'save information' 
        WebDriverWait(driver= self.driver, timeout=200, poll_frequency= 2).until(
            EC.url_contains("/accounts/onetap")
        )
        # then click on 'Not now'
        self.click_string_now('Not now')

        ## wait to load primary instagram page 
        WebDriverWait(driver= self.driver, timeout=200, poll_frequency=2).until(
            EC.url_to_be(self.INSTAGRAM_URL)
        )
        print(f"Successfully Logged in INSTAGRAM\nuser:\t<{self.INSTAGRAM_USERNAME}>")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def find_followers(self, target_url):
        """by loading target_url instagram page, click on 'followers' part and open followers list, ready to push follow each by each"""
        ## GET TO TARGET PAGE
        self.driver.get(target_url)
        ## CHECK FOR EXISTENCE OF 'FOLLOWER' PANE 
        WebDriverWait(driver= self.driver, timeout=30, poll_frequency=1).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), 'follower')]")
                )
        )
        ## CLICK ON FOLLOWER PANE TO OPEN FOLLOWERS PAGE SCROLLING
        self.driver.find_element(by= By.XPATH, value="//*[contains(text(), 'followers')]").click() # TODO: could be just target_url/followers and continue : comment out webdriverwait above and below (just check with exact url), and change get() with 'target_url/followers' string

        ## CHECK FOR FOLLOWER PANE OPENED OR NOT
        WebDriverWait(driver= self.driver, timeout= 30, poll_frequency= 1).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe")
                )
        )

        ## STORE FOLLOWERS LOCATOR AS A ATTRIBUTE
            # self.followers_pane = self.driver.find_element(
            #     By.CLASS_NAME, value="x7r02ix.x15fl9t6.x1yw9sn2.x1evh3fb.x4giqqa.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe"
            # )

        ## PRINT IN CONSOLE FOLLOWER PAGE IS OPENED NOW FOR TARGET_URL
        print(f'\nFollower scrol page opened!\ntarget_url:\t<{target_url}>')

    def click_string_now(self, string):
        """click on very first given string in page, NOTICE: its case sensitive"""
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(by= By.XPATH, value= fr"//*[contains(text(), '{string}')]").click()

    def follow_procedure(self):
        """start following from 'self.followers_pane', each by each"""
        self.switch_last_window()

        ## WAIT TO LOAD FOLLOWERS
        WebDriverWait(driver= self.driver, timeout=30, poll_frequency=1).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.x1qnrgzn.x1cek8b2.xb10e19.x19rwo8q.x1lliihq.x193iq5w.xh8yej3")
                )
        )
        
        ## CATCH THE ELEMENTS OF FOLLOWERS
                # followers_div = self.followers_pane.find_elements(By.CSS_SELECTOR, "div.html-div.xdj266r.x14z9mp.xat24cr.x1lziwak.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xv54qhq.xf7dkkf.xwib8y2.x1y1aw1k.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
            # TODO: just check for next follower exist in xpath find for 'followers' , follow all
            # TODO: followers_div must renew with ending first phase, figure .
                # for div in followers_div:
                #     ## THE LAST DIV EXISTING, IS FOLLOW BUTTON
                #     follow_btn = div.find_elements(By.CSS_SELECTOR, "div")[-1]

                #     ## check if follow btn is 'following' right now
                #     if 'following' == follow_btn.text.lower() or 'requested' == follow_btn.text.lower():
                #         continue

                #     follow_btn.click()

        print()


