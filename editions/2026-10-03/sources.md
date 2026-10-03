# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Updates to Full Disk Access in macOS
Lobsters | full text via Lobsters | ~185 words

Updates to Full Disk Access in macOS
October 2, 2026
We give developers powerful APIs to build incredible capabilities into their apps for Apple products, backed by a set of controls designed to protect users’ private data. Full Disk Access largely sidesteps these controls in order to allow backup apps to function properly on the Mac. Some developers are using Full Disk Access in ways that could put users at risk, exposing everything on their systems—including files, mail, messages, and even browsing history—without users’ full knowledge and understanding. For communication apps, this can also compromise the privacy of the people users are communicating with.
Going forward, we will introduce additional controls to ensure that users who genuinely wish to grant an app this extraordinary level of access can only do so with very explicit user action. Addressing this is critical. As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially. We are committed to ensuring users clearly understand these risks before granting such access, so they can make informed decisions about their own data and privacy.

## [8] Court agrees with EFF: Utah's VPN law demands a technical impossibility
Hacker News | full text via Hacker News | ~1041 words

When state lawmakers attempt to rewrite how the internet works, users rely on courts to recognize that laws can’t make technical impossibilities a reality. That’s why we were happy to see that a court has blocked Utah’s attempt to outlaw the privacy protections of Virtual Private Networks (VPNs).
In a win for digital rights, a federal judge has issued a preliminary injunction blocking Utah’s SB 73, the state’s draconian anti-VPN age verification law. The decision comes as EFF submitted our comments to the Utah Department of Commerce, detailing how forcing platforms to detect and block privacy-preserving tools undermines user privacy and security worldwide while demanding the impossible.
What SB 73 Does
Signed into law earlier this year, SB 73 attempted to regulate adult websites by requiring them to block VPN users or to identify the physical location of visitors using them or similar tools that mask their network traffic. It even went so far as to prohibit websites from offering instructions on how to use a VPN to bypass these checks. This made Utah, to EFF’s knowledge, the first state in the nation to target the use of VPNs to avoid legally mandated age-verification gates.
The Utah federal court halted enforcement of the law's VPN provisions last week, ruling that the law likely violates the U.S. Constitution’s prohibition on passing laws that significantly burden businesses and people outside Utah’s borders.
SB 73 burdens the rights of all internet users outside of Utah because it requires adult websites to either know every visiting user’s physical location, and then block those in Utah, or to verify every visitor’s age just in case they might be in Utah. The law’s “actual-location provision in practice requires an entity to perform age verification services for every user visiting its site from any location because the entity would violate the law if even one of those users happened to be obfuscating,” the court wrote. The court essentially ruled that Utah has less-burdensome ways to prevent Utah minors from accessing adult websites than requiring all users in the world to comply with SB 73.
Aylo’s lawsuit does not challenge SB 73’s provision prohibiting the websites covered by the law from sharing information about VPNs.
The Legal Challenge
This court order follows months of legal maneuvering. [...]

## [9] With most information hidden, the game Stratego had stumped AI until now
Hacker News | full text via Hacker News | ~375 words

Deep Blue took down Garry Kasparov at chess in 1997, AlphaGo beat Lee Sedol at Go in 2016, and poker bots have been beating professionals for years. But one classic game called Stratego held out. Even DeepMind, with its exceptional budget, couldn’t build a machine that reliably beat the best human players.
Now, a team of researchers from Carnegie Mellon, MIT, New York University, and Stanford University has done it. Their AI, called Ataraxos, beat Pim Niemeijer, arguably the best Stratego player of all time, 15 games to one, with four draws. And it took just 16 GPUs and a few thousand dollars to train it.
Hidden armies
In Stratego, each player gets 40 pieces representing military ranks, from a marshal down to a spy, plus bombs and a flag. You win by capturing the opponent’s flag. Your opponent knows where your pieces are, but not what they are. Identities are revealed only when two pieces collide in battle—the weaker one is removed, and the identity of the winner is revealed. That makes Stratego an imperfect-information game, just like poker, which computers cracked years ago. “There’s something super distinctive about Stratego, which is that it is a massive amount of hidden information that unfolds over a very long time scale,” said Eugene Vinitsky, a researcher at NYU and co-author of the study.
In some forms of poker, the hidden information is tiny. In Texas Hold’em, “You only have two hidden cards,” said Gabriele Farina, an MIT computer scientist and another co-author. That leaves just 1,326 possible hands, few enough for a machine to weigh them all. “In Stratego, there’s 40 pieces on the board that could be in any order,” Farina said. That’s more than a decillion possible setups. Then there’s the game’s length.
“In chess, usually the game lasts 40 moves, but in Stratego, a game can easily last 2,000 moves,” Farina said. On top of that, Stratego is a game of bluffing. Sometimes you move a weak piece as if it were a marshal, just to scare the opponent off. When players bluff too often, their threats mean nothing; when they never bluff, they become predictable. That balancing act, the team explains, is what stumped earlier AIs like DeepMind’s DeepNash, introduced in 2022.

## [42] OpenAI DevDay 2026 Recap for Developers
InfoQ | full text via InfoQ | ~524 words

OpenAI announced a series of product and developer updates at DevDay 2026, including GPT-6.1 Sol, computer use for the Agents API, cloud-based Codex environments, a Decisions API, and new plugin capabilities for ChatGPT.
For developers building agents, the Agents API now supports computer use, allowing applications to operate software through graphical interfaces. The API also incorporates multi-agent capabilities from Codex, tool search, tool calling, and context compaction, with OpenAI managing the underlying execution infrastructure. The functionality is available through the API and in Codex and ChatGPT Work for selected plans.
OpenAI also released GPT-6.1 Sol, an update to GPT-6 Sol aimed at coding, computer use, and professional tasks. OpenAI says the model approaches GPT-6 Astra on several evaluations while charging one-fifth of Astra's standard input and output token prices. Cached input costs $0.10 per million tokens. GPT-6.1 Sol is available through the API, ChatGPT Work, and Codex.
Codex can now run in cloud environments in addition to local computers, allowing developers to start remote tasks from other devices. OpenAI also updated the Codex CLI with voice input and an /agents interface for delegating and monitoring multiple tasks. A new code-review workflow can analyze diffs and potential issues in GitHub pull requests and GitLab merge requests, while Codex Security Cloud can scan repositories and new commits, investigate findings, remove duplicates, and prepare fixes.
Another developer release is the Decisions API, currently in limited preview. It uses the smaller Luna model to select from a predefined set of answers based on text or image context. OpenAI positions the API for tasks such as classification, request routing, and choosing an agent's next action.
OpenAI also expanded ChatGPT's plugin system. Developers can now build sidebar experiences, interactive conversation panels, and custom file viewers. Plugins can also respond to events through the proposed MCP Events specification, allowing automations to start when an event occurs in a connected application.
DevDay also introduced Dots, persistent agents that can work on ongoing tasks, and ChatGPT Space, a shared workspace where teams and agents can work with common context. Together with the developer releases, these changes extend OpenAI's platform from individual model calls toward persistent agents that can use tools, operate software, collaborate, and execute tasks remotely. [...]

## [28] US arrests tech CEO accused of smuggling $300M in Nvidia chips into China
Ars Technica | full text via Ars Technica | ~1613 words

The US has arrested another suspect accused of smuggling high-end computer servers containing export-controlled Nvidia chips into China.
In a press release on Thursday, the Department of Justice accused 38-year-old Greg Lui of using false paperwork to mask shipments of servers worth more than $300 million that he allegedly knew were ultimately destined for China.
As the CEO of Earthmade Computer, Lui allegedly conspired with freight-forwarding firms in South Asian countries like Malaysia and Singapore to illegally divert chip shipments into China, including Nvidia’s A100 GPUs and H100 GPUs, the FBI’s indictment alleged. These are not Nvidia’s most advanced chips. However, the chips can process large amounts of data and train large language models, which the US fears could pose national security risks if China suddenly gets access to enough chips to drastically advance its AI or strengthen its military.
Emails and bank records exposed the smuggling scheme, the DOJ alleged, which started in October 2023 and continued until August 2026.
One key piece of evidence is a 2024 email discussing an order for 70 servers with export-restricted GPUs that were fraudulently claimed as destined for Malaysia. After “Lui submitted a purchase order to a US manufacturer for 27 of these servers for approximately $7,614,000,” the DOJ alleged that a co-conspirator told a Malaysian government official that all 27 were shipped to China.
A similar shipment of 92 export-controlled servers was allegedly routed through Singapore to Malaysia, then Hong Kong. Finally, the chips went to a Chinese firm based in Hangzhou, the FBI alleged, which The Wall Street Journal last year described as China’s AI hub.
Yet another flagged 2024 shipment shows how far Lui allegedly went to fool US officials.
When shipping 100 Malaysian-bound servers—each containing Nvidia H100 GPUs worth over $22 million—Lui allegedly submitted fraudulent documentation from a fake buyer identifying its CEO as “Jackie Lui.” Three years prior, Lui “purchased the identifying documents of an individual whose identity is known to the grand jury and used this identity to conduct business transactions in furtherance of the export evasion scheme,” the FBI alleged.
In 2024, Lui’s firm allegedly received more than $176 million from the scheme. Payment records from Lui’s accounts with Bank of America and JP Morgan provided further evidence of how he allegedly operated the smuggling business. [...]

## [34] A model guide for the GPT-6 family
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~21 words

Learn how startups can choose GPT-6 models, tune reasoning effort, improve prompts and skills, coordinate tools, and prepare workflows for production.

## [32] The Four Horsemen of Agentic Coding
Lobsters | full text via Lobsters | ~1384 words

Agentic coding is undeniably very useful. It’s also very bad. Or rather, it’s having some horrible effects on us, our craft, and our relationships with each other. I can feel it in my bones, and a lot of others can too. But whenever I try to explain what exactly is wrong, I find myself waving my hands wildly and jumping from point to point. What do you mean, what’s wrong? So many things are wrong!
Fine, here’s a list. 4 problems with no solution in sight–or, as I call them, the four horsemen of agentic coding.
Slop
LLM-generated code has a strong smell that makes codebases repulsive to humans.
LLMs aren’t humans, and the way they write code is... different. Not strictly worse, but different for sure. We quickly came up with a name for it—slop—and it undoubtedly carries a negative connotation.
For plain prose, humanity seems to be converging on the opinion that AI prose is bland at best and an insult at worst. For code, due to its instrumental nature, the debate is far from over. A lot of people latch on to the idea that very soon we won’t have to read the code at all. “Remember, it’s the worst the models will ever be,” they say.
And yet, the latest generation of models is surprisingly underwhelming. They’re certainly smart, but they seem to be moving towards “unemployable smart” rather than “inspiring smart.” Claude now famously communicates entirely through word salad, and Astra writes in a bizarre competitive code-golfy style, incomprehensible to normal humans. Sloppiness turned out to be a surprisingly persistent property of LLM output and at this point looks like a signature move rather than a growing pain.
Which is very bad news for people who still want to poke around in the codebase and maintain some familiarity with it, especially in a team setting. Once agents are allowed, they very quickly take over. What used to be a shared space for humans where each team member contributed became an AI wasteland where people don’t want to spend time.
But what if we don’t have to spend time in these slop caves? Why spend your time there when you can be a design mastermind and reign over a swarm of loyal agents from the comfort of the chat interface?
Alienation
Engineers become alienated from code and, as a result, care less.
Software engineering used to be a fairly... kinesthetic field of work. Maybe not to the same degree as woodworking, but we loved our tools too, both real and virtual. Text editors had a cult-like following. [...]

## [39] NVIDIA DGX Spark 64GB Gives Developers More Ways to Build and Scale Local AI
NVIDIA Blog | full text via NVIDIA Blog | ~1027 words

Local AI is becoming more useful by the token.
As AI agents move from experiments into everyday development, increasingly capable open models are shrinking to fit on more devices, giving builders more to run locally.
Coming this month, NVIDIA DGX Spark will be available with 64GB of unified memory from top manufacturer partners — Acer, ASUS, Dell, Gigabyte, HP and MSI — giving developers, researchers and AI enthusiasts a new configuration with DGX OS and the NVIDIA AI software stack ready to use from day one.
The new SKU runs capable local agents on device — privately, without cloud dependency. And when workloads grow, two units can cluster together via NVIDIA Sync Cluster Assistant without any additional setup.
A New Starting Point for Personal AI Supercomputing
DGX Spark combines NVIDIA Grace Blackwell compute, unified memory, NVIDIA ConnectX-7 networking and an NVIDIA CUDA-accelerated AI software stack in one system. It’s a complete local AI platform for agents, inference, fine-tuning, data science and edge development.
The compact, personal AI supercomputer provides a place to experiment with models and developers’ own data without turning to a cloud instance for every task.
The new 64GB configuration, available exclusively from manufacturer partners, keeps the platform at an accessible price point while retaining the GB10 Grace Blackwell Superchip, DGX OS and full NVIDIA AI software stack — same as the 128GB model. It supports up to 100-billion-parameter models and the agentic applications built on them, fully on device.
Two 64GB units clustered together don’t just double the memory. In NVIDIA’s Qwen 3.8 27B test, two clustered 64 GB systems delivered up to 1.7x performance compared with a single system, with room to keep scaling as workloads demand.
DGX Spark ships ready for agent development from day one — NVIDIA Agent Toolkit, CUDA-X AI libraries, Nemotron open models, and popular runtimes like Ollama, vLLM, and PyTorch with CUDA are all supported out of the box. Developers can go from power-on to running models in minutes.
Blender is among the first major creator application providers to support the platform, with a prebuilt, downloadable installer coming soon.
Scale Up With NVIDIA Sync Cluster Assistant
Developers can start with the memory their projects need today and build on a platform designed to seamlessly scale multi-node clusters for larger workloads as their pipelines grow. [...]

## [36] Uber Eats Rebuilds Search Pipeline to Cut End-to-End Latency by 50%
InfoQ | full text via InfoQ | ~467 words

Uber has rebuilt major parts of the Uber Eats search pipeline and reports a 50% reduction in end-to-end search latency. The changes span retrieval, feature hydration, ranking, advertising, presentation, and infrastructure, while an agentic coding workflow was also used to identify, benchmark, and validate additional optimizations.
The work began with a change in the primary latency metric. Instead of focusing on backend API response time, Uber began measuring Above-the-Fold completion, defined as the time until the first screen of results is rendered with images. Pagination with server-side caching reduced the initial response, while asynchronous rendering allowed result items to be processed concurrently. Uber reports that these changes improved Above-the-Fold latency by more than 200 milliseconds.
Uber Eats search pipeline architecture (Source: Uber Blog Post)
Uber reduced retrieval work after finding that tens of thousands of candidates were hydrated before ranking, and discarded many of them. Removing low-value retrieval strategies cut about 120 milliseconds, while product-level embeddings reduced data lookups by more than 100 times and saved another 50 milliseconds. Separating ranking hydration from presentation data reduced latency by more than 100 milliseconds, with dependency removal and request hedging contributing another 35 and 40 milliseconds, respectively. The advertising path was redesigned with column-oriented bid data, in-memory access, and less serialization, reducing latency by about 130 milliseconds. Additional infrastructure changes included parallel encoding, smaller embeddings, connection management improvements, and Go data structure changes to reduce garbage collection overhead.
The approach has drawn attention from engineers discussing the work publicly. Anubhooti Nagar described the performance challenge as,
It’s less about doing things faster and more about doing less work and avoiding unnecessary waiting.
Nagar also highlighted Uber’s
Measure, Identify, Fix, Validate loop as a model for continuous performance optimization.
Pratik Dhanave emphasized that the result came from incremental optimization rather than a single architectural change, describing it as no single big idea behind it, but a long list of careful decisions across the full stack. He pointed to changes across latency measurement, hydration, advertising, and infrastructure as examples.
Vidya Pandey distilled those changes into three principles: Do less work. [...]

## [45] Docker Sandbox Kit Spec: Packaging AI Agent Permissions as OCI Images
InfoQ | full text via InfoQ | ~618 words

Docker has announced that it is bringing the Sandbox Kit Specification to the CNCF, aiming to make what an AI agent may access as portable as the agent itself. The Apache 2.0 spec, now at v3, packages an agent, its tools, and a typed list of the hosts, credentials, and volumes it requests into an ordinary OCI image. Docker announced the move at WeAreDevelopers on September 24.
Agents such as Claude Code and Codex install packages, call APIs, and use credentials on a user's behalf. The grants that make them useful, such as bind mounts, broad tokens, and opened firewall rules, usually live in shell history, dashboards, and memory rather than in a reviewable artifact. Docker argues this is the fragmentation OCI was created to prevent, and that every runtime vendor could otherwise invent its own answer.
In v3, a Kit is no longer its own artifact type. It has no custom media type and no sidecar file. The manifest has one declaration: vnd.docker.sandbox.kit.descriptor. So, a Kit can be built with docker buildx build, pulled with docker pull, and scanned, signed, or used in a FROM. Pinning the digest pins content and permissions together.
Declarations are typed and versioned capabilities, for example com.docker.sandbox/network-policy@2 and com.docker.sandbox/credential@1. In the spec's GitHub CLI example, the Kit allows api.github.com but denies DELETE on /repos/**, since deny wins. Credentials can be proxy-managed: a conforming runtime injects the real token into requests to named domains, and only a sentinel value exists inside the sandbox.
A Kit only requests permissions; the host decides. Without a conforming runtime, the annotation is inert. If a required request cannot be satisfied, the launch is refused. Docker Sandboxes, which run agents in microVMs with their own kernel, is the first conforming runtime.
A launch combines one workload Kit, which supplies the root filesystem, with any number of mixin overlays. Mixins are ordered by the provides/requires dependency graph rather than by flag order. Resolution fails if a requires is unmet or if two Kits provide the same name. Overlapping declarations reconcile, with network rules unioned, and incompatible ones are errors.
Every descriptor also reduces to a normalized set of grants. A runtime that gates updates can record that set and stop any version that widens it, including one that removes a deny rule. Docker says two conformance suites ship with the spec, one for Kit artifacts and one for runtimes. [...]

## [46] DigitalOcean Managed Agents Brings Managed Cloud Infrastructure to AI Agents
InfoQ | full text via InfoQ | ~536 words

DigitalOcean recently launched DigitalOcean Managed Agents in public preview, offering a managed cloud infrastructure layer for AI agents with isolated microVM runtimes, governed tool access, and serverless AI inference.
According to DigitalOcean, agentic workflows differ substantially from traditional cloud-based applications, requiring developers who run agents on conventional VMs to build and manage the supporting runtime environment themselves:
Developers are forced to invest in plumbing work to preserve the agent's context, persist artifacts and keep them accessible beyond the agent that created them, coordinate parallel work, and security-hardened access to tools.
Further challenges include maintaining spare VM capacity to ensure agents can start quickly, as well as provisioning and configuring compute resources on demand. DigitalOcean Managed Agents aim to address these challenges by combining two integrated services: a Harness Runtime and an Action Gateway.
Together, they let developers scale the work their agents can do while DigitalOcean manages the execution, persistence, tool access, and infrastructure underneath. Let’s dive a bit deeper into each of these new services, their capabilities and how they enable you to scale agentic work in the cloud.
Built on a lightweight microVM, the Harness Runtime provides persistent, isolated compute environments for agents across a range of supported harnesses, including coding agents like Claude Code, Codex CLI, and OpenCode; general-purpose agents such as Hermes; and custom agents built with LangGraph.
The harness runtime can persist conversational history and working state across sessions, which can be pauses, resumed, or forked. Sessions can also automatically pause agents when they are idle, i.e., when there are no ongoing LLM or tool calls.
Each session runs on security-hardened compute and storage resources, while allowing developers to connect to internal services without exposing them publicly. Sessions can be launched in parallel across repositories and tasks, supporting workflows like divide and conquer, collaboration and map/reduce.
The Action Gateway is the agent's interface to external tools and services though a unified MCP endpoint, with more than 16,000 tools currently available. These include Web Search, Web Fetch, Browser Automation, as well as the DigitalOcean infrastructure management APIs, as well as connectors for popular platforms like GitHub, HubSpot, Stripe, and others. [...]

## [43] Engineering Production Systems for an Agentic Era: QCon San Francisco 2026
InfoQ | full text via InfoQ | ~996 words

AI agents are changing more than the way code is written. They are becoming users of production systems, initiating customer actions, querying observability data, and influencing how software is tested and released. That creates practical questions for senior engineers. Which decisions can safely be delegated to an agent? What evidence is needed before agent-generated work reaches production? How should existing systems expose context without expanding risk? Where must experienced engineers retain direct control?
QCon San Francisco 2026, taking place November 16–20, brings together practitioners from Airbnb, OpenAI, Netflix, Honeycomb, and other engineering organizations to share how they are answering these questions in production. The program connects emerging AI practices with established lessons from distributed systems, architecture, data platforms, observability, and resilient operations.
Moving AI agents into customer-facing systems
An agent that drafts text presents a different level of risk from one that can take action on a customer’s account. Teams building these systems need controls that go beyond a prompt or a single model-level safeguard.
In "How Airbnb Guardrailed Its AI Customer Support Agent", Weiping Peng, Distinguished Engineer at Airbnb, will examine the safeguards behind an agent that serves millions of customers, maintains context across conversations, and can initiate account actions.
Weiping will discuss the layered approach used to prepare the agent for production, including input sanitization, classifiers, shadow testing, false-positive management, and rapid-response mitigations. For engineers introducing agents into customer-facing workflows, the session offers a concrete example of how preventive controls, offline testing, and production response can work together.
Deciding what coding agents should and should not own
Coding agents can reduce the time required to implement and iterate on software, but speed does not remove the need for engineering judgment. Teams still need to decide how generated work is verified and who owns architecture, quality, and release decisions.
Brian Yang, Member of Technical Staff at OpenAI, will address these boundaries in "Lessons from Building a $100M Product in Six Weeks at OpenAI". Brian will share the operating model used to build OpenAI Ads with coding agents from the beginning and scale it to more than $100 million in annual recurring revenue in under six weeks. [...]

## [59] Google Researchers Built an Agent for Automated Research
TLDR AI | full text via TLDR AI | ~559 words

A map of possibilities. A reason for the next experiment.
AIM searches over explicit research ideas. Inspired by Bayesian optimization, it separates understanding the idea space from choosing where to spend the experimental budget.
AGENTIC SURROGATE
What looks promising?
Organize. Group ideas by semantic research direction, even when they come from different generation lineages. Rebuild the map as the pool grows.
Estimate. Rank clusters and unevaluated ideas using observed scores, evidence gaps, novelty, and implementation lessons.
Dispatch. Choose explore/exploit actions at both the cluster and idea levels, then select concrete ideas for parallel solvers.
Solve & Expand. Implement and evaluate the selected ideas. Use audited evidence to refine, combine, repair, or introduce new ideas.
A promising direction can still contain an unfamiliar idea worth exploring.
SOLUTION AUDITOR
What did we actually test?
Validate. Check task validity and idea–solution alignment before results inform the next research decision.
Align. Discard invalid evidence. When the implementation differs from the proposed idea, reconstruct the idea to describe the mechanism actually evaluated.
Attribute scores and lessons to the method that was built.
RESOURCE PLANNER
How should we spend the budget?
Allocate. Choose the number of parallel solver branches for each iteration within the remaining experimental budget.
Adapt. Balance wider exploration with more sequential rounds, so new evidence can guide later experiments.
Adapt parallelism while preserving the total branch and execution budgets.
02 / INTERPRETABILITY IN PRACTICE
Follow the decision. Inspect the evidence.
Replay recorded research iterations across nine tasks and 27 runs. See the map, the rankings, the chosen actions, and what actually happened.
More to explore
Iteration
Reading this replay. Scores are the recorded score field on a 0–1 scale, not raw task accuracy. Ranks are relative; 1 is most promising. Cluster IDs are local to each iteration and may change meaning. Rationale text and lessons are agent-authored records, not independent verification. This explorer does not rerun experiments.
03 / RESULTS FROM THE PAPER
Better ideas. Better outcomes.
Mean scores across three runs. AIM leads the two task-group averages; individual task outcomes vary. Values below are transcribed from Tables 1 and 2, separately from the artifact replay. [...]

## [60] Microsoft's first streaming transcription model debuts at No. 1 on Artificial Analysis
TLDR AI | full text via TLDR AI | ~795 words

Our first streaming transcription model debuts at no. 1 on Artificial Analysis 
  
Along with today’s launch of our top-ranking MAI-Transcribe-2-Streaming, we’re also announcing two new voice models: MAI‑Voice‑2.1 and our blazing-fast variant, MAI‑Voice‑2.1‑Flash.
Together, they give users the fast and fluid building blocks to create conversational experiences, with no compromise on accuracy or voice quality.
Meet MAI-Transcribe-2-Streaming: Real-time transcriptions. Really fast.
MAI-Transcribe-2-Streaming delivers low-latency, real-time transcripts in 60 languages, all while supporting automatic, continuous language detection.
It ranks no. 1 for accuracy for both final and partial transcripts on Artificial Analysis. And on its accuracy-versus-latency evaluation, we sit on the Pareto frontier, showing that higher accuracy doesn’t have to come with a hefty latency tradeoff.
Rather than waiting for someone to finish speaking before returning text, it produces its first hypotheses (known as “partials”) in just over 100ms of receiving audio. It then revises them as more context rolls in and commits a stable transcript right away. These partials enable voice-enabled applications to act on speech before the speaker even finishes.
For example, voice agents can start reasoning or calling tools mid-sentence, and live transcripts can appear as people talk. For use cases such as real-time dictation or subtitling, our internal evaluations show that words appear in the transcript 2x faster than with our closest competitor.
MAI-Transcribe-2-Streaming is available at an introductory price of $0.54 per hour of audio through the end of the year.
MAI-Voice-2.1: Seamlessly support multilingual experiences
With the launch of MAI-Voice-2.1, we offer our strongest multilingual text-to-speech model yet.
We’ve expanded the model to support 23 languages and 26 locales, while enabling one single “voice” to use all languages with a truly native accent. Just ask it to speak English… then Mandarin… then German… and the speaker stays unmistakably the same, naturally picking up the local parlance, rather than dragging one accent across languages.
That means your brand can keep a single voice everywhere: a tutoring app can switch languages mid‑lesson without swapping teachers, and a multilingual assistant can reply in whatever language it’s addressed in, all while still sounding like the same voice.
And it’s priced at $22 per 1M characters. [...]

## [11] Greg Kroah-Hartman – Security in the LLM Age [video]
Hacker News | SNIPPET ONLY (Hacker News: HTTP 429) | ~0 words



## [33] Redefining enterprise intelligence with autonomous AI
MIT Technology Review | full text via MIT Technology Review | ~584 words

Sponsored
Redefining enterprise intelligence with autonomous AI
Composable infrastructure, sovereign data, and cross-functional coordination can enable intelligence to flow and AI to grow smarter.
In partnership withUniphore
Enterprise AI is no longer a future ambition. It is in full operational flight. Model capabilities are advancing faster than most organizations can absorb, while the cost of performance continues to fall. Globally, AI investment is set to reach $2.5 trillion in 2026, up 44% from the previous year.
For many enterprises, this investment has produced fragmentation. Intelligence can accumulate in silos so that sales agents are unaware of open support tickets, for instance, or marketing systems are personalizing content without visibility into what finance already knows about a customer. Each function may perform well in isolation, but the enterprise as a whole learns little and has less information to act upon.
The shift from AI as a tool to AI as an operating model—what we call the “agentic shift” in this report—demands something more fundamental than better models or faster infrastructure. It requires connecting people, processes, and data in real time, along with the governance and control to act on that intelligence reliably.
This means rethinking both architecture and operating models simultaneously. First, rebuilding data infrastructure for accessibility rather than volume. Second, replacing fixed tech stacks with composable architectures that can evolve as models and tools change. And, lastly, resolving questions of AI sovereignty, including where intelligence runs, who controls it, and how it operates across organizational and jurisdictional boundaries.
Key findings include the following:
Enterprise AI’s scaling problem is structural. Process-first companies are pulling ahead. Global AI spending is rising sharply and model capabilities are advancing faster than most organizations can integrate them. Yet the majority of enterprises are still not growing revenue through AI or fundamentally rethinking how they operate. The companies generating sustained returns share a common discipline. They treat process redesign as the work that precedes model selection, building for how the technology will evolve rather than retrofitting roles and workflows after deployment. For them, the agentic shift begins with the operating model.
Data readiness, not data abundance, is what makes AI compoundable. [...]

## [70] Weave Router (GitHub Repo)
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403) | ~40 words

Weave Router is an open-source model router for agentic systems that sends each prompt to a suitable model behind an OpenAI-compatible endpoint. It targets sub-50 ms routing overhead and lower inference costs, with a quick-start path for proxying existing applications.

## [71] Pi 1.0
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~562 words

Pi 1.0
Today we are proudly shipping Pi 1.0: a hardened, minimal, extensible agent harness that you can make your own. Hundreds of thousands of people around the world use Pi every week. Many of you submit issues and pull requests. Over the course of many months, we have used that feedback to improve, harden and evolve Pi into a stable piece of software that people and businesses can depend on.
Pi is known for being minimal. We care about holding that line. While agentic tooling changes every week, many of the changes do not last. Pi does not work that way. We wait until something has proven itself, and only then do we consider adopting it; weighing its true functionality against its inherent added complexity. We spoke more about that process and how it relates to Codemode and MCP earlier this week here.
The Pi 1.0 we are shipping today is a result of that process. Pi already ran the latest models from every major provider, became a daily driver coding agent for people around the world, and provided a supermalleable substrate on which to build agentic applications. With Pi 1.0 we are adding the following into Pi:
- Codemode (native support for MCP, and non-LLM models like Jev and image models)
- Extension support for virtual models
- Deferred tool loading
- Cache warming for anthropic models
- Mid-conversation system messages (transcript-aware prompt and tool changes)
- A new TUI theme
- Full-screen mode by default
We have thought about many of these features for months. They were thrown up against the wall and stuck. The list of things that fell off the wall is much longer. When we use Pi with all these new features it feels like a major step forward, but it also still feels simple, like Pi.
Alongside this work of continually refining and evolving Pi, we also began to understand that there were aspects of Pi that did not fit the shape of how many people wanted to use it. At Earendil, we want to bring Pi's minimalism and the way it allows you to wield AI outside of the coding agent and outside of the terminal. It needs to be reachable from different surfaces and support longer-running conversations and tasks. In short, Pi must become more durable. Rather than stray from our minimal roots and try to make Pi something it wasn't, we combined that work into a new experimental package that we are shipping today, Pi Durable. [...]

## [102] Paramount and Warner Bros. Discovery to become Skydance
TechCrunch | full text via TechCrunch | ~186 words

Paramount and Warner Bros. Discovery will operate as Skydance once their merger closes, Paramount CEO David Ellison announced Friday. Skydance is the name of Ellison’s original film production company.
The roughly $110 billion deal is expected to close October 6. It will combine two major Hollywood studios, Paramount+ and HBO Max, and networks including CBS, CNN, MTV, TBS, Comedy Central, and Food Network. Skydance will also control franchises such as “The Lord of the Rings,” “Game of Thrones,” the DC Universe, and “Yellowstone.”
The merger followed a drawn-out corporate battle. Netflix had agreed to acquire Warner Bros.’ streaming and studio businesses before the broader Paramount deal moved forward. Twelve states challenged the deal, arguing it could reduce competition and harm consumers and workers, but a judge approved a settlement with the state attorneys general this week.
Ellison said the Paramount and Warner Bros. brands will remain central. “We never wanted a new corporate identity to diminish, alter or overshadow either one,” he wrote on X. The new name, he said, gives the company “an identity of its own” while letting both studios “remain in the spotlight.”

## [23] Amazon’s $1B plan to combat data center backlash draws more backlash
Ars Technica | full text via Ars Technica | ~302 words

On Friday, Amazon committed to donating more than $1 billion over the next five years to communities neighboring data centers.
In a press release, Amazon Web Services’ CEO Matt Garman said that communities would decide how to prioritize funds across “education, job training, energy affordability, water, and energy preservation, and local priorities.”
Laying out other community commitments, Amazon also promised to ensure data centers wouldn’t increase power bills or wipe out local water supplies. Regarding the latter, Amazon promised to be “water positive” by 2030, while claiming that 75 percent of projects have already met this goal.
Rolling out these commitments, Amazon seemed bent on convincing Americans that the swelling data center backlash is based on lies. Echoing Donald Trump’s claims that foreign disinformation campaigns are fueling widespread protests, Garman urged that calls for data moratoriums must end or else American frontier AI might fall behind China’s.
According to Garman, US rivals are trying to “trick us into slowing down,” and Amazon’s commitments are meant to reassure Americans that everything’s okay and that we should instead plow ahead, as Trump endlessly advocates.
However, advocates at Stand.Earth—a global nonprofit that’s been fighting for environmental protections in communities hosting data centers—told Ars that Amazon is the one being “misleading” by spreading “corporate propaganda.” Seemingly in crisis mode as billions of dollars in data center projects have been blocked nationwide, Amazon’s promised donations represent “a flailing attempt at damage control for the harm its data center build-out has already caused,” Stand.Earth said.
Most problematic, Stand.Earth suggested, is Amazon’s plan to back a power plant that experts expect will become the largest source of US climate pollution. Glaringly, Amazon’s data center commitments don’t mention the power plant and scarcely address pollution, apart from promising to exclusively rely on back-up generators that use the lowest possible emissions.

## [26] Lyft settles landmark driver misclassification lawsuit for $272.5M
Ars Technica | full text via Ars Technica | ~280 words

California’s attorney general and three city attorneys announced a $272.5 million settlement with Lyft after allegations that the company “committed wage theft by misclassifying drivers as independent contractors rather than employees” between 2016 and 2020, according to a Thursday statement.
The case dates back to May 2020, when then-Attorney General Xavier Becerra, who is now the Democratic candidate for governor, sued both Uber and Lyft. That lawsuit said the ridehailing companies evaded state law when they declared that their drivers were not employees.
Thursday’s settlement affects only Lyft, while the case against Uber continues.
“We are proud to announce this landmark win for workers, the largest misclassification settlement in California’s history,” Attorney General Rob Bonta said in the statement. “Rideshare companies like Lyft have enjoyed massive growth and profits on the backs of drivers over the past decade, many who are from immigrant communities and communities of color.”
The city attorneys echoed this sentiment.
“Los Angeles and our statewide partners will not allow businesses to exploit their workers and evade their obligations under the law,” Los Angeles City Attorney Hydee Feldstein Soto said in the same statement. “When companies misclassify their workers, they deny them critical protections and shift the burden onto taxpayers. This historic settlement sends a clear message: Companies must follow the law, pay their fair share, and play by the rules.”
Ever since these rideshare companies began in the early 2010s, they have been scrutinized for underpaying and mistreating drivers. The specific state law that California used to challenge the companies is known as Assembly Bill 5 (AB5), which enshrined a three-part test to determine if someone is properly classified as an independent contractor or an employee.

## [22] Zig 0.17.0 Release Notes
Lobsters | full text via Lobsters | ~6761 words

Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.
Zig development is funded via Zig Software Foundation, a 501(c)(3) non-profit organization. Please consider a recurring donation so that we can offer more billable hours to our core team members. This is the most straightforward way to accelerate the project along the Roadmap to 1.0. If you need donation receipts or are looking to migrate away from GitHub Sponsors, we recommend donating via Every.org.
This release features 5 months of work: changes from 206 different contributors, spread among 925 commits.
Originally predicted to be shorter, this release cycle ended up substantial, with the Build System reworked, including the introduction of the Build Server Protocol, and the ELF Linker enhanced to the point where we expect Incremental Compilation to work for everyone on x86_64-linux.
Zig supports a wide range of architectures and operating systems. The Support Table and Additional Platforms sections cover the targets that Zig can build programs for, while the zig-bootstrap README covers the targets that the Zig Compiler itself can be easily cross-compiled to run on.
Notable changes:
aarch64-openbsd is now tested natively in Zig's CI, ensuring high-quality
      support going forward.aarch64-freebsd and aarch64-netbsd CI jobs now run on pull
      requests too, in addition to master pushes.aarch64-windows binaries, including the Zig Compiler, has been
      worked around.loongarch32-linux-gnu[sf] targets has been added.sparc64-linux. This is largely thanks to Zig's new ELF linker which now has better
      support for this target than LLD.aarch64-switch,
      arm-gba, mipsel-psx, and powerpc-wiiuxtensa-linux support has been added to Zig. Note that, for now,
      this support can only be exercised via the C backend or the experimental LLVM
      backend.arc[eb]-linux,
      csky-linux, and m88k-openbsd when using the C backend.microblaze[el]-linux,
      sh[eb]-linux, and sparc-linux.-mabi=ieeelongdouble for all PowerPC targets. This is just a
      formalization of what was already reality; Zig has never supported the IBM "double-double"
      format for long double and likely never will. As a result, this release drops
      support for powerpc-linux-gnueabi[hf] because glibc only supports the "double-double"
      format on these targets. [...]

## [35] AI is changing developer work. Here are three skills to strengthen.
GitHub Blog | full text via GitHub Blog | ~613 words

Gwen Davis
Gwen Davis is a senior content strategist at GitHub, where she writes about developer experience, AI-powered workflows, and career growth in tech.
AI is changing how developers work and apply their skills. Writing code is still essential, but developers increasingly need to know how to direct AI, evaluate its output, communicate tradeoffs, and make sound technical decisions.
The good news? You can start preparing today. Here’s where to focus:
AI is changing what execution looks like. Increasingly, great execution means defining the problem clearly, providing the right context, evaluating AI-generated code, and deciding what’s ready to ship. As AI agents take on more of the implementation, these skills become even more valuable.
For example, imagine you’re asked to add a new authentication flow.
A traditional workflow might look like this:
Task: Add authentication  
→ Create branch  
→ Write code  
→ Run tests  
→ Open pull request
As AI tools become more capable and more deeply integrated into day-to-day workflows, those same skills can help you coordinate multiple AI agents. Your workflow might look more like this:
Workspace: Add authentication  
Agent 1 ✓ Authentication ready for review 
Agent 2 ✓ Documentation draft ready  
Agent 3 ✓ Test suite ready
Notice what changed. You’re still responsible for the outcome, but you’re spending less time implementing every piece yourself. Instead, you’re defining the work, reviewing outputs, and making the technical decisions that bring everything together.
Takeaway: Learn to direct AI agents.
Start your first agent session >
AI can generate impressive solutions in seconds, but the first answer isn’t always the best. Your experience writing clean, maintainable code can help you evaluate AI’s output.
Ask a second AI model to critique the first model’s work, then use your own judgment to evaluate both responses.
Here’s a prompt that shows what that might look like in practice:
"Write a SQL query that returns each customer's most recent order." 
↓ 
AI Model #1 
✓ Generates the query 
↓ 
AI Model #2 (Critique) 
⚠ Doesn't handle duplicate timestamps 
⚠ Missing index recommendation 
⚠ May perform poorly on large tables
Different AI models have different strengths and blind spots. That’s why GitHub Copilot’s built-in Rubber Duck agent uses a second model to critique plans, code, and tests before you move forward. A second perspective often catches issues the first model misses. [...]

## [55] RoR creator sparks new “death of coding by hand” debate
TLDR Tech | full text via TLDR Tech | ~2596 words

Before we start: if you happen to be in San Francisco on Thursday, 5 November, join me on the System Update with The Pragmatic Engineer event. This is an evening with OpenAI, Linear and DoorDash and myself, organized by Sentry. We get into what AI-augmented automations they’re running in prod, and how it’s going, in an off-the record (that is: not recorded!) and raw conversation. Seats are limited, and you can RSVP here.
Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics from the last week’s issue of The Pulse. Full subscribers received the article below seven days ago. If you’ve been forwarded this email, you can subscribe here.
The creator of Ruby on Rails, David Heinemeier Hansson, caused quite a stir last week with comments in his Rails World keynote, when he revealed that coding by hand is dead at his company, 37signals.
This is a big deal because 37signals created Ruby on Rails, and they are known for their software craft there, especially when it comes to code quality. It’s also a business that’s 27 years old and is profitable. Despite that pedigree, DHH caused a stir among the dev community, saying:
“At 37signals, a couple of weeks ago, we made the decision that it clearly means we’re done writing code by hand. We have gone pencils down on the idea that we were gonna write code by hand, as a normal course of business creating things.
Writing code by hand at 37signals is now an exceptional state. It is like seeing a bug in Sentry: something here went wrong; why was the agent not able to produce what we wanted? Okay, maybe for a little while, we’ll still get the old pencil out and dot it down for them, but then we fix the machine, we fix the factory, we get things going again. This is a recognition of what’s already happening.”
DHH compared the maturation of AI tools into being highly capable at coding with the impact upon the craft of painting of the arrival of the camera:
“On November 24th, 2025, we got the “Kodak Brownie” of our era. We got Opus 4.5. AI technology, accessible in a harness that many people could afford to use and experience for the first time what it’s like to create software in pairing with a new form of intelligence. This was the tipping point for me. There was everything before November 24th, and then there was everything after. [...]

## [16] The Download: a biological de-aging contest and why LLMs don’t reason
MIT Technology Review | full text via MIT Technology Review | ~1043 words

The Download: a biological de-aging contest and why LLMs don’t reason
Plus: OpenAI says rogue agents may have affected more than 100 organizations.
This is today's edition of The Download, our weekday newsletter that provides a daily dose of what's going on in the world of technology.
A new contest pits competitors against each other in a race to biological youth
—Jessica Hamzelou
This week, I officially signed up for an unusual competition. One that rewards competitors for getting younger.
I recently turned 40, and I don’t need reminding that both time and my chronological age only tick forward. But this game is focused on competitors’ biological ages, figures that are meant to provide a better way to measure the age-related health of our organs and bodies.
Over six months, around 500 of us will try to reverse our biological age using a bunch of different measures. There’s even a leaderboard! But is it even possible to measure whether someone is getting younger?
This story is from The Checkup, our weekly biotech newsletter. Sign up to receive it in your inbox every Thursday.
Opinion: Don’t be fooled—LLMs don’t reason
—Thore Graepel
Ten years ago, I watched a program I helped build stun the world by beating Go champion Lee Sedol. AlphaGo won after making a move so strange that some commentators thought it was a programming glitch. It was AlphaGo’s powers of reasoning that made this creative choice—and these are powers that today’s AI lacks.
This is why I recently left my position at Google DeepMind. I believe we need a fresh approach to machine reasoning, one that draws on AlphaGo’s architecture.
Here’s why today’s AI doesn’t really reason—and what it would take to change that.
Thore Graepel is chair of machine learning at University College London. He was a core member of the AlphaGo team at DeepMind.
The must-reads
I’ve combed the internet to find you today’s most fun/important/scary/fascinating stories about technology.
1 OpenAI says rogue agents may have affected more than 100 organizations
The company is searching 50 petabytes of data for incidents. (Reuters $)
+ It says none of the incidents matched the Hugging Face attack. (Gizmodo)
+ OpenAI has fired three workers for allegedly mishandling information. (BBC)
+ California has subpoenaed OpenAI over its rogue AI agents. (Guardian)
+ Who's liable when AI agents go rogue? [...]

## [21] Someone got Doom in an SQL database
Ars Technica | full text via Ars Technica | ~258 words

