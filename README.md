                        ██████╗ ██╗   ██╗██╗  ██╗ ██████╗ ███╗   ██╗
                        ██╔══██╗╚██╗ ██╔╝██║ ██╔╝██╔═══██╗████╗  ██║
                        ██████╔╝ ╚████╔╝ █████╔╝ ██║   ██║██╔██╗ ██║
                        ██╔═══╝   ╚██╔╝  ██╔═██╗ ██║   ██║██║╚██╗██║
                        ██║        ██║   ██║  ██╗╚██████╔╝██║ ╚████║
                        ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                            

> Pykon is a way to allow constant and publicly immutable data.

> Though, data can be modified its type cannot.

> With Pykon, errors are returned rather than being raised

> giving the user the ability to control when an error should be raised.

## Example
```python
from pykon import Pykon
from typing import Union

mylist: Pykon = Pykon(list, [1,2,3,4])

if hasattr(mylist, "error"):
    raise mylist.error
else:
    print(mylist.data)


# Using a try except block
#
# try:
#    print(mylist.data)
# except AttributeError:
#    raise mylist.error


# Return a PykonError from a function
#
# def test() -> Union[None, Pykon.PykonError]:
#     constantInt: Pykon = Pykon(int, 20)
#     if hasattr(constantInt, "data"):
#         print(constantInt.data)
#         return None
#     else:
#         return constantInt.error
```
