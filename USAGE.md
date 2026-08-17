<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->