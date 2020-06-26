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

Properties

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

Property

| Property / attribute | Description                               | Example        |
| -------------------- | ----------------------------------------- | -------------- |
| size                 | gets the size of the item                 | login.size     |
| tag_name             | gets the name of the HTML tag of the item | login.tag_name |
| text                 | gets the text of the item                 | login.text     |

Methods

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

## pyunittest

Form to make a report of the test

- Test fixture: preparation of before and after of the test
- Test case: unit of code to test
- Test suite: test case collections in one file to execute all test sequentially
- Test runner: give order of the execution
- Test report: report of the test
