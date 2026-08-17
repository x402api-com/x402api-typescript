# Wallets

## Overview

### Available Operations

* [retrieveBalance](#retrievebalance) - Retrieve wallet balances

## retrieveBalance

Retrieve finalized external-wallet balance observations at the requested finality.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="wallets_retrieve_balance" method="get" path="/v1/wallets/{id}/balances" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.wallets.retrieveBalance({
    id: "c1f2a3df-2c04-4581-9a87-37857b52b3e9",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { walletsRetrieveBalance } from "@x402api/sdk/funcs/wallets-retrieve-balance.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await walletsRetrieveBalance(x402Api, {
    id: "c1f2a3df-2c04-4581-9a87-37857b52b3e9",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("walletsRetrieveBalance failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.WalletsRetrieveBalanceRequest](../../models/operations/wallets-retrieve-balance-request.md)                                                                        | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.WalletsRetrieveBalanceResponse](../../models/operations/wallets-retrieve-balance-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |