# ReceivingAddressesGetControlCapabilitiesResponse

## Example Usage

```typescript
import { ReceivingAddressesGetControlCapabilitiesResponse } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesGetControlCapabilitiesResponse = {};
```

## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `httpMeta`                                                                                         | [models.HTTPMetadata](../../models/http-metadata.md)                                               | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `externalAddressControlCapabilities`                                                               | [models.ExternalAddressControlCapabilities](../../models/external-address-control-capabilities.md) | :heavy_minus_sign:                                                                                 | Successful response for get receiving-address control capabilities.                                |
| `apiErrorEnvelope`                                                                                 | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                                      | :heavy_minus_sign:                                                                                 | The request failed with a stable machine-readable error.                                           |