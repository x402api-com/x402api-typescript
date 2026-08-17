# OrdersRetrieveResponse

## Example Usage

```typescript
import { OrdersRetrieveResponse } from "@x402api/sdk/models/operations";

let value: OrdersRetrieveResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `order`                                                       | [models.Order](../../models/order.md)                         | :heavy_minus_sign:                                            | Successful response for retrieve an order.                    |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |