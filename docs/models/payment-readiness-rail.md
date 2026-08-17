# PaymentReadinessRail

## Example Usage

```typescript
import { PaymentReadinessRail } from "@x402api/sdk/models";

let value: PaymentReadinessRail = {
  network: "<value>",
  tenantChallengesEnabled: false,
  tenantSettlementEnabled: true,
  networkAssistanceEnabled: true,
  challengeControlReady: true,
  settlementControlReady: false,
  assets: [
    {
      assetId: "<id>",
      displayName: "Yasmeen_Simonis",
      contractAddress: "<value>",
      issuerNative: false,
      registryEnabled: true,
      tenantEnabled: true,
      operatorAssistanceEnabled: false,
      baseReadinessBlockers: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      challengeControlReady: false,
      settlementControlReady: false,
    },
  ],
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `network`                                                              | *string*                                                               | :heavy_check_mark:                                                     | N/A                                                                    |
| `tenantChallengesEnabled`                                              | *boolean*                                                              | :heavy_check_mark:                                                     | N/A                                                                    |
| `tenantSettlementEnabled`                                              | *boolean*                                                              | :heavy_check_mark:                                                     | N/A                                                                    |
| `networkAssistanceEnabled`                                             | *boolean*                                                              | :heavy_check_mark:                                                     | N/A                                                                    |
| `challengeControlReady`                                                | *boolean*                                                              | :heavy_check_mark:                                                     | N/A                                                                    |
| `settlementControlReady`                                               | *boolean*                                                              | :heavy_check_mark:                                                     | N/A                                                                    |
| `assets`                                                               | [models.PaymentReadinessAsset](../models/payment-readiness-asset.md)[] | :heavy_check_mark:                                                     | N/A                                                                    |