# ReceivingAddressesRefreshReadinessResponse

## Example Usage

```typescript
import { ReceivingAddressesRefreshReadinessResponse } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesRefreshReadinessResponse = {};
```

## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `httpMeta`                                                                    | [models.HTTPMetadata](../../models/http-metadata.md)                          | :heavy_check_mark:                                                            | N/A                                                                           |
| `externalReceivingAddress`                                                    | [models.ExternalReceivingAddress](../../models/external-receiving-address.md) | :heavy_minus_sign:                                                            | Successful response for refresh receiving-address readiness.                  |
| `apiErrorEnvelope`                                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                 | :heavy_minus_sign:                                                            | The request failed with a stable machine-readable error.                      |