#!/usr/bin/python3
"""
Standart list klassını genişləndirən VerboseList klassı
"""

class VerboseList(list):
    """
    Siyahıya element əlavə edildikdə və ya silindikdə bildiriş çap edir
    """

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
