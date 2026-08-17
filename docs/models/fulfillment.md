# Fulfillment

## Example Usage

```typescript
import { Fulfillment } from "@x402api/sdk/models";

let value: Fulfillment = {
  status: "not_created",
  id: "13ecdb1d-34b5-4d48-8ddf-f513ab96f8ed",
  mode: "<value>",
  state: "West Virginia",
  attemptCount: 807227,
  lastErrorCode: "<value>",
  completedAt: new Date("2026-06-04T17:25:25.614Z"),
};
```

## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `status`                                                                                                              | [models.TenantPaymentFulfillmentProjectionStatusEnum](../models/tenant-payment-fulfillment-projection-status-enum.md) | :heavy_check_mark:                                                                                                    | * `not_created` - not_created<br/>* `created` - created                                                               |
| `id`                                                                                                                  | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `mode`                                                                                                                | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `state`                                                                                                               | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `attemptCount`                                                                                                        | *number*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `lastErrorCode`                                                                                                       | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `completedAt`                                                                                                         | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)                         | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |