from item import Item


def addItems(room):
    room['outside'].inventory.append(Item("eggs", "They're just eggs"))
    room['outside'].inventory.append(Item("bacon", "It's just bacon"))
    room['outside'].inventory.append(Item("milk", "It's just milk"))
