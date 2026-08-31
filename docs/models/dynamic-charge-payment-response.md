# DynamicChargePaymentResponse

## Example Usage

```typescript
import { DynamicChargePaymentResponse } from "@x402api/sdk/models";

let value: DynamicChargePaymentResponse = {
  chargeId: "09a47394-7026-4ab1-af28-7eb1db233afe",
  orderId: "bce83b14-5215-4564-8995-3fa4890bef74",
  paymentId: "beb2a8f5-d464-447c-bd96-115d8aec006a",
  state: "Louisiana",
  payer: "<value>",
  transaction: "<value>",
  network: "<value>",
  errorReason: "<value>",
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `chargeId`                                                      | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `orderId`                                                       | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `paymentId`                                                     | *string*                                                        | :heavy_check_mark:                                              | Durable settlement identifier used by payment and receipt APIs. |
| `state`                                                         | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `payer`                                                         | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `transaction`                                                   | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `network`                                                       | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `errorReason`                                                   | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |