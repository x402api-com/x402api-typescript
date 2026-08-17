# PaymentReadiness

## Example Usage

```typescript
import { PaymentReadiness } from "@x402api/sdk/models";

let value: PaymentReadiness = {
  observedAt: new Date("2024-06-21T14:32:52.163Z"),
  tenantStatus: "<value>",
  tenantAcceptingNewChallenges: false,
  globalChallengesEnabled: false,
  globalSettlementEnabled: true,
  controlPlaneReadyForNewChallenges: true,
  controlPlaneReadyForSettlement: false,
  externalOnboarding: "<value>",
  rails: [],
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tenantStatus`                                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tenantAcceptingNewChallenges`                                                                | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `globalChallengesEnabled`                                                                     | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `globalSettlementEnabled`                                                                     | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `controlPlaneReadyForNewChallenges`                                                           | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `controlPlaneReadyForSettlement`                                                              | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `externalOnboarding`                                                                          | *any*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `rails`                                                                                       | [models.PaymentReadinessRail](../models/payment-readiness-rail.md)[]                          | :heavy_check_mark:                                                                            | N/A                                                                                           |