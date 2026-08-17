# ExternalAddressControlChallenge

## Example Usage

```typescript
import { ExternalAddressControlChallenge } from "@x402api/sdk/models";

let value: ExternalAddressControlChallenge = {
  id: "eda36850-5582-4c37-8f1a-2d7ad1e77166",
  network: "<value>",
  assetId: "<id>",
  addressDisplay: "<value>",
  proofMethod: "onchain_canary",
  message: "<value>",
  challengeDigest: "<value>",
  canaryInstructions: "<value>",
  expiresAt: new Date("2026-10-23T15:54:08.558Z"),
  consumedAt: new Date("2026-07-25T17:25:54.854Z"),
  createdAt: new Date("2025-01-03T10:25:30.485Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `network`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `assetId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `addressDisplay`                                                                              | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `proofMethod`                                                                                 | [models.ProofMethod](../models/proof-method.md)                                               | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `message`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `challengeDigest`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `canaryInstructions`                                                                          | *any*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `expiresAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `consumedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |