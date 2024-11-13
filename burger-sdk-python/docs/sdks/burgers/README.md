# Burgers
(*burgers*)

## Overview

### Available Operations

* [list](#list) - List Burgers
* [create](#create) - Create Burger
* [delete](#delete) - Delete Burger
* [get](#get) - Read Burger
* [update](#update) - Update Burger

## list

List all burgers

### Example Usage

```python
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.burgers.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.BurgerOutput]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a burger

### Example Usage

```python
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.burgers.create(request={
    "name": "Hamburger",
    "description": "A classic cheeseburger",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BurgerCreate](../../models/burgercreate.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BurgerOutput](../../models/burgeroutput.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a burger

### Example Usage

```python
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.burgers.delete(burger_id=199926)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `burger_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResponseMessage](../../models/responsemessage.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ResponseMessageError | 404                         | application/json            |
| models.HTTPValidationError  | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get

Read a burger

### Example Usage

```python
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.burgers.get(burger_id=102880)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `burger_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BurgerOutput](../../models/burgeroutput.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ResponseMessageError | 404                         | application/json            |
| models.HTTPValidationError  | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update

Update a burger

### Example Usage

```python
from burger_sdk import BurgerSDK

s = BurgerSDK()

res = s.burgers.update(burger_id=174868, burger_update={
    "description": "technician eulogise whereas till mild than during",
    "name": "Cheeseburger",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `burger_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `burger_update`                                                     | [models.BurgerUpdate](../../models/burgerupdate.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BurgerOutput](../../models/burgeroutput.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ResponseMessageError | 404                         | application/json            |
| models.HTTPValidationError  | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |