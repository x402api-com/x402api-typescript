# ExternalAddressControlProofInput

Reject extra or missing JSON keys instead of silently projecting them.

## Example Usage

```typescript
import { ExternalAddressControlProofInput } from "@x402api/sdk/models";

let value: ExternalAddressControlProofInput = {
  method: "signed_message",
};
```

## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `method`                                                                                            | [models.ExternalAddressProofInputMethodEnum](../models/external-address-proof-input-method-enum.md) | :heavy_check_mark:                                                                                  | * `signed_message` - signed_message<br/>* `onchain_canary` - onchain_canary                         |
| `signature`                                                                                         | *string*                                                                                            | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `transactionHash`                                                                                   | *string*                                                                                            | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |