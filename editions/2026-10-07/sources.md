# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Mistral Large 4
Hacker News | full text via Simon Willison's Blog | ~211 words

6th October 2026 - Link Blog
Introducing Mistral Large 4: Le chonk (via) Mistral are back in the game. Today they're releasing a preview of Mistral Large 4, a 1 trillion parameter, 49 billion active parameter model trained on their own cluster of 3,800 NVIDIA Grace Blackwell GPUs.
The preview is available via their API. They promise to release the open weights model at the "end of this month".
The model only supports two reasoning levels - "none" and "high" - via the Mistral API. Here are both pelicans - the "high" one looks better, though surprisingly it only used 2,717 output tokens compared to "none" which used 3,275:
On Artificial Analysis it scores 38, just behind DeepSeek 4.1 Flash, which is a 552B model. It's a huge improvement on last December's Mistral Large 3, which drew this terrible pelican and scored 9 on AA.
It's certainly not a Fable-class model, but it's great to see Mistral put out a model that's back to being maybe about 6 months behind the frontier.
Recent articles
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026
- 2026 in LLMs (so far) - 27th September 2026

## [8] Sharing AI progress in mathematics
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [6] EmbeddingGemma 2: An open, lightweight multimodal embedding model
Hacker News | full text via Hacker News | ~678 words

EmbeddingGemma 2: an open, lightweight multimodal embedding model
We introduced EmbeddingGemma last year to provide a lightweight option for high-quality text embeddings, to help your apps organize, search, and connect information directly on consumer hardware. The developer community’s response blew past our expectations. With more than 20 million downloads, builders have used it to power smarter on-device search tools and privacy-first retrieval augmented generation (RAG) pipelines.
Today, we’re launching EmbeddingGemma 2, expanding beyond text to unify code, images, video, and audio in a shared embedding space. Built on the Gemma 4 architecture and released under a commercially permissive Apache 2.0 license, EmbeddingGemma 2 has 740 million parameters, making it optimal for on-device inference. It can help find a specific video clip from a voice memo, or search through hours of audio recordings based on a text query, all processed by a single, natively multimodal model.
Built from the same technology as Gemini Embedding models, EmbeddingGemma 2 is:
- Best-in-class for its size: Achieves leading scores among sub-1B multimodal embedders for its size across benchmarks like MTEB (Massive Text Embedding Benchmark) Code and MAEB (Massive Audio Embedding Benchmark), while matching or outperforming many larger models across text, vision, and audio tasks.
- Modular by design: Requires as little as 270M parameters for text-only workloads with optional vision (170M) and audio (300M) encoders for full multimodal support.
- Storage-efficient: Using Matryoshka Representation Learning (MRL), developers can dynamically truncate output vectors from 768 dimensions down to 512, 256, or 128 dimensions. This provides up to 6x storage reduction for local vector databases and memory usage.
- Optimized for on-device performance: Runs efficiently within tight resource constraints. With quantization, on a Google Pixel 11 Pro, EmbeddingGemma 2 requires as little as ~191MB active RAM for text-only weights and ~567MB for the full multimodal model.
- Extended context ready: Features an 8K token context window (4x larger than EmbeddingGemma 1), allowing it to process up to 5.5 minutes of audio, 29 images, 58 video frames, or interleaved combinations thereof directly on local hardware. [...]

## [9] OpenTPU – An open-source AI accelerator, developed by AI
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [34] Hackers obtain counterfeit TLS certificates for Google and other large services
Ars Technica | full text via Ars Technica | ~304 words

Attackers hijacked three top-level domains and used their control to mint counterfeit TLS certificates for Google and other large organizations, Google said Tuesday.
The attackers launched a series of attacks on the .gh, .sl, and .as country code top-level domains (ccTLDs) and then modified authoritative DNS records for selected domains within those namespaces. By controlling those DNS records, the attackers were able to pass automated domain control validation checks and obtain unauthorized certificates for “several Google domains” and “several leading global brands and widely used online services.” Google said it updated Chrome to block all certificates it identified as unauthorized, and worked with the issuing certification authorities to ensure the unauthorized certificates for Google properties were revoked.
Certificate issuance: The weak link in the chain
TLS certificates are the cryptographic credentials that underpin authentication and encryption protections for websites, mail servers, and other Internet infrastructure. These x.509 certificates use a digital signature to bind a domain name such as google.com to a public key. The public key is publicly available, while the private key is held only by the website operator. When a connection shows that the keys match, the visiting party knows it’s connected to the authentic site rather than an impostor. Possession of unauthorized certificates allows attackers to cryptographically impersonate the affected infrastructure.
Google didn’t identify the affected domains it owns or name any of the other organizations whose domains were affected. While noting that Chrome users do not need to take any action to be protected, Google cautioned domain owners not to rely solely on browser-side interventions to protect their users. The company is advising domain owners to monitor certificate transparency logs for unexpected certificate issuance across their domains and to publish restrictive Certification Authority Authorization DNS records to prevent attackers from reusing cached validation data after DNS control is restored.

## [27] OpenAI will watermark ChatGPT outputs by default—but only in the EU
Ars Technica | full text via Ars Technica | ~222 words

OpenAI will begin automatically watermarking text generated with ChatGPT in the European Union, the company has announced. It will also offer the watermarking feature in other regions, but it will be off by default outside of the EU.
The move in Europe is driven by a need to comply with the EU AI Act, which took effect in August. It requires marking content produced by AI models in a way that another tool can detect. Unfortunately, there is still no completely effective and reliable way to do that. A few standards already exist, like SynthID and the C2PA project, but they are relatively easy to circumvent for anyone with basic know-how.
The same is likely true for OpenAI’s watermark. Its method is proprietary; the company calls it textGrain, and has published a technical paper explaining how it works. But in general, it works like other LLM watermarking tools we’ve seen in the past: It puts patterns in the word choices that are not clear to a human reader, and that don’t meaningfully change the general quality of the output, but that someone with a key can use a specialized detector to find. OpenAI says it will be giving access to the detector to a limited number of researchers and organizations, and providing a request-for-approval process for others to be added over time.

## [28] Building Git infrastructure for agent-scale development
GitHub Blog | full text via GitHub Blog | ~1169 words

Brian Celenza
Brian is a Principal Software Engineer working on the storage and core services that power all repository interactions on GitHub.
We’re rebuilding GitHub’s Git infrastructure while GitHub keeps running, creating a foundation for agent-scale software development.
Every day on GitHub, millions of developers build the products their customers rely on, contribute to open source, and pursue personal projects. GitHub’s architecture has changed steadily over the years to support that work and the growing demands of the developers and organizations who depend on it.
Agentic software development is driving the next architectural shift. With developers and agents working concurrently in repositories that receive millions of commits a day, these workloads demand a different Git architecture. We’re rebuilding GitHub’s Git infrastructure to support them. This post explores the demands shaping that work and the design principles behind it.
Today’s highest-volume workloads show the scale we’re building for. The gap between a typical repository and the busiest ones is wider than most people expect. Here’s a rough picture of the monthly repository activity distribution on GitHub from August 2026:
Repository activity climbs sharply at the far end of the distribution. The busiest repository on GitHub saw roughly a billion requests in August.
Beyond these highest-volume workloads, total Git activity on GitHub is also growing rapidly: between September 2025 and August 2026, it increased to more than 2x its previous level, from 218.2 billion events per month to 473.3 billion.
In September alone, developers and agents made 7.38 billion commits on GitHub, more than five times as many as a year earlier.
The repositories at the top of this curve show what agentic development looks like at its leading edge: large engineering teams running busy CI pipelines alongside growing fleets of agents. Supporting these teams means building Git infrastructure for sustained, concurrent reads and writes at a scale few repositories reach today. We’re investing deeply in Git infrastructure to meet the demands of agentic software development and give teams a foundation built for their most ambitious workloads.
Building for this scale means addressing several architectural challenges:
This is why fast clones only solve part of the problem. Reads are relatively easy to scale: add caches, add replicas, and serve the same bytes to more clients. [...]

## [99] OpenAI in $30 Billion Round Talks With UAE Funds, BlackRock
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~70 words

OpenAI is in talks with multiple investment funds from the United Arab Emirates to help anchor a $30 billion round of financing. The UAE funds have discussed forming a syndicate to invest as much as $10 billion in the round. The University of California's endowment fund, BlackRock, Thrive Capital, and Andreessen Horowitz may also participate in the round alongside that syndicate. The fundraise is ongoing, and the details could change.

## [101] OpenAI's B2B Marketplace: The Hyperscaler Of AI Apps
TLDR AI | full text via TLDR AI | ~992 words

OpenAI announced its own Muse/Instinct competitor Dots, new models, team environments, and lots more at Dev Day last week.
The announcement that’s flown relatively under the radar is its B2B marketplace.
OpenAI Marketplace launched at DevDay on 29 Sep 2026 with 32 partners. Eligible enterprise customers can put part of an existing OpenAI commitment toward those products.
The full set is:
The most notable partner on this list is Baseten, given what it implies.
From the announcement:
OpenAI enterprise customers can now use existing OpenAI commitments for open models served by Baseten within Codex or via the Responses API. For enterprises, this means delivering even more intelligence per dollar through your existing OpenAI commitment.
Agentic coding is currently the most widely-adopted AI use case, and OpenAI’s Codex and GPT models are two of the most popular choices for scaling code generation workflows. With open models powered by Baseten now available to OpenAI customers, organizations can optimize agentic workflows across open and closed models and route each task to the best-fit model.
A lot has been said about open models eclipsing closed models on token volumes over the summer and the role this has played in a delay in Anthropic’s IPO.
If we use Vercel’s gateway as a proxy:
The first nuance that’s widely acknowledged is that although open weight token volumes have surpassed closed, spend and requests remain higher for closed models and the delta in token volumes is attributable to the higher token consumption of open models for the same tasks.
Ramp’s AI Index underlined this further - 5% of business spend going to open weight models.
This is a function of many reasons, but a clear recent development is how aggressively OpenAI and Anthropic are price-cutting to retain market share.
The Marketplace is another move consistent with this strategy, but the ambition is bigger.
OpenAI wants to position itself as the platform that the wider AI ecosystem is built on and relies on for distribution, just like hyperscalers became the distribution platform for enterprise software in the SaaS era.
Here are the similarities between OpenAI’s marketplace and the cloud ecosystem:
The intended benefits for OpenAI and its customers are clear to see: consolidation of AI sprawl and easier budgeting. [...]

## [102] How Devin's Memory and Dreaming Work
TLDR AI | full text via TLDR AI | ~673 words

Today we’re introducing Memory and Dreaming in Devin.
Memory lets Devin carry useful learnings about the way you like to work across sessions: your preferences, corrections you’ve made, and lessons learned about your projects and workflows.
Dreaming is a daily asynchronous process that improves the index of Devin’s memories about you. Memories generated during your sessions are deduplicated, linked to relevant sessions and artifacts, and new knowledge emerges.
You can browse Devin’s memories under Customize → Memory, and inspect recent dreaming sessions. Memory is personal to you within each organization on devin.ai.
We have also open sourced the standard we used to build Devin’s memory system. We invite you to integrate it into your agents and contribute at cognition.ai/agent-memory-repo.
Learning as you work
Some of the most useful context only emerges once work is underway. You correct an assumption, explain why an approach won’t work in your current project, or clarify a personal preference. Other lessons come out of the work itself: an environment gotcha that took several attempts to get right, or a project decision that will matter again later.
Memory gives Devin a way to proactively retain these lessons beyond the session itself, without you having to pause the session to update a skill. It is personal to you, rather than becoming shared instructions for your organization. Memories are not summaries of sessions. They are lessons Devin learned from working with you, written as short notes with a link back to the session where they were learned.
Devin’s memory drive
Memories live in your personal Memory Drive, a persistent Git repository of markdown files. Notes can be organized by repository, project, or topic, while a short MEMORY.md holds general preferences and an index of the other files in the drive. At the start of a session, Devin receives MEMORY.md as context. From there, it can search and read relevant notes using the same tools it uses to navigate code, without loading the entire memory archive into its prompt.
Each session works with its own Git checkout of the drive. After editing a note, Devin commits its changes, merges updates from other sessions, and saves the result to your persistent memory drive. If another session saves an update while a sync is underway, a revision check rejects the stale write so Devin can retry against the newer version. Conflicting edits are surfaced for resolution rather than silently overwritten. [...]

## [104] Announcing d1 with vision
TLDR AI | full text via TLDR AI | ~431 words

Liquid AI on X: "Announcing d1 with vision. 👁️👁️ Our first decision model now supports images, text or both as inputs. We tested d1 against GPT-6.1 Sol and Claude Opus 5.5 on six real applications, from filtering support tickets to inspecting circuit boards. d1 matches or beats GPT-6.1 Sol on fou… / X
Liquid AI on X: "Announcing d1 with vision. 👁️👁️ Our first decision model now supports images, text or both as inputs. We tested d1 against GPT-6.1 Sol and Claude Opus 5.5 on six real applications, from filtering support tickets to inspecting circuit boards. d1 matches or beats GPT-6.1 Sol on four of them. It costs 19x to 200x less than both models and answers significantly faster on every task.
> probabilities for yes/no, choice, or score questions
> one forward pass, without generating tokens
> text decisions in 200 to 300 ms
> Liquid API: https://t.co/HxYWoaUnAU
🧵"
Announcing d1 with vision. 👁️👁️ Our first decision model now supports images, text or both as inputs. We tested d1 against GPT-6.1 Sol and Claude Opus 5.5 on six real applications, from filtering support tickets to inspecting circuit boards. d1 matches or beats GPT-6.1 Sol on four of them. It costs 19x to 200x less than both models and answers significantly faster on every task.
> probabilities for yes/no, choice, or score questions
> one forward pass, without generating tokens
> text decisions in 200 to 300 ms
> Liquid API: console.liquid.ai
🧵
Announcing d1 with vision. 👁️👁️ Our first decision model now supports images, text or both as inputs. We tested d1 against GPT-6.1 Sol and Claude Opus 5.5 on six real applications, from filtering support tickets to inspecting circuit boards. d1 matches or beats GPT-6.1 Sol on four of them. It costs 19x to 200x less than both models and answers significantly faster on every task.
> probabilities for yes/no, choice, or score questions
> one forward pass, without generating tokens
> text decisions in 200 to 300 ms
> Liquid API: console.liquid.ai
🧵
Vision lets d1 inspect parts directly from camera images. It is currently the best vision-enabled decision model on the market.
> 85% to 97% accuracy across four VisA inspection tasks
> circuit boards, candles, cashews, and chewing gum
> understands the task from a shortShow more
d1 can read game screens and pick the next move with improved performance.
> Tetris: adding the screen raises cleared lines from 70 to 81
> Wordle: solved 12/12 games in 3.8 guesses on average, reading the board from screenshots. [...]

## [105] Build an agent loop a small model can finish
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2019 words

Build an agent loop a small model can finish
We got a small, cheap coding agent to finish a job that looked too big for it. Then we built a second loop from scratch, on a job small enough to try yourself, to see which parts actually mattered.
An agent loop keeps a coding agent working on a task, one attempt after another, until something says it's done. The loop is the easy part. Most of the work goes into that "something": a check the agent can run by itself that says whether each attempt got closer.
If you've tried a Ralph loop or /goal, you've already seen the part where the agent keeps going. Geoffrey Huntley calls the other half "back pressure": tests, builds, type checks, and anything else that can reject a bad attempt. Neither of our jobs came with a test suite, so we had to build the back pressure ourselves.
The first job was fixing Figma and slide imports in Agent-Native, our free, open-source framework and collection of apps. One slide came through our importer so broken that 88% of its pixels didn't match the original. Over one weekend, one of OpenAI's smaller models got that down to 2%. Here's a walkthrough of that loop.
The first loop: fixing our imports
Our imports started out rough. People wanted to bring Figma files into Agent-Native Design and decks into Agent-Native Slides. Diagrams came apart into loose shapes. Icons disappeared. One slide came through as a black rectangle. So we looked at the results, described what was wrong, asked the agent for a fix, and looked again.
That loop could only move as fast as a person could look at slides, and the agent only knew what somebody remembered to tell it. We were the verifier, typing "still wrong, the heading moved again" into a chat over and over.
Turning "looks right" into a number
Comparing visuals feels like a judgment call. That's hard to write as a unit test or a browser test.
But every imported file already came with a right answer: the original. So we rendered the original and the converted version and compared them with a pixel diff.
A pixel diff compares two images and flags every pixel that differs. Tools like pixelmatch and ImageMagick's compare do this out of the box. Our check gave the agent two things: a number, and an image with the mismatches marked in red.
The number told the agent whether a change helped. The red overlay told it where to look next.
Checking the check
An agent working against a number will believe the number, so the number had to be right. [...]

## [106] How we built the fastest, cheapest browser agent with Jev
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~5072 words

How We Built the Fastest, Cheapest Browser Agent with Jev
IronBee Express runs a nine-action checkout in 6.7 seconds for $0.0005 in model cost. Here is what we ask Jev, what we show it, how it judges a run, and when we hand the wheel to an LLM.
The clip above is a real run at normal speed. IronBee Express signs in to our demo shop, buys an iPhone 15 Pro with an address and a card, and waits until the order page says COMPLETED. Nine actions, 6.7 seconds.
The decision engine, Jev, cost $0.00054 for that whole run. That includes the review at the end.
There is no LLM in that loop. Every step is one call to Jev, a model that picks from a list of options and gives a probability for each. It doesn't write text and it doesn't look at screenshots. That covers most of what a browser agent does, and a step takes about 300 ms.
Speed is the easy part to show. The part I care more about is this run of the same checkout:
  8 +5.34s ✓ CLICK [23] button "Place order — $ 311.10"  [p=0.98 decide 298ms act 1143ms]
  9 +6.80s ✗ DONE  [p=0.74 decide 323ms]  (the goal failed (p=0.83); the evidence shows GET /api/orders/131 → 200)
FAILED in 7.57s — 8 actions, 9 decisions
…
FAILED — the goal was not reached: notification-service: … Order #131 Could Not Be Processed. Reason: Insufficient inventory
The page said "Order placed successfully!". The order API answered 200, but the order inside it said FAILED. Express failed the run, pointed at that response, and then at the backend log that says why. Nobody wrote an assertion for any of it.
This post is about how we got there. What we ask Jev, what we show it, how it judges a run, how we replay a run without it, and when we hand the wheel to an LLM. Most of it is about things that broke. All numbers come from our own runs between September 21 and October 1, 2026.
Why a classifier
Jev picks. It never writes. Almost everything good about Express comes from that.
Jev is a model from TypeSafe that answers typed questions. You send it a state, which is any JSON you like, and a set of questions. Each question is a choice: a few options, each with a short description. Jev sends back the option it picked, a probability for every option, and a confidence. [...]

## [60] How Jump Trading is scaling quant research with ChatGPT
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

Jump Trading uses OpenAI to expand quantitative research. See how longer-running AI workflows combine multiple data sources with human review.

## [58] Why Telecom Operators Are Building Their AI Strategy on Open Models
NVIDIA Blog | full text via NVIDIA Blog | ~901 words

Telecom operators are increasingly building their AI strategies on open models — and the reasons go beyond mere cost.
Open models give telcos the ability to trust, control and customize AI across their most critical workloads — from autonomous networks to customer care.
NVIDIA’s latest State of AI in Telecommunications report reflects this shift, with 89% of respondents reporting that open source models and software are important to their company’s AI strategy.
For operators, the strategic value of open models is fivefold:
- They expand access to frontier‑level intelligence at lower cost, allowing operators to reserve closed models for the workloads where they drive the most value. Independent benchmarks such as the Artificial Analysis Intelligence Index v4.3.2 show that leading open models are becoming more competitive across demanding reasoning, coding, scientific and agentic workloads.
- They support telco‑specific customization, with open weights and training recipes that operators can fine‑tune for their own operations using network, customer and industry data.
- They enable trustworthy AI by giving telcos greater visibility into and control over model artifacts and behavior, so models can be evaluated, adapted and governed in alignment with regulations and business policies.
- They enable flexible, secure deployment: teams can size and optimize open models to run across public clouds, private infrastructure and edge environments.
- They unlock the opportunity for telcos to deliver locally adapted AI services to enterprise and government customers by hosting and fine-tuning open models.
Open Foundations, Tuned for Telecom Operations
The NVIDIA Nemotron family of open models provides frontier-level reasoning performance optimized for agentic workflows, as well as speech capabilities for voice applications, with open weights, training data and recipes.
SoftBank Corp. illustrates how an operator can use open models as a basis for developing and continuously advancing its telecom-specific AI capabilities.
“Open models allow SoftBank Corp. to build on the rapid progress of global foundation models while applying the network knowledge and operational expertise we have accumulated over many years,” said Rajeev Koodli, principal fellow of SoftBank Corp. and senior vice president of SB Telecom America. [...]

## [57] Scrimshaw Jukebox
Simon Willison's Blog | full text via Simon Willison's Blog | ~188 words

6th October 2026
I wanted to see if Claude Opus 5.5 could compose music, so I tried this:
I want you to write some computer game music for me. First design simple text based format for the music and build an artifact that can play it out loud - include some example tracks in that artifact
I am looking for music of the quality of the original secret of Monkey Island
It leaned a lot harder into the Monkey Island theme than I had intended, but the results are surprisingly good.
I wonder if the ability to compose competent music is similar to the 3D graphics thing - a new capability for text models that emerged in the past few months?
Would need some careful experiments with other recent and not-so-recent models to confirm if this is new or if they've been able to do this for a while.
Recent articles
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026
- 2026 in LLMs (so far) - 27th September 2026

## [98] Instinct in group chats
TLDR AI | full text via TLDR AI | ~298 words

Instinct in group chats
Starting today, early access users can add Instinct to group chats. A new Instinct joins and works for the whole group.
Making plans with friends usually turns into a frustrating back-and-forth over times and places. With Instinct in the group, you can explore options together, agree on a plan and get it done, all in one thread. Your friends don't even need Instinct to join in.
A few things it’s good at:
- Planning a weekend trip with friends, including dates and arrival times
- Coordinating logistics with a roommate
- Getting tickets as soon as they go on sale, then splitting the cost and sending one to everyone
- Running a fantasy league, keeping standings, settling rules disputes, and reminding everyone to set their lineups
- Sorting out carpool schedules - works out who’s driving each day from everyone’s schedules
- Organizing Thanksgiving, keeping track of who’s bringing what and ordering the shopping list
Group chats are new territory for Instinct, and we put a lot of care into getting the permissions right. Here’s how it works:
- Your personal Instinct asks before connecting with the group’s Instinct. You choose which groups to trust and can remove trust at any time.
- The group’s Instinct has no direct access to your personal accounts. Your Instinct checks your permissions before sharing information or taking action.
- If someone new joins the group, all pending replies from your Instinct are held until you grant it permission to share with the expanded group.
Group chats are available to all of our early access users, and will be rolling out to everyone soon. To join early access for this release, ask your Instinct to put you on the list.
Great work with @GajanNagaraj @anuda_w and @saagarwashere
00:00

## [108] TanStack Charts 1.0
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1529 words

TanStack Charts is already getting a 1.0, and I know that’s fast. I have other blog posts that talk about how and why that was possible, but I’d like to talk about why I’m so excited about TanStack Charts.
Getting a line on a screen has never really been the problem. There have been lots of charting libraries and utilities, big and small. I think the really interesting part is what happens down the road, after you build that line chart, as your product grows, your data visualization requirements grow, and your clients demand more detail.
We’d like to think that our charts are just one and done, or even that we could build a couple of chart types and they’ll be sufficient for everything we need. But the reality is that eventually you’ll probably need some bars underneath that line, or you’ll need to highlight a couple of points and throw in a couple of annotations. Oh, and then the tooltip will need to show something specific to your application, not just the chart.
None of this sounds super ambitious. You’re just building your app. I get it. But this is usually where I start finding out which choices a charting library has already made for me.
I’ve spent a lot of time in this space myself, adding wrappers and trying to figure out how far I can push something before I have to start over or build something completely custom. So when I say “charts you don’t have to outgrow,” that’s exactly what I’m talking about. I want you to get a chart working, but then be able to keep using that same system throughout the entire lifespan of that data visualization.
My charting history goes way back to when I was working on Nozzle, my last startup. We had tons of marketing and SEO data, and we needed really useful ways to look at it. I spent lots of time with D3. I even helped maintain and build Chart.js 2.0 alongside Everett Timberg. Then I eventually built react-charts because I wanted my charts to feel more like the way I was building the rest of my UI.
There were a ton of things I liked about each of these projects, and I learned a ton, probably more sometimes than the value I was actually contributing. I spent a lot of time learning about animation, geometry, trigonometry, and label rotation. A little too much about label rotation, because you would never have guessed, but “just figure out how much space that rotated label needs” is a pretty big request, especially when you’re doing everything by hand. [...]

## [59] OpenTelemetry Makes Kubernetes Attributes Processor Stable as Observability Schema Matures
InfoQ | full text via InfoQ | ~663 words

OpenTelemetry has promoted its Kubernetes Attributes Processor to v1.0.0, marking a significant step in making Kubernetes telemetry more predictable and stable across observability pipelines. The processor enriches logs, metrics, and traces with Kubernetes metadata, and its graduation means the component now meets OpenTelemetry's stability requirements around testing, benchmarking, documentation, and telemetry. It also provides API stability for organisations redistributing the processor as part of their own Collector distributions or binaries.
The milestone is important because the Kubernetes Attributes Processor sits at a key point in many OpenTelemetry deployments. It discovers Kubernetes resources and associates telemetry with metadata such as pods, namespaces, nodes, and workloads, turning otherwise generic telemetry into data that can be queried and correlated by Kubernetes context. The processor is currently stable for logs, metrics, and traces, although profiles remain under development.
The move to v1.0.0 is not entirely backwards compatible. The processor's stable release adopts the newer OpenTelemetry Kubernetes semantic conventions, which themselves reached stable status in Semantic Conventions v1.42.0 in June 2026. OpenTelemetry says this required close coordination between the Collector and Kubernetes Semantic Conventions SIGs because stabilising the processor also required stabilising the conventions on which its telemetry depends.
Several attribute names therefore change. For example, container.image.tag becomes container.image.tags, while Kubernetes label and annotation attributes move from plural forms such as k8s.pod.labels and k8s.pod.annotations to k8s.pod.label and k8s.pod.annotation. Equivalent changes apply to node and namespace labels and annotations.
That makes the migration more significant for observability teams than simply changing a Collector component version. Dashboards, alerts, recording rules, queries, data pipelines and downstream integrations that reference the older attribute names may need to be updated. OpenTelemetry provides feature gates that allow the old and new conventions to be emitted during the migration period, giving users a way to transition before relying exclusively on the stable schema.
The processor's graduation forms part of OpenTelemetry's broader "Stable by Default" work. [...]

## [46] The Shift to cgroup v2 in Kubernetes: What You Need to Know
Kubernetes Blog | full text via Kubernetes Blog | ~2364 words

The Shift to cgroup v2 in Kubernetes: What You Need to Know
In Linux, cgroups (control groups) are a kernel feature used for managing system resources. Kubernetes uses cgroups to allocate resources like CPU and memory to containers, ensuring that applications run smoothly without interfering with each other. With the release of Kubernetes v1.31, support for v1 cgroup management moved into maintenance mode. Support for v2 cgroup management has been stable since Kubernetes v1.25.
Compared with cgroup v1, cgroup v2 provides a single unified hierarchy, a more consistent interface, and a stronger foundation for resource isolation and modern resource-management features.
Deprecation of cgroup v1
Kubernetes has deprecated cgroup v1.
Starting with Kubernetes v1.35, failCgroupV1 defaults to true, so the kubelet does not start
on a cgroup v1 node by default. Administrators can temporarily set failCgroupV1: false in the
kubelet configuration file, but removal will
follow the Kubernetes deprecation policy.
Further removal work is tracked in KEP-5573: Remove cgroup v1 support.
If you are still on a release older than v1.35, migrate every Linux node to
cgroup v2 before upgrading, or plan to set the temporary failCgroupV1: false
override. If you are already on v1.35 or later, confirm that every Linux node
runs cgroup v2 (or that you intentionally keep the override). Under the default
configuration, a remaining cgroup v1 node fails during kubelet startup.
For kubeadm-managed clusters, Kubernetes v1.35 also makes this an earlier, stricter check. The
SystemVerification preflight check, provided by k8s.io/system-validators, returns an error during
kubeadm init, kubeadm join, and kubeadm upgrade when it detects cgroup v1 with kubelet v1.35 or
later; with an older kubelet, the check remains a warning. See
kubernetes/system-validators#1.12.1 release notes for details.
The top FAQs cover three main areas: why to migrate, the benefits and drawbacks, and key points to keep in mind when using cgroup v2.
Limitations of cgroup v1 and Improvements with cgroup v2
The Linux kernel documentation describes both interfaces:
Let's enumerate some known issues.
active_file memory is not considered available memory
The kubelet treats active_file memory as not reclaimable. For I/O-intensive workloads, a large
page cache can therefore make the kubelet report memory pressure and evict Pods. [...]

## [113] Scaling Kubernetes Workloads with Node Swap
Kubernetes Blog | full text via Kubernetes Blog | ~1325 words

Scaling Kubernetes Workloads with Node Swap
Memory is often the first hard limit a Kubernetes cluster hits. Nodes run out of RAM long before they run out of CPU, and the new wave of agentic AI workloads makes this worse. These workloads demand large memory footprints to start up and run untrusted code, then sit idle waiting for the next prompt. That idle but resident memory is expensive, and it caps how many pods a node can hold. This is where swap helps. Kubernetes support for running nodes with swap enabled reached General Availability in v1.34, and by backing that swap with fast NVMe solid state drives (SSDs), a node can page out dormant memory and pack in far more pods. This post explains how we benchmarked that approach across three workloads, including CI/CD kernel builds, sandboxed headless browsers, and isolated Python runtimes; we found density gains of up to 3×, often with little or no latency cost.
The node density problem
The Kubernetes ecosystem has reached a fundamental physical resource constraint: the strict limits of hardware memory versus the growing demand for dynamic, bursty workloads in the new agentic era.
Historically, administrators provisioning memory-intensive workloads encountered a persistent dilemma: set memory limits too high and you waste expensive infrastructure on idle RAM; set them too low and you risk Out-Of-Memory (OOM) kills.
This conflict is amplified when deploying autonomous AI agents using secure execution environments like the agent-sandbox framework. These agentic pods require large memory footprints to initialize and execute untrusted code. However, after their burst of activity, they typically enter long-tail idle phases waiting for user prompts. Keeping this idle state in physical RAM caps cluster density and makes AI infrastructure expensive to run.
The solution: Kubernetes node swap
With the introduction of Kubernetes' support for running nodes with swap enabled (which reached General Availability in v1.34), this paradigm shifts. By enabling the Linux kernel to page out anonymous memory to disk, node swap acts as a shock absorber during traffic spikes or periods of heavy memory oversubscription.
Historically, swap was discouraged in Kubernetes for two reasons. The first was memory accounting. Under cgroup v1, the controls treated memory and swap as a single combined limit rather than letting operators set an independent limit for disk swap. [...]

## [165] Google’s power-hungry data centers crave nuclear energy
The Verge | full text via The Verge | ~510 words

Google announced a new agreement to update six nuclear power plant sites across the US as the tech giant seeks to generate more electricity for its power-hungry data centers.
Google’s power-hungry data centers crave nuclear energy
Google signed long-term agreements meant to cover the costs of upgrades at nuclear power plants.
Google signed the 20-year deal with Constellation, the leading nuclear power plant operator in the US. The power purchase agreement is meant to guarantee the revenue needed to cover the cost of efficiency upgrades at existing nuclear plants and “represents more than $4.3 billion of new investment by Constellation,” according to the press release.
Over the next five years, the companies expect new equipment at each site to collectively lead to 890 megawatts of additional nuclear capacity. That’s roughly equivalent to the amount of electricity one large new nuclear reactor or three small modular reactors might generate, according to Google and Constellation.
PJM has struggled lately to meet growing demand from AI data centers
They plan to modernize 11 reactors at six sites in Illinois, Pennsylvania, and New Jersey. Each is connected to the PJM Interconnection grid, the largest power grid in the US, which spans 13 states and the District of Columbia — including the nation’s largest hub for data centers in Loudoun County, Virginia.
PJM has struggled lately to meet growing demand from AI data centers. An independent market monitor filed a complaint last year with the Federal Energy Regulatory Commission (FERC) saying that PJM was planning to allow huge data centers to connect to the grid that it could not reliably serve, which could lead to blackouts.
In January, the Trump administration and governors from all of the states where PJM operates issued a joint statement calling on PJM to hold an “emergency” power auction to support the buildout of new power plants through long-term contracts. PJM postponed its auction last week following a directive from FERC to revise its proposal in order to ensure stronger protections to prevent data centers from raising electricity bills for other customers. Electricity rates have skyrocketed in states connected to PJM, including New Jersey, where prices have climbed 54 percent over five years. [...]

## [25] Janet on x32: 32-bit Pointers, 64-bit Speed, 25% Less RAM
Lobsters | full text via Lobsters | ~2405 words

Janet on x32: 32-bit Pointers, 64-bit Speed, 25% Less RAM
It’s possible to save a dramatic amount of memory (close to half for programs with pointer heavy heaps) and also speed up programs by a modest amount (by way of more data fitting in cache) by using 32 bit pointers on 64 bit systems.
The Linux x32 ABI lets you do just this, but it’s tragically underused and overlooked. It’s disabled by default on Debian (though you can enable it with a boot flag) and not even compiled in on Arch Linux. Most software compiles just fine for x32, but there isn’t much packaging for it so you do have to compile nearly everything yourself.
I experimented with deploying mastodon on x32 and it cut the app’s memory usage from 650mb to 350mb. There’s so much potential here, but the work is mostly of the thankless coordination and communication type and I don’t have the time or motivation to push it forward myself. - Hailey
How to Compile for 32 Bits?
Janet libraries like Spork supply their own build flags, but we can hijack them with a fake cc which starts the real one with the necessary -m32 -msse2 -mfpmath=sse flags. I modified the beginning of my default Janet build script:
#!/bin/sh
set -eu
TARGET="$PWD/janet32"
JANET="$TARGET/bin/janet"
mkdir -p "$TARGET/cc32"
printf '#!/bin/sh\nexec gcc -m32 -msse2 -mfpmath=sse "$@"\n' > "$TARGET/cc32/cc"
chmod +x "$TARGET/cc32/cc"
export PATH="$TARGET/cc32:$PATH"
export JANET_TOOLCHAIN=cc
unset JANET_PATH JANET_TREE
mkdir -p "$TARGET"
cd "$TARGET"
rm -rf build/spork janet
git clone https://github.com/janet-lang/janet
cd janet
Easy enough! Now let’s try it!
Failing on Arch
tl;dr: 20% memory reduction, 50% slower
See the Scripts and Results
This is on cachyos (arch, btw) with lib32-glibc lib32-gcc-libs. [...]

## [118] Building advertising for the way people use AI
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

OpenAI introduces a new visual ad format in ChatGPT and expands measurement tools, attribution partnerships, and brand suitability for advertisers.

## [49] Last rites for Gentoo's Chromium package
Lobsters | full text via Lobsters | ~2455 words

Last rites for Gentoo's Chromium package
[LWN subscriber-only content]
Chromium, the open-source upstream project for Google's Chrome web browser, is the browser of choice for many Linux users. It has also gained a reputation as being difficult for Linux distributions to package and build: Chromium has a complex build system, the project bundles many of its dependencies, and it has frequent releases. All of that, plus user complaints, has led the maintainers of the Gentoo Chromium package to give up on trying to maintain the package.
Gentoo focuses on allowing users to build their own software from source
using the Portage
software-management tool. Gentoo packagers create ebuild files, which are text
files written in a Bash-like syntax that contain the information needed by
Portage to build the software. Users then build packages themselves using emerge, which is the
command-line interface for Portage. A
recent ebuild for Chromium illustrates the complexity of the package.
Gentoo does offer prebuilt binary packages for some software via its Binhost project. However, building from source gives users the flexibility to declare USE flags to set compile-time options or change a package's configuration. For example, a user may wish to specify which optional libraries are linked with a package, or whether to install the accompanying documentation. With Chromium in particular, a user might employ the -bundled-toolchain USE flag (which tells Portage not to use the bundled toolchain) in order to use their system's version of Clang to compile Chromium rather than the bundled version included by the upstream project. That is optional for Gentoo users on x86-64 systems, but -bundled-toolchain is required for users on other architectures, since Chromium's bundled toolchain is only shipped for x86-64.
It is worth noting that Chromium is currently not available as a binary package from Gentoo due to problems with building the package with proprietary codecs.
Last rites
Many distributions, including Arch Linux, Debian, and Fedora, use the term "orphan" to refer to packages that have been abandoned by their maintainer; the developer announces that a package has been orphaned, and other contributors have the opportunity to claim maintainership of it if they wish to do so. [...]

## [22] OpenAI “rogue” agent activities found on Wikimedia projects
Simon Willison's Blog | full text via Simon Willison's Blog | ~248 words

7th October 2026 - Link Blog
OpenAI “rogue” agent activities found on Wikimedia projects. Given how tempting a target wikis are for rogue agent swarms, it's not a huge surprise that Wikipedia found evidence of that activity once they went looking:
The Wikimedia Foundation conducted its own investigation to see whether Wikimedia websites had been similarly affected by AI agents, focusing on those operated by OpenAI. We can confirm that we have discovered some activity by these “rogue” OpenAI agents on Wikimedia platforms. The unauthorized bot activities included edits to our wikis, some unsuccessful attempts to exploit a public note-taking tool we host, and heavy traffic, which are described more below.
They found evidence of agents editing sandbox pages, trying to use pieces of infrastructure such as Etherpad to help proxy content from elsewhere, and saw widespread crawling and "hundreds of thousands of data queries" to their Wikidata Query Service.
My best guess is that most of this was a similar (or the same) swarm of agents as those that defaced that German wiki while training for research tasks.
The Wikipedia sandbox wiki edits appear to have started on May 12th, and the initial test edits to the UseModWiki Sandbox page reported by that incident started on May 11th.
Recent articles
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026
- 2026 in LLMs (so far) - 27th September 2026

## [163] AI computing startup Lambda to raise $4B ahead of planned IPO
TechCrunch | full text via TechCrunch | ~314 words

Cloud provider Lambda is raising up to $4 billion at a $14.5 billion pre-money valuation, marking what could be its last private round before a planned 2027 IPO, according to The Wall Street Journal. Coatue Management and Blackstone are leading the round.
A letter to investors reviewed by the Journal shows Lambda’s backlog grew from $15 billion in June to $50 billion in September. While that might look like a hearty increase in demand, much of that increase appears to be driven by a $35 billion commitment from one company: Anthropic, which signed a deal with Lambda in late August.
That means Lambda’s valuation, which has climbed significantly since its 2025 funding round, could be leaning heavily on Anthropic’s ability to keep paying. Still, with reliable GPU capacity so scarce, investors are clearly still willing to bet on companies that provide it, especially ones with large contracts with a major AI lab.
For neoclouds like Lambda, demand isn’t so much the problem as is the cost of meeting it. Data center buildouts are largely funded by debt — of which Lambda just raised an additional $1 billion last week — and lenders are getting choosier about who they offer cash to and under what circumstances. Lambda’s decision to raise more now not only sets the tone for its IPO pricing, but also gives it access to more capital before the scrutiny of public markets arrives.
If and when Lambda does IPO — the company was reportedly meant to debut this year, but has pushed that back amid market uncertainty — it will join other Nvidia-backed neoclouds, like CoreWeave and Nebius, that now depend on the health of their stock to fund their data center buildouts. British neocloud Nscale filed for an IPO last month and is expected to begin trading soon.
Lambda, Coatue, and Blackstone did not immediately respond to a request for comment.

## [55] What AI gets wrong and what failure teaches us
Microsoft Research Blog | full text via Microsoft Research Blog | ~6320 words

Jennifer Neville is a partner research manager at Microsoft who’s built a career around understanding and advancing AI for real-world use, and much like the human-AI interactions she’s been studying, her early-career path was multiturn: math, then physics; cognitive science, then work; and finally computer science—despite her best efforts to avoid the field.
In this conversation with Principal Applied Scientist Chad Atalla, she explores the role evaluation plays in pushing the performance boundaries of today’s AI systems to meet user needs and the “surprising failures” that emerge when models are tested beyond traditional benchmarks. Neville also shares practical guidance for working with current AI systems and discusses why looking closely at data matters when results defy expectations, and what decades of AI progress have taught her about predicting what comes next.
From an unexpected career trajectory to the frontier of AI interaction and learning, this episode asks a larger question: what can we learn when the path—whether human or artificial—doesn’t unfold the way we expect?
Subscribe to the Microsoft Research Podcast:
Transcript
[MUSIC]
JENNIFER NEVILLE: There were times that I felt like I was spinning my wheels. Things weren’t working. I would get, kind of, dejected. And then we’d get to a point where we did learn something, and it was just the, the emotional thrill of that was, that was really what hooked me. The being able to, kind of, understand something that no one else understood yet …
CHAD ATALLA: Sure …
NEVILLE: … because it’s just at the frontier of what we know about things.
STANDARD INTRODUCTION: This is the Microsoft Research Podcast, where Microsoft researchers—driving advancement through fundamental science and technology research—explore the who, how, and what’s next in computing and AI.
[MUSIC ENDS]
CHAD ATALLA: Hello, and welcome. I’m Chad Atalla, an applied scientist here at Microsoft Research.
Today, I’m joined by Jennifer Neville, a partner research manager at Microsoft Research and the Samuel D. Conte chair professor of computer science and statistics at Purdue.
Her research examines machine learning and AI for interactive domains and structured data, looking at how the data points that AI systems are trained on affect their behaviors and how that aligns with what users actually want. [...]

## [122] Your AI Agent Will Do Something Terrible. Here's How to Survive It.
Dev.to | full text via Dev.to | ~1733 words

Here's a pattern I keep seeing.
A team wires up an AI agent that can do real things — send emails, run commands, query and modify the database, call external APIs. The demo is magical. It reads a request, figures out the steps, takes them, reports success. Everyone's impressed, and it ships.
Then comes the first incident. It emails the wrong list. It runs a destructive command against the wrong environment. It reads a web page that quietly tells it to do something nobody asked for, and it obliges. Suddenly the magical demo is a very un-magical cleanup, and someone's asking how this was allowed to happen.
Here's the thing: the demo was never the hard part. Getting an agent to do something is genuinely easy now. The hard part — the part that almost always gets skipped in the rush — is everything that keeps the agent from hurting you when it inevitably does the wrong thing. And it will do the wrong thing, because it's a probabilistic system acting in an unpredictable world.
So this is the checklist I think belongs before you let an agent touch anything that matters. Not the fun part. The part that separates an agent you can actually deploy from a liability with a good demo.
1. Least privilege — the agent can only reach what it strictly needs
This is the highest-leverage guardrail, and it's the one most worth getting right first, because it makes entire categories of disaster simply impossible.
An agent that cannot reach production cannot wipe production. An agent that cannot send money cannot be talked into sending money. An agent with no access to a system can't be the cause of an incident in that system, no matter how confused or compromised it gets. So the question to ask before anything else isn't "what should this agent be able to do?" — it's "what is the least it needs to do its job?" Then give it exactly that and nothing more.
Almost every catastrophic agent story, when you trace it back, turns out to be a permissions decision someone made without quite noticing — handing over credentials that could reach production at all, or a tool scope broader than the task required. The destructive action got the headline, but the over-broad grant was the actual mistake, made quietly, long before. Least privilege is the guardrail that catches the error at the point where it's cheapest to prevent.
2. Human approval for consequential actions — gated by blast radius
Some actions you can let an agent take freely. Some you absolutely should not let it take unattended. [...]

## [31] A Terminal Protocol for Program Status (OSC 7501)
Lobsters | full text via Lobsters | ~1177 words

Mitchell Hashimoto
A Terminal Protocol for Program Status (OSC 7501)
I wrote a specification for a new terminal escape sequence: OSC 7501, the Program Status Protocol. It lets any program tell the terminal what it's doing: idle, working, waiting on the user, finished, or failed, and why.
For example, here is how Terraform could indicate that it is blocked waiting for user input, with the message "Apply 3 to add, 1 to change, 0 to destroy?" (base64-encoded). A terminal (or any other tool running Terraform) could show this information however it feels appropriate: a notification, an inbox, a status icon, etc.
ESC ] 7501 ; state=blocked:kind=permission:app=terraform:msg=QXBwbHkgMyB0byBhZGQsIDEgdG8gY2hhbmdlLCAwIHRvIGRlc3Ryb3k/ ESC \
This post covers why I think this protocol needs to exist, why the existing approaches aren't good enough (especially for coding agents), and how the protocol works.
This is a completely generic, terminal-native specification and protocol. It emerged from my work on Superlogical and Ghostty but the specification has no product-specific functionality or language. It is designed as an idiomatic, well-formed specification that any terminal developer will find familiar.
The Problem
Long-running work is common in terminals: builds, deployments, package upgrades, data processing, and, more and more today, coding agents. These programs alternate between working on their own, waiting on the user, and finishing. Meanwhile, users usually go off and do something else and want to know when the work finishes or needs them.
Aspects of this problem have been solved in various ways going back decades. For example, some terminals monitor the active foreground process and have features to notify when it changes. Or, they wait for some time period of "quiet" (for various definitions) output. The specification also lists the reasons why existing sequences aren't enough.
Ultimately, I felt there wasn't a cohesive, interaction-agnostic, generic solution to this problem that conveyed progress, blocking, completion, and trees of tasks. And it wasn't possible to cobble together pre-existing sequences to achieve it robustly, either.
Singling Out "Agentic Inboxes"
Don't care about AI, LLMs, etc.? Skip this section. The problem is generic and applies in a compelling way without bringing in AI. It's particularly nasty with AI so I want to call it out, but if you don't care about any of that, just skip this. [...]
