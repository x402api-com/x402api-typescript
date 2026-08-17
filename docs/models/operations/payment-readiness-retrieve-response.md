# PaymentReadinessRetrieveResponse

## Example Usage

```typescript
import { PaymentReadinessRetrieveResponse } from "@x402api/sdk/models/operations";

let value: PaymentReadinessRetrieveResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `paymentReadiness`                                            | [models.PaymentReadiness](../../models/payment-readiness.md)  | :heavy_minus_sign:                                            | Successful response for retrieve payment readiness.           |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |