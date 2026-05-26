# Platform Foundation

This repository currently runs as a Frappe/ERPNext lending application. The future architecture should be built as a parallel platform initiative instead of being mixed directly into the existing runtime.

## Dual-Track Delivery

### Track 1: Current-System Hardening

- secure whitelisted methods
- tighten validation and permission checks
- improve regression coverage
- stabilize deployment and CI
- document actual operating assumptions

### Track 2: Independent Platform Rebuild

Target stack:

- Appwrite for auth, data services, realtime, functions, and team-based access
- Cloudflare Pages for the frontend
- Cloudflare Workers for public APIs and orchestration
- Cloudflare R2 for document/object storage
- Cloudflare Queues for asynchronous processing

## Foundation Deliverables

1. Canonical domain model for leads, applications, loans, repayments, collateral, and classifications
2. API boundary definitions for borrower, staff, partner, and internal service flows
3. Security model covering auth, authorization, audit trails, and file access
4. Migration mapping from core Frappe entities to the future platform
5. A separate implementation workspace or repository for the new frontend and backend services

## Near-Term Recommendation

Do not attempt to gradually convert the Frappe app into the future platform inside the same runtime. Keep the current app operational, and build the new platform as a separate system with explicit migration and cutover phases.