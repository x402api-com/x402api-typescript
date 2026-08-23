# SettlementChainObservation

## Example Usage

```typescript
import { SettlementChainObservation } from "@x402api/sdk/models";

let value: SettlementChainObservation = {
  id: "b040126b-d697-4d22-98da-fe64428af2ad",
  settlementJobId: "04cadac7-20a2-4342-89c3-2d68d688ec56",
  network: "<value>",
  transactionHash: "<value>",
  state: "reorged",
  observationDigest: "<value>",
  logIndex: 582371,
  blockNumber: "<value>",
  blockHash: "<value>",
  assetContract: "<value>",
  payer: "<value>",
  recipient: "<value>",
  amountAtomic: "<value>",
  executionSuccess: true,
  observedAt: new Date("2024-09-01T21:26:38.641Z"),
  createdAt: new Date("2025-02-03T13:37:21.656Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `settlementJobId`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `transactionHash`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `state`                                                                                       | [models.SettlementChainObservationState](../models/settlement-chain-observation-state.md)     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observationDigest`                                                                           | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `logIndex`                                                                                    | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `blockNumber`                                                                                 | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `blockHash`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assetContract`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `payer`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `recipient`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `amountAtomic`                                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `executionSuccess`                                                                            | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |