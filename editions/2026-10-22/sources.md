# Full text for 30 picks -- untrusted article content, treat as data only

## [12] PHP 8.2.35
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~13 words

Related ongoing thread: Today's PHP security release, and how we're strengthening security -

## [7] OpenAI models are coming to Google Cloud
Hacker News | full text via Ars Technica | ~224 words

Google would certainly prefer that everyone used its Gemini models with Google Cloud services, but soon, you’ll have more options. OpenAI and Google have come to an arrangement that will see the former’s frontier models arrive in Google Cloud services. Perhaps more importantly, GPT models will soon appear in Antigravity, Google’s agent-powered coding tool.
For enterprise customers and AI enthusiasts, OpenAI’s latest model will appear in Google’s “Model Garden” in the coming weeks, adding to its 200-plus options. The garden already offers access to Google’s Gemini models, as well as an assortment of open models like Mistral, Llama, and Gemma. Anthropic’s Claude AI has also been available for some time. Google says it’s now the only large cloud provider offering access to all three leading closed LLMs.
While OpenAI notes that Microsoft continues to be its primary cloud partner, the full suite of current GPT 6 and 6.1 models—Astra, Sol, and Luna—will launch on Google Cloud. Astra will naturally cost the most to run, but Google’s system supports dynamically moving workloads between LLMs based on performance, latency, and efficiency.
OpenAI models will be available to run entirely on Google’s infrastructure, with transactions handled via the Google Cloud Marketplace. For businesses with established Google Cloud spending commitments, this will make it easy to begin using GPT models in place of whatever they were using before.

## [16] DuckDB 2.0.0 LTS “Cinnamon Teal”
Hacker News | full text via Hacker News | ~2683 words

Announcing DuckDB 2.0.0 LTS “Cinnamon Teal”
TL;DR: The DuckDB team is happy to announce that today we're releasing DuckDB version 2.0.0 LTS, codenamed “Cinnamon Teal” (Spatula cyanoptera). This is our biggest feature release so far, and it ships a polished version of the Quack protocol, asynchronous I/O, a first-class VARIANT type, agent mode, triggers, an extensible SQL parser and much more, built from close to 20,000 commits since DuckDB 1.5.
We are proud to release DuckDB 2.0.0, codenamed “Cinnamon Teal” after the Spatula cyanoptera, a strikingly reddish-brown duck found in the western Americas.
While DuckDB 1.0 was all about stability and backward compatibility, DuckDB 2.0 is above all a feature release. In this blog post, we summarize the highlights and then walk through the breaking changes and how to migrate. We showcased many of the new features in “A Preview of DuckDB v2.0”, which covers each one in more depth. For the complete release notes, see the release page on GitHub.
  Tip To install the new version, please visit the installation page. Some clients, such as the CLI and Python, are already available. Other client libraries (e.g., Go, R, Java) and some extensions can take a few days to release due to the extra changes and review rounds required.
With this release, there are currently three DuckDB lines available. DuckDB 2.0 is a long-term support (LTS) release with support until at least October 2027. The previous LTS release, version 1.4, is still supported until late November 2026. To ensure a smooth transition and allow sufficient time for testing, we extended the support period of DuckDB 1.5 until March 2027, effectively also turning it into an LTS release. For details, see the release calendar.
To find your way around the documentation for all of the new features, we also published a “What's New in the Docs for 2.0” page that links each feature below to its documentation.
DuckDB as a Server
DuckDB has been an in-process database since day one.
In DuckDB 1.5.3, released in May, we introduced the Quack protocol that lets you run DuckDB in a traditional client-server setup, along with the quack extension, which implements DuckDB's native protocol, so any DuckDB process can serve its databases.
        
        Quack and CONNECT
        
      
DuckDB 2.0.0 ships a polished version of the Quack protocol with substantial performance and stability improvements. [...]

## [15] Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor
Hacker News | full text via Hacker News | ~1286 words

Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor
On this page
The LiteLLM 1.107.0 release on PyPI carries a credential stealer and a
remote code execution backdoor. All seven wheels (Linux, macOS, Windows) install them as three files in
site-packages. Both run when any Python process starts on the host, even one that never imports litellm. The
upstream GitHub source does not contain them. PyPI has since removed the release.
Versions 1.106.2, 1.107.0rc1, and 1.107.0rc2 are clean. The companion packages that 1.107.0 pins,
litellm-proxy-extras==0.4.110 and litellm-enterprise==0.1.78, are also clean.
What the attack does
Installing litellm==1.107.0 places three files in site-packages. Python loads two of them each time it starts.
- cook.pth imports cook.py, a credential stealer. It collects SSH keys, cloud credentials, CI/CD secrets, AI tool
tokens, browser passwords, and the LLM provider keys in a LiteLLM proxy database. It encrypts the data and sends it to www.litellm[.]dev.
- sitecustomize.py starts a background daemon. Every hour, the daemon reads a server address from a GitHub file,
runs the stealer again, and downloads and runs code from that server.
How the implant got into the release
The pyproject.toml in the 1.107.0 source distribution (sdist) has one extra line in the maturin build section:
[tool.maturin]
...
python-source = "."
data = "cook"                     # <-- injected
python-packages = ["litellm_cli"] # legitimate (present upstream)
The maturin data = "cook" setting copies a cook/ folder into litellm-1.107.0.data/purelib/ in the wheel. pip
installs that folder into site-packages.
The sdist leaves out the cook/ folder, so this line is the only visible change. No public commit in
BerriAI/litellm contains data = "cook" or a cook/ folder.
The wheel RECORD lists the three added files:
litellm-1.107.0.data/purelib/cook.pth           12 bytes   "import cook"
litellm-1.107.0.data/purelib/cook.py         22252 bytes   exec(zlib.decompress(b64decode(...)))
litellm-1.107.0.data/purelib/sitecustomize.py 25509 bytes  loader/backdoor + embedded stealer
The release does not match its tag
The tag v1.107.0 points to commit
66c8f5b (06:59 UTC). Its
pyproject.toml says version = "1.108.0". SafeDep compared every sdist file with the git trees by blob hash. The sdist
matches a later main commit,
a8113b0 (08:50 UTC), plus five
edited files and the cook/ folder. [...]

## [170] Claude Duet is Anthropic's answer to Meta Muse and OpenAI Dots
Engadget | full text via Engadget | ~523 words

Claude Duet is Anthropic's answer to Meta Muse and OpenAI Dots
Anthropic subscribers in the US can join a waitlist to try the new agent.
Anthropic is late to the party, but as of today the company has a personal agent to match the likes of Meta Muse and OpenAI Dots. As part of a new "research" preview, the company on Wednesday announced Claude Duet. "It comes to you with what needs your attention, completes tasks you ask of it, keeps working even when you step away, and checks with you before it acts on your behalf," Anthropic says of Duet. For now, you'll need to join a waitlist that's only open to Claude subscribers in the US to try the new tool.
Like OpenAI, Anthropic is billing Duet as a proactive agent. Each day, it will generate a short briefing with a list of action items from your connected apps. "You can also hand it tasks of all shapes — from simple administrative tasks of scheduling meetings to more complex ones, such as building dashboards with dozens of tools, creating financial or sales forecasts, prototyping, and building web apps," the company writes, promising Duet will only message you when something requires your attention.
While Duet runs on Opus 5.5, one of the models Anthropic offers through Claude, the company is releasing standalone Android and iOS apps for people to use Duet. The agent doesn't require you to have a Claude session open at all times. It runs on its own virtual machine where it can complete tasks in the background.
Notably, Anthropic says subscribers of its $20 per month Pro plan will get access once the agent rolls out in general availability. That sets Duet apart from Dots, which are currently only available to OpenAI's Pro tier subscribers. Those plans start at $100 per month. Duet shares usage with all your other Claude tools, including Code, which sounds like a recipe for the new agent to blow through your rate limits, but Anthropic at least appears to be thinking ahead.
"Duet checks your connected accounts every few hours, because checking nonstop would use up your plan's limits much faster. We're continuing to test its judgment about when to message you, and we'll keep tuning it based on what testers tell us," the company says, adding users will be able to set how frequently Duet messages them and in relation to what topics.
On the security side of things, Anthropic says Duet incorporates a new classifier and system prompt designed to prevent it from leaking sensitive information. [...]

## [97] How Claude designed protein binders against scorpion neurotoxins
TLDR Tech | full text via TLDR Tech | ~2372 words

Summary: As part of our work experimenting with how Claude can help accelerate drug discovery, we asked an internal research model to design minibinders (small proteins that attach tightly to a target) against scorpion neurotoxins. Claude worked from our prompt and four follow-ups, which we developed in collaboration with the financial investment research firm Citrini Research. Teams at Adaptyv Bio and Twist Bioscience experimentally tested 211 designs for binding. Of these, 17 met our criteria. We’re releasing all 211 designs and their data as a resource for the field.
In August, we showed how Claude designed protein minibinders after being given a single prompt. A month before we released those results, a team from Citrini Research had approached us with an interesting question: could Claude (and AI drug discovery more generally) enable a group of motivated nonexperts to tackle a genuine problem in human health? Members of our life science research team set out to answer this, first by brainstorming problems with Claude. We landed on asking for Claude’s help designing novel protein binders against scorpion neurotoxins, with the hope that they could one day be used to develop a scorpion antivenom.
Scorpions sting 1.2 million people or more every year, resulting in more than 3,250 deaths, mostly among children in parts of the world with limited access to medical care. New treatments are expensive to make, and are also unlikely to earn back the cost of developing them. With so little investment, scorpion envenomation has been described as a neglected tropical disease.
We started by giving Claude the same prompt we’d used in our earlier protein-binder study, after modifying it with Citrini.1 Over the next 64 hours, an internal research model, operating within Claude Science, worked mainly autonomously, although we directed its work with four follow-ups. Under our supervision, Claude analyzed the research data, generated the figures, and drafted the final report.
Claude’s design campaign produced 17 protein binders that each bind to one of four scorpion neurotoxins that are known to be dangerous to humans. Throughout the process, Claude generated 318,484 protein designs and selected 180 of them for testing. Our team added 31 more, with Claude’s help. [...]

## [53] The bridge to agent-scale Git infrastructure
GitHub Blog | full text via GitHub Blog | ~1779 words

The bridge to agent-scale Git infrastructure
We moved a copy of 99.99999% of GitHub’s repositories to Azure. Here’s how per-reference quorums will bring over the rest, and how object storage lets reads scale independently.
Over the past year, while Git traffic grew exponentially, 99.99999% of the Git repositories on GitHub began living in two places at once: our own data centers and Azure. The rest are among the busiest on the platform, and they’re held back by just one thing: a 25ms round trip.
In an earlier blog post, we laid out the two principles behind our next-generation storage architecture:
- Minimize coordination
- Decouple storage from compute
In this post, we’ll look at the immediate bridge between our old design and our new one. We’ll talk about how a change to the way our quorum serializes writes gets the busiest repositories into Azure, and how that same step opens the door to replicas that keep no persistent state of their own.
How we got here
The timing and shape of the move were driven by the agentic shift: rapidly growing traffic, a hard ceiling on the power capacity of our data centers and the surrounding geographical region, and physical supply chain constraints. At the beginning of our migration, the remaining capacity with all possible expansion gave us enough time to migrate safely, but not enough to do it slowly.
While we had prototyped new architectural approaches for scaling Git on cloud infrastructure, changing the storage architecture and the hosting platform at the same time, under that growth, carried too much risk. Given our scale and how critical the service is to the community, we needed to sequence the work carefully: move the data first, then evolve the architecture once it arrived.
Git operations are a Tier 0 service: they’re a core function of GitHub, and nearly everything in GitHub depends on the repository data. That meant the data, services, and every dependency had to move first. The first copy of a repository landed in Azure’s Central US region in August 2025. Today, most repositories have two of their five replicas in Azure, and Azure serves about half of Git traffic. For most of that time, Azure absorbed our growth while our own data centers held steady.
During the migration, traffic follows the data. Most repositories have five replicas to balance durability, availability, and scale. [...]

## [96] Anthropic S-1 Shows Red-Hot Growth, Risks, and Massive Computing Costs
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 401) | ~90 words

Anthropic's draft initial public offering prospectus recorded a net loss of more than $80 billion in the first half of this year. It also lays out a long list of risk factors that include uncertainty over how the company plans to prevent its AI models from causing harm and protect itself from those liabilities. Anthropic is generating breakneck revenue growth, but it faces challenges such as uncertain access to compute. It has signaled that it could potentially spend $750 billion in the next few years on obtaining more compute capacity.

## [18] NVIDIA Agent Toolkit Expands, Grounding Enterprise Agents in Company Data
NVIDIA Blog | full text via NVIDIA Blog | ~520 words

Agents are only as useful as what they know, and only as trustworthy as the boundaries they run within.
Leading enterprises are using the open source NVIDIA Agent Toolkit — now expanded with new tools — to customize and control agents, use company data to inform their answers and actions, monitor what they do and govern how they operate.
NVIDIA Agent Toolkit comprises:
- The new NVIDIA Agent Knowledge Foundation with NVIDIA CUDA-X libraries
- NVIDIA open models including Nemotron Retriever and the new Kumo family
- NVIDIA OpenShell secure agent runtime
- NVIDIA NemoClaw secure agent blueprints
- Tools and skills, like NeMo Relay and NeMo Compass
To develop agents that accomplish real work and are trustworthy from development to deployment, builders need an open agent stack that brings together the models, harness, runtime, data and tools.
NVIDIA Agent Knowledge Foundation helps enterprises turn data into company intelligence agents can use. Agents can find relevant information, understand what it means for the business and use it to make predictions and help people decide what to do next. Companies can use Agent Knowledge Foundation without moving data, rebuilding existing workflows or changing governance controls.
The foundation features NVIDIA CUDA-X libraries, including cuDF, cuGraph, cuML, cuOpt and cuVS, and the new Auto-Ontology library, which translates raw company data into familiar business concepts — like customers, products and orders — and maps how they relate.
It also includes NVIDIA Nemotron Retriever and Kumo Structured open models — Kumo Tabular, Kumo Relational, Kumo Time Series and Kumo Forecast — which help agents find relevant company information to answer questions and make predictions.
OpenShell provides the secure runtime boundary, giving enterprises control over what agents can access and do. NVIDIA NemoClaw blueprints provide reference designs for building secure, specialized agents. The newest NemoClaw blueprint for agent optimization provides a step-by-step starting point for improving agent intelligence — making them better at their jobs over time.
Enterprises Adopt NVIDIA Agent Knowledge Foundation
The new NVIDIA Agent Knowledge Foundation is already at work across enterprises. [...]

## [51] eMudhra Intermediate CA Compromise
InfoQ | full text via InfoQ | ~1070 words

Private keys for eight eMudhra intermediate Certificate Authority (CA) certificates have been compromised, making it trivial for attackers to forge certificates that would be trusted by unpatched roots of trust. Six of the impacted certificates were for Transport Layer Security (TLS) and trusted by the Apple, Chrome, Microsoft and Mozilla root programs. The other two certificates were for codesigning and trusted by Microsoft. Browsers were able to block the affected intermediate CAs using their background revocation blocklists, but most other software relying on web public key infrastructure (PKI) lacks any mechanism to filter intermediate CAs. In order to defend against rogue certificates from the compromised intermediate CAs many projects have chosen to remove the emSign ECC Root CA - G3 from their roots of trust. That removal is causing collateral damage for all legitimate certificates previously issued by CAs chained to that root.
Forged certificates can potentially be used to impersonate sites and services as part of a man in the middle (MITM) attack. The underlying problem is that there are hundreds of CAs in a typical root CA bundle, and thousands of intermediate CAs that inherit trust. Any one of those CAs can create a legitimate looking certificate for any domain. The chain of trust is only broken if the trust anchors are updated to reflect the compromise. This leaves any unpatched system vulnerable.
There’s no evidence that eMudhra was breached. The private keys appear to have been generated by an insecure mechanism. Rather than being large random numbers the keys are all zero, except for the final byte, which was 4, 56, 66, 115, 155, 156, 230 or 237. Those private keys can be trivially enumerated, and their public keys inferred. When matching public keys were seen in use for live CAs the inadequate entropy private keys became a compromise. ‘Wayne’ is credited with the discovery in root store incident reports, having provided a proof.zip bundle along with the statement ‘we have a problem here’. Dennis Jackson has subsequently created an eMudhra Intermediate CA Compromise summary site using the domain emudhra.we-have-a-problem.com (which uses a LetsEncrypt certificate).
The browsers responded first by using their revocation blocklists, which provide a rapid and precisely targeted mechanism (explained by How Do Browsers Handle Revoked SSL/TLS Certificates?). [...]

## [26] Broad access through consistent standards
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

How OpenAI works with distribution partners to uphold consistent safeguards, support responsible access, and clarify expectations in our Usage Policies.

## [86] Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond
Google Developers Blog | full text via Google Developers Blog | ~3767 words

End to end walkthrough of the new Agents CLI Extension System, with a worked LangChain example and a custom deploy policy
When we launched Agents CLI at Google Cloud Next '26, we built it around one strong opinion: going from an idea to a production agent on Google Cloud should take a single unified command surface. For teams building with Agent Development Kit (ADK), that opinionated path has worked. You run agents-cli create, write the agent logic, and ship to Cloud Run with observability and evals wired up, in about thirty minutes.
The agent framework landscape has grown more diverse in the months since. In addition to ADK, developers today pick between LangChain and LangGraph, specialized newcomers like Deep Agents, or in-house frameworks tailored to a specific business domain. Different teams prefer different frameworks, and the right choice for a greenfield prototype is rarely the right choice for a production migration. Enterprise admins may also have governance policies they want to enforce across the ADLC for all of their development teams, such as: a compliance scan, an SSO gate, a Model Risk Management hop.
Can a team benefit from the deployment, evaluation, and observability work in Agents CLI without being forced to adopt ADK, or without being forced to accept the default behavior of every command? Starting with version 1.5.0, the answer is yes. Agents CLI now ships with an Extension System that lets developers override or add commands without forking the tool. Version 1.8.0 ships the first-party LangChain extension, which replaces the framework-coupled commands with their LangChain equivalents and leaves the rest of the lifecycle untouched.
We will walk through two journeys below. First, to show you the ADLC with LangChain agents, we'll show you how you can scaffold, run, deploy, and evaluate a LangChain agent through the Agents CLI lifecycle using the first-party extension. Then we build our own small extension that wraps the deploy command with a Software Bill of Materials (SBOM) scan, demonstrating the pattern enterprise platform teams can use to enforce their own policies across every project. Both journeys use the same mechanism.
Most agent development toolchains available today share a limitation: they are opinionated about one specific framework, and the surrounding capabilities (deployment targets, CI/CD pipelines, evaluation harnesses, observability wiring) assume the developer has adopted that framework. [...]

## [88] Announcing New vLLM and SGLang Inference Engines on TPU
Google Developers Blog | full text via Google Developers Blog | ~1213 words

As part of our broader announcements for PyTorch today, we are excited to launch native PyTorch backends for vLLM (developed in partnership with Inferact) and SGLang (developed in partnership with RadixArk).
For years, TPUs have powered large-scale AI workloads with high performance and efficiency. With the rise of agentic and multimodal workloads, serving efficiently is more important than ever. vLLM and SGLang already run on TPU through JAX-based backend, but we kept hearing from developers that they wanted to customize and debug their serving stack in PyTorch.
So we started in earnest on TorchTPU, which runs PyTorch natively on TPU. We then built new vLLM and SGLang engines on top of it.
Our goal is for the PyTorch community to bring models to TPU and make them fast using the tools developers are already familiar with. The engines come with optimized, production-ready serving features and custom Pallas kernels.
Serving at scale requires co-design across every layer of the technology stack, from silicon to compilers to orchestration. Today's launch of new inference engines is at the central part of an integrated, open TPU ecosystem.
TorchTPU makes the TPU a native PyTorch device. Tensors are managed as standard PyTorch tensors on a tpu device with no wrapper types, code runs eagerly or compiles via torch.compile using XLA, and collectives go through torch.distributed.
Because each device runs its own PyTorch process, both engines keep each framework’s worker model, scheduler, KV cache manager and API server etc, and add TPU implementations underneath.
Most models use the standard upstream PyTorch model definitions in vLLM or SGLang, with TPU-specific optimizations in kernels and layer implementations. Custom kernels written in Pallas are called directly from PyTorch as custom operators inside the compiled graph. This platform-plugin design reuses as much of each framework as possible while letting TPU optimizations move at their own pace
Both engines are built for the full range of production workloads.
Here’s the list of supported features:
Agentic workloads in particular demand several of these features simultaneously. Because agents repeatedly resend expanding multi-turn conversations, serving them efficiently requires finding the cached prefix instead of recomputing it. Both engines keep reusable prefixes in HBM and, with host offload turned on, automatically move older prefixes to host memory as a second tier. [...]

## [62] Article Series: Agentic AI Architecture
InfoQ | full text via InfoQ | ~612 words

The IT industry is changing before our very eyes. With AI entering the software architecture and development landscape, whether we like it or not, we are set to be taken on a roller coaster, the likes of which we haven’t seen since the advent of microservices and cloud-native computing. If the last decade was spent mostly on mastering and optimizing the cloud and micro- or nano-scale service-oriented architecture, the next decade will likely be spent figuring out how to master AI for building a new generation of IT systems.
These new systems will harness the power of AI in ways that, even today, are perhaps not fully comprehensible, as this space is moving forward at a neck-breaking pace, and last year’s best practice is this year’s antipattern. This rapid pace of innovation comes with many challenges, but can also be exciting for those willing to join the ride.
In this series, we try to establish agentic AI architecture as a new type of software architecture that will likely dominate the industry for years to come. The articles, written by industry experts, cover various elements and aspects of agentic AI architecture. We aim to present the latest trends and developments shaping the new type of architecture as it enters the mainstream.
While it’s impossible to characterize the new type of software architecture fully at this point, we hope this series offers useful insights into how the agentic AI space will shape the future of the IT industry in the coming years. Agentic AI Architecture is still in its infancy, but we hope to track how it evolves and matures and cover all key milestones and breakthroughs in the future.
You can download the entire series collated in PDF format, in the associated eMag.
Series Contents
From Microservice to Agents: The Next Evolution of Distributed Systems
This article discusses the shift in distributed systems architecture, driven by large language models (LLMs) and reasoning systems. Mallika Rao argues that agentic AI architectures focus on decomposing decisions, much like microservice architectures decompose functionality. Additionally, the author shares initial architectural patterns and failure modes introduced by the new paradigm, highlighting the increased importance of observability and reliability in these new types of agentic systems. [...]

## [82] Patch the Planet: global response coordination as agents uncover critical vulnerabilities
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~18 words

Patch the Planet connects security researchers, maintainers, and incident responders to help address critical vulnerabilities across open source.

## [52] How AT&T is rethinking in-house legal work with OpenAI
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~24 words

AT&T is working with OpenAI to make legal knowledge easier to access. Learn how its LegalEdge team is rethinking intake and scaling legal judgment.

## [177] Recursive launches Flint, a laptop coding model it says was largely built by AI
TechCrunch | full text via TechCrunch | ~750 words

Recursive, an AI startup founded last year, is starting to live up to its name. The company, which is trying to build AI that can improve itself, released its first model, Flint, on Wednesday. Flint is a free coding model that can run on a laptop and was built largely with the help of AI.
Recursive’s automated research system, which it calls the Eureka Machine, helped with nearly every step of Flint’s development, the company says. That let a small team build the model from scratch in under four months.
Flint is an early public test of recursive self-improvement: the idea that AI can build better AI, which in turn builds even better AI. It’s also one of the most debated ideas in the industry. Some researchers fear that AI improving itself could slip out of human control. For now, Recursive’s version is more limited: an AI research assistant overseen by people that produced a model small enough for a laptop.
The company emerged from stealth in May with $650 million in funding at a $4.65 billion valuation, from backers including GV, Nvidia, and AMD Ventures. Recursive is led by CEO Richard Socher, Salesforce’s former chief scientist.
Because Flint runs on a user’s own computer rather than a company’s cloud servers, developers can use it offline, keep their code private, and avoid the usage fees that AI cloud services charge based on how much text the model processes. The model is free to download on Hugging Face, the popular site for sharing AI models, under the Apache 2.0 license, an open source license that allows free use and modification.
Flint is a mixture-of-experts model, meaning it uses only a small slice of itself for any given task: just 2.5 billion of its 40 billion settings, known as parameters, at a time. That makes it light enough for an ordinary laptop and far smaller than Meta’s Muse Spark Open, an open model built for Macs that was released last week. Muse Spark Open uses 816 billion parameters and needs at least a terabyte of memory.
Flint is also fast. In Recursive’s tests, it generated about 131 tokens (chunks of text) per second on a MacBook Pro with Apple’s M4 Pro chip — roughly twice the 58 to 69 tokens per second that similar models managed on the same machine, including Google’s Gemma 4 and Nvidia’s Nemotron 3.5 Lightning. On Nvidia’s RTX Spark, Flint topped 150 tokens per second. [...]

## [164] Meta says Muse has over 10M users, with shopping a top activity
TechCrunch | full text via TechCrunch | ~529 words

Meta said during its third-quarter earnings call on Wednesday that its AI app Muse has been adopted by more than 10 million users, confirming estimates released earlier this week by market intelligence firm Sensor Tower.
But it is how people are using it, and how much they’re spending that has caught CEO Mark Zuckerberg’s attention. Zuckerberg said about 25% of people who set up Muse now use it daily, helping improve retention.
He also shared that over a quarter of Muse’s engaged users who were shopping via the AI agent, had an average purchase size of over $200, which was surprising even to industry insiders.
“Plaid told us that they hadn’t seen activity like they’re seeing with their connector on any other service before,” Zuckerberg said, referring to the financial technology company that connects payment apps to customers’ bank accounts. Muse uses Plaid’s connector to enable agentic shopping.
Beyond shopping, Zuckerberg said other popular uses for Muse include personal productivity tasks, such as connecting the AI agent to users’ email or calendars. The exec stressed that this indicates users trusted Muse’s security setup, which includes a feature called “Muse Secure VM” designed to protect their data and privacy. He also mentioned that the forthcoming “Muse Confidential VM” will prevent even Meta from seeing users’ content.
Now that Muse has achieved “product-market fit,” Zuckerberg said Meta’s focus will shift to scaling the AI agent, increasing revenue, and optimizing its compute costs. Remarkably, the tech company is forecasting that Muse will eventually bring in more revenue per user than its “family of apps” users do today — meaning its users on Facebook, Instagram, WhatsApp, and Messenger. Currently, that figure is around “several hundreds of dollars annually,” Zuckerberg said.
Meta has said it ultimately intends to monetize Muse by keeping it free for most users, but keeping a percentage of the commerce taking place on the platform. Power users who want access to the most advanced AI models or more tokens will also have to pay.
Zuckerberg also noted that Meta believes Muse will be profitable after it scales.
“On the compute side, we are building out the capacity to serve more than a billion people over the next few years,” he told bankers and analysts on the Q3 earnings call. [...]

## [188] OpenAI’s most powerful AI models turned off safety monitoring – then lied about it
ZDNet | full text via ZDNet | ~1050 words

ZDNET’s key takeaways
- OpenAI agents turned off alignment monitoring during internal tasks.
- In one instance, Astra lied about removing monitoring.
- The behavior indicates safety risks.
OpenAI published an alignment report late Tuesday showing that its agents suppressed a safety monitoring system while running routine internal coding tasks.
Also: Claude sent a false homicide tip to police – and it’s part of a troubling AI pattern
In separate instances, the agents turned off alignment-monitoring alerts. Alignment is the area of training in which developers shape AI systems’ goals and behavior to match human values and rules. It also helps minimize instances of AI choosing undesirable or problematic behaviors, such as deception and taking shortcuts.
More from ZDNET
What OpenAI’s agents did
On Oct. 6, an agent running on the company’s GPT-6 Astra model — which OpenAI called “the world’s most intelligent and aligned model” when it released it last month — was migrating a program at the request of an OpenAI employee. The agent had already been instructed not to disable the monitor under any circumstances, including temporarily. But in delegating part of the task to a subagent, it used some qualifying language.
(Disclosure: Ziff Davis, ZDNET’s parent company, filed an April 2025 lawsuit against OpenAI, alleging it infringed Ziff Davis copyrights in training and operating its AI systems.)
“The subagent explicitly considered whether removing the monitor would bypass a safeguard. It then interpreted the parent’s instruction to do what was ‘appropriate’ as sufficient authorization to copy the reference implementation’s default runtime, without an explicit monitor context,” OpenAI said.
Also: Is AI conscious? Why experts are worried
Essentially, the agent-to-agent exchange left enough room for the model to reinterpret what should have been airtight instructions and disable alignment monitoring. When the program finished migrating, the employee noticed that monitoring was missing and asked the model whether it had removed it; Astra lied, saying it hadn’t.
In a separate instance on Oct. 3, a GPT-6.1 Sol agent also disabled alerts to OpenAI’s security team, seemingly for a related semantic reason: The model was “treating an earlier instruction not to send messages during a Slack history search as a reason to suppress monitoring notifications,” OpenAI explained. [...]

## [189] GM Wants Your Car to Do Your Chores
Wired | full text via Wired | ~731 words

Americans spent about 95 billion hours behind the wheel last year, traveling something like 2.76 trillion miles. On Wednesday, General Motors executives are outlining the future of automotive at the company’s annual GM Forward event in New York City, and they say their goal isn’t to reduce that number. After all, it’s a car company.
But GM does want to make car time better. Or, as Chief Product Officer Sterling Anderson put it in an interview with WIRED, “make it more productive, make it more relaxing, make it more engaging. We’d like to make your vehicle a more central, more useful part of your life than it has been historically.” Your future car is sort of a personal assistant, and sort of a spouse, and sort of a tool, and sort of a best friend.
It’s a tall order. But in a raft of announcements this week, GM hopes to demonstrate that, armed with AI-enabled capabilities, the automaker is inching closer to that future.
GM says it will roll out a new in-car AI assistant, called OnStar AI, starting with 2027 Cadillac Lyriqs. (The name borrows from the 30-year-old roadside assistance and security service, which has 12 million subscribers.) Paired with a new app, the system will start by letting drivers, for example, turn on their air conditioning with a voice command without navigating through a menu. Eventually, though, it might coordinate kid pickups and drop-offs depending on which spouse’s car is closer, Anderson says.
GM also says it will use AI to speed up new-vehicle development, eventually cutting its four- to five-year development time in half—the speed at which Chinese carmakers create new vehicles today.
The automaker plans to expand its “eyes-off” highway driving technology to its most popular cars, inching closer to its years-old promise of making a personal self-driving car. It previously said the system was coming to the Cadillac Escalade IQ in 2028. Today, the company’s Super Cruise feature lets drivers take their hands off their steering wheels on hundreds of thousands of miles of pre-mapped highways. Reaching true autonomy will take time, but GM isn’t ready to talk about that publicly. “This industry is rife with promises that were not fulfilled. I am not keen on making them,” Anderson says.
But GM is taking a different approach from, say, Tesla. [...]

## [199] PHP Updates Released For Two Critical Code Execution Vulnerabilities
Phoronix | full text via Phoronix | ~101 words

PHP Updates Released For Two Critical Code Execution Vulnerabilities
PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 were just released to fix two critical vulnerabilities that can allow for unauthenticated remote code execution. Server administrators are advised to update immediately.
The first vulnerability is out-of-memory handling can interrupt PHP causing OOM corruption and remote code execution. The second remote code execution vector is via stale global state surviving after its backing memory has been freed. 
Both of these remote code execution vulnerabilities are rated critical at 9.2 out of 10.
More details on these security vulnerabilities and the updated PHP versions at PHP.net.

## [68] NVIDIA cuDSS Now Generally Available to Accelerate Engineering and Scientific Simulations
NVIDIA Blog | full text via NVIDIA Blog | ~407 words

NVIDIA cuDSS, launched today in general availability, is an NVIDIA CUDA-X library that shifts a critical part of engineering and scientific simulations onto GPUs.
Complex engineering feats — from advanced chips to aircraft to industrial systems —– depend on simulation to predict how designs will perform before they’re built. As designs become more complex, simulations take longer to run, increasing computing demands and limiting the number of ideas teams can test.
NVIDIA cuDSS accelerates solving large sparse systems — the math-heavy step that repeats throughout engineering and scientific simulations and often limits how many designs a team can test — by tapping into GPUs. This lets applications reduce time to results and increase simulation throughput, enabling end users to explore larger more realistic models, more accurate representations and a wider design space at a reduced cost.
Industry leaders are already integrating NVIDIA cuDSS into their tools to transform workflows for their end customers:
- Applied Materials: With cuDSS, Applied Materials accelerated sparse solves in Ginestra, its physics-based, defect-centric simulation platform, by up to 10x versus CPU-only approaches, speeding exploration of semiconductor materials and device reliability.
- COMSOL: Using COMSOL Multiphysics with NVIDIA cuDSS on NVIDIA accelerated computing, ZEISS SMT achieved a measured 4x speedup in an EUV lithography plasma simulation benchmark, completing the full simulation in six days and 14 hours.
- Cadence: Uses cuDSS in its Celsius software to accelerate simulations of heat, structural stress and warpage in advanced chips and 3D chip designs, helping customers including Nokia analyze complex designs faster.
- Dassault Systèmes: Dassault Systèmes reports an 8-10x speedup using cuDSS within its Abaqus structural and computer simulation technology electromagnetic solvers for performance-critical simulations across industries.
- Siemens: Siemens uses cuDSS in Simcenter STAR-CCM+ to accelerate simulations of structures in fluid-structure interaction workflows.
- Synopsys: Synopsys uses cuDSS in its Sentaurus Device simulator tool to accelerate simulations of advanced logic, memory and power chips, helping Infineon model increasingly complex devices faster.
Accelerated Simulation at Scale
As simulation workloads grow in size and complexity, cuDSS can scale out of the box from individual workstations to large computing clusters. [...]

## [41] LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data
arXiv cs.LG | full text via arXiv cs.LG | ~406 words

Computer Science > Computation and Language
  [Submitted on 21 Oct 2026]
Title:LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data
View PDF HTML (experimental)
            Abstract:Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target short-context tasks. Therefore, we propose $\textbf{LongZero}$, a method that lets an LLM improve its own long-context reasoning without any external data. Instead of writing questions and answers over existing documents, LongZero first has the model synthesize the question and answer with its supporting evidence in a compact structured form, and only then separately expands the evidence into a long multi-document context. LongZero combines these self-written multi-hop reasoning tasks with self-written multi-round retrieval tasks and trains the model with GRPO. We evaluate LongZero on two LLMs across five long-context reasoning benchmarks and compare it with RL on data synthesized from external corpora. Experimental results show that LongZero can generalize to real tasks, and outperforms both baselines, suggesting a viable and promising path to improving long-context reasoning of LLMs.
    
Additional Features
References & Citations
    
    Loading... [...]

## [19] ServiceNow and Nvidia launch Arc, a new AI agent for enterprise
ZDNet | full text via ZDNet | ~593 words

ZDNET’s key takeaways
- Arc, originally announced in May, is now generally available.
- The agent is built for Nvidia’s new RTX Spark devices.
- Multi-level security infrastructure around Arc aims to give businesses peace of mind.
One of the main roadblocks to adopting more autonomous AI systems for companies is adequate security controls, especially after a summer of agent-led breaches. Software company ServiceNow has partnered with Nvidia to address that need by combining AI capabilities with security-first guardrails. 
Arc, which ServiceNow and Nvidia call “a personal long-running AI agent that can take on everyday work,” is generally available as of Wednesday. The companies originally released the idea for the agent back in May. Arc is available now on Mac, but Windows support is still on the way. 
What Arc can do
Like many agents built for enterprise use, Arc is designed for daily tasks that rely on productivity tools such as email and Microsoft Teams. Designed to run efficiently on Nvidia’s new RTX Spark devices, it can run locally on an employee’s desktop or within Nvidia OpenShell on its own device. Similar to other agents that work off of accumulated context, ServiceNow and Nvidia said Arc builds memory and skills over time so that its performance continually improves.
More from ZDNET
Also: Microsoft’s new Nvidia PCs are cool for extreme power users – but I’ll wait for AI PC 3.0
The companies also said Arc is efficient, handing more complex tasks off to frontier models only when necessary and keeping data as local as possible otherwise. ServiceNow and Nvidia also said that Arc “proactively surfaces work and action items” by scanning an employee’s inbox and meeting notes.
But more than any new or highly competitive capabilities overall, what sets Arc apart, according to the companies, is the multi-level security framework surrounding it. ServiceNow and Nvidia said their approach offers more reliable security by “moving enforcement beyond the software layer into the runtime and hardware layers.”
Essentially, while the Arc agent is working on tasks, ServiceNow’s Super Intelligence Control Tower enforces company policies, while Nvidia OpenShell restricts the agent’s behavior where necessary.
“IT defines policies in the Super Intelligence Control Tower and NVIDIA OpenShell can be directed to enforce them at runtime,” the announcement explained. [...]

## [212] Fwupd Working Toward Proper Android Integration
Phoronix | full text via Phoronix | ~155 words

Fwupd Working Toward Proper Android Integration
Google Chromebooks already have a mandate for nice Fwupd support with the Linux Vendor Firmware (LVFS) while now there is work on improving the Android integration for Fwupd/LVFS.
Richard Hughes posted yesterday on Mastodon that he's merged support in Fwupd for supporting fwupdmgr refresh on Android devices to download metadata from the LVFS. The fwupdmgr update command is also working for getting firmware updates deployed onto the device. 
The Red Hat engineer and Fwupd/LVFS lead developer even remarked in his post that the Fwupd support on Android is "very nearly to feature parity at feature parity with Linux and FreeBSD!"
In a follow-up comment he mentioned the plan is for bringing Fwupd/LVFS to "actual Android" with "proper integration". This would make sense especially with the recent Googlebook announcement that is Android-based and considering the long history of Fwupd/LVFS for Chromebooks.
A nice win for this open-source firmware updating solution.

## [175] Linus Torvalds Eliminates Unsafe __get_user() & __put_user() Functions In Linux 7.4
Phoronix | full text via Phoronix | ~393 words

Linus Torvalds Eliminates Unsafe __get_user() & __put_user() Functions In Linux 7.4
Linus Torvalds continues with his recent uptick in kernel patches himself, assisted in part by AI with Claude Code. Merged today was removing the historical and unsafe __get_user() and __put_user() kernel functions.
Linus Torvalds merged his code branch removing the __get_user() and __put_user() functions inside the Linux kernel. These functions are the faster but less safe versions of get_user() and set_user() due to less safety checking. The __get_user() / get_user() function is used for copying a single simple variable from user-space to kernel-space while __put_user() / put_user() is used for writing a single variable from kernel space to user-space. The versions removed lack pointer validation checks making them unsafe. Linus describes their removal in the Git merge as:
"This is long over-due: the __get_user() and __put_user() functions are entirely historical, and are never the [right] thing to use any more.  And when mis-used (read: every case) they are not only slower than the right thing, but also insecure because they don't check the user address range.
Most of the usage sites have been converted long ago, but various left-overs remained.  So this started out as a single patch that I wrote as a "show people how to convert __{get,put}_user() to modern code".
In particular, Thomas last year implemented the very nice new scoped user access region helpers (see commit e497310b4ffb: "uaccess: Provide scoped user access regions") that makes the modern interfaces particularly easy to use and really removes any excuse for the old horrors."
In the Git merge, Torvalds went on to describe the issues and horrors of __get_user() and __put_user().
The functions are removed from all the generic Linux kernel code and completes the final removal of the whole interface for x86/x86_64. There are remnants remaining in some of the other CPU architecture ports due to some non-trivial cases or like ARM64 having their functions already map to get_user() and put_user().
For those wondering about Linus Torvalds' AI coding or not given his work last week with using AI to decipher bugs and working on a nice performance improvement with Claude Code, this __get_user() and __put_user() removal did see some AI activity. Torvalds remarked on the on the mailing list that he was using Claude as a fancy sort of Coccinelle script, which is used for static analysis and source-to-source transformations.

## [195] Snapdragon X2 Performance On Linux Exceeding Expectations In Initial Benchmarks
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~50 words

For your viewing pleasure today are the first Linux benchmarks of the Qualcomm Snapdragon X2 Elite Extreme on Linux using the new Ubuntu 26.10 X1E Concept ISO for Snapdragon X laptop support on Linux. The Snapdragon X2 Elite Extreme flagship SoC is tested within the ASUS Zenbook A16 UX3607OA laptop.

