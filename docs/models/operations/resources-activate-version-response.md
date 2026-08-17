# ResourcesActivateVersionResponse

## Example Usage

```typescript
import { ResourcesActivateVersionResponse } from "@x402api/sdk/models/operations";

let value: ResourcesActivateVersionResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `resourceVersion`                                             | [models.ResourceVersion](../../models/resource-version.md)    | :heavy_minus_sign:                                            | Successful response for activate a resource version.          |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed.                                           |