# NetworkFeePreviewResponse

## Example Usage

```typescript
import { NetworkFeePreviewResponse } from "@x402api/sdk/models";

let value: NetworkFeePreviewResponse = {
  feePolicy: {
    type: "<value>",
    version: 382903,
    feeMode: "tenant_absorbs_up_to_cap",
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
      providerDisagreementBps: 123225,
      feeAllowanceQuoteMicros: "<value>",
      feeAllowanceAtomic: "<value>",
      buyerPaymentAtomic: "<value>",
      tenantProceedsAtomic: "<value>",
      quoteExpiresAt: new Date("2026-12-13T08:24:16.315Z"),
      feeEvidence: {
        type: "<value>",
        version: 530752,
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