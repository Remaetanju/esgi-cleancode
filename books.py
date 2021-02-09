library = {
             "Mangezdespates": {"author": "Richard", "borrowed": False},
             "Chauvequipeut": {"author": "Renee", "borrowed": False},
             "truc": {"author": "Daniel", "borrowed": False}
}


# INTERNAL


def GetBookByTitle(title):
    return library[title]


def IsBookBorrowable(title):
    return not GetBookByTitle(title)['borrowed']


# SERVICE


def getall():
    return library


def borrowable(title):
    return not IsBookBorrowable(title)


def add(title, author):
    library[title] = {"author": author, "borrowed": False}
    return True


def unborrow(borrowedtitle):
    if library[borrowedtitle]:
        library[borrowedtitle]['borrowed'] = False


def borrow(title):
    if IsBookBorrowable(title):
        GetBookByTitle(title)['borrowed'] = True
        return True
    return False
