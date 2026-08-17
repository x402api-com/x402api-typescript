# SettlementJobState

* `created` - Created
* `verifying` - Verifying
* `verified` - Verified
* `reserved` - Reserved
* `broadcasting` - Broadcasting
* `broadcast_unknown` - Broadcast unknown
* `broadcast` - Broadcast
* `confirming` - Confirming
* `confirmed` - Confirmed
* `finalized` - Finalized
* `rejected` - Rejected
* `failed` - Failed
* `expired` - Expired
* `reverted` - Reverted
* `reorged` - Reorged
* `late_confirmed` - Late confirmed
* `manual_review` - Manual review

## Example Usage

```typescript
import { SettlementJobState } from "@x402api/sdk/models";

let value: SettlementJobState = "broadcast";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"created" | "verifying" | "verified" | "reserved" | "broadcasting" | "broadcast_unknown" | "broadcast" | "confirming" | "confirmed" | "finalized" | "rejected" | "failed" | "expired" | "reverted" | "reorged" | "late_confirmed" | "manual_review" | Unrecognized<string>
```