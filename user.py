import books

user_data = [{"borrowed": [], "role": "guest"},
             {"borrowed": [], "role": "librarian"},
             {"borrowed": [], "role": "member"}]


# INTERNAL


def getUser(who):
    return user_data[who]


def CanUserBorrow(who):
    if getUser(who)['role'] is "guest":
        return False
    return True


def CanUserAdd(who):
    if getUser(who)['role'] is "librarian":
        return True
    return False


def addBorrowedToUser(who, title, isborrowable):
    if len(user_data[who]['borrowed']) < 3 and isborrowable:
        user_data[who]['borrowed'].append(title)
        return True
    return False


# SERVICE


def getall():
    return user_data


def add(who, title, author):
    if CanUserAdd(who):
        return books.add(title, author)
    return False


def giveback(who, title):
    if getUser(who)['borrowed']:
        getUser(who)['borrowed'].remove(title)
    books.unborrow(title)


def borrow(who, title):
    if CanUserBorrow(who):
        isborrowable = books.borrow(title)
        addBorrowedToUser(who, title, isborrowable)
        return True
    return False
