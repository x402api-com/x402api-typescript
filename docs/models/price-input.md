# PriceInput

## Example Usage

```typescript
import { PriceInput } from "@x402api/sdk/models";

let value: PriceInput = {
  assetId: "<id>",
  walletVersionId: "cc52aec0-00e9-4c26-9ee4-925c5e4512ea",
  amountAtomic: "<value>",
  maxTimeoutSeconds: 545059,
};
```

## Fields

| Field               | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `assetId`           | *string*            | :heavy_check_mark:  | N/A                 |
| `walletVersionId`   | *string*            | :heavy_check_mark:  | N/A                 |
| `amountAtomic`      | *string*            | :heavy_check_mark:  | N/A                 |
| `maxTimeoutSeconds` | *number*            | :heavy_check_mark:  | N/A                 |