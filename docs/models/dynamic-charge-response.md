# DynamicChargeResponse

## Example Usage

```typescript
import { DynamicChargeResponse } from "@x402api/sdk/models";

let value: DynamicChargeResponse = {
  chargeId: "a10990cc-e0a7-4d74-93dc-7af1a49c1814",
  chargeDigest: "<value>",
  orderId: "686f173d-520b-4e36-9d24-f5e6cd6bac6e",
  status: "<value>",
  resourceVersionId: "0efb322f-aa94-4a2c-b778-8f4949ae80e1",
  paymentIdentifier: "<value>",
  expiresAt: new Date("2025-04-16T10:07:50.606Z"),
  createdAt: new Date("2026-05-05T17:34:36.308Z"),
  prices: [
    {
      assetId: "<id>",
      amountAtomic: "<value>",
    },
  ],
  requestedExpiresInSeconds: 671031,
  metadata: {
    "key": "<value>",
    "key1": "<value>",
  },
  metadataDigest: "<value>",
  paymentRequired: "<value>",
  paymentRequiredHeader: "<value>",
  eligibleAlternatives: [
    {
      type: "<value>",
      version: 767689,
      network: "<value>",
      assetId: "<id>",
      contractAddress: "<value>",
      feeMode: "tenant_absorbs_up_to_cap",
      quoteCurrency: "USD",
      listedAmountAtomic: "<value>",
      feeAllowanceCapQuoteMicros: "<value>",
      estimatedNativeFeeAtomic: "<value>",
      nativeSymbol: "<value>",
      nativeDecimals: 351973,
      nativeUsdQuoteMicros: "<value>",
      estimatedFeeQuoteMicros: "<value>",
      providerDisagreementBps: 498775,
      feeAllowanceQuoteMicros: "<value>",
      feeAllowanceAtomic: "<value>",
      buyerPaymentAtomic: "<value>",
      tenantProceedsAtomic: "<value>",
      quoteExpiresAt: new Date("2025-09-12T13:27:21.073Z"),
      feeEvidence: {
        type: "<value>",
        version: 530752,
        network: "<value>",
        assetId: "<id>",
        payloadProfile: "<value>",
      },
      feeEvidenceDigest: "<value>",
      eligible: true,
      exclusionReason: null,
    },
  ],
  feePolicy: {
    type: "<value>",
    version: 382903,
    feeMode: "tenant_absorbs_up_to_cap",
    quoteCurrency: "USD",
    feeAllowanceCapQuoteMicros: "<value>",
  },
  feeQuoteDigest: "<value>",
};
```

## Fields

| Field                                                                                                                                 | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `chargeId`                                                                                                                            | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `chargeDigest`                                                                                                                        | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `orderId`                                                                                                                             | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `status`                                                                                                                              | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `resourceVersionId`                                                                                                                   | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `paymentIdentifier`                                                                                                                   | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `expiresAt`                                                                                                                           | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                         | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `createdAt`                                                                                                                           | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                         | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `prices`                                                                                                                              | [models.DynamicChargePrice](../models/dynamic-charge-price.md)[]                                                                      | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `requestedExpiresInSeconds`                                                                                                           | *number*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `metadata`                                                                                                                            | Record<string, *any*>                                                                                                                 | :heavy_check_mark:                                                                                                                    | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. |
| `metadataDigest`                                                                                                                      | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `paymentRequired`                                                                                                                     | *any*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `paymentRequiredHeader`                                                                                                               | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `eligibleAlternatives`                                                                                                                | [models.NetworkFeeAlternative](../models/network-fee-alternative.md)[]                                                                | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `feePolicy`                                                                                                                           | [models.FeePolicyDocument](../models/fee-policy-document.md)                                                                          | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `feeQuoteDigest`                                                                                                                      | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |