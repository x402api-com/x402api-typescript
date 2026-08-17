# ResourcesCreateRequest

## Example Usage

```typescript
import { ResourcesCreateRequest } from "@x402api/sdk/models/operations";

let value: ResourcesCreateRequest = {
  idempotencyKey: "<value>",
  body: {
    key: "<key>",
    name: "<value>",
    method: "PATCH",
    path: "/proc",
    description: "gerbil blah phew perfectly blah runway meh ectoderm tenement",
    fulfillmentMode: "entitlement",
    prices: [
      {
        assetId: "<id>",
        walletVersionId: "fb3fc417-9cc2-4191-8a6d-7c9ce648745c",
        amountAtomic: "<value>",
        maxTimeoutSeconds: 662252,
      },
    ],
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `body`                                                                                                                             | [models.ResourceCreate](../../models/resource-create.md)                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |