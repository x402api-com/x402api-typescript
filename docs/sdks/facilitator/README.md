# Facilitator

## Overview

### Available Operations

* [getSupported](#getsupported) - Get supported facilitator profiles

## getSupported

Return the currently approved public x402 facilitator profiles.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="facilitator_get_supported" method="get" path="/v1/facilitator/supported" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api();

async function run() {
  const result = await x402Api.facilitator.getSupported();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { facilitatorGetSupported } from "@x402api/sdk/funcs/facilitator-get-supported.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore();

async function run() {
  const res = await facilitatorGetSupported(x402Api);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("facilitatorGetSupported failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.FacilitatorGetSupportedResponse](../../models/operations/facilitator-get-supported-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |