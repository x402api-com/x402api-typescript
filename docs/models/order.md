# Order

## Example Usage

```typescript
import { Order } from "@x402api/sdk/models";

let value: Order = {
  id: "a5917dc6-d4c1-4905-8966-40204be078eb",
  resourceVersionId: "ca527226-4d30-4fd6-8481-be5305284dcf",
  requestFingerprint: "<value>",
  paymentIdentifier: "<value>",
  buyerPaymentIdentifier: "<value>",
  status: "fulfilled",
  paidAt: new Date("2024-06-19T18:03:47.639Z"),
  fulfilledAt: new Date("2026-05-09T02:45:28.699Z"),
  createdAt: new Date("2026-05-02T03:27:58.102Z"),
  updatedAt: new Date("2024-02-26T02:43:14.148Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `resourceVersionId`                                                                           | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `requestFingerprint`                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `paymentIdentifier`                                                                           | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `buyerPaymentIdentifier`                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `status`                                                                                      | [models.Status](../models/status.md)                                                          | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `paidAt`                                                                                      | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `fulfilledAt`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |