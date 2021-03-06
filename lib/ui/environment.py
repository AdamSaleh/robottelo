#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

from lib.ui.base import Base
from lib.ui.locators import locators
from selenium.webdriver.common.keys import Keys


class Environment(Base):

    def __init__(self, browser):
        self.browser = browser

    def create(self, name):
        self.wait_until_element(locators["env.new"]).click()
        if self.wait_until_element(locators["env.name"]):
            self.find_element(locators["env.name"]).send_keys(name)
        self.find_element(locators["submit"]).click()

    def delete(self, name, really):
        dropdown = self.wait_until_element((locators["env.dropdown"][0],
                                           locators["env.dropdown"][1] % name))
        dropdown.click()
        element = self.wait_until_element((locators["env.delete"][0],
                                           locators["env.delete"][1] % name))
        if element:
            element.click()
            if really:
                alert = self.browser.switch_to_alert()
                alert.accept()
            else:
                alert = self.browser.switch_to_alert()
                alert.dismiss()

    def search(self, name):
        searchbox = self.wait_until_element(locators["search"])
        if searchbox:
            searchbox.clear()
            searchbox.send_keys(name)
            searchbox.send_keys(Keys.RETURN)
            env = self.wait_until_element((locators["env.env_name"][0],
                                           locators["env.env_name"][1] \
                                           % name))
            if env:
                env.click()
        return env
