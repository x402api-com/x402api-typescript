# ReceivingAddressesActivateResponse

## Example Usage

```typescript
import { ReceivingAddressesActivateResponse } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesActivateResponse = {};
```

## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `httpMeta`                                                                    | [models.HTTPMetadata](../../models/http-metadata.md)                          | :heavy_check_mark:                                                            | N/A                                                                           |
| `externalReceivingAddress`                                                    | [models.ExternalReceivingAddress](../../models/external-receiving-address.md) | :heavy_minus_sign:                                                            | Successful response for activate a receiving address.                         |
| `apiErrorEnvelope`                                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                 | :heavy_minus_sign:                                                            | The request failed with a stable machine-readable error.                      |