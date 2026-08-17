# ResourceVersionFeeMode

* `buyer_pays` - Buyer pays
* `tenant_absorbs_up_to_cap` - Tenant absorbs up to cap

## Example Usage

```typescript
import { ResourceVersionFeeMode } from "@x402api/sdk/models";

let value: ResourceVersionFeeMode = "tenant_absorbs_up_to_cap";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"buyer_pays" | "tenant_absorbs_up_to_cap" | Unrecognized<string>
```