# ReceivingAddressesRotateRequest

## Example Usage

```typescript
import { ReceivingAddressesRotateRequest } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesRotateRequest = {
  idempotencyKey: "<value>",
  readinessId: "07fd8238-826c-4d17-96ad-e255d81cf390",
  body: {
    challengeId: "b34b9be6-0a43-424e-aa50-baa499a59a93",
    proof: {
      method: "signed_message",
    },
    reason: "<value>",
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `readinessId`                                                                                                                      | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `body`                                                                                                                             | [models.ExternalReceivingAddressRotation](../../models/external-receiving-address-rotation.md)                                     | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |