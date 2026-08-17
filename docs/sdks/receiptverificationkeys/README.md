# ReceiptVerificationKeys

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve receipt verification keys

## retrieve

Return the public receipt verification-key history for out-of-band-pinned verification.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="receipt_verification_keys_retrieve" method="get" path="/v1/payment-receipt-verification-keys" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api();

async function run() {
  const result = await x402Api.receiptVerificationKeys.retrieve();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { receiptVerificationKeysRetrieve } from "@x402api/sdk/funcs/receipt-verification-keys-retrieve.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore();

async function run() {
  const res = await receiptVerificationKeysRetrieve(x402Api);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("receiptVerificationKeysRetrieve failed:", res.error);
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

**Promise\<[operations.ReceiptVerificationKeysRetrieveResponse](../../models/operations/receipt-verification-keys-retrieve-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |