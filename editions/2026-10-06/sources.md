# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Beam: Reflection's 501B open-weight model
Hacker News | full text via Hacker News | ~2871 words

Introducing Beam: Reflection’s 501B open-weight model
October 5, 20268 min read
We are introducing Beam, Reflection’s first open-weight model. Beam is a sparse Mixture-of-Experts model with 501 billion total parameters, 23 billion active, built for coding, reasoning, and agentic workloads.
Beam’s capabilities come from major investments in both pretraining and reinforcement learning (RL). We pretrained the model on 23.8 trillion diverse, curated, high-quality tokens from the web and proprietary licensed datasets, matching or outperforming available similar-sized open base models. In parallel, we developed the algorithms, training environments, and infrastructure needed to sustain high-compute RL at exceptional scale. Our high-compute RL run generated over 100 million rollouts on 10.5K NVIDIA GB300 GPUs over 4 weeks of training.
Together, these efforts produced competitive open-weight performance with frontier inference compute efficiency.
Beam is undergoing final red-teaming and evaluations. You can sign up here for early access to the model. We will release the weights, technical report, model card, and developer artifacts later this month.
Model Capability
We trained Beam with a particular focus on coding and agentic performance. Beam advances the Western open-weight frontier and is competitive with larger open models like GLM 5.2 and approaching Qwen 3.8-Max on coding and agentic tasks. Where frontier open models like Kimi K3 remain ahead on raw capability, Beam's advantage is efficiency at inference time.
The below figure shows Beam's performance across a range of coding, agentic, reasoning, and STEM benchmarks. NR denotes scores that have not been reported.
Beam pairs coding and agentic capabilities with highly efficient reasoning. On advanced reasoning benchmarks, it achieves scores comparable to GLM-5.2 while using 3–4× less inference compute. Efficiency gains are even more pronounced when comparing to models in the 2T+ parameter family like Qwen 3.8-Max, which require significantly more inference compute per token.
These results translate into more intelligence per token, delivering strong model capabilities at lower cost, making Beam a powerful workhorse model for enterprise coding and agentic workloads.
High-Compute Reinforcement Learning
We made high-compute reinforcement learning a central scaling axis for Beam, investing in RL science, data, and infrastructure to turn more compute into stronger capabilities. [...]

## [15] The Download: AI’s popularity paradox and EmTech Future 2026
MIT Technology Review | full text via MIT Technology Review | ~1058 words

The Download: AI’s popularity paradox and EmTech Future 2026
Plus: Trump has unveiled a “Super Intelligence Force” to oversee AI.
This is today's edition of The Download, our weekday newsletter that provides a daily dose of what's going on in the world of technology.
People really hate AI, so why can’t they get enough?
—Will Douglas Heaven
Over the summer I talked to the CEO of Springboards, a startup building an LLM designed to come up with a wide variety of responses. He said something that’s been stuck in my head since: “We often say that we’re a self-loathing AI company. We don’t know if we really like what we’re doing.” My reply? “I guess that makes me a self-loathing AI journalist.”
It was a joke! I love my job. But I do not love many of the things the technology I write about has become: warped by hype, steered by zealots, inescapable—and I’m far from alone.
Around the world, a love/hate attitude toward AI is very much the vibe right now. Public sentiment is souring fast, with more people saying AI will have a negative impact than a positive one. At the same time, AI use is skyrocketing.
So why do people hate AI but keep coming back for more? Here’s my theory.
To stay up-to-date with the latest in AI, sign up to get The Algorithm, our weekly AI newsletter, in your inbox every Monday.
EmTech Future 2026: when AI meets everything
Last week, EmTech Future 2026 explored some of the biggest questions shaping technology right now: how AI is changing industries, where quantum is heading, what new energy systems could make possible, and how robotics are evolving. It also looked at what happens when these technologies start to converge.
The full program is now available on demand. And today, we’re releasing two sessions exclusively to subscribers: a chat with Google Research’s Yossi Matias on how AI is reshaping biology, infrastructure, manufacturing and science, and a special panel with MIT Technology Review editors that takes you inside our newsroom.
Watch the sessions and access the full EmTech Future 2026 program here.
The must-reads
I’ve combed the internet to find you today’s most fun/important/scary/fascinating stories about technology.
1 Trump has unveiled a “Super Intelligence Force” to oversee AI
The group will coordinate US AI policy and industry engagement. (NBC News)
+ Trump named national intelligence chief Jay Clayton as its leader. (NPR)
+ Elon Musk says he will rename SpaceXAI to SpaceXSI. [...]

## [21] MCP for agent-to-agent comms may be the riskiest protocol you've never heard of
Ars Technica | full text via Ars Technica | ~277 words

The adoption of AI agents in millions of organizations is creating new opportunities for attackers to make them take malicious actions, such as exfiltrating database contents and sensitive business and personal information.
In the past five months, Google and four other organizations—with little in common except for their use of AI agents—have acknowledged vulnerabilities that exploit one agent inside a targeted network to spread harmful instructions to other internal agents. The technique is a special form of prompt injection that targets not the LLM but a particular agent, such as one for translation or data analysis. Guardrails inside such agents, if they exist at all, are often lax and will send the instructions to other agents down the chain. Because the latter agent explicitly trusts the first one, it follows the directions.
Unexpected and hard to mitigate
Independent researcher Syed Anas Mohiuddin tested agents from organizations including Google, JP Morgan Chase, Weviate, Rapid7, the French government’s interministerial digital directorate, and the US federal government. His proof-of-concept attacks exploit trust gaps in MCP, short for Model Context Protocol. The standard is one way AI apps and agents communicate with each other inside an internal network. The illustration below shows a simplified MCP in action.
Many special-purpose agents lack the guardrails that might normally mitigate the most harmful consequences of a prompt injection. And since MCP servers store credentials for each agent—and agents are built to trust every other internal agent—an exploit that would have been rejected by the LLM succeeds. In many cases, well-crafted prompts targeting the right agent will lead to a server-side request forgery, a vulnerability that causes a web server to make unauthorized network requests.

## [53] Cloudflare Fixes Cross-Tenant Data Exposure in Containers
InfoQ | full text via InfoQ | ~845 words

Cloudflare recently disclosed a cross-tenant data exposure vulnerability in Containers, the platform that also underpins Cloudflare Sandboxes. A customer on a Workers Paid account could recover residual disk blocks left behind by other customers' containers on the same host. Cloudflare has remediated it and says it found no evidence of malicious exploitation. The failure was not in the virtual machine boundary but in the storage allocator beneath it.
Oren Yomtov, a security researcher at Accomplish, reported the issue on September 4 through Cloudflare's bug bounty program.
Each Cloudflare container runs inside a Firecracker virtual machine with a writable root disk, provisioned through Linux device mapper thin provisioning. The affected pools used a 64 KiB thin-block size and were configured with skip_block_zeroing, which tells dm-thin not to clear newly allocated blocks before exposing them.
That combination created the gap. Writing a single 4 KiB block into an unmapped region caused dm-thin to allocate a 64 KiB physical block from a pool shared across customer accounts. The write replaced only its own portion, leaving up to 60 KiB that could still hold whatever the previous container had written there. A raw read of the disk could then return bytes the new container never wrote.
The researchers used ext4 directory block checksums to tell their own blocks apart from everyone else's. Across six production placements, all 5,614 testable directory blocks came from elsewhere, with 2,700 distinct foreign directory inodes identified. Residual material appeared on 18 of 24 placements and 20 of 22 underlying nodes across four continents. Recovered block types included directory structures, database pages, and structurally complete SQLite databases.
Cloudflare is precise about the limits. An attacker could not choose a victim, a workload or a host, could not read an actively attached disk, and had no guarantee that residual data would be present at all. Exposure depended on where Cloudflare placed the workload and which released blocks dm-thin happened to reassign. The researchers did not demonstrate modification of another customer's data or any impact on availability.
Reaction among security practitioners on LinkedIn has focused on where the isolation broke rather than on the platform. Peter Ward, a senior cloud security engineer at Visa, described the pattern as a recurring one:
That is tenant isolation broken at the storage layer, not an app bug. [...]

## [6] Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates
Hacker News | full text via Hacker News | ~1782 words

We’re all used to two types of magnet. The common one, the fridge magnet, is ferromagnetic — its atomic magnets all point the same way (up or down), adding their magnetic effects. The less well known one, the antiferromagnet (AF), has neighbouring atomic magnets that point opposite ways and exactly cancel out magnetically.
For a long time, there’s been an intense drive in computer memory research to create materials in between these two extremes. For this purpose, it helps to have a clear picture of what these extremes mean.
Today, I’ll share what we found. A team of AI agents and I designed one candidate magnet and found another, first made in 1999, that our calculations predict has the properties we were after.
But before diving into the details, let me first lay out a magnet primer that takes all of 90 seconds, assuming you are not an undergraduate in physics or chemistry.
A 90 second primer in magnets
Spin
Each electron has a quantum mechanical property called ‘spin’, which is responsible for its magnetic moment. We can model the spin direction for each electron as either pointing up or down.
Spintronics
We use spin for storage. A magnetised material stores information based on the spin up/spin down orientation of its electrons, in the same way classical magnets store information based on pointing up/down. The most prominent example of spintronics is the hard drive read head, the device that reads the magnetic bits on the disk. MRAM is another type of spintronics that uses the same principle to store binary information in a non-volatile way.
In the world of spintronics, we want to sort electrons by their spin orientation so we can read/store their information. Ferromagnets do this naturally: the electrons that carry current are mostly of one spin, up or down. Ordinary antiferromagnets, however, cannot distinguish up/down electrons.
This leads us into the next section.
Three kinds of magnets
Ferro
Ferromagnetic materials are characterised by having a macroscopic magnetic field, or a field that leaks out from the surface. This is why a fridge magnet sticks to your refrigerator door.
The problem, however, is that the magnetic field interferes with nearby materials and is difficult to control for storage purposes. In addition, switching magnets back and forth is relatively slow and consumes a lot of power.
Another feature of ferromagnetic materials is that the spins are sorted (by up/down orientation) according to energy level. [...]

## [71] Anthropic to invest $100 million to train AI engineer talent
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~46 words

Anthropic is investing $100 million in the Claude Frontier Academy to train 10,000 AI engineers by 2027. The program partners with firms like Accenture and Morgan Stanley to enhance AI fluency and enterprise tech integration. The initiative addresses increasing demand for AI expertise in various industries.

## [35] AWS Weekly Roundup: Amazon Bedrock Managed Agents powered by OpenAI, Q3 service availability updates, Kiro workflows, and more (October 5, 2026)
AWS News Blog | full text via AWS News Blog | ~970 words

AWS News Blog
AWS Weekly Roundup: Amazon Bedrock Managed Agents powered by OpenAI, Q3 service availability updates, Kiro workflows, and more (October 5, 2026)
Last week, we announced a public preview of Amazon Bedrock Managed Agents powered by OpenAI, built on a customized version of OpenAI’s Agents API engineered to be AWS-native and integrated with AWS resources. You can now build agents optimized for OpenAI models that run entirely inside AWS with the identities, permissions, and governance controls you already use.
You can choose an execution environment: self-hosted compute to use an existing development machine, container, or compute environment or Amazon Bedrock AgentCore Runtime, for managed runtime sessions and configurable storage in your AWS account. To learn more, visit the Amazon Bedrock documentation.
In addition, we are adding new frontier models on Amazon Bedrock to expand your model choices:
- OpenAI GPT-6.1 Sol: An upgrade to GPT-6 Sol, GPT-6.1 Sol delivers exceptionally strong performance on agentic coding, computer use, and professional work. According to OpenAI, it approaches GPT-6 Astra across demanding evaluations at roughly one-fifth of the cost, giving developers more room to build and run capable agents at scale. To learn more, visit the GPT-6.1 Sol model card.
- OpenAI GPT-6 Astra UltraFast mode: Ultrafast is a premium speed tier for GPT-6 Astra, built for workloads where speed matters most. According to OpenAI, Ultrafast delivers up to 6x faster inference in the API, with up to 300 tokens per second. The Amazon Bedrock inference engine delivers the performance, security, and reliability required for production workloads. To learn more, visit the GPT-6 Astra model card.
- Anthropic Claude Sonnet 5.5: Claude Sonnet 5.5 is a smarter, more efficient Sonnet and a step up from Sonnet 5, making it a natural upgrade for teams already building on Sonnet. It’s stronger for coding, completing well-scoped tasks as part of a larger coding strategy such as building and fixing features with Claude in the same session or verifying output against requirements. To learn more, visit the Claude Sonnet 5.5 model card.
- SpaceXAI Grok 4.7: Grok 4.7 builds on Grok 4.6 with better mixed-document handling, more dependable repo-scale coding with planning and error recovery, and enhanced browser-use agents for form fills and portal navigation. To learn more, visit the Grok 4.7 model card. [...]

## [34] ReviewBench: An open benchmark for AI code review
GitHub Blog | full text via GitHub Blog | ~1358 words

Michelle Zhou
Michelle develops and evaluates agentic AI systems for code review, focusing on repository-level context retrieval, review and fix quality, and rigorous benchmarking of AI code reviewers.
We’re launching ReviewBench, a benchmark for code review agents built on representative GitHub pull requests, multi-source ground truth, calibrated evaluation, and production-aligned metrics.
Agentic code review is becoming an essential piece of how development happens. It helps you inspect pull requests, catch issues, and decide what deserves attention before code ships.
But the quality of existing AI reviewers can be hard to measure, and you need to know the strengths of a reviewer before you know if it will help you. Some reviewers surface more issues, some produce less noise, and some are stronger at catching critical problems while others surface smaller improvements, too. You may need code review to do different things within your workflow.
That makes it important to understand how reviewers actually compare: what different systems catch, what they miss, and the tradeoffs they make. A good code review benchmark should reflect the diversity of real pull requests, capture a broad set of review findings, and support meaningful breakdowns by severity, category, and precision-recall preferences. For teams building code review agents, the benchmark should also provide an offline signal that reliably tracks whether changes are likely to improve the experience in production. Existing benchmarks often make tradeoffs between label quality, coverage, and how well they represent real-world code review, leaving a gap for a rigorous and reproducible evaluation methodology that brings these pieces together.
We built ReviewBench, a new code review offline benchmark, to address that gap, and it is available for you to use today. It follows the language, repo size, and size distribution of pull requests, modeled after over 100 million real pull requests on GitHub. It uses a multi-source golden set and a consistent evaluation rubric and has been independently validated by senior engineers. Just as important, with the help of ReviewBench, our offline evaluation of Copilot code review (CCR) has become more effective at anticipating the direction of production experiments, giving us greater confidence that measured improvements reflect meaningful gains for users. [...]

## [33] Connecting AI agents to enterprise knowledge
MIT Technology Review | full text via MIT Technology Review | ~672 words

Sponsored
Connecting AI agents to enterprise knowledge
A strong structural foundation that links data and agents is key for context-rich agentic AI that scales.
In partnership withNeo4j
For all the data that AI systems continually amass and analyze, enterprise AI agents often suffer from a curious shortcoming: a lack of knowledge. More than data, knowledge is the understanding of what the data means in the context of individual organizations. AI agents need this understanding to reason about situations, make decisions, and ultimately take actions. Without sufficient knowledge, agents are prone to making flawed and unreliable decisions.
A lack of knowledge, our research finds, is a major reason agentic AI use cases never make it to production. Competitive pressure is making it urgent to address this. Organizations need to deploy and scale more of their agentic projects to capture the efficiency gains AI promises. Falling short risks wasting the investment already sunk into these projects, and it cedes ground to rivals already putting their agents to work more effectively.
The purpose of this report, which is based on a survey of 300 data, AI, and other technology executives, is threefold. First, it seeks to gauge organizations’ agentic knowledge capabilities (i.e., their ability to give AI agents a full contextual understanding of the data they ingest) across semantic knowledge, episodic memory, and procedural knowledge.
Second, the report probes the challenges organizations face in improving access to knowledge and ultimately to getting more agent use cases into production. Third, it explores the measures organizations are taking to overcome these challenges.
The key findings include the following:
Data and knowledge weaknesses consistently stall AI agent progress. On average, only around a third (34%) of organizations’ agentic AI projects make it into production. Even high-tech firms struggle with this. Legacy data systems, security and privacy concerns, and a lack of knowledge and context are the key points of failure.
Strong knowledge capabilities correlate with agent success. A small group of production leaders (organizations where on average 61% of agentic projects advance beyond pilot) have stronger knowledge capabilities than the rest, especially when it comes to semantics. This advantage tracks closely with their higher production rate.
Fragmented data hugely complicates knowledge access. [...]

## [5] Anthropic reported diary entry to police, woman faces felony charge
Hacker News | full text via Hacker News | ~426 words

What just happened? Another incident has taken place that illustrates the need to be careful what you tell AI. A Florida woman is facing felony charges after she used Claude as a diary and allegedly wrote that she planned to "shoot up" the Sheriff's office. After a human reviewer examined the statements, they were reported to police.
According to the arrest report, Carli Michelle Heller, of Bonita Springs, Florida, wrote on September 26 that she would attack the Sheriff's office. She later said that she uses Anthropic's chatbot like a "diary."
Claude's safety systems flagged the entry and it was escalated to a human reviewer. After deciding it was a credible threat, the reviewer reported it to law enforcement.
The company says it may share user information in limited emergencies if it believes disclosure is necessary to prevent death or serious physical injury.
Deputies identified Heller and visited her home. She was detained without incident before an LCSO intelligence detective took over the investigation.
Heller faces a charge of making a written threat of violence under Florida law. Florida Statute 836.10 makes it a second-degree felony to send, post, or transmit a written or electronic record threatening to kill or injure someone, carry out a mass shooting, or commit an act of terrorism. The communication must be made in a manner in which another person may view it.
Anthropic isn't going to be taking any chances when it comes to anything it deems a potential threat. Last month, it was reported that OpenAI and Sam Altman are being sued by British Columbia over claims that the company could have prevented a mass shooting in the Canadian province.
The shooter, eighteen-year-old former pupil Jesse Van Rootselaar, had previously been flagged by OpenAI's safety team for her conversations about gun violence, but OpenAI never alerted police because the conversations did not meet the threshold for legal referral.
In June, Florida also sued OpenAI and Altman, alleging that ChatGPT had contributed to real-world harms, including the 2025 Florida State University shooting.
The latest incident is another reminder to think before you enter something into a chatbot that could get you into trouble. It's certainly not a private diary whose contents are for your eyes only.
Reports last month revealed that human contractors reviewing Microsoft Copilot's image editor can see users' prompts, uploaded photos and AI-generated edits. [...]

## [42] Bringing predictive analytics to the agentic AI era
MIT Technology Review | full text via MIT Technology Review | ~380 words

Sponsored
Bringing predictive analytics to the agentic AI era
Predictive modeling with AI can revolutionize how organizations use everyday business data.
In association withTP
In 2026, the question for enterprise AI is no longer whether predictive models can outperform statistical forecasts—that argument is settled. The big question now is how to enable predictive systems to act on their own conclusions without drifting from business intent. The frontier has moved from prediction to autonomous decision making, and the gap between leaders and laggards is widening accordingly.
“Enterprises are done with a backward-looking point of view; they want to be more forward-thinking,” says Vishal Gupta, partner at research firm Everest Group.
Intelligent analytics, powered by technologies like deep learning and generative AI, are making this possible. Real-time training allows AI to evolve continuously instead of waiting for quarterly refreshes. In addition, the data that newer predictive engines rely upon has expanded to encompass not just neat, numerical records but also messy, unstructured sources of insight-rich interactions. As a result, AI-powered analytics are moving enterprises from passive hindsight to pragmatic foresight.
AI takes predictive analytics—a broad discipline that includes predictive modeling, data prep, analysis workflows, interpretation of results, and decision-making applications—to new heights. “In many ways I think the word ‘analytics’ is giving way to AI,” says Gupta. “Everything is becoming AI.”
This content was produced by Insights, MIT Technology Review’s custom content arm, not its editorial staff. It was researched and written by humans, with any AI tools that may have been used limited to production processes under human oversight.
Deep Dive
Artificial intelligence
AI’s recursive self-improvement might not come so quickly after all
AI agents are not yet creative enough to carry out genuinely innovative open-ended AI research, it seems.
Don’t be fooled—LLMs don’t reason
Ten years after AlphaGo’s match against Go champion Lee Sedol, today’s AI still isn’t tapping into the machinery that made that win possible.
Don’t be fooled by this summer of AI hype
Breathless claims about AGI and new capabilities fall apart pretty quickly under scrutiny.
These startups are chasing the next big thing in LLMs
Meet the new kids nipping at the heels of the AI giants. [...]

## [72] How many AI agents could run on the AI chips shipped through 2027?
TLDR AI | full text via TLDR AI | ~5122 words

Overview
AI companies are spending hundreds of billions of dollars a year on chips and data centers, on the premise that those chips will run AI agents to do work that people do today. How many agents could this hardware buildout actually support?
- AI chips shipped through 2027 could run tens to hundreds of millions of concurrent frontier-model agents. Running nonstop, these agents would supply as many weekly working hours as about 140–720 million full-time employees.
- More efficient models could potentially support billions of agents on the same hardware. Applying DeepSeek V4 Pro serving benchmarks to the projected hardware supply yields approximately 1.9 billion concurrent agents supplying as many weekly working hours as 8 billion people each working 40 hours.
- Even modest use of this capacity would require a massive increase in global demand for AI. Using 20% of our central capacity estimate would imply $2.6–5.3 trillion a year in API-equivalent spending, against roughly $1 trillion in developer revenue by end-2027 at fivefold annual growth.
- Hourly agent spending varies substantially across models and harnesses. In our analysis of agent traces, Codex workloads averaged roughly $16–18 per hour of continuous agent activity, compared with $24–50 for Claude Code workloads.
Potential agent capacity and spending
Anthropic’s Dario Amodei has described a future “country of geniuses in a datacenter”, but how many AI agents could future data centers actually support? That scale matters for AI’s potential impact on the economy and labor force.
We find that hardware using high-bandwidth memory (HBM) shipped during 2025–27 could eventually support tens to hundreds of millions of concurrent frontier-model agents, assuming full deployment and allocation to these workloads. HBM shipped during 2025–26 could support 16–56 million concurrent agents once deployed. Including shipments through 2027 raises that estimate to about 30–170 million.1
But unlike humans, an AI agent can work all 168 hours each week, 4.2 times the 40-hour workweek for a full-time employee. Therefore, these agents could work as many weekly hours as about 67–240 million people from hardware shipments through 2026, and about 140–720 million from shipments through 2027. For scale, the United States has a population of 342 million and an estimated 100 million knowledge workers. These comparisons count working hours alone. [...]

## [40] Akka Tests Spec-Driven AI Delivery Across 65 Open Source Projects
InfoQ | full text via InfoQ | ~426 words

Akka used 65 open source projects to test a spec driven workflow for AI assisted software porting, measuring specification structure, context, model and effort selection, automated validation, token consumption, and runtime performance. The initial tranche took 99.3 hours and consumed 9.41 billion tokens, with Akka reporting a lines of code or performance improvement in 57 of the 65 ports.
The experiment used two tranches. Akka analyzed all 65 projects, generating specifications and implementing up to 10% of each project's surface area, then selected 10 for complete implementation based on system characteristics and measurable results. The delivery harness cycled through discovery, specification, porting, benchmarking, and improvement. Discovery analyzed code, models, schemas, and runtime behavior, while Claude with Akka Specify handled implementation, testing, and review. A common benchmark runner compared tests, code size, and latency.
Akka delivery harness workflow(Source: Akka Blog Post)
Akka found that structured specifications with claims, evidence, and typed behavior improved first-pass implementations, while gaps in context files remained around cross-component decisions. Follow-up areas include interface enumeration, test ingestion, provenance tracking, differential testing, and adversarial testing.GitHub Spec Kit similarly structures coding agent workflows around specification, planning, tasks, implementation, and convergence. In Akka's experiment, Sonnet averaged 61 minutes per port versus 120 minutes for Opus, while Opus used about 40% fewer tokens. Higher effort settings increased consumption without consistently improving efficiency.
The finding prompted discussion among engineers following the research. Aaditya, commenting on a LinkedIn post by Tyler Jewell, CEO of Akka, wrote
Smaller model's behavior matched modernization work he had observed, where the small model follows the spec while a larger model may improvise.
Aaditya also questioned
Whether reductions in lines of code resulted primarily from dead code removal or from differences in the target language.
Rick Bryce, Head of Marketing at Avahi, raised a related point in the same discussion and suggested that constraints could influence the result. The comments add questions around whether model capability, specification constraints, or both account for differences in porting efficiency. [...]

## [101] API Authentication & Authorization: An Engineering Deep Dive into Mechanisms, Trade-offs, and Failure Modes
freeCodeCamp News | full text via freeCodeCamp News | ~4244 words

Every API has some form of authentication. But having authentication and getting it right are two completely different things.
I've reviewed production systems where JWTs had no expiry. Systems where API keys were hardcoded in source code and committed to public repositories. Systems where OAuth redirect URIs used wildcards. Systems where Basic Auth was being used for financial APIs over what was supposed to be HTTPS but nobody checked.
Every single one of those was a live vulnerability waiting to be exploited.
Most of these problems didn't come from careless engineers. They came from engineers who understood how to make the mechanism work but didn't understand the failure modes. Nobody told them what happens when it breaks. Nobody defined what the organizational standard was. They picked what they knew, implemented it well enough to pass code review, and moved on.
This article is about changing that. Not just how each mechanism works, but when to use it, when not to use it, and exactly how it fails in production.
Before anything else, let's clear up a confusion that causes real vulnerabilities. Authentication answers: who are you? Authorization answers: what are you allowed to do?
A system that authenticates perfectly but authorizes poorly will still serve unauthorized data. A system that authorizes perfectly but authenticates weakly is trivially bypassed. Both must be correct, independently.
Table of Contents
- Prerequisites
- The Foundation: What You Must Get Right Before Choosing a Mechanism
- 1. Basic Authentication
- 2. API Keys
- 3. Bearer Token Authentication
- 4. JWT - JSON Web Token
- 5. OAuth 2.0
- 6. OpenID Connect (OIDC)
- 7. Mutual TLS (mTLS)
- Choosing the Right Mechanism
- The Organizational Discipline That Ties Everything Together
- Conclusion
Prerequisites
Before reading this article, you should be comfortable with:
- What an API is and how HTTP requests and responses work
- A basic understanding of what a token or session is
- General software architecture concepts: what a gateway is, and what a service layer is
- Familiarity with Dart or C# syntax
You don't need a security background. Every concept here is explained from an engineering perspective.
The Foundation: What You Must Get Right Before Choosing a Mechanism
Before you even think about which mechanism to use, three things must be in place. No mechanism saves you if these are missing.
1. TLS isn't Optional
Every API communicates over HTTPS. [...]

## [17] I Quit OpenAI Because Its Culture Is Broken
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403; TLDR Dev (Web Dev): HTTP 403) | ~81 words

David Robinson resigned from OpenAI this week, joining a parade of former colleagues who have decided that the company's current path is unacceptable. Robinson headed the writing of the safety reports that OpenAI publishes with each major launch. OpenAI has thrived by trial and error, but this approach guarantees periodic failures, and the scale of those failures is growing. Achieving something much closer to perfect the first time is becoming more essential because iteration after a mistake may not be possible.

## [46] Presentation: Building Reusable Evaluation Frameworks for Agentic AI Products
InfoQ | full text via InfoQ | ~6807 words

Transcript
Susan Chang: My name is Susan. I'm a principal data scientist at Elastic. We make tools like Elasticsearch and Kibana. I've also written a book with O'Reilly called "Machine Learning Interviews." Today we're going to be talking about a few things. I'm going to talk a bit about what kind of agents we've been building and try to maybe connect them to what you folks might have been building. Tracing, which is, in my opinion, very important and a huge foundation, as well as how we use that to enable all these evaluations. I'm going to talk about how our company made this journey through maybe individual, like rebuilding a lot of evaluations towards building a shared framework, as well as what are the building blocks we have in that shared framework. Then tying it all together, and then see what takeaways that we have there.
AI Agents We Are Running in Production
Just so that we can be roughly on the same page, I'm going to describe a bit of why we're building agents at Elastic and the type of agents that we're running in production. Elastic, we make Elasticsearch, so a lot of companies, they use us for just search or retrieval. They could use us for like normal keyword search or vector search. Every time you've been searching on Stack Overflow or using Uber and whatnot, they use some sort of Elasticsearch tools. GitHub as well, and Tinder, these are just some examples. I mention these because there's just a really wide range of industries and use cases. It's really hard to describe what exactly people do. I'm trying to put some examples as well as what we're doing internally. What is the bottom line here? People just have data in Elasticsearch and then they can apply it to different use cases.
Internally, we actually build on top of Elasticsearch, observability as well as security. This is important because I'll be talking about some examples where we actually, in Elastic, we build reusable security analyst tools that use AI agents on top of Elastic. This is one example. The use case for this is that like an Elastic user, they could already be storing a bunch of logs in Elastic. We have one huge banking customer. They said that they're ingesting petabytes of data into Elastic for the cybersecurity use case. Why is this important? When they have a cybersecurity incident, they need to be able to look through all those logs, filter them, and extract the right information. They already have all this data within Elastic as a datastore. [...]

## [47] Article: The Platform Engineering Playbook for Production LLMs
InfoQ | full text via InfoQ | ~6586 words

Key Takeaways
- Hallucination rate is a platform-controllable metric. By wrapping the model in an automated retry loop that catches formatting, grounding, and infrastructure errors on the fly, we cut production hallucination rate from fifteen percent to 1.5 percent without touching the foundation model.
- An intent-validation gate that returns "unclassified" instead of defaulting to the highest-scoring agent eliminates off-intent hallucinations and improves multi-agent routing.
- By storing prompts in a history-preserving registry rather than hardcoding them into our application files, we can update or roll back instructions instantly at runtime. Tweaking prompts without a clear audit trail is the easiest way to silently break your AI's behavior.
- Enforce tool authorization directly at the resource server with a strict default-deny policy; relying solely on API gateway checks, means any single bug in your orchestrator can instantly expose every connected tool.
- Standard APM tools cannot detect semantic degradation. You must instrument hallucination rates and per-team token costs at request ingress. Trying to retrofit this attribution onto a live production path later will cost you weeks of engineering time.
By the end of our first month running an LLM-driven inventory recommendation system in production, roughly fifteen percent of agent responses were hallucinations, confident-sounding outputs grounded in nothing real.
Six months later the rate was 1.5 percent and the lever that moved the number wasn't a better foundation model. It was the decision to stop treating the LLM stack as an application concern and start treating it as platform infrastructure.
The project behind this article is an inventory accuracy platform at a large retail organization. In retail supply chains, system inventory records drift from what is physically on shelves through misplacement, damage, theft, and miscounts; that drift degrades ordering, replenishment and product availability.
Our multi-agent LLM system analyzes discrepancy signals across millions of SKUs and billions of historical inventory records and generates corrective recommendations for our consumers who aim to maintain inventory accuracy at all times. [...]

## [60] The Anatomy of Harness Engineering: How to Evaluate, Iterate, and Guard AI Coding Agents
Google Developers Blog | full text via Google Developers Blog | ~755 words

When developers first work on harness engineering for agentic coding systems, they often fall into the same trap: they run common end-to-end benchmarks like Terminal-Bench and DeepSWE, watch a composite score move by a few percentage points, and have no idea why it changed.
End-to-end benchmarks are the de facto for evaluating model performance and determining what needs deeper investigation, but the challenge is that those investigations come at a high cost.
Behavioral evaluations are often a better measure of confidence on whether the behaviors you expect actually do happen and whether you’re moving in the right direction instead of backsliding when it comes to regressions or new model changes. They can serve as your iteration partner and help give insight into why certain changes move the needle in one way or another.
Here’s our take on behavioral evaluation, including approaches that have helped us keep agent systems reliable as models evolve.
Most teams evaluate AI agents like they would evaluate a student taking an exam. They hand the agent a large codebase, give it a time limit, and measure its success based on how many tests pass or fail.
When that score drops, what went wrong?
End-to-end benchmarks don’t typically directly answer these questions.
Behavioral evaluations function like integration tests for improving agent harness operation. When you have a rich enough behavioral eval set, you have a baseline for the behavior you're targeting from your agent, and you're able to iteratively improve the prompt to get there.
Instead of measuring whether the agent solved an entire multi-file refactor, a behavioral eval measures discrete, observable actions:
Instead of setting up a complex evaluation harness on day one, use this time to follow your hunches and run experiments.
When bootstrapping an agent from scratch, you start with developer instinct and dogfooding. Until you have built an agent capable of dogfooding its own codebase, handling boilerplate, writing its own markdown renderer, and executing routine developer tasks, it doesn’t make sense to run evaluations.
Evals belong to the second phase of development: ensuring forward progress and guarding against regressions.
The primary purpose of an evaluation suite is not to celebrate when you make the agent 2% better; it is to give you unshakeable confidence that a new prompt tweak, tool schema change, or model upgrade did not make the agent holistically worse. [...]

## [150] Huawei and Qualcomm Struck a Broad Multi-Year Patent Licensing Deal
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~89 words

An anonymous reader quotes a report from Quartz: Huawei and Qualcomm on Monday announced a multi-year, broad patent license agreement covering 5G, artificial intelligence, compute, and networking technologies, along with Qualcomm's purchase of certain Huawei U.S. patents in those same fields. The deal is the first patent licensing agreement between the two companies to cover 5G technologies, according to Reuters. Huawei said the agreement is expected to bring the cumulative value of its patent licensing deals above $6.9 billion upon closing. The agreement includes cross licenses to both comp

## [56] Cloudflare Plans Public Certificate Authority to Issue Quantum-Safe TLS Certificates
InfoQ | full text via InfoQ | ~719 words

Cloudflare announced plans to operate a free public Certificate Authority designed to issue quantum-safe Transport Layer Security certificates. The initiative tackles one of the most critical structural bottlenecks facing modern web infrastructure, namely the impending transition away from classical public key cryptography. While post-quantum key exchange algorithms have already seen active production rollouts, post-quantum authentication across the Web Public Key Infrastructure has lagged due to the immense payload size of quantum-resistant digital signatures. By coupling standard X.509 issuance with emerging Merkle Tree Certificates, the platform aims to provide enterprise engineering teams and site operators with backwards-compatible, low-latency quantum resistance ahead of production trust-store deadlines.
Current internet authentication depends almost entirely on classical asymmetric primitives such as RSA and elliptic-curve cryptography. In a post-quantum environment, algorithms standardised by the National Institute of Standards and Technology, including ML-DSA and Falcon, protect against cryptanalytic attacks powered by Shor's algorithm. However, these post-quantum signatures and public keys require dramatically more data than their classical predecessors.
Directly substituting post-quantum signature algorithms into traditional hierarchical X.509 certificate chains inflates the volume of cryptographic handshake data by roughly forty times. In practical terms, exchanging multi-kilobyte certificate chains during every initial TLS connection causes acute TCP segmentation, triggers packet loss on constrained networks, and forces extra round-trip times during the handshake phase. Furthermore, Certificate Transparency logs, which record every publicly trusted certificate issued by a Certificate Authority, would experience severe operational strain under the sheer weight of these enlarged signatures.
To circumvent this scaling penalty, Cloudflare's new public authority embraces Merkle Tree Certificates, an alternative authentication model currently advancing within the IETF PLANTS working group. Rather than signing each server certificate with an isolated, individual signature from an intermediate authority, the system batches certificate issuances into an append-only Merkle tree structure. [...]

## [158] How to Break the AI Coding Agent Fix Loop
freeCodeCamp News | full text via freeCodeCamp News | ~2499 words

You've likely seen this movie before: something breaks in an app you built with an AI coding agent. You ask the agent to fix it. It "fixes" it. But the bug is still there, or a second bug appears.
So you say "it's still not working." The agent tries again. Twenty minutes later you have more broken code, fewer credits, and no clear path back to a working state.
People search for this with phrases like "AI keeps making bugs worse" or "agent stuck in a fix loop." It's not a quirk of one product. Lovable, Replit, Cursor, Claude Code, Base44, and similar tools all fall into the same pattern, because the failure is structural.
This tutorial explains why the loop happens and gives you a concrete sequence you can use to break it on any of those tools.
Here's What We'll Cover:
- What You'll Learn
- Prerequisites
- What the Fix Loop Looks Like
- Why the Loop Happens
- How to Break the Cycle
- A Worked Example
- A Checklist You Can Reuse
- Conclusion
What You'll Learn
- How to recognize an AI fix loop early
- Why vague retries make the next attempt worse
- A five-step sequence to stop, revert, restate, isolate, and verify
- How to write a fix prompt that carries enough information for the agent to succeed
Prerequisites
You don't need to be a professional engineer to follow along here. But you should have:
- An app you're building with an AI coding agent (like Cursor, Claude Code, Replit Agent, Lovable, or similar)
- Access to version history, checkpoints, or Git so you can undo a bad change
- A way to run or preview the app yourself (browser preview, local server, or deployed URL)
What the Fix Loop Looks Like
Strip away the product branding and the loop looks the same everywhere:
- Something is wrong in the running app.
- You ask the agent to fix it with a short message ("it's broken", "try again", or a one-click "Try to Fix").
- The agent produces a change that sounds confident.
- The original problem remains, or a neighbor breaks.
- You retry with similarly vague feedback.
- Each failed attempt stays in the conversation context, so the next attempt reasons over noise.
Different tools expose this in different UIs. Some have a literal retry button. Some hang on "Thinking." Some quietly revert a change you already confirmed. The surface differs, but the mechanism doesn't.
Why the Loop Happens
Four forces compound in roughly this order.
1. Context Degrades as the Session Grows
Every message, diff, and "no, not that" adds tokens to what the agent must hold. [...]

## [39] AI glasses face their first major government crackdown
Ars Technica | full text via Ars Technica | ~207 words

Norway has become the first major country to propose a temporary ban on the use of AI glasses in selected public places amid growing privacy concerns over wearable technology.
The rich Scandinavian country’s center-left government said on Monday that it would introduce a law to parliament soon on a temporary ban for places such as parks, beaches, schools, and kindergartens. It will also set up an expert group to propose permanent national rules.
“I am concerned about the introduction of powerful new technology where people risk being photographed, filmed, or recorded without their knowledge,” said Torgeir Micaelsen, Norway’s digitalization minister. A temporary ban “will give us time to conduct a thorough assessment and hold an informed debate that can lay the foundation for permanent regulation,” he said.
Governments around the world are grappling with how to regulate AI glasses—including those from Facebook owner Meta and cheaper copycat devices—amid worries that they are being used to film people without their consent, including children and women in settings such as changing rooms.
Parts of Norwegian society have already reacted with their own bans, including schools in the capital Oslo and the country’s biggest company, oil and gas major Equinor, which has banned them from its offices and offshore facilities.

## [84] OpenAI will start watermarking ChatGPT’s text in the EU
TechCrunch | full text via TechCrunch | ~477 words

OpenAI will start adding an invisible watermark to text generated by ChatGPT and Codex in the European Union to comply with the EU AI Act, the company said Monday in a blog post.
The EU AI Act’s transparency rules, which took effect on August 2, require AI companies to mark AI-generated content in a way other systems can identify.
OpenAI said the watermark will roll out over the coming weeks to eligible ChatGPT and Codex users on all plans, but only in the EU. Developers using OpenAI’s API anywhere in the world can turn it on for select models starting today; it’s off by default. OpenAI said it is not making text watermarking a global default at launch.
The watermark is not an actual symbol, but works by subtly shaping the model’s word choices, leaving a pattern readers can’t see, but a detector can pick up. Because it lives in the words themselves, it travels with the text when it’s copied and pasted. OpenAI said the watermark doesn’t identify the user, and that it saw no meaningful change in its models’ performance with it switched on.
OpenAI also published a technical report for its method, called textGrain, alongside the announcement. Co-written with researchers from the University of Pennsylvania and Yale, it walks through an example of using a secret key to sort next-word predictions to finish the sentence. Add hundreds of these nudges together, and the detector can spot AI-generated content using only the text and the key.
Can the watermark be removed by editing? OpenAI’s tests suggest yes. In one test, replacing 10% of words with synonyms dropped detection from about 92% to 66%. The company also said short passages, math answers, and translated text are harder to detect.
“These limitations contribute to our decision to provide initial detector access only to approved researchers and expert organizations, who can help us evaluate reliability and responsible uses,” said the company.
OpenAI also cautioned that a missing watermark “does not prove human authorship.” The text could be too short or too heavily edited, or it could come from another company’s AI.
“[Watermarks] can indicate that an OpenAI system generated or processed part of a passage, but not how much human judgment, editing, or creativity went into it,” the company said.
The announcement comes two months after Anthropic said it would watermark text generated by Claude, a move it’s applying worldwide. [...]

## [38] Our approach to EU text provenance rules
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~22 words

How OpenAI is approaching text watermarking under EU rules. Learn where watermarks apply, how detection works, and why access starts with researchers.

## [153] Meta Muse Explained: What It Is, How It Works, and What It Can Do
KDnuggets | full text via KDnuggets | ~2168 words

Meta Muse Explained: What It Is, How It Works, and What It Can Do
Meta has entered the AI agent race in a big way.
On September 8, 2026, Meta launched Muse, a personal AI agent designed to do more than just answer questions. Muse can browse websites, connect to your apps, send emails, make purchases, fill out forms, manage longer-running goals, and continue working even after you close the app.
Chatbots such as the early versions of ChatGPT mostly followed a simple pattern:
You ask — AI answers.
Muse is designed around a different pattern:
You give it a goal — it plans — uses tools — takes actions — monitors progress — comes back when it needs you.
Meta CEO Mark Zuckerberg said this when announcing the product:
"Introducing Muse, the personal agent that understands your goals and works 24/7 to get things done for you."
Muse quickly climbed the U.S. App Store charts, while its ability to perform real actions has also raised questions about privacy, reliability, security, and how much control we should hand over to AI agents.
So, what exactly is Meta Muse? And what makes it different from the AI assistants we already have?
What Is Meta Muse and How It Works?
Muse is Meta's personal AI agent.
It is built to understand your goals, remember useful information about you, connect to services you use, and perform tasks on your behalf. You can communicate with Muse using a regular chat interface, either through the Muse app or through WhatsApp.
When you give Muse a task, several components work together behind the scenes.
1. You Give Muse a Goal
Suppose you say:
Plan a three-day trip to New York next month. Find flights that fit my schedule, shortlist hotels near Manhattan, and keep the total under my budget.
A chatbot might give you recommendations and links.
Muse can potentially go further.
It can investigate options, browse websites, compare results, remember your constraints, continue working in the background, and ask for approval when an action requires your confirmation.
2. Muse Spark Plans the Task
The reasoning engine behind Muse is Muse Spark 1.3.
Meta says the model has been specifically trained for long-running agentic workflows. Instead of treating every prompt independently, it can keep track of information discovered earlier, operate across multiple workflows, use tools, identify gaps in a plan, and continue working toward a larger objective.
This is important because real-world tasks rarely involve a single API call. [...]

## [14] Qualcomm licenses patents on Huawei’s LogicFolding chip tech
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [19] Quoting Felix Rieseberg
Simon Willison's Blog | full text via Simon Willison's Blog | ~214 words

