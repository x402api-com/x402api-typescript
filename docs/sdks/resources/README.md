# Resources

## Overview

### Available Operations

* [list](#list) - List resources
* [create](#create) - Create a resource
* [listVersions](#listversions) - List resource versions
* [createVersion](#createversion) - Create a resource version
* [activateVersion](#activateversion) - Activate a resource version
* [retireVersion](#retireversion) - Retire a resource version

## list

List tenant resources and their visible versions using opaque cursor pagination.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="resources_list" method="get" path="/v1/resources" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.resources.list({});

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { resourcesList } from "@x402api/sdk/funcs/resources-list.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await resourcesList(x402Api, {});
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("resourcesList failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ResourcesListRequest](../../models/operations/resources-list-request.md)                                                                                           | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ResourcesListResponse](../../models/operations/resources-list-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |

## create

Create one tenant resource idempotently.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="resources_create" method="post" path="/v1/resources" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.resources.create({
    idempotencyKey: "<value>",
    body: {
      key: "<key>",
      name: "<value>",
      method: "PATCH",
      path: "/usr/obj",
      description: "round abaft reasonable correctly meh gum anti on porter",
      fulfillmentMode: "webhook",
      prices: [
        {
          assetId: "<id>",
          walletVersionId: "375c4cad-6c97-4d9b-b5e1-f49a97a81a1f",
          amountAtomic: "<value>",
          maxTimeoutSeconds: 731344,
        },
      ],
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
import { resourcesCreate } from "@x402api/sdk/funcs/resources-create.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await resourcesCreate(x402Api, {
    idempotencyKey: "<value>",
    body: {
      key: "<key>",
      name: "<value>",
      method: "PATCH",
      path: "/usr/obj",
      description: "round abaft reasonable correctly meh gum anti on porter",
      fulfillmentMode: "webhook",
      prices: [
        {
          assetId: "<id>",
          walletVersionId: "375c4cad-6c97-4d9b-b5e1-f49a97a81a1f",
          amountAtomic: "<value>",
          maxTimeoutSeconds: 731344,
        },
      ],
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("resourcesCreate failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ResourcesCreateRequest](../../models/operations/resources-create-request.md)                                                                                       | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ResourcesCreateResponse](../../models/operations/resources-create-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |

## listVersions

List immutable versions of one tenant resource using opaque cursor pagination.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="resources_list_versions" method="get" path="/v1/resources/{resource_id}/versions" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.resources.listVersions({
    resourceId: "8708876c-2512-4cc7-b848-ea858ec14d24",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { X402ApiCore } from "@x402api/sdk/core.js";
import { resourcesListVersions } from "@x402api/sdk/funcs/resources-list-versions.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await resourcesListVersions(x402Api, {
    resourceId: "8708876c-2512-4cc7-b848-ea858ec14d24",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("resourcesListVersions failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ResourcesListVersionsRequest](../../models/operations/resources-list-versions-request.md)                                                                          | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ResourcesListVersionsResponse](../../models/operations/resources-list-versions-response.md)\>**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| errors.X402ApiError | 4XX, 5XX            | \*/\*               |

## createVersion

Create an immutable priced version of one tenant resource idempotently.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="resources_create_version" method="post" path="/v1/resources/{resource_id}/versions" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.resources.createVersion({
    idempotencyKey: "<value>",
    resourceId: "f83cc099-f1dd-459f-8cc4-02bb4e39cf7c",
    body: {
      expectedLatestVersion: 132672,
      method: "PATCH",
      path: "/usr/src",
      description: "at ew as entire ugh menacing brr mid",
      fulfillmentMode: "static",
      prices: [
        {
          assetId: "<id>",
          walletVersionId: "ae4d6407-83f8-46ea-8ce6-d7edeab3f5f4",
          amountAtomic: "<value>",
          maxTimeoutSeconds: 228205,
        },
      ],
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
import { resourcesCreateVersion } from "@x402api/sdk/funcs/resources-create-version.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await resourcesCreateVersion(x402Api, {
    idempotencyKey: "<value>",
    resourceId: "f83cc099-f1dd-459f-8cc4-02bb4e39cf7c",
    body: {
      expectedLatestVersion: 132672,
      method: "PATCH",
      path: "/usr/src",
      description: "at ew as entire ugh menacing brr mid",
      fulfillmentMode: "static",
      prices: [
        {
          assetId: "<id>",
          walletVersionId: "ae4d6407-83f8-46ea-8ce6-d7edeab3f5f4",
          amountAtomic: "<value>",
          maxTimeoutSeconds: 228205,
        },
      ],
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("resourcesCreateVersion failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ResourcesCreateVersionRequest](../../models/operations/resources-create-version-request.md)                                                                        | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ResourcesCreateVersionResponse](../../models/operations/resources-create-version-response.md)\>**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ApiErrorEnvelope | 409                     | application/json        |
| errors.X402ApiError     | 4XX, 5XX                | \*/\*                   |

## activateVersion

Activate one immutable resource version idempotently.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="resources_activate_version" method="post" path="/v1/resources/{resource_id}/versions/{version_id}/activate" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.resources.activateVersion({
    idempotencyKey: "<value>",
    resourceId: "87fdaa04-13b8-418c-bb9e-9076d195ff02",
    versionId: "7f5a1532-643b-42d2-81d6-e7d1ba0c8021",
    body: {
      expectedTargetVersion: 530555,
      expectedActiveVersionId: "916e6962-e50f-446c-95de-5100c39d4b2f",
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
import { resourcesActivateVersion } from "@x402api/sdk/funcs/resources-activate-version.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await resourcesActivateVersion(x402Api, {
    idempotencyKey: "<value>",
    resourceId: "87fdaa04-13b8-418c-bb9e-9076d195ff02",
    versionId: "7f5a1532-643b-42d2-81d6-e7d1ba0c8021",
    body: {
      expectedTargetVersion: 530555,
      expectedActiveVersionId: "916e6962-e50f-446c-95de-5100c39d4b2f",
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("resourcesActivateVersion failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ResourcesActivateVersionRequest](../../models/operations/resources-activate-version-request.md)                                                                    | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ResourcesActivateVersionResponse](../../models/operations/resources-activate-version-response.md)\>**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ApiErrorEnvelope | 409                     | application/json        |
| errors.X402ApiError     | 4XX, 5XX                | \*/\*                   |

## retireVersion

Retire one immutable resource version idempotently.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="resources_retire_version" method="post" path="/v1/resources/{resource_id}/versions/{version_id}/retire" -->
```typescript
import { X402Api } from "@x402api/sdk";

const x402Api = new X402Api({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const result = await x402Api.resources.retireVersion({
    idempotencyKey: "<value>",
    resourceId: "0554cf63-9750-4399-b653-7ec259a25ed5",
    versionId: "bc2a4fef-ae62-4652-a16a-16ae6a056787",
    body: {
      expectedVersion: 832056,
      expectedState: "draft",
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
import { resourcesRetireVersion } from "@x402api/sdk/funcs/resources-retire-version.js";

// Use `X402ApiCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const x402Api = new X402ApiCore({
  tenantApiKey: process.env["X402API_TENANT_API_KEY"] ?? "",
});

async function run() {
  const res = await resourcesRetireVersion(x402Api, {
    idempotencyKey: "<value>",
    resourceId: "0554cf63-9750-4399-b653-7ec259a25ed5",
    versionId: "bc2a4fef-ae62-4652-a16a-16ae6a056787",
    body: {
      expectedVersion: 832056,
      expectedState: "draft",
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("resourcesRetireVersion failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ResourcesRetireVersionRequest](../../models/operations/resources-retire-version-request.md)                                                                        | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ResourcesRetireVersionResponse](../../models/operations/resources-retire-version-response.md)\>**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ApiErrorEnvelope | 409                     | application/json        |
| errors.X402ApiError     | 4XX, 5XX                | \*/\*                   |