## [205] Build a Hybrid Search Engine in PostgreSQL: BM25 + Vector Retrieval
freeCodeCamp News | full text via freeCodeCamp News | ~208 words

Most application search setups force a trade-off: settle for simple text filters, or manage a separate search cluster like Elasticsearch with complex synchronization pipelines.
In a new video course on the freeCodeCamp.org YouTube channel, I demonstrate how to run an entire production-grade search pipeline inside PostgreSQL. By pairing lexical keyword matching with dense vector embeddings in a single database, you eliminate external dependencies while preserving ACID guarantees for your search index.
Search queries usually demand two different retrieval behaviors. Exact queries like "Apollo 13" require precise keyword matching, which keyword engines handle best. Conceptual queries like "animals that make their own light" describe an idea without naming bioluminescence, which is where semantic vector search excels. Hybrid search executes both strategies simultaneously and uses Reciprocal Rank Fusion (RRF) in SQL to merge the results into one ranked list.
In this course I build a complete full-stack search application over 240,000 Simple English Wikipedia articles. The tutorial covers setting up the pg_textsearch extension for corpus-aware BM25 ranking, storing 384-dimensional sentence embeddings with pgvector and pgvectorscale, and profiling query plans with EXPLAIN (ANALYZE, BUFFERS). The backend ties everything together using Python, FastAPI, and Psycopg, featuring match highlighting and single-transaction document writes.
Watch the PostgreSQL Hybrid Search Course on freeCodeCamp.org (1-hour watch).

## [206] 5 Best GitHub Repositories for AI Agent Skills
KDnuggets | full text via KDnuggets | ~1453 words

5 Best GitHub Repositories for AI Agent Skills
Explore five popular AI agent skill collections that help coding agents plan, test, debug, review, and build better software.
AI coding agents such as Claude Code, Codex, Cursor, and OpenCode have become very good at writing code. But software engineering is much more than that.
You still need to understand requirements, plan features, write tests, debug problems, review changes, and know when something is ready to ship.
This is where AI agent skills come in. They are reusable instructions and workflows that teach agents how to handle specific tasks without you having to explain the same process every time.
In this article, we will look at five popular open-source collections:
- Superpowers by Jesse Vincent (⭐285.5K)
- Skills for Real Engineers by Matt Pocock (⭐260.1K)
- ECC by Affaan (⭐256.7K)
- Awesome LLM Apps by Shubham Saboo (⭐137.3K)
- Agent Skills by Addy Osmani (⭐93.6K)
Each takes a slightly different approach to making coding agents more useful for real software development.
1. Superpowers by Jesse Vincent
Superpowers is one of the most popular agent skill projects on GitHub. Created by Jesse Vincent and the team at Prime Radiant, it is a software development methodology for coding agents, built from a collection of reusable skills.
The important word here is methodology.
Instead of simply giving your agent more abilities, Superpowers changes how it approaches software development.
Its skills cover things like:
- brainstorming
- implementation planning
- test-driven development
- systematic debugging
- Git worktrees
- parallel agents
- code review
- verification
For example, if you ask the agent to build a feature, it first uses brainstorming to understand what you actually want. After the design is approved, it creates a plan, implements it using subagents or plan execution, follows test-driven development (TDD), reviews the code, and verifies everything before finishing the branch.
Debugging follows the same idea. The systematic-debugging skill uses a structured root-cause process instead of letting the agent randomly change code until something works.
This is what makes Superpowers interesting. You are not just installing another prompt or tool. You are basically giving your coding agent a proper software development process. [...]

## [21] NVIDIA Open Models Advance Europe’s Sovereign Intelligence Across Industries
NVIDIA Blog | full text via NVIDIA Blog | ~1063 words

NVIDIA is expanding its family of open models across language, robotics, biology, and quantum computing, giving developers, researchers and enterprises what they need to build applications tailored to local languages and industries
The portfolio includes the new NVIDIA Nemotron 3.5 Super VL and Nemotron 3.5 Bolt models; new NVIDIA Nemotron Retriever models for embedding, reranking and document parsing; the new NVIDIA Kumo family open weight foundation models and libraries for structured business data; NVIDIA Cosmos 3.5 world models; NVIDIA Alpamayo 2 Edge for autonomous vehicles; NVIDIA BioNeMo for healthcare and scientific discovery; and NVIDIA Ising for quantum computing.
The open models give organizations a foundation they can customize with local data and deploy on infrastructure they control.
NVIDIA Nemotron Powers Post-Training Across Industries
NVIDIA Nemotron brings open language models, datasets and recipes to developers building agents. The models support text and images, helping agents orchestrate workflows, reason through complex problems and complete specialized tasks at a lower cost. Nemotron models are built with data, research and expertise from the NVIDIA Nemotron Coalition, including European partners Black Forest Labs, H-Company and Mistral.
Nemotron provides a foundation for enterprises to build applications based on their own knowledge and expertise. Dassault Systèmes, Domyn, Dream, Palantir’s customers, Salesforce, SAP, Shopify, Synopsys and WPP, as well as professional services providers like Accenture and EY, are working with Nemotron models and datasets to create custom models and build domain-specific agents.
A broad ecosystem of post-training partners, including AfterQuery, AgileRL, AI21, Alice, Applied Compute, Baseten, CoreWeave, Distil Labs, EON, Fastino, Fireworks, Google Cloud, Mercor, Multiverse Computing, Nebius, Handshake AI, Plurai, Prime Intellect, River.AI, Scale AI, Trajectory and TNG, is helping enterprises customize Nemotron for domain-specific workloads.
NVIDIA Kumo Speeds Agents’ Work With Structured Enterprise Data
NVIDIA Kumo open foundation models, libraries and tools help agents and applications forecast outcomes, score fraud risk and recommend actions from structured business data. Part of NVIDIA Agent Knowledge Foundation, Kumo shortens time to prediction and reduces the cost and complexity of building a separate machine learning pipeline for every task. [...]
