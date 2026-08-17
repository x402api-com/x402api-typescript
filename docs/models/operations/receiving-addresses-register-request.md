# ReceivingAddressesRegisterRequest

## Example Usage

```typescript
import { ReceivingAddressesRegisterRequest } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesRegisterRequest = {
  idempotencyKey: "<value>",
  body: {
    label: "<value>",
    challengeId: "6ba5c501-5b75-4c74-86fa-8396f3e7e608",
    proof: {
      method: "signed_message",
    },
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `body`                                                                                                                             | [models.ExternalReceivingAddressCreate](../../models/external-receiving-address-create.md)                                         | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |