import pytest
import main

form1 = main.Form("Admin", "qwerty")
form2 = main.Form('User', 'qwerty', 'example@mail.ru', 'https://itproger.com')

@pytest.mark.parametrize('login, password', [
    ('Aboba', 'bebr'),
    ('User', 'usage')
])
def test_form_2(login, password):
    form = main.Form(login, password)
    assert form.login == login
    assert form.password == password

@pytest.mark.parametrize('login, password, mail, url', [
    ("Admin", "qwerty", "admin@mail.ru", "https://bebra.com"),
    ('User', 'qwerty', 'example@mail.ru', 'https://itproger.com')
])
def test_form_4(login, password, mail, url):
    form = main.Form(login, password, mail, url)
    assert form.login == login
    assert form.password == password
    assert form.mail == mail
    assert form.url == url


@pytest.mark.parametrize('url, res', [
    ("https://bebra.com", "https://bebra.com"),
    ("akdjgnkjfdngsgg", "https://bebra.com"),
    ("https://itproger.com", "https://itproger.com")
])
def test_set_web_url(url, res):
    form2.set_web_url(url)
    assert form2.url == res
