# _*_ coding: utf-8 _*_
DONORS = {
    'kevin': [23, 34, 1000, 2849],
    'bob': [234, 888, 9023],
    'josh': [6, 1, 9, 5000, 9, 1, 2, 3],
    'alice': [3, 1]
}


def interface():
    response = input(u"Press 1 to send a thank you note\nPress 2 to create a report ")
    while (response != '1') and (response != '2'):
        print(u"Please enter 1 or 2")
        response = input(u"Press 1 to send a thank you note\nPress 2 to create a report ")
    if response == '1':
        name = input(u"Enter a donor\'s full name or enter the word 'list' to "
                     u"see a list of donors ")
        name = name.lower()
        while name == "list":
            for key in DONORS:
                print(key)
            name = input(u"Enter a donor\'s full name or enter the word 'list' to see a list of donors ")
            name = name.lower()
        donation = input(u"Enter the donation amount for {0}".format(name))
        while not donation.isnumeric():
            print("Please enter the donation using numbers.")
            donation = input(u"Enter the donation amount for {0}".format(name))
        handle_name(name, donation, DONORS)
        handle_donation(name, donation, DONORS)
        compose_email(name, donation)
    else:
        create_report()


def handle_name(name, donation, DONORS):
    if name not in DONORS:
        DONORS[name] = []
    return DONORS


def handle_donation(name, donation, DONORS):
    DONORS[name].append(int(donation))
    return DONORS


def compose_email(name, donation):
    print("Dear {0}, Thank you for your generous donation of ${1}."
          .format(name, donation))
    interface()


def create_report():
    report_list = []
    for i in range(0, len(report_names(DONORS))):
        person = []
        names = report_names(DONORS)
        totals = report_totals(DONORS)
        num_donations = report_num_donations(DONORS)
        average = report_average(report_totals(DONORS), report_num_donations(DONORS))
        person.extend((names[i], totals[i], num_donations[i], average[i]))
        report_list.append(person)
    report_list.sort(key=lambda x: x[1])
    report_list.reverse()
    print(report_list)
    interface()


def report_names(DONORS):
    list_names = []
    for key in DONORS:
        list_names.append(key)
    return list_names


def report_totals(DONORS):
    total_donated = []
    for i in DONORS:
        totals = (sum(DONORS[i]))
        total_donated.append(totals)
    return total_donated


def report_num_donations(DONORS):
    num_donations = []
    for i in DONORS:
        num = len(DONORS[i])
        num_donations.append(num)
    return num_donations


def report_average(total_donated, num_donations):
    report_average = []
    for i in range(0, len(total_donated)):
        average = total_donated[i] / num_donations[i]
        report_average.append(average)
    return report_average


if __name__ == '__main__':
    interface()
