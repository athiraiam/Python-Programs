# import pytest
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import unittest
import pytest
from traceback import print_stack

class Test():

    #Login elements
    _loginLink = "//a[contains(text(),'Login')]"
    _email_field = "//input[@class='_2zrpKA _1dBPDZ']"
    _password_field = "// input[ @ type = 'password']"
    _login_button = "// div[@class='_1avdGP']/button[@type='submit']"

    #Home page elements
    _search_field = "//input[@class='LM6RPg']"
    _search_icon = "//*[local-name()='svg']//*[local-name()='path' and @class='_2BhAHa']"
    _mobile_product = "//div[contains(text(),'Apple iPhone XS (Gold, 64 GB)')]"
    _go_to_cart = "//button[@class='_2AkmmA _2Npkh4 _2MWPVK']"
    _remove_cart = "//div[contains(text(),'Remove')]"
    _confirm_rem_cart = "//div[@class='_2K02N8 _2x63a8']/div[contains(text(),'Remove')]"
    _wishlist_icon = "//div[@data-id='9789380349305']//*[local-name()='svg']"
    _book_product = "//div[@class='_3BTv9X']//img[@alt='Life is What You Make it']"
    _buy_now = "//span[@class='_279WdV']"
    _proceed_checkout = "//button[@class='_2AkmmA iwYpF9 _7UHT_c']"


    #My Activity drop down
    _my_activity = "//div[@class='_1jA3uo'][1]//*[local-name()='svg' and @class='_34Yjv1']//*"
    _my_wishlist = "//div[contains(text(),'Wishlist')]"
    _my_orders ="//div[contains(text(),'Orders')]"

    #Wishlist page
    _del_wishlist = "//div[@class='_20yN1P _3FfcKU _3piyP1']//span"
    _confirm_del_wishist = "//button[contains(text(),'YES, REMOVE')]"

    #Product Cancellation
    _cancel_btn = "//span[contains(text(),'Cancel Item')]"
    _cancel_reasonList = "//select[@name='reasonList']"
    _cancel_link = "//span[contains(text(),'Cancel Item')]"
    _cancel_reason_textarea = "//textarea[@class='cK8cRO']"
    _prdouct_cancel = "//button[@class='_2AkmmA _7UHT_c']//span"
    _product_cancel_confrim = "//button[@class='_2AkmmA _2qAAoj _7UHT_c']"

    #Checkout- Address
    _state = "//select[@name='state']"
    _home_radio_btn = "//div[@class='_3qg3HS']//div[@class='_6ATDKp']"
    _saveAddress = "//div[@class='_3qg3HS']//div[@class='_6ATDKp']"
    _checkout_continue = "//button[contains(text(),'CONTINUE')]"
    #checkout - Payment
    _debit_payment = "//label[@for='CREDIT']/div[@class='_6ATDKp']"
    _debit_no = "//input[@name='cardNumber']"
    _year = "//select[@name='year']"
    _month = "//select[@name='month']"
    _cvv = "//input[@name='cvv']"
    _pay_btn = "//button[contains(text(),'PAY ₹137')]"

    def test_switchHandle(self):
        parentHandle = self.driver.current_window_handle

        handles = self.driver.window_handles
        print("Parent handle is : {}".format(handles))

        for handle in handles:
            print("Handle:" + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print(f"switched to window: {handle}")



    def test_commonsteps(self):
        driverLocation = "/home/athira/PycharmProjects/libs/chromedriver_linux64/chromedriver"
        os.environ["webdriver.Chrome.driver"] = driverLocation
        self.driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://www.flipkart.com/"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

        login_ele = self.getElement(locator=self._loginLink, locatorType="xpath")
        print("Login element is found.")
        self.getElement(locator=self._email_field, locatorType="xpath").send_keys("athira.jenu@gmail.com")
        self.getElement(locator=self._password_field, locatorType="xpath").send_keys("jesusjenu1")
        self.getElement(locator=self._login_button, locatorType="xpath").click()
        time.sleep(3)



    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def test_searchProduct(self, data):
        self.sendKeys(locator=self._search_field, locatorType="xpath", data=data)
        print(f"{data} is the item to be searched")
        self.elementClick(locatorType="xpath", locator=self._search_icon)
        print(f"Search result of {data} is displayed")

    def test_clickSearchResult(self, locatorType, locator):
        print("Product details is clicked")
        return self.elementClick(locatorType=locatorType, locator=locator)

    def test_goToCart(self):
        print("Product is added to cart")
        self.elementClick(locatorType="xpath", locator=self._go_to_cart)

    def test_removeFromCart(self):
        self.elementClick(locator=self._remove_cart, locatorType="xpath")
        self.elementClick(locatorType="xpath", locator=self._confirm_rem_cart)
        print("Product is removed from Cart")

    def test_hover(self, locator, locatorType):
        actions = ActionChains(self.driver)
        element = self.getElement(locator=locator, locatorType=locatorType)
        actions.move_to_element(element).perform()




    def test_delWishlist(self,locator, locatorType):
        self.elementClick(locator=locator, locatorType=locatorType)
        print("Confirm to delete from wishlist")

    def test_confirmDelWishlist(self, locator, locatorType):
        self.elementClick(locator=locator, locatorType=locatorType)
        print("Product is deleted from wishlist")

    def selectFromList(self, visibleText, locator, locatorType):
        element = self.getElement(locator, locatorType)
        select = Select(element)
        select.select_by_visible_text(visibleText)

    def test_buyNow(self, locator, locatorType):
        self.elementClick(locatorType, locator)
        print("Proceed to checkout page after clicking on buy now")


    def test_add(self):
        self.test_commonsteps()
        self.test_searchProduct(data="iphone xs mobile")
        self.test_clickSearchResult(locatorType="xpath", locator=self._mobile_product)
        self.test_switchHandle()
        self.test_goToCart()
        time.sleep(3)
        self.test_removeFromCart()
        time.sleep(3)
        self.driver.quit()

    def test_wishlist(self):
        print("#"*200)
        self.test_commonsteps()
        self.test_searchProduct(data="books")
        self.test_clickSearchResult(locator=self._wishlist_icon, locatorType="xpath")
        time.sleep(3)
        print("Wishlist icon is clicked")
        self.test_hover(locatorType="xpath", locator=self._my_activity)
        time.sleep(3)
        self.elementClick(locatorType="xpath", locator=self._my_wishlist)
        time.sleep(3)
        self.test_delWishlist(locator=self._del_wishlist, locatorType="xpath")
        self.test_confirmDelWishlist(locator=self._confirm_del_wishist, locatorType="xpath")
        self.driver.quit()

    def test_multipleItemsCart(self):
        print("#" * 100)
        self.test_commonsteps()
        self.test_searchProduct(data="book")
        self.test_clickSearchResult(locatorType="xpath", locator=self._book_product)
        time.sleep(3)
        self.test_switchHandle()
        self.test_goToCart()
        self.test_searchProduct(data="iphone xs mobile")
        time.sleep(3)
        self.test_clickSearchResult(locatorType="xpath", locator=self._mobile_product)
        self.test_switchHandle()
        self.test_goToCart()
        time.sleep(7)
        self.driver.quit()

    def test_creditPurchase(self):

        print("#" * 100)
        self.test_commonsteps()
        self.test_searchProduct(data="book")
        self.test_clickSearchResult(locatorType="xpath", locator=self._book_product)
        time.sleep(3)
        self.test_switchHandle()
        self.test_goToCart()
        self.test_buyNow(locatorType="xpath", locator=self._buy_now)
        time.sleep(4)
        self.elementClick(locatorType="xpath", locator=self._proceed_checkout)
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='name']").send_keys("Athira Krishnan")
        self.driver.find_element_by_xpath("//input[@name='phone']").send_keys("8106636589")
        self.driver.find_element_by_xpath("//input[@name='pincode']").send_keys("560090")
        self.driver.find_element_by_xpath("//input[@name='addressLine2']").send_keys("Kereguddadahalli")
        self.driver.find_element_by_xpath("//textarea[@name='addressLine1']").send_keys(
            "F3, Block B, Diamond Dwellings")
        self.selectFromList(visibleText="Karnataka", locator=self._state, locatorType="xpath")
        self.elementClick(locatorType="xpath", locator=self._home_radio_btn)
        self.elementClick(locatorType="xpath", locator=self._saveAddress)
        print("Enter all the address details")
        self.elementClick(locatorType="xpath", locator=self._checkout_continue)
        self.elementClick(locator=self._debit_payment, locatorType="xpath")
        self.sendKeys(data="52676950xx680540", locatorType="xpath", locator=self._debit_no)
        self.selectFromList(visibleText="12", locator=self._month, locatorType="xpath")
        self.selectFromList(visibleText="20", locator=self._year, locatorType="xpath")
        self.sendKeys(data="899", locatorType="xpath", locator=self._cvv)
        self.elementClick(locator=self._pay_btn, locatorType="xpath")
        self.test_switchHandle()
        time.sleep(10)
        print("Proceeded payment")
        self.test_hover(locatorType="xpath", locator=self._my_activity)
        self.elementClick(locator=self._my_orders, locatorType="xpath")
        self.driver.quit()

    def test_cancelPurchase(self):

        print("#" * 100)
        self.test_commonsteps()
        self.test_hover(locator=self._my_activity, locatorType="xpath")
        time.sleep(3)
        self.elementClick(locator=self._my_orders, locatorType="xpath")
        self.elementClick(locatorType="xpath", locator=self._cancel_btn)
        self.selectFromList(visibleText="My reason is not listed", locator=self._cancel_reasonList,
                            locatorType="xpath")
        self.sendKeys(data="would like to buy some other item", locatorType="xpath",
                      locator=self._cancel_reason_textarea)
        self.elementClick(locator=self._prdouct_cancel, locatorType="xpath")
        self.elementClick(locatorType="xpath", locator=self._product_cancel_confrim)
        print("Cancellation Success")
        time.sleep(3)
        self.driver.quit()

test1 = Test()
test1.test_add()
test1.test_wishlist()
test1.test_multipleItemsCart()
test1.test_creditPurchase()
test1.test_cancelPurchase()

