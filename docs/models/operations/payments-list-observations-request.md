# PaymentsListObservationsRequest

## Example Usage

```typescript
import { PaymentsListObservationsRequest } from "@x402api/sdk/models/operations";

let value: PaymentsListObservationsRequest = {
  id: "c53e83ad-f608-4c92-ba8b-b938724449d1",
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `cursor`                                                               | *string*                                                               | :heavy_minus_sign:                                                     | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link.  |
| `id`                                                                   | *string*                                                               | :heavy_check_mark:                                                     | N/A                                                                    |
| `pageSize`                                                             | *number*                                                               | :heavy_minus_sign:                                                     | Number of results in the bounded array page (default and maximum 100). |