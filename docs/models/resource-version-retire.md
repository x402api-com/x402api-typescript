# ResourceVersionRetire

## Example Usage

```typescript
import { ResourceVersionRetire } from "@x402api/sdk/models";

let value: ResourceVersionRetire = {
  expectedVersion: 19199,
  expectedState: "draft",
};
```

## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `expectedVersion`                                                                                         | *number*                                                                                                  | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `expectedState`                                                                                           | [models.ResourceVersionRetireExpectedStateEnum](../models/resource-version-retire-expected-state-enum.md) | :heavy_check_mark:                                                                                        | * `draft` - draft<br/>* `active` - active                                                                 |