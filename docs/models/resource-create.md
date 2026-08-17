# ResourceCreate

## Example Usage

```typescript
import { ResourceCreate } from "@x402api/sdk/models";

let value: ResourceCreate = {
  key: "<key>",
  name: "<value>",
  method: "PUT",
  path: "/opt/share",
  description: "essay yet provided like mismatch blah indeed shush zowie",
  fulfillmentMode: "webhook",
  prices: [],
};
```

## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `feeMode`                                                                                    | [models.ResourceCreateFeeMode](../models/resource-create-fee-mode.md)                        | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `quoteCurrency`                                                                              | [models.ResourceCreateQuoteCurrency](../models/resource-create-quote-currency.md)            | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `feeAllowanceCapQuoteMicros`                                                                 | *string*                                                                                     | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `key`                                                                                        | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `name`                                                                                       | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `method`                                                                                     | [models.HTTPMethodEnum](../models/http-method-enum.md)                                       | :heavy_check_mark:                                                                           | * `GET` - GET<br/>* `POST` - POST<br/>* `PUT` - PUT<br/>* `PATCH` - PATCH<br/>* `DELETE` - DELETE |
| `path`                                                                                       | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `description`                                                                                | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `mimeType`                                                                                   | *string*                                                                                     | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `fulfillmentMode`                                                                            | [models.ResourceInputFulfillmentModeEnum](../models/resource-input-fulfillment-mode-enum.md) | :heavy_check_mark:                                                                           | * `webhook` - webhook<br/>* `static` - static<br/>* `entitlement` - entitlement              |
| `fulfillmentConfig`                                                                          | *models.ResourceCreateFulfillmentConfig*                                                     | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `prices`                                                                                     | [models.PriceInput](../models/price-input.md)[]                                              | :heavy_check_mark:                                                                           | N/A                                                                                          |