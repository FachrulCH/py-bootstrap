from typing import Dict

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="function", autouse=True)
def goto(page: Page, request: SubRequest):
    """Fixture to navigate to the base URL based on the user.

    If the 'storage_state' is set in 'browser_context_args', it navigates to the inventory page,
    otherwise, it navigates to the login page.

    Args:
        page (Page): Playwright page object.
        request (SubRequest): Pytest request object to get the 'browser_context_args' fixture value.
            If 'browser_context_args' is set to a user parameter (e.g., 'standard_user'),
            the navigation is determined based on the user.

    Example:
        @pytest.mark.parametrize('browser_context_args', ["standard_user"], indirect=True)
    """
    if request.getfixturevalue("browser_context_args").get("storage_state"):
        page.goto("/inventory.html")
    else:
        page.goto("")

@pytest.fixture(scope="function")
def browser_context_args(
    browser_context_args: Dict, base_url: str, request: SubRequest
):
    """This fixture allows setting browser context arguments for Playwright.

    Args:
        browser_context_args (dict): Base browser context arguments.
        request (SubRequest): Pytest request object to get the 'browser_context_args' fixture value.
        base_url (str): The base URL for the application under test.
    Returns:
        dict: Updated browser context arguments.
    See Also:
        https://playwright.dev/python/docs/api/class-browser#browser-new-contex

    Returns:
        dict: Updated browser context arguments.
    """
    context_args = {
        **browser_context_args,
        "no_viewport": True,
        "user_agent": "Playwright-FCH",
    }

    if hasattr(request, "param"):
        context_args["storage_state"] = {
            "cookies": [
                {
                    "name": "session-username",
                    "value": request.param,
                    "url": base_url,
                }
            ]
        }
    return context_args


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict, playwright: Playwright):
    """Fixture to set browser launch arguments.

    This fixture updates the browser launch arguments to start the browser maximized
    and sets the test ID attribute for selectors.

    Args:
        browser_type_launch_args (Dict): Original browser type launch arguments.
        playwright (Playwright): The Playwright instance.

    Returns:
        Dict: Updated browser type launch arguments with maximized window setting.

    Note:
        This fixture has a session scope, meaning it will be executed once per test session.

    See Also:
        https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
    """
    playwright.selectors.set_test_id_attribute("data-test")
    return {**browser_type_launch_args, "args": ["--start-maximized"]}