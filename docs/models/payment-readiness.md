# PaymentReadiness

## Example Usage

```typescript
import { PaymentReadiness } from "@x402api/sdk/models";

let value: PaymentReadiness = {
  state: "accepting",
  acceptingNewPayments: false,
  readyForNewPayment: false,
  pausedByTenant: true,
  platformAvailable: true,
  healthValidUntil: new Date("2024-03-08T05:04:37.218Z"),
  observedAt: new Date("2026-02-11T17:25:12.143Z"),
  tenantStatus: "<value>",
  tenantAcceptingNewChallenges: false,
  globalChallengesEnabled: true,
  globalSettlementEnabled: true,
  controlPlaneReadyForNewChallenges: false,
  controlPlaneReadyForSettlement: true,
  externalOnboarding: "<value>",
  rails: [],
  canonicalRails: [
    {
      assetId: "<id>",
      network: "<value>",
      symbol: "<value>",
      selected: false,
      walletReady: true,
      platformAvailable: true,
      acceptingNewPayments: true,
      challengeControlReady: true,
      settlementControlReady: false,
      feeQuoteReady: true,
      feeQuoteValidUntil: new Date("2024-03-13T11:49:42.736Z"),
      readyForNewPayment: true,
      readinessValidUntil: new Date("2026-06-30T09:54:32.301Z"),
      status: "not_selected",
      blockers: [
        {
          code: "<value>",
          owner: "manual_platform_pause",
          message: "<value>",
        },
      ],
    },
  ],
};
```

## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `state`                                                                                                                 | [models.PaymentReadinessState](../models/payment-readiness-state.md)                                                    | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `acceptingNewPayments`                                                                                                  | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `readyForNewPayment`                                                                                                    | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `pausedByTenant`                                                                                                        | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `platformAvailable`                                                                                                     | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `healthValidUntil`                                                                                                      | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                           | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `observedAt`                                                                                                            | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                           | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `tenantStatus`                                                                                                          | *string*                                                                                                                | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| ~~`tenantAcceptingNewChallenges`~~                                                                                      | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| ~~`globalChallengesEnabled`~~                                                                                           | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| ~~`globalSettlementEnabled`~~                                                                                           | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| ~~`controlPlaneReadyForNewChallenges`~~                                                                                 | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| ~~`controlPlaneReadyForSettlement`~~                                                                                    | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| `externalOnboarding`                                                                                                    | *any*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `rails`                                                                                                                 | [models.PaymentReadinessRail](../models/payment-readiness-rail.md)[]                                                    | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `canonicalRails`                                                                                                        | [models.CanonicalPaymentReadinessRail](../models/canonical-payment-readiness-rail.md)[]                                 | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
