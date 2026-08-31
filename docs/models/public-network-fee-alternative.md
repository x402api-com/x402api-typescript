# PublicNetworkFeeAlternative

## Example Usage

```typescript
import { PublicNetworkFeeAlternative } from "@x402api/sdk/models";

let value: PublicNetworkFeeAlternative = {
  type: "<value>",
  version: 735496,
  network: "<value>",
  assetId: "<id>",
  contractAddress: "<value>",
  listedAmountAtomic: "<value>",
  gasMode: "buyer_pays",
  buyerNativeFeeAtomic: "<value>",
  buyerPaymentAtomic: "<value>",
  tenantProceedsAtomic: "<value>",
  quoteExpiresAt: new Date("2024-04-15T08:19:53.300Z"),
  eligible: true,
  exclusionReason: "<value>",
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
| `listedAmountAtomic`                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `gasMode`                                                                                     | [models.GasModeEnum](../models/gas-mode-enum.md)                                              | :heavy_check_mark:                                                                            | * `buyer_pays` - buyer_pays<br/>* `sponsored` - sponsored                                     |
| `buyerNativeFeeAtomic`                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `buyerPaymentAtomic`                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tenantProceedsAtomic`                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `quoteExpiresAt`                                                                              | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `eligible`                                                                                    | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `exclusionReason`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |