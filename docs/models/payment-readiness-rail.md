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
  status: "<value>",
  blockers: [
    {
      code: "<value>",
      owner: "manual_platform_pause",
      message: "<value>",
    },
  ],
  tenantChallengesEnabled: false,
  tenantSettlementEnabled: false,
  networkAssistanceEnabled: false,
  challengeControlReady: false,
  settlementControlReady: true,
  assets: [],
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `assetId`                                                                  | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `network`                                                                  | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `symbol`                                                                   | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `selected`                                                                 | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `walletReady`                                                              | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `platformAvailable`                                                        | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `acceptingNewPayments`                                                     | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `status`                                                                   | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `blockers`                                                                 | [models.PaymentReadinessBlocker](../models/payment-readiness-blocker.md)[] | :heavy_check_mark:                                                         | N/A                                                                        |
| `tenantChallengesEnabled`                                                  | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `tenantSettlementEnabled`                                                  | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `networkAssistanceEnabled`                                                 | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `challengeControlReady`                                                    | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `settlementControlReady`                                                   | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `assets`                                                                   | [models.PaymentReadinessAsset](../models/payment-readiness-asset.md)[]     | :heavy_check_mark:                                                         | N/A                                                                        |