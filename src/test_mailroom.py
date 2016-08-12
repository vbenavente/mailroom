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


def test_report_names():
    from mailroom import report_names
    assert 'vic' in report_names({'james': [4, 8], 'vic': [1, 2]})


def test_report_totals():
    from mailroom import report_totals
    assert 100 in report_totals({'james': [40, 60], 'vic': [28, 55]})


def test_report_num_donations():
    from mailroom import report_num_donations
    assert 3 in report_num_donations({'james': [1, 2, 3], 'vic': [1, 2, 3, 4]})


def test_report_average():
    from mailroom import report_average
    assert 10 in report_average([20, 50], [2, 7])


def test_create_report():
    from mailroom import create_report
    from mailroom import report_names
    from mailroom import report_totals
    from mailroom import report_num_donations
    from mailroom import report_average
    assert ['James', 60, 3, 20] in create_report(report_names({'James': []}), report_totals({'James': [40, 20]}), report_num_donations({'James': [1, 2, 3]}), report_average([40], [2]))
