# ExternalAddressControlCapability

## Example Usage

```typescript
import { ExternalAddressControlCapability } from "@x402api/sdk/models";

let value: ExternalAddressControlCapability = {
  network: "<value>",
  proofMethods: [
    "onchain_canary",
  ],
};
```

## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `network`                                                                                             | *string*                                                                                              | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `proofMethods`                                                                                        | [models.ExternalAddressProofInputMethodEnum](../models/external-address-proof-input-method-enum.md)[] | :heavy_check_mark:                                                                                    | N/A                                                                                                   |