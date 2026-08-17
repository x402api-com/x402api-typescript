# ExternalAddressControlChallengeCreate

Reject extra or missing JSON keys instead of silently projecting them.

## Example Usage

```typescript
import { ExternalAddressControlChallengeCreate } from "@x402api/sdk/models";

let value: ExternalAddressControlChallengeCreate = {
  network: "<value>",
  assetId: "<id>",
  address: "787 W Monroe Street",
  proofMethod: "onchain_canary",
};
```

## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `network`                                                                                           | *string*                                                                                            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `assetId`                                                                                           | *string*                                                                                            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `address`                                                                                           | *string*                                                                                            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `proofMethod`                                                                                       | [models.ExternalAddressProofInputMethodEnum](../models/external-address-proof-input-method-enum.md) | :heavy_check_mark:                                                                                  | * `signed_message` - signed_message<br/>* `onchain_canary` - onchain_canary                         |