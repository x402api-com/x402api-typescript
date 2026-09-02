# CanonicalPaymentReadinessRail

## Example Usage

```typescript
import { CanonicalPaymentReadinessRail } from "@x402api/sdk/models";

let value: CanonicalPaymentReadinessRail = {
  assetId: "<id>",
  network: "<value>",
  symbol: "<value>",
  selected: true,
  walletReady: true,
  platformAvailable: true,
  acceptingNewPayments: false,
  challengeControlReady: false,
  settlementControlReady: true,
  feeQuoteReady: false,
  feeQuoteValidUntil: new Date("2025-11-24T00:00:46.577Z"),
  readyForNewPayment: true,
  readinessValidUntil: new Date("2026-11-08T15:42:26.720Z"),
  status: "not_selected",
  blockers: [
    {
      code: "<value>",
      owner: "manual_platform_pause",
      message: "<value>",
    },
  ],
};
```

## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `assetId`                                                                                          | *string*                                                                                           | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `network`                                                                                          | *string*                                                                                           | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `symbol`                                                                                           | *string*                                                                                           | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `selected`                                                                                         | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `walletReady`                                                                                      | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `platformAvailable`                                                                                | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `acceptingNewPayments`                                                                             | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `challengeControlReady`                                                                            | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `settlementControlReady`                                                                           | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `feeQuoteReady`                                                                                    | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `feeQuoteValidUntil`                                                                               | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)      | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `readyForNewPayment`                                                                               | *boolean*                                                                                          | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `readinessValidUntil`                                                                              | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)      | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `status`                                                                                           | [models.CanonicalPaymentReadinessRailStatus](../models/canonical-payment-readiness-rail-status.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `blockers`                                                                                         | [models.PaymentReadinessBlocker](../models/payment-readiness-blocker.md)[]                         | :heavy_check_mark:                                                                                 | N/A                                                                                                |