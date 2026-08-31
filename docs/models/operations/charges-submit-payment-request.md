# ChargesSubmitPaymentRequest

## Example Usage

```typescript
import { ChargesSubmitPaymentRequest } from "@x402api/sdk/models/operations";

let value: ChargesSubmitPaymentRequest = {
  paymentSignature: "<value>",
  chargeId: "78324c41-0479-4e03-860a-181aec74fafe",
};
```

## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `paymentSignature`                               | *string*                                         | :heavy_check_mark:                               | Canonical base64-encoded x402 v2 PaymentPayload. |
| `chargeId`                                       | *string*                                         | :heavy_check_mark:                               | N/A                                              |