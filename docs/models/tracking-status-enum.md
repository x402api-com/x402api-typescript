# TrackingStatusEnum

* `healthy` - healthy
* `degraded` - degraded
* `indexer_disabled` - indexer_disabled
* `awaiting_first_observation` - awaiting_first_observation
* `wallet_version_unavailable` - wallet_version_unavailable

## Example Usage

```typescript
import { TrackingStatusEnum } from "@x402api/sdk/models";

let value: TrackingStatusEnum = "wallet_version_unavailable";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"healthy" | "degraded" | "indexer_disabled" | "awaiting_first_observation" | "wallet_version_unavailable" | Unrecognized<string>
```