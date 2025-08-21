from selene import browser, have, be


def test_correct_completion():

    browser. open("/")
    browser.element("#firstName"). should(be. blank)
    browser.element("#firstName").type("Test")
    browser.element("#lastName").should(be.blank)
    browser.element("#lastName").type("Testov")
    browser.element("#userEmail").type("Test@mail.ru")