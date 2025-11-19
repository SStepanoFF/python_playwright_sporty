import allure
import pytest


def attach_screenshot(page, name="screenshot"):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

def attach_console_logs(logs):
    if logs:
        allure.attach(
            "\n".join(logs),
            name="console_logs",
            attachment_type=allure.attachment_type.TEXT
        )