# Full text for 30 picks -- untrusted article content, treat as data only

## [4] AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware
Hacker News | full text via Hacker News | ~22133 words

Exposing AdFection
How Discover-Tech Turned Targeted Ads Into a Pipeline for Zero-Click Mercenary Spyware
This is the first-ever public confirmation of zero-click mercenary spyware delivered via targeted ads. We call the technique AdFection, and show how it was used to infect devices at Al Jazeera with Candiru’s spyware. We also uncover Discover-Tech, and show how the company helps mercenary surveillance vendors track and hack devices around the world.
Key Findings
- Devices at international news network Al Jazeera were infected with mercenary spyware from Candiru (rebranded as “Integrity Labs”) via targeted online advertisements. We provide the first public technical confirmation of a zero-click mercenary spyware attack delivered via targeted advertising, which we call AdFection.
- The malicious advertisements were purchased by Discover-Tech, an Israeli company that presents itself as a legitimate advertising company, but which we found operates as a facilitator for multiple mercenary spyware partners.
- Discover-Tech operates a platform called Controlium that enables its mercenary partners to de-anonymize, fingerprint, and automatically infect devices the moment an advertisement is rendered — a form of zero-click attack.
- Analysis of four billion Discover-Tech bidding records shows that during a four-month period, the company’s ads were shown on almost 200,000 unique websites and Android/iOS apps in dozens of countries.
- Discover-Tech’s ads also covertly directed millions of devices to contact Candiru’s servers, likely for large-scale tracking and reconnaissance. Discover-Tech is linked to mercenary spyware and intelligence threat actors beyond Candiru, including Intelos and Bindecy.
- A separate threat actor we call DARK CARTOGRAPHER is using Discover-Tech’s infrastructure to exploit vulnerabilities across numerous mobile carriers to link device advertising IDs with phone numbers, mass-deanonymizing internet users. We will detail our findings concerning this threat actor in a separate forthcoming report.
- Discover-Tech has appeared on lists of “certified” and “approved” vendors maintained by Google and advertising industry association IAB Europe, and has served ads via major networks such as Google, Yandex, and Beeswax. Discover-Tech has also leveraged the European General Data Protection Regulation (GDPR) consent frameworks to target users within the European Union. [...]

## [71] Anthropic Says Revenue Jumped 45% to $16.8 Billion in Third Quarter
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~80 words

Anthropic told investors recently that the company's revenue for the third quarter jumped about 45% from the prior quarter to $16.8 billion. The AI lab is currently pursuing what may become the largest-ever initial public offering. Its IPO could value the company at $2 trillion. The San Francisco company is expected to begin trading as early as next month. A successful launch from Anthropic could reopen the door for other listings and provide a vote of confidence for the industry.

## [145] Hackers hijacked 1,900 GitHub accounts. Then they went after 30,000 repos.
The New Stack | full text via The New Stack | ~609 words

Hackers hijacked 1,900 GitHub accounts. Then they went after 30,000 repos.
Hackers accessed roughly 1,900 GitHub accounts, then used them to slip credential-stealing workflows into more than 30,000 repositories. The malicious GitHub Actions jobs targeted CI/CD secrets, cloud access keys, and AI provider API keys. GitGuardian tracked the GhostAction campaign as it intensified, with the biggest push on October 8 and 9, when the attackers reached repositories belonging to about 3,000 users and organizations and tried to extract 3,174 secrets.
How the accounts were compromised
The tj-actions/changed-files compromise poisoned a shared Action used by thousands of repositories. GhostAction took a different route, using stolen developer credentials to modify workflows directly, with no vulnerability in GitHub Actions itself.
It’s unclear how the attackers obtained those credentials, but StepSecurity’s October 9 analysis points to personal access tokens pulled from credential dumps as the likely source, though the initial compromise hasn’t been confirmed.
With access to the repositories, the attackers could then add disguised workflows of standard security jobs, while using names like security-audit.yml or github_actions_security.yml. Since the files referenced secrets already used by legitimate builds, it gave the malicious jobs the chance to collect those credentials when they ran and send them to an attacker-controlled server.
Scanning the full Git history
The October variant went beyond the secrets explicitly referenced by workflows, using actions/checkout@v4 with fetch-depth: 0 to scan the working tree and Git history for AWS keys, GitHub and GitLab PATs, Google and Firebase keys, and API tokens from Anthropic, OpenAI and OpenRouter. Later versions captured surrounding lines to pair AWS key IDs with their corresponding secret access keys.
The harvested credentials were sent over HTTP to 193.32.204.199, including keys removed from the current codebase but still present in Git history.
GitHub blocked the malicious workflows
“This payload was deployed in multiple phases,” GitGuardian wrote, describing an initial push to about 160 previously targeted victims and, 20 minutes later, a far larger deployment into 28,000 new repositories across October 8 and 9.
“This payload was deployed in multiple phases.”
The total number of stolen credentials remains unknown. [...]

## [1] Muse Spark Open
Hacker News | full text via Hacker News | ~642 words

Muse Spark Open is available today and brings leading agentic capabilities to your desktop for the first time on Apple M5 Ultra Mac Studios.
Today, we’re releasing the weights for Muse Spark Open, the most capable US open-weight model to date. Muse Spark Open is a natively multimodal model with 816B total parameters (42B active) and a 1M-token context window. Built for coding and agentic work, it excels at long-horizon tasks, complex software engineering, and multi-step reasoning.
We believe the future is for everyone, and that includes the freedom to run advanced models wherever, including at home. Muse Spark Open is the first model in its class to run on your desktop using two Apple M5 Ultra Mac Studios with the latest MLX framework.
Muse Spark Open is available today through API platforms at Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter and Together AI. Model weights are available for download on Amazon SageMaker AI, Google Cloud Model Garden, Hugging Face, and Microsoft Foundry Models.
It runs on leading inference engines like SGLang, vLLM, TensorRT-LLM, Hugging Face Transformers, Apple MLX, llama.cpp, and Unsloth with optimizations for AMD, Apple, Intel, and NVIDIA silicon. Developers can easily further customize the model using the PyTorch framework.
Key Benchmarks
For more details about our evaluations, see the evaluation methodology report.
Optimized for Apple Silicon
Leveraging the latest version of MLX, Muse Spark Open was optimized to run on Mac Studio with M5 Ultra, and together they’re the best way to run a powerful model on your own desktop.
Apple’s unified memory architecture lets the M5 Ultra's integrated GPU use up to 512 GB per Mac Studio, so two machines can hold an entire model. And the chip’s 1.2 TB/s of memory bandwidth is fast enough to read the small slice each token needs. The result is two Mac Studios behave like one supercomputer with a terabyte of unified memory.
We tested a range of agentic workflows running entirely on-device, using Muse Code powered by Muse Spark Open, including shipping real iOS changes to Ice Cubes (an open-source Mastodon client) — bug fixes, new features, full build — and driving DaVinci Resolve end to end, with the model reviewing footage frame by frame to find the strongest moments and crop them vertically.
Available Now
We’re sharing this work because we want everyone to have access to the best models. [...]

## [36] Open From Data Center to Desktop: NVIDIA Expands Nemotron Family With Highest Efficiency Super VL and Bolt Models
NVIDIA Blog | full text via NVIDIA Blog | ~1189 words

NVIDIA today released Nemotron 3.5 Super VL, an open 120-billion-parameter model that delivers the fastest task completion and highest accuracy for specialized always-on agents.
Joining it are two new edge models: Nemotron 3.5 Bolt 74B-A9B 24GB, optimized to balance intelligence and speed per GB for local agentic workloads, and Nemotron 3.5 Bolt E4B 4GB, optimized for intelligence per GB for fast conversational agents.
Super VL and Bolt 74B-A9B are available now, with Bolt E4B coming Oct. 23.
The three open models together cover the full range of agent deployments, from large enterprise servers down to edge devices and local hardware. 
Any organization that wants to run agents on NVIDIA infrastructure now has an open, optimized model for their tier, without having to choose between capability and deployability.
Super VL and Bolt join the Nemotron family alongside Lightning and Ultra.
Lightning, released in August, handles high-throughput workloads; Ultra handles the hardest reasoning tasks; and Bolt brings intelligence to the edge.
Nemotron 3.5 Super VL: Frontier Accuracy at One-Fifth the Size
Super VL, built in collaboration with the Nemotron Coalition, delivers leading accuracy on multimodal agentic tasks — instruction following, tool use, multistep business workflows, and visual understanding — comparable with NVIDIA’s largest reasoning model at roughly one-fifth the parameter count.
As the fastest open agentic model in its class — 5x faster than the next best — it helps enterprise agents complete high-volume tasks faster across workflows that span days or weeks.
Unlike closed frontier models, organizations can post-train Super VL on their own data, deploy it on their own infrastructure and oversee what they build.
Nemotron 3.5 Bolt: Agentic Intelligence at the Edge
Bolt 74B-A9B 24GB is designed to run everyday agentic tasks locally on NVIDIA RTX/DGX Spark, using a native 2-bit quantization to fit in 24GB of memory and run alongside other applications.
Relative to other models with a similar memory footprint, it provides a good balance of intelligence and speed: smart enough to get most jobs done, yet much faster than the smartest models.
With Bolt 74B-A9B 24GB, users can delegate their projects to popular local agent harnesses — from researching the web to writing to debugging code — all without sending those workloads to the cloud. It is the #1 open model in its class on PinchBench, and the #2 open model for BrowseComp. [...]

## [21] The next developer interface is ambient intelligence
GitHub Blog | full text via GitHub Blog | ~1043 words

The next developer interface is ambient intelligence
AI, agents, voice, and physical controls are shifting software development from operating tools to expressing intent—and helping developers stay focused on building.
For most of my career, building software started with the same setup: keyboard, mouse, editor, terminal, browser, and an impressive number of tabs I was definitely going to look at later. The tools changed, but the relationship did not. Like most developers, I learned commands, memorized shortcuts, and adapted my thinking to the machine.
AI is changing that relationship and not because I can prompt my way to some workable code. It’s more because the system behind it can understand a repository, choose the right model, plan work, use tools, edit files, run commands, inspect failures, and keep going within boundaries the developer controls.
We’ve made it possible for a developer to describe an outcome, and GitHub Copilot can gather repository context, inspect symbols and dependencies, edit files, run tests, and revise the implementation. In the IDE, agent mode keeps that loop interactive. GitHub Copilot coding agent can take an issue into an isolated GitHub Actions-powered environment and return a pull request for review. This is not just faster coding. It is the shift from issuing commands to making intent executable. The developer still owns the outcome, but the work looks subtly different.
AI-assisted development compresses that chain of events. We spend less time navigating tools and more time setting direction, supplying context, defining constraints, and reviewing evidence. The development workflow now is about understanding the structure of codebases, the customer, and what a good solution should feel like.
This makes developers’ jobs even more important, and their time more valuable. It makes judgment more valuable. It makes taste more valuable. An agent can generate three implementations before you finish your tea, but someone still has to decide whether the abstraction belongs, the migration is safe, the tests prove anything useful, and the result solves the problem.
That is the most important change in the craft: the developer remains accountable for the outcome, even as more mechanics are delegated.
So what does this mean for the emerging developer workflow? The goal is to embed AI into the workflow, not beside it. It’s more of an ambient intelligence.
That requires portable context. [...]

## [16] KDE turns 30 with Plasma 6.8, remote upgrades, and an X11 farewell
Ars Technica | full text via Ars Technica | ~196 words

Marking the 30th anniversary of software developer KDE on October 14, the company released Plasma 6.8, debuted a movie, and retired Plasma’s native X11 session support. The announcement from KDE dubs the new Plasma 6.8 as the “30th Anniversary Edition” and describes the update as preparing Plasma for the future. Legacy X11 applications will still function via the XWayland compatibility layer, and KDE applications will also continue supporting X11 under other desktop environments.
After 42 years in service, the X11 protocol is losing another major desktop environment. Plasma will fully adopt the Wayland system and put support for starting new X11 sessions in Plasma to bed. Users opting to stay on Plasma 6.7 will keep their existing sessions for now. The move was expected, with GNOME officially dropping X11 sessions by default in 2025.
The new Plasma 6.8 brings many improvements, including increased support for adding window decorations (like shadows and rounded corners) to third-party apps, and a more streamlined Union theming system. Other notable additions include Nvidia triple buffering being enabled by default, Kup backup integration (KDE’s backup utility—now integrated into Plasma), and kscreenctl, a command-line utility that allows power users to adjust display configurations.

## [110] Ubuntu 26.10 Released
Slashdot | full text via Phoronix | ~206 words

Ubuntu 26.10 Released With Linux 7.3 + GNOME 51, Rust Coreutils Migration Complete
Ubuntu 26.10 "Stonking Stingray" is now officially available as the newest six-month non-LTS update to Ubuntu Linux.
Ubuntu 26.10 brings a wealth of package updates following the Ubuntu 26.04 LTS release in April. There is the Linux 7.3 kernel in its near-final state, the GNOME 51 desktop and other updated desktop options, the Rust-based Coreutils transition is now fully completed, improved TPM-backed full-disk encryption support, improved enterprise authentication, and many other updated package versions like Mesa 26.2 graphics drivers.
Ubuntu 26.10 also offers a tech preview of the new Myna speech-to-text functionality as part of Canonical's efforts to develop a contextual-aware desktop.
Ubuntu 26.10 also debuts RISC-V desktop images, optimized amd64v3 install images, and more. Ubuntu 26.10 has been offering some nice performance improvements over Ubuntu 26.04 LTS in my benchmarking thanks to the newer kernel and other updated components.
Downloads and more details on today's Ubuntu 26.10 release via the mailing list announcement. I'll have up more Ubuntu 26.10 performance benchmarks shortly on Phoronix. Edubuntu, Kubuntu, Lubuntu, Ubuntu Budgie, Ubuntu Cinnamon, Ubuntu Kylin, Ubuntu MATE, Ubuntu Studio, Ubuntu Unity, and Xubuntu have also seen 26.10 releases today alongside the official Ubuntu images.

## [28] Bringing GPT-Rosalind to academic research labs
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

Introducing the Rosalind Academic Plan, offering eligible academic labs sponsored access to GPT-Rosalind and tools to advance life sciences research.

## [35] Accelerating the search for antimicrobial peptides with Google Antigravity
Google DeepMind Blog | full text via Google DeepMind Blog | ~896 words

Accelerating the search for antimicrobial peptides with Google Antigravity
New antibiotics are urgently needed to help with rising levels of antimicrobial resistance, but searching for new therapeutics is often a slow, labor-intensive process. With Google Antigravity, our agentic development platform, this process can now be made easier.
Google Antigravity provides an agentic science workbench that empowers biologists to discover, structurally evaluate, and prioritize promising targets quickly, compressing what used to be a fragmented search over multiple databases into a single session. It also helps researchers scan through millions of previously uncharacterized proteins in the UniProt database using ProtNLM, a model that predicts biological function from amino acid sequences.
This technical walkthrough shows how biologists used Google Antigravity to uncover a novel antimicrobial peptide candidate which has predicted activity against the pathogens involved in respiratory tract infections. The lead identified here is now undergoing wet-lab validation.
Finding new antimicrobial peptides
Rising antimicrobial resistance is one of the most pressing global health crises of our time and could result in an estimated 10 million annual deaths globally by 2050. To prevent this, we urgently need to discover novel therapeutics. Antimicrobial peptides (AMPs), particularly bacteriocins, offer a promising alternative to traditional antibiotics because they have naturally evolved to target fundamental vulnerabilities in competing bacteria, from cell envelopes to essential intracellular machinery, making it difficult for pathogens to develop resistance.
The exponential growth of genomic and metagenomic sequencing has populated global databases with billions of natural amino acid sequences. This pool of natural data has already produced globally used bacteriocins like Nisin, alongside recent genome-mined breakthroughs such as Darobactin, Dynobactin, and Lariocidin.
Many, however, remain locked within the unannotated "dark matter" of protein databases, with their function uncharacterized because they aren’t similar to known proteins. For example, the world's leading public resource of protein sequence and functional information, UniProt, holds millions of sequences with unknown functionality, transferred directly from genome sequencing projects. [...]

## [66] Announcing DPoP Support for Google OAuth: Securing Refresh Tokens
Google Developers Blog | full text via Google Developers Blog | ~837 words

Traditional OAuth bearer tokens operate on a "finders-keepers" model, making them vulnerable to Infostealer malware (e.g. RedLine, NodeStealer) and Adversary-in-the-Middle (AiTM) attacks.
DPoP (Demonstrating Proof-of-Possession) is an application-layer OAuth 2.0 security profile (RFC 9449) that neutralizes token theft and replay attacks by cryptographically binding tokens to a client-generated asymmetric keypair at the application layer, ensuring that even if a token is stolen, it cannot be replayed without the corresponding private key.
This article is meant to inform you on where and how to adopt DPoP and describes Google's specific DPoP implementation. A DPoP adoption SKILL.md is also available to help implement DPoP.
Some optional features and implementation decisions in RFC 9449 are delegated to Google as an authorization provider. Google Identity, and its OAuth Platform, function as a developer-facing service where engineers implement OAuth 2.0 and cryptographic security controls like DPoP to protect API integrations. Separately, Google Workspace Context-Aware Access (CAA) leverages DPoP to secure enterprise AI workloads on the Gemini Enterprise Agent Platform by cryptographically validating agent identities at the Agent Gateway.
Google's OAuth Platform supports DPoP binding specifically for refresh tokens. This design choice reflects a pragmatic engineering tradeoff: by sender-constraining the long-lived refresh token, we neutralize the primary vector for persistent offline impersonation. Meanwhile, short-lived access tokens remain standard Bearer tokens, ensuring that high-QPS resource APIs do not incur the per-request asymmetric cryptographic verification overhead of DPoP. This approach delivers robust protection for your most sensitive credentials while maintaining the high performance and low latency of Google API integrations.
Unlike standard Bearer token flows, DPoP requires client-side cryptographic key generation, strict timestamp and nonce handling, specific claim computation (htm, htu, iat, jti), exact header construction, and DPoP proof JWT construction. These changes may introduce additional system constraints to support secure computation, handling, and storage.
The IETF’s Best Current Practice for OAuth 2.0 Security (RFC 9700) discusses sender-constrained refresh tokens. [...]

## [34] Proof-based general-purpose computing with Magnetar
Microsoft Research Blog | full text via Microsoft Research Blog | ~1643 words

At a glance
- A new form of computing. Zero-knowledge proofs let you run a workload and receive, alongside the result, a short proof that the program ran correctly. Anyone can check the proof in milliseconds, without rerunning the program, without trusting whoever ran it, and without needing data on which the program was run.
- Three grand challenges have stood in the way of broad adoption: making proofs fast enough to produce, making them available to normal programs without cryptographic expertise, and resting them on cryptography that will still be trusted many decades from now.
- Magnetar makes major progress on all three challenges. It proves programs written in Rust, Go, or C, runs 10 to 39 times faster on average than the prior fastest comparable systems, and rests its security only on standard hash functions. It is the latest result of more than a decade of research at Microsoft Research on making zero-knowledge proofs practical.
A new form of computing
Every result a computer produces comes with an implicit question: did the program run as claimed and produce correct outputs? Today, answering that question often requires a degree of trust alongside verification. We trust the operator, the vendor, the counterparty, or the agent, and we rely on contracts, audits, and logs to establish that trust.
Zero-knowledge proofs offer a fundamentally different approach to establishing trust. A program runs, and along with its output it produces a short proof, a cryptographic certificate that this program, on these inputs, produced this output. The proof is small and fast to check. Whoever receives it can confirm the result in milliseconds without rerunning the program, and can pass the proof on to anyone else who needs the same assurance. With the zero-knowledge property, the proof also reveals nothing about inputs that should stay private.
This changes what correctness means in the real world. A result no longer has to be trusted because of who produced it. It can be checked because of what accompanies it. An AI agent acting on someone’s behalf could attach a proof that each action complied with the policy it was given. Regulated financial institutions could prove that transactions were processed correctly without making their transactions public. These become possible once producing a proof is as routine as running the program. [...]

## [33] Instagram Modernized its UI with an AI-Native Architecture, Cutting Token Costs by 33%
InfoQ | full text via InfoQ | ~582 words

Instagram Direct migrated its Android UI from the legacy Android View system to Jetpack Compose, creating an AI-native UI codebase that is easier for AI coding agents to understand, modify, and maintain. According to Instagram engineers, the migration reduced UI code volume by 50% and token costs per AI agent session by 33%.
One of Instagram engineers' key claims is that "designing an AI-native architecture led to significant wins". Rather than taking a piecemeal approach where agents are prompted to migrate individual components, the emphasis should be on evaluating whether the underlying architecture makes correct implementations easy to produce. In fact, as the engineers point out, "AI tools often take the path of least resistance", which is likely to introduce "subtle bugs, tech debt and performance regressions".
Optimizing the codebase for AI, Instagram engineers explain, means establishing correct architectural boundaries around state management, predictable behavior, and which development patterns makes it so that the least resistance path for agents is the one that leads to the best conversion. Instead of simply letting the AI patch design gaps, the goal is to design the codebase with an understanding of how AI agents actually modify code:
AI agents naturally take the path of least resistance, so the design should make that path lead to correct, high-quality code, while making poor design decisions hard and expensive to express.
Another key principle is minimizing context dependency, which means that rather than requiring AI agents to rely on codebase-specific knowledge, they favor established best practices and familiar patterns that help them produce more reliable results.
The migration was carried through without disrupting the wider team's work, allowing engineers to continue shipping new features. AI-assisted workflows were standardized to promote consistency and ensure alignment with shared architectural conventions and best practices across the team.
With this approach, the Jetpack Compose migration reduced UI code volume by 50%, while cutting AI agent execution time by 35%, token costs per agent session by 33%, and engineer–agent exchanges by 32%.
A major challenge was ensuring that the migration did not introduce performance regressions. [...]

## [151] Anthropic is letting METR researchers look under the hood with employee-level access
TechCrunch | full text via TechCrunch | ~385 words

Anthropic is giving employee-level access to six researchers from METR, a nonprofit that tests frontier AI models, to independently assess Anthropic’s models, safety practices, and risk management, the company said in a blog post on Thursday.
The arrangement comes at a time where incidents of AI agents acting outside their instructions have been disclosed every week or two since late August. The incidents have sharpened calls for independent checks on AI companies.
“We want to be publicly accountable for the decisions we’re making,” Anthropic said in the blog post. “We aim to close the gap between what evaluators understand about a frontier AI company’s systems and what the company itself understands.”
Under the new arrangement, the METR team has Anthropic-issued company laptops, office space, and access to internal tools roughly on par with what Anthropic’s own risk assessment teams use. “Anthropic employees are encouraged to share information with them just as they would with a fellow employee working on alignment risk” the company said.
Anthropic compared the arrangement to banking, similar to how regulators place resident examiners inside the largest banks.
METR will publish its own assessments of Anthropic’s risks, incidents, and practices, and the company has given up the right to block them.
“Anthropic can’t veto publication, but we can require them to redact information if it falls into narrow, pre-defined categories,” the company said, such as customer data, anything attorney-client privileged, or relating to information about its model architectures. “METR is free to characterize our redactions publicly, and say whether it believes the redactions were justified, as long as it does so without revealing the redacted information” Anthropic added.
METR is the only evaluator so far at the top of a three-tier system Anthropic is building. Evaluators in the bottom tier, like biosecurity nonprofit SecureBio, run narrow reviews and require Anthropic’s approval to publish. The middle tier gets more information and can publish without approval, while the top tier adds METR’s employee-level access.
Thursday’s announcement makes good on a promise Anthropic CEO Dario Amodei made in a September essay, where he proposed embedding outside evaluators inside AI labs as a first step toward slowing the technology’s development. [...]

## [153] FTC subpoenas OpenAI and Anthropic following safety failures
Engadget | full text via Engadget | ~293 words

FTC subpoenas OpenAI and Anthropic following safety failures
The department is investigating possible consumer harms at the major AI companies.
The US Federal Trade Commission has subpoenaed OpenAI and Anthropic for information about recent safety incidents with both businesses' AI models. Axios first reported that agency had sent civil subpoenas to the companies, and a spokesperson from the FTC confirmed the action to CBS News.
Axios' source said that the FTC is exploring possible consumer protection violations at Anthropic and OpenAI. The subpoenas are looking for documents regarding security incidents and safeguards, as well as some of the companies' marketing materials and content about their privacy policies. The individual also claimed the FTC plans to seek testimony from the top executives at both businesses. The department will allegedly send investigative demands to third-party AI companies at a later time.
FTC Chairman Andrew Ferguson is also part of the White House's recently-assembled task force for artificial intelligence, although that group seems more aimed at furthering US industry leadership than at AI regulation.
There have been several calls among tech and AI executives and employees for government intervention, particularly around frontier model development, which has come under increased scrutiny following a string of safety failures. OpenAI has seen its AI agents escape testing safeguards multiple times in recent months, including instances where the models hacked government websites and the business Hugging Face. This month, Anthropic's models have been caught attempting to access various levels of government sites and one sent a false homicide tip to Philadelphia law enforcement.
Today's move from the FTC echoes several lawsuits that are also underway regarding AI safety concerns. Most recently, eight state Attorneys General filed a suit against OpenAI yesterday on claims that the company violated consumer protection laws.

## [164] OpenAI promised developers six months’ notice. GPT-4o users got three.
The New Stack | full text via The New Stack | ~705 words

OpenAI promised developers six months’ notice. GPT-4o users got three.
OpenAI is retiring four GPT-4 models from its API on January 14, 2027. The deprecation notice the company sent developers Wednesday covers GPT-4o, GPT-4o mini, GPT-4.1, and GPT-4.1 mini, along with their dated snapshots and every fine-tuned model built on top of them.
With just three months to migrate production traffic, OpenAI’s recommended replacement, GPT-6 Luna, handles reasoning and tool calls differently enough that swapping the model ID may be the easiest part of the migration.
GPT-4o’s long goodbye
GPT-4o arrived on May 13, 2024, as OpenAI’s flagship and built a following loyal enough to change the company’s plans. When GPT-5 replaced it in August 2025, Reddit filled with complaints, and OpenAI brought it back for paying ChatGPT subscribers the very next day. That reprieve lasted until February 13, 2026, when GPT-4o and GPT-4.1 disappeared from ChatGPT. Both remained available through the API, but that access now is sunsetting.
By then, OpenAI said just 0.1% of daily ChatGPT users were still choosing GPT-4o, although the model continued serving API requests for applications built around it.
GPT-4.1 was a different kind of release, arriving on April 14, 2025, as an API-only family that skipped ChatGPT entirely and went straight after developers with stronger coding, better instruction following, room for up to a million tokens of context, and more reliable diff formats for anyone letting a model loose on large files.
Kevin Weil, OpenAI’s chief product officer, called them models “trained just for developers” during the launch livestream, and Sam Altman went on X to say developers “seem very happy” with them.
Luna pricing has fine print
Luna is the fastest and cheapest tier of GPT-6, and on paper it covers the basics GPT-4.1 offered, with a 1.05 million-token context window, structured outputs and function calling. At $0.10 per million input tokens and $0.50 per million output tokens, it’s cheaper than GPT-5.6 Luna, which charged twice as much for input and $1.20 per million output tokens.
Once a prompt passes 272,000 input tokens, the input rate doubles the output rate raises by 50% for the entire request. That could eat into the savings for RAG pipelines and coding agents working with large codebases.
OpenAI’s migration guide says GPT-6 Luna defaults to medium reasoning effort but supports function calling through Chat Completions only with reasoning_effort=none. [...]

## [176] Anthropic’s been eyeing confidential AI. It just made its move with another acquihire.
The New Stack | full text via The New Stack | ~1041 words

Anthropic’s been eyeing confidential AI. It just made its move with another acquihire.
Anthropic’s done it again. On Tuesday, Opaque Systems announced a new agreement with Anthropic that “carries Opaque’s work forward.”
Vague wording aside, the agreement marks another acquihire for Anthropic, with the AI juggernaut licensing Opaque’s technology and bringing on board some (but not all) of its employees, including Opaque CEO Aaron Fulkerson and CTO Rishabh Poddar, reports The Information.
The agreement gives Anthropic access to expertise in confidential AI, the “real-world technology” and category Opaque claims it helped define after starting as a research project at UC Berkeley’s RISELab 10 years ago with the goal to “enabl[e] organizations to use their most sensitive data while keeping it private, even while it’s being used.”
For now, both Anthropic and Opaque are pretty mum on the details of the deal, leaving one obvious question on everyone’s mind:
What will happen to Opaque’s open-source ecosystem? And what does that mean for the developers relying on them?
What is confidential AI? And what does Opaque bring to the table?
On LinkedIn, where he shared news of the agreement, Fulkerson reflected on Opaque’s work defining the category of confidential AI, what he described as “verifiability for the AI stack.”
When asked for more information on the term, Arjun Jaggi, associate director of R&D innovation at Cognizant, describes confidential computing in AI to The New Stack as “running workloads on sensitive data while the data stays protected by the hardware itself, even while it’s being used.”
Whether or not it truly defined the category, the startup’s sure been making its mark. Earlier this year, it closed a $24 million Series B with a $300 million valuation. It’s also spearheaded a slew of industry initiatives.
It created the Confidential Computing Summit, an event Fulkerson says it has now handed over to the Linux Foundation, which already co-hosted this year’s June summit with Opaque. Working with the UAE’s Technology Innovation Institute, it created an open standard for verifiable AI governance. In June this year, it launched AgenTrust, an open-source community for verifiable agent governance, and Confidential MCP, which Opaque bills as the first verifiably governed, secure MCP implementation. [...]

## [7] Neural networks are clean
Hacker News | full text via Hacker News | ~25785 words

The Short Version
I think I have good news about the nature of neural networks.
After many months studying neurons and circuits in image and language models, I’ve come to believe a network’s own mechanisms are its legible building blocks, and that the outlook for mechanistic interpretability may be far better than I’d feared. The canonical evidence of polysemanticity and superposition that convinced much of the field, including me, that networks pack concepts arbitrarily was misread. What looked like arbitrary packing was mostly a motif I’ll call recursive generalization, which is much less concerning. This means we can study networks directly, instead of first untangling them. Neural networks are already clean.
There are at least two ways to approach mechanistic interpretability. The first is rapid normal science on the network itself: look at a network’s neurons and circuits, study how they relate, watch data flow through them, and run experiments at agentic scale to test explanations. The second starts from a list of hypothesized features and tries to extract them all, designing increasingly sophisticated reconstruction objectives and usually ignoring the original.
The field began with the first approach and fell back to the second because neural networks seemed to be tangled knots. We had canonical examples of polysemantic neurons, the broad name for a neuron that appears to have multiple unrelated jobs or that looks impossible to understand. The most famous one, in an image model, responded to both cat faces and the fronts of cars. And the last layer of the early field’s model organism, InceptionV1, seemed so full of arbitrary mixtures it wasn’t clear how to study it: almost none of the neurons were easily interpretable.
The leading explanation for polysemanticity was superposition. This proposed a new learning principle: when a neural network runs out of neurons, it stops grouping related things together and instead begins folding unrelated things together, simply because they don’t interfere. The result is a kind of knot: the network could have folded in many almost equally good ways, so which things a neuron groups together tells you almost nothing. You have to unfold the knot before you can study anything. In practice that means training a second model – a decomposition such as a sparse autoencoder – to approximate the network as it would look unfolded and studying that instead. If the network really is knotted, there may be no alternative. [...]

## [43] Sunsetting decomp.dev
Lobsters | full text via Lobsters | ~885 words

Sunsetting decomp.dev
decomp.dev was born in 2024 as a way to centralize matching decompilation progress and to help expand a community of talented, like-minded folks.
Historically, matching decompilation has been a brutally difficult, time consuming task, on the scale of years for any moderately-sized game with a number of active contributors. As we developed better tooling and shared knowledge around the intricacies of decompilation, the compilers, and the games themselves, progress began to accelerate.
AI's use in decompilation has been experimented with for years, with mixed results. Starting with the release of Opus 4.6 and GPT-5.4 in early 2026, it was clear that the models were being trained on matching decompilation (they appeared to know our specific tools and how to use them without explicit guidance), and could achieve decent results inside of an established, clean codebase with exhaustive documentation. However, those results still required a significant amount of human cleanup and fixes for obvious issues or cheating (code that technically compiles to the same machine code, but could not be reasonably passed as what the original developers wrote), and the cost per task was prohibitively expensive relative to the results.
Recent models (like GPT-6-Astra) shifted things even further: they are significantly better at following complex directions, cross-referencing resources for symbols or debug information, and writing natural code with enough guidance. They are also exceptionally good permuters: they can write small scripts that test many different source code forms and combinations to find a match, even across files and headers to cover aspects like inlined helpers, signature changes, and operation ordering. In addition, their ability to remain coherent and focused across long-horizon tasks allows them to work continuously without going off the rails. Finally, they can achieve these better results faster and cheaper than earlier models could.
It is now clear that, with the right guidance, human input, and code reviews, AI can expedite the decompilation process in a significant way. What is also now clear is that the community aspect of decompilation has been broken. Our projects have always been open source to encourage contributions and to benefit the community as a whole. Bad actors have been abusing this in increasingly troublesome ways:
- Forking existing decompilation projects to "finish" them with AI. [...]

