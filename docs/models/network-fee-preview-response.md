# NetworkFeePreviewResponse

## Example Usage

```typescript
import { NetworkFeePreviewResponse } from "@x402api/sdk/models";

let value: NetworkFeePreviewResponse = {
  feePolicy: {
    type: "<value>",
    version: 519921,
    feeMode: "buyer_pays",
    quoteCurrency: "USD",
    feeAllowanceCapQuoteMicros: "<value>",
  },
  alternatives: [
    {
      type: "<value>",
      version: 579672,
      network: "<value>",
      assetId: "<id>",
      contractAddress: "<value>",
      feeMode: "tenant_absorbs_up_to_cap",
      quoteCurrency: "USD",
      listedAmountAtomic: "<value>",
      feeAllowanceCapQuoteMicros: "<value>",
      estimatedNativeFeeAtomic: "<value>",
      nativeSymbol: "<value>",
      nativeDecimals: 870595,
      nativeUsdQuoteMicros: "<value>",
      estimatedFeeQuoteMicros: "<value>",
      gasMode: "sponsored",
      buyerNativeFeeAtomic: "<value>",
      maximumTenantGasReservationMicros: "<value>",
      providerDisagreementBps: 982984,
      feeAllowanceQuoteMicros: "<value>",
      feeAllowanceAtomic: "<value>",
      buyerPaymentAtomic: "<value>",
      tenantProceedsAtomic: "<value>",
      quoteExpiresAt: new Date("2025-11-16T16:33:25.883Z"),
      feeEvidence: {
        type: "<value>",
        version: 312,
        network: "<value>",
        assetId: "<id>",
        payloadProfile: "<value>",
      },
      feeEvidenceDigest: "<value>",
      eligible: true,
      exclusionReason: "<value>",
    },
  ],
  feeQuoteDigest: "<value>",
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `feePolicy`                                                            | [models.FeePolicyDocument](../models/fee-policy-document.md)           | :heavy_check_mark:                                                     | N/A                                                                    |
| `alternatives`                                                         | [models.NetworkFeeAlternative](../models/network-fee-alternative.md)[] | :heavy_check_mark:                                                     | N/A                                                                    |
| `feeQuoteDigest`                                                       | *string*                                                               | :heavy_check_mark:                                                     | N/A                                                                    |