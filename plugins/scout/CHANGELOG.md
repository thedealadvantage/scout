# Scout plugin changelog

## 0.13.1 (2026-11-18)

- When the plugin is out of date, Scout gives the exact steps: Customize > Plugins > Scout > Update (or Check
  for updates on the marketplace first). First release delivered through the GitHub marketplace.

## 0.13.0 (2026-11-18)

- The plugin now carries the Scout connector (`.mcp.json`), so installing it adds the connector: users
  only click Connect and sign in with their email. Plugin listing fields: display name, homepage,
  privacy notice and license links.

- Adding a user: Scout says whether the setup email went (service 0.9.0) and what to tell the person if not.
- Billing: owners of paid licenses are given the Stripe customer-portal link to update a card or see invoices.

## 0.12.0 (2026-11-17)

- Users sign in with their work email (service 0.7.0). Owners add and remove their own team from
  Scout: "add Sam Lee, sam@firm.com". New section: Your organization's users.

## 0.11.0 (2026-11-17)

- Profile data (license 8.4, needs service 0.5.0): before ending an analysis or update run, Scout sends
  de-identified ranges and counts with `scout_record_profile`, from what the run read. It never asks
  the user for them. A company opted out by written notice is skipped silently.
- Privilege step wording: who needs an instrument depends on who is doing the work (carried from the
  17 Nov privilege-forms review).

## 0.10.2 (2026-11-17)

- Builder 3.7.2: the advisor's own deliverables placed in the room (last period's update, a request
  letter) are never counted as the company's arrivals. `--ours "Scout Log.csv"` excludes files logged as
  `delivered` (or, in an older log, copied out of the working folder). New run-log action: `delivered`.

## 0.10.1 (2026-11-17)

- Builder 3.7.1, from the first Hammock maintenance run: seeding gives each request line the priority
  and area of the finding it serves (named on the line, citing the document, or named in a typed item's
  `finding_ids`), and flags each finding item whose ask repeats a request line (`W-ASK-OVERLAP`).
- The update marks each item raised this period "(new this period)" and counts them in the summary,
  so a new item is visible even in a period when no documents arrived.

## 0.10.0 (2026-11-17)

- The maintenance run: a periodic Data Room Update rendered from an Open Items Register, never composed
  fresh. Builder 3.7.0 adds:
  - `snapshot-diff`: what changed in the room between two full walks; a moved file is not an arrival.
  - `seed-open-items`: the register seeded from the findings and the request letter the company has,
    or topped up from a prior register without duplicates.
  - `validate-update`, `build-update`, `build-open-items`: rows never deleted, five statuses, a closed
    item shown once, deferred items kept off the update, arrivals checked against the snapshots, only
    this period's work reported as handled, every open item confirmed in the built PDF by its ID and
    text, consecutive periods enforced, and moves paired one to one (a replaced file's old version moved
    aside is a move, not an arrival). Reviewed independently; all thirteen points addressed.

## 0.9.0 (2026-11-17)

- Reviewing a room in place: the contracts and analysis runs can read a data room the company (or a
  seller) built their own way, where it sits, with nothing moved, renamed, created or deleted in it.
  Everything Scout writes goes to the working folder. Available on every license.
- Builder 3.6.0: the contracts record carries `room_mode` (`built` or `in_place`); the findings record's
  `scope.in_place` records how the room is organized and the folder and file counts, and the builder
  refuses a walk that listed fewer folders than it found. The report and the analysis workbook say the
  room was reviewed where it sits.

## 0.8.0 (2026-11-17)

- Builder 3.5.0, from the TDA analysis port:
  - Deal impact is always a likelihood ("may", "would likely", "commonly"); "will", "certainly" and an
    impact with no likelihood at all are refused.
  - Key people: each key employee or contractor's IP assignment and confidentiality, graded by the
    instrument that covers it (standalone agreement, in an employment or contractor agreement,
    handbook acknowledgment only, not located). Anything weak is tied to a finding. Shown on a Key
    people tab in the internal analysis workbook.
  - When every policy of the company's own coverage in the room has ended, current insurance becomes
    an item to finalize and a letter request; a findings request for it must cover those policies.

## 0.7.3 (2026-11-16)

- Builder 3.4.1: a missing attachment's reason reads as part of its own line ("Exhibit B (rates), needed
  for the payments and pricing commitments terms") instead of a semicolon that looked like another
  document in the letter.

## 0.7.2 (2026-11-14)

- Builder 3.4.0: the document request asks for each document once. A findings request that needs a
  document the contracts record already asks for must list it in `covers` (the letter then asks on the
  findings line only), and a register row whose evidence is its agreement's missing attachment must say
  so (`request_same_as`) or ask only for the rest. The builder refuses the repeat.

## 0.7.1 (2026-11-14)

- Builder 3.3.1, from the first Hammock rebuild: every document class can list missing attachments,
  so a stockholders agreement's missing schedule becomes a request instead of a note; a charter filed
  with the state can be recorded as `Filed`, so it no longer asks for proof of signing. A record built
  by 3.3.0 adds `missing_exhibits` to each non-agreement row.

## 0.7.0 (2026-11-14)

- Builder 3.3.0: every tracker row has a document class (Agreement, Governing, Insurance policy,
  Dispute, Filing, Policy, Other) and the company's role from that class's closed list (a lease is
  Landlord or Tenant, a one-way NDA Discloser or Recipient). "Other" needs a note.
- The Contract Tracker gets a tab per class, with the fields that fit it, so a bylaw or a policy is never
  shown against agreement terms. An additional-insured certificate is shown as another party's policy,
  never as the company's own coverage. The company's own documents are named for the company.
- Records built by builder 3.2.0 need `document_class` and a role from the new list; the contracts run
  describes the migration.

## 0.6.0 (2026-11-14)

- Two parent folders, set up once per licensee: `[Prefix] - Data Rooms` for the rooms and
  `[Prefix] - Internal WF/Client Files/[Name] - WF` for each company's working folder, prefix `TDA` or
  `Scout`. Companies set up before keep their folders where they are.
- `Scout settings/defaults.json` is now specified: parents, storage, retention policy, naming,
  counterparty obligations, contact, send-to and `always_cc`. Each company can add or replace the copies
  on its emails, asked once at room setup.
- One brand file: `brand.json` is the firm's; every build takes `Drafts/build-brand.json`, written from it.
  Its `white_label` comes from `scout_whoami` (service 0.4.5), never from a user's request.
- Builder 3.2.0: `check-run` reconciles a filing run's counts against its run log before the run ends,
  and refuses a count the log does not support. Scout sends the line it prints.
- ADVOS storage: ShareFile through the ADVOS Filing Service, with both run records.
- The builder key is available on every license, since every run needs the builder. The assessment step
  is offered only when the license includes it.

## 0.5.0 (2026-11-11)

- Intake: builder 3.1.0 builds the intake package under the licensee's brand: the Due Diligence
  Request List (163 requests, self-scoring), the Data Room Categories page, the Deep-Dive Assessment
  Guide for the company, and the interviewer's outline for the licensee's team. The request list, guide
  and categories carry "© ADVOS Pro LLC. Used under license." on every license; white-label drops the TDA
  mark and method credit, not the notice. Scout drafts the cover
  email. The builder key is now available before privilege is recorded, so the package can go out first.
- The assessment conversation: the licensee's team runs and records it; Scout reads the full transcript
  and the company's request-list responses into management's account, which the analysis tests.

## 0.4.0 (2026-11-11)

- Real names by default on the licensee's side, with codenames or both by choice; a company log in
  Scout settings ties each codename to its real name (the service still sees codenames only).
- Builder 3.0.0, from the first round of client-deliverable feedback:
  - Every deliverable says it does not purport to identify every potential issue.
  - Report: nine sections, with "Confirmed by the documents" on its own and "Missing & Open Items";
    a bold action title on every finding; personal-information documents set aside for a person to
    review, never called irrelevant; no stranded headings or half-empty pages.
  - Letter: a contact for questions and how to send documents; plain wording for every request; terms
    an agreement incorporates fold into the missing exhibit that holds them, so nothing is asked twice.
  - Tracker: one word per meaning ("Not addressed", "No", "No obligation").
  - Register: optional counterparty obligations (what others owe the company), by election, with
    coverage on both sides; an opted-out register says so.
- Records built by builder 2.0.0 need a short migration, which the contracts and analysis runs describe.

## 0.3.0 (2026-11-08)

- Builder 2.0.0: the data room analysis. One findings record builds the client Findings &
  Recommendations report (PDF, fixed eight sections), the internal analysis workbook and a request
  letter (or, for a target, a diligence request list). It refuses a finding that is unverified or has
  no source, any figure on deal value, legal conclusions, advice on whether to do the deal, accusatory
  wording, file names or internal wording in anything the company reads, the product's name, and, in
  a target report, "your". IDs (H1, M1, L1) are the same in every deliverable.
- The Contract Tracker groups each counterparty's agreements in one band and keeps the counterparty
  and agreement in view while scrolling.
- Needs the matching scout--builder-key and the new analysis pieces, published with this release.

## 0.2.2 (2026-11-08)

- Builder 1.3.0: every sheet's footer leads with "Prepared by [firm]", with the method credit beside
  it in small type. The TDA mark moves to the top right of the first tab, apart from the firm's logo.
  The tracker's How to read no longer lists OCR as a way signatures are confirmed. Needs the matching
  scout--builder-key, published with this release.

## 0.2.1 (2026-11-08)

- Builder 1.2.0: refuses a typed item to finalize about an agreement already in the tracker, since
  the tracker derives those items itself and the typed one would appear twice (first Hammock build
  listed three items twice). Needs the matching scout--builder-key, published with this release.

## 0.2.0 (2026-10-28)

- Contracts: the plugin carries Scout's contracts builder, locked, and a small loader. Each run fetches
  the key from the service (scout--builder-key), so the builder runs only for a licensee holding the
  contracts or data room module. It validates the source record and builds the Contract Tracker and,
  with the contracts module, the Contract Obligations Register, refusing to build from anything
  incomplete or misquoted. Ships the TDA mark for the co-branded workbooks.

## 0.1.5 (2026-10-22)

- Codename first: when the user asks Scout to take on a company, Scout settles the codename before
  anything else. It asks whether they already use one and offers to pick one; if they have none, it
  proposes a neutral two-word name. A real company name in the chat is expected and no cause for a
  warning; it simply never goes to Scout's service.

## 0.1.4 (2026-10-22)

- Every run records the plugin version (sent with scout_start_run). Feedback must state the Scout
  version running when the issue occurred, from the run itself via scout_run_info, plus the current
  version; Scout will not offer to submit a report without it. Needs service 0.3.2.

## 0.1.3 (2026-10-22)

- Feedback now goes to the ADVOS Wrike feedback form, as for Andy, Addie and CAM. Scout shows the exact
  text (with the name and email it will enter) and submits only after a yes; the user ticks the
  CAPTCHA; copy-paste fallback if the browser is unavailable. Plugin and service versions are required
  in every report.

## 0.1.2 (2026-10-22)

- Feedback: Scout asks for feedback when a run ends (at most weekly, per the service), and offers it
  after a refused step or when the user is frustrated. It shows the exact text and sends only after
  the user approves; never with company or document names.

## 0.1.1 (2026-10-15)

- After adding a company, Scout starts an intake run and fetches the privilege step from the
  service, which picks the form for the company's lens and walks the signing through.

## 0.1.0 (2026-10-14)

- First release: thin loader. Checks in with the Scout service every session, tracks companies and
  runs, fetches method one step at a time, stops if the service is unreachable.
