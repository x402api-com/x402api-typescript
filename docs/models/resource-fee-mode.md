# ResourceFeeMode

* `buyer_pays` - Buyer pays
* `tenant_absorbs_up_to_cap` - Tenant absorbs up to cap

## Example Usage

```typescript
import { ResourceFeeMode } from "@x402api/sdk/models";

let value: ResourceFeeMode = "buyer_pays";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"buyer_pays" | "tenant_absorbs_up_to_cap" | Unrecognized<string>
```