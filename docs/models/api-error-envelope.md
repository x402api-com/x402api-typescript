# ApiErrorEnvelope

## Example Usage

```typescript
import { ApiErrorEnvelope } from "@x402api/sdk/models";

let value: ApiErrorEnvelope = {
  error: {
    status: 991506,
    code: "<value>",
    detail: "<value>",
  },
};
```

## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `error`                                   | [models.ApiError](../models/api-error.md) | :heavy_check_mark:                        | N/A                                       |