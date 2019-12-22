

# #-*-coding:utf-8-*-
#
from robot.libraries import BuiltIn
from SeleniumLibrary.base import DynamicCore
from SeleniumLibrary.keywords import (AlertKeywords,
                                      BrowserManagementKeywords,
                                      CookieKeywords,
                                      ElementKeywords,
                                      FormElementKeywords,
                                      FrameKeywords,
                                      JavaScriptKeywords,
                                      RunOnFailureKeywords,
                                      ScreenshotKeywords,
                                      SelectElementKeywords,
                                      TableElementKeywords,
                                      WaitingKeywords,
                                      WebDriverCache,
                                      WindowKeywords)
from SeleniumLibrary.locators import ElementFinder
from SeleniumLibrary.utils import Deprecated, LibraryListener, timestr_to_secs
from  SeleniumLibrary import SeleniumLibrary

from BlogSeleniumLibrary.keywords import (
                                            KeyboardKeywords)


class  BlogSeleniumLibrary(SeleniumLibrary):


    def  __init__(self, timeout=5.0, implicit_wait=0.0,
                 run_on_failure='Capture Page Screenshot',
                 screenshot_root_directory=None):
        SeleniumLibrary.__init__(self, timeout=5.0, implicit_wait=0.0,
                 run_on_failure='Capture Page Screenshot',
                 screenshot_root_directory=None)
        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0
        self.run_on_failure_keyword \
            = RunOnFailureKeywords.resolve_keyword(run_on_failure)
        self._running_on_failure_keyword = False
        self.screenshot_root_directory = screenshot_root_directory
        libraries = [
            AlertKeywords(self),
            BrowserManagementKeywords(self),
            CookieKeywords(self),
            ElementKeywords(self),
            FormElementKeywords(self),
            FrameKeywords(self),
            JavaScriptKeywords(self),
            RunOnFailureKeywords(self),
            ScreenshotKeywords(self),
            SelectElementKeywords(self),
            TableElementKeywords(self),
            WaitingKeywords(self),
            WindowKeywords(self),
            KeyboardKeywords(self)
        ]
        self._drivers = WebDriverCache()
        DynamicCore.__init__(self, libraries)
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()
        self._element_finder = ElementFinder(self)

    _speed_in_secs = Deprecated('_speed_in_secs', 'speed')
    _timeout_in_secs = Deprecated('_timeout_in_secs', 'timeout')
    _implicit_wait_in_secs = Deprecated('_implicit_wait_in_secs',
                                        'implicit_wait')
    _run_on_failure_keyword = Deprecated('_run_on_failure_keyword',
                                         'run_on_failure_keyword')

