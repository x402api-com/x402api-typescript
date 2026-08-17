# NetworkFeesCreateQuoteResponse

## Example Usage

```typescript
import { NetworkFeesCreateQuoteResponse } from "@x402api/sdk/models/operations";

let value: NetworkFeesCreateQuoteResponse = {};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `httpMeta`                                                                       | [models.HTTPMetadata](../../models/http-metadata.md)                             | :heavy_check_mark:                                                               | N/A                                                                              |
| `networkFeePreviewResponse`                                                      | [models.NetworkFeePreviewResponse](../../models/network-fee-preview-response.md) | :heavy_minus_sign:                                                               | Successful response for create a network-fee quote.                              |
| `apiErrorEnvelope`                                                               | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                    | :heavy_minus_sign:                                                               | The request failed with a stable machine-readable error.                         |