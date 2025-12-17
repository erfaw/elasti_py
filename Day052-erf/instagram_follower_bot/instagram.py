from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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
        ## BUILD A DRIVER FOR FIREFOX 
        self.driver = Firefox(options=FirefoxOptions())
        self.install_veepn()
        self.login_instagram()
        self.find_followers()

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
        self.driver.get(self.INSTAGRAM_URL)

        ## WAIT FOR PAGE TO LOAD
        WebDriverWait(driver= self.driver, timeout= 30, poll_frequency= 2).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "_a9--")
            )
        )

        ## CLICK ON DECLINE COOKIES
        self.driver.find_element(by= By.CLASS_NAME, value= "_a9--").click()
        time.sleep(3)

        ## FILL INFORMATIONS
        # GET LOGIN FORM DIV FIRST TO GET ANOTHER WITH IT
        instagram_login_form = self.driver.find_element(by= By.CSS_SELECTOR, value= "#loginForm").find_elements(By.CSS_SELECTOR, "div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")[0]
        # GET USERNAME_INPUT DIV
        username_input = instagram_login_form.find_elements(
            by= By.CSS_SELECTOR,
            value= "._aa4b"
        )[0]
        # GET PASSWORD INPUT DIV
        password_input = instagram_login_form.find_elements(
            by= By.CSS_SELECTOR,
            value= "._aa4b"
        )[1]
        # GET LOGIN BTN DIV (LOOP THROUGH ALL DIVS AND GET A DIV WHICH HAS 'LOG IN' IN IT)
        login_btn = None
        for div in instagram_login_form.find_elements(By.CSS_SELECTOR,"div"):
            if div.get_attribute('innerHTML').lower() == "log in":
                login_btn = div
            else: 
                pass

        # FILL USERNAME 
        username_input.send_keys(self.INSTAGRAM_USERNAME)

        # FILL PASSWORD
        password_input.send_keys(self.INSTAGRAM_PASSWORD)

        ## PUSH 'LOGIN' BTN
        time.sleep(1)
        login_btn.click()

        # TODO : figure out for try again soon error codes function right
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'try again soon')]")
        except NoSuchElementException:
            pass
        else: 
            time.sleep(5)
            login_btn.click()

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
        

    def find_followers(self, target_url="https://www.instagram.com/chefsteps/"):
        """find follower to follow"""
        ## GET TO TARGET PAGE
        self.driver.get(target_url)
        ## CHECK FOR EXISTENCE OF 'FOLLOWER' PANE 
        WebDriverWait(driver= self.driver, timeout=30, poll_frequency=1).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), 'follower')]")
                )
        )
        ## CLICK ON FOLLOWER PANE TO OPEN FOLLOWERS PAGE SCROLLING
        self.driver.find_element(by= By.XPATH, value="//*[contains(text(), 'followers')]").click()

        ## CHECK FOR FOLLOWER PANE OPENED OR NOT
        WebDriverWait(driver= self.driver, timeout= 30, poll_frequency= 1).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl"))
        )

        ## PRINT IN CONSOLE FOLLOWER PAGE IS OPENED NOW FOR TARGET_URL
        print(f'\nFollower scrol page opened!\ntarget_url:\t<{target_url}>')

    def click_string_now(self, string):
        """click on very first given string in page, NOTICE: its case sensitive"""
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(by= By.XPATH, value= fr"//*[contains(text(), '{string}')]").click()


    # def follow(self):
    #     """follow targeted account"""
    #     pass