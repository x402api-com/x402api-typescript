# ResourcesListResponse

## Example Usage

```typescript
import { ResourcesListResponse } from "@x402api/sdk/models/operations";

let value: ResourcesListResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `paginatedResourceList`                                       | [models.Resource](../../models/resource.md)[]                 | :heavy_minus_sign:                                            | Successful response for list resources.                       |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |