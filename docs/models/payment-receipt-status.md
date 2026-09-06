# PaymentReceiptStatus

## Example Usage

```typescript
import { PaymentReceiptStatus } from "@x402api/sdk/models";

let value: PaymentReceiptStatus = {
  paymentId: "a2ec6677-0edc-48d9-9aa3-0041d75359ec",
  state: "Alaska",
  confirmed: false,
  finalized: true,
  confirmedAt: new Date("2025-02-09T13:52:46.418Z"),
  finalizedAt: new Date("2025-01-14T09:19:59.601Z"),
  transaction: "<value>",
  network: "<value>",
  receiptStatus: "pending_confirmation",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `paymentId`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `state`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `confirmed`                                                                                   | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `finalized`                                                                                   | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `confirmedAt`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `finalizedAt`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `transaction`                                                                                 | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `receiptStatus`                                                                               | [models.ReceiptStatusEnum](../models/receipt-status-enum.md)                                  | :heavy_check_mark:                                                                            | * `pending_confirmation` - pending_confirmation<br/>* `pending_finality` - pending_finality   |