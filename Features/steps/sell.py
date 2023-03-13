import time

from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I open Application URL in the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.magicbricks.com/")
    time.sleep(3)


@given(u'I navigate to web page')
def step_impl(context):
    # Navigate to web page
    pass


@when(u'I click on the Sell tab')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Sell").click()
    time.sleep(3)



@when(u'I click the Post Property button')
def step_impl(context):
    context.driver.get("https://post.magicbricks.com/")


@when(u'I am prompted to enter details about the seller type, property type, and WhatsApp number')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,".pp-form__fieldset__wrap:nth-child(5) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()
    context.driver.find_element(By.CSS_SELECTOR,".pp-form__fieldset__wrap:nth-child(2) > .pp-form__elem-radio:nth-child(1) > .pp-form__elem-radio__label").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pp-form__label").click()
    context.driver.find_element(By.ID, "ownerMobile").send_keys("8328419354")
    context.driver.find_elements(By.CSS_SELECTOR, ".pp-form__cta")


@when(u'I click on the Ad Packages button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Ad Packages").click()
    time.sleep(5)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)


@then(u'I should see a list of available Ad Packages')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#userTypeList > .active > label").click()
    context.driver.find_element(By.CSS_SELECTOR, "#sellId > label").click()
    context.driver.find_element(By.CSS_SELECTOR, ".m-t-10:nth-child(4) .active > label").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(4)
    context.driver.find_element(By.LINK_TEXT, "Buy Now").click()
    time.sleep(3)
    context.driver.find_element(By.LINK_TEXT, "Add to My Orders").click()
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, ".orderNoArrow").click()
    context.driver.quit()


@when(u'I click on the iAdvantage option')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "iAdvantage").click()
    time.sleep(5)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)
    #context.driver.set_window_size(1296, 688)


@then(u'I can add package to my cart')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Add to My Orders").click()
    time.sleep(5)
@then(u'I should click on got to cart option')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".orderNoArrow").click()
    context.driver.quit()

@when(u'I click on the Find an Agent button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[3]/div/div/div[3]/ul/li[2]/a").click()
    #context.driver.get( "https://www.magicbricks.com/Real-estate-property-top-agents/agent-in-Mumbai?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai&mbTrackSrc=tabChange&page=1&category=S")
    time.sleep(4)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)


@then(u'I should see a list of Top Agents in city and in particular area')
def step_impl(context):
    context.driver.find_element(By.ID, "cityList").click()
    time.sleep(3)
    dropdown = context.driver.find_element(By.ID, "cityList")
    time.sleep(3)
    dropdown.find_element(By.XPATH, "//option[. = 'Pune']").click()
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, ".srpSort").click()
    time.sleep(3)
    context.driver.find_element(By.ID, "localityList").click()
    time.sleep(3)
    dropdown = context.driver.find_element(By.ID, "localityList")
    time.sleep(3)
    dropdown.find_element(By.XPATH, "//option[. = 'Hinjewadi']").click()
    time.sleep(3)
    #vars["window_handles"] = context.driver.window_handles
    context.driver.find_element(By.LINK_TEXT, "Contact Agent").click()
    context.driver.execute_script("window.scrollTo(0,16.66666603088379)")
    elements=context.driver.find_elements(By.ID, "contactObjButton")
    assert len(elements) > 0
