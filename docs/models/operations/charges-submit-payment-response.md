# ChargesSubmitPaymentResponse

## Example Usage

```typescript
import { ChargesSubmitPaymentResponse } from "@x402api/sdk/models/operations";

let value: ChargesSubmitPaymentResponse = {};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `httpMeta`                                                                             | [models.HTTPMetadata](../../models/http-metadata.md)                                   | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `dynamicChargePaymentResponse`                                                         | [models.DynamicChargePaymentResponse](../../models/dynamic-charge-payment-response.md) | :heavy_minus_sign:                                                                     | Successful response for submit a programmatic charge payment.                          |
| `apiErrorEnvelope`                                                                     | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                          | :heavy_minus_sign:                                                                     | The request failed.                                                                    |