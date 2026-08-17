# ActiveVersion

## Example Usage

```typescript
import { ActiveVersion } from "@x402api/sdk/models";

let value: ActiveVersion = {
  id: "ef18d017-773e-4bb6-8a42-d3077ca70d1d",
  version: 609715,
  method: "<value>",
  path: "/usr/share",
  description: "closely deprave pupil saw mythology trash",
  mimeType: "<value>",
  fulfillmentMode: "webhook",
  fulfillmentConfig: {},
  feeMode: "tenant_absorbs_up_to_cap",
  quoteCurrency: "USD",
  feeAllowanceCapQuoteMicros: "<value>",
  state: "active",
  prices: [
    {
      assetId: "<id>",
      network: "<value>",
      contractAddress: "<value>",
      displayName: "Kayli_Metz",
      symbol: "<value>",
      decimals: 149019,
      walletId: "f57dada4-fee1-4d0c-8123-fcfb907660ff",
      walletVersionId: "af0ecde9-60a8-49bf-86ce-ac1751ec3249",
      recipient: "<value>",
      amountAtomic: "<value>",
      listedAmountAtomic: "<value>",
      maxTimeoutSeconds: 604713,
    },
  ],
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `version`                                                                | *number*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `method`                                                                 | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `path`                                                                   | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `description`                                                            | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `mimeType`                                                               | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `fulfillmentMode`                                                        | [models.ResourceFulfillmentMode](../models/resource-fulfillment-mode.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `fulfillmentConfig`                                                      | *models.ResourceFulfillmentConfig*                                       | :heavy_check_mark:                                                       | N/A                                                                      |
| `feeMode`                                                                | [models.ResourceFeeMode](../models/resource-fee-mode.md)                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `quoteCurrency`                                                          | [models.ResourceQuoteCurrency](../models/resource-quote-currency.md)     | :heavy_check_mark:                                                       | N/A                                                                      |
| `feeAllowanceCapQuoteMicros`                                             | *string*                                                                 | :heavy_check_mark:                                                       | N/A                                                                      |
| `state`                                                                  | [models.ResourceState](../models/resource-state.md)                      | :heavy_check_mark:                                                       | N/A                                                                      |
| `prices`                                                                 | [models.ResourcePrice](../models/resource-price.md)[]                    | :heavy_check_mark:                                                       | N/A                                                                      |