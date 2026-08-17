# ReceivingAddressesRefreshReadinessRequest

## Example Usage

```typescript
import { ReceivingAddressesRefreshReadinessRequest } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesRefreshReadinessRequest = {
  idempotencyKey: "<value>",
  readinessId: "9327b864-419b-44ea-a329-2af2be8f8248",
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `readinessId`                                                                                                                      | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |