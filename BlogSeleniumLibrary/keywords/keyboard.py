


from SeleniumLibrary.base import keyword, LibraryComponent
from selenium.webdriver.chrome.options import Options
from  selenium import webdriver
from SeleniumLibrary.locators import WindowManager

class KeyboardKeywords(LibraryComponent):

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self._window_manager = WindowManager(ctx)

    @keyword()
    def get_chrome_options(self, downloads_path):
        '''
        自定义chrome启动参数
        :param downloads_path: 设置默认的文件下载路径
        :return:
        '''
        chrome_options = Options()
        prefs = {
            "download.default_directory": str(downloads_path),
        }
        chrome_options.add_experimental_option('prefs', prefs)  # 设置默认的文件下载路径
        chrome_options.add_argument('disable-infobars')  # chrome76以下禁用chrome受自动软件控制
        # 下面2行chrome76及以上禁用chrome受自动软件控制
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return chrome_options

    @keyword()
    def open_browser_new(self, alias=None,**kwargs):
        '''
        :return:
        '''
        desired_caps = {
            "platform": kwargs["platform"],
            # "platform":"LINUX",
            "browserName": kwargs["browserName"],
            "version":kwargs["version"]
        }

        driver = webdriver.Remote(command_executor=kwargs["remote_url"],
                                  desired_capabilities=desired_caps,
                                  options=kwargs["chrome_options"])
        return self.ctx.register_driver(driver,alias)