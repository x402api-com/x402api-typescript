# ReceivingAddressesListResponse

## Example Usage

```typescript
import { ReceivingAddressesListResponse } from "@x402api/sdk/models/operations";

let value: ReceivingAddressesListResponse = {};
```

## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `httpMeta`                                                                      | [models.HTTPMetadata](../../models/http-metadata.md)                            | :heavy_check_mark:                                                              | N/A                                                                             |
| `paginatedExternalReceivingAddressList`                                         | [models.ExternalReceivingAddress](../../models/external-receiving-address.md)[] | :heavy_minus_sign:                                                              | Successful response for list receiving addresses.                               |
| `apiErrorEnvelope`                                                              | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)                   | :heavy_minus_sign:                                                              | The request failed with a stable machine-readable error.                        |