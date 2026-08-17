# PaymentsRetrieveReceiptResponse

## Example Usage

```typescript
import { PaymentsRetrieveReceiptResponse } from "@x402api/sdk/models/operations";

let value: PaymentsRetrieveReceiptResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `paymentReceipt`                                              | [models.PaymentReceipt](../../models/payment-receipt.md)      | :heavy_minus_sign:                                            | Successful response for retrieve a payment receipt.           |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |