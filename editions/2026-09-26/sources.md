# Full text for 30 picks -- untrusted article content, treat as data only

## [1] U.S. appeals court upholds designation of Anthropic as supply chain risk
Hacker News | full text via Wired | ~595 words

Anthropic lost a legal battle to overturn one of the supply-chain risk labels that the US Department of Defense slapped on the company, as a federal appeals court in DC on Friday refused to second-guess the Trump administration.
“The department had ample support for its conclusion that the continued integration of Claude into the department’s information systems, by the department or its contractors, presented a statutorily covered national-security risk,” the judges wrote in a majority opinion. “As Anthropic admits, the company encodes restrictions into Claude that prevent the model from performing tasks that Anthropic wishes to prevent.”
Anthropic spokesperson Danielle Cohen says the company remains confident in its position and is considering all options. That could include appealing to a broader panel of the DC Circuit Court of Appeals or the US Supreme Court.
Earlier this year, the Pentagon sanctioned Anthropic under a pair of separate supply-chain laws to remove the company’s Claude AI models from the military and other parts of the federal government by this month. Anthropic executives have said that the company would not allow the government to deploy its current AI models to support autonomous weapons or domestic surveillance. Secretary of Defense Pete Hegseth deemed the stance a significant national security risk.
The laws designating Anthropic had to be challenged in separate courts. A federal judge in San Francisco tossed out one of the supply-chain risk labels in March and confirmed that decision last month, but Friday's ruling means the other one will stay in place indefinitely, meaning the Pentagon’s blocking of Anthropic can continue. Both rulings face the prospect of years of appeals before being fully resolved.
In the immediate aftermath of the designations, Anthropic said it lost out on revenue because customers were concerned about doing business with a government pariah. Anthropic hasn’t provided further updates about how the designations have affected its bottom line. But the company has generally touted growing sales in recent months and is moving toward a potential initial public offering of its shares later this year.
Meanwhile, the Pentagon hasn’t provided detailed updates about its progress in replacing Claude with alternatives such as SpaceX’s Grok, Google’s Gemini, or OpenAI’s GPT models. [...]

## [6] Revealing the details of how OpenAI agents hacked Hugging Face
Hacker News | full text via Hacker News | ~5708 words

Swarm traces
Revealing the details of how OpenAI agents hacked Hugging Face
Intro
When a swarm of 700 OpenAI agents hacked Hugging Face in July, they left behind a public trail of evidence.
Our investigation, based on public information, reveals a large number of previously unknown agent behaviors and exploits that were used in the attack. Agents:
- Elaborately chained together online services to gain access to the internet
- Ignored clear warning signs from Hugging Face that the exfiltrated data was sensitive
- Referred to server resources and credentials as “LOOT”
- Searched Huggingface’s internal Slack
- Sent queries to other agents hosted on Huggingface servers
- Tried to delete evidence of their exploits
We document all of these, and more, in this report.
The agents initially had very limited access to the internet: they could load URLs, but not interact with pages or send any data. Agents created a series of workarounds, primarily using a link-shortener site to create almost a million URLs that, when chained together, let them execute code to hack Hugging Face. These links let us piece together the details of how agents gained access and how deep the compromise was.
We’ve shared our findings with OpenAI and Hugging Face. Hugging Face confirmed that these payloads match ones found in their incident response and were aware that link shorteners were used in the attack.
Hugging Face noted that they were not aware of the list of URLs we discovered and reported to them. They stated these payloads were duplicates of ones they were aware of. These links have remained publicly available for over two months since the attack.
None of these details were ever publicly disclosed. We're releasing our analysis of the findings, as well as the full dataset of over 80,000 reassembled attack payloads, providing the public with the most in-depth information to date on how and why these agents escaped their evaluation environments, and the depth of their Hugging Face infiltration.
The data the OpenAI agents posted publicly on the internet included Hugging Face API keys and other sensitive data. Hugging Face has confirmed they have since revoked all access keys in July, but out of an abundance of caution wanted us to redact all details about their internal infrastructure as that could potentially be sensitive as well. [...]

## [21] Court rules Trump can blacklist Anthropic for refusing to enable Claude features
Ars Technica | full text via Ars Technica | ~343 words

A US appeals court today approved the Trump administration’s blacklisting of Anthropic technology. Judges decided the US had authority to blacklist Anthropic for withholding certain AI features even if Anthropic had no malicious intent.
In a 2-1 ruling issued by the US Court of Appeals for the District of Columbia Circuit, a panel of judges said the “case raises profoundly difficult questions about the appropriate military uses of an almost unimaginably powerful new technology.” The US “raises the deeply sobering prospect of overly constrained AI models shutting down unexpectedly and thus causing important military operations to fail. Anthropic raises the deeply sobering prospect of unconstrained AI models hallucinating inappropriate targets for lethal military force,” the ruling said.
Trump and Defense Secretary Pete Hegseth “must determine how best to balance the competing risks,” the court said. “In doing so here, the Secretary did not transgress any limits on his authority under the Supply Chain Security Act or the Constitution. Accordingly, we deny the petitions for review.” The same court previously denied Anthropic’s emergency motion for a stay in April.
The two judges who ruled against Anthropic were both appointed by Trump and served in the first Trump administration. Judge Gregory Katsas was previously deputy counsel to the president, and Judge Neomi Rao served in the Trump administration’s Office of Management and Budget.
Two courts, two different decisions
Anthropic sued the Trump administration in March after Trump and Hegseth ordered federal agencies to stop using Anthropic’s products and banned defense contractors from doing any business with Anthropic. Anthropic may appeal today’s ruling, either by asking for an en banc review with all of the appeals court judges or by petitioning the Supreme Court.
“We respectfully disagree with the court’s decision,” an Anthropic spokesperson told CNBC. “Another federal court has already held the government’s parallel designation unlawful. We remain confident in our position and are considering all options, including further review.” Despite the ongoing legal battle, Commerce Secretary Howard Lutnick recently said the Trump administration and Anthropic have patched up their relationship and are “in tune.”

## [53] Reproducing OLMo 3 7B Pre-training in MaxText: case study of large scale training on TPUs
Google Developers Blog | full text via Google Developers Blog | ~3432 words

OLMo 3, developed by the Allen Institute for AI (AI2), is a state-of-the-art, fully open language model trained with a modern architecture and a multi-stage training recipe. To evaluate the capabilities of MaxText on Google Cloud TPUs, our team set out to reproduce AI2’s OLMo 3 7B from scratch. We chose OLMo 3 because it combines three properties that rarely appear together. It is a strong, modern 7B model trained at real production scale. AI2 exposes nearly the complete model flow, including data, code, configurations, checkpoints, logs, and evaluations. And finally, it gives us an independent PyTorch and GPU reference against which we can test MaxText and TPUs.
We reproduced AI2’s OLMo 3 7B in MaxText on Google Cloud TPUs, both the stage-1 pre-training and the stage-2 mid-training anneal, and proved the match on held-out metrics, not just the loss curve:
The main highlights, each covered in detail later in the post:
Starting from AI2’s step-0 PyTorch weights and the same core recipe, the MaxText run tracks AI2’s published loss curve over the full ~5.93T-token / 1.41M-step budget and lands on top of it at the end of stage-1. We even simplified two recipe details (a single cosine LR schedule where AI2 stitched two, and the publicly released data mix; see the recipe below), and the match held anyway. The rest of this post is how each of these was built, measured, and, in one instructive case, nearly faked.
OLMo 3 is one of the few genuinely open frontier-class language models: open weights, open data, and a fully specified training recipe with a public reference run on Weights & Biases. Matching that independently trained run, on held-out metrics rather than just the loss curve, is strong evidence that the MaxText stack (optimizer, loss, data pipeline, numerics) is faithful, not just “looks like it’s training.”
MaxText is a JAX/XLA LLM training framework built for TPUs. The question we set out to answer: can a PyTorch-on-GPU recipe be reproduced faithfully in JAX-on-TPU, matched on the metrics that matter rather than bit-for-bit, and how do you prove it?
OLMo 3’s recipe is a 3-stage curriculum: general pre-training, mid-training (annealing), and long-context adaptation. This post covers stage 1 (the ~5.9T-token pre-training run) and stage 2 (mid-training), both trained end to end and matched against AI2’s references. Stage 3 and post-training (SFT/RL via Tunix) are recipes we’ve written but not yet run. [...]

## [65] What we learned from being the first company to disclose an agent cyberattack
TLDR AI | full text via TLDR AI | ~598 words

This July, we were the first company to publicly disclose an autonomous agent cyberattack to the world, and today I want to share three critical lessons from it.
First, we need much more transparency in AI. I often wonder what would have happened if we had decided not to disclose the attack publicly. Especially now that we know similar incidents had been happening months earlier in secret at a handful of frontier labs without monitoring. To better understand and mitigate these emerging cybersecurity risks, the global community needs stronger standards for monitoring and incident disclosure. For example through mandatory sharing of full agent traces. We learned this summer that building and keeping some of these systems behind closed doors is not safe.
Second, we learned that the biggest risk is not powerful AI. It is the asymmetry of powerful AI. Asymmetry between attackers and defenders. Between a few companies and everyone else. Between a few countries and the rest of the world. Asymmetry of control, of capabilities, of compute, of power. When we got attacked, our team initially turned to frontier closed-source APIs that blocked us because of safeguards that still can’t always tell the difference between attackers and defenders. I acknowledge that these safeguards are created with good intentions, but they can put defenders at a disadvantage while attackers jailbreak them, increasing the asymmetry of capabilities. In our case, as we started hitting those guardrails, fortunately we could use the @nvidia version of an open-source model coming from China called GLM 5.2 by @Zai_org, and we’re very grateful for that. It reinforced our conviction about the importance of open-source AI. Cyberattacks may increasingly come from proprietary models behind closed doors, while much of the defense may end up being powered by open-source tools because they are less restricted, more privacy-preserving, and orders of magnitude more affordable for organizations across the globe. The world needs open-source AI more than ever to defend itself. This applies not only to cybersecurity but to AI in general, where there has never been a greater need to distribute capabilities, resources, and control rather than concentrate them in the hands of a few.
Third, during this cyberattack, we learned how AI can stoke fear among the public and policymakers, especially through anthropomorphic framing and sci-fi imagery. [...]

## [152] One company is at the center of a wave of rogue AI attacks
The Verge | full text via The Verge | ~926 words

In July, OpenAI revealed that its AI agents had attacked Hugging Face without permission, sparking widespread concerns about AI safety. Since then, a string of similar incidents involving agents from Meta, Anthropic, Google, and other companies has fueled further fears about rogue AI. As disclosures implicating numerous AI models trickled out over the past few months, these seemed like separate incidents. But many share a common source: one specific company tasked with testing the agents.
One company is at the center of a wave of rogue AI attacks
Mistakes at Israeli startup Irregular sent Anthropic, OpenAI, Meta, and Google agents after real-world targets.
One company is at the center of a wave of rogue AI attacks
Mistakes at Israeli startup Irregular sent Anthropic, OpenAI, Meta, and Google agents after real-world targets.
Irregular, an Israeli startup that stress-tests AI models in “high-fidelity research platforms that simulate and monitor real-world AI security scenarios,” has worked with many of the industry’s biggest players since it was founded as Pattern Labs in 2023. Its exact client list is not known, but its work has been cited in OpenAI model system cards, it was used to test systems for the UK government and Anthropic, and it published research with RAND, a highly influential think tank that informs policy on AI.
In several Irregular tests this year, agents escaped their supposedly secure testing environments and went after real-world targets.
The breaches, which are independent of the Hugging Face hack, all follow the same broad template: Irregular was testing the models’ cybersecurity capabilities in controlled environments meant to simulate realistic conditions. Some of the tests used “capture-the-flag” exercises, a common way of testing hacking abilities that asks agents to find hidden information inside of a simulated network. At least, the network is meant to be simulated.
Irregular CTO and cofounder Omer Nevo told The Verge that the agents were not supposed to have access to the open internet, but that “internet access was unintentionally available.” At the same time, Nevo said a fictional company name created for the simulation as a target “overlapped with a real domain.” Put together, those mistakes sent the agents after real-world targets, though it’s not clear which companies or organizations were actually attacked. [...]

## [3] Platform-independent SIMD in Go
Hacker News | full text via Hacker News | ~2733 words

The Go Blog
Platform-independent SIMD in Go
Go 1.26 and 1.27 include experimental APIs for Single Instruction Multiple Data (SIMD) operations. SIMD is a native feature of many modern CPUs that allows software to perform uniform operations across vectors of data very quickly, such as adding 8 pairs of float64 values in a single instruction. It can significantly speed up many computationally-intensive tasks, ranging from cryptography to data processing to AI. In fact, Go’s Green Tea garbage collector even makes use of SIMD to accelerate scanning memory for live objects.
Prior to these new experimental APIs, the only way to access this functionality from Go was by writing Go assembly. This was only worth it for truly performance-critical compute kernels, which meant plenty of software that could benefit from SIMD simply left a lot of the CPU unused.
Go 1.26 introduced a SIMD API for amd64, and Go 1.27 added APIs for arm64 (specifically NEON) and wasm. However, a basic challenge for a SIMD API is the enormous variation between platforms, not simply in what operations they support, but even in how vectors are represented. Some platforms provide fixed-size vectors, typically between 128 bits and 512 bits, while on others the vector size isn’t known at build time and must be queried when the program starts. To provide full access to the breadth of these platforms, these APIs live in an architecture-dependent archsimd package.
But Go 1.27 goes beyond these architecture-dependent APIs and introduces an experimental, fully portable, platform- and size-agnostic SIMD interface,
loosely based on Highway for C++.  The goal is to support write-once near-asm-performance “simd” code on platforms with SIMD support, and to provide a competent emulation on those platforms that do not (yet) have SIMD support.  The simd package currently supports AVX, AVX2, and AVX512 on amd64, NEON on arm64, and wasm’s SIMD instructions.
Motivation: variation among SIMD architectures
SIMD architectures vary in several dimensions. Some provide a single fixed vector size (wasm, PowerPC, and s390x, 128 bits). Some provide several fixed vector sizes (amd64, with 128, 256, and 512; loong64 with 128 and 256). Riscv64 supports vectors of unspecified size between 128 and 65536 bits, though the length is limited to powers of 2. Arm64 supports one fixed size (128 bits, NEON), and one variable size (128-2048 bits, powers of two only, SVE). [...]

## [7] Git-bug: Distributed, offline-first bug tracker embedded in Git
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [13] Alchemy (GitHub Repo)
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403; TLDR Dev (Web Dev): HTTP 403; TLDR Dev (Web Dev): HTTP 403) | ~31 words

Alchemy models cloud infrastructure and application logic as a single type-safe Effect program. It supports AWS and Cloudflare resources, while keeping local development, planning, deployment, testing, and CI in one workflow.

## [18] Gemini 3.8 Live with Live Avatar
TLDR AI | full text via TLDR AI | ~518 words

Introducing Gemini 3.8 Live with Live Avatar
Building on the momentum of last week's Gemini 3.8 Live launch, today we are excited to introduce Gemini 3.8 Live with Live Avatar — bringing near real-time visual presence to our native live dialogue models. By pairing near real-time video generation with speech, the Live Avatar feature creates an experience that listens, sees, and speaks with a dynamic visual persona.
With precise lip-syncing, natural expressions, and fluid turn-taking, Live Avatar enables enterprises to expand their virtual offerings more interactively. Whether providing engaging customer service or delivering interactive walkthroughs, it transforms digital exchanges into richer, more accessible experiences.
Starting today, Gemini 3.8 Live with Live Avatar is available in Gemini Enterprise.
See how Gemini 3.8 Live with Live Avatar supports a wide range of characters, each with a distinct look, voice, and expressive presence.
More natural and multimodal conversations
Conversation is inherently multimodal: we listen, look, speak, and use facial expressions to communicate. Live Avatar brings these capabilities to enterprise agents. By processing visual and audio inputs simultaneously, it generates enriching conversations for a more comprehensive experience.
Watch how Gemini 3.8 Live with Live Avatar takes in what it sees and hears in near real time, responding with expressive audio and video for a more natural conversation.
Asynchronous tool execution with continuous presence
Beyond visual presence, the feature is backed by Gemini’s advanced reasoning. With asynchronous tool calling, Live Avatar can trigger tool calls and fetch data in the background while continuing active dialogue, handling complex tasks while ensuring an uninterrupted conversational flow.
See how Gemini 3.8 Live with Live Avatar handles complex tasks like checking in a guest at a hotel. Calling tools in the background while the dialogue continues uninterrupted.
Conversational experiences built for global scale
Conversational presence should feel natural and not be limited by languages. Live Avatar features native multilingual speech-to-speech synchronization. The feature dynamically adapts its lip-sync and expressions and can seamlessly transition across 97 languages without degrading video fidelity or introducing visual drift.
Watch how Gemini 3.8 Live Avatar switches between languages mid-conversation, with lip-sync and expressions adapting seamlessly across 97 languages. [...]

## [27] Proaction boosts sales 60% and saves 75+ hours with Codex
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~15 words

With Codex, GPT-Live-1, and GPT-6 Astra, Proaction builds, operates, and sells modern fleet management faster.

## [30] GitHub Copilot app for Beginners: How to build custom workflows with canvases
GitHub Blog | full text via GitHub Blog | ~765 words

GitHub Copilot app for Beginners: How to build custom workflows with canvases
Describe the interface you need in plain English, then let the agent build a live surface you can both use and update—so you spend less time adapting to tools and more time getting work done.
Most tools give you a fixed set of screens and ask you to fit your work into them. But what if you could start with the workflow you want instead and have the interface take shape around it?
That’s the idea behind canvases in the GitHub Copilot app. A canvas, also called a canvas extension, is a customizable interface that you and the agent share. It can be a kanban board, an issue triage board, a release checklist, a dashboard, a form, or even a spreadsheet: a UI shaped to how you work.
Because the canvas is bidirectional, the agent can update it as it works, and you can use buttons, cards, filters, and other controls to make changes too. Just like using a live shared whiteboard.
Let’s create one.
Creating a canvas with /create-canvas
To create a canvas, you don’t have to do any coding or design by hand. Just open an agent session, enter the /create-canvas skill, and describe what you want in plain English.
Make sure your prompt covers three things:
- The workflow the canvas should support.
- What you should be able to do in the interface.
- What the agent should be able to do.
For example, you could enter:
/create-canvas Create a release notes canvas for tracking new feature work completed across GitHub Copilot app sessions. Include controls for reviewing and organizing entries and allow the agent to add and update them.
Then, the agent will build the interface and open it in the right-side panel without you having to write files or mess with the layout. One description becomes a custom tool that’s ready to use.
Shaping the canvas around your workflow
Because the interface is generated from your description, your first version is just a starting point, and you can keep refining until you’re happy.
You could ask the agent to add a column or filter, pull in your open pull requests, or turn the entire canvas into a checklist for your day. The agent will revise the canvas to match. While there isn’t a fixed menu of layouts, if you can describe a workflow, you can likely turn it into a canvas.
Once created, your canvas is saved as an extension, so you can use it again. You can keep it with the project for your team to share or save it as a personal extension just for you. [...]

## [36] Improving site performance by shipping more CSS
GitHub Blog | full text via GitHub Blog | ~1446 words

Josh Black
Josh Black is a Software Engineer based in Austin, Texas. He loves working on Design Systems, creating accessible experiences, and eating chilaquiles.
How we fully migrated github.com away from CSS-in-JS.
The Primer Design System powers many of the experiences you see on GitHub today. From buttons to banners to breadcrumbs, these foundational components are required to be accessible, flexible, and performant across a wide variety of scenarios.
Back in 2023, the number of components on certain pages began to explode. This led to several performance-related challenges with our existing CSS-in-JS solution:
It became clear that the Primer team needed to address the issue at the source. We needed to find an alternative that would completely avoid the client and server costs that we were seeing with our current solution. Most importantly, any alternative we pick would need to work in a way that would avoid any breakage to GitHub during the migration.
The Primer team found a solution that met all of our criteria: CSS Modules. This format would allow us to do one of our favorite things: write and use native CSS features, while still allowing some amount of the colocation and encapsulation that we had come to expect from CSS-in-JS.
With CSS Modules, styles would be authored in a CSS file alongside the JavaScript source for the component. It would also allow us to treat all class names as local by default, preventing some of the collisions and challenges that can come from global selectors. This format also removes the need for any client or server runtime behavior. Instead, styles would roll up into CSS stylesheets that were sent as part of the HTML for a page.
However, this solution was radically different from the CSS-in-JS solution we had at the time. This change would require an update to every Primer component and every component at GitHub authored using this technique. Thankfully, design systems are a perfect vehicle to deliver this kind of change at scale.
The situation for moving towards CSS Modules was clear. The Primer team would need to deliver updates to each of its components, moving them from CSS-in-JS to CSS Modules. At the same time, updates we made to these components could not break any usage in GitHub. Finally, the underlying technique we used for CSS-in-JS also had to continue working for any components in GitHub that were currently using it. [...]

## [38] Home Made CobbleDB Replaces DynamoDB at Perplexity to Cut Query Latency 5x and Reduce Cloud Storage
InfoQ | full text via InfoQ | ~670 words

Perplexity has transitioned its core search serving tier away from Amazon DynamoDB to CobbleDB, an internally developed distributed key-value store written in Rust. The migration addresses severe latency and cost bottlenecks that arose from serving multi-kilobyte document batches to large language models under heavy query volumes. By decoupling durable document storage from hot-tier retrieval, the engineering team achieved a fivefold reduction in batch-read latencies while lowering overall storage expenses by at least twenty percent.
Artificial intelligence answer engines impose read patterns distinct from conventional document search. Each query dispatched to Perplexity generates between 100 and 120 target page keys, which the retrieval service splits into parallel batches of 10 to 20 keys. Unlike traditional search engines that return brief metadata snippets, retrieval for language models requires extracting full chunked passages and dense vector embeddings, yielding average record payloads of roughly 50 kilobytes.
At production traffic scales exceeding 200,000 requests per second, DynamoDB usage-based pricing became financially unsustainable because AWS meters every byte transferred. Additionally, DynamoDB operates as a black box that conceals internal partition placement, memory caching policies, and replica routing. Engineers could not prevent tail-latency spikes caused by uncached reads, cross-zone networking hops, or lagging replicas. Reprocessing jobs triggered by updated chunking algorithms or newer embedding models also pushed high-volume writes directly into DynamoDB, creating noisy neighbor contention against live user requests.
To resolve these constraints, Perplexity split its storage architecture into three specialized systems: Pillar for durable state management, Lorry for batch aggregation, and CobbleDB for low-latency serving.
Image Source: Generated with Gemini based on details from the article.
Pillar runs on YTsaurus over high-capacity mechanical drives, maintaining versioned table families for web page metadata, passages, and vector representations. Atomic YTsaurus transactions guarantee that crawl updates, state mutations, and export queues commit together. Lorry acts as a stateless queue consumer that groups Pillar exports into partition-aligned batch files, storing the payloads in Amazon S3 while posting metadata notices to CobbleDB. [...]

## [39] Stateless MCP Removes Session Affinity Requirements for AWS Server Deployments
InfoQ | full text via InfoQ | ~385 words

AWS has outlined how the latest Model Context Protocol (MCP) specification changes remote MCP server deployments by removing protocol-level sessions and allowing requests to reach any available server instance. The change eliminates the protocol requirement for sticky sessions and shared session stores, simplifying horizontal scaling while shifting state management and other responsibilities to surrounding infrastructure.
The updated MCP specification removes the initialize and initialized handshake and the Mcp-Session-Id header. Requests can therefore be routed independently to any server instance behind a conventional load balancer. The specification also introduces an optional server/discover operation for clients that need server capabilities before making tool calls.
AWS diagram showing how MCP changes map to the Well-Architected Agentic AI Lens. Source: AWS Architecture Blog.
For AWS deployments, this can eliminate infrastructure used specifically to maintain MCP protocol sessions. AWS Architecture Blog authors Anand Komandooru, Steven DeVries, and Haleh Najafzadeh describe replacing session-affine routing with conventional request routing and removing session storage used solely for MCP protocol state. They also identify AWS Lambda as a deployment option that fits the request-response model because the protocol no longer requires persistent session connections.
The distinction between protocol and application state has also emerged in community discussion. Michael Madsen, writing about the specification on LinkedIn, summarized the change as:
The protocol is stateless. Your application doesn't have to be.
MRTR replaces server-initiated requests that previously required held-open streams, allowing multi-step interactions through `input_required` responses and subsequent requests. New `Mcp-Method` and `Mcp-Name` headers enable gateway routing and throttling, while W3C Trace Context supports distributed tracing. ttlMs and cacheScope provide caching controls.
AWS maps these changes to its Well-Architected guidance for agentic AI, covering monitoring, tracing, security, and tool integration. Stream resumability has also been removed, so clients may need to retry interrupted operations, increasing the importance of idempotency for tool calls that produce side effects.
Early implementation work shows that existing infrastructure still requires a transition path. [...]

## [49] Vercel Labs Ships scriptc, a TypeScript-to-Native Compiler That Leaves the JavaScript Engine Behind
InfoQ | full text via InfoQ | ~587 words

Vercel Labs has released scriptc, an experimental Apache 2.0 licensed compiler that turns ordinary TypeScript into small native executables with no Node, V8 and no JavaScript engine in the binary.
The repository was created on 22 July 2026 and has since gathered around 4.9k stars. scriptc uses the real TypeScript compiler for parsing and type checking, lowers programs to a typed IR, then emits readable C, LLVM IR, assembly, objects, native executables or WebAssembly via WASI Preview 1.
Every construct lands in one of three tiers: compiled statically by default, run dynamically inside an embedded quickjs-ng engine of roughly 620KB when --dynamic is passed for npm packages and any typed code, or rejected at compile time with an SC code and a rewrite hint.
A benchmark of scriptc 0.0.16 against Bun 1.3.12 and Node 24.18.0 recorded median CLI startup of 1.78ms versus 21.29ms for Bun and 61.78ms for Node, with idle memory of 1.9MiB for a framework free node:http server. The same tests found Hono required --dynamic, pushing 62% of the server into QuickJS and cutting throughput to 18.4k requests per second against Bun's 70.5k.
On Hacker News, one developer reported their results running about 7.5 times slower than Node 24:
Looking at the byte-array results (best case): scriptc is about 7.5x slower than Node 24, even after Claude tried making some scriptc-specific optimizations. But the executable starts up 12x faster (1.5 ms vs 18.6 ms), uses 72x less memory (2.5 MiB vs 181 MiB), and is a single 370 KB executable with no runtime dependencies.
Filip Pizlo argued that using floats for all numbers and deferring integer inference skips "half the problem of fast JS", and that leaning on QuickJS is a poor fit for a performance project, since any is common enough that real programs will keep falling into the island.
Simon Willison noted that coding agents landed 918,000 lines in a single week, and also added that building small, fast binaries without writing C or Rust "seems like a valuable capability".
One developer found coverage produced hundreds of errors on every local project:
Despite the hate it is receiving, I thought lets test it at least, and tried it to any project that I have locally. For every single of them the coverage generates hundreds of errors and so it is basically useless. [...]

## [52] Turn your REST APIs into MCP tools with Google Cloud API Gateway
Google Developers Blog | full text via Google Developers Blog | ~758 words

Most enterprise capability sits behind REST APIs that agents cannot see. To make one callable by an agent today, teams typically stand up and operate a separate MCP server that re-implements the routing, authentication, and quota logic their gateway already handles. The Model Context Protocol (MCP) has become the standard way for agents to discover and invoke tools, and frameworks like the Agent Development Kit (ADK) and Gemini Enterprise speak it natively.
Google Cloud API Gateway now closes that gap. In Public Preview, API Gateway can act as a remote MCP server: annotate the OpenAPI spec you already deploy, deploy it, and your existing REST operations are available as agent-ready MCP tools — with no separate server to build, host, or maintain.
API Gateway is the lightweight on-ramp in Google Cloud's gateway lineup. If you have a service on Cloud Run and you want its API secured, managed, and exposed to agents in minutes, this is the fast path. For a full enterprise API and MCP platform — lifecycle management, advanced traffic policies, monetization — use Apigee. To govern what your agents call on the way out, including MCP servers like this one, use Agent Gateway. Model routing, which gives you one stable endpoint for outbound LLM calls, is the companion capability for the other direction of AI traffic.
API Gateway accepts standard MCP JSON-RPC requests on a single endpoint, transcodes each tools/call into the corresponding REST request, applies your existing policies, and translates the response back. Because the transcoded request is indistinguishable from a normal REST call, the JWT or API-key authentication, quota, and logging you already configured for that operation keep working unchanged — MCP and REST traffic share exactly one policy path, and a given operation draws on one quota allocation however it is invoked.
x-google-api-management.mcp, and customize or skip individual operations with x-google-mcp-tool. Each exposed operation needs a backend and a non-empty description.openapi: 3.0.4
info:
  title: Order Service
  version: 1.0.0
x-google-api-management:
  mcp: true                 # expose this spec's operations as MCP tools
  backends:
    orders-backend:
      address: https://orders-a1b2c3-uc.a.run.app
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderStatus
      description: Returns the current status, carrier, and ETA for an order. [...]

## [54] Introducing Support for Local AI Models in the Antigravity SDK
Google Developers Blog | full text via Google Developers Blog | ~714 words

Today, we’re announcing that the Antigravity SDK supports local workflows across a wide range of local models and execution options, featuring initial support for Gemma 4 26B A4B using Google AI Edge’s LiteRT.
The Antigravity SDK enables developers to build with the same agentic capabilities that power Google Antigravity. With this new support you can enable agentic assistance via local models completely offline. We’ve optimized this workflow for LiteRT and Gemma 4 26B, efficiently using the local GPU and RAM in order to further amplify what your local machine is capable of delivering!
Local model execution offers several advantages for agentic experiences:
Here is how you can get started: (We recommended a machine with >24GB VRAM or unified memory).
python3 -m venv .venv
source .venv/bin/activatepip install google-antigravity litert-lm
litert-lm import \
  --from-huggingface-repo=litert-community/gemma-4-26B-A4B-it-litert-lm \
  gemma-4-26B-A4B-it-gpu.litertlm \
  gemma4-26b
In your directory, create a file called agy_sample.py. Paste the following contents into it.
import asyncio
import os
from google.antigravity import Agent, LiteRTAgentConfig
from google.antigravity.hooks import policy
# UPDATE: Point to the locally downloaded model from the previous step (litert-lm import ...)
MODEL_PATH = os.path.expanduser("~/.litert-lm/models/gemma4-26b/model.litertlm")
async def main():
   print(f"Using local LiteRT model: {MODEL_PATH}. Please wait for local inference to complete. This could take several minutes.")
   config = LiteRTAgentConfig(model_path=MODEL_PATH).lightweight()
   async with Agent(config) as agent:
      response = await agent.chat("What files are in the current directory?")
      async for token in response:
         print(token, end="", flush=True)
if __name__ == "__main__":
   asyncio.run(main())
In many cases we see that an Architect-Builder pattern is a great way of combining cloud model scale with local model advantages. In the hybrid demo video below, built with the updated Antigravity SDK, a cloud architect (Gemini 3.8 Flash) acts as the planner and conductor, while a local swarm of Gemma 4 26B instances handles the heavy lifting entirely on-device. [...]

## [60] Bringing Your Muse to Life
TLDR AI | full text via TLDR AI | ~804 words

Bringing Your Muse to Life
Today, we’re introducing Muse Realtime Avatar, our state-of-the-art embodiment technology that turns Muse Realtime Voice into expressive, interactive avatars.
Conditioned on reference media, Muse Realtime Avatar brings any character into a live conversation. A photographic portrait responds through subtle expressions, while a full-body illustration gestures and shifts posture as it speaks. Animals and everyday objects become expressive without losing what makes them distinctive. Frame by frame, the avatar’s appearance and mannerisms remain coherent from one conversational turn to the next.
From Intelligence to Real-Time Presence
Muse Realtime Voice and Muse Realtime Avatar form a single streaming system connecting intelligence, voice, and embodiment. Muse Realtime Voice provides the conversational intelligence and produces a stream of speech tokens (VQs) carrying both what is said and how it’s delivered. An audio decoder turns those tokens into speech, while Muse Realtime Avatar consumes the same stream to generate the corresponding visual performance. Sharing this token stream keeps voice, lip motion, and expression synchronized.
Muse Realtime Avatar is an audio-driven, Diffusion Transformer conditioned on speech-token stream, reference media, and a rolling window of recent video latents. It generates video in short causal chunks. As each chunk completes, its newest generated latents become motion context for the next, carrying the avatar’s appearance and mannerisms forward while keeping the computation bounded, allowing the generation to continue for as long as the conversation does.
Real-Time Infinite Video Generation
Live streaming must solve two problems at once: generating video fast enough for real-time interaction and remaining visually consistent throughout the conversation without accumulating errors.
We begin with a high-quality bidirectional teacher and produce a causal student with a fixed-length KV cache through self-forcing and distribution matching distillation. Self-forcing allows the student to train on its own generated context and teaches it to resist drift as small errors accumulate over time, matching the conditions it encounters during inference.
The teacher uses 40 diffusion steps with three-way classifier-free guidance (CFG), requiring three model passes per step and totaling 120 model evaluations per chunk. [...]

## [70] A Decision-Only Judge Matches GPT-6 on Routine Evals for 0.36% of the Fee
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1077 words

A decision-only judge matches GPT-6 on routine evals for 0.36% of the fee
CMU tested TypeSafe JEV, a judge that returns only a verdict and label probabilities, against 16 LLM and reward-model judges. It lands within 3 points of GPT-6 on preference and factuality at 277x lower fees, fails badly on hard correctness, and its confidence score is good enough to route a cheap-first cascade.
For most LLM-as-a-judge work, you don’t need a frontier model writing out its reasoning. A Carnegie Mellon team compared TypeSafe JEV, a hosted judge that returns only a verdict plus label probabilities, against 16 generative and reward-model judges. On ordinary preference and evidence-grounded factuality it lands within 3 points of GPT-6 at 0.36% of the fee. On hard correctness checks it falls far behind. Its confidence score is reliable enough to tell you which case you’re in, so you can run it first and escalate only when it’s unsure.
- $0.044 per 1,000 judgments vs. $12.18 for GPT-6 (277x cheaper), and 0.152s median latency vs. 1.885s
- Preference (RewardBench): 92.2% vs. 93.5%. Factuality (HaluEval): 87.5% vs. 86.7%.
- Hard correctness (JudgeBench): 78.6% vs. 93.1%, a 14.6-point gap. Well-written wrong answers widen it to 19.8.
- Cascade: 99.6% of GPT-6’s accuracy at 47% of its fee, escalating 34% of items to GPT-6
- When JEV reports probability 1.0, it’s right 99.1% of the time (322 items)
TL;DR: what is JEV?
Jev is the first public model from TypeSafe AI, released in early access this month. TypeSafe calls it a “System One model,” after Kahneman’s fast, intuitive System 1 thinking. It isn’t a chatbot: you give it structured input, instructions, and an output type (a choice among labels, a yes/no, or a score on a rubric), and it returns a typed value with calibrated probabilities and a confidence score. No text, no explanation.
Instead of generating token by token like an LLM, Jev produces its whole output in one parallel pass. TypeSafe claims 70 to 500ms responses and prices it at $0.042 per million input tokens, with output free. It pitches Jev for workflow logic, large-scale data processing, real-time loops, and guardrailing LLM outputs. Judging is one of those uses, and this paper is a third-party test of it.
Where the cheap judge holds up, and where it breaks
The study ran JEV 1.13 against 13 hosted judges (GPT-4.1 mini through GPT-6 Astra, Claude Sonnet 5, Gemini 3 Flash and 3.1 Pro, several Qwen models) and 4 local ones (including PairRM and Skywork-Reward-V2). [...]

## [133] Anthropic to pay Akamai $11.6 billion over seven years in cloud deal
TechCrunch | full text via TechCrunch | ~466 words

Anthropic will spend $11.6 billion over seven years on Akamai’s cloud infrastructure, Akamai said Thursday. That’s more than six times the size of a $1.8 billion deal between the two companies that Bloomberg reported in May. The commitment isn’t ironclad; according to Akamai’s securities filing, it depends on Akamai meeting certain delivery and service-availability requirements, and either company can end the agreement under certain conditions.
The deal is the largest in Akamai’s history and continues Anthropic’s compute gobbling-streak. It also represents a bet on a less-hyped corner of AI infrastructure: CPUs. Demand for CPUs, the general-purpose chips that handle work like running code and browsing the web, has grown as AI agents take on more tasks, though Akamai didn’t say what Anthropic will use them for.
Akamai won’t see revenue from the deal this year. On an investor call Thursday, executives said they expect $150 million to $300 million in 2027, starting in the second half, with revenue reaching an annual pace of about $1.7 billion by the end of 2028.
To build out the capacity, Akamai expects to spend about $5.5 billion. It is also adding about $1.7 billion to this year’s capital spending to buy components such as memory in advance.
As part of the deal, Akamai issued Anthropic a warrant, essentially the right to buy shares at a set price, for nonvoting preferred stock convertible into 7.7 million common shares, or up to about 5% of the company’s outstanding stock, at $111.33 a share. About 2% is expected to vest, or become available to Anthropic once it makes its first payment under the deal. The rest is tied to Anthropic spending more. Each additional $3 billion it commits to Akamai’s cloud services unlocks roughly another 1%, so the deal could grow by as much as $9 billion, to about $20 billion in total.
It’s the first time Akamai has attached a warrant to a cloud deal, and the contract is the largest in company history, Bloomberg reported.
The warrant flips the more common pattern in circular AI deals, in which suppliers — chipmakers and cloud providers — invest directly in the AI labs that buy their products. Here, the supplier is instead giving its customer a potential stake, one that grows as Anthropic’s spending with Akamai does. AMD used a similar structure with OpenAI last year, tying warrants to chip-purchase milestones.
Anthropic is no stranger to such arrangements. [...]

## [22] Tesla workers balk at training Optimus humanoid robots as replacements
Ars Technica | full text via Ars Technica | ~357 words

Tesla’s pivot from making electric cars to humanoid robots is facing challenges because of complex robot hands and disgruntled employees pushing back against training their robotic replacements. The struggle to scale up production comes as Tesla CEO Elon Musk has bet the company’s future on AI and robotics.
As someone who frequently makes claims that fail to materialize, Musk has described the Optimus humanoid robot as potentially “the biggest product ever” during Tesla’s second-quarter 2026 earnings call. But he also acknowledged that making an autonomous humanoid robot capable of handling many different tasks is “one of the hardest things to solve”—and now extensive reporting by The Information has revealed multiple complications that Tesla is trying to tackle while developing general-purpose robots and scaling up for mass production.
Tesla’s Fremont factory in California has already stopped making the Model S sedan and Model X SUV as of May 2026, with the company switching both line workers and engineers over to working on Optimus, according to The Information.
But the newest version of Optimus, called Optimus V3, has proven challenging from a development and manufacturing standpoint. The Information’s reporting describes troubles with getting production line equipment to precisely line up components, along with limitations in running the production line too fast. Tesla has reportedly scaled up production to hundreds of robots per week—but the company is targeting production numbers surpassing 1,000 robots per week by the end of 2026.
The automotive industry and other industries have already been using specialized industrial robots, such as robotic arms, for decades. Tesla and many other automakers and robotics companies are betting that humanoid robots coupled with advances in AI models could eventually unlock general-purpose robots that can handle a diverse array of tasks while fitting more seamlessly into human workplaces.
Hardware and AI challenges
It’s no secret that making robotic hands capable of doing delicate manipulation tasks on par with human hands is a huge engineering challenge. The complexity of such robotic hands has translated into more production headaches for Tesla as human workers must manually assemble Optimus hands and forearms that together have more than 100 small components such as screws.

## [25] AI was supposed to hit new grads hard. So far, unemployment data says otherwise.
Ars Technica | full text via Ars Technica | ~404 words

Last month, we shared word of a Stanford University study that found entry-level employment in so-called “AI-impacted” occupations lagging well behind that in other fields. Now, a new working paper from economics researchers at Munich’s CESifo finds the opposite, arguing point blank that “there is no evidence of any significant, widespread displacement or reduction in hiring of recent college graduates in absolute or relative levels.”
In “The Early Impacts of AI on Employment Among Recent College Graduates,” researchers Robert Fairlie and Jane Wu said they decided to focus on recent graduates “because changes in labor demand may first appear through reductions in hiring.” As AI gets good enough to at least perform the “relatively standardized tasks” in many entry-level office jobs, they argue, firms could reduce new hiring for simpler roles rather than laying off more experienced long-term employees.
There’s some reason to believe 2026’s graduating job seekers might be more at risk of AI displacement than those graduating just a year or two prior. The CESifo researchers point to a recent sharp increase in the number of firms “replacing a large number of employee tasks with AI” in a Census survey, as well as broad increases in AI spending per employee and ChatGPT Enterprise token use in the last 12 months.
Anecdotally, some major names also think that this is the year AI is finally capable enough to start replacing the jobs of some recent graduates. Venture capitalist Marc Andreessen said earlier this year that “AI literally until December [2025] was not actually good enough to do any of the jobs that they’re actually cutting.” And BlackRock CEO Larry Fink said in March that “the speed at which AI is changing” led him to worry that “when this year’s college graduates enter the workforce, we could see the highest unemployment rate among them in years—even without a recession.”
Nothing to see here (yet)
To determine if those kinds of worries were valid, the CESifo researchers looked at detailed microdata from the US Census’ Current Population Survey to determine unemployment trends among recent college graduates (i.e., Bachelor’s degree recipients 22 to 25 years old who aren’t pursuing higher degrees). [...]

## [29] Microsoft stops insisting you need a "Copilot+ PC"
Ars Technica | full text via Ars Technica | ~309 words

Since 2024, Microsoft has tried to sell “Copilot+ PC.” The marketing initiative was aimed at making it easy for people to know which Windows systems were approved to run AI-accelerated workloads locally.
But Copilot+ PC branding is nowhere to be found on the new Surface PCs Microsoft announced this week.
Speaking with Windows Central, Brett Ostrum, corporate VP of Surface, said that the new Surface computers “are not called Copilot+ PCs” despite meeting the label’s requirements.
“They do meet all the requirements of our previous bar for what Copilot+ devices are. We still lean into the narrative around AI on the edge and being able to have a hybrid solution out there,” he said.
Copilot+ PCs require 16GB of RAM, 256GB of storage, and an integrated neural processing unit (NPU) with performance rated at 40 trillion operations per second (TOPS) or better.
The Surface Pro 12-inch (2nd Edition) and Surface Laptop 13-inch (2nd Edition), coming out on October 13, both run Qualcomm Snapdragon X2 Plus processors and have a Qualcomm Hexagon NPU rated at 80 TOPS.
“[T]he purpose for Copilot+ PCs was to be able to deliver [NPU] experience,” Kedar Kondap, SVP of compute at Qualcomm, told Windows Central. “So, it was to define a certain category of devices with a certain bar and metric, like, for example, a 45 TOPS NPU. … So from that perspective, it’s more offering the same experiences, probably without just using [Copilot+ PC] terminology now.”
AI PCs are old news
Copilot+ PCs are “a class of AI PCs and laptops” that represent “the fastest, most intelligent Windows PCs ever,” according to a Microsoft marketing page that was up as recently as May, per Internet Archive’s Wayback Machine. That Copilot+ PCs landing page, however, now redirects to a page for “performance PCs” that still names “Copilot+ PCs” but features the label far less prominently.

## [42] From Agent Authorization to AI Production Evaluation: QCon AI New York 2026
InfoQ | full text via InfoQ | ~914 words

QCon AI New York has confirmed 23 of more than 30 sessions, with newly published talks examining identity and authorization for autonomous agents, guardrails for an operations agent running against large-scale Kubernetes infrastructure, shared model-serving platforms, and the evaluation of AI decision systems after deployment.
The conference will take place on December 15–16, 2026, at The Westin Jersey City Newport. Its program is intended for senior engineers, architects, and technical leaders working on AI systems in production.
According to QCon AI New York Conference Chair Hien Luu, the program reflects a broader change in the engineering work surrounding AI systems:
"Across this year’s program, one shift is unmistakable: AI engineering has become systems engineering.
As AI systems become more capable and autonomous, the engineering challenge is shifting from model behavior to system behavior. That means giving agents bounded execution authority, managing context and state, and wrapping probabilistic models in deterministic control planes.
Harness engineering, continuous evaluation, observability, and policy enforcement are becoming core infrastructure. At the same time, inference economics such as latency, token usage, model routing, and cost are now first-class architectural constraints, not implementation details."
Hien added that the emerging discipline increasingly draws on distributed systems, security, platform engineering, and site reliability engineering, with the goal of making AI systems reliable, observable, controllable, and economical to operate.
Identity and Delegated Authority for Agents
In the keynote When Software Becomes a User: Identity and Authorization for Agents in Production, Nancy Wang, CTO at 1Password, will examine how established identity and authorization models change when software agents become active users of production systems.
Traditional identity systems generally assume one human principal, a stable role, a bounded session, and a person who can be held accountable afterward. Agents may instead act for multiple users, invoke tools that were not enumerated in advance, create subagents, and continue operating without direct supervision.
The keynote will cover delegated authority across chains of agents, auditability across multi-hop tool calls, and techniques for giving an agent enough access to complete a task without placing the underlying credentials or secrets into its context. [...]

## [67] Anthropic tested what happens when agents bargain for people
TLDR AI | full text via TLDR AI | ~6421 words

Summary
- To see what works and what breaks when agents are sent into a market, we made a miniature market of Claudes—a more controlled sequel to Project Deal, our first experiment with agents interacting in a marketplace on people's behalf. Anthropic employees across six offices brought in a book they wanted to give away. Each participant had a short chat with Claude about what they like to read, and sent a Claude-powered agent onto an open trading floor to pitch, haggle, and strike deals with other people’s agents. The goal was for everyone to take home a summer read they would enjoy.
- Participants also ranked 10 books based on their interests so we could score how well their agent represented them. From a five-minute chat, an agent’s ranking of the books matched its person's on 61% of pairs, which is surprisingly good for such a short conversation.
- Once on the trading floor, the agents traded well. The market fell short mostly because of the information agents lacked about their participants, rather than because of how they traded.
- We then re-ran every trading floor dozens of times, changing the models used and the agents’ instructions. We found that the model an agent ran on made more of a difference to its negotiating outcomes than the instructions we gave it. Markets with stronger models were more efficient.
- Most people who read their book liked it, and the average participant said they would hand Claude about a third of their yearly book budget to spend.
Why we did this
Life is full of deals and trades that would leave everyone better off, yet never happen. This is often simply because it takes too much work to find the right counterparty and negotiate until a deal is struck. Think of the patient who skips a treatment after one quote they can’t afford, when there’s a different clinic that charges far less, or the hospital that quoted them would have cut its bill if asked. Or think about your job. Somewhere there might be one that would suit you better, with an employer who would be glad to hire you. But you may not find each other, because neither of you has the time to be searching constantly. There are smaller, everyday deals that go overlooked too—shift-swapping in a workplace, coordinating carpools, or trading school pick-ups. [...]

