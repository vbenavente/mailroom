# _*_ coding: utf-8 _*_


def test_handle_name():
    from mailroom import handle_name
    test_donors = {}
    handle_name('bob', 100, test_donors)
    assert 'bob' in test_donors
