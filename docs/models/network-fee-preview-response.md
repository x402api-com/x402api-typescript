# NetworkFeePreviewResponse

## Example Usage

```typescript
import { NetworkFeePreviewResponse } from "@x402api/sdk/models";

let value: NetworkFeePreviewResponse = {
  feePolicy: {
    type: "<value>",
    version: 555497,
    feeMode: "tenant_absorbs_up_to_cap",
    quoteCurrency: "USD",
  },
  alternatives: [
    {
      type: "<value>",
      version: 579672,
      network: "<value>",
      assetId: "<id>",
      contractAddress: "<value>",
      listedAmountAtomic: "<value>",
      gasMode: "sponsored",
      buyerNativeFeeAtomic: "<value>",
      buyerPaymentAtomic: "<value>",
      tenantProceedsAtomic: "<value>",
      quoteExpiresAt: new Date("2026-07-07T03:04:14.742Z"),
      eligible: false,
      exclusionReason: "<value>",
    },
  ],
  feeQuoteDigest: "<value>",
};
```

## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `feePolicy`                                                                         | [models.PublicFeePolicyDocument](../models/public-fee-policy-document.md)           | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `alternatives`                                                                      | [models.PublicNetworkFeeAlternative](../models/public-network-fee-alternative.md)[] | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `feeQuoteDigest`                                                                    | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |