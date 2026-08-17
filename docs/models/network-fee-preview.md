# NetworkFeePreview

## Example Usage

```typescript
import { NetworkFeePreview } from "@x402api/sdk/models";

let value: NetworkFeePreview = {
  prices: [],
};
```

## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `feeMode`                                                                 | [models.FeeMode](../models/fee-mode.md)                                   | :heavy_minus_sign:                                                        | N/A                                                                       |
| `quoteCurrency`                                                           | [models.QuoteCurrency](../models/quote-currency.md)                       | :heavy_minus_sign:                                                        | N/A                                                                       |
| `feeAllowanceCapQuoteMicros`                                              | *string*                                                                  | :heavy_minus_sign:                                                        | N/A                                                                       |
| `prices`                                                                  | [models.NetworkFeePreviewPrice](../models/network-fee-preview-price.md)[] | :heavy_check_mark:                                                        | N/A                                                                       |