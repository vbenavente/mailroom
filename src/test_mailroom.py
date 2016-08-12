# _*_ coding: utf-8 _*_


def test_handle_name():
    from mailroom import handle_name
    test_donors = {}
    handle_name('bob', 100, test_donors)
    assert 'bob' in test_donors


def test_handle_donation():
    from mailroom import handle_donation
    test_donors = {'james': [3, 1]}
    handle_donation('james', 100, test_donors)
    assert test_donors == {'james': [3, 1, 100]}
