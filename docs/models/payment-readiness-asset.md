# PaymentReadinessAsset

## Example Usage

```typescript
import { PaymentReadinessAsset } from "@x402api/sdk/models";

let value: PaymentReadinessAsset = {
  assetId: "<id>",
  displayName: "Dangelo_Metz",
  contractAddress: "<value>",
  issuerNative: true,
  registryEnabled: true,
  tenantEnabled: false,
  operatorAssistanceEnabled: false,
  baseReadinessBlockers: [
    "<value 1>",
  ],
  challengeControlReady: true,
  settlementControlReady: true,
};
```

## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `assetId`                   | *string*                    | :heavy_check_mark:          | N/A                         |
| `displayName`               | *string*                    | :heavy_check_mark:          | N/A                         |
| `contractAddress`           | *string*                    | :heavy_check_mark:          | N/A                         |
| `issuerNative`              | *boolean*                   | :heavy_check_mark:          | N/A                         |
| `registryEnabled`           | *boolean*                   | :heavy_check_mark:          | N/A                         |
| `tenantEnabled`             | *boolean*                   | :heavy_check_mark:          | N/A                         |
| `operatorAssistanceEnabled` | *boolean*                   | :heavy_check_mark:          | N/A                         |
| `baseReadinessBlockers`     | *string*[]                  | :heavy_check_mark:          | N/A                         |
| `challengeControlReady`     | *boolean*                   | :heavy_check_mark:          | N/A                         |
| `settlementControlReady`    | *boolean*                   | :heavy_check_mark:          | N/A                         |