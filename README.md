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

mylist: Union[Pykon, PykonError] = Pykon(list, [1,2,3,4])

if type(mylist) is Pykon.PykonError:
    raise mylist
else:
    print(mylist.data)
```
