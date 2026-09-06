# PaymentReadinessRail

## Example Usage

```typescript
import { PaymentReadinessRail } from "@x402api/sdk/models";

let value: PaymentReadinessRail = {
  assetId: "<id>",
  network: "<value>",
  symbol: "<value>",
  selected: false,
  walletReady: true,
  platformAvailable: true,
  acceptingNewPayments: true,
  readyForNewPayment: false,
  readinessValidUntil: new Date("2026-12-19T09:40:18.076Z"),
  feeQuoteReady: false,
  feeQuoteValidUntil: new Date("2026-12-18T06:59:29.286Z"),
  status: "<value>",
  blockers: [],
  tenantChallengesEnabled: true,
  tenantSettlementEnabled: false,
  networkAssistanceEnabled: true,
  challengeControlReady: true,
  settlementControlReady: false,
  assets: [
    {
      assetId: "<id>",
      displayName: "Julianne.Langosh99",
      contractAddress: "<value>",
      issuerNative: false,
      registryEnabled: false,
      tenantEnabled: true,
      operatorAssistanceEnabled: true,
      baseReadinessBlockers: [
        "<value 1>",
      ],
      challengeControlReady: false,
      settlementControlReady: true,
    },
  ],
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `assetId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `symbol`                                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `selected`                                                                                    | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletReady`                                                                                 | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `platformAvailable`                                                                           | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `acceptingNewPayments`                                                                        | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `readyForNewPayment`                                                                          | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `readinessValidUntil`                                                                         | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeQuoteReady`                                                                               | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeQuoteValidUntil`                                                                          | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `status`                                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `blockers`                                                                                    | [models.PaymentReadinessBlocker](../models/payment-readiness-blocker.md)[]                    | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tenantChallengesEnabled`                                                                     | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tenantSettlementEnabled`                                                                     | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `networkAssistanceEnabled`                                                                    | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `challengeControlReady`                                                                       | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `settlementControlReady`                                                                      | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assets`                                                                                      | [models.PaymentReadinessAsset](../models/payment-readiness-asset.md)[]                        | :heavy_check_mark:                                                                            | N/A                                                                                           |
