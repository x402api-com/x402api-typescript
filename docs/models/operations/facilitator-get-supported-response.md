# FacilitatorGetSupportedResponse

## Example Usage

```typescript
import { FacilitatorGetSupportedResponse } from "@x402api/sdk/models/operations";

let value: FacilitatorGetSupportedResponse = {};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `httpMeta`                                                     | [models.HTTPMetadata](../../models/http-metadata.md)           | :heavy_check_mark:                                             | N/A                                                            |
| `supportedResponse`                                            | [models.SupportedResponse](../../models/supported-response.md) | :heavy_minus_sign:                                             | Successful response for get supported facilitator profiles.    |
| `apiErrorEnvelope`                                             | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)  | :heavy_minus_sign:                                             | The request failed with a stable machine-readable error.       |