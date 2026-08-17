# ResourceVersionCreate

## Example Usage

```typescript
import { ResourceVersionCreate } from "@x402api/sdk/models";

let value: ResourceVersionCreate = {
  expectedLatestVersion: 462914,
  method: "PATCH",
  path: "/etc",
  description: "quadruple after briefly enraged woeful gadzooks brr",
  fulfillmentMode: "entitlement",
  prices: [
    {
      assetId: "<id>",
      walletVersionId: "fb3fc417-9cc2-4191-8a6d-7c9ce648745c",
      amountAtomic: "<value>",
      maxTimeoutSeconds: 662252,
    },
  ],
};
```

## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `feeMode`                                                                                        | [models.ResourceVersionCreateFeeMode](../models/resource-version-create-fee-mode.md)             | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `quoteCurrency`                                                                                  | [models.ResourceVersionCreateQuoteCurrency](../models/resource-version-create-quote-currency.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `feeAllowanceCapQuoteMicros`                                                                     | *string*                                                                                         | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `expectedLatestVersion`                                                                          | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `method`                                                                                         | [models.HTTPMethodEnum](../models/http-method-enum.md)                                           | :heavy_check_mark:                                                                               | * `GET` - GET<br/>* `POST` - POST<br/>* `PUT` - PUT<br/>* `PATCH` - PATCH<br/>* `DELETE` - DELETE |
| `path`                                                                                           | *string*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `description`                                                                                    | *string*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `mimeType`                                                                                       | *string*                                                                                         | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `fulfillmentMode`                                                                                | [models.ResourceInputFulfillmentModeEnum](../models/resource-input-fulfillment-mode-enum.md)     | :heavy_check_mark:                                                                               | * `webhook` - webhook<br/>* `static` - static<br/>* `entitlement` - entitlement                  |
| `fulfillmentConfig`                                                                              | *models.ResourceVersionCreateFulfillmentConfig*                                                  | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `prices`                                                                                         | [models.PriceInput](../models/price-input.md)[]                                                  | :heavy_check_mark:                                                                               | N/A                                                                                              |