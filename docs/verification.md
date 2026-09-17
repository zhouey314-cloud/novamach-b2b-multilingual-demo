# Verification

Run the deterministic checks locally:

```bash
pnpm install
pnpm lint
pnpm typecheck
pnpm build
pnpm smoke
```

The smoke check covers the built artifact, route markers, the three language
labels, responsive-safe asset references and the local RFQ/demo boundary. It
does not prove production hosting, database persistence, authentication or a
real WhatsApp/CRM connection.
