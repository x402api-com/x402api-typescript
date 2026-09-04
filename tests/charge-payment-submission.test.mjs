import assert from "node:assert/strict";
import test from "node:test";

import { HTTPClient, X402Api } from "../dist/esm/index.js";

test("submits one exact PAYMENT-SIGNATURE with no request body", async () => {
  let capturedRequest;
  const httpClient = new HTTPClient({
    fetcher: async (request) => {
      capturedRequest = request;
      return new Response(JSON.stringify({
        charge_id: "00000000-0000-4000-8000-000000000001",
        order_id: "00000000-0000-4000-8000-000000000002",
        payment_id: "00000000-0000-4000-8000-000000000003",
        state: "submitted",
        confirmed: true,
        finalized: false,
        payer: "0x0000000000000000000000000000000000000001",
        transaction: "0xtransaction",
        network: "eip155:8453",
        error_reason: "",
      }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    },
  });
  const client = new X402Api({
    tenantApiKey: "test-tenant-key",
    httpClient,
    serverURL: "https://api.x402api.com",
  });

  const response = await client.charges.submitPayment({
    chargeId: "00000000-0000-4000-8000-000000000001",
    paymentSignature: "canonical-signature-artifact",
  });

  assert.ok(capturedRequest);
  assert.equal(capturedRequest.method, "POST");
  assert.equal(
    capturedRequest.url,
    "https://api.x402api.com/v1/charges/00000000-0000-4000-8000-000000000001/payments",
  );
  assert.equal(
    capturedRequest.headers.get("PAYMENT-SIGNATURE"),
    "canonical-signature-artifact",
  );
  assert.equal(capturedRequest.body, null);
  assert.equal(response.dynamicChargePaymentResponse.paymentId,
    "00000000-0000-4000-8000-000000000003");
  assert.equal(response.dynamicChargePaymentResponse.confirmed, true);
  assert.equal(response.dynamicChargePaymentResponse.finalized, false);
});
