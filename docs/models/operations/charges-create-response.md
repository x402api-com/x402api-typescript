# ChargesCreateResponse

## Example Usage

```typescript
import { ChargesCreateResponse } from "@x402api/sdk/models/operations";

let value: ChargesCreateResponse = {};
```

## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `httpMeta`                                                              | [models.HTTPMetadata](../../models/http-metadata.md)                    | :heavy_check_mark:                                                      | N/A                                                                     |
| `dynamicChargeResponse`                                                 | [models.DynamicChargeResponse](../../models/dynamic-charge-response.md) | :heavy_minus_sign:                                                      | Successful response for create a programmatic charge.                   |
| `apiErrorEnvelope`                                                      | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)           | :heavy_minus_sign:                                                      | The request failed.                                                     |