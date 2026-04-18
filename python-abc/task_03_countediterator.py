#!/usr/bin/python3
"""
CountedIterator klassı - iterasiya sayını izləyir
"""

class CountedIterator:
    """
    Iteratoru bükür (wrap) və hər __next__ çağırışında sayğacı artırır
    """
    def __init__(self, iterable):
        # Obyekti iteratora çeviririk və sayğacı sıfırlayırıq
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        # Cari sayğac göstəricisini qaytarır
        return self.count

    def __next__(self):
        # Elementi götürürük, əgər varsa sayğacı artırırıq
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # Element bitdikdə StopIteration xətasını ötürürük
            raise StopIteration

    def __iter__(self):
        return self
