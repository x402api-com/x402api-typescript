# SupportedResponse

## Example Usage

```typescript
import { SupportedResponse } from "@x402api/sdk/models";

let value: SupportedResponse = {
  kinds: [
    {
      x402Version: 186680,
      scheme: "<value>",
      network: "<value>",
    },
  ],
  extensions: [
    "<value 1>",
    "<value 2>",
  ],
  signers: {},
};
```

## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `kinds`                                               | [models.SupportedKind](../models/supported-kind.md)[] | :heavy_check_mark:                                    | N/A                                                   |
| `extensions`                                          | *string*[]                                            | :heavy_check_mark:                                    | N/A                                                   |
| `signers`                                             | Record<string, *string*[]>                            | :heavy_check_mark:                                    | N/A                                                   |