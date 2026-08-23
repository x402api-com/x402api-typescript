# PaymentReadinessBlocker

## Example Usage

```typescript
import { PaymentReadinessBlocker } from "@x402api/sdk/models";

let value: PaymentReadinessBlocker = {
  code: "<value>",
  owner: "tenant_action",
  message: "<value>",
};
```

## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `code`                             | *string*                           | :heavy_check_mark:                 | N/A                                |
| `owner`                            | [models.Owner](../models/owner.md) | :heavy_check_mark:                 | N/A                                |
| `message`                          | *string*                           | :heavy_check_mark:                 | N/A                                |
| `actionUrl`                        | *string*                           | :heavy_minus_sign:                 | N/A                                |