# Screening

## Example Usage

```typescript
import { Screening } from "@x402api/sdk/models";

let value: Screening = {
  evaluatedAt: new Date("2025-08-18T18:24:26.456Z"),
  buyer: {
    status: "allowed",
  },
  recipient: {
    status: "not_allowed",
  },
};
```

## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `evaluatedAt`                                                                                              | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)              | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `buyer`                                                                                                    | [models.TenantPaymentScreeningSubjectProjection](../models/tenant-payment-screening-subject-projection.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `recipient`                                                                                                | [models.TenantPaymentScreeningSubjectProjection](../models/tenant-payment-screening-subject-projection.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |