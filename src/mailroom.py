# _*_ coding: utf-8 _*_
DONORS = {
    'kevin': [23, 34, 1000, 2849],
    'bob': [234, 888, 9023],
    'josh': [6, 1, 9, 5000, 9, 1, 2, 3],
    'alice': [3, 1]
}


def interface():
    response = input(u"Press 1 to send a thank you note\nPress 2 to create a \
report ")
    print(response)
    if response == '1':
        get_name()
    elif response == '2':
        create_report()
    else:
        print(u"Please enter 1 or 2")
        interface()


def get_name(name):
    name = input(u"Enter a donor\'s full name or to see a list of donors enter \
the word 'list'")
    name = name.lower()
    if name == "list":
        for key in DONORS:
            print(key)
        get_name()
    else:
        if name not in DONORS:
            DONORS[name] = []
            get_donation(name)
        else:
            get_donation(name)


def get_donation(name):
    donation = input(u"Enter the donation amount for {0}".format(name))
    if donation.isnumeric():
        DONORS[name].append(donation)
        print(DONORS)
        compose_email(name, donation)
    else:
        print("Please enter the donation using numbers.")
        get_donation(name)


def compose_email(name, donation):
    print("Dear {0}, Thank you for your generous donation of ${1}."
          .format(name, donation))
    interface()


interface()
