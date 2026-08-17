# WalletVersionBalance

## Example Usage

```typescript
import { WalletVersionBalance } from "@x402api/sdk/models";

let value: WalletVersionBalance = {
  walletVersionId: "99433028-3281-48ab-a213-490f9f8baea5",
  version: 247033,
  walletAddress: "<value>",
  state: "draining",
  observationState: "healthy",
  observedAt: new Date("2025-11-04T00:54:11.874Z"),
  assets: [
    {
      assetId: "<id>",
      displayName: "Dock42",
      symbol: "<value>",
      contractAddress: "<value>",
      decimals: 964015,
      amountAtomic: "<value>",
      amount: "638.26",
      issuerNative: true,
      observedAt: new Date("2024-04-26T14:11:57.298Z"),
      nodeSource: "<value>",
      sourceConsensus: "<value>",
      block: {
        number: "<value>",
        hash: "<value>",
        finality: "<value>",
      },
    },
  ],
  reseedContext: null,
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `walletVersionId`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `version`                                                                                     | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletAddress`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `state`                                                                                       | [models.WalletVersionBalanceStateEnum](../models/wallet-version-balance-state-enum.md)        | :heavy_check_mark:                                                                            | * `active` - active<br/>* `draining` - draining                                               |
| `observationState`                                                                            | [models.ObservationStateEnum](../models/observation-state-enum.md)                            | :heavy_check_mark:                                                                            | * `healthy` - healthy<br/>* `degraded` - degraded<br/>* `unavailable` - unavailable           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assets`                                                                                      | [models.BalanceAsset](../models/balance-asset.md)[]                                           | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `reseedContext`                                                                               | [models.ReseedContext](../models/reseed-context.md)                                           | :heavy_check_mark:                                                                            | N/A                                                                                           |