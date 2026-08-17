# Charges

## Overview

### Available Operations

* [create](#create) - Create a programmatic charge
* [retrieve](#retrieve) - Retrieve a programmatic charge

## create

Create one idempotent dynamic charge with immutable x402 payment terms.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="charges_create" method="post" path="/v1/charges" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "charge-example-001",
    body: {
      resourceVersionId: "00000000-0000-4000-8000-000000000001",
      resourceUrl: "https://merchant.example/products/pro-plan",
      prices: [
        {
          assetId: "base_usdc",
          amountAtomic: "1000000",
        },
      ],
      expiresInSeconds: 900,
    },
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { chargesCreate } from "@x402api/sdk/funcs/charges-create.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await chargesCreate(x402Api, {
    idempotencyKey: "charge-example-001",
    body: {
      resourceVersionId: "00000000-0000-4000-8000-000000000001",
      resourceUrl: "https://merchant.example/products/pro-plan",
      prices: [
        {
          assetId: "base_usdc",
          amountAtomic: "1000000",
        },
      ],
      expiresInSeconds: 900,
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("chargesCreate failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ChargesCreateRequest](../../models/operations/charges-create-request.md)                                                                                           | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ChargesCreateResponse](../../models/operations/charges-create-response.md)\>**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ApiErrorEnvelope | 409, 422                | application/json        |
| errors.X402ApiError     | 4XX, 5XX                | \*/\*                   |

## retrieve

Retrieve the frozen terms and current projected status of a tenant charge.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="charges_retrieve" method="get" path="/v1/charges/{charge_id}" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.retrieve({
    chargeId: "5769b058-4489-472a-bf4c-54470a13ba4a",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { chargesRetrieve } from "@x402api/sdk/funcs/charges-retrieve.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await chargesRetrieve(x402Api, {
    chargeId: "5769b058-4489-472a-bf4c-54470a13ba4a",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("chargesRetrieve failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ChargesRetrieveRequest](../../models/operations/charges-retrieve-request.md)                                                                                       | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ChargesRetrieveResponse](../../models/operations/charges-retrieve-response.md)\>**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ApiErrorEnvelope | 404                     | application/json        |
| errors.X402ApiError     | 4XX, 5XX                | \*/\*                   |
