#!/usr/bin/python3
"""
Standart dict klassını genişləndirən SimpleCustomDict klassı
"""

class SimpleCustomDict(dict):
    """
    Lüğət elementlərinə atribut kimi müraciət etməyə imkan verən klass
    """
    def __setitem__(self, key, value):
        # element əlavə ediləndə standart dict funksiyasını çağırır
        super().__setitem__(key, value)

    def __getattr__(self, name):
        # obyekt.atribut kimi müraciət edildikdə işə düşür
        try:
            return self[name]
        except KeyError:
            raise AttributeError("No such attribute: {}".format(name))

    def __setattr__(self, name, value):
        # obyekt.atribut = dəyər kimi təyin edildikdə işə düşür
        self[name] = value
