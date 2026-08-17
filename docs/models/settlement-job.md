# SettlementJob

## Example Usage

```typescript
import { SettlementJob } from "@x402api/sdk/models";

let value: SettlementJob = {
  id: "95668e4f-6d06-40b8-8ca3-5076bcdceb72",
  orderId: "7c87d591-09b6-4a51-ab57-2ffff19276fe",
  reservationId: "e43790e4-065b-4a10-ae1d-86e94b8c21df",
  state: "broadcast_unknown",
  network: "<value>",
  transactionHash: "<value>",
  originalTransactionHash: "<value>",
  replacedByHash: "<value>",
  gasExecutionState: "<value>",
  gasExecutionSequence: 488433,
  gasExecutionMaterialDigest: "<value>",
  gasExecutionObservedAt: new Date("2024-11-21T22:07:22.916Z"),
  payer: "<value>",
  lastErrorCode: "<value>",
  broadcastAttemptCount: 609805,
  settlementResult: "<value>",
  confirmedAt: new Date("2025-11-18T06:56:48.464Z"),
  finalizedAt: new Date("2025-11-25T22:02:32.976Z"),
  createdAt: new Date("2024-08-23T05:34:13.093Z"),
  updatedAt: new Date("2024-05-03T14:05:29.125Z"),
  order: {
    id: "81012182-a145-45a5-81a1-4f812e912c32",
    status: "<value>",
    buyerPaymentIdentifier: "<value>",
    paidAt: new Date("2025-08-21T12:31:09.331Z"),
    fulfilledAt: new Date("2025-05-23T05:41:21.640Z"),
  },
  resource: {
    id: "3135a18f-5723-4931-aa5e-03c7b3505d9e",
    key: "<key>",
    name: "<value>",
    version: 90265,
    method: "<value>",
    path: "/lib",
    description: "pressure hype shout bind fail terraform including edible own",
    fulfillmentMode: "<value>",
  },
  asset: {
    network: "<value>",
    contractAddress: "<value>",
    amountAtomic: "<value>",
    recipient: "<value>",
  },
  chain: {
    state: "Colorado",
    transactionHash: "<value>",
    blockNumber: "<value>",
    blockHash: "<value>",
    confirmations: 669522,
    confirmationsRequired: 163286,
    observedAt: new Date("2024-04-20T00:51:26.072Z"),
  },
  receipt: {
    status: "issued",
    id: "616b53c4-16ea-4173-89ce-4b39bcd15f2f",
    receiptDigest: "<value>",
    signingKeyVersion: "<value>",
    createdAt: new Date("2026-10-14T15:56:03.262Z"),
  },
  screening: {
    evaluatedAt: new Date("2025-11-23T19:58:22.324Z"),
    buyer: {
      status: "allowed",
    },
    recipient: {
      status: "not_allowed",
    },
  },
  fulfillment: {
    status: "not_created",
    id: null,
    mode: "<value>",
    state: "Delaware",
    attemptCount: 776097,
    lastErrorCode: "<value>",
    completedAt: new Date("2024-02-23T04:57:01.794Z"),
  },
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `orderId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `reservationId`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `state`                                                                                       | [models.SettlementJobState](../models/settlement-job-state.md)                                | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `transactionHash`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `originalTransactionHash`                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `replacedByHash`                                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `gasExecutionState`                                                                           | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `gasExecutionSequence`                                                                        | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `gasExecutionMaterialDigest`                                                                  | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `gasExecutionObservedAt`                                                                      | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `payer`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `lastErrorCode`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `broadcastAttemptCount`                                                                       | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `settlementResult`                                                                            | *any*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `confirmedAt`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `finalizedAt`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `order`                                                                                       | [models.SettlementJobOrder](../models/settlement-job-order.md)                                | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `resource`                                                                                    | [models.SettlementJobResource](../models/settlement-job-resource.md)                          | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `asset`                                                                                       | [models.Asset](../models/asset.md)                                                            | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `chain`                                                                                       | [models.Chain](../models/chain.md)                                                            | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `receipt`                                                                                     | [models.Receipt](../models/receipt.md)                                                        | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `screening`                                                                                   | [models.Screening](../models/screening.md)                                                    | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `fulfillment`                                                                                 | [models.Fulfillment](../models/fulfillment.md)                                                | :heavy_check_mark:                                                                            | N/A                                                                                           |