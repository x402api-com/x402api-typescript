# ReadinessStatus

* `current` - current
* `refresh_required` - refresh_required
* `durable` - durable
* `activation_required` - activation_required
* `inactive` - inactive

## Example Usage

```typescript
import { ReadinessStatus } from "@x402api/sdk/models";

let value: ReadinessStatus = "current";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"current" | "refresh_required" | "durable" | "activation_required" | "inactive" | Unrecognized<string>
```