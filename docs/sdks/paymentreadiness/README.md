# PaymentReadiness

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve payment readiness

## retrieve

Return the tenant's current external-wallet payment-readiness projection.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="payment_readiness_retrieve" method="get" path="/v1/payment-readiness" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.paymentReadiness.retrieve();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { paymentReadinessRetrieve } from "@x402api/sdk/funcs/payment-readiness-retrieve.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await paymentReadinessRetrieve(x402Api);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("paymentReadinessRetrieve failed:", res.error);
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

**Promise\<[operations.PaymentReadinessRetrieveResponse](../../models/operations/payment-readiness-retrieve-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |