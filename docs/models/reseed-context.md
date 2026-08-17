# ReseedContext

## Example Usage

```typescript
import { ReseedContext } from "@x402api/sdk/models";

let value: ReseedContext = {
  checkpointId: "ff5c90da-76df-426c-a971-508b4d1948cf",
  network: "<value>",
  finality: "latest",
  manifestDigest: "<value>",
  policyDigest: "<value>",
  expectedGeneration: 258582,
  expectedNextBlockNumber: "<value>",
  expectedLastScannedBlockNumber: "<value>",
  expectedLastScannedBlockHash: "<value>",
  expectedReviewRequiredAt: new Date("2025-01-24T07:05:39.508Z"),
  expectedReviewErrorCode: "<value>",
  observedAt: new Date("2024-01-31T02:26:44.195Z"),
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