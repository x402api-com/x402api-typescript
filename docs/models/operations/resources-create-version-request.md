# ResourcesCreateVersionRequest

## Example Usage

```typescript
import { ResourcesCreateVersionRequest } from "@x402api/sdk/models/operations";

let value: ResourcesCreateVersionRequest = {
  idempotencyKey: "<value>",
  resourceId: "32367948-9f11-4a21-88d3-ec7d913d35af",
  body: {
    expectedLatestVersion: 193969,
    method: "GET",
    path: "/Applications",
    description:
      "snuggle nasalise unnaturally tremendously besmirch voluntarily as",
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
| `resourceId`                                                                                                                       | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `body`                                                                                                                             | [models.ResourceVersionCreate](../../models/resource-version-create.md)                                                            | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |