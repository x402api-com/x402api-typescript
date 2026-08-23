# PaymentReadinessState

* `accepting` - accepting
* `setup_required` - setup_required
* `temporarily_unavailable` - temporarily_unavailable
* `paused_by_tenant` - paused_by_tenant

## Example Usage

```typescript
import { PaymentReadinessState } from "@x402api/sdk/models";

let value: PaymentReadinessState = "paused_by_tenant";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"accepting" | "setup_required" | "temporarily_unavailable" | "paused_by_tenant" | Unrecognized<string>
```