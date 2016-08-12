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
        name = input(u"Enter a donor\'s full name or enter the word 'list' to see a list of donors ")
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
    DONORS[name].append(donation)
    print(DONORS)



def compose_email(name, donation):
    print("Dear {0}, Thank you for your generous donation of ${1}."
          .format(name, donation))
    interface()


# interface()