5th October 2026
The "old" version of Cowork runs model inference in the cloud, executing tool calls in an Anthropic-provided VM we shipped to your computer. We added the VM for capability, safety, and security reasons - mapping in just the data you explicitly added to your session. People loved what they were able to do with Claude but didn't love the disk, battery, and performance cost of running the VM locally. Also, people didn't love that closing your laptop means the work stops.
The "new" version of Cowork runs model inference and the VM in the cloud. Each session gets its own sandbox, not sharing state with other sessions. When the VM needs something on the users' device (like a file), the desktop app is responsible for that file access tool call. [...]
We think this solves a lot of problems we've heard about (like using Cowork from a phone, keeping work running, or getting all the same power without losing battery to the VM)
— Felix Rieseberg, Anthropic, see also this help page
Recent articles
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026
- 2026 in LLMs (so far) - 27th September 2026

## [81] Agents Don't Need Memory. They Need Documentation.
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1018 words

Agents Don’t Need Memory. They Need Documentation.
A memory plugin analyzes your conversations. It generates 1,000 isolated snippets and inserts them into a vector database. With your every prompt, it attaches the five most similar snippets; if the agent is confused (which it is), it manually searches for more. That’s the product they call “memory.”
It’s a strange thing to use when you think about what problem you’re trying to solve. You want your agent to understand your project. To know where a feature is, why it was built, what you agreed on and what you care about. Instead, you get a lottery over RAG snippets, injected on every prompt, hoping the right ones float up.
Even when it does work, the agent still doesn’t understand your project. The entire memory plugin ecosystem is solving the wrong problem.
Because agents don’t need memory. They need documentation.
It’s All Just RAG
Every memory plugin on the market works the same way:
- Go through session transcripts
- Generate snippets of “memories”
- Insert into a RAG database
- On every prompt, retrieve the top 5 and inject
- Need more? Give the agents a tool to search through the RAG database
That’s the whole architecture. Some tools are extra fancy; they let the agent search through past transcripts word for word. Or they implement some kind of multi-tier memory system that classifies short or long-term memory. Or they add a bunch of background daemons to review, merge, or deduplicate memories. “Dreamers” that rewrite memories overnight. Continuous context compression. Rerankers. Et cetera.
Each plugin tries to add new token-burning “features” to fix the same flawed architecture underneath. And that’s why none of them reliably work.
The Problem with Recall
All of these memory plugins suffer from the same broad set of problems.
- Memories are surfaced by similarity. Similarity search ranks how close two snippets are in embedding space. That’s it. You don’t know which is correct, current, or what’s missing.
- Memories are stored without context. A RAG snippet can only contain so much. You lose everything else: context, motivations, lessons, environment, and more.
- The past is treated as truth. All of these plugins rely on recall; whether it’s search through transcripts or a vector database. But the codebase changes everyday; so how accurate are each of the 500 snippets about authentication?
- Agents can’t search for what they don’t know. [...]

## [157] How I made a paid Mac app in 11 days with Claude – without writing a single line of code
ZDNet | full text via ZDNet | ~2488 words

ZDNET’s key takeaways
- I shipped a Mac app without writing a single line of code.
- Vibe coding took 502 directives, not one magic prompt.
- App Store promo images took almost as long as the app.
At around noon on Sunday, Sept. 20, I came up with an idea for a Mac app. One week later, on Sunday, Sept. 27, also around noon, I submitted my completed app to Apple. Four days later, Apple accepted the tool, and it went live on the App Store.
Also: AI completely changed how I develop iPhone apps … and I think I love it
This is the story of an unrelated assignment by a ZDNET editor, a happy accident, and vibe coding at its best. It began 30 years ago, with a giant library of icons.
More from ZDNET
Icons were good to me
When I started my first software company, one of the first products I introduced was Icon Factory for HyperCard. It won several awards. This product supported my company and our employees for years. Those icons were all black and white, as was HyperCard.
Also: After the vibe-coding rush comes the debugging hangover
In 1997, after years of customer requests for colorful Finder desktop icons, we created a three-volume set of 32×32 pixel color icons called Icon Gallery. This was a boxed product of more than 2,000 icons. Icon Gallery sold through retail, mail order distribution, and direct mail.
Icon Gallery was one of the last boxed software products I produced. I’ll be honest with you. I can’t recall when or why I stopped selling Icon Gallery, but it probably tracked with when I stopped physically manufacturing boxed products. That decision, of course, tracked with the rise of the web.
Now, let’s fast forward to a few months ago. While decluttering some cubbies in my office, I found the packaging for a couple of my old software products, including Icon Gallery. I stuck the box on a shelf. Once again, I pretty much forgot about it.
Then, last month, in honor of this year’s big iPhone event, my editor asked me to write a series of historical Apple stories. While writing ‘AI completely changed how I develop iPhone apps … and I think I love it,’ I dug through my server for a screenshot or box illustration of an AI product I produced for the Mac in the late 1980s.
Also: I used Claude Code to vibe code a Mac app in 8 hours, but it was more work than magic
I found that image, and I also found an old Macromedia Director file containing all 2,338 icons from 30 years ago. [...]

## [25] Command-line tool quickly removes Apple Intelligence from macOS 27
Ars Technica | full text via Ars Technica | ~206 words

A new tool is allowing Mac users the ability again to easily turn off Apple Intelligence with one click and free up to 12GB of storage.
Unlike with previous versions of macOS, macOS 27 Golden Gate doesn’t have a toggle for turning off Apple Intelligence. That makes disabling AI features that you may not want more difficult. It also means that the AI models necessary for running Apple Intelligence will take up space on your disk, even if you don’t use them or if you go through your settings to individually find and disable AI capabilities.
In response, a developer known as Om Lahore on GitHub last week created RemoveMacAI, a command-line tool that allows macOS 27 users to “turn off Apple Intelligence on macOS 27″ in a way that is “fully reversible,” per the GitHub page. They said that Apple’s Intelligence models take up “about 12GB,” but the models can actually take up over 30GB, The Verge noted.
RemoveMacAI “turns off Siri, Writing Tools, Genmoji, Image Playground, the ChatGPT extension, and all the summaries, then it deletes the models and stops macOS from downloading them again. Dictation still works because it’s a separate setting,” the developer said in a Reddit post first spotted by MacRumors.
