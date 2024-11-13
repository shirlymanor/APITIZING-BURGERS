# Order
(*order*)

## Overview

Operations related to orders

### Available Operations

* [get](#get) - Read Order
* [update](#update) - Update Order

## get

Read an order

### Example Usage

```python
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.order.get(order_id=816257)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `order_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrderOutput](../../models/orderoutput.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ResponseMessageError | 404                         | application/json            |
| models.HTTPValidationError  | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update

Update an order

### Example Usage

```python
import burger_sdk
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.order.update(order_id=994562, order_update={
    "burger_ids": [
        1,
        3,
    ],
    "note": "Extra ketchup",
    "status": burger_sdk.OrderUpdateOrderStatus.PREPARING,
    "table": 3,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `order_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `order_update`                                                      | [models.OrderUpdate](../../models/orderupdate.md)                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrderOutput](../../models/orderoutput.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ResponseMessageError | 404                         | application/json            |
| models.HTTPValidationError  | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |