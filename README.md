# Selenium - Python

Selenium web driver is a portable framework for testing web applications

## Download the webdriver

Download the webdriver of Chrome and Python for your navigator in the official web of [Selenium](https://sites.google.com/a/chromium.org/chromedriver/downloads).  
to download the webdriver for another navigator use this [Selenium](https://pypi.org/project/selenium/).  
If you want use another language enter [Selenium](https://www.selenium.dev/downloads/).

---

## Install Selenium

Install selenium from pip.

```bash
pip3 install selenium
```

---

## Selectors

Help to find elements for:

- ID
- Name of the attribute
- Name of the class
- Name of the tag
- XPath
- Css selector
- Text of the link
- Partial text of the link

---

## WebDriver

Have some methods for interact with the browser and its elements

### Properties

| Property / attribute  | Description                                                     | Example                      |
| --------------------- | --------------------------------------------------------------- | ---------------------------- |
| current_url           | gets the URL of the site                                        | driver.get_url               |
| current_window_handle | gets the reference that identify the window active              | driver.current_window_handle |
| name                  | gets the name of the underlying browser for the active instance | driver.name                  |
| orientation           | gets the orientation of the mobile                              | driver.orientation           |
| page_source           | gets the source code of the website                             | driver.page_source           |
| title                 | gets the value of the tag \<title>                              | driver.title                 |

## WebElement

This class allows interact with elements of the website

### Property

| Property / attribute | Description                               | Example        |
| -------------------- | ----------------------------------------- | -------------- |
| size                 | gets the size of the item                 | login.size     |
| tag_name             | gets the name of the HTML tag of the item | login.tag_name |
| text                 | gets the text of the item                 | login.text     |

### Methods

| Method / Attribute                   | Description                                                | Example                                                                  |
| ------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------ |
| clear()                              | clean the content of a textarea                            | first_name.clear()                                                       |
| click()                              | make click in the item                                     | send_button.click()                                                      |
| get_attribute(name)                  | gets the value of the attribute of the item                | submit_button.get_attribute('value') last_name.get_attribute(max_length) |
| is_displayed()                       | check if the item is in view of the user                   | banner.is_displayed()                                                    |
| is_enabled()                         | check if the item is enabled                               | radio_button.is_enabled()                                                |
| is_selected()                        | check if the item is selected, for radiobutton or checkbox | checkbox.is_selected()                                                   |
| send_keys()                          | simulates write in an element of press key in an item      | email_field.send_keys('github')                                          |
| submit()                             | send a form o confirmation in a text area                  | search_field.submit()                                                    |
| value_of_css_property(property_name) | gets the value of one property css of the item             | header.value_of_css_property('background-color')                         |

---

## Explicit and implicit delay

Implicit: search for one or more elements in the DOM if not available for the quantity of time assign
Explicit: uses specified waiting conditions and continues until they are met

| Expected conditionals           | Description                                                                                                              | Example                                                                                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| element_to_be_clickable         | waits for the item to be visible and enabled to click on it                                                              | WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "accept_button")))                                      |
| element_to_be_selected          | waits for the item to be selected                                                                                        | subscription = self.driver.find_element_by_name("terms").WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_selected((terms))) |
| invisibility_of_element_located | waits for the item don't be visible o not be in the DOM                                                                  | WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located((By.ID,“loading_banner”)))                                 |
| presence_of_all_element_located | waits for almost one of the elements indicated match with the elements presented in the website                          | WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,“input-text”)))                            |
| presence_of_element_located     | waits for the item be visible and be present in the DOM                                                                  | WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,“search-bar”)))                                         |
| text_to_be_present_in_element   | waits for the item with the indicated text to be present                                                                 | WebDriverWait(self.driver,10).until(expected_conditions.text_to_be_present_in_element((By.ID,“seleorder”),“high”))                                 |
| title_contains                  | waits for the page contain exactly the title as the indicated                                                            | WebDriverWait(self.driver, 10).until(expected_conditions.title_contains(“Welcome”))                                                                |
| title_is                        | waits for the page contains identic the title as the indicated                                                           | WebDriverWait(self.driver, 10).until(expected_conditions.title_is(“Welcome”))                                                                      |
| visibility_of                   | waits for the indicated item is in the DOM, is visible, is height and width are greater than zero                        |
| visibility_of_element_located   | waits for the item indicated by the selector to be in the DOM, be visible and its height and width are greater than zero | WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,“firstname”)))                                        |

---

## pyunittest

Form to make a report of the test

- Test fixture: preparation of before and after of the test
- Test case: unit of code to test
- Test suite: test case collections in one file to execute all test sequentially
- Test runner: give order of the execution
- Test report: report of the test
