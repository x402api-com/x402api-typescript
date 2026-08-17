<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->
