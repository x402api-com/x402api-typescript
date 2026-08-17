# Resource

## Example Usage

```typescript
import { Resource } from "@x402api/sdk/models";

let value: Resource = {
  id: "bb4906c9-ddac-4512-97bf-d9db56c3ec92",
  publicPaymentId: "<id>",
  key: "<key>",
  name: "<value>",
  activeVersion: {
    id: "71d5d2e3-dfae-4718-9775-b096659e1fe9",
    version: 220061,
    method: "<value>",
    path: "/opt/lib",
    description:
      "charlatan representation reel abaft peppery carelessly loudly ah healthily",
    mimeType: "<value>",
    fulfillmentMode: "webhook",
    fulfillmentConfig: {
      entitlementKey: "<value>",
      quantityAtomic: "<value>",
      provisionerAdapterId: "4fc9d05e-13a4-4547-b8cc-d0ec69586962",
    },
    feeMode: "buyer_pays",
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
  },
  versions: [],
  createdAt: new Date("2026-03-19T06:03:47.279Z"),
  updatedAt: new Date("2026-01-18T23:01:46.827Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `publicPaymentId`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `key`                                                                                         | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `name`                                                                                        | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `activeVersion`                                                                               | [models.ActiveVersion](../models/active-version.md)                                           | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `versions`                                                                                    | [models.ResourceVersion](../models/resource-version.md)[]                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |