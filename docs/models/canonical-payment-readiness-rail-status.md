# CanonicalPaymentReadinessRailStatus

* `ready` - ready
* `needs_wallet` - needs_wallet
* `paused_by_tenant` - paused_by_tenant
* `temporarily_unavailable` - temporarily_unavailable
* `not_selected` - not_selected

## Example Usage

```typescript
import { CanonicalPaymentReadinessRailStatus } from "@x402api/sdk/models";

let value: CanonicalPaymentReadinessRailStatus = "paused_by_tenant";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"ready" | "needs_wallet" | "paused_by_tenant" | "temporarily_unavailable" | "not_selected" | Unrecognized<string>
```