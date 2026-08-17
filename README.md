# x402api TypeScript and JavaScript SDK

Official server-side TypeScript and JavaScript SDK for the x402api public API.
The package name is `@x402api/sdk` and the production API endpoint is
`https://api.x402api.com`.

> **Release status:** this repository contains the generation and release
> configuration. The package installation command becomes available when the
> first synchronized SDK release is published.

## Requirements

Node.js 22 or newer.

## Installation

```bash
npm install @x402api/sdk
# or: pnpm add @x402api/sdk
```

## Using the x402api TypeScript and JavaScript SDK

The examples below show the configured public surface. Generated request and
response model names are documented under `docs/` after the first SDK generation.

### Configure authentication

Create a scoped tenant API key in x402api and expose it to the server process as
`X402API_TENANT_API_KEY`. The SDK sends it as a bearer credential. Never embed a
tenant API key in browser, mobile, desktop, or other distributed client code.

### Initialize the client

```typescript
import { X402Api } from "@x402api/sdk";

const sdk = new X402Api({
  tenantApiKey: process.env.X402API_TENANT_API_KEY ?? "",
});

const readiness = await sdk.paymentReadiness.retrieve();
const payments = await sdk.payments.list({ pageSize: 25 });

console.log(readiness);
console.log(payments);
```

The idiomatic method shape for this SDK is `sdk.resourceName.methodName(request)`.
All request fields are collected into a typed request object so new optional API
fields do not break existing call sites.

### Create a charge

The logical SDK call is `charges.create`. Supply a unique `Idempotency-Key` for
each intended mutation and reuse the same key only when retrying that exact
request. The request contains a resource-version UUID, the protected URL, one or
more asset prices expressed in atomic units, and an expiry between 30 and 3600
seconds.

The equivalent HTTP request is useful for validating credentials independently
of the SDK:

```bash
curl --request POST https://api.x402api.com/v1/charges \
  --header "Authorization: Bearer $X402API_TENANT_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: charge-$(date +%s)" \
  --data '{
    "resource_version_id": "00000000-0000-4000-8000-000000000001",
    "resource_url": "https://merchant.example.com/premium-report",
    "prices": [{
      "asset_id": "base_usdc",
      "amount_atomic": "1000000"
    }],
    "expires_in_seconds": 900,
    "metadata": {"customer_reference": "customer-123"}
  }'
```

### Read payment state and receipts

Use `payments.list` for a tenant-wide view, `payments.retrieve` for one payment,
`payments.listObservations` for chain evidence, and `payments.retrieveReceipt`
for the signed final receipt. Retrieve the public verification-key history with
`receiptVerificationKeys.retrieve` before verifying receipts offline.

### Cursor pagination

`orders.list`, `payments.list`, `payments.listObservations`,
`receivingAddresses.list`, `resources.list`, and `resources.listVersions` accept
`pageSize` (1-100) and an optional opaque `cursor`. Do not decode or construct
cursors. Read the next cursor from `X-X402API-Next-Cursor` or the `Link` response
header and pass it unchanged to the next call.

### Idempotent mutations

Every mutating operation marked in the function table requires an idempotency
key of 8-160 characters matching `[A-Za-z0-9._:-]+`. A transport timeout does
not prove that a mutation failed. Retry the same payload with the same key, or
call `idempotency.getOutcome` to resolve its durable outcome.

### Errors, retries, and HTTP metadata

The SDK raises or returns a typed `X402ApiError` for documented 4xx, 5xx, and
default error responses. Generated responses use the `envelope-http` format so
callers can inspect the decoded body, status code, and response headers. The SDK
applies short exponential-backoff retries to connection failures and status
codes 408, 429, 500, 502, 503, and 504. Application-level retries must still
respect idempotency requirements.


## Available resources and functions

Method names below use the language-neutral generated names. The generator
applies the normal casing conventions for this language.

| SDK resource | Function | HTTP endpoint | Purpose |
| --- | --- | --- | --- |
| `charges` | `create` | `POST /v1/charges` | Create a programmatic charge. Requires an idempotency key. |
| `charges` | `retrieve` | `GET /v1/charges/{charge_id}` | Retrieve a charge by UUID. |
| `facilitator` | `getSupported` | `GET /v1/facilitator/supported` | Discover supported facilitator profiles. |
| `idempotency` | `getOutcome` | `GET /v1/idempotency-outcomes/{idempotency_key}` | Inspect the recorded result for an idempotent mutation. |
| `networkFees` | `createQuote` | `POST /v1/network-fee-quotes` | Preview network fees for one or more prices. |
| `orders` | `list` | `GET /v1/orders` | List orders with cursor pagination. |
| `orders` | `retrieve` | `GET /v1/orders/{id}` | Retrieve an order by UUID. |
| `paymentReadiness` | `retrieve` | `GET /v1/payment-readiness` | Inspect assets and payment-control readiness. |
| `receiptVerificationKeys` | `retrieve` | `GET /v1/payment-receipt-verification-keys` | Retrieve the public receipt-verification key history. |
| `payments` | `list` | `GET /v1/payments` | List payments with cursor pagination. |
| `payments` | `retrieve` | `GET /v1/payments/{id}` | Retrieve a payment by UUID. |
| `payments` | `listObservations` | `GET /v1/payments/{id}/observations` | List chain observations for a payment. |
| `payments` | `retrieveReceipt` | `GET /v1/payments/{id}/receipt` | Retrieve the signed payment receipt. |
| `receivingAddresses` | `getControlCapabilities` | `GET /v1/receiving-address-control-capabilities` | Inspect supported address-control proofs. |
| `receivingAddresses` | `createControlChallenge` | `POST /v1/receiving-address-control-challenges` | Create an address-control challenge. Requires an idempotency key. |
| `receivingAddresses` | `list` | `GET /v1/receiving-addresses` | List receiving addresses with cursor pagination. |
| `receivingAddresses` | `register` | `POST /v1/receiving-addresses` | Register a receiving address. Requires an idempotency key. |
| `receivingAddresses` | `activate` | `POST /v1/receiving-addresses/{readiness_id}/activate` | Activate a ready receiving address. Requires an idempotency key. |
| `receivingAddresses` | `refreshReadiness` | `POST /v1/receiving-addresses/{readiness_id}/readiness-refreshes` | Re-run readiness checks. Requires an idempotency key. |
| `receivingAddresses` | `rotate` | `POST /v1/receiving-addresses/{readiness_id}/rotations` | Rotate a receiving address. Requires an idempotency key. |
| `resources` | `list` | `GET /v1/resources` | List payment-gated resources with cursor pagination. |
| `resources` | `create` | `POST /v1/resources` | Create a payment-gated resource. Requires an idempotency key. |
| `resources` | `listVersions` | `GET /v1/resources/{resource_id}/versions` | List immutable resource versions. |
| `resources` | `createVersion` | `POST /v1/resources/{resource_id}/versions` | Create a resource version. Requires an idempotency key. |
| `resources` | `activateVersion` | `POST /v1/resources/{resource_id}/versions/{version_id}/activate` | Activate a resource version using optimistic concurrency. |
| `resources` | `retireVersion` | `POST /v1/resources/{resource_id}/versions/{version_id}/retire` | Retire a resource version using optimistic concurrency. |
| `wallets` | `retrieveBalance` | `GET /v1/wallets/{id}/balances` | Retrieve confirmed, finalized, or latest wallet balances. |

## Source contract and releases

This repository is generated from the versioned public OpenAPI contract at
[`https://api.x402api.com/openapi/openapi.json`](https://api.x402api.com/openapi/openapi.json).
SDK releases are prepared from an immutable Speakeasy registry tag only after
the deployed production contract matches the source artifact at the JSON data
model level.

- All five official SDKs use the same stable SemVer as the public API contract.
- Backward-compatible production contracts may publish automatically.
- Breaking contracts require a new major version and explicit approval.
- Every generation run records the source Git revision and contract digest.
- `USAGE.md` contains hand-maintained examples that survive regeneration.

## Contributing

Most source files in this repository are generated. Open an issue for API or SDK
feedback. Changes to the public contract, generator configuration, or persistent
documentation should be made in the source repository so they propagate to all
five SDKs consistently.

Licensed under the MIT License.

<!-- Start Summary [summary] -->
## Summary

x402api Public API: Public External-Wallet x402 integration endpoints for programmatic charges, readiness, receiving addresses, resources, payments, receipts, and facilitator discovery.

For more information about the API: [x402api production documentation](https://x402api.com/docs/api)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [x402api TypeScript and JavaScript SDK](#x402api-typescript-and-javascript-sdk)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Using the x402api TypeScript and JavaScript SDK](#using-the-x402api-typescript-and-javascript-sdk)
  * [Available resources and functions](#available-resources-and-functions)
  * [Source contract and releases](#source-contract-and-releases)
  * [Contributing](#contributing)
  * [SDK Installation](#sdk-installation)
  * [Requirements](#requirements-1)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Standalone functions](#standalone-functions)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to npm and others you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either [npm](https://www.npmjs.com/), [pnpm](https://pnpm.io/), [bun](https://bun.sh/) or [yarn](https://classic.yarnpkg.com/en/) package managers.

### NPM

```bash
npm add https://github.com/x402api-com/x402api-typescript
```

### PNPM

```bash
pnpm add https://github.com/x402api-com/x402api-typescript
```

### Bun

```bash
bun add https://github.com/x402api-com/x402api-typescript
```

### Yarn

```bash
yarn add https://github.com/x402api-com/x402api-typescript
```

> [!NOTE]
> This package is published with CommonJS and ES Modules (ESM) support.
<!-- End SDK Installation [installation] -->

<!-- Start Requirements [requirements] -->
## Requirements

For supported JavaScript runtimes, please consult [RUNTIMES.md](RUNTIMES.md).
<!-- End Requirements [requirements] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "<value>",
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
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type | Scheme      | Environment Variable     |
| -------------- | ---- | ----------- | ------------------------ |
| `tenantApiKey` | http | HTTP Bearer | `X402API_TENANT_API_KEY` |

To authenticate with the API the `tenantApiKey` parameter must be set when initializing the SDK client instance. For example:
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "<value>",
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Charges](docs/sdks/charges/README.md)

* [create](docs/sdks/charges/README.md#create) - Create a programmatic charge
* [retrieve](docs/sdks/charges/README.md#retrieve) - Retrieve a programmatic charge

### [Facilitator](docs/sdks/facilitator/README.md)

* [getSupported](docs/sdks/facilitator/README.md#getsupported) - Get supported facilitator profiles

### [Idempotency](docs/sdks/idempotency/README.md)

* [getOutcome](docs/sdks/idempotency/README.md#getoutcome) - Get an idempotency outcome

### [NetworkFees](docs/sdks/networkfees/README.md)

* [createQuote](docs/sdks/networkfees/README.md#createquote) - Create a network-fee quote

### [Orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - List orders
* [retrieve](docs/sdks/orders/README.md#retrieve) - Retrieve an order

### [PaymentReadiness](docs/sdks/paymentreadiness/README.md)

* [retrieve](docs/sdks/paymentreadiness/README.md#retrieve) - Retrieve payment readiness

### [Payments](docs/sdks/payments/README.md)

* [list](docs/sdks/payments/README.md#list) - List payments
* [retrieve](docs/sdks/payments/README.md#retrieve) - Retrieve a payment
* [listObservations](docs/sdks/payments/README.md#listobservations) - List payment observations
* [retrieveReceipt](docs/sdks/payments/README.md#retrievereceipt) - Retrieve a payment receipt

### [ReceiptVerificationKeys](docs/sdks/receiptverificationkeys/README.md)

* [retrieve](docs/sdks/receiptverificationkeys/README.md#retrieve) - Retrieve receipt verification keys

### [ReceivingAddresses](docs/sdks/receivingaddresses/README.md)

* [getControlCapabilities](docs/sdks/receivingaddresses/README.md#getcontrolcapabilities) - Get receiving-address control capabilities
* [createControlChallenge](docs/sdks/receivingaddresses/README.md#createcontrolchallenge) - Create a receiving-address control challenge
* [list](docs/sdks/receivingaddresses/README.md#list) - List receiving addresses
* [register](docs/sdks/receivingaddresses/README.md#register) - Register a receiving address
* [activate](docs/sdks/receivingaddresses/README.md#activate) - Activate a receiving address
* [refreshReadiness](docs/sdks/receivingaddresses/README.md#refreshreadiness) - Refresh receiving-address readiness
* [rotate](docs/sdks/receivingaddresses/README.md#rotate) - Rotate a receiving address

### [Resources](docs/sdks/resources/README.md)

* [list](docs/sdks/resources/README.md#list) - List resources
* [create](docs/sdks/resources/README.md#create) - Create a resource
* [listVersions](docs/sdks/resources/README.md#listversions) - List resource versions
* [createVersion](docs/sdks/resources/README.md#createversion) - Create a resource version
* [activateVersion](docs/sdks/resources/README.md#activateversion) - Activate a resource version
* [retireVersion](docs/sdks/resources/README.md#retireversion) - Retire a resource version

### [Wallets](docs/sdks/wallets/README.md)

* [retrieveBalance](docs/sdks/wallets/README.md#retrievebalance) - Retrieve wallet balances

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Standalone functions [standalone-funcs] -->
## Standalone functions

All the methods listed above are available as standalone functions. These
functions are ideal for use in applications running in the browser, serverless
runtimes or other environments where application bundle size is a primary
concern. When using a bundler to build your application, all unused
functionality will be either excluded from the final bundle or tree-shaken away.

To read more about standalone functions, check [FUNCTIONS.md](./FUNCTIONS.md).

<details>

<summary>Available standalone functions</summary>

- [`chargesCreate`](docs/sdks/charges/README.md#create) - Create a programmatic charge
- [`chargesRetrieve`](docs/sdks/charges/README.md#retrieve) - Retrieve a programmatic charge
- [`facilitatorGetSupported`](docs/sdks/facilitator/README.md#getsupported) - Get supported facilitator profiles
- [`idempotencyGetOutcome`](docs/sdks/idempotency/README.md#getoutcome) - Get an idempotency outcome
- [`networkFeesCreateQuote`](docs/sdks/networkfees/README.md#createquote) - Create a network-fee quote
- [`ordersList`](docs/sdks/orders/README.md#list) - List orders
- [`ordersRetrieve`](docs/sdks/orders/README.md#retrieve) - Retrieve an order
- [`paymentReadinessRetrieve`](docs/sdks/paymentreadiness/README.md#retrieve) - Retrieve payment readiness
- [`paymentsList`](docs/sdks/payments/README.md#list) - List payments
- [`paymentsListObservations`](docs/sdks/payments/README.md#listobservations) - List payment observations
- [`paymentsRetrieve`](docs/sdks/payments/README.md#retrieve) - Retrieve a payment
- [`paymentsRetrieveReceipt`](docs/sdks/payments/README.md#retrievereceipt) - Retrieve a payment receipt
- [`receiptVerificationKeysRetrieve`](docs/sdks/receiptverificationkeys/README.md#retrieve) - Retrieve receipt verification keys
- [`receivingAddressesActivate`](docs/sdks/receivingaddresses/README.md#activate) - Activate a receiving address
- [`receivingAddressesCreateControlChallenge`](docs/sdks/receivingaddresses/README.md#createcontrolchallenge) - Create a receiving-address control challenge
- [`receivingAddressesGetControlCapabilities`](docs/sdks/receivingaddresses/README.md#getcontrolcapabilities) - Get receiving-address control capabilities
- [`receivingAddressesList`](docs/sdks/receivingaddresses/README.md#list) - List receiving addresses
- [`receivingAddressesRefreshReadiness`](docs/sdks/receivingaddresses/README.md#refreshreadiness) - Refresh receiving-address readiness
- [`receivingAddressesRegister`](docs/sdks/receivingaddresses/README.md#register) - Register a receiving address
- [`receivingAddressesRotate`](docs/sdks/receivingaddresses/README.md#rotate) - Rotate a receiving address
- [`resourcesActivateVersion`](docs/sdks/resources/README.md#activateversion) - Activate a resource version
- [`resourcesCreate`](docs/sdks/resources/README.md#create) - Create a resource
- [`resourcesCreateVersion`](docs/sdks/resources/README.md#createversion) - Create a resource version
- [`resourcesList`](docs/sdks/resources/README.md#list) - List resources
- [`resourcesListVersions`](docs/sdks/resources/README.md#listversions) - List resource versions
- [`resourcesRetireVersion`](docs/sdks/resources/README.md#retireversion) - Retire a resource version
- [`walletsRetrieveBalance`](docs/sdks/wallets/README.md#retrievebalance) - Retrieve wallet balances

</details>
<!-- End Standalone functions [standalone-funcs] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "<value>",
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
  }, {
    retries: {
      strategy: "backoff",
      backoff: {
        initialInterval: 1,
        maxInterval: 50,
        exponent: 1.1,
        maxElapsedTime: 100,
      },
      retryConnectionErrors: false,
    },
  });

  console.log(result);
}

run();

```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  retryConfig: {
    strategy: "backoff",
    backoff: {
      initialInterval: 1,
      maxInterval: 50,
      exponent: 1.1,
      maxElapsedTime: 100,
    },
    retryConnectionErrors: false,
  },
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "<value>",
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`X402APIBaseError`](./src/models/errors/x402-api-base-error.ts) is the base class for all HTTP error responses. It has the following properties:

| Property                  | Type       | Description                                                                             |
| ------------------------- | ---------- | --------------------------------------------------------------------------------------- |
| `error.message`           | `string`   | Error message                                                                           |
| `error.httpMeta.response` | `Response` | HTTP response. Access to headers and more.                                              |
| `error.httpMeta.request`  | `Request`  | HTTP request. Access to headers and more.                                               |
| `error.data$`             |            | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```typescript
import { X402Api } from "@x402api/sdk";
import * as errors from "@x402api/sdk/models/errors";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  try {
    const result = await x402Api.charges.create({
      idempotencyKey: "<value>",
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
  } catch (error) {
    // The base class for HTTP error responses
    if (error instanceof errors.X402APIBaseError) {
      console.log(error.message);
      console.log(error.httpMeta.response.status);
      console.log(error.httpMeta.response.headers);
      console.log(error.httpMeta.request);

      // Depending on the method different errors may be thrown
      if (error instanceof errors.ApiErrorEnvelope) {
        console.log(error.data$.error); // models.ApiError
      }
    }
  }
}

run();

```

### Error Classes
**Primary error:**
* [`X402APIBaseError`](./src/models/errors/x402-api-base-error.ts): The base class for HTTP error responses.

<details><summary>Less common errors (7)</summary>

<br />

**Network errors:**
* [`ConnectionError`](./src/models/errors/http-client-errors.ts): HTTP client was unable to make a request to a server.
* [`RequestTimeoutError`](./src/models/errors/http-client-errors.ts): HTTP request timed out due to an AbortSignal signal.
* [`RequestAbortedError`](./src/models/errors/http-client-errors.ts): HTTP request was aborted by the client.
* [`InvalidRequestError`](./src/models/errors/http-client-errors.ts): Any input used to create a request is invalid.
* [`UnexpectedClientError`](./src/models/errors/http-client-errors.ts): Unrecognised or unexpected error.


**Inherit from [`X402APIBaseError`](./src/models/errors/x402-api-base-error.ts)**:
* [`ApiErrorEnvelope`](./src/models/errors/api-error-envelope.ts): The request failed. Applicable to 5 of 27 methods.*
* [`ResponseValidationError`](./src/models/errors/response-validation-error.ts): Type mismatch between the data returned from the server and the structure expected by the SDK. See `error.rawValue` for the raw value and `error.pretty()` for a nicely formatted multi-line string.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `serverURL: string` optional parameter when initializing the SDK client instance. For example:
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  serverURL: "https://api.x402api.com",
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.charges.create({
    idempotencyKey: "<value>",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The TypeScript SDK makes API calls using an `HTTPClient` that wraps the native
[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). This
client is a thin wrapper around `fetch` and provides the ability to attach hooks
around the request lifecycle that can be used to modify the request or handle
errors and response.

The `HTTPClient` constructor takes an optional `fetcher` argument that can be
used to integrate a third-party HTTP client or when writing tests to mock out
the HTTP client and feed in fixtures.

The following example shows how to:
- route requests through a proxy server using [undici](https://www.npmjs.com/package/undici)'s ProxyAgent
- use the `"beforeRequest"` hook to add a custom header and a timeout to requests
- use the `"requestError"` hook to log errors

```typescript
import { X402Api } from "@x402api/sdk";
import { ProxyAgent } from "undici";
import { HTTPClient } from "@x402api/sdk/lib/http";

const dispatcher = new ProxyAgent("http://proxy.example.com:8080");

const httpClient = new HTTPClient({
  // 'fetcher' takes a function that has the same signature as native 'fetch'.
  fetcher: (input, init) =>
    // 'dispatcher' is specific to undici and not part of the standard Fetch API.
    fetch(input, { ...init, dispatcher } as RequestInit),
});

httpClient.addHook("beforeRequest", (request) => {
  const nextRequest = new Request(request, {
    signal: request.signal || AbortSignal.timeout(5000)
  });

  nextRequest.headers.set("x-custom-header", "custom value");

  return nextRequest;
});

httpClient.addHook("requestError", (error, request) => {
  console.group("Request Error");
  console.log("Reason:", `${error}`);
  console.log("Endpoint:", `${request.method} ${request.url}`);
  console.groupEnd();
});

const sdk = new X402Api({ httpClient: httpClient });
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass a logger that matches `console`'s interface as an SDK option.

> [!WARNING]
> Beware that debug logging will reveal secrets, like API tokens in headers, in log messages printed to a console or files. It's recommended to use this feature only during local development and not in production.

```typescript
import { X402Api } from "@x402api/sdk";

const sdk = new X402Api({ debugLogger: console });
```

You can also enable a default debug logger by setting an environment variable `X402API_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
