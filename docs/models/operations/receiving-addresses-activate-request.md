# ReceivingAddressesActivateRequest

## Example Usage

```typescript
import { ReceivingAddressesActivateRequest } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesActivateRequest = {
  idempotencyKey: "<value>",
  readinessId: "801d2215-8e25-4d05-9d99-1f4f1eb56896",
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `readinessId`                                                                                                                      | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |