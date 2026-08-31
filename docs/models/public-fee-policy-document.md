# PublicFeePolicyDocument

## Example Usage

```typescript
import { PublicFeePolicyDocument } from "@x402api/sdk/models";

let value: PublicFeePolicyDocument = {
  type: "<value>",
  version: 393685,
  feeMode: "buyer_pays",
  quoteCurrency: "USD",
};
```

## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `type`                                                                                      | *string*                                                                                    | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `version`                                                                                   | *number*                                                                                    | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `feeMode`                                                                                   | [models.FeePolicyModeInputEnum](../models/fee-policy-mode-input-enum.md)                    | :heavy_check_mark:                                                                          | * `buyer_pays` - buyer_pays<br/>* `tenant_absorbs_up_to_cap` - tenant_absorbs_up_to_cap     |
| `quoteCurrency`                                                                             | [models.FeePolicyQuoteCurrencyInputEnum](../models/fee-policy-quote-currency-input-enum.md) | :heavy_check_mark:                                                                          | * `USD` - USD                                                                               |