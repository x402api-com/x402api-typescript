import assert from "node:assert/strict";
import test from "node:test";

import { paymentReceiptFromJSON } from "../dist/esm/models/payment-receipt.js";

test("PaymentReceipt preserves sponsored gas accounting evidence", () => {
  const parsed = paymentReceiptFromJSON(JSON.stringify({
    id: "00000000-0000-4000-8000-000000000001",
    order_id: "00000000-0000-4000-8000-000000000002",
    settlement_job_id: "00000000-0000-4000-8000-000000000003",
    receipt: { type: "x402api.payment-receipt" },
    receipt_digest: "sha256:receipt",
    signature: "signature",
    signing_key_version: "v1",
    eligible_alternatives: [],
    fee_policy: null,
    fee_evidence: null,
    fee_quote_digest: null,
    fee_quote_expires_at: null,
    settlement_amount_atomic: "20000000",
    gas_mode: "sponsored",
    buyer_native_fee_atomic: "0",
    sponsored_native_fee_atomic: "5000",
    sponsored_native_symbol: "SOL",
    tenant_gas_charge_micros: "1250",
    gas_sponsorship_evidence_digest: "sha256:sponsorship",
    created_at: "2026-08-23T15:00:00Z",
  }));

  assert.equal(parsed.ok, true);
  if (!parsed.ok) {
    assert.fail(parsed.error.message);
  }
  assert.equal(parsed.value.gasMode, "sponsored");
  assert.equal(parsed.value.buyerNativeFeeAtomic, "0");
  assert.equal(parsed.value.sponsoredNativeFeeAtomic, "5000");
  assert.equal(parsed.value.sponsoredNativeSymbol, "SOL");
  assert.equal(parsed.value.tenantGasChargeMicros, "1250");
  assert.equal(
    parsed.value.gasSponsorshipEvidenceDigest,
    "sha256:sponsorship",
  );
});
