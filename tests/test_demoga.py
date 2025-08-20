from selene import browser, have, be


def test_complete_todo():

    browser. open("/")
    browser.element("#firstName"). should(be. blank)

    browser.element("#firstName").type("Test").press_enter()