# Case Study — NovaMach Industrial

## Problem
A B2B industrial-site concept needs enough product, RFQ and content depth to demonstrate a customer journey, while never passing fictional material off as a real manufacturer.

## Context
NovaMach is a fictional brand with eight sample products, English/Chinese/Spanish content and a self-built public demo.

## Constraints
Static React/Vite deployment, sample visuals and data, no real leads, backend, company claims or customer authorization.

## My Role
Built and deployed the public demo, product and multilingual content flow, RFQ/admin browser loop, responsive layout and verification documents.

## Architecture
React/TypeScript renders route-level pages from structured content. RFQs and admin edits live in browser localStorage. Vercel serves the SPA; default robots/meta behavior disallows indexing.

## Key Decisions
Place Demo/Sample Data disclosure throughout the site. Keep admin explicitly a demo and `noindex,nofollow`; require a separate verified-content switch before search indexing.

## Hardest Problem
Making the customer-facing journey and three language paths coherent while preserving the fictional-content boundary.

## Failure/Tradeoff
Browser-only RFQs demonstrate interaction but are not transmitted leads. AI-generated industrial imagery does not document real equipment.

## Testing
Run `pnpm lint`, `pnpm typecheck`, `pnpm build`, and the repository smoke checks. Check direct routes, layout, language and sample RFQ-to-admin behavior.

## Eval
This is a deterministic site/demo; provider-backed AI behavior is not part of the runtime.

## Current Evidence
The Vercel production alias serves the rebuilt demo. The README records the tested routes and synthetic browser loop.

## Limitations
No real company, certification, inventory, RFQ delivery, authentication or customer validation. Git-connected auto-deployment is not confirmed.

## What I Would Do in Production
Replace all sample claims with client-approved material, integrate a secure lead endpoint and access control, then enable indexing only after legal/content review.

## What I Learned
A polished sales demo needs a stronger truth boundary, not a weaker one.
