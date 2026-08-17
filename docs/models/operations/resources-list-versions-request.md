# ResourcesListVersionsRequest

## Example Usage

```typescript
import { ResourcesListVersionsRequest } from "@x402api/sdk/models/operations";

let value: ResourcesListVersionsRequest = {
  resourceId: "7cf39d58-ce2e-45d1-b1f9-2253c98aa853",
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `cursor`                                                               | *string*                                                               | :heavy_minus_sign:                                                     | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link.  |
| `pageSize`                                                             | *number*                                                               | :heavy_minus_sign:                                                     | Number of results in the bounded array page (default and maximum 100). |
| `resourceId`                                                           | *string*                                                               | :heavy_check_mark:                                                     | N/A                                                                    |