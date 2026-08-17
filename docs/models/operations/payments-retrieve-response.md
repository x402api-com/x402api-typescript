# PaymentsRetrieveResponse

## Example Usage

```typescript
import { PaymentsRetrieveResponse } from "@x402api/sdk/models/operations";

let value: PaymentsRetrieveResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `settlementJob`                                               | [models.SettlementJob](../../models/settlement-job.md)        | :heavy_minus_sign:                                            | Successful response for retrieve a payment.                   |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |