# Status

* `created` - Created
* `payment_pending` - Payment pending
* `paid` - Paid
* `fulfillment_pending` - Fulfillment pending
* `fulfilled` - Fulfilled
* `expired` - Expired
* `failed` - Failed

## Example Usage

```typescript
import { Status } from "@x402api/sdk/models";

let value: Status = "fulfilled";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"created" | "payment_pending" | "paid" | "fulfillment_pending" | "fulfilled" | "expired" | "failed" | Unrecognized<string>
```