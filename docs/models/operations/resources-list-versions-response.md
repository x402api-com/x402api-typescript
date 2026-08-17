# ResourcesListVersionsResponse

## Example Usage

```typescript
import { ResourcesListVersionsResponse } from "@x402api/sdk/models/operations";

let value: ResourcesListVersionsResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `paginatedResourceVersionList`                                | [models.ResourceVersion](../../models/resource-version.md)[]  | :heavy_minus_sign:                                            | Successful response for list resource versions.               |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |