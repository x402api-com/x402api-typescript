# ResourceVersionState

* `draft` - Draft
* `active` - Active
* `retired` - Retired

## Example Usage

```typescript
import { ResourceVersionState } from "@x402api/sdk/models";

let value: ResourceVersionState = "active";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"draft" | "active" | "retired" | Unrecognized<string>
```