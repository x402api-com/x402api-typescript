# ResourceVersion

## Example Usage

```typescript
import { ResourceVersion } from "@x402api/sdk/models";

let value: ResourceVersion = {
  id: "ff7ef2e7-8b1b-4104-bc0d-a06c29d64cfa",
  version: 303887,
  method: "<value>",
  path: "/private/var",
  description: "till owlishly sonnet phew um indolent determined",
  mimeType: "<value>",
  fulfillmentMode: "static",
  fulfillmentConfig: {},
  feeMode: "tenant_absorbs_up_to_cap",
  quoteCurrency: "USD",
  feeAllowanceCapQuoteMicros: "<value>",
  state: "active",
  prices: [],
};
```

## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `version`                                                                           | *number*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `method`                                                                            | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `path`                                                                              | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `description`                                                                       | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `mimeType`                                                                          | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `fulfillmentMode`                                                                   | [models.FulfillmentMode](../models/fulfillment-mode.md)                             | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `fulfillmentConfig`                                                                 | *models.FulfillmentConfig*                                                          | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `feeMode`                                                                           | [models.ResourceVersionFeeMode](../models/resource-version-fee-mode.md)             | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `quoteCurrency`                                                                     | [models.ResourceVersionQuoteCurrency](../models/resource-version-quote-currency.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `feeAllowanceCapQuoteMicros`                                                        | *string*                                                                            | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `state`                                                                             | [models.ResourceVersionState](../models/resource-version-state.md)                  | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `prices`                                                                            | [models.ResourcePrice](../models/resource-price.md)[]                               | :heavy_check_mark:                                                                  | N/A                                                                                 |