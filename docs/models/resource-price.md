# ResourcePrice

## Example Usage

```typescript
import { ResourcePrice } from "@x402api/sdk/models";

let value: ResourcePrice = {
  assetId: "<id>",
  network: "<value>",
  contractAddress: "<value>",
  displayName: "Jarod_Hackett",
  symbol: "<value>",
  decimals: 614761,
  walletId: "b5b4016c-f8d0-4ef8-9c2a-1a6feeae3a23",
  walletVersionId: "c49f0fab-ac33-4886-9666-83560b6b7203",
  recipient: "<value>",
  amountAtomic: "<value>",
  listedAmountAtomic: "<value>",
  maxTimeoutSeconds: 115340,
};
```

## Fields

| Field                | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `assetId`            | *string*             | :heavy_check_mark:   | N/A                  |
| `network`            | *string*             | :heavy_check_mark:   | N/A                  |
| `contractAddress`    | *string*             | :heavy_check_mark:   | N/A                  |
| `displayName`        | *string*             | :heavy_check_mark:   | N/A                  |
| `symbol`             | *string*             | :heavy_check_mark:   | N/A                  |
| `decimals`           | *number*             | :heavy_check_mark:   | N/A                  |
| `walletId`           | *string*             | :heavy_check_mark:   | N/A                  |
| `walletVersionId`    | *string*             | :heavy_check_mark:   | N/A                  |
| `recipient`          | *string*             | :heavy_check_mark:   | N/A                  |
| `amountAtomic`       | *string*             | :heavy_check_mark:   | N/A                  |
| `listedAmountAtomic` | *string*             | :heavy_check_mark:   | N/A                  |
| `maxTimeoutSeconds`  | *number*             | :heavy_check_mark:   | N/A                  |