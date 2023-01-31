import pytest
from py.xml import html
from config import RunConfig
import allure
from slugify import slugify
from common.config import *
from playwright.sync_api import sync_playwright, expect



# 定义基本测试环境
@pytest.fixture(scope='session')
def base_url():
    return RunConfig.baseUrl


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    allure报告模版
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    """
    if call.when == "call":
        # 失败的情况下
        if call.excinfo is not None and "page" in item.funcargs:
            from playwright.async_api import Page
            page: Page = item.funcargs["page"]

            allure.attach(
                page.screenshot(type='png'),
                name=f"{slugify(item.nodeid)}.png",
                attachment_type=allure.attachment_type.PNG
            )

            # # 向报告中添加视频
            # video_path = page.video.path()
            # page.context.close()  # ensure video saved
            # allure.attach(
            #     open(video_path, 'rb').read(),
            #     name=f"{slugify(item.nodeid)}.webm",
            #     attachment_type=allure.attachment_type.WEBM
            # )

    callers = yield


def capture_screenshots(case_name, page):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        page.screenshot(path=image_dir)
#     context.close()

@pytest.fixture(scope="class")
def page():
    with sync_playwright() as play:
        if os.getenv("DOCKER_RUN") or os.getenv("GITHUB_RUN"):
            browser = play.chromium.launch(headless=True, args=["--no-sandbox"])
        else:
            browser = play.chromium.launch(headless=False)
        permissions = ["clipboard-read", "clipboard-write"]
        context = browser.new_context(permissions=permissions)
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page
        # 保存日志
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()



def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html