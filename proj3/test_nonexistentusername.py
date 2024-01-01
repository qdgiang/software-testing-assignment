from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


class TestNonexistentusername():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://localhost/moodle/")
    self.driver.set_window_size(550, 694)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_all(self):
    counter = 0
    with open("./incorrect_login.csv", "r") as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        username = row["username"]
        password = row["password"]
        self._test_nonexistentusername(username, password)
        counter += 1
    print(f"Number of tests passed: {counter}")


  def _test_nonexistentusername(self, username: str, password: str):
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys(f"{username}")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys(f"{password}")
    self.driver.find_element(By.ID, "loginbtn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    assert self.driver.find_element(By.ID, "loginerrormessage").text == "Invalid login, please try again"
  
if __name__ == '__main__':
  a = TestNonexistentusername()
  a.setup_method()
  a.test_all()
  a.teardown_method()