# ResourcesActivateVersionRequest

## Example Usage

```typescript
import { ResourcesActivateVersionRequest } from "@x402api/sdk/models/operations";

let value: ResourcesActivateVersionRequest = {
  idempotencyKey: "<value>",
  resourceId: "158a29d8-adb4-4656-8c6b-dfffa9f5b5a8",
  versionId: "af48fe43-4f17-4978-ae78-0faaf9452127",
  body: {
    expectedTargetVersion: 282284,
    expectedActiveVersionId: "8a6b4bf4-2514-4f44-9620-ded86e03b39b",
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `resourceId`                                                                                                                       | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `versionId`                                                                                                                        | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `body`                                                                                                                             | [models.ResourceVersionActivate](../../models/resource-version-activate.md)                                                        | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |