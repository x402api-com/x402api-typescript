# OrdersListResponse

## Example Usage

```typescript
import { OrdersListResponse } from "@x402api/sdk/models/operations";

let value: OrdersListResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `paginatedOrderList`                                          | [models.Order](../../models/order.md)[]                       | :heavy_minus_sign:                                            | Successful response for list orders.                          |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |