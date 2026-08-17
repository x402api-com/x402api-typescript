# WalletFencedChainReseedContext

## Example Usage

```typescript
import { WalletFencedChainReseedContext } from "@x402api/sdk/models";

let value: WalletFencedChainReseedContext = {
  checkpointId: "34ff234e-be68-4b4c-8a2c-7cf9614b02fb",
  network: "<value>",
  finality: "confirmed",
  manifestDigest: "<value>",
  policyDigest: "<value>",
  expectedGeneration: 985762,
  expectedNextBlockNumber: "<value>",
  expectedLastScannedBlockNumber: "<value>",
  expectedLastScannedBlockHash: "<value>",
  expectedReviewRequiredAt: new Date("2025-11-15T13:00:59.586Z"),
  expectedReviewErrorCode: "<value>",
  observedAt: new Date("2024-10-20T21:33:02.343Z"),
  walletVersionId: "f35cc782-fb86-44d3-8a73-00e0e436fc5c",
  walletVersion: 123019,
  walletAddress: "<value>",
  walletVersionState: "active",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `checkpointId`                                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `finality`                                                                                    | [models.WalletObservationFinalityEnum](../models/wallet-observation-finality-enum.md)         | :heavy_check_mark:                                                                            | * `latest` - latest<br/>* `confirmed` - confirmed<br/>* `finalized` - finalized               |
| `manifestDigest`                                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `policyDigest`                                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expectedGeneration`                                                                          | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expectedNextBlockNumber`                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expectedLastScannedBlockNumber`                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expectedLastScannedBlockHash`                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expectedReviewRequiredAt`                                                                    | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expectedReviewErrorCode`                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletVersionId`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletVersion`                                                                               | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletAddress`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletVersionState`                                                                          | [models.WalletVersionStateEnum](../models/wallet-version-state-enum.md)                       | :heavy_check_mark:                                                                            | * `pending` - pending<br/>* `active` - active<br/>* `draining` - draining<br/>* `revoked` - revoked |