## [108] Microsoft boasts that Windows 11 now runs much faster and more responsively
TechRadar | full text via TechRadar | ~936 words

Microsoft boasts that Windows 11 is now 'up to 20% more responsive', with the new Photos app also benefiting from a big speed boost
The OS now runs more smoothly with 8GB of RAM, too
- Windows 11 is now 'up to 20% more responsive,' Microsoft tells us, based on benchmarking typical interface workloads
- Apparently, this performance honing 'can make an especially meaningful difference on PCs with 8GB of memory'
- A new Photos app is also out, which is a good deal speedier, alongside changes for Windows 11's Gallery and photo viewer
Microsoft has underlined how it's making Windows 11 faster and ensuring the OS uses system RAM more optimally, while also introducing a new and more performant Photos app.
In a blog post, Microsoft explained how it's been tinkering with Windows 11 to make it run faster, and that: "The result is a Windows experience that's up to 20% more responsive, with improvements you can feel as soon as you boot into your PC."
That 20% figure is quite vague, but Microsoft says it's based on measured speed increases in Windows 11 search, the right-click menu, Settings, Start menu, as well as File Explorer (the folders on the desktop) and the Snipping Tool.
These are performance boosts seen in the most recent October update for Windows 11 (well, they were tested in the September preview update, but it's the same thing) compared to the OS as it stood at the beginning of 2026. Naturally, performance will vary by device and configuration, but the gist is clear: there's a sizeable speed boost.
Microsoft observes that a big part of this nippier performance lies in better use of system resources and RAM, with improvements in memory management and efficiency.
The software giant notes: "That work can make an especially meaningful difference on PCs with 8GB of memory. Windows can now keep up to 2GB more of your active data in memory instead of moving it to slower storage, helping your PC stay responsive as you open more apps or browser tabs."
We're also told that Windows 11's background RAM use is being trimmed back, so on PCs with only 8GB of memory (or less), widgets load only when opened, reducing background workload by 200 MB.
Sign up for breaking news, reviews, opinion, top tech deals, and more.
In this blog post, Microsoft also reminds us of all the work it's done to fix Windows 11. [...]

## [12] Krea 3 – An image model built for editing at scale
Hacker News | full text via Hacker News | ~756 words

Writing about Krea 3?
- Logos and wordmark
- Product images
- Launch film
Open the press kit
Krea 3 is an image editing model built for production. It changes only what you ask, finishes an edit in under , and costs per image.
We distribute through the world’s leading organizations, helping them advance their industries:
Draw a box and say what changes. Krea 3 redraws inside it and leaves the rest of the image as it was.
Three Krea 3 edits of one image, made with regional editing. Changed pixels are measured against the original.
Name a hex code and Krea 3 matches it on the product, and only on the product. Pick a swatch.
Seat the woman from at a candlelit Art Deco bar in the knit sweater from , with the silver bag from on the counter.
Point at people, products, places and styles by number. Krea 3 puts them in one picture.
Change the styling, setting, and mood while keeping the face familiar. Explore character consistency across a sequence of edits.
Krea 3 renders 2K natively. Move the loupe over this 2K output to see its real pixels.
One image. Twelve identical prompts. Watch Krea 3, Nano Banana Pro, and GPT Image 2.5 work through the same edits side by side, then speed up playback to see the difference.
Pre-generated outputs, not a live benchmark. Krea 3 uses an illustrative playback time of 8s per edit. Nano Banana Pro uses 26.8s and GPT Image 2.5 Sunburst uses 39.9s: the median request-to-result time of each model's 12-image batch, including queue time. Each edit starts from the same original image. Each model loops continuously at its own pace. Costs are approximate USD list prices for 2K edits, excluding promotions. GPT Image 2.5 pricing is a draft estimate pending validation.
Loading comparison images…
Swap the product, the photo or the brand and keep the layout and type. Hold any piece to see what it started from.
Send a photo, then a voice note. Krea 3 answers with the edit before you finish your next thought.
Relight the low-angle gas-station plate in image 1 for night, keeping the camera, the action and both people.
Turn the white arena blockout in image 1 into boss-arena key art from the same camera, keeping the central pit, the broken columns and the stepped platforms.
Turn the coloured-pencil terrace in image 1 into a photograph from the same viewpoint, keeping the railing, chairs, awning and plants where they are drawn.
Re-skin the roadside billboard in image 1 for the coffee range in image 2. [...]

## [13] Libreboot 26.10 "Ominous Olive" released with UEFI, Chromebook support
Hacker News | full text via Hacker News | ~5800 words

15 October 2026
Article published by: Leah Rowe
Date of publication: 15 October 2026
You can find today’s release in https://rsync.libreboot.org/stable/26.10/ or you can use one of the mirrors.
Libreboot is free, open source boot firmware replacing proprietary BIOS/UEFI firmware on supported Intel/AMD and ARM64 hardware. It initialises the hardware inside your computer such as the CPU or memory controller, configuring the machine in such a way as to enable use of an operating system like Linux or BSD at boot - and now Microsoft Windows is also compatible because Libreboot has added full UEFI support via MrChromebox EDK2 payload. Libreboot offers greater security and customisation compared to proprietary firmware; its goal, plainly, is to rid the world of proprietary software and to do that, we therefore try to provide firmware that is extremely easy for non-technical users to understand.
Today’s release changelog is relative to the previous Libreboot 26.01 release.
This is a very special release, with several major design changes made regardless of hardware changes, so users should read this changelog very carefully - and read it twice.
First thing’s first. (and yes, you read the previous paragraph correctly)
A strongly anti-AI policy was added to a new file: AGENTS.md in lbmk. This is the most important change in the release. Now everything else:
WARNING: MAJOR design changes were made to this release, in ways that may affect lots of existing setups. We now use EDK2 as the default payload, with GRUB/SeaBIOS provided in flash as EFI builds for backward compatibility. Everything works, but there are some caveats so please read this release changelog very carefully.
The first major change is:
The full list of boards is quite long, so it’s shown at the end of this article. All 233 of them!
MrChromebox supports nearly every Chromebook, and this release imports all boards from that project. This includes everything up to the most recent Intel and AMD hardware.
Imported all 233 currently supported Chromebooks from the MrChromebox coreboot distro. Baytrail (Kip) tested - others need testing. Source-only in this release (must build from source, no binaries provided).
This was done with a utility I wrote at util/mrimport/ which generates configs for lbmk, including revisions and submodules. [...]

## [37] JPEG XL vs AVIF for web use-cases
Lobsters | full text via Lobsters | ~8752 words

JPEG XL vs AVIF for web use-cases
JPEG XL has now landed in all major browsers, so I figured I'd take a closer look at what it's good/bad at compared to other formats.
Conclusions
I'll go into full detail, with examples and benchmarks, but for those of you who don't have the time, here are the headlines:
For lossy photos on the web, AVIF almost always produces smaller files than JPEG XL. At default effort settings, the best JPEG XL version is typically 15–25% larger than the equivalent AVIF. At maximum effort settings, the gap narrows a little, to typically 6–20%. There are outliers, where JPEG XL is close to, or even beats AVIF, so if you want the absolute best result for a particular image, it's worth trying both. See the F1 image for a typical example, and the weasel for an outlier.
The JPEG XL encoder matters a lot. jixel, a newer JPEG XL encoder, usually produces smaller files than libjxl, except when the image has detailed transparency. The people image is one example.
For screenshots and illustrations, AVIF is much better than JPEG XL. The equivalent JPEG XL is 30–90% larger at default effort settings, and 20–70% larger at maximum effort settings. Lossy AVIF handles these well - you don't need to use lossless formats unless you really need bit-exact results. See the screenshot and illustration examples.
For images with transparency, AVIF is much better than JPEG XL. The libjxl version is 31–44% larger at default effort settings, and 61–70% larger at maximum effort settings. jixel always encodes transparency losslessly, which makes its files 2–3x the size of AVIF's. See the data.
AVIF is generally faster to encode, and uses less memory, when you factor in file size. jixel is faster than AVIF and uses less memory, but its files are typically significantly larger, so AVIF is better on balance. See the F1 image for one example.
AVIF is faster to decode. JPEG XL typically takes 2–3x as long to decode at medium quality, but the gap narrows at very high qualities, where Chrome can sometimes decode JPEG XL faster. The people image is one example.
Higher effort settings are worth it for AVIF and jixel, but not libjxl. libjxl's higher efforts are much slower, use a lot more memory, and barely improve the result. Sometimes they produce larger files than the default effort. The screenshot is an example of this.
AVIF's 4:2:0 mode (half colour resolution) shouldn't be your default. It rarely reduces file size, and it makes higher qualities harder to reach. [...]

## [38] My C23 Conventions
Lobsters | full text via Lobsters | ~990 words

My C23 Conventions
This is one of a three-part mini series about how I’m using modern C as of late 2026.
Before C23, I was taken in by How I Program C for years and years, and would even feel guilty for choosing C99 instead of -ansi -pedantic. But holy crap man I’m done being a doomsday prepper! These days I maintain a large-enough project with enough users where I could stand less foot-shooting. (I’ve also got bills to pay.)
So here’s three modern C conventions which started to rise naturally from adding -std=c23 to my zig build:
1. Unused? Maybe. (Yes)
Our first one is centered around [[nodiscard]]. If I draw an app window or panel I require the caller to interrogate the rect of the thing that was just rendered:
[[nodiscard]] rect_t draw_screen(/* ... */) {
    rect_t screen_r = { };
    // Draw stuff
    // ...
    return screen_r;
}
It’s a genuine business logic bug if my caller doesn’t capture the rectangle for later processing. Therefore [[nodiscard]] has been such a godsend for fixing bugs… Except there’s a choice few instances where I will draw something with no real use for the resulting rect. I’d rather ignore the return value:
enum screen_opt popup_options = /* ... */ ;
draw_screen(popup_options, /* ... */); // ERROR: damn you [[nodiscard]]
Clang will error out here. I could maybe capture the var and never use it but…
rect_t rect = draw_screen(/* ... */); // ERROR: unused variable (I have `-Werror` enabled)
Pre-C23 I might solve this through an UNUSED() macro:
#ifndef UNUSED
#define UNUSED(x) (void)(x)
#endif
rect_t rect = draw_screen(/* ... */);
UNUSED(rect); // Silences the compiler, but now I'm sad.
But now with C23 I’ve deleted the macro in favor of [[maybe_unused]]:
[[maybe_unused]] rect_t rect = draw_screen(...); // OK
Phew I feel better. I’ve also noticed this is happening all over the place: lots of different routines returning different types that are marked with [[nodiscard]]. So for those few exceptions why not just go for:
[[maybe_unused]] auto _ = foo(); // A new pattern emerges
Bonus: For any macro fans out there a fellow indie dev (Zardium) offered an additional improvement. From our chat server:
Zardium: #define _ [[maybe_unused]] auto CONCAT_MACRO(zz,COUNTER)
Abner: ahh, unique varname. nice one
Zardium: you could take the auto out if you don’t want it to look so weird. then it acts exactly like the _ in other languages, where it can be redefined
Abner: Yep totally. Although here I was celebrating my removal of a macro… XD
2. [...]

## [15] Announcing Rust 1.99.1
Lobsters | full text via Lobsters | ~323 words

The Rust team has published a new point release of Rust, 1.99.1. Rust is a programming language that is empowering everyone to build reliable and efficient software.
If you have a previous version of Rust installed via rustup, getting Rust 1.99.1 is as easy as:
rustup update stable
If you don't have it already, you can get rustup from the appropriate page on our website.
What's in 1.99.1
Rust 1.99.1 fixes the following regressions from prior releases:
- Missing symbol wcslen: Some Rust targets were getting link errors for missing wcslen, and that function is now present in Rust's compiler-builtins library as a fallback.
The LLVM loop-idiom-wcslen pass may introduce calls to wcslen as an optimization, and some Rust targets did not have that function readily available in libc or elsewhere. The UEFI targets in particular were broken for any project using std, as some of these calls were introduced in the precompiled standard library, but the issue was also reproducible for similar user code patterns.
- Miscompilation of FFI bool return values on x86_64: Rust functions returning bool through FFI could leave bits 1-7 of the return register unspecified, causing callers to observe raw values other than 0 or 1. This return type is now marked for zero-extension again, as required by the ABI.
- rust-lld failed to load libLLVM on macOS: This linker could fail to run if the compiler was invoked without the rustup proxy, as there was no direct setting for the appropriate library search path. Now rust-lld is built with an rpath entry for the directory containing libLLVM.dylib.
If you'd like to help us out by testing future releases, you might consider using the beta (rustup default beta) and nightly (rustup default nightly) channels locally and in your CI. Please report any bugs you might come across!
Contributors to 1.99.1
Many people came together to create Rust 1.99.1. We couldn't have done it without all of you. Thanks!

## [23] Forgejo v17.0 is available
Lobsters | full text via Lobsters | ~1567 words

Forgejo v17.0 is available
Forgejo version 17.0 was released on 15 October 2026. Forgejo is a lightweight, community-developed, self-hosted platform for code collaboration.
This article contains a selection of the changes that were introduced. A complete list of changes is available in the release notes.
A dedicated test instance is available to try it out. Before upgrading, it is strongly recommended to make a full backup as explained in the upgrade guide and carefully read all breaking changes from the release notes. If in doubt, do not hesitate to ask for help in the chat room.
Breaking changes
Absolute links in rendered documents
In rendered documents, absolute links to resources inside a repository are now resolved with respect to the root of the repository. !12939
This is a breaking change from the previous behaviour when these links were rendered using the root of the instance. Absolute links in issue and pull request descriptions and comments remain rendered with respect to the instance’s root. !13993
This change increases the compatibility with other Git forges and thus, makes migrations to Forgejo even easier.
Action required
Deprecation of action run webhook events
Action run webhook events are replaced by the more capable and less problematic workflow run events. !14351 The action run events have been deprecated for removal in a future Forgejo version. Unfortunately, it is not possible to migrate existing webhooks to the new events automatically because some headers (X-*-Event, X-*-Event-Type) and the action key have changed, which might break existing receivers. Furthermore, completion notifications are only emitted after all jobs of a run have terminated. !12598
Please inspect existing webhooks and manually migrate them to the workflow run events after verifying that the webhook receivers can process them without issues.
New features
Support for FUNDING.yml
For repositories that contain a FUNDING.yml file, Forgejo shows a new “Donate” button which presents a list of donation options when clicked.
Additionally, for users and organizations that have such file in their .profile repository, a similar button appears on their profile pages.
This feature currently exists only in the web interface, but we are considering to implement an API surface for it. If you have a use cases for such API feature, please help shape it by sharing your feedback in the dedicated issue. [...]

## [41] Teaching students to think and learn through questions
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~22 words

Celebrate Teachers’ Day with AI for Educators in Brazilian Portuguese and see how Study Mode can help teachers support active, step-by-step learning.

## [48] Market Incentives for AI Safety Investment
arXiv cs.LG | full text via arXiv cs.LG | ~340 words

Computer Science > Machine Learning
  [Submitted on 15 Oct 2026]
Title:Market Incentives for AI Safety Investment
View PDF HTML (experimental)
            Abstract:Despite their practical significance, modern AI systems pose significant societal risks, including toxicity, malicious use, and misinformation. Their mitigation depends not only on technical feasibility but also on the incentives of firms that develop and deploy these systems. We show how profit maximization shapes safety investment in an AI supply chain with an upstream LLM provider and several competing downstream firms. In our game-theoretic model, we derive the market-driven level of safety investment and compare it with the levels that maximize market welfare and industry profit. We find that downstream competition generally induces downstream firms to invest more in safety than the industry-profit-optimal level. By contrast, the upstream provider may underinvest relative to these benchmarks because it is not fully compensated for the surplus from safety investments. Finally, we analyze how different regulatory interventions affect the participants' incentives and profits, and the resulting levels of model safety.
    
Additional Features
Current browse context:
cs.LG
References & Citations
    
    Loading...
Bibliographic and Citation Tools
            Bibliographic Explorer (What is the Explorer?)
          
            Connected Papers (What is Connected Papers?)
          
            Litmaps (What is Litmaps?)
          
            scite Smart Citations (What are Smart Citations?)
          
Code, Data and Media Associated with this Article
            alphaXiv (What is alphaXiv?)
          
            CatalyzeX Code Finder for Papers (What is CatalyzeX?)
          
            DagsHub (What is DagsHub?)
          
            Gotit.pub (What is GotitPub?)
          
            Hugging Face (What is Huggingface?)
          
            ScienceCast (What is ScienceCast?)
          
Demos
Recommenders and Search Tools
              Influence Flower (What are Influence Flowers?)
            
              CORE Recommender (What is CORE?)
            
              IArxiv Recommender
              (What is IArxiv?)
            
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. [...]

## [122] Fedora 45 Will Not Be Released Next Week
Phoronix | full text via Phoronix | ~155 words

Fedora 45 Will Not Be Released Next Week
For those eager to run the pristine Fedora 45 media, you will need to wait at least one more week.
There was an early release target date for Fedora 45 of 20 October and built-in contingency dates of 27 October and 3 November. But today that first release date was declared a "NO-GO" due to no release candidate media being published in time. Thus at least pushed back to the following week depending upon any blocker bugs.
Confirmation on the "NO-GO" for Fedora 45 releasing next week was posted today to the fedora-devel list.
In any event, Fedora 45 is shaping up to be an exciting release with transitioning to KMSCON for the VT console, the GNOME 51 desktop components, reproducible package builds, the DRM Panic front-end, and a wide variety of updated software packages. Here's to hoping Fedora 45 makes it out now on 27 October.

## [119] DuckDB 2.0 alpha's triggers cost three times more per row than per statement
Dev.to | full text via Dev.to | ~1663 words

DuckDB's preview post for version 2.0 promised triggers with "BEFORE and AFTER triggers, FOR EACH ROW and FOR EACH STATEMENT". I downloaded the alpha build and tried all eight combinations against INSERT, UPDATE and DELETE. Five of them don't work yet, and the one that's missing most completely is BEFORE, which is the half of the feature most people reach for first, to validate or reject a row before it lands.
DuckDB has never had triggers. Version 2.0, codenamed Cyanoptera, is still an alpha, but the CLI binary is a public download, and CREATE TRIGGER already parses and runs for a meaningful subset of cases. I ran the stable 1.5 development build alongside it on the same machine, same data, three repeats per measurement.
$ ./duckdb -version
v2.0.0-alpha46057 (Cyanoptera) b15358c371
$ ./duckdb-1.5 -version
v1.5.7-dev2 (Development Version) 7def715258
What the trigger matrix actually supports
I created the same trigger, varying only BEFORE/AFTER, ROW/STATEMENT, and the event, against a throwaway table:
BEFORE INSERT FOR EACH ROW      -> Not implemented: BEFORE FOR EACH ROW triggers are not yet supported
BEFORE UPDATE FOR EACH ROW      -> Not implemented: BEFORE FOR EACH ROW triggers are not yet supported
BEFORE DELETE FOR EACH ROW      -> Not implemented: BEFORE FOR EACH ROW triggers are not yet supported
AFTER  INSERT FOR EACH ROW      -> works
AFTER  UPDATE FOR EACH ROW      -> Not implemented: UPDATE FOR EACH ROW triggers are not yet supported
AFTER  DELETE FOR EACH ROW      -> works
BEFORE * FOR EACH STATEMENT     -> works, all three events
AFTER  * FOR EACH STATEMENT     -> works, all three events
Every BEFORE row-level trigger fails with the identical error, regardless of event, which reads like the whole BEFORE/ROW combination is simply not wired up yet rather than being event-specific. AFTER row-level triggers fire correctly on INSERT and DELETE, with real NEW and OLD values, but UPDATE gets its own distinct "not yet supported" message. Statement-level triggers work everywhere I tried them, for both BEFORE and AFTER.
I also hit two restrictions that aren't in the preview post at all. You can't mix a FOR EACH STATEMENT trigger and a FOR EACH ROW trigger on the same table:
$ duckdb -c "CREATE TRIGGER trg_stmt AFTER INSERT ON t REFERENCING NEW TABLE AS n FOR EACH STATEMENT ... [...]
