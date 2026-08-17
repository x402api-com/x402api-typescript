# WalletBalanceResponse

## Example Usage

```typescript
import { WalletBalanceResponse } from "@x402api/sdk/models";

let value: WalletBalanceResponse = {
  walletId: "e7dd97c5-eae2-485e-94f8-e3546366347a",
  network: "<value>",
  walletAddress: null,
  requestedFinality: "latest",
  observationState: "healthy",
  observedAt: new Date("2025-10-25T11:19:56.569Z"),
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
  walletVersions: [],
  reseedContexts: [],
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `walletId`                                                                                    | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletAddress`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `requestedFinality`                                                                           | [models.WalletObservationFinalityEnum](../models/wallet-observation-finality-enum.md)         | :heavy_check_mark:                                                                            | * `latest` - latest<br/>* `confirmed` - confirmed<br/>* `finalized` - finalized               |
| `observationState`                                                                            | [models.ObservationStateEnum](../models/observation-state-enum.md)                            | :heavy_check_mark:                                                                            | * `healthy` - healthy<br/>* `degraded` - degraded<br/>* `unavailable` - unavailable           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assets`                                                                                      | [models.BalanceAsset](../models/balance-asset.md)[]                                           | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletVersions`                                                                              | [models.WalletVersionBalance](../models/wallet-version-balance.md)[]                          | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `reseedContexts`                                                                              | [models.WalletFencedChainReseedContext](../models/wallet-fenced-chain-reseed-context.md)[]    | :heavy_check_mark:                                                                            | N/A                                                                                           |