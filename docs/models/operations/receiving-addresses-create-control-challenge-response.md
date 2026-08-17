# ReceivingAddressesCreateControlChallengeResponse

## Example Usage

```typescript
import { ReceivingAddressesCreateControlChallengeResponse } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesCreateControlChallengeResponse = {};
```

## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `httpMeta`                                                                                   | [models.HTTPMetadata](../../models/http-metadata.md)                                         | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `externalAddressControlChallenge`                                                            | [models.ExternalAddressControlChallenge](../../models/external-address-control-challenge.md) | :heavy_minus_sign:                                                                           | Successful response for create a receiving-address control challenge.                        |
| `apiErrorEnvelope`                                                                           | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                                | :heavy_minus_sign:                                                                           | The request failed with a stable machine-readable error.                                     |