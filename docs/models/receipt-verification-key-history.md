# ReceiptVerificationKeyHistory

## Example Usage

```typescript
import { ReceiptVerificationKeyHistory } from "@x402api/sdk/models";

let value: ReceiptVerificationKeyHistory = {
  type: "<value>",
  keys: {
    "key": {
      algorithm: "<value>",
      publicKeyBase64: "<value>",
      keyFingerprint: "<value>",
    },
  },
};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `type`                                                                                 | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `keys`                                                                                 | Record<string, [models.ReceiptVerificationKey](../models/receipt-verification-key.md)> | :heavy_check_mark:                                                                     | N/A                                                                                    |