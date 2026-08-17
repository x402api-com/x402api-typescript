# FulfillmentMode

* `proxy` - Reverse proxy
* `webhook` - Signed webhook
* `static` - Static response
* `entitlement` - Paid entitlement

## Example Usage

```typescript
import { FulfillmentMode } from "@x402api/sdk/models";

let value: FulfillmentMode = "entitlement";

// Open enum: unrecognized values are captured as Unrecognized<string>
```

## Values

```typescript
"proxy" | "webhook" | "static" | "entitlement" | Unrecognized<string>
```