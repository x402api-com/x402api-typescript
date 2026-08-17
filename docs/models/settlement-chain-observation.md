# SettlementChainObservation

## Example Usage

```typescript
import { SettlementChainObservation } from "@x402api/sdk/models";
import { Decimal } from "@x402api/sdk/types";

let value: SettlementChainObservation = {
  id: "b040126b-d697-4d22-98da-fe64428af2ad",
  settlementJobId: "04cadac7-20a2-4342-89c3-2d68d688ec56",
  network: "<value>",
  transactionHash: "<value>",
  state: "reorged",
  observationDigest: "<value>",
  logIndex: 582371,
  blockNumber: new Decimal("5214.96"),
  blockHash: "<value>",
  assetContract: "<value>",
  payer: "<value>",
  recipient: "<value>",
  amountAtomic: new Decimal("225.91"),
  executionSuccess: true,
  observedAt: new Date("2024-10-22T06:48:19.155Z"),
  createdAt: new Date("2025-01-05T06:07:25.216Z"),
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
| `blockNumber`                                                                                 | *Decimal*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `blockHash`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assetContract`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `payer`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `recipient`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `amountAtomic`                                                                                | *Decimal*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `executionSuccess`                                                                            | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |