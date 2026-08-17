# ReceivingAddressesRotateResponse

## Example Usage

```typescript
import { ReceivingAddressesRotateResponse } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesRotateResponse = {};
```

## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `httpMeta`                                                                    | [models.HTTPMetadata](../../models/http-metadata.md)                          | :heavy_check_mark:                                                            | N/A                                                                           |
| `externalReceivingAddress`                                                    | [models.ExternalReceivingAddress](../../models/external-receiving-address.md) | :heavy_minus_sign:                                                            | Successful response for rotate a receiving address.                           |
| `apiErrorEnvelope`                                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                 | :heavy_minus_sign:                                                            | The request failed with a stable machine-readable error.                      |