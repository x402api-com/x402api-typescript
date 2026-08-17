# PaymentReceipt

## Example Usage

```typescript
import { PaymentReceipt } from "@x402api/sdk/models";

let value: PaymentReceipt = {
  id: "378af1d7-4440-40ff-892e-1a88f886b509",
  orderId: "f58dde1a-dbab-4790-b485-176cfda84e32",
  settlementJobId: "57858006-cd65-431a-8440-af0369166018",
  receipt: "<value>",
  receiptDigest: "<value>",
  signature: "<value>",
  signingKeyVersion: "<value>",
  eligibleAlternatives: [],
  feePolicy: {
    type: "<value>",
    version: 699685,
    feeMode: "tenant_absorbs_up_to_cap",
    quoteCurrency: "USD",
    feeAllowanceCapQuoteMicros: "<value>",
  },
  feeEvidence: {
    type: "<value>",
    version: 647188,
    network: "<value>",
    assetId: "<id>",
    payloadProfile: "<value>",
  },
  feeQuoteDigest: "<value>",
  feeQuoteExpiresAt: new Date("2026-03-18T11:53:47.416Z"),
  settlementAmountAtomic: "<value>",
  createdAt: new Date("2024-10-17T10:26:37.869Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `orderId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `settlementJobId`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `receipt`                                                                                     | *any*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `receiptDigest`                                                                               | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `signature`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `signingKeyVersion`                                                                           | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `eligibleAlternatives`                                                                        | [models.NetworkFeeAlternative](../models/network-fee-alternative.md)[]                        | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feePolicy`                                                                                   | [models.FeePolicy](../models/fee-policy.md)                                                   | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeEvidence`                                                                                 | [models.FeeEvidence](../models/fee-evidence.md)                                               | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeQuoteDigest`                                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `feeQuoteExpiresAt`                                                                           | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `settlementAmountAtomic`                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |