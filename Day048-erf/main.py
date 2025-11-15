from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_events_details = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
events_df = pd.DataFrame(
    data={},
    columns=["Title", "Date"]
)
for li in upcoming_events_details:
    title = li.find_element(By.CSS_SELECTOR, "a").text
    datetime = li.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime").split('T')[0]
    events_df.loc[(len(events_df))] = {"Title": title, "Date": datetime}
    
course_challenge_output = events_df.to_dict(orient='index')
print(events_df)
print(course_challenge_output)
