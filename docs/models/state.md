# State

* `absent` - absent
* `in_progress` - in_progress
* `completed` - completed

## Example Usage

```typescript
import { State } from "@x402api/sdk/models";

let value: State = "absent";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"absent" | "in_progress" | "completed" | Unrecognized<string>
```