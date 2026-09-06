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
      listedAmountAtomic: "<value>",
      gasMode: "sponsored",
      buyerNativeFeeAtomic: "<value>",
      buyerPaymentAtomic: "<value>",
      tenantProceedsAtomic: "<value>",
      quoteExpiresAt: new Date("2026-03-17T11:04:28.621Z"),
      eligible: true,
      exclusionReason: "<value>",
    },
  ],
  feePolicy: {
    type: "<value>",
    version: 555497,
    feeMode: "tenant_absorbs_up_to_cap",
    quoteCurrency: "USD",
  },
  feeQuoteDigest: "<value>",
};
```

## Fields

| Field                                                                                                                                 | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `chargeId`                                                                                                                            | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | Immutable challenge UUID created for this charge.                                                                                     |
| `chargeDigest`                                                                                                                        | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `orderId`                                                                                                                             | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `status`                                                                                                                              | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | Current projected order status; payment terms remain immutable.                                                                       |
| `resourceVersionId`                                                                                                                   | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `paymentIdentifier`                                                                                                                   | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | Opaque server challenge handle. Return it to the buyer as X-X402API-Challenge-Handle; it is not the buyer payment identifier.         |
| `expiresAt`                                                                                                                           | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                         | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `humanCheckoutUrl`                                                                                                                    | *string*                                                                                                                              | :heavy_minus_sign:                                                                                                                    | Optional HTTPS hosted checkout for this exact charge. It is a short-lived bearer capability and expires with expires_at.              |
| `qrPayload`                                                                                                                           | *string*                                                                                                                              | :heavy_minus_sign:                                                                                                                    | Optional canonical hosted-checkout URL to encode as a QR; never a recipient address.                                                  |
| `createdAt`                                                                                                                           | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                                         | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `prices`                                                                                                                              | [models.DynamicChargePrice](../models/dynamic-charge-price.md)[]                                                                      | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `requestedExpiresInSeconds`                                                                                                           | *number*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `metadata`                                                                                                                            | Record<string, *any*>                                                                                                                 | :heavy_check_mark:                                                                                                                    | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. |
| `metadataDigest`                                                                                                                      | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `paymentRequired`                                                                                                                     | *any*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | Complete immutable x402 v2 PAYMENT-REQUIRED document.                                                                                 |
| `paymentRequiredHeader`                                                                                                               | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | Canonical base64-encoded value to return in the buyer-facing PAYMENT-REQUIRED header.                                                 |
| `eligibleAlternatives`                                                                                                                | [models.PublicNetworkFeeAlternative](../models/public-network-fee-alternative.md)[]                                                   | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `feePolicy`                                                                                                                           | [models.PublicFeePolicyDocument](../models/public-fee-policy-document.md)                                                             | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `feeQuoteDigest`                                                                                                                      | *string*                                                                                                                              | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |