# Receipt

## Example Usage

```typescript
import { Receipt } from "@x402api/sdk/models";

let value: Receipt = {
  status: "issued",
  id: null,
  receiptDigest: "<value>",
  signingKeyVersion: "<value>",
  createdAt: null,
};
```

## Fields

| Field                                                                                                         | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `status`                                                                                                      | [models.TenantPaymentReceiptProjectionStatusEnum](../models/tenant-payment-receipt-projection-status-enum.md) | :heavy_check_mark:                                                                                            | * `not_issued` - not_issued<br/>* `issued` - issued<br/>* `integrity_failure` - integrity_failure             |
| `id`                                                                                                          | *string*                                                                                                      | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `receiptDigest`                                                                                               | *string*                                                                                                      | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `signingKeyVersion`                                                                                           | *string*                                                                                                      | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `createdAt`                                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                 | :heavy_check_mark:                                                                                            | N/A                                                                                                           |