# PaymentReadiness

## Example Usage

```typescript
import { PaymentReadiness } from "@x402api/sdk/models";

let value: PaymentReadiness = {
  state: "accepting",
  acceptingNewPayments: false,
  pausedByTenant: false,
  platformAvailable: true,
  healthValidUntil: new Date("2025-03-03T02:32:14.246Z"),
  observedAt: new Date("2025-11-07T17:09:00.734Z"),
  tenantStatus: "<value>",
  tenantAcceptingNewChallenges: true,
  globalChallengesEnabled: false,
  globalSettlementEnabled: false,
  controlPlaneReadyForNewChallenges: true,
  controlPlaneReadyForSettlement: true,
  externalOnboarding: "<value>",
  rails: [
    {
      assetId: "<id>",
      network: "<value>",
      symbol: "<value>",
      selected: true,
      walletReady: true,
      platformAvailable: false,
      acceptingNewPayments: false,
      status: "<value>",
      blockers: [],
      tenantChallengesEnabled: true,
      tenantSettlementEnabled: true,
      networkAssistanceEnabled: true,
      challengeControlReady: false,
      settlementControlReady: true,
      assets: [],
    },
  ],
  canonicalRails: [],
};
```

## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `state`                                                                                                                 | [models.PaymentReadinessState](../models/payment-readiness-state.md)                                                    | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `acceptingNewPayments`                                                                                                  | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
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