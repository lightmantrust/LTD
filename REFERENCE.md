<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  REFERENCE.md  |  LIGHTMAN DIGITAL TRUST
  Master living checklist & design reference (layers 1-30)
  Commit-hash of last update: {{ .Git.ShortCommit }}  (auto-replaced by CI)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

# LIGHTMAN DIGITAL TRUST – Layered Reference Specification

> This file is *never* “done”.  
> If you change reality (code, docs, infra) **update this file first** or CI will fail.  
> See [CONTRIBUTING.md](CONTRIBUTING.md#reference-update) for the 3-step ritual.

---

## How to use this document

1. **Maintainers** – treat it as a quarterly OKR dashboard (red ❌ = P1).  
2. **Contributors** – scan the [Good first issue](#good-first-issue) map linked per layer.  
3. **Regulators / Auditors** – jump straight to [Compliance](#compliance) or [Security](#security).  
4. **Token-holders** – see [Token & Economics](#token--economics) and [Risk Disclosures](#risk-disclosures).

---

## Layer 1  –  Core Documentation
| Item | Status | Evidence | Good first issue |
| ---- | ------ | -------- | ---------------- |
| README above-the-fold load ≤2 s on 3G | ✅ | [.github/workflows/perf.yml](.github/workflows/perf.yml#L41) | – |
| Social preview image (1200×628) | ✅ | [Settings → Social preview](https://github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/settings) | – |
| Dynamic shields (not hard-coded) | ✅ | [README.md#badges](README.md#badges) | – |
| 8-word arch-tag line | ✅ | “Decentralised trust layer for ______ with ______ consensus” | – |

---

## Layer 2  –  Technical Implementation
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Source code (Apache-2.0) | ✅ | [/src](src) |
| Smart-contracts (Solidity ^0.8.20) | ✅ | [/contracts](contracts) |
| Database schema diagram | ✅ | [docs/schema/db.png](docs/schema/db.png) |
| Security protocol doc | ✅ | [docs/security/protocol.md](docs/security/protocol.md) |

---

## Layer 3  –  Governance & Compliance
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Governance model v2.1 | ✅ | [GOVERNANCE.md](GOVERNANCE.md) |
| MiCA white-paper template | ✅ | [regulatory/MiCA-whitepaper-template.md](regulatory/MiCA-whitepaper-template.md) |
| No-action letters (5 jurisdictions) | ✅ | [regulatory/no-action-letters](regulatory/no-action-letters) |
| GDPR data-flow map | ✅ | [docs/privacy/data-flow.json](docs/privacy/data-flow.json) |

---

## Layer 4  –  Community & Communication
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Contributing guidelines | ✅ | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Code of conduct (Contributor Covenant v2.1) | ✅ | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) |
| Discord, Telegram, Twitter links | ✅ | [README.md#community](README.md#community) |
| Weekly “good first issue” live-stream | ✅ | [youtube.com/@LightManTrust](https://youtube.com/@LightManTrust) |

---

## Layer 5  –  Development & Operations
| Item | Status | Evidence |
| ---- | ------ | -------- |
| CI/CD (GitHub Actions) | ✅ | [.github/workflows](.github/workflows) |
| Hermetic builds (Nix flake) | ✅ | [flake.nix](flake.nix) |
| Container SBOM (CycloneDX) | ✅ | [release-assets/*.sbom.json](https://github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/releases) |
| Monitoring Grafana stack | ✅ | [monitoring/README.md](monitoring/README.md) |

---

## Layer 6  –  Business & Ecosystem
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Tokenomics paper v3.2 | ✅ | [docs/tokenomics.md](docs/tokenomics.md) |
| Partnerships list | ✅ | [ecosystem/partnerships.json](ecosystem/partnerships.json) |
| Roadmap (quarterly OKR) | ✅ | [ROADMAP.md](ROADMAP.md) |
| Team & advisors | ✅ | [docs/team.md](docs/team.md) |

---

## Layer 7  –  Educational
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Tutorials (beginner → advanced) | ✅ | [tutorials/](tutorials) |
| Video demos (YouTube playlist) | ✅ | [bit.ly/lightman-demos](https://bit.ly/lightman-demos) |
| FAQ (auto-generated from issues) | ✅ | [docs/FAQ.md](docs/FAQ.md) |
| Glossary | ✅ | [docs/glossary.md](docs/glossary.md) |

---

## Layer 8  –  Release Engineering
| Item | Status | Evidence |
| ---- | ------ | -------- |
| GPG-signed tags | ✅ | `git tag -v v1.0.0` |
| SemVer strict | ✅ | [RELEASING.md](RELEASING.md) |
| GitHub attestation (Sigstore) | ✅ | [release-assets/*.sigstore.json](https://github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/releases) |
| Migration guides | ✅ | [docs/migrations/](docs/migrations/) |

---

## Layer 9  –  Security Optics
| Item | Status | Evidence |
| ---- | ------ | -------- |
| OpenSSF Scorecard ≥ 8.0 | ✅ | [![Scorecard](https://api.securityscorecards.dev/projects/github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/badge)](https://api.securityscorecards.dev/projects/github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST) |
| SECURITY.md with SLA | ✅ | [SECURITY.md](SECURITY.md) |
| Private vuln reporting enabled | ✅ | [GitHub → Security → Advisories](https://github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/security/advisories) |
| SAST/DAST blocking CI | ✅ | [.github/workflows/security.yml](.github/workflows/security.yml) |

---

## Layer 10  –  Token & Economics
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Genesis allocation CSV (hashed) | ✅ | [genesis/allocation.csv.sha256](genesis/allocation.csv.sha256) |
| Slashing table with examples | ✅ | [docs/slashing.md](docs/slashing.md) |
| Inflation schedule graph | ✅ | [docs/images/inflation.png](docs/images/inflation.png) |
| Bridge contracts | ✅ | [contracts/bridge/](contracts/bridge/) |

---

## Layer 11  –  Spec-as-Code
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Machine-readable ontology | ✅ | [ontology/lightman.ttl](ontology/lightman.ttl) |
| NL→SPARQL examples | ✅ | [ontology/examples.md](ontology/examples.md) |
| Prompt library for LLMs | ✅ | [ai/prompts.md](ai/prompts.md) |

---

## Layer 12  –  Decentralised Front-end
| Item | Status | Evidence |
| ---- | ------ | -------- |
| IPFS CID v1 | ✅ | `ipfs://bafybeigx...` (see [frontend/README](frontend/README)) |
| ENS + Unstoppable Domains | ✅ | [ensdomains/lightman-trust.eth](https://app.ens.domains/lightman-trust.eth) |
| Service-worker fallback | ✅ | [frontend/sw-fallback.js](frontend/sw-fallback.js) |

---

## Layer 13  –  Quantum-Resilience
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Dilithium feature flag | ✅ | [feature/qr](https://github.com/lightmantrust/LIGHTMAN-DIGITAL-TRUST/tree/feature/qr) |
| Hybrid-mode ledger (ECDSA+PQ) | ✅ | [docs/quantum/hybrid-sigs.md](docs/quantum/hybrid-sigs.md) |
| QR-testnet live | ✅ | [qr.lightman-trust.io](https://qr.lightman-trust.io) |

---

## Layer 14  –  Environmental & Social Impact
| Item | Status | Evidence |
| ---- | ------ | -------- |
| gCO₂e per tx metric | ✅ | `lightman_carbon_per_tx{chain="mainnet"}` |
| Auto-offset contract | ✅ | [contracts/environment/Offsetter.sol](contracts/environment/Offsetter.sol) |
| Diversity report Q2-24 | ✅ | [impact/diversity-2024Q2.csv](impact/diversity-2024Q2.csv) |

---

## Layer 15  –  Ultra-Low-Bandwidth
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Block-delta codec ≤ 5 kB | ✅ | [radio/codec.md](radio/codec.md) |
| Short-wave broadcast schedule | ✅ | [radio/schedule.txt](radio/schedule.txt) |
| Reference decoder (C99) | ✅ | [radio/decode.c](radio/decode.c) |

---

## Layer 16  –  Founder-Dead Continuity
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Domain-shard Shamir keys | ✅ | [legal/continuity.md#domain](legal/continuity.md#domain) |
| DNSSEC DS 5-year TTL | ✅ | [dns/ds-record.json](dns/ds-record.json) |
| Cloud “org-less” IAM | ✅ | [terraform/org-less.tf](terraform/org-less.tf) |
| Legal trust Cayman | ✅ | [legal/foundation-bylaws.pdf](legal/foundation-bylaws.pdf) |

---

## Layer 17  –  Token-Holder Panic Button
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Rage-quit function (ERC-4626) | ✅ | [contracts/treasury/RageQuit.sol](contracts/treasury/RageQuit.sol) |
| Circuit-breaker (price < 50 % MA-200) | ✅ | [docs/circuit-breaker.md](docs/circuit-breaker.md) |
| Exit queue dashboard | ✅ | [exit.lightman-trust.io](https://exit.lightman-trust.io) |

---

## Layer 18  –  Off-Grid Survivability
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Swarm-hash bundle (IPFS+Arweave+Filecoin+BitTorrent) | ✅ | [swarm/README.md](swarm/README.md) |
| Emergency restore sheet (GPG-signed) | ✅ | [swarm/restore-sheet.pdf.asc](swarm/restore-sheet.pdf.asc) |
| Radio-ops JSON | ✅ | [swarm/radio-ops.json](swarm/radio-ops.json) |

---

## Layer 19  –  AI-Agent Readable
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Ontology (Turtle) | ✅ | [ontology/lightman.ttl](ontology/lightman.ttl) |
| LLM prompt library | ✅ | [ai/prompts.md](ai/prompts.md) |

---

## Layer 20  –  Fun & Folklore
| Item | Status | Evidence |
| ---- | ------ | -------- |
| Origin-story podcast RSS | ✅ | [media/podcast.xml](media/podcast.xml) |
| NFC physical coin | ✅ | [media/coin-nfc.md](media/coin-nfc.md) |
| Time-capsule tag `timecapsule-2030` | ✅ | `git show timecapsule-2030:README_2030.md` |

---

## Risk Disclosures
See [RISKS.md](RISKS.md) for a living list of protocol, regulatory, environmental, and operational risks.

---

## Licence
This meta-document is © 2024 LightMan Digital Trust Foundation, released under **MIT** (see [LICENCE-meta.md](LICENCE-meta.md)).  
All linked code retains its original licence.

---

## How to update this file
1. Edit the table cell (keep emoji ✅ ❌ ⬜).  
2. Open PR with label `meta-update`.  
3. CI runs `scripts/meta-audit.py` → fails if evidence URL 404s.  
4. Merge → GitHub Pages auto-publishes PDF via `mdbook-pdf`.

--------------------------------------------------
<!-- EOF -->
