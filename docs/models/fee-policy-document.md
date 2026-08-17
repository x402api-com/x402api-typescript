# FeePolicyDocument

## Example Usage

```typescript
import { FeePolicyDocument } from "@x402api/sdk/models";

let value: FeePolicyDocument = {
  type: "<value>",
  version: 289760,
  feeMode: "buyer_pays",
  quoteCurrency: "USD",
  feeAllowanceCapQuoteMicros: "<value>",
};
```

## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `type`                                                                                      | *string*                                                                                    | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `version`                                                                                   | *number*                                                                                    | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `feeMode`                                                                                   | [models.FeePolicyModeInputEnum](../models/fee-policy-mode-input-enum.md)                    | :heavy_check_mark:                                                                          | * `buyer_pays` - buyer_pays<br/>* `tenant_absorbs_up_to_cap` - tenant_absorbs_up_to_cap     |
| `quoteCurrency`                                                                             | [models.FeePolicyQuoteCurrencyInputEnum](../models/fee-policy-quote-currency-input-enum.md) | :heavy_check_mark:                                                                          | * `USD` - USD                                                                               |
| `feeAllowanceCapQuoteMicros`                                                                | *string*                                                                                    | :heavy_check_mark:                                                                          | N/A                                                                                         |