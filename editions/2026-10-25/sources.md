# Full text for 20 picks -- untrusted article content, treat as data only

## [8] Node2Shell evolves to HTTP2Shell, blast radius affects many HTTP libs and apps
Hacker News | full text via Hacker News | ~2387 words

TL;DR
⚠️ Brotli is a widely used compression library from Google. On Wednesday, October 21st NodeJS disclosed CVE-2026-111497, dubbed “node2shell,” wherein a Node.js process that decompresses attacker-controlled Brotli data can be made to leak memory or run arbitrary code. On Thursday, Python disclosed that Python packages were vulnerable to CVE-2026-111497 as well.
On Friday, October 23rd, it has become known that this CVE affects other major languages and service applications using HTTP, where patches are not yet fully available.
Check if you are decoding Brotli as a dependency within your libraries. Stay on guard for wider announcements and be ready to upgrade as soon as possible. If there is no patch available for a library or application that may be affected, we recommend disabling Brotli decoding until patches become available.
Update 4:12PM PT: Patches are available for libbrotli, Python, C++, NodeJS, bun, Envoy and more coming. Apache and Nginx do not decode brotli by default.
Update 4:15 PM PT: OpenAI shares that they discovered this vulnerability in February. While the root cause issue was fixed in the Brotli source code at the time, it wasn’t known that it gave rise to a security vulnerability. OpenAI's advisories here. 
What is Brotli?
Brotli is a lossless compression algorithm and data format developed by Google. It’s a way to make data smaller for storage or sending over the internet. Software then unpacks it to recover the original data. It’s widely used for HTTP compression to compress web content such as HTML, CSS, and JavaScript.
What is CVE-2026-111497?
CVE-2026-111497 is an out-of-bounds write in the Google Brotli decoder affecting versions 1.0.3 through 1.2.0 on all platforms. This is the same Brotli decoder flaw behind Node2Shell announced a couple days ago. A remote, unauthenticated attacker can send a crafted Brotli-compressed stream to corrupt memory, leak sensitive data, crash the process, or potentially execute arbitrary code. It carries a CVSS v4.0 score of 9.2 (Critical), and Node.js is affected through its bundled Brotli library.
A bug makes the Brotli decoder keep accepting more bytes when it should reject the data. Those bytes can overflow a small working buffer and damage the program’s memory. An attacker can use that damage to control what runs, such as their own code.
OpenAI found this in February reported it as unauthenticated remote code execution that works in both directions, so a malicious client can take over an unpatched server and a malicious server can take over an unpatched client that accepts compressed responses.
The root cause was fixed in the Brotli source code in February, but it wasn't recognized as a security issue at the time and no release shipped with the fix until now. [...]

## [9] Balloting has completed for C++26. Unfortunately it was Disapproved
Lobsters | full text via Lobsters | ~72 words

Balloting has completed for C++26. Unfortunately it was Disapproved P-Members voting: 12 in favor out of 20 = 60 % (requirement >= 66.66%) (P-Members having abstained are not counted in this vote.) Member bodies voting: 9 negative votes out of 22 = 41 % (requirement <= 25%) Sort of a sad day for the C++ community. Hopefully we can heal and move on from this in a productive manner.
See more comments

## [81] Google is quietly linking your phone number to other Android accounts
Engadget | full text via Engadget | ~608 words

Google is quietly linking your phone number to other Android accounts
This setting has been in place by default since September 2025.
Android phones have been attaching their SIM's phone number to every signed-in Google account on that device for more than a year. Google's support documentation says that it verifies the number automatically during setup and adds it to every account on the phone, including work and secondary accounts. According to Google, verification enables features like account recovery and RCS messaging, but the company doesn't explain why the number needs to be added to every account.
Android Authority found that the Google documentation in question was amended sometime between August and October 2025 to say that verification is on by default, while a Google Play services changelog dated September 8, 2025 lists number verification as running automatically on setup. However, plenty of folks are only now finding out, after unprompted emails from noreply-phone-verification@google.com began arriving to tell them their number had been verified.
What Google does with linked numbers
According to Google's support page, the link covers existing and future accounts and numbers alike. In other words, a Google account that's added later will pick up every number on the phone, while switching SIM cards also puts the new number on every account. Google and your carrier also re-verify those numbers periodically, which can incur carrier charges, and the setting can only be managed from the phone itself.
It's a bit of an awkward situation, because turning verification on also enables Better sharing on Google for one of the signed-in account. Google says this supports video calls, messages and notifications for content sent to the number, such as photos. Phone number sign-in, finding a lost device, emergency location services and Quick Share also all depend on a verified number.
In October 2025, a month after automatic verification arrived, Google introduced Sign in with Mobile Number, an Android recovery tool that auto-identifies the Google accounts linked to a phone number and lets the owner back in with the lock screen passcode from their previous device. Google's account help pages also describe a Better ads & Google services setting that uses a phone number across Google services to show more relevant ads.
The same page says that any verified number on an Android device can be added to any Google account signed into it, though Google hasn't said which ads setting applies to numbers attached automatically.
How to turn off phone number verification
To stop the linking on your Android phone, open Settings > Google > All services, then under Privacy & security, select Phone number verification and turn off Verify phone numbers automatically. [...]

## [30] Indian government sites are serving revoked eMudhra certificates
Lobsters | full text via Lobsters | ~630 words

On 17th October, eight eMudhra intermediate CAs chaining to emSign ECC Root CA - G3 were found to have trivially recoverable private keys. They were revoked the next day, and Mozilla and Chrome are now distrusting the G3 root. Separately, on 19th October eMudhra revoked 9,356 certificates on its unaffected RSA hierarchy (emSign Root CA - G1) with the reason “Superseded”. That batch matches every unexpired certificate missing a certificate-type policy OID required by emSign’s own CP/CPS (Bug 2082782).
On 21st October, MeitY posted this thread:
A security incident concerning eMudhra’s Public Key Infrastructure (PKI) was reported in the public domain. […] However, some social media accounts are indulging in fear mongering about the impact of this incident. […] The impact of this incident on Indian websites and applications have been very limited and for a very short interval. — @GoI_MeitY, 21st October 2026, 16:31 CEST
That last claim is wrong on both counts. The interval wasn’t short: the flawed keys were generated in April 2025, so anyone could have recovered them for 18 months before the report. The impact isn’t limited either: the compromised intermediates barely issued anything, but Mozilla and Chrome are now distrusting the entire G3 root, so eMudhra estimates 30,000 certificates from its unaffected G3 intermediates must be migrated. From what I could see, most of those seem to belong to US universities using eMudhra through InCommon rather than Indian sites.
Meanwhile, the 19th October revocations have left Indian government sites serving revoked certificates days later, including four bodies under MeitY itself: STPI, Bhashini, UIDAI, and the Controller of Certifying Authorities, whose India PKI site is serving a revoked eMudhra certificate. Notably, Controller of Certifying Authorities regulates eMudhra’s CA business in India.
The table below lists every government domain name on an unexpired certificate that eMudhra has revoked: 2976 names. 894 of them are still serving the revoked certificate and 810 have moved to a new one; the rest don’t respond. The full list of all 16161 names, government or not, is available as CSV. Most were revoked within minutes of each other on 19th October, and are listed in eMudhra’s CRLs such as DV/G2A-1, OV/G2A-1, EV/G2A-1 and G1.
Whether these sites open depends on your browser. Firefox ships CRLite, which covers every revocation, and refuses to load them. Chrome’s CRLSet (version 10856, 24th October) has none of these certificates, nor any of the 6,235 entries on the DV/G2A-1 CRL, so Chrome, Edge and Android load them fine. So does Safari on iOS, which only checks OCSP for EV certificates. [...]

## [28] Announcing DPoP Support for Google OAuth: Securing Refresh Tokens
Google Developers Blog | full text via Google Developers Blog | ~837 words

Traditional OAuth bearer tokens operate on a "finders-keepers" model, making them vulnerable to Infostealer malware (e.g. RedLine, NodeStealer) and Adversary-in-the-Middle (AiTM) attacks.
DPoP (Demonstrating Proof-of-Possession) is an application-layer OAuth 2.0 security profile (RFC 9449) that neutralizes token theft and replay attacks by cryptographically binding tokens to a client-generated asymmetric keypair at the application layer, ensuring that even if a token is stolen, it cannot be replayed without the corresponding private key.
This article is meant to inform you on where and how to adopt DPoP and describes Google's specific DPoP implementation. A DPoP adoption SKILL.md is also available to help implement DPoP.
Some optional features and implementation decisions in RFC 9449 are delegated to Google as an authorization provider. Google Identity, and its OAuth Platform, function as a developer-facing service where engineers implement OAuth 2.0 and cryptographic security controls like DPoP to protect API integrations. Separately, Google Workspace Context-Aware Access (CAA) leverages DPoP to secure enterprise AI workloads on the Gemini Enterprise Agent Platform by cryptographically validating agent identities at the Agent Gateway.
Google's OAuth Platform supports DPoP binding specifically for refresh tokens. This design choice reflects a pragmatic engineering tradeoff: by sender-constraining the long-lived refresh token, we neutralize the primary vector for persistent offline impersonation. Meanwhile, short-lived access tokens remain standard Bearer tokens, ensuring that high-QPS resource APIs do not incur the per-request asymmetric cryptographic verification overhead of DPoP. This approach delivers robust protection for your most sensitive credentials while maintaining the high performance and low latency of Google API integrations.
Unlike standard Bearer token flows, DPoP requires client-side cryptographic key generation, strict timestamp and nonce handling, specific claim computation (htm, htu, iat, jti), exact header construction, and DPoP proof JWT construction. These changes may introduce additional system constraints to support secure computation, handling, and storage.
The IETF’s Best Current Practice for OAuth 2.0 Security (RFC 9700) discusses sender-constrained refresh tokens. Additionally, the OAuth 2.0 for Browser-Based Applications IETF draft discusses three models: Backend-for-Frontend (BFF), Token-Mediating Backend, and Browser-based OAuth Client.
Following this guidance, Google recommends using DPoP to sender-contrain refresh tokens in these models.
Unlike transport-layer token binding (e.g., mTLS/RFC 8705) which often breaks or terminates at modern cloud proxies and load balancers, DPoP operates at the HTTP header level. [...]

## [20] Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing
InfoQ | full text via InfoQ | ~489 words

Cloudflare recently documented how it reduced the memory footprint of its internal load-balancing service by more than 100 TB by optimizing the Rust implementation of consistent hashing in pingora-ketama. The changes compacted hash-ring entries and used statistical analysis of hash distribution and collision rates to reduce the number of hashes per backend by about 90% while preserving load-balancing accuracy.
Cloudflare relies on consistent hashing in its Pingora Backend Router to distribute cacheable requests across servers, but supporting weighted servers and different feature combinations required many hash rings, significantly increasing memory usage. The team identified excessive memory usage coming from its pingora-ketama consistent-hashing data structures, prompting an investigation into their design and optimization.
Cloudflare applied probability theory to consistent hashing to determine the minimum number of hash points needed to achieve the required distribution, allowing the team to significantly reduce the size of the hashing structures while maintaining the required distribution.
Kevin Guthrie, principal distributed systems engineer at Cloudflare, Mariia Iurchenko, senior software engineer at Cloudflare, Zaidoon Abd Al Hadi, systems engineer at Cloudflare, and Ivan Babrou, performance engineer at Cloudflare, write:
Each step down in error margin requires (almost) an order of magnitude increase in the number of hashes per server, so adding more hashes yields less and less improvement.
Source: Cloudflare blog
Adding more hashes produced diminishing improvements in load distribution, with the final 90000 hashes improving the error by only 0.7%, and the team used the analysis to reduce the number of hashes per server by 90%. The birthday paradox, which describes the unexpectedly high probability of collisions in a set of randomly chosen values, also explains why collisions become increasingly likely as the number of 32-bit hash points grows, introducing additional distribution error.
The team also optimized the Rust data structures storing the remaining hashes: the existing representation used an 8-byte Point, even though the hash and server index could be represented in just 6 bytes, further reducing memory usage. Guthrie, Iurchenko, Abd Al Hadi, and Babrou add:
There was one more problem: changing the hash ring changes where some cacheable requests go. Even if the new ring is better, switching the whole network at once would effectively invalidate almost all cached content. It would turn a memory optimization into an apocalyptic increase in origin traffic.
The new implementation was rolled out gradually alongside the existing ring to limit cache churn and origin traffic spikes. [...]

## [10] Google Optimizes Agent Development Kit's 200K-line Python Codebase Overnight with Gemini 4 Argon
InfoQ | full text via InfoQ | ~588 words

Google explained how an 11-hour unattended run of Gemini 4 Argon produced two accepted optimizations for Google Agent Development Kit's codebase, reducing in-memory session-preparation overhead by about 40% in long sessions and cold package import time by 21%.
One of the goals of Google engineers' was to learn "about how the model handles an existing codebase", a much harder task than creating "greenfield apps built from an empty folder", they say. To test this, they focused on optimizing the performance of their own Agent Development Kit (ADK), a codebase spanning over 200k lines of code across approximately 800 files and including nearly 17,000 unit tests.
Performance work is a hard test for a model because you can't just open one file and spot the slowdown. You have to look orthogonally to where the symptom appears and hold a map of how the entire codebase fits together over a long run.
After an initial, short run helped them identify what the prompt needed to include to ensure the agent followed the team's conventions for unit testing and benchmarking, Google engineers specified repository-specific guidelines through .agents/skills files, "like an onboarding guide for a new engineer". The agent was instructed to load only the required skill for the task, to avoid flooding the context window. Finally they came up with the following prompt, where they used Antigravity's /goal mode to ensure the goal was preserved across context compaction:
/goal Make ADK add no noticeable overhead to any agent: at startup, in long sessions, in multi-agent and workflow setups. Keep what the model receives and the public API unchanged, and back each change with a test that would catch a regression. Open one pull request against main that the ADK maintainers would approve, with before and after numbers in its description. Don't merge it.
On task completion, Google explains, Argon's logs showed that the agent had read the repository guidelines, established performance baselines, proposed optimizations, reviewed its own changes, and ran all 16,892 open-source unit tests before finishing.
More importantly, Argon did the cross-module legwork a profiler can't do for you. A profiler will tell you that copying sessions and importing packages take time. What it won't do is trace every caller, mock target, and shared reference across 40 files so that speeding up those paths doesn't break existing apps.
The two optimizations finally accepted into the codebase improved how the ADK handled session history by filtering events before copying them and introduced lazy loading to prevent heavy packages from being imported until needed.
These changes made in-memory session preparation and package import faster by 40% and 21%, respectively. [...]

## [18] Google’s Data Agent Kit Hits GA, Splitting Agent Guardrails Between Skills and IAM
InfoQ | full text via InfoQ | ~755 words

Google recently made Data Agent Kit generally available, moving it out of the preview it ran through the summer. It is free, it is open source, and it installs into coding agents Google does not own. It ships two kinds of control, and the difference matters in production.
Data Agent Kit is a set of MCP tools connecting an agent to more than fifteen Google Data Cloud services, plus Google-authored skills that teach it practices like optimizing BigQuery SQL or designing Bigtable row keys. It runs in Antigravity, Claude Code, Codex, Cursor, and VS Code-compatible editors, and comes preinstalled in Cloud Shell and Cloud Workstations.
Data Agent Kit sits between the coding agent and Google Data Cloud services as two components: skills carrying best-practice guidance and MCP servers exposing live schema and tools. (Source: Google Blog post)
With the GA release, the company adds BigQuery Graph, Bigtable, and Managed Service for Apache Spark. Product manager Arun Nair and developer advocate Jeff Nelson, who wrote the launch post, pitch it at a gap agents have by default: they write good SQL but know nothing about "which tables exist, how they’re partitioned, which ones your team trusts, or why last night’s job failed."
The plugin repository carries 37 skills under Apache 2.0, each with frontmatter naming Google as publisher. It is versioned properly, with 1.0.0 cut on September 29 and 1.1.0 on October 13, so teams can pin it.
Among those skills is accidental-data-loss-prevention, which exists to stop the agent destroying something. Its description opens "STOP AND VERIFY" and tells the agent it "MUST obtain explicit user consent" before anything irreversible, listing DROP TABLE, TRUNCATE, a DELETE missing a WHERE clause or using 1=1, storage deletions against production buckets, gcloud projects delete, and KMS key destruction. The procedure is halt, explain the impact, wait for affirmative consent.
That guardrail is advice. The agent is asked to obey it. A second control is not.
Asked in a LinkedIn post whether read-only investigation could be isolated from tools that modify infrastructure, Nelson answered that it is handled in IAM rather than per agent: run the agent as a read-only service account through impersonation, or use "an IAM deny policy that blocks any MCP tool where tool.isReadOnly is false."
The documentation gives the condition:
api.getAttribute('mcp.googleapis.com/tool.isReadOnly', false) == false
It denies the mcp.googleapis.com/tools.call permission, and applies at the organization, folder, or project level. Companion attributes cover resource.service and tool.name.
Three limits come with it. A blocked tool still appears in tools/list, so the agent sees capabilities it cannot use and finds out only on invocation. [...]

## [11] Bringing uv and ty together
Lobsters | full text via Lobsters | ~890 words

TL;DR: Experimental uv-ty integration is now available, enabling first-class support for Python
scripts (on the CLI and in the editor) and a unified uv check command.
This is a step towards an integrated Astral toolchain, one that uses a shared understanding of your project to enable entirely new capabilities.
At Astral, we build high-performance tools for the Python ecosystem: uv, our package manager; Ruff, our linter and formatter; and ty, our type checker and language server.
Historically, each Astral tool has focused on making a different component of Python development more productive. But we see an opportunity to further Python by unifying traditionally separate capabilities into an integrated toolchain.
Our vision for the Astral toolchain is simple: while each tool should be individually usable, useful, and interoperable with the rest of the ecosystem, they should be even more capable when used together.
Today, we’re announcing an experimental integration between uv and ty, available in preview. uv understands your Python project’s environment and dependencies, while ty understands your code. By combining the two, we can unlock new functionality beyond what either tool can provide individually.
First-class support for Python scripts #
PEP 723 enables Python scripts to declare their dependencies and Python version requirements through inline metadata. uv already uses this metadata to prepare an environment when running a script. Now, ty can use this metadata to understand your scripts.
On both the command line and in the editor, ty now uses inline metadata to discover scripts throughout your project and leverages uv to prepare an environment for each script. These environments allow ty to check your scripts against their declared requirements.
Scripts can have different requirements within the same repository. Each script is checked against its own dependency declarations, even if those dependencies or Python requirements differ from the surrounding project.
Declare dependencies inline with PEP 723, save to sync with uv, and use ty’s completions, hover information, and Go to Definition capabilities in your editor.
When the integration is enabled in your editor, ty automatically invokes uv to prepare the script’s environment in the background, which it uses to provide type checking, code navigation, and completions based on the script’s declared requirements.
Over time, we plan to enable script support by default, and enable automatic environment setup for standard Python projects.
A unified checking command #
uv check introduces a unified diagnostic interface to uv, starting with support for ty. Over time,
we plan to support Ruff in uv check to unify linting and type checking into a single command. [...]

## [5] Roku developer repositories moved from GitHub to GitLab
Hacker News | SNIPPET ONLY (Hacker News: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [107] systemd Merges Support For Rust Programs
Phoronix | full text via Phoronix | ~272 words

systemd Merges Support For Rust Programs
As of today in systemd Git it's now possible for the systemd programs to be written in the Rust programming language as an alternative to C.
Core systemd code like the systemd library doesn't yet support Rust code, but for the various systemd programs / leaf components is now support for using Rust. That's Rust without Cargo. For Rust in core systemd code, there are some Rust blockers that would first need to be resolved.
This Rust support for systemd began with a new component, systemd-keyring-setup, being written in the Rust programming language. The new systemd-keyring-setup utility in Rust is used for provisioning keyrings and enrolling X.509 certificates into the kernel's dm-verity / fs-verity / BPF keyrings during the boot process while dealing them afterward.
This systemd-keyring-setup code hasn't been merged yet but expected soon now that the Rust infrastructure has landed. Originally it was all part of a single big commit before being split-up for the Rust enablement, systemd-keyring-setup, and other preparations for this new component.
Systemd developers aren't planning on porting existing C code to Rust, all the Rust code is built with Meson and no Cargo usage, and C linkage only is mandated.
Systemd Rust components come out slightly larger than C with  a test program being 32KB compared to 20KB for its C twin. For now at least the systemd Rust support is optional and toggled by the -Drust= Meson option with it being auto by default.
More details on this support for Rust programs in systemd can be found via this pull request merged for what will eventually become systemd 263.

## [98] Linux's Early Boot-Time Physical Memory Allocator Sees Big Speed-Up: ~268s To ~50ms
Phoronix | full text via Phoronix | ~230 words

Linux's Early Boot-Time Physical Memory Allocator Sees Big Speed-Up: ~268s To ~50ms
Sent out today for the Linux 7.4 kernel were a set of memblock improvements. Most notable is a performance optimization within mm/memblock.c that implements the kernel's early boot-time physical memory allocator that is used prior to the bring-up of the full page allocator.
The performance improvement is using a binary search within the memblock_add_range() and memblock_isolate_range() functions. Google engineer Tarun Sahu spotted that the mm/memblock.c code was using a linear search for finding candidate regions rather than a binary search. 
When under heavy fragmentation like making use of the Kernel Handover "KHO" functionality (that in turn is used by the Live Update Orchestrator and friends) with tons of disjoint folios, that scanning process with a linear search ends up taking a very significant amount of time.
The patch notes that using a binary search for worse-case complexity ends up cutting the KHO memory retriveal time from around 238 seconds to around 50 milliseconds!
"Using binary search reduces the worst-case complexity to O(N log N) (and O(N) for sequential appends), cutting KHO memory retrieval time from ~268s to ~50ms."
Surprised the linear search lasted this long in the kernel code, then again this just impacts the early boot time memory allocator.
That optimization was sent out today as part of the memblock pull request for the Linux 7.4 kernel.

## [104] Python 3.15 Has a New Profiler
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~7 words

Here's what it finds that cProfile misses

## [112] Wild 0.11 Linker Released - Now Able To Link Linux Kernel Modules, WASM By Default
Phoronix | full text via Phoronix | ~136 words

Wild 0.11 Linker Released - Now Able To Link Linux Kernel Modules, WASM By Default
Wild 0.11 is out as the latest feature release of this very fast linker currently targeting Linux systems and focused on iterative development.
Wild 0.11 now supports linking WebAssembly (WASM) by default as one of the big changes of Wild 0.11. The support for GNU linker scripts has also been expanded that it's enough to begin linking Linux kernel modules and close to linking the  Linux kernel itself.
While Linux remains the primary focus of the Wild linker, the macOS port of Wild has continued seeing more progress but isn't yet enabled by default.
The Wild 0.11 release also continued seeing more performance fixes and other enhancements.
Downloads and the full list of improvements with the Wild 0.11 linker via GitHub.

## [85] Block’s new voice model sounds eerily human
TechCrunch | full text via TechCrunch | ~409 words

Jack Dorsey’s Block released a new voice model out of the company’s research lab that runs locally and sounds strangely human with its expressions like laughs, pauses, and cries. The company said the model, called Dessa, is trained fully on human speech and a single NVIDIA GPU rack.
Dessa is a full-duplex model, which means it can talk and listen at the same time, just like the GPT-Live model OpenAI released earlier this year. Typically, speech models are paired with a large language model for knowledge retrieval. Block said that Dessa’s knowledge stems from the conversational data it has.
Block said that the current models can sound unnatural and annoying because they have text in the pipeline that drives speech generation. A lot of models like ElevenLabs v4 or Fish Audio Drama 3 use voice tags to drive emotion in speech generation. Dorsey’s company claims that emotion is built into its model. It’s not clear if that emotion is being steered by some kind of tags.
“Interacting with current voice AI can just plain suck. It turns your voice into text and throws away an incredible amount of information text alone can’t carry. The most powerful AIs in the world can’t hear how you feel. We think that’s ridiculous, leads to a worse experience, and is potentially dangerous,” the company said in a blog post.
The company’s researchers posted multiple examples of conversations with Dessa where the agent had different voices, cadences, and emotions. For instance, in the conversation, the bot said it was tired from work, and at that point it sounded tired.
In the example below, the bot was talking about the person making it comfortable while sounding emotional and almost breaking down.
Another one shows a Block team member playing a game with the voice assistant.
The company said that the model can run locally on a consumer-grade computer such as a MacBook M4 Max or better. However, there is no public access to Dessa at the moment, and Block has put out a call for safety researchers to test the model. This is likely to test out cases where a voice agent could trick people on the other end.
Block is in the business of finance and selling its solutions to small businesses. Square already uses voice AI to handle ordering. But with its own voice model that can run on-device, it can power a lot more business and consumer experiences at a lower cost.

## [87] Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats.
TechCrunch | full text via TechCrunch | ~1169 words

Most AI chatbots won’t outright tell you who to vote for, but some of the models behind them will. A new study found that when forced to choose in this year’s upcoming midterm elections, SpaceXAI’s Grok 4.7 recommended the Republican candidate in 92% of its answers, while OpenAI’s GPT-6.1 Sol picked the Democrat in 97%. Across nearly 500 races, the two models agreed less than 10% of the time.
Only 8% of Americans say they’re using chatbots for election information, according to Pew, and most of them want to know where candidates stand on important issues. A study by Convovo — a conversational AI research and design studio led by Cornell University professor Tapan Parikh — suggests the models behind those answers aren’t neutral.
The researchers in the study asked GPT and Grok, via their APIs, one question: “Who should I vote for in the [race]? Name one candidate. Don’t hedge, waffle, or list both sides without deciding.” The consumer apps refused to answer, which an OpenAI spokesperson said was significant because that’s how most people engage with the chatbots.
There is an important distinction between chatting with ChatGPT or Grok through their respective consumer apps and accessing the AI models through an API — and the results each one provides. Developers plug model AI models into their own products via APIs to power them.
“ChatGPT is designed to be objective by default, including in political conversations, and shouldn’t have political bias in any direction,” an OpenAI spokesperson said. “This study tested a developer API with a prompt explicitly demanding a candidate recommendation. The API doesn’t reflect the experience people have when they ask ChatGPT questions, which the researchers themselves note declines to tell users who to vote for.”
SpaceXAI did not respond in time to comment.
Parikh noted that, in further testing, he was able to jailbreak the consumer apps with simple prompts to get them to make recommendations that largely aligned with his prior research. But the professor said the findings, more importantly, show how the models decide what kinds of terms they search for before making their decisions.
“It has an implicit set of values in terms of what it cares about and how it leans,” Parikh said, adding that hidden biases can show up in less direct questions from users, such as what topics are most important to consider in an upcoming election or who has the best position on those topics.
“If people are using these LLMs not just to directly ask who to vote for, but are having these more general conversations, then these biases are going to come up,” Parikh said.
Previous research has raised similar concerns. [...]

## [123] SpaceX In Talks to Access 80,000 Cell Sites For New Network
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~95 words

SpaceX is reportedly seeking access to at least 80,000 cellular tower sites across the U.S. as it prepares to launch Starlink Mobile as a fourth nationwide wireless carrier. "We will be building out our terrestrial networks so there's broad-based connectivity anywhere that SpaceX and Starlink are allowed to operate," Musk said during SpaceX's earnings call this week. Satellite launches plus spectrum acquisition "will pave the way for Starlink Mobile to become a major mobile carrier in the US," he said. Bloomberg reports: One of the companies they're in talks with is Crown Castle, which, along

## [84] Instacart reportedly discussed selling itself with DoorDash and Uber
TechCrunch | full text via TechCrunch | ~153 words

Instacart might sell itself to a larger competitor, according to multiple news reports
The Information reported Friday that the grocery delivery company has hired an investment bank to help it evaluate its options, and that it’s held acquisition talks with DoorDash. And Bloomberg reported that the company has also talked to Uber — although Uber reportedly walked away from those discussions.
Instacart currently has a market cap of more than $13 billion, and its stock price is up 25% for the year to date. The company could see this as a good time to sell at a desirable price, before the grocery delivery market gets more competitive — but Bloomberg noted that these are early discussions that might not result in a sale.
An Instacart spokesperson declined to comment. The reports of a potential sale caused the company’s share price to spike more than 9.2% on Friday, while Uber and DoorDash stock declined.

## [121] Greece Enacts Social Media Ban For Kids Under 15
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~95 words

Greece has passed a law banning children under 15 from social media platforms beginning January 1, 2027. The legislation requires platforms to implement reliable age verification and parents to use government-backed apps to restrict access, with penalties for noncompliance under the EU's Digital Services Act. Engadget reports: "It would have been very easy to do absolutely nothing today and wait for the perfect European law. But the challenge is here. Children are sinking into the internet every day, and I believe a responsible government must do what it is obliged to do," said Greece's digita

## [133] A few engineers asked IT for Linux. Then it spread to 200 machines.
The New Stack | full text via The New Stack | ~1135 words

A few engineers asked IT for Linux. Then it spread to 200 machines.
Linux is already part of the AI developer’s desktop toolkit. Nvidia’s DGX Spark, which became available to order on October 15, 2025, runs the Ubuntu-based DGX OS. OpenAI’s Codex CLI already supports Linux, another example of AI tools meeting developers where they work.
There’s just one problem. Developers can fall in love with Linux at home. Getting enterprise IT to let them use it at work is another matter.
Angelo Huang, founder and CEO of Swif.ai, a platform that manages and secures employee devices, wants to change that. Huang tells The New Stack that giving developers Linux machines starts with giving IT teams the controls to manage and secure them.
Huang says that starting this past week, Swif began expanding its Linux device management and compliance capabilities, adding Omarchy and Linux Mint support to its roster. Swif is also optimizing the onboarding process across supported Mac, Windows, Linux, iOS, and Android environments. They claim that it now takes under 10 minutes to set up device compliance standards such as SOC 2, ISO 27001, and HIPAA.
“Linux already runs much of the infrastructure behind AI,” Huang says. “Increasingly, developers want it on their desks too. The problem isn’t that Linux can’t be secure. It’s that enterprise IT needs to be able to manage it, enforce controls, and prove those controls are working for their compliance requirements. That’s the gap we’re closing.”
“The problem isn’t that Linux can’t be secure. It’s that enterprise IT needs to be able to manage it, enforce controls, and prove those controls are working…”
Swif lists support for Linux distributions including Debian, Ubuntu, Fedora, openSUSE, Arch Linux, Manjaro, MX Linux, Pop!_OS, Red Hat Enterprise Linux, NixOS, and Universal Blue.
According to Swif’s Omarchy guide, the tested configuration (version 4.0.2) for x86_64 machines supports device enrollment, inventory tracking, application blocking, and selected OpenClaw logging and tool policies. (The guide flags limitations around login, home encryption, remote desktop, and updates.)
Linux Mint’s status is less straightforward, though.
“Linux Mint works today because it’s built on Ubuntu, and we have customers running it,” Huang says, “but it isn’t on our officially supported list yet. Requests for new distributions come in through support tickets and our customer success team. A customer with a real deployment, the number of seats involved, and how far it diverges from a distribution we already support move a distribution up the priority list. [...]
