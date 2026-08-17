# ResourcesCreateResponse

## Example Usage

```typescript
import { ResourcesCreateResponse } from "@x402api/sdk/models/operations";

let value: ResourcesCreateResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `resource`                                                    | [models.Resource](../../models/resource.md)                   | :heavy_minus_sign:                                            | Successful response for create a resource.                    |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed with a stable machine-readable error.      |