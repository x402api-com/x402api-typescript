# Charges

## Overview

### Available Operations

* [create](#create) - Create a programmatic charge
* [retrieve](#retrieve) - Retrieve a programmatic charge
* [submitPayment](#submitpayment) - Submit a programmatic charge payment

## create

Create one idempotent dynamic charge and immutable PAYMENT-REQUIRED challenge from an active resource template. resource_version_id is the current active_version.id returned by GET /v1/resources, not the top-level resource id or pay_ public_payment_id. The 201 management response contains the canonical buyer challenge; it does not submit or settle payment. Requires a tenant API key with the `commerce:write` scope.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="charges_create" method="post" path="/v1/charges" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "<value>",
    body: {
      resourceVersionId: "aee1e97c-ebca-42b0-8a09-a29fca93ee2a",
      resourceUrl: "https://impressionable-sand.net",
      prices: [
        {
          assetId: "<id>",
          amountAtomic: "<value>",
        },
      ],
      expiresInSeconds: 652390,
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
    idempotencyKey: "<value>",
    body: {
      resourceVersionId: "aee1e97c-ebca-42b0-8a09-a29fca93ee2a",
      resourceUrl: "https://impressionable-sand.net",
      prices: [
        {
          assetId: "<id>",
          amountAtomic: "<value>",
        },
      ],
      expiresInSeconds: 652390,
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

Retrieve the frozen terms and current projected status of a tenant charge. Requires a tenant API key with the `commerce:read` scope.

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

## submitPayment

Submit one exact canonical PAYMENT-SIGNATURE for a tenant charge. The request body is empty. Preserve and retry the identical signature after HTTP 202 or 503; never create a replacement authorization for an ambiguous outcome. Requires a tenant API key with the `commerce:write` scope.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="charges_submit_payment" method="post" path="/v1/charges/{charge_id}/payments" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.submitPayment({
    paymentSignature: "<value>",
    chargeId: "d4ecf58a-9753-44e8-8116-85ac0a65642e",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { chargesSubmitPayment } from "@x402api/sdk/funcs/charges-submit-payment.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await chargesSubmitPayment(x402Api, {
    paymentSignature: "<value>",
    chargeId: "d4ecf58a-9753-44e8-8116-85ac0a65642e",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("chargesSubmitPayment failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ChargesSubmitPaymentRequest](../../models/operations/charges-submit-payment-request.md)                                                                            | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ChargesSubmitPaymentResponse](../../models/operations/charges-submit-payment-response.md)\>**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ApiErrorEnvelope | 400, 402, 404, 409      | application/json        |
| errors.ApiErrorEnvelope | 503                     | application/json        |
| errors.X402ApiError     | 4XX, 5XX                | \*/\*                   |