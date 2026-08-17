# ApiError

## Example Usage

```typescript
import { ApiError } from "@x402api/sdk/models";

let value: ApiError = {
  status: 23788,
  code: "<value>",
  detail: "<value>",
};
```

## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `status`                                                    | *number*                                                    | :heavy_check_mark:                                          | HTTP response status.                                       |
| `code`                                                      | *string*                                                    | :heavy_check_mark:                                          | Stable machine-readable error code.                         |
| `detail`                                                    | *any*                                                       | :heavy_check_mark:                                          | Human-readable text or structured field validation details. |