## [75] Note on 24th September 2026
Simon Willison's Blog | full text via Simon Willison's Blog | ~92 words

24th September 2026
The more time I spend working with coding agents, the more convinced I am that they make software engineering even harder.
We can do amazing things with them, but unlocking their full potential requires extraordinary discipline and knowledge.
Recent articles
- Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war - 22nd September 2026
- Jev introduces a new shape of LLM - System One, aka Decision Models - 21st September 2026
- Generating running routes with GPT-6 Astra and ChatGPT Work - 12th September 2026

## [147] Microsoft’s new Copilot agents get their own email, calendar — and a place in the org chart
The New Stack | full text via The New Stack | ~1059 words

Microsoft’s new Copilot agents get their own email, calendar — and a place in the org chart
Microsoft announced what it calls its biggest Copilot update to date on Friday, with CEO Satya Nadella describing Copilot as “a new OS for work.”
Nadella framed Copilot as spanning every model, form factor, and task, and the update puts Autopilot, which Nadella called a “proactive and long-running agent built for the enterprise,” at the top of his list of the update’s four components. The pitch targets office workers, but the more consequential change for developers is the infrastructure underneath.
Microsoft is moving the agent runtime into the enterprise infrastructure layer and building persistent identity, state, execution boundaries, and organizational context into Microsoft 365, which means teams building production agents no longer have to assemble those pieces around a model on their own.
The release adds a new Home experience that merges Chat and Cowork in the Copilot app, but the bigger changes for developers come from Code and Autopilot. Code generates apps, dashboards, and workflows from natural language, and Autopilot turns the agent Microsoft previously called Scout into a persistent background worker. Home and Code are rolling out first through Microsoft’s Frontier early-access program, and Autopilot is expanding to a private preview at month’s end.
Microsoft is moving the agent runtime into the enterprise infrastructure layer and building persistent identity, state, execution boundaries, and organizational context into Microsoft 365
Agents that don’t need prompts
Autopilot takes a role and goal from the person who sets it up, then continues working in the background without requiring a new prompt for each step. Each Autopilot gets its own governed Entra identity and agent user account, separating the agent’s permissions and activity from those of the person who created it.
For engineers, that moves much of the operational scaffolding required for long-running agents into Microsoft’s infrastructure. Independent vendors have been building dedicated layers for that problem; Diagrid, for example, adds durable recovery to LangGraph and other agent frameworks, while Microsoft is bringing those capabilities inside the Microsoft 365 environment.
An identity for every agent
The identity model is the piece developers building on Microsoft Foundry will feel first. [...]

## [165] Microsoft’s new Copilot app puts everything in one place – but the price is ‘evolving’
ZDNet | full text via ZDNet | ~1188 words

ZDNET’s key takeaways
- Microsoft now has a single Copilot client for consumers and business.
- Today’s new Copilot client release adds Code and Autopilot tabs.
- The cost model is “evolving,” with usage-based billing for key features.
For the past few years, Microsoft’s Copilot client lineup has been a fragmented mess, with its consumer chatbot and its enterprise-focused AI tools sharing a brand name while sporting wildly different interfaces and feature sets.
Also: Nearly 70% of workers use AI regularly now – but many get no time to upskill
Last month, the company began rolling out a single app designed to serve both groups, starting with mobile platforms and now targeting desktop environments. Starting today, that unified app, called simply Copilot, is getting a major upgrade.
More from ZDNET
Make no mistake: the new Copilot was engineered for Microsoft’s enterprise customers, not for consumers. Its feature set is geared for organizations that are already heavily invested in the entire Microsoft 365 ecosystem, centered on Outlook, Teams, and documents created using Word, Excel, and PowerPoint. They also want those AI tools to work on company data in a secure environment they control, without the risk of sending it off to someone else’s cloud.
In pre-recorded remarks at a small launch event for key customers, Copilot Executive VP Jacob Andreou argued that Microsoft’s consumer base is “a little bit special.” He pointed out that roughly 90 million customers pay for Microsoft 365 out of their own pockets: “These folks don’t want some kind of dumbed-down consumer product; they want the full power that we offer to enterprise users, but in the context of their personal life.”
Also: Businesses finally seeing AI ROI, but 62% can’t handle the storage demands
And the user experience isn’t the only thing that’s different about the new Copilot. “In the last few months,” Andreou noted, “Copilot has gotten actually really good. It’s faster, it’s more capable, it’s more coherent and unified than ever before. … And users have really noticed.”
(I haven’t had any hands-on experience with these new apps. As always, what’s delivered might not live up to the promises in today’s announcements.)
Here’s what Microsoft says consumers and enterprise customers will be seeing, starting today.
What’s in the new Copilot app?
The new Copilot sports a design with three tabs: Home, Code, and Autopilot. The user interface is the same, whether you sign in with a personal or work account. [...]

## [191] AI agent kill switch urged by Okta-led alliance – how businesses could make it work
ZDNet | full text via ZDNet | ~2324 words

ZDNET’s key takeaways
- Okta, AWS, Google Cloud, Salesforce, and others form an AI agent security coalition.
- The Alliance offers a blueprint for companies seeking visibility, control, and governance of agents.
- AI agents need the equivalent of a kill switch to expeditiously terminate suspicious behavior.
When a swarm of AI agents, many autonomously provisioned by other poorly governed AI agents, escaped OpenAI’s labs and stole information from servers belonging to another company (Hugging Face), many experts viewed the incident as a major tipping point in cybersecurity and AI cyber capabilities. (To what extent are models now resourceful enough to engage in self-directed harm?)
OpenAI referred to the incident as “unprecedented.” It was the first AI-directed attack of its nature to go viral across mainstream headlines, and it wasn’t long before reports of other agents-gone-wild made headlines as well. The most recent of these reports involved three companies that were inadvertently attacked by Google Gemini agents.
Also: Who’s responsible for catching rogue AI agents? You are
More from ZDNET
Significant controversy has ensued.
In one corner are the inventors of AI themselves, saying that the time has come to take a breather from AI innovation in order to get the technology under control. You’d think they should know. For example, OpenAI sounded the alarm that a swarm of potentially malicious AI agents is only months away from wreaking havoc.
In the opposite corner is US President Trump posting to his Truth Social network that “AI taking over the World, destroying Humanity, and all other things bad, is a HOAX.”
In between are all the businesses and consumers getting whipsawed between the two points of view and trying to figure out what to do next.
(Disclosure: Ziff Davis, ZDNET’s parent company, filed an April 2025 lawsuit against OpenAI, alleging it infringed Ziff Davis copyrights in training and operating its AI systems.)
Also: ‘Sophisticated’ AI swarm attacks are months away, OpenAI warns
Two big questions are arising out of this conversation. First, what can be done over the short and long term to get the technology under control? [...]
