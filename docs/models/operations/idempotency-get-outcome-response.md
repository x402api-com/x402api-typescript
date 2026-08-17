# IdempotencyGetOutcomeResponse

## Example Usage

```typescript
import { IdempotencyGetOutcomeResponse } from "@x402api/sdk/models/operations";

let value: IdempotencyGetOutcomeResponse = {};
```

## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `httpMeta`                                                       | [models.HTTPMetadata](../../models/http-metadata.md)             | :heavy_check_mark:                                               | N/A                                                              |
| `idempotencyOutcome`                                             | [models.IdempotencyOutcome](../../models/idempotency-outcome.md) | :heavy_minus_sign:                                               | Successful response for get an idempotency outcome.              |
| `apiErrorEnvelope`                                               | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)    | :heavy_minus_sign:                                               | The request failed with a stable machine-readable error.         |