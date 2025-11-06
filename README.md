                            ██████╗ ██╗   ██╗██╗  ██╗ ██████╗ ███╗   ██╗
                            ██╔══██╗╚██╗ ██╔╝██║ ██╔╝██╔═══██╗████╗  ██║
                            ██████╔╝ ╚████╔╝ █████╔╝ ██║   ██║██╔██╗ ██║
                            ██╔═══╝   ╚██╔╝  ██╔═██╗ ██║   ██║██║╚██╗██║
                            ██║        ██║   ██║  ██╗╚██████╔╝██║ ╚████║
                            ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                            

| Pykon is a way to allow constant and publicly immutable data.

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
