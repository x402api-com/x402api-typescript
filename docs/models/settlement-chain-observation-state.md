# SettlementChainObservationState

* `included` - Included
* `finalized` - Finalized
* `reverted` - Reverted
* `reorged` - Reorged

## Example Usage

```typescript
import { SettlementChainObservationState } from "@x402api/sdk/models";

let value: SettlementChainObservationState = "reorged";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"included" | "finalized" | "reverted" | "reorged" | Unrecognized<string>
```