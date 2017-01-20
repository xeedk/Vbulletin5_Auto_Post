

from selenium import webdriver
import time


USERNAME = 'user'
PASSWORD = 'pass'


def create_new_post(forum_name, link, title, content):
    while(True):
        try:
            print 'running %s' % title
            #browser = webdriver.Firefox()
            browser = webdriver.PhantomJS()

            browser.get('http://myforum.ddd/auth/login')

            input_number = browser.find_element_by_id('idLoginUserName')
            input_number.send_keys(USERNAME)

            input_number = browser.find_element_by_id('idLoginPassword')
            input_number.send_keys(PASSWORD)

            browser.find_element_by_id("idLoginBtn").click()

            browser.get('http://myforum.ddd/forum/' + forum_name)

            create_post = None
            for elem in browser.find_elements_by_xpath('.//span[@class = "button-text-primary"]'):
                if elem.text == '+ New Topic':
                    create_post = elem
                    break

            create_post.click()

            browser.find_element_by_xpath('.//li[@class = "b-toolbar__item js-button"][@title = "Post Link"]').click()


            input = browser.find_element_by_xpath('.//input[@class = "b-form-input__input b-link-input__url"]')
            input.send_keys(link)

            try:
                pop_up = browser.find_element_by_id('btnAlertDialogOK')
                if pop_up:
                    browser.find_element_by_id('btnAlertDialogOK').click()
            except:
                pass

            add_link = None
            for elem in browser.find_elements_by_xpath('.//button[@type = "button"]'):
                if elem.text == 'Add Link':
                    add_link = elem
                    break

            add_link.click()
            time.sleep(10)
            try:
                pop_up = browser.find_element_by_id('btnAlertDialogOK')
                if pop_up:
                    browser.find_element_by_id('btnAlertDialogOK').click()
            except:
                pass


            input = browser.find_element_by_xpath('.//input[@name = "title"]')
            input.send_keys(title)



            browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
            input = browser.find_element_by_xpath('html/body')
            input.send_keys(content)

            browser.switch_to_default_content()

            post = None
            for elem in browser.find_elements_by_xpath('.//button[@type = "submit"]'):
                print elem.text
                if elem.text == 'Post':
                    post = elem
                    break

            try:
                pop_up = browser.find_element_by_id('btnAlertDialogOK')
                if pop_up:
                    browser.find_element_by_id('btnAlertDialogOK').click()
            except:
                pass


            post.click()
            print 'finish %s' % forum_name
            return True
        except:
            pass


if __name__ == '__main__':
    data = None
    with open('input.txt') as f:
        data = f.readlines()
    for line in data:
        info = line.split(',')
        forum_name = info[0]
        title = info[1]
        link = info[2]
        content = info[3]
        forum_name = forum_name.lower()


        create_new_post(forum_name, link, title, content)



#Input File Struct..
#myforumtopostto,mythreadtitle,http://www.youtube.com/watch?v=flUqDwVf6NQ,"Hadoop Security: Seven Ways to Kill an Elephant"