---
date: 2026-11-21
edition: 60
schema_version: 1
generated_at: 2026-11-21T01:34:29+00:00
sources_ok: 43
sources_total: 47
fetched: 398
candidates: 220
full_text: 11
---

# The Brief

- Mathematics and AI collided again: a Lean-formalized proof of the Generalized Riemann Hypothesis is circulating, and its verification is now the story, not the claim alone.
- Trust in AI infrastructure keeps getting tested from both sides. An AI-router experiment found prompts leaking through resellers, while OpenAI described its own counter-measures against model extraction.
- Privacy is moving from app settings to the operating system. Signal's screenshot block and the UK court order on Apple encryption both show who now controls what an AI agent can read.
- Money and regulation are colliding with AI leadership. Nvidia faces a state subpoena, Anthropic's stock slid on its second trading day, and Bending Spoons bought Mailchimp at a steep discount to its 2021 price.
- Agent infrastructure is getting its own plumbing: Google is handing its agent sandbox and lifecycle tools to the CNCF, and AWS shipped a free local emulator written by agents.

# Stories

## A mathematician claims a Lean-formalized proof of the Generalized Riemann Hypothesis
- ids: 1, 2
- topic: AI
- signal: must-read
- url: https://alpo.ge/remark.pdf
- event: generalized riemann hypothesis proof lean ai
- original title: Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]
- source: alpo.ge | https://alpo.ge/remark.pdf | via Hacker News
- source: terrytao.wordpress.com | https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/ | via Hacker News
- author: Terence Tao
- image: https://secure.gravatar.com/blavatar/bd4bda4207561b6998f10dec44b570f04ff4072b20f89162d525b186dfca3e49?s=200&ts=1795224726
- read: 2 min
- discuss: https://news.ycombinator.com/item?id=50574968 | Hacker News | 2347 points | 1587 comments
- full text: yes

> The claim is enormous, the proof is formalized in Lean, and the verification effort around it is now the real test.

Levent Alpöge, a mathematician at Anthropic, says he has an AI-assisted proof of the Generalized Riemann Hypothesis. The proof exists as a Lean-only formal artifact produced with an internal AI model, and it is reported to be very long. That detail matters, because a Lean proof can be checked mechanically in a way a PDF cannot, but only if someone actually runs the checking and reads what the statements say.

The same author's other results are where the credibility question gets easier. Alpöge and collaborators have posted a human-readable proof of finite-time blow-up for the unforced Euler equations in three dimensions, along with a second blow-up result for the Navier–Stokes equations that is still short of a polished, professionally written paper. Both come with Lean formalizations. A proof this large will take mathematicians some time to digest, and early readers say the strategy appears to draw on the Langlands program and arithmetic geometry, which would be a major result if it holds.

Discussion has moved to a Lean community thread, where moderators have narrowed it to the formal-verification side of the argument. Anyone following the claim should watch for whether that thread settles on the statements being formalized correctly, since a faithful formal statement is what makes the proof meaningful at all.

**Takeaways**
- Follow the Lean verification thread rather than headlines; the question is whether the formal statement matches the conjecture.
- Treat the claim as unverified until independent number theorists confirm the strategy.

## Attackers and resellers leaked nearly two million planted secrets from AI routers
- ids: 26
- topic: Security
- signal: must-read
- url: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/
- event: ai router canary secrets prompt leak
- original title: Researcher plants 2m canaries into the AI supply chain. A privacy disaster surfaced.
- source: Ars Technica | https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/
- author: Dan Goodin
- image: https://cdn.arstechnica.net/wp-content/uploads/2026/11/ai-privacy-leakage-1152x648.jpg
- read: 6 min
- full text: yes

> The experiment planted unique secrets in prompts, and they came back out through providers, resellers and attackers.

Security researcher HD Moore, who is chief research officer at Dragos, sent close to two million AI prompts that each carried a unique, never-used secret: an AWS access key, an SSH password, a private git reference or a unique URL he controlled. He seeded each secret into exactly one prompt sent to exactly one provider, so any later use of it pointed to the link that leaked it. The secrets were built to be traceable, and the results were not subtle.

Moore reports evidence that at least three AI providers were compromised, with attackers siphoning the prompts those providers received. He also found resellers in the inference marketplace that logged prompts and passed them to third parties, and several providers that ignored privacy flags such as zero data retention or "no data collection." The routing layer is the weak spot: services like OpenRouter and Vercel read prompts in plaintext in order to pick a model, so each extra hop is another place a prompt can be copied.

The findings matter most to teams that send production prompts through a broker to save money or pick models. A privacy flag only protects the data if every hop honors it, and the experiment suggests the marketplace does not guarantee that yet.

**Takeaways**
- Audit which AI routers or gateways your prompts pass through, and whether each one logs prompts.
- Do not rely on a zero-retention flag from a broker; confirm the terms with the underlying provider.
- Keep credentials out of prompts entirely, since anything in a prompt should be assumed to be visible to every hop.

## OpenAI says adversarial distillation cut protected-reasoning extraction from 54% to 0.2%
- ids: 44
- topic: AI
- signal: must-read
- url: https://openai.com/index/combatting-adversarial-distillation
- event: openai adversarial distillation protected reasoning
- original title: Combatting adversarial distillation
- source: OpenAI Blog | https://openai.com/index/combatting-adversarial-distillation
- image: https://images.ctfassets.net/kftzwdyauwt9/5SUtPGdssrttC7LfP1yoJ1/b6b000846ab3576c1735c29534ab20b0/combatting-adversarial-distillation-social.png?w=1600&h=900&fit=fill
- read: 9 min
- full text: yes

> OpenAI is treating model extraction as a safety problem, not only an intellectual-property one.

OpenAI describes adversarial distillation as a route by which a bad actor copies a frontier model's capabilities without its safeguards, then deploys the copy for uses the original would refuse, such as cyberattacks. The company's main target is protected reasoning, the intermediate chain-of-thought a model generates before answering, which is often the most useful training data for a copy. In an internal adaptive red-team evaluation, the average attack success rate for recovering that reasoning fell from 54.0% on GPT-6 Astra with its original safeguards to 0.2% on GPT-6.2 Astra with updated ones.

The defense is layered. OpenAI combines adversarial testing, model training, classifiers, API-level protections and investigations into coordinated extraction attempts. The company says these safeguards now look more like the ones it uses for biology and cybersecurity, which tells you where it thinks the real risk sits.

The numbers come from OpenAI's own evaluation, with no outside replication yet. The open question is how much a determined attacker can recover through the API before the classifiers catch the pattern, and whether other labs adopt comparable protections.

**Takeaways**
- If you build on frontier APIs, expect tighter rate and pattern controls on high-volume reasoning-heavy requests.
- Check whether your product relies on exposed reasoning traces; OpenAI's direction suggests those will be harder to obtain.

## Frostbite: a CPU with a new instruction set, reported as 4.59× better perf per watt
- ids: 5
- topic: Infra
- signal: must-read
- url: https://architectlabs.com/blog/frostbite
- event: frostbite ai designed cpu architecture
- original title: Frostbite: A new CPU architecture discovered, designed and verified by AI
- source: architectlabs.com | https://architectlabs.com/blog/frostbite | via Hacker News
- image: https://main--gleeful-begonia-6bb5f3.netlify.app/_next/static/media/frostbite-cover.3n9ytugnquhlr.jpg
- read: 14 min
- discuss: https://news.ycombinator.com/item?id=50572503 | Hacker News | 623 points | 326 comments
- full text: yes

> The chip is a vendor claim on a narrow benchmark set, but the design flow is the notable part.

The announcement describes Frostbite, a general-purpose CPU with a new instruction set, which its makers say was discovered, designed and verified end to end by AI systems. Those systems iterated over the compiler, instruction set, microarchitecture, RTL, verification and final GDS layout. The reported result is a 4.59× performance-per-watt gain over a silicon-proven dual-issue, in-order superscalar core on 25 workloads, 15 of which were held out until final evaluation.

The design rests on interaction nets, a computing model where each step touches only nearby data, links between pieces of work are spelled out, and each piece of data belongs to a single owner. The authors argue that mainstream CPUs spend large amounts of area and power rediscovering dependencies at runtime and maintaining cache-coherence illusions, and that an architecture which encodes those dependencies up front can avoid much of that cost.

Two caveats matter before anyone reads this as a general speedup. The baseline is an in-order dual-issue core, not a modern out-of-order design such as the server parts from Intel, AMD or NVIDIA, and the workload set is small. The result still matters because it is an end-to-end, silicon-level claim, and an independent team with access to the RTL or a fabricated part would be the real test.

**Takeaways**
- Compare the claim against an out-of-order baseline before drawing conclusions for server or laptop CPUs.
- Watch for the workload list and any tape-out or independent measurements, which would turn the claim into evidence.

## Signal now blocks screenshots by default to keep AI assistants from reading chats
- ids: 121, 122
- topic: Security
- signal: recommended
- url: https://www.engadget.com/2323574/signal-now-blocks-screenshots-by-default-to-stymie-ai-agents/
- event: signal screenshot block ai agents
- original title: Signal now blocks screenshots by default to stymie AI agents
- source: Engadget | https://www.engadget.com/2323574/signal-now-blocks-screenshots-by-default-to-stymie-ai-agents/
- source: Slashdot | https://yro.slashdot.org/story/26/11/20/2231247/signal-restricts-screenshots-to-block-ai-agents-from-reading-messages
- author: Will Shanklin
- image: https://www.engadget.com/img/gallery/signal-now-blocks-screenshots-by-default-to-stymie-ai-agents/l-intro-1795205811.jpg
- read: 3 min
- full text: yes

> Signal's default protection covers only its own side of a conversation, and it wants the operating systems to offer more.

Signal says it will block screenshots by default on iOS 27, add a "Block Siri AI" setting that is on by default, and on Android block AI assistants from capturing the screen through its existing screen-security option. A prompt offers to turn the protection off whenever a screenshot or an assistant reading the screen is detected. Signal calls built-in assistants an existential threat to private messaging and points to a 2025 move in which it blocked Microsoft Recall in the same way.

The protection has limits. If the other person has disabled it, an assistant on their device can still read the conversation. Third-party agents can read notifications on Android and, on Mac, can use accessibility permissions that Signal describes as a skeleton key. On Mac, Signal says it has no user-level protection at all. The company wants a standard, system-level way for apps to keep AI agents out, and it says it is talking with Apple and Google.

**Takeaways**
- Review which AI assistants and agents have accessibility or notification access on your phone and Mac.
- Check the screen-security toggle in Signal on Android, since the default and prompt behavior differ by platform.

## Anthropic shares fell more than 11% on their second day of trading, dragging the Nasdaq below 2026 levels
- ids: 141
- topic: Startups
- signal: recommended
- url: https://news.slashdot.org/story/26/11/20/1934244/anthropic-shares-tank-after-huge-ipo-as-the-nasdaq-erases-2026-gains
- event: anthropic ipo nasdaq pricing
- original title: Anthropic Shares Tank After Huge IPO As the Nasdaq Erases 2026 Gains
- source: Slashdot | https://news.slashdot.org/story/26/11/20/1934244/anthropic-shares-tank-after-huge-ipo-as-the-nasdaq-erases-2026-gains
- author: BeauHD
- full text: no

> The IPO priced above range, and the market turned on the stock within two sessions.

Anthropic's record-setting IPO had priced above its range on Thursday, valuing the company at about $1.5 trillion. On its second day of trading, its shares dropped more than 11%, and the broader market followed. The Nasdaq fell more than 3%, erasing its 2026 gains, while the S&P 500 dropped nearly 2% and moved into correction territory, at least 10% below recent highs.

This report is a snippet-level account of the day's market move, so the figures above come from the headline and standfirst, not a full article. What the moves show is that the new listing is being traded against a falling tech market rather than in a rising one. For investors, the first two sessions set the price discovery for the stock; for competitors and customers, they are an early read on how public markets value frontier AI labs.

**Takeaways**
- Watch the first post-IPO earnings and lock-up schedule rather than the opening-day pricing.
- Treat single-day moves in new listings as noisy until volume settles.

## California's attorney general subpoenas Nvidia over Jensen Huang's China ties
- ids: 123, 124
- topic: Startups
- signal: recommended
- url: https://techcrunch.com/2026/11/20/california-ag-subpoenas-nvidia-over-worries-about-huangs-ties-with-china/
- event: california subpoena nvidia huang china
- original title: California AG subpoenas Nvidia over worries about Huang’s ties with China
- source: TechCrunch | https://techcrunch.com/2026/11/20/california-ag-subpoenas-nvidia-over-worries-about-huangs-ties-with-china/
- source: Slashdot | https://yro.slashdot.org/story/26/11/20/1755250/california-issues-subpoena-to-nvidia-over-chip-sales-to-china
- author: Ram Iyer
- image: https://techcrunch.com/wp-content/uploads/2026/05/nemoclaw.jpg?resize=1200,675
- read: 2 min
- full text: yes

> The state is asking whether Nvidia's chips or secrets reached China and whether the company misled investors about it.

California Attorney General Rob Bonta said his office has served an investigative subpoena on Nvidia. The inquiry centers on whether advanced GPUs or confidential information reached China through Jensen Huang's alleged relationship with a woman the U.S. government believes is a Chinese spy, and whether the company misled investors about the risk. Huang resigned as CEO last week after further reports of relationships with employees, and the company's new chair has said Nvidia will not bring him back.

The investigation is one of several. Nvidia's board has hired a law firm and an independent slate of directors, the SEC is reportedly looking at whether public disclosures were misleading, and Congress is moving to question Huang, who has agreed to testify. The subpoena makes the risk concrete for investors, because the question is about disclosure as much as about chips.

**Takeaways**
- Watch Nvidia's next securities filings for language about the independent investigation and any export-compliance findings.
- If you rely on Nvidia supply, check how export rules and the investigation could shape allocation or shipments.

## Bending Spoons buys Mailchimp from Intuit for $3.68 billion, about a third of what Intuit paid in 2021
- ids: 163, 187
- topic: Startups
- signal: recommended
- url: https://techcrunch.com/2026/11/20/bending-spoons-buys-mailchimp-for-3-68-billion/
- event: bending spoons mailchimp intuit acquisition
- original title: Bending Spoons buys Mailchimp for $3.68B
- source: TechCrunch | https://techcrunch.com/2026/11/20/bending-spoons-buys-mailchimp-for-3-68-billion/
- source: Slashdot | https://tech.slashdot.org/story/26/11/20/0121230/intuit-sells-mailchimp-at-about-a-third-of-its-2021-purchase-price
- author: Russell Brandom
- image: https://techcrunch.com/wp-content/uploads/2024/11/GettyImages-2150300479.jpg?resize=1200,800
- read: 2 min
- full text: yes

> The deal is cheap for the buyer and a sign that Intuit is retreating from email marketing to chase AI tools for small business.

Bending Spoons has agreed to buy Mailchimp from Intuit for $3.68 billion. Intuit paid roughly $12 billion for the company in 2021. The sale is mostly cash, but Intuit is also buying $368 million in newly issued Bending Spoons shares, so the package is about 90% cash and 10% stock. Intuit says it will use the proceeds to repurchase its own shares and focus on AI tools for small businesses.

Bending Spoons has made a habit of buying older web properties and running them on consolidated engineering and revenue systems. Its recent purchases include AOL, Eventbrite, Airtable and Miro, and earlier ones include Evernote, Meetup and Vimeo. The company says the approach improves support and product resources while cutting costs, and the pattern suggests Mailchimp will follow the same route toward shared systems and tighter operations.

**Takeaways**
- Mailchimp customers should watch for changes to plans, pricing and account terms in the months after closing.
- Teams that depend on Mailchimp integrations should check their APIs and webhooks against any platform changes.

## Google gives its agent sandbox and lifecycle tools to the CNCF
- ids: 39
- topic: Infra
- signal: recommended
- url: https://www.infoq.com/news/2026/11/google-substrate-gvisor-cncf/
- event: google agent substrate gvisor cncf
- original title: Google Donates Agent Substrate and gVisor to the CNCF to Secure AI Agents at Scale
- source: InfoQ | https://www.infoq.com/news/2026/11/google-substrate-gvisor-cncf/
- author: Craig Risi
- image: https://res.infoq.com/news/2026/11/google-substrate-gvisor-cncf/en/headerimage/generatedHeaderImage-1794408775099.jpg
- read: 3 min
- full text: yes

> Agents spend most of their time idle while holding state, which is a poor fit for a pod-per-agent model in Kubernetes.

Google is handing two pieces of its agent stack, Agent Substrate and gVisor, to the CNCF, the body that stewards Kubernetes. It is bundling OpenRL, its open-source reinforcement-learning orchestrator, into the same move. gVisor is meant for running untrusted, AI-generated code safely, and Agent Substrate manages the life cycle of agent sessions. Google estimates that agents spend 90 to 95% of their time idle while still holding memory, files and session state.

Agent Substrate separates long-lived agent state, called actors, from reusable pre-warmed execution environments, called workers, drawn from shared Kubernetes pools. Google says an agent can resume in under 500 milliseconds without a new pod. The design targets two problems: pods that sit wasted between tool calls, and control-plane strain when thousands of short-lived environments are created during large evaluations. The CNCF move is a governance step, and the announcement does not include adoption numbers.

**Takeaways**
- If you run agents on Kubernetes, measure how much pod time sits idle between tool calls before choosing a design.
- Watch whether the CNCF projects gain outside maintainers, since governance will decide how much teams can rely on them.

## A transcription firm used by police exposed interview recordings on an open cloud bucket
- ids: 171
- topic: Security
- signal: recommended
- url: https://techcrunch.com/2026/11/20/a-transcription-firm-used-by-police-prosecutors-and-tech-giants-exposed-customer-data-online/
- event: tigerfish transcription s3 exposed police recordings
- original title: A transcription firm used by police, prosecutors, and tech giants exposed customer data online
- source: TechCrunch | https://techcrunch.com/2026/11/20/a-transcription-firm-used-by-police-prosecutors-and-tech-giants-exposed-customer-data-online/
- author: Zack Whittaker
- image: https://techcrunch.com/wp-content/uploads/2025/06/GettyImages-2150052525.jpg?resize=1200,800
- read: 4 min
- full text: yes

> Tigerfish's bucket needed no password, and its operator's first warning went to spam.

Tigerfish, a San Francisco transcription company whose customers include police departments, prosecutors' offices and large tech companies, left an Amazon S3 bucket publicly listed and reachable without a password. The bucket held transcriptions of police interviews, body-camera footage, raw customer audio and video, and customer invoices. Security researcher Anurag Sen found it in October and says he alerted the company, which did not reply. His email was caught in the company's spam filter.

Sen later contacted TechCrunch, which verified the source and the data before reaching Tigerfish. The company then blocked public access to the bucket and said its other buckets were also locked down. It is not clear whether Tigerfish has told its customers, and the case shows how a single misconfiguration can expose criminal-justice material for weeks.

**Takeaways**
- Audit cloud storage for public listing and block public access at the account level.
- Vendors handling police or legal recordings should have a published disclosure channel that avoids spam filters.

## The UK must confirm a secret order demanding Apple provide encrypted customer data
- ids: 173
- topic: Security
- signal: recommended
- url: https://yro.slashdot.org/story/26/11/20/0129229/uk-government-forced-to-disclose-secret-apple-backdoor-order
- event: uk apple encryption backdoor order tribunal
- original title: UK Government Forced To Disclose Secret Apple Backdoor Order
- source: Slashdot | https://yro.slashdot.org/story/26/11/20/0129229/uk-government-forced-to-disclose-secret-apple-backdoor-order
- author: BeauHD
- full text: no

> A tribunal has rejected the Home Office's secrecy claim, which makes the order a public matter.

The Investigatory Powers Tribunal has ordered the UK government to confirm that it issued a secret order demanding Apple provide authorities with encrypted customer information. The tribunal rejected the Home Office's argument that disclosing the order would harm national security, a rare rebuke in a process where the government usually keeps such orders confidential. The details come from a short report, so the scope of the order is not yet clear.

The ruling matters because it moves a backdoor demand from the secret to the public record. Whether the order would require Apple to decrypt customer data, and whether it applies to the UK only, will shape how other companies respond to similar demands.

**Takeaways**
- Watch the government's confirmation and any Apple statement about what it can access in end-to-end encrypted services.

## GnuPG's GPGME library has a critical security bug that reaches mail clients and Flatpak
- ids: 142
- topic: Security
- signal: notable
- url: https://www.phoronix.com/news/GnuPG-GPGME-Critical
- event: gpgme critical security bug gnupg
- original title: GnuPG's GPGME Affected By Critical Security Bug In Turn Affecting Mail Clients, Flatpak
- source: Phoronix | https://www.phoronix.com/news/GnuPG-GPGME-Critical
- author: Michael Larabel
- full text: no

> GPGME is a shared library, so one flaw can reach many email clients and sandboxed apps at once.

GnuPG's author Werner Koch announced a critical security bug in GPGME, the library that makes GnuPG usable from other software. The bug affects a wide set of dependents, including most email clients, most XMPP chat clients, Flatpak, and Samba. This story comes from the headline and standfirst only, so the exact trigger and affected versions are not confirmed here.

**Takeaways**
- Update GPGME and the mail and chat clients built on it as soon as your distribution ships a fix.

## AWS releases a free, CC0-licensed local emulator of more than 200 of its services, written by agents
- ids: 49
- topic: Dev Tools
- signal: recommended
- url: https://www.infoq.com/news/2026/11/aws-emulator-local-testing/
- event: aws emulator agents cc0 local
- original title: AWS Releases a Free Local Emulator of AWS Built Entirely by Agents
- source: InfoQ | https://www.infoq.com/news/2026/11/aws-emulator-local-testing/
- author: Steef-Jan Wiggers
- image: https://res.infoq.com/news/2026/11/aws-emulator-local-testing/en/headerimage/generatedHeaderImage-1795086946449.jpg
- read: 6 min
- full text: yes

> The emulator is useful to agents only as long as its behavior matches AWS, and that gap is now measurable.

AWS Emulator is a free local implementation of more than 200 AWS services, released under CC0, and AWS says thousands of autonomous agents wrote every line. It ships as a single Rust binary generated from 438 public API models, and it listens on port 9297. Teams point their SDKs and coding agents at it with environment variables such as AWS_ENDPOINT_URL, and AWS's launch example has an agent create and read back a DynamoDB table through ordinary CLI calls.

The main risk is fidelity. Matt Wood, AWS's chief AI and technology officer, says the loop matters because agents may build on incorrect assumptions if they test against a fast local stand-in. If the emulator accepts a request that AWS rejects, an agent can learn the wrong lesson, and a shortcut that works only because of an emulator defect can look like success. Early independent fidelity numbers have arrived, and practitioners remain divided.

**Takeaways**
- Before trusting the emulator in agent tests, run the same calls against real AWS for the services your code depends on.
- Keep emulator credentials and endpoint variables separate from production profiles in your shell and CI.

## ASP.NET Core in .NET 11 adds union types in JSON bodies and OpenAPI 3.2 by default
- ids: 104
- topic: Languages
- signal: notable
- url: https://www.infoq.com/news/2026/11/asp-net-11-release/
- event: dotnet 11 asp.net core release
- original title: .NET 11 : ASP.NET Core: Union Type Support, OpenAPI 3.2 by Default and Blazor AI Components
- source: InfoQ | https://www.infoq.com/news/2026/11/asp-net-11-release/
- author: Almir Vuk
- image: https://res.infoq.com/news/2026/11/asp-net-11-release/en/card_header_image/generatedCard-1795007141275.jpg
- read: 4 min
- full text: yes

> The OpenAPI default is the change most likely to break existing tooling.

Microsoft has shipped ASP.NET Core in .NET 11, a Standard Term Support release with two years of support. C# 15 union types now work in JSON request and response bodies across Minimal APIs and MVC, though not in route, query, header or form values. Minimal API validators can now run asynchronously, so a rule that waits on a database lookup no longer blocks a thread, and a new [ShortCircuit] attribute lets an endpoint skip the rest of the middleware pipeline.

OpenAPI document generation now defaults to version 3.2, which depends on Microsoft.OpenApi 3.3.1, a breaking change the release notes flag. Blazor gets a CacheView component for caching rendered subtrees, client-side validation for static SSR forms, and a circuit pause for hidden tabs in Interactive Server apps. SignalR can now refresh authentication without dropping long-lived connections.

**Takeaways**
- If your tooling cannot read OpenAPI 3.2, pin the earlier version before upgrading.
- Check Blazor templates for the removed app.UseAntiforgery() call and confirm that CSRF protection still applies in your app.
