# PaymentsListObservationsResponse

## Example Usage

```typescript
import { PaymentsListObservationsResponse } from "@x402api/sdk/models/operations";

let value: PaymentsListObservationsResponse = {};
```

## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `httpMeta`                                                                          | [models.HTTPMetadata](../../models/http-metadata.md)                                | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `paginatedSettlementChainObservationList`                                           | [models.SettlementChainObservation](../../models/settlement-chain-observation.md)[] | :heavy_minus_sign:                                                                  | Successful response for list payment observations.                                  |
| `apiErrorEnvelope`                                                                  | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                       | :heavy_minus_sign:                                                                  | The request failed with a stable machine-readable error.                            |