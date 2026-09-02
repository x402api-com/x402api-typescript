# FeeEvidence

Published shape for available and explicitly unavailable fee evidence.

## Example Usage

```typescript
import { FeeEvidence } from "@x402api/sdk/models";

let value: FeeEvidence = {
  type: "<value>",
  version: 537308,
  network: "<value>",
  assetId: "<id>",
  payloadProfile: "<value>",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `type`                                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `version`                                                                                     | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assetId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `payloadProfile`                                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `nativeSymbol`                                                                                | *string*                                                                                      | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `nativeDecimals`                                                                              | *number*                                                                                      | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `nativeFeeObservations`                                                                       | [models.NativeFeeObservationEvidence](../models/native-fee-observation-evidence.md)[]         | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `nativeUsdObservations`                                                                       | [models.NativeUsdObservationEvidence](../models/native-usd-observation-evidence.md)[]         | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `expiresAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_minus_sign:                                                                            | N/A                                                                                           |