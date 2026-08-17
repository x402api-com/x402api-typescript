# ResourcesRetireVersionRequest

## Example Usage

```typescript
import { ResourcesRetireVersionRequest } from "@x402api/sdk/models/operations";

let value: ResourcesRetireVersionRequest = {
  idempotencyKey: "<value>",
  resourceId: "f9a8f3ae-6be5-4cb9-a452-7587ad22623c",
  versionId: "2dabe736-42e0-404f-8a4f-ee4dc4d2b1b4",
  body: {
    expectedVersion: 915501,
    expectedState: "draft",
  },
};
```

## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `idempotencyKey`                                                                                                                   | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
| `resourceId`                                                                                                                       | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `versionId`                                                                                                                        | *string*                                                                                                                           | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `body`                                                                                                                             | [models.ResourceVersionRetire](../../models/resource-version-retire.md)                                                            | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |