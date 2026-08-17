# ExternalReceivingAddressRotation

Reject extra or missing JSON keys instead of silently projecting them.

## Example Usage

```typescript
import { ExternalReceivingAddressRotation } from "@x402api/sdk/models";

let value: ExternalReceivingAddressRotation = {
  challengeId: "ab69ac9b-359a-4e8a-aabf-7b017be3e8e4",
  proof: {
    method: "signed_message",
  },
  reason: "<value>",
};
```

## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `challengeId`                                                                                | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `proof`                                                                                      | [models.ExternalAddressControlProofInput](../models/external-address-control-proof-input.md) | :heavy_check_mark:                                                                           | Reject extra or missing JSON keys instead of silently projecting them.                       |
| `reason`                                                                                     | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |