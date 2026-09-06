# PaymentsRetrieveReceiptResponse

## Example Usage

```typescript
import { PaymentsRetrieveReceiptResponse } from "@x402api/sdk/models/operations";

let value: PaymentsRetrieveReceiptResponse = {};
```

## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `httpMeta`                                                            | [models.HTTPMetadata](../../models/http-metadata.md)                  | :heavy_check_mark:                                                    | N/A                                                                   |
| `paymentReceipt`                                                      | [models.PaymentReceipt](../../models/payment-receipt.md)              | :heavy_minus_sign:                                                    | Successful response for retrieve a payment receipt.                   |
| `paymentReceiptStatus`                                                | [models.PaymentReceiptStatus](../../models/payment-receipt-status.md) | :heavy_minus_sign:                                                    | Payment status while the signed finalized receipt is pending.         |
| `apiErrorEnvelope`                                                    | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)         | :heavy_minus_sign:                                                    | The request failed.                                                   |
