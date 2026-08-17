# ReceivingAddressesCreateControlChallengeRequest

## Example Usage

```typescript
import { ReceivingAddressesCreateControlChallengeRequest } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesCreateControlChallengeRequest = {
  idempotencyKey: "<value>",
  body: {
    network: "<value>",
    assetId: "<id>",
    address: "29656 Baker Street",
    proofMethod: "signed_message",
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `body`                                                                                                                             | [models.ExternalAddressControlChallengeCreate](../../models/external-address-control-challenge-create.md)                          | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |