# ResourceState

* `draft` - Draft
* `active` - Active
* `retired` - Retired

## Example Usage

```typescript
import { ResourceState } from "@x402api/sdk/models";

let value: ResourceState = "retired";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"draft" | "active" | "retired" | Unrecognized<string>
```