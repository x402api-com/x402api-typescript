# TenantPaymentScreeningSubjectProjection

## Example Usage

```typescript
import { TenantPaymentScreeningSubjectProjection } from "@x402api/sdk/models";

let value: TenantPaymentScreeningSubjectProjection = {
  status: "allowed",
};
```

## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `status`                                                                                                                         | [models.TenantPaymentScreeningSubjectProjectionStatusEnum](../models/tenant-payment-screening-subject-projection-status-enum.md) | :heavy_check_mark:                                                                                                               | * `not_enforced` - not_enforced<br/>* `allowed` - allowed<br/>* `not_allowed` - not_allowed<br/>* `unavailable` - unavailable    |