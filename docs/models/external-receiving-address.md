# ExternalReceivingAddress

## Example Usage

```typescript
import { ExternalReceivingAddress } from "@x402api/sdk/models";

let value: ExternalReceivingAddress = {
  id: "53a4dc95-c8a6-471d-8355-058c24f3bda5",
  walletId: "9b6f7e81-a900-4544-abdf-170d497433c5",
  walletVersionId: "b10bda34-301f-4877-a6c2-d48df301e708",
  label: "<value>",
  network: "<value>",
  assetId: "<id>",
  address: "487 Maria Plains",
  status: "<value>",
  proofMethod: "signed_message",
  proofVerifiedAt: new Date("2025-08-27T10:58:36.607Z"),
  readinessState: "<value>",
  readinessUsable: true,
  readinessRefreshEligible: false,
  readinessStatus: "durable",
  activationEligible: false,
  activationEligibleAt: new Date("2025-08-17T10:13:06.625Z"),
  verifiedAt: new Date("2025-11-24T13:50:27.632Z"),
  expiresAt: new Date("2026-11-29T11:58:46.201Z"),
  activatedAt: new Date("2026-11-21T08:48:02.361Z"),
  observedBalanceAtomic: "<value>",
  createdAt: new Date("2024-08-26T15:25:05.704Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletId`                                                                                    | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `walletVersionId`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `label`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assetId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `address`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `status`                                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `proofMethod`                                                                                 | *models.ExternalReceivingAddressProofMethod*                                                  | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `proofVerifiedAt`                                                                             | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `readinessState`                                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `readinessUsable`                                                                             | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `readinessRefreshEligible`                                                                    | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `readinessStatus`                                                                             | [models.ReadinessStatus](../models/readiness-status.md)                                       | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `activationEligible`                                                                          | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `activationEligibleAt`                                                                        | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `verifiedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expiresAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `activatedAt`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observedBalanceAtomic`                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |