# ExternalReceivingAddressCreate

Reject extra or missing JSON keys instead of silently projecting them.

## Example Usage

```typescript
import { ExternalReceivingAddressCreate } from "@x402api/sdk/models";

let value: ExternalReceivingAddressCreate = {
  label: "<value>",
  challengeId: "4f804a65-bb97-42dd-9d21-cc00839c20e4",
  proof: {
    method: "signed_message",
  },
};
```

## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `label`                                                                                      | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `challengeId`                                                                                | *string*                                                                                     | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `proof`                                                                                      | [models.ExternalAddressControlProofInput](../models/external-address-control-proof-input.md) | :heavy_check_mark:                                                                           | Reject extra or missing JSON keys instead of silently projecting them.                       |