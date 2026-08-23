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
  status: "temporarily_unavailable",
  blockers: [],
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
| `status`                                                                                           | [models.CanonicalPaymentReadinessRailStatus](../models/canonical-payment-readiness-rail-status.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `blockers`                                                                                         | [models.PaymentReadinessBlocker](../models/payment-readiness-blocker.md)[]                         | :heavy_check_mark:                                                                                 | N/A                                                                                                |