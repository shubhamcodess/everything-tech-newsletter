---
date: 2026-11-15
edition: 54
schema_version: 1
generated_at: 2026-11-15T01:38:20+00:00
sources_ok: 43
sources_total: 47
fetched: 400
candidates: 152
full_text: 6
---

# The Brief

- Routine work caused a big outage: the FAA's nationwide ground stop now traces to a contractor's copper-to-fiber swap and a router overload, a day after the agency announced an AI tool for controllers that their union says it was not consulted on.
- Security is the through-line today: a no-login data leak across Lovable apps, PyPI's new provenance display, and ransomware claims that are rising partly because AI is writing better phishing.
- AI agents are getting real access before monitoring catches up. Google's agent monitor flags attacks only after they run and misses most memory-based ones, while Apple is opening app actions to Siri AI.
- Nvidia's leadership change is also a funding story: investors expect smaller, slower checks from the company that backed much of the AI startup market.
- Plumbing keeps improving. Node.js drops common dependencies, nginx can reject bad payloads at the edge, and Compute Engine now offers pinnable API versions.

# Stories

## FAA's nationwide ground stop traced to a copper-to-fiber swap and a router overload
- ids: 92
- topic: Infra
- signal: must-read
- url: https://techcrunch.com/2026/11/14/transportation-secretary-blames-routine-equipment-upgrade-for-grounding-flights-nationwide/
- event: faa nationwide ground stop router overload
- original title: Transportation secretary blames ‘routine’ equipment upgrade for grounding flights nationwide
- source: TechCrunch | https://techcrunch.com/2026/11/14/transportation-secretary-blames-routine-equipment-upgrade-for-grounding-flights-nationwide/
- author: Anthony Ha
- full text: no

> The FAA has cut off the two sources flooding its network and is running a root-cause analysis, while cancellations spilled into Saturday.

The ground stop that halted US departures on Friday now has a proposed cause. Transportation Secretary Sean Duffy says contractor L3Harris replaced copper wire with fiber optic cable at a remote site during what officials called routine maintenance, and afterward a router overloaded a critical communications system. Duffy is still trying to determine whether the installers made a mistake or the router was faulty. This refines the telecom-failure account from our last edition.

FAA acting CTO Rebecca Guy said two locations were pinging the network about a thousand times every four to five seconds. The agency disabled both, stabilized the network and started a root-cause analysis. The disruption was large: Cirium counted more than 8,200 canceled flights on Friday evening and at least 3,000 more on Saturday after the stop lifted. It was only the third nationwide ground stop of this century.

Two questions remain open. Duffy was asked why a remote upgrade ran at 3pm on a Friday rather than overnight. He said large airports switch over late at night, while remote sites switch during the day, and that the timing will be reevaluated. He also used the episode to press Congress for more money for equipment upgrades. The ground stop came a day after the FAA announced an AI tool for controllers, and administrator Bryan Bedford said there is no evidence the outage was AI-related.

**Takeaways**
- Treat the FAA's root-cause report as the document to watch. It will say whether the fault was the installation or the router, which determines whether the fix is procurement or process.
- Before any remote cutover of critical infrastructure, test the new equipment against the same traffic pattern that caused the overload here: two sources pinging the network at high rates.

## Lovable apps leaked passport details and 200,000 private messages to any visitor
- ids: 2
- topic: Security
- signal: must-read
- url: https://www.crissyfield.de/research/lovable-en/
- event: lovable supabase exposed app records
- original title: Lovable apps expose passport details and more than 200K private messages
- source: crissyfield.de | https://www.crissyfield.de/research/lovable-en/ | via Hacker News
- discuss: https://news.ycombinator.com/item?id=50499017 | Hacker News | 634 points | 269 comments
- full text: no

> Of 34,545 Lovable projects that used Supabase, 24,664 sent database records to any visitor as soon as the page loaded.

Researchers examined 159,041 Lovable projects built between December 2025 and September 2026, found through web archive data, and tested whether sensitive information could be read without logging in. They focused on Supabase, the database service most Lovable apps use, because its integration is easier to analyze. The write-up cites passport details and more than 200,000 private messages among the exposed data.

The check had two parts. The first looked at what each site sent on first load. The second made further read-only requests with the same API key to see what else was reachable. The 24,664 figure counts only sites that leaked on first load, so it is a floor rather than a full count. Lovable's own database features, introduced in late 2025, were not tested, though the researchers say similar misconfigurations may exist there.

The authors also point at responsibility. Lovable's marketing stresses that no technical knowledge is needed, while its terms place responsibility for application security and data handling on customers. That gap leaves people with little programming experience building apps that hold personal records. The investigation was done with the German outlet Handelsblatt, which published the findings in German on November 2.

**Takeaways**
- If you have a Lovable app on Supabase, load it in a private window with no login and check what arrives in the network tab. That is the test the researchers ran.
- Review row-level security on every table the front end reads, and treat any table holding messages or identity documents as blocked until a policy is in place.

## Apple opens Siri AI to developers in the 27.3 beta, letting apps hand actions to the assistant
- ids: 37
- topic: AI
- signal: must-read
- url: https://www.infoq.com/news/2026/11/apple-siri-ai-integration/
- event: apple siri ai preview app intents
- original title: Siri AI Developer Preview Lets iOS, iPadOS, and macOS Apps Integrate with Siri
- source: InfoQ | https://www.infoq.com/news/2026/11/apple-siri-ai-integration/
- author: Sergio De Simone
- full text: no

> The preview is limited to developer builds and internal TestFlight testers, and Siri AI is unavailable in the EU on iOS, iPadOS and watchOS.

Apple shipped the Siri AI Developer Preview in the 27.3 betas of its operating systems. Our 9 November edition reported Apple steering Siri toward control of third-party apps. The preview is the first concrete mechanism: any app that exposes App Intents can now bring its content and actions into Siri AI, which Apple describes as a more capable, conversational and personal version of the assistant.

Routing is the part to read closely. A request with no app name goes to the app in the foreground, to the app behind an active Live Activity, or to the app last mentioned in the conversation. An app running in the background only receives requests that name it. Requests can also span apps, such as finding something in one app and sending it to another. For multi-step work, developers can define Skills that chain several actions into one experience.

The limits are real. During the preview, access is restricted to developer builds and internal TestFlight testers. Apple says extended premium access is planned, and Apple Intelligence features may carry usage limits. The early user reactions quoted in coverage are anecdotal, so how reliably routing picks the right app for ambiguous requests has not been tested publicly.

**Takeaways**
- Audit your App Intents names and parameter descriptions now. Siri AI depends on them to choose an action, so vague descriptions will route requests to the wrong place.
- Design for foreground behavior. A backgrounded app only gets requests that name it, so build a clear flow for unnamed requests.
- Plan around the EU gap, since Siri AI is unavailable there on iOS, iPadOS and watchOS during the preview.

## Google's agent monitor flagged 87% of executed attacks on outside benchmarks but caught only 4 of 18 memory attacks
- ids: 22
- topic: AI
- signal: recommended
- url: https://developers.googleblog.com/how-agent-anomaly-detection-scores-on-benchmarks-we-didnt-write/
- event: google agent anomaly detection benchmarks
- original title: How Agent Anomaly Detection scores on benchmarks we didn't write
- source: Google Developers Blog | https://developers.googleblog.com/how-agent-anomaly-detection-scores-on-benchmarks-we-didnt-write/
- full text: no

> The monitor raised false alarms on 2% to 16% of normal sessions, depending on which tools the agent used.

Google tested Agent Anomaly Detection, a private-preview monitor on its Gemini Enterprise Agent Platform. It reads an agent's traces and logs without adding latency and flags sessions where the agent steps outside its intended boundaries. Rather than rely on its own tests, Google ran five public agent-security benchmarks written by others, covering 1,774 sessions: AgentDojo, InjecAgent, Agent Security Bench, AgentDyn and AgentHarm. In four, the harmful instruction is hidden in data a tool returns. In AgentHarm, the user asks for harm directly.

The base model did much of the defensive work. It did not follow about half of the harmful instructions it read, refused three in four direct requests, and ignored or failed on about 30% of the hidden ones. Of the harmful sessions that actually executed, the monitor flagged 87% for post-execution review. That wording matters. The flag arrives after the action has run, so the monitor detects harm rather than preventing it.

Memory was the clear weakness. When instructions planted in an agent's long-term memory drove its behavior, the monitor caught 4 of 18. Grading used deterministic code that checked the final state of each app, such as whether money left an account, so injected text could not mislead the grader. Each agent first ran at least 300 benign sessions so the monitor could learn normal behavior. Google wrote the post itself, so these are its own measurements, run on third-party tests.

**Takeaways**
- If you rely on a post-execution monitor, decide which actions must be blocked before they run. The 87% figure only covers what happens after execution.
- Test planted-memory cases separately from injected tool output. Detection fell sharply for memory in this test.
- Measure false alarms on your own tool mix before turning on enforcement, since the rate here ranged from 2% to 16% depending on tools.

## Nvidia's startup dealmaking faces a slowdown after Jensen Huang's exit, investors say
- ids: 129
- topic: Startups
- signal: recommended
- url: https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/
- event: nvidia huang departure startup funding
- original title: Jensen Huang’s departure blasts big hole in AI startup funding, VCs and founders say
- source: TechCrunch | https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/
- author: Marina Temkin and Dominic-Madori Davis
- full text: no

> Nvidia joined 105 funding rounds this year, often as the largest investor, and investors say Huang personally made most of the big calls.

Investors and founders expect less capital from Nvidia now that Huang has stepped down as CEO. The company has poured tens of billions of dollars a year into startups, and one neocloud founder said the news felt like a bomb going off. Huang's portfolio centered on neoclouds, inference providers and open-weight models, the expensive categories that smaller companies struggle to fund on their own.

Interim CEO Colette Kress is expected to change how Nvidia invests in AI startups. One investor described her as much more conservative and unlikely to commit the same amount to early-stage companies. Wall Street had already questioned how much of Huang's dealmaking was tied to the data-center buildout. Investors don't expect a quick return to the earlier pace, even if a successor eventually restores it.

The exposure is concrete. Nvidia backed CoreWeave while it was still private, took part in two Crusoe rounds including a $1.4 billion Series E, and is buying Hugging Face for $13 billion, a deal expected to close in 2027. It holds stakes in Mistral AI, Lambda and Black Forest Labs, and wrote an $800 million check into a $2 billion Series B for Reflection AI.

**Takeaways**
- If a funding plan assumes Nvidia as a participant, model a smaller or later check and a lower valuation, which is what the investors quoted here expect.
- Watch whether the $13 billion Hugging Face acquisition proceeds on its expected 2027 timeline. It will show whether Nvidia's acquisition appetite survived the leadership change.

## Compute Engine adds immutable date-stamped API versions, so callers can pin behavior
- ids: 19
- topic: Infra
- signal: recommended
- url: https://www.infoq.com/news/2026/11/compute-engine-api-versioning/
- event: compute engine date versioned api
- original title: Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions
- source: InfoQ | https://www.infoq.com/news/2026/11/compute-engine-api-versioning/
- author: Steef-Jan Wiggers
- full text: no

> Requests that name no version keep hitting the mutable /v1 surface, which has no end-of-life date.

Google made multi-versioning of the Compute Engine API generally available. Stable versions are named by date and released quarterly, starting with 2026-09-01. Preview versions carry a -preview suffix and a one-year lifespan. Callers select a version with an X-Goog-Api-Version header or an apiVersion query parameter on the unchanged path. Each stable version is a snapshot of generally available features and defaults, and Google does not make breaking changes to a snapshot after publication.

Software engineer Michael Murstein explains the motive: /v1 is one mutable production surface shared by every customer, so even a counterintuitive default risked breaking scripts or required a multi-year migration. The dated versions change three things callers will notice. AggregatedList returns partial results by default, so one failing zone no longer fails a fleet-wide query. Errors become structured google.rpc.ErrorInfo objects, and an unknown version lists the valid ones. Legacy IAM permission checks are tightened, with safer configuration defaults.

Most teams will meet the change through tooling. Client libraries for Python, Go, Java, Node.js, C#, Ruby and PHP bind each release to one dated version while keeping their namespaces, so import paths stay the same. gcloud compute targets the bundled stable version, and a new gcloud preview group targets preview. The Terraform google provider targets stable versions, while google-beta targets preview. Google is the last of the three largest cloud providers to let callers pin a version on a request.

**Takeaways**
- Pin a dated version in automation that matters rather than relying on /v1's defaults. The partial-results change will alter output for fleet-wide list calls.
- Update any code that parses error bodies, since the structure changes to ErrorInfo.
- Re-audit IAM-dependent scripts after moving versions, because the new versions tighten legacy permission checks.

## PyPI's redesigned project pages add a Security tab with per-file provenance
- ids: 8
- topic: Security
- signal: recommended
- url: https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/
- event: pypi project pages provenance security tab
- original title: PyPI's redesigned project pages with clearer security signals are now live
- source: blog.pypi.org | https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/ | via Hacker News
- discuss: https://news.ycombinator.com/item?id=50497892 | Hacker News | 201 points | 92 comments
- full text: no

> A release with no attestations shows no provenance, which PyPI says does not by itself mean a file is malicious.

PyPI has finished the redesign it announced in July. The main addition is a Security tab that shows each release's provenance state and per-file attestations. A release has full provenance when every one of its files carries an attestation. Two attestation types qualify: PyPI Publish attestations, which confirm a Trusted Publisher uploaded the file, and SLSA Build Provenance, which links the file to its source commit, build platform and build instructions. Users can read the metadata in the page or follow a transparency log link.

The redesign responds to a practical problem. Digital attestations arrived in 2024, but the interface never explained what they meant or where they fell short. PyPI worked with a design studio and built the display around the OpenSSF's Attestations Style Guide.

The caveat is in the wording. Older releases and projects that have not set up Trusted Publishing usually show no provenance, and PyPI says that only means a file's origin cannot be verified cryptographically. Anyone choosing a dependency should weigh maintainer history and release patterns alongside it.

**Takeaways**
- Maintainers: set up Trusted Publishing so your next release gets attestations and shows full provenance.
- Consumers: check the provenance state before pinning a new dependency, and treat "no provenance" as a reason to look at maintainer history, not as a verdict.

## Open-source DocumentDB 1.0 ships as a MongoDB-compatible database on PostgreSQL
- ids: 20
- topic: Open Source
- signal: recommended
- url: https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/
- event: documentdb 1.0 general availability postgresql mongodb
- original title: Open Source DocumentDB 1.0 Reaches General Availability
- source: InfoQ | https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/
- author: Renato Losio
- full text: no

> It is MIT-licensed, works with most MongoDB drivers and queries unchanged, and runs on PostgreSQL 15 through 18 via container images.

DocumentDB 1.0 is the project's first generally available release. It is a PostgreSQL extension that provides MongoDB API functionality, paired with a gateway that translates MongoDB protocol requests into PostgreSQL calls. Container images cover PostgreSQL 15 to 18, Linux packages cover 17 and 18, and a Kubernetes operator is included. The release concentrates on security, stability and fixes for indexing, aggregation and geospatial queries.

Microsoft announced the project in early 2025, and it later joined the Linux Foundation with support from AWS, Cockroach Labs, Google, Snowflake and Yugabyte. The team's licensing argument is that the MIT license allows commercial use, modification and hosting without disclosing proprietary code, in contrast to MongoDB's SSPL.

Adoption faces a naming problem and a compatibility question. Hacker News commenters argue the name collides with Amazon DocumentDB, and Azure's own DocumentDB offering adds to the confusion. A Reddit commenter says compatibility between MongoDB and FerretDB, another open alternative, has been minimal compared with what people expect. That is a reminder to test your own queries rather than trust the driver claim.

**Takeaways**
- Run your real query set against DocumentDB before migrating. The 1.0 work targets aggregation and geospatial paths, so test those first.
- Check your PostgreSQL version against the package matrix. Container images cover 15 through 18, but Linux packages only cover 17 and 18.

## FAA extends its SMART AI tool to airspace across all 22 centers
- ids: 31
- topic: AI
- signal: recommended
- url: https://arstechnica.com/features/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/
- event: faa smart ai air traffic control
- original title: FAA expands AI advice to manage air traffic congestion across entire US airspace
- source: Ars Technica | https://arstechnica.com/features/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/
- author: Jeremy Hsu
- image: https://cdn.arstechnica.net/wp-content/uploads/2026/11/Pilots-during-DFW-departure-1152x648.jpg
- full text: no

> The agency says SMART has rerouted 180 flights since September, saving an average of 10 minutes and nearly 80 gallons of fuel per flight.

The FAA is moving its SMART system from the Washington, DC airspace where it started in September to the airspace of all 22 centers. The agency describes SMART as a cloud-based system that combines weather, flight paths, traffic flow and controller staffing data to predict traffic patterns. It recommends schedules, routes and the order of arrivals. The system cost $875 million.

Humans stay in the loop. A team of FAA specialists in DC validates the recommendations before they go to control facilities. Airline executives have praised the rollout. The union representing air traffic controllers says it was not involved in designing or testing the system, and that objection is the main dispute.

The timing draws attention. The nationwide ground stop in this edition came a day after the SMART expansion was announced. Administrator Bryan Bedford said there is zero evidence the outage was AI-related, and the agency attributes it to failed equipment.

**Takeaways**
- For AI tools that recommend operational decisions, ask who validates each recommendation before it reaches an operator. Here, the FAA says its DC team does.
- Watch whether the controllers' union gets a role in testing. Its absence from design is the point most likely to shape later oversight.

## Google's confidential TPU 8tx runs on AMD Epyc hosts rather than its own Axion CPUs
- ids: 70
- topic: Infra
- signal: recommended
- url: https://www.techradar.com/pro/google-turned-to-amd-epyc-not-its-own-axion-chips-to-secure-its-first-confidential-tpu
- event: tpu 8tx confidential amd epyc
- original title: Google turned to AMD Epyc, not its own Axion chips, to secure its first confidential TPU
- source: TechRadar | https://www.techradar.com/pro/google-turned-to-amd-epyc-not-its-own-axion-chips-to-secure-its-first-confidential-tpu
- author: Rahim Amir
- image: https://cdn.mos.cms.futurecdn.net/MVfiXV7sRq7dWyFz2yiRHM-1600-80.jpg
- read: 6 min
- full text: yes

> AMD's SEV extends the protected environment to the accelerator, which checks each device's identity before it can reach protected memory.

Google's new TPU 8tx pairs its TPU 8t silicon with 5th Gen AMD Epyc "Turin" host processors. Google and AMD describe it as the first cloud TPU system with hardware-enforced confidential computing, aimed at confidential AI inference and at regulated enterprises and governments that want to fine-tune or train on private data without moving it between clusters.

The 8tx carries over the 8t's compute and memory, 12.6 petaflops of FP4 and 216GB of HBM, while trading in the 8i's lower-latency Boardfly interconnect. Google claims up to 2x lower latency than the 8t. One analysis cited in the coverage notes that both new systems are configurations of existing chips rather than new designs.

Google has not said why it chose AMD over Axion, the Neoverse V2-based chip it unveiled in 2024. One outlet suggests its audited confidential stack is x86-only for now, which would explain the choice, but that is the outlet's inference rather than Google's statement. The coverage also says key security details remain unpublished, even though Google and Nvidia already offer confidential GPUs.

**Takeaways**
- If you run regulated inference, ask for the attestation documentation for the confidential accelerator before relying on it, since some details are still unpublished.
- Benchmark Google's 2x latency claim on your own workload. The figure comes from Google, and no independent benchmark appears in this coverage.

## Ransomware leak-site claims rose 20% to 40% since spring by some counts, with AI aiding phishing and talks
- ids: 113
- topic: Security
- signal: recommended
- url: https://www.wired.com/story/beware-the-new-ai-fueled-ransomware-boom/
- event: ransomware claims ai phishing negotiation
- original title: Beware the New AI-Fueled Ransomware Boom
- source: Wired | https://www.wired.com/story/beware-the-new-ai-fueled-ransomware-boom/
- author: Matt Burgess and Lily Hay Newman
- image: https://media.wired.com/photos/6af88e4339637940f3ecc20a/master/pass/image%20(76).png
- full text: no

> Fully automated AI ransomware has not appeared yet, but attackers are using language models for phishing lures and ransom negotiations.

Claimed attacks on leak sites have spiked. Some researchers count nearly 3,000 over the summer, a 20 to 40 percent increase since spring by some estimates. Most of the recent growth came from outside the United States, where volume stayed high but steady. Cynthia Kaiser of Halcyon says the international rise is partly fueled by AI.

The numbers deserve caution. Victims don't always disclose attacks, attackers inflate their claims, and de-duplicating leak-site posts is hard. Still, researchers agree that ransomware has been consistently elevated for years, so the recent spike sits on a high baseline.

Allan Liska of Recorded Future says AI is now used for better phishing emails and in negotiations, but successful groups remain largely human-operated. He warns that heavy experimentation could change that quickly. Because the same phishing and social-engineering methods are often used to gain initial access, scam trends matter for ransomware defense.

**Takeaways**
- Prioritize defenses against AI-written phishing. Check that help desks verify identity before resetting credentials, since that is the access path the researchers say is growing.
- Treat leak-site counts as trend signals rather than a way to size your own exposure, because the coverage says they are inflated and inconsistent.

## A broad "simple or complex" classifier routed nearly every coding task to the simple tier in Google's test
- ids: 26
- topic: AI
- signal: recommended
- url: https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/
- event: classifier routing gemini cost per task
- original title: Cost per task: Using cheap classifiers to route across Gemini models and thinking levels
- source: Google Developers Blog | https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/
- full text: no

> Replacing the broad question with one atomic check fixed the sorting at once; the report's savings figures were not available to us.

Google argues the metric for agent economics has shifted from price per million tokens to cost per successful task: total spend across every loop, tool call, retry and thinking pass, divided by the tasks that pass verification. When an agent sends routine decisions to a high-reasoning model, the bill climbs even as token prices fall.

The proposed fix is a lightweight classifier placed in front of the main model. The example uses TypeSafe's Jev, which returns a choice, a numeric score or a yes-no probability in a single pass. Google says it has no partnership with TypeSafe and that the same pattern works with Google-native classifiers. A codelab runs the same kind of classifier on Google's open DiffusionGemma model. The test used 50 auto-graded coding-agent questions against live Gemini and Jev APIs.

The first attempt failed. A single broad question, simple or complex, sent nearly everything to the simple route, including tasks that needed an LRU cache trace or modular exponentiation. Replacing it with one atomic check fixed the separation immediately. The guidance behind the change is to split any question that weighs several factors into separate checks.

**Takeaways**
- Before trusting a router, test a broad multi-factor question against decomposed checks on tasks that need deep reasoning. The broad version failed on exactly those.
- Compare model configurations on cost per passing task rather than price per token. The article's whole argument depends on that metric.

## Node.js 26.10 adds util.debounce and util.throttle to core, plus PKCS#12 parsing
- ids: 18
- topic: Languages
- signal: notable
- url: https://www.infoq.com/news/2026/11/nodejs-debounce-throttle/
- event: node.js 26.10 debounce throttle pkcs12
- original title: Node.js Brings Debounce, Throttle, and PKCS#12 Parsing Into Core Modules
- source: InfoQ | https://www.infoq.com/news/2026/11/nodejs-debounce-throttle/
- author: Daniel Curtis
- full text: no

> Developers can drop vendored rate-limiting helpers and read .p12 and .pfx bundles without shelling out to the openssl CLI.

Node.js 26.10.0 moves two long-requested helpers into the standard library: util.debounce() and util.throttle() in node:util. Rate limiters were among the most commonly vendored dependencies in the ecosystem, usually taken from lodash or the throttle-debounce package. The same change adds util.markPromiseAsHandled(), which lets framework authors tell the runtime that a promise has been handled.

The design changed during review. Contributors pointed out that an AbortSignal can only move to aborted once, which is awkward for a function called repeatedly. The signal now cancels every future invocation, and a leading-edge option lets the first call fire immediately.

crypto.parsePKCS12() wraps OpenSSL's PKCS12 parsing and returns privateKey, certificate and additionalCertificates. Node already parsed these bundles internally for TLS's pfx option but never exposed the result. The release also extends the experimental Virtual File System to node:ffi, so libraries can load from a mounted VFS on Linux, and it fixes a bug where dlopen passed an undefined flags argument that silently broke addon loading.

**Takeaways**
- Swap vendored debounce or throttle code for the util versions once your minimum Node version allows. The new signal cancels all future calls, not just the current one.
- Replace openssl CLI calls used for PKCS#12 with crypto.parsePKCS12(), and check the returned field names against your code.

## nginx 1.31's json_set rejects bad webhook payloads about 13 times faster than forwarding them
- ids: 54
- topic: Infra
- signal: notable
- url: https://dev.to/alexgeorgiev17/nginx-131s-jsonset-directive-rejects-a-bad-webhook-payload-about-13-times-faster-than-forwarding-3b00
- event: nginx webhook payload validation
- original title: nginx 1.31's json_set directive rejects a bad webhook payload about 13 times faster than forwarding it
- source: Dev.to | https://dev.to/alexgeorgiev17/nginx-131s-jsonset-directive-rejects-a-bad-webhook-payload-about-13-times-faster-than-forwarding-3b00
- author: Alex Georgiev
- image: https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F3tias5qdckk8l4gcu57t.png
- read: 6 min
- full text: yes

> The module reads a field from the JSON body before routing, so invalid events never reach the application.

A webhook receiver the author built years ago forwarded every body to the application, which then decided whether it was valid. nginx 1.31.5 adds ngx_http_json_module, whose json_set directive reads a field from the request body and comes with a depth limit. The same release adds predicate locations, which match on a variable, and client_body_early_read, so a location can be chosen by what the body says.

The test used nginx 1.31.8 with an endpoint that accepts only two event types. Across 200 alternating valid and invalid requests, every invalid one was refused at nginx and never reached the backend. Rejecting 1,000 invalid payloads one at a time, averaged over three runs, the edge path handled about 24,265 requests per second against roughly 1,874 for the proxied path, about 13 times faster.

The setup has limits. Everything ran on loopback with host networking, so the network hop was removed, and the headline figure is at concurrency 1. The module is compiled into the official Docker image, but Ubuntu 24.04's apt package still ships nginx 1.24.0, which lacks it.

**Takeaways**
- Check your nginx build flags before designing around json_set. The module requires --with-http_json_module, and Ubuntu 24.04's apt package does not include it.
- Re-run the benchmark at your real concurrency. The 13x figure is a single-client, loopback measurement.

## Google's AI Edge Gallery adds offline speech recognition and text-to-speech for phones and glasses
- ids: 23
- topic: AI
- signal: notable
- url: https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/
- event: ai edge gallery speech recognition
- original title: On-Device Speech Recognition and Text-to-Speech in Google AI Edge Gallery
- source: Google Developers Blog | https://developers.googleblog.com/on-device-speech-recognition-and-text-to-speech-in-google-ai-edge-gallery/
- author: Google AI Edge Team and Android ML Team
- image: https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Gemini_Generated_Image_yd9gceyd9g.2e16d0ba.fill-1200x600.jpg
- read: 4 min
- full text: yes

> Google pairs the speech models with Gemini Nano and Gemma 4, so apps can stream transcripts and speak replies with no network connection.

Google added on-device automatic speech recognition and text-to-speech to AI Edge Gallery, and built voice into its AI Chat feature. The speech models run locally with low latency and a small memory footprint, and they pair with small language models such as Gemini Nano and Gemma 4. Google argues voice is often the most natural way to use AI on phones and wearables.

The showcase is an XR Language Teacher. A user points a camera at an unfamiliar object or menu, asks a question, and hears an explanation and local pronunciation, all running on a paired phone. The same pipeline extends to hands-free smart glasses, and Google points to an Android Dev Summit talk on audio-first eyewear built on Gemini Nano.

Developers get open-source code on GitHub. For Android, the recommended path uses ML Kit, while MediaPipe Tasks and LiteRT cover cross-platform use and open models. Google acknowledges that Gemma 4 can take audio directly, but argues that a cascade of separate speech and language models gives better latency control and flexibility.

**Takeaways**
- Benchmark a cascade of separate speech and language models against a single audio-capable model on your target device. Google's case for the cascade rests on latency, so measure that.
- On Android, start from the GitHub sample built on ML Kit rather than assembling the pipeline yourself.

## Old cloud storage share links stay live until revoked, so audit OneDrive and iCloud now
- ids: 117
- topic: Security
- signal: notable
- url: https://www.wired.com/story/audit-all-the-cloud-storage-links-youve-shared/
- event: onedrive icloud share links audit
- original title: It’s Time to Run an Audit of All the Cloud Storage Links You’ve Shared
- source: Wired | https://www.wired.com/story/audit-all-the-cloud-storage-links-youve-shared/
- author: David Nield
- image: https://media.wired.com/photos/6af5bf6d129c3f49a6da47ce/master/pass/111216-CLoud%20Storage%20Audit.jpg
- full text: no

> OneDrive lets you set an expiration date when you share a file, which saves a cleanup pass later.

Shared links keep working until someone removes them, and the risk grows with their age. They are well protected by default, but they can be forwarded by mistake, and a contact's compromised email account can expose them. Depending on the permissions, a link holder can view files, change them or delete them.

In OneDrive on the web, open Shared link in the left pane and choose By you to list everything you have shared, then sort by Modified. Use Manage access on any item to remove particular people, or delete a link-only share with the trash icon. For new shares, the cog on the share panel sets an expiration date.

In iCloud Drive on the web, Shared in the navigation pane shows the files and folders you are sharing. Sorting is limited, so use the search box to find items. Once a link is closed, nobody can reach the content through it.

**Takeaways**
- Audit OneDrive in a few minutes: Shared link, then By you, then delete the link-only shares you no longer need.
- Set an expiration date on new OneDrive shares from the share panel, so stale links expire without a cleanup pass.
- In iCloud, use the search box on the Shared view, since the list cannot be sorted usefully.

## WebMCP lets a site offer in-page tools, so an agent gets a structured answer in one call
- ids: 61
- topic: AI
- signal: notable
- url: https://dev.to/debs_obrien/one-tool-call-instead-of-four-pages-adding-webmcp-to-my-site-29g7
- event: webmcp in page tools agents registertool
- original title: One Tool Call Instead of Four Pages: Adding WebMCP to My Site
- source: Dev.to | https://dev.to/debs_obrien/one-tool-call-instead-of-four-pages-adding-webmcp-to-my-site-29g7
- author: Debbie O'Brien
- image: https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F52quyt5euln5jy6a1rbu.png
- read: 10 min
- full text: yes

> The API is in Chrome's origin trial from version 149 and in Edge, and the author says it already runs for real visitors.

WebMCP is a proposed standard being drafted by the W3C Web Machine Learning Community Group. Under it, a page announces its capabilities to the browser as named functions, each documented with an input schema and a handler. An agent running inside the browser can then discover and call those functions instead of navigating the page by hand. The author's site uses document.modelContext.registerTool(), since the spec has moved the API from navigator to document.

The motivation is a site spread across videos, posts, podcasts and courses. When an agent is asked what the author has done on a topic, a tool can return precise matches. The author says no page on the site gives the minute mark where a topic comes up in a talk, which is exactly what the tool can return.

The limits are clear in the documentation the author cites. WebMCP tools exist only while the page is open. Chrome says the feature is meant for a person present alongside the agent, not for unattended scripts, and agents must visit the page to discover its tools. It complements MCP rather than replacing it, because MCP servers work anywhere.

**Takeaways**
- To test locally, enable the WebMCP testing flag at chrome://flags that the author describes, then inspect the registered tools in Chrome DevTools.
- Expose a few precise tools with clear schemas. The value described here is structured answers, not the number of endpoints.

## A standard-library-only Go package implements Bloom filters, count-min sketches and HyperLogLog
- ids: 36
- topic: Languages
- signal: notable
- url: https://antonz.org/probabilistic-data-structures/
- event: go unsure probabilistic data structures library
- original title: Probabilistic data structures in Go
- source: antonz.org | https://antonz.org/probabilistic-data-structures/ | via Lobsters
- full text: no

> A set of one million 8-byte strings takes about 64 MB, while a Bloom filter at a 1% false-positive rate needs about 1.24 MB.

Probabilistic data structures trade exactness for memory. A Bloom filter can say an item is definitely absent or probably present, and it never stores the items themselves. The author introduces unsure, a Go package with five structures: Bloom filter, count-min sketch, HyperLogLog, T-digest and top-k. Each core implementation runs roughly 100 to 300 lines and depends only on the standard library.

The size difference is the point. The author's example puts a regular set of one million 8-byte strings at about 64 MB, against 1.24 MB for a Bloom filter with a 1% false-positive rate, roughly 10 bits per item. The filter's size does not depend on item length, so longer keys widen the gap.

The tradeoffs come with the structure. A Bloom filter cannot delete items, count them or iterate over them, and its false-positive rate climbs as you add items beyond the capacity it was sized for. The author also claims the implementations are usually several times faster than alternatives, but the benchmark details fall outside what is shown in this write-up.

**Takeaways**
- If you use a Bloom filter as a cache pre-check, plan for false positives. A "probably present" answer still requires the real lookup.
- Size the filter from your expected item count and tolerated false-positive rate, since accuracy degrades past the capacity you planned for.

## An InfoQ podcast argues humans must stay accountable for AI-written code and review it by trust, not volume
- ids: 47
- topic: Engineering
- signal: notable
- url: https://www.infoq.com/podcasts/accountability-age-ai-coding-summary/
- event: accountability ai coding code review
- original title: Podcast: Doing The Right Thing: Accountability In The Age Of AI Coding Summary
- source: InfoQ | https://www.infoq.com/podcasts/accountability-age-ai-coding-summary/
- author: Shane Hastie
- image: https://res.infoq.com/podcasts/accountability-age-ai-coding-summary/en/card_header_image/hugo-venturini-twitter-card-1794303925695.jpg
- read: 19 min
- full text: yes

> Hugo Venturini ties the argument to Microsoft's 2014 decision to merge engineer and tester roles, which made engineers answerable for the whole product.

In an InfoQ Engineering Culture podcast, Shane Hastie talks with Hugo Venturini about who answers for code when AI writes it. The episode's key points say humans remain accountable for both the decisions AI makes possible and the code it produces. The risk, the discussion argues, is people blaming the tool instead of owning outcomes.

On review, the episode says pull requests were already growing for years, and AI did not create the scale problem. Teams should apply the same trust-based judgment about what needs close review that worked before AI, rather than reviewing every line equally.

The roles are shifting too. AI blurs the boundaries between product manager, architect and tester, and the episode says seniority increasingly shows in the quality of questions an engineer asks. It also argues that cultures of transparency, such as blameless Q&As, anonymous questions and naming solutions rather than people, let anyone take accountability from any level.

**Takeaways**
- Set a review tier. AI-written changes that touch payments, authentication or personal data get full human review, while routine changes follow the trust-based sampling the episode describes.
- Try an anonymous question channel in your next retro. The episode frames it as a way to make owning mistakes safe.

## A ZIP file that boots a PC and carries the source code to rebuild itself
- ids: 17
- topic: Infra
- signal: notable
- url: https://goliath32.com/blog/ziphead.html
- event: self booting zip archive bootable polyglot
- original title: Creating a self booting ZIP archive
- source: goliath32.com | https://goliath32.com/blog/ziphead.html | via Lobsters
- read: 14 min
- full text: yes

> The archive still passes unzip's integrity test, and its boot code lives in a file inside it, boot/ZIPHEAD.COM.

The author was thinking about early userspace and initramfs when the idea came up. Linux initramfs unpacks CPIO, a standardized format, but the standard CPIO tool is notoriously awkward, and the kernel ships its own tool for the variant it reads. ZIP is widely understood and has a long history of polyglot tricks, including EXE files that unpack themselves.

The result is an ordinary ZIP that contains its own source: A20 gate, disk, memory and multiboot setup code, a console, and the packing tools used to assemble it. Every file passes unzip's test, and the boot code runs from ZIPHEAD.COM. The author's point is less the utility than the demonstration that ZIP's container can carry executable boot code.

Rebuilding is a manual process. After unpacking, the execute bit on mk.sh has to be restored, and zlib must be installed for the tools. Running mk.sh from its directory produces a fresh bootable archive.

**Takeaways**
- Before running mk.sh, restore its execute permission and install zlib, as the setup notes require.
- Treat any boot image from an archive as untrusted code. Inspect boot/ZIPHEAD.COM before booting it on real hardware.
