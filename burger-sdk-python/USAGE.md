<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.burgers.list()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from burger_sdk import BurgerSDK

async def main():
    s = BurgerSDK()
    res = await s.burgers.list_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->