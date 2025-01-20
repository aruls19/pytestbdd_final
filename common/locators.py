lead_pagetitle="//div/span[text()='Leads']"

#lead creation xpath
lead_new_button="//div[@title='New']"
new_lead_window="//div/h2[text()='New Lead']"
lead_firstname="//input[@name='firstName']"
lead_lastname="//input[@name='lastName']"
lead_companyname="//input[@name='Company']"
lead_savebutton="//button[text()='Save']"

#lead conversion xpaths
leadpage_convertbutton="//button[@name='Convert']"
lead_convertwindow="//h1[contains(text(),'Convert Lead ')]"
leadtoaccount_convert_button="(//div/span/button[@type='button'])[2]"
lead_convertedtitle="//div[@class='title']"
leadconvert_existingbutton="//span[text()='Choose Existing Account']"
leadconvert_accountsearch="//input[@title='Search for matching accounts']"
searchaccount_select="//tr/td/a[@data-refid='recordId']"
gotolead_button="(//button[@class='slds-button slds-button_brand'])[2]"

account_name_link="//div[@class='primaryField truncate']/a[@title='OLD']"
account_pagetitle="//slot[@name='entityLabel']/records-entity-label[contains(text(),'Account')]"

#account creation xpaths
account_page_button = "(//a[@class='slds-context-bar__label-action dndItem']/child::span)[3]"
new_account_button = "//a/div[@title='New']"
dropdown_new_button="//span/span[text()='New Account']"
create_accountname = "//input[@name='Name']"
create_account_save_button = "//button[@name='SaveEdit']"

#contact creation xpaths
contact_page_button="//one-app-nav-bar-item-root/a/span[text()='Contacts']"
new_contact_button="//a/div[@title='New']"
contact_firstname="//input[@name='firstName']"
contact_lastname="//input[@name='lastName']"
search_accountname_xpath="//input[@placeholder='Search Accounts...']"
new_contact_save_button="//button[text()='Save']"

#opportunities creation xpaths
opportunites_page_button="//one-app-nav-bar-item-root/a/span[text()='Opportunities']"
new_opp_button="//a/div[@title='New']"
opp_name_xpath="//input[@name='Name']"
close_date_xpath="//input[@name='CloseDate']"
scroll_xpath="//div[@class='actionBody']"
stage_xpath="//button[@aria-label='Stage']"
new_opp_save_button="//button[text()='Save']"

#verify account page xpaths
scroll = "//html[@lang='en-US']"
first_account_xpath="(//a[@data-refid='recordId'])[1]"
contact_name="//span/slot[contains(text(),'CNAME')]"
opportunities_name="//span/slot[contains(text(),'ONAME')]"
