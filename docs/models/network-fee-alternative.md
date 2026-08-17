# NetworkFeeAlternative

## Example Usage

```typescript
import { NetworkFeeAlternative } from "@x402api/sdk/models";

let value: NetworkFeeAlternative = {
  type: "<value>",
  version: 607196,
  network: "<value>",
  assetId: "<id>",
  contractAddress: "<value>",
  feeMode: "buyer_pays",
  quoteCurrency: "USD",
  listedAmountAtomic: "<value>",
  feeAllowanceCapQuoteMicros: "<value>",
  estimatedNativeFeeAtomic: "<value>",
  nativeSymbol: "<value>",
  nativeDecimals: 881455,
  nativeUsdQuoteMicros: "<value>",
  estimatedFeeQuoteMicros: "<value>",
  providerDisagreementBps: null,
  feeAllowanceQuoteMicros: "<value>",
  feeAllowanceAtomic: "<value>",
  buyerPaymentAtomic: "<value>",
  tenantProceedsAtomic: "<value>",
  quoteExpiresAt: new Date("2025-03-03T21:19:26.953Z"),
  feeEvidence: {
    type: "<value>",
    version: 530752,
    network: "<value>",
    assetId: "<id>",
    payloadProfile: "<value>",
  },
  feeEvidenceDigest: "<value>",
  eligible: false,
  exclusionReason: null,
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `type`                                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `version`                                                                                     | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assetId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `contractAddress`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeMode`                                                                                     | [models.FeePolicyModeInputEnum](../models/fee-policy-mode-input-enum.md)                      | :heavy_check_mark:                                                                            | * `buyer_pays` - buyer_pays<br/>* `tenant_absorbs_up_to_cap` - tenant_absorbs_up_to_cap       |
| `quoteCurrency`                                                                               | [models.FeePolicyQuoteCurrencyInputEnum](../models/fee-policy-quote-currency-input-enum.md)   | :heavy_check_mark:                                                                            | * `USD` - USD                                                                                 |
| `listedAmountAtomic`                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeAllowanceCapQuoteMicros`                                                                  | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `estimatedNativeFeeAtomic`                                                                    | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `nativeSymbol`                                                                                | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `nativeDecimals`                                                                              | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `nativeUsdQuoteMicros`                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `estimatedFeeQuoteMicros`                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `providerDisagreementBps`                                                                     | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeAllowanceQuoteMicros`                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeAllowanceAtomic`                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `buyerPaymentAtomic`                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tenantProceedsAtomic`                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `quoteExpiresAt`                                                                              | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeEvidence`                                                                                 | [models.NetworkFeeEvidence](../models/network-fee-evidence.md)                                | :heavy_check_mark:                                                                            | Published shape for available and explicitly unavailable fee evidence.                        |
| `feeEvidenceDigest`                                                                           | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `eligible`                                                                                    | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `exclusionReason`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |