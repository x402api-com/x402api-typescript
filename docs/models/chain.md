# Chain

## Example Usage

```typescript
import { Chain } from "@x402api/sdk/models";

let value: Chain = {
  state: "Kentucky",
  transactionHash: "<value>",
  blockNumber: null,
  blockHash: "<value>",
  confirmations: 937946,
  confirmationsRequired: 803284,
  observedAt: new Date("2024-02-02T08:03:13.547Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `state`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `transactionHash`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `blockNumber`                                                                                 | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `blockHash`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `confirmations`                                                                               | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `confirmationsRequired`                                                                       | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `observedAt`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | N/A                                                                                           |