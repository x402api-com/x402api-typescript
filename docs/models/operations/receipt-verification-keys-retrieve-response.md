# ReceiptVerificationKeysRetrieveResponse

## Example Usage

```typescript
import { ReceiptVerificationKeysRetrieveResponse } from "@x402api/sdk/models/operations";

let value: ReceiptVerificationKeysRetrieveResponse = {};
```

## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `httpMeta`                                                                               | [models.HTTPMetadata](../../models/http-metadata.md)                                     | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `receiptVerificationKeyHistory`                                                          | [models.ReceiptVerificationKeyHistory](../../models/receipt-verification-key-history.md) | :heavy_minus_sign:                                                                       | Successful response for retrieve receipt verification keys.                              |
| `apiErrorEnvelope`                                                                       | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                            | :heavy_minus_sign:                                                                       | The request failed with a stable machine-readable error.                                 |