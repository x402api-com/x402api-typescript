# ResourcesCreateVersionResponse

## Example Usage

```typescript
import { ResourcesCreateVersionResponse } from "@x402api/sdk/models/operations";

let value: ResourcesCreateVersionResponse = {};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `httpMeta`                                                    | [models.HTTPMetadata](../../models/http-metadata.md)          | :heavy_check_mark:                                            | N/A                                                           |
| `resourceVersion`                                             | [models.ResourceVersion](../../models/resource-version.md)    | :heavy_minus_sign:                                            | Successful response for create a resource version.            |
| `apiErrorEnvelope`                                            | [models.ApiErrorEnvelope](../../models/api-error-envelope.md) | :heavy_minus_sign:                                            | The request failed.                                           |