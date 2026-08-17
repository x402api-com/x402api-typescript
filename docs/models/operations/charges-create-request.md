# ChargesCreateRequest

## Example Usage

```typescript
import { ChargesCreateRequest } from "@x402api/sdk/models/operations";

let value: ChargesCreateRequest = {
  idempotencyKey: "<value>",
  body: {
    resourceVersionId: "b1238902-acfa-4f9a-8c21-fc5bb3e08222",
    resourceUrl: "https://fluffy-arcade.name/",
    prices: [
      {
        assetId: "<id>",
        amountAtomic: "<value>",
      },
    ],
    expiresInSeconds: 989020,
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `body`                                                                                                                             | [models.DynamicChargeCreate](../../models/dynamic-charge-create.md)                                                                | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |