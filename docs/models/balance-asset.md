# BalanceAsset

## Example Usage

```typescript
import { BalanceAsset } from "@x402api/sdk/models";

let value: BalanceAsset = {
  assetId: "<id>",
  displayName: "Murl35",
  symbol: "<value>",
  contractAddress: "<value>",
  decimals: 128005,
  amountAtomic: "<value>",
  amount: "743.54",
  issuerNative: false,
  observedAt: new Date("2025-09-30T16:38:34.392Z"),
  nodeSource: "<value>",
  sourceConsensus: "<value>",
  block: {
    number: "<value>",
    hash: "<value>",
    finality: "<value>",
  },
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `assetId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `displayName`                                                                                 | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `symbol`                                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `contractAddress`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `decimals`                                                                                    | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `amountAtomic`                                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `amount`                                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `issuerNative`                                                                                | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `nodeSource`                                                                                  | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `sourceConsensus`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `block`                                                                                       | [models.ObservationBlock](../models/observation-block.md)                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |