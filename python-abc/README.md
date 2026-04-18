# Python - Abstract Classes and Interfaces

Bu layihə **ALX/Holberton School** kurrikulumunun bir hissəsidir və Python-da Obyekt Yönümlü Proqramlaşdırmanın (OOP) qabaqcıl konsepsiyalarını əhatə edir. Əsas diqqət abstrakt klasslar, interfeyslər və "duck typing" prinsiplərinə ayrılmışdır.

## Öyrənilən Konsepsiyalar
- **Abstrakt Klasslar (ABC):** Ümumi interfeysləri təyin etmək və alt klassların müəyyən metodları tətbiq etməsini məcburi etmək.
- **Interfaces & Duck Typing:** Obyektlərin tipindən asılı olmayaraq, onların davranışına (metodlarına) əsaslanan proqramlaşdırma.
- **Subclassing:** Standart Python klasslarını genişləndirmək.
- **Method Overriding:** Baza klassın metodlarını alt klasslarda yenidən təyin etmək.

## Fayl Strukturu

| Fayl | Təsvir |
| --- | --- |
| `task_00_abc.py` | `Animal` abstrakt klassı və onun `Dog`, `Cat` alt klassları. |
| `task_01_duck_typing.py` | `Shape` abstrakt klassı, `Circle`, `Rectangle` klassları və duck typing-i nümayiş etdirən `shape_info` funksiyası. |

## Necə İstifadə Etməli?

Hər bir tapşırıq fərdi şəkildə işə salına bilər. Məsələn, `task_00_abc.py` faylını yoxlamaq üçün:

```python
from task_00_abc import Dog, Cat

bobby = Dog()
print(bobby.sound())  # Çıxış: Bark

garfield = Cat()
print(garfield.sound())  # Çıxış: Meow
