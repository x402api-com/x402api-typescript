# OrdersListRequest

## Example Usage

```typescript
import { OrdersListRequest } from "@x402api/sdk/models/operations";

let value: OrdersListRequest = {};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `cursor`                                                               | *string*                                                               | :heavy_minus_sign:                                                     | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link.  |
| `pageSize`                                                             | *number*                                                               | :heavy_minus_sign:                                                     | Number of results in the bounded array page (default and maximum 100). |