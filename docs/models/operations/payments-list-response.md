# PaymentsListResponse

## Example Usage

```typescript
import { PaymentsListResponse } from "@x402api/sdk/models/operations";

let value: PaymentsListResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `paginatedSettlementJobList`                                  | [models.SettlementJob](../../models/settlement-job.md)[]      | :heavy_minus_sign:                                            | Successful response for list payments.                        |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |