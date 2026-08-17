# WalletsRetrieveBalanceResponse

## Example Usage

```typescript
import { WalletsRetrieveBalanceResponse } from "@x402api/sdk/models/operations";

let value: WalletsRetrieveBalanceResponse = {};
```

## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `httpMeta`                                                              | [models.HTTPMetadata](../../models/http-metadata.md)                    | :heavy_check_mark:                                                      | N/A                                                                     |
| `walletBalanceResponse`                                                 | [models.WalletBalanceResponse](../../models/wallet-balance-response.md) | :heavy_minus_sign:                                                      | Successful response for retrieve wallet balances.                       |
| `apiErrorEnvelope`                                                      | [models.ApiErrorEnvelope](../../models/api-error-envelope.md)           | :heavy_minus_sign:                                                      | The request failed with a stable machine-readable error.                |