“Rendering Doom in a database is obviously a bad idea,” Lukas Vogel writes in a lengthy blog post explaining how exactly he managed to render Doom using an SQL database.
OK, that’s not entirely accurate. The SQLDoom project uses a small Python client to handle input and output, drive the game’s timing, and display each frame to the screen. Behind that, a series of CedarDB tables tracks the game geometry and state, while about 1,300 lines of SQL queries spread across 89 common table expressions implement the game logic and generate 35 bitmap framebuffers per second.
In this, SQLDoom is a major improvement over Vogel’s previous DoomQL project, which last year set out to build “a multiplayer Doom-like shooter entirely in SQL.” Unfortunately, that effort ended up with raycasting-based, grayscale ASCII graphics that were more akin to the simplistic 90-degree-angled maps of Wolfenstein 3D. The newer SQLDoom, on the other hand, generates full-color 640×480 frames that look like they could have come from the original Doom executable.
It’s all just data, man
Converting Doom‘s classic WAD files to a relational database was relatively simple and straightforward, Vogel writes, because of the way the original game broke levels down into vertices, lines, sectors, and so on. Even Doom‘s famous binary-space partition trees can be broken down into SQL using a sort_key for objects that’s pre-computed for each position at load time. With this set in your table, a simple “ORDER BY” statement can determine every frame which parts of walls to display and which to ignore, vastly improving performance.

## [38] The forgetful CPU (Linux on M4)
Lobsters | SNIPPET ONLY (Lobsters: fetch failed: ReadTimeout) | ~0 words



## [57] The Dot and the Swarm
TLDR Tech | full text via TLDR Tech | ~1812 words

I generally think I have done a good job anticipating the direction and pace of AI over the few years I have been writing this Substack, but I think I recently got something fairly large wrong. In the last year I have been posting about how I suspected that humans would have to approach working with agents as a manager, deciding how to delegate work to agents and specifying how those agents should be organized. I thought that getting agents to work effectively as a group would take careful construction, akin to building a company, and that this would take time to figure out.
Nope.
I fell prey to The Bitter Lesson, the hard truth, learned over and over again, that things that we thought required elaborate human rules and thinking can be solved with the brute force of better machine learning systems and more AI. The Bitter Lesson is everywhere among AI startups and companies adopting AI. A huge amount of effort went into building elaborate computer systems to feed AIs the right information at the right time, but AI systems have learned to seek out information themselves. The same thing happened to prompting. People built elaborate templates and chains of prompts that walked the AI through a task one step at a time. Then newer models turned out to be better at planning the steps themselves, and, as our research shows, planning steps have much less value. The history of the Bitter Le—
— you know what? I don’t really need to explain the Bitter Lesson, I asked Claude to do it in a music video. With one prompt, Fable wrote the lyrics and submitted it to Suno; Opus 5.5 did everything else using code alone without any image generation (How did Opus 5.5 pull this off? The Bitter Lesson tells you!). I gave no feedback at all.
As somebody who teaches managers and has published research on management, I guess I believed that managing agents would be different. Humans have been working on management for a very long time without fully figuring it out. It seemed like the kind of thing that would need to be designed by people, at least for a while.
It turns out that organizing work is just one more thing AI can learn to do.
Which brings us to dots and Muse.
Dots and Muse
The number one app in the App Store right now is Meta’s Muse, a personal agent that promises to do work for you. OpenAI has now released a competitor tool, called dots. They aren’t alone: SpaceX’s Grok Bot, Instinct, and Gemini Spark all do similar things, more or less. [...]

## [75] Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents
arXiv cs.AI | full text via arXiv cs.AI | ~382 words

Computer Science > Robotics
  [Submitted on 1 Oct 2026]
Title:Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents
View PDF HTML (experimental)
            Abstract:Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights. RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation. During practice, RPG uses execution feedback, privileged simulator state, and available dataset videos to diagnose failures. It develops new reusable symbolic skills, refines existing skills, and revises the system prompt based on these diagnoses. Cross-task evaluation tests individual candidate changes and merged revisions before they are retained for reuse. At test time, a multimodal LLM uses the resulting system prompt and skill library to coordinate perception and robot control. On held-out initializations of 22 manipulation tasks, RPG improves task success from 28.6% after the first practice round to 95.0% after 15 rounds, outperforming all evaluated baselines, including ASPIRE (75.5%) and CaP-Agent0 powered by GPT-6 Astra Pro (60.0%). After a common calibration and hardware-adaptation procedure, the frozen system succeeds in all 30 physical trials, with ten trials on each of three tasks. Project Website: this https URL
    
Current browse context:
cs.RO
References & Citations
    
    Loading... [...]

## [145] GitHub’s advice for its new Copilot feature is to try something else first
The New Stack | full text via The New Stack | ~616 words

GitHub’s advice for its new Copilot feature is to try something else first
GitHub launched computer use in public preview on Thursday, giving Copilot CLI and its desktop app the ability to operate applications on macOS and Windows. Agents can read app content and click, type, scroll, and drag, including in older, GUI-only software with no API, command-line interface, or MCP integration.
An expense report in Safari was GitHub’s launch demonstration but the company described other uses including summarizing information in a legacy application, updating a presentation, entering data, and moving information between apps. Developers can access the feature from the terminal or through the Copilot app, which runs on Copilot CLI and launched earlier this year as a rival to Claude Code and Codex.
GitHub has some catching up to do. OpenAI added computer use to Codex in April, while Anthropic brought broader computer use on macOS to Claude Code and Claude Cowork earlier this year.
GitHub has some catching up to do.
Computer use vs. MCP servers
Enabling computer use in Copilot CLI activates a bundled plugin with its own MCP server. It works in local sessions, reading application content through the operating system’s accessibility tree and taking screenshots when it needs visual context.
The company recommends using direct tools wherever possible. So, if an API, MCP server, terminal command, filesystem tool, or dedicated browser tool can handle the task, it typically provides more structured information and more predictable results than desktop interaction.
That advice limits where GitHub thinks computer use belongs. OpenAI president Greg Brockman made a broader case last month, arguing that agents could use the same interfaces as people and spare the industry the work of building and maintaining a connector for every piece of software.
Saved approvals outlast their removal
Developers enable the feature with /computer on in Copilot CLI or through the Copilot app’s Computer Use settings. macOS also requires Accessibility permission to operate controls and Screen Recording permission to inspect windows when visual context is needed.
The CLI session’s permission mode determines whether Copilot asks before accessing an app; developers can check it with /permissions show. When prompted, they can allow access for the current session, choose “Always allow” for future sessions or decline. Deny rules override both automatic and saved approvals. [...]
