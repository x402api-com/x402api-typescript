import assert from "node:assert/strict";
import test from "node:test";

import { HTTPClient, X402Api } from "../dist/esm/index.js";

test("returns confirmed payment status while the signed receipt is pending", async () => {
  const httpClient = new HTTPClient({
    fetcher: async () => new Response(JSON.stringify({
      payment_id: "00000000-0000-4000-8000-000000000003",
      state: "confirmed",
      confirmed: true,
      finalized: false,
      confirmed_at: "2026-09-04T04:45:27Z",
      finalized_at: null,
      transaction: "5wHu1qwD7...solana-signature",
      network: "solana:mainnet",
      receipt_status: "pending_finality",
    }), {
      status: 202,
      headers: { "Content-Type": "application/json" },
    }),
  });
  const client = new X402Api({
    tenantApiKey: "test-tenant-key",
    httpClient,
    serverURL: "https://api.x402api.com",
  });

  const response = await client.payments.retrieveReceipt({
    id: "00000000-0000-4000-8000-000000000003",
  });

  assert.equal(response.httpMeta.response.status, 202);
  assert.equal(response.paymentReceipt, undefined);
  assert.equal(response.paymentReceiptStatus.paymentId,
    "00000000-0000-4000-8000-000000000003");
  assert.equal(response.paymentReceiptStatus.confirmed, true);
  assert.equal(response.paymentReceiptStatus.finalized, false);
  assert.equal(response.paymentReceiptStatus.receiptStatus, "pending_finality");
  assert.equal(response.paymentReceiptStatus.network, "solana:mainnet");
});
