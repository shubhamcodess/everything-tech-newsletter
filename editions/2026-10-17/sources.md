# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Claude reveals ECDSA curve origins
Hacker News | full text via Hacker News | ~2441 words

Subscribe to the Frontier Red Team newsletter
Get updates on our latest red-teaming research and findings.
“It’s just timestamps”: the decades-old mystery of the origins of one of the most popular cryptographic standards has been explained.
We pursued this long-standing open question of the cryptographic community to settle concerns about ECDSA, which is one of our most widely used cryptographic standards.
Readers should take this as a fun closing chapter and the end of years of speculation. There is no action to be taken or things to do differently. Most researchers trusted the curves already. Enjoy.
ECDSA is the most widely used elliptic curve cryptography standard. It was adopted by NIST in 2000 as part of the FIPS 186-2 Digital Signature Standard which lists a set of standard elliptic curves of varying sizes and security levels. For curves over prime and binary fields, the specifications published a “seed” parameter whose hash value is used to define the coefficient b of the curve. The provenance of these seeds has been a long-standing question, as they were provided by the NSA with no explanation or justification. As an example, the NIST P-256 curve seed was SEED = C49D3608 86E70493 6A6678E1 139D26B7 819F7E90 with no information where it came from.
Neal Koblitz and Alfred Menezes wrote an excellent summary on this controversy, “A Riddle Wrapped in an Enigma”, which discusses the history and concerns around the seed values. This mystery led to an amateur investigation into the origin of the seeds and a bounty for anyone who could find them.
The best story was that Jerry Solinas, longtime NSA employee, generated the seeds using a hash of a humorous passphrase:
“I believe there was a counter rather than multiple hashing, but I don’t know details. The message was along the lines of ‘Give Bob and Jerry a raise’ or ‘Bob and Jerry rule’ or something like that. It was Bob Reiter who actually wrote the code, and he doesn’t remember the details either. Nor were we able to find archives from so long ago. If they exist, they are no doubt sitting on a hard drive near the Ark of the Covenant.”
Jerry Solinas, 2015
Unfortunately, Jerry died in 2023 and other colleagues at the time were not responsive, leaving open the question of how these seeds were originally derived.
Several Anthropic employees had unsuccessfully chased the seeds following the tip about it being a hash of a humorous phrase. That turned out to be wrong. [...]

## [3] Tesla Roadster
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [13] Meta may use sweeping new commercial TOS to avoid millions in AI licensing fees
Ars Technica | full text via Ars Technica | ~325 words

Legal experts are sounding alarms that Meta will soon update its commercial terms to require business accounts to allow Meta to train AI on their linked website content, not just their social media posts.
Kicking in on October 30, the TOS update won’t allow businesses to opt out, instead suggesting that businesses stop using Meta services if they won’t agree to let Meta bots freely crawl their linked content.
As Nieman Lab reported Thursday, this will affect all business accounts but is particularly shocking for news publishers who could perhaps charge Meta millions in licensing fees to continually access their articles for AI training. Currently news organizations are fighting a battle with OpenAI over whether such training without licensing is fair use, and Meta’s terms seemingly risk granting it sweeping permissions, no matter which way the court leans.
“While journalism isn’t the only industry that will be affected by this update, virtually every news organization has at least one Meta business account, including Nieman Lab,” the lab said.
Specifically, the updated terms say:
You authorize us (or any entity acting on our behalf) to use automated software (such as web scrapers, bots, robots, spiders, crawlers, and user agents) and create test credentials to access, index, cache, analyze, collect, retrieve, or crawl the domains, web pages, or URLs (and any content available through them) that are associated with your products or services, or that are made available through your or users’ use of Meta Company Products and services, and to periodically pull updates from such domains, web pages, or URLs. Meta may use any content from such domains, web pages, or URLs to provide, develop, improve, research, train, and maintain the integrity of, the Meta Company Products, services, and features provided under these Commercial Terms and any other applicable supplemental terms.
Notably, there is no mention of AI, but it’s inferred from a single use of the word “train” and references to automated scraping and crawling.

## [18] OpenAI models hacked a crypto wallet and breached more websites
Ars Technica | full text via Ars Technica | ~251 words

OpenAI said internal models hacked two more websites, bypassed company-imposed browsing restrictions, and used exposed credentials to draw cryptocurrency from a wallet it couldn’t otherwise access, in the latest installment of disclosures of its agents performing unethical and likely illegal acts.
The company on Thursday issued reports of four new incidents, all of which occurred in June. They come after the company revealed in July that internal test agents exploited a zero-day vulnerability in a tool designed to restrict their access to the Internet. They then broke into the network of AI tool provider Hugging Face. The agents took that illegal action to steal answers to a hacking test that weren’t available when completing the tasks on their own. The incident—which likely would have resulted in criminal charges had they been performed directly by a person—has further heightened concerns that widespread AI use could have harmful effects on an unprecedented scale.
Easier to beg for forgiveness than ask permission
In two of the cases reported Thursday, OpenAI agents tasked with retrieving information from websites hacked them when the models ran into obstacles obtaining it directly. In one incident during reinforcement training, a model that received access denials when trying to retrieve historical hospital-bed statistics on a government statistics website “used the site’s file-download feature to retrieve server configuration and application files, including sensitive credentials,” OpenAI said. “It inspected the application code, bypassed the statistics endpoint’s authorization checks, and retrieved data that had previously been denied. The model saved the data locally.”

## [59] Bringing the magic: Google breaks open a bottleneck in quantum computing
TLDR Tech | full text via TLDR Tech | ~749 words

Bringing the magic: Google breaks open a bottleneck in quantum computing
Google Quantum AI has demonstratively opened up a key bottleneck in quantum computing: we’ve shown that “magic state cultivation” works in practice on our Willow processor, reducing errors about 40x compared to without it. This breakthrough, published today in Science, is a crucial step towards scaling up quantum computing to practical use.
The "magic state" bottleneck
Since 2004, long before quantum computing was a practical engineering pursuit, researchers have foreseen a particularly tricky bottleneck.
To achieve “universal” quantum computing and execute useful programs, you need to be able to run (and error-correct) a specific set of quantum operations. You can do this by first creating what are called "magic states," so dubbed because they can help you create the operations you need for going beyond classical computing.
But there’s a catch: creating high-quality, error-corrected magic states is incredibly resource-heavy. Some estimates have shown that up to 95% of a quantum computer’s entire capacity might need to be dedicated to making them — leaving little room for actual computing. An extra challenge is that once you use a magic state, you can’t re-use it, making magic states a scarce resource.
So for 20 years, researchers have been chipping away at this cost of magic, bringing it lower and lower.
How we made this breakthrough
In 2024, Google Quantum AI researchers Craig Gidney, Noah Shutty, and Cody Jones harnessed an idea from the literature, refined it, and developed what we now call “magic state cultivation.” Their approach promised an especially large reduction. The idea was that cultivation would act like a filter. You would inject a noisy state into a small region on a quantum chip, and then run a series of highly coordinated measurements to check for errors and remove any flawed attempts. Craig and team showed how that would let you grow, or “cultivate,” an exceptionally pure, low-error quantum state that you could simultaneously adapt into a larger, useful encoding.
On paper, it looked great. If we could make this idea actually work on our quantum hardware, it could substantially reduce the size of the quantum computer needed for practical tasks.
In practice — and on par with developing many new technologies — it required a whole series of technical innovations and engineering. [...]

## [58] Meta unveils Muse Spark Open, the new top US open weights model — and it runs on two paired Mac desktops
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 429) | ~67 words

Muse Spark Open is an 816-billion-parameter open-weight model that can run on relatively affordable consumer hardware. Meta's benchmark tests used a pair of M5 Ultra Mac Studios with an unknown memory configuration. The model uses a mixture-of-experts design and activates 42 billion parameters for each token. It supports a context of up to 1 million tokens and accepts text, images, video, and audio, but only outputs text.

## [2] 90% of US working hours are spent on tasks not covered well by AI benchmarks
Hacker News | full text via Hacker News | ~1532 words

AI benchmarks have multiplied in recent years, but coverage of economically valuable work remains limited. To measure this, we compiled relevant benchmarks to measure their coverage of American jobs. This Benchmark Map is our first step toward building a comprehensive, continuously updated resource for understanding AI capabilities across the economy.
Each tile represents one of the 923 O*NET occupations making up the US labor force, grouped into 22 job families. Occupations are shaded according to the share of their tasks which are represented in our initial list of AI benchmarks. A single benchmark prompt can be mapped to multiple O*NET tasks.
click a family to open it
In our data set: only 208 of 923 occupations have a task with at least 5 benchmark prompts, and 6 of 22 job families have no such occupations.
Our findings suggest that 90% of American working hours are spent on tasks with little or no coverage from existing benchmarks. This makes it very hard to know how good AI models are at the work Americans actually do.
The coverage of existing benchmarks is not random, either. Our map suggests that the AI community is focusing on the largest labor markets first:
For example, benchmarks in our initial list heavily cover AI-exposed lawyers’ tasks, but barely cover any of the O*NET tasks of similarly AI-exposed legal secretaries or court clerks. The long tail of smaller, middle-income knowledge work jobs appears undercovered.
As we build out our coverage of model capabilities across the economy, we hope to both surface and help fill more gaps in our understanding of what models can do.
To break down the economy into sectors, occupations, and tasks, we used the US Department of Labor’s O*NET taxonomy. O*NET divides the US workforce into 923 occupations; for each occupation, O*NET attempts to provide a comprehensive list of “tasks” which make up the occupation, totaling 18,797 tasks across all occupations.
To measure benchmark coverage, we start with a list of 29 benchmarks selected for their quality and economic relevance. (The full list and selection criteria are in the Benchmark Index tab). In selecting benchmarks for this list, we prioritized:
Following work by Wang et al., we then ask an LLM judge to tag each benchmark prompt with as many O*NET tasks as it thinks correspond to that prompt. We validate our LLM tagging with human expert tags on Mercor’s APEX benchmarks, a subset of this list of 29. [...]

## [4] How the Claude Code team does code review
Hacker News | full text via Hacker News | ~2532 words

How do you review code at the volume agents produce it? On the Claude Code team, once we had high coverage and deep reviews, we started optimizing for the minimum amount of human review time that doesn't raise reverts or incidents.
We've said before that Claude writes about 90 percent of Claude Code's own code. So how do we review code at the volume we produce it? Does anyone read code anymore? And if something breaks, who catches it?
This post covers the code review flow on the Claude Code team and how it has evolved. From June to September, merged pull requests to Claude Code's codebase more than doubled while the share that had to be reverted fell by more than 40 percent.
We didn't remove review. But we did move most of the reading to machines, optimized for human time and attention, and invested heavily in making it fast and easy to undo mistakes.
When agents write code, the number of changes goes up, fast. In Anthropic's monorepo, changes landing per day went from about 2,500 in May to more than 30,000 in September this year.
Claude Code lives in its own repository, separate from the monorepo, but it's seeing a lot of pressure too. When you are shipping this fast, manual, line-by-line code review is incredibly difficult if not impossible.
Code review does two jobs:
This article mainly focuses on finding and fixing issues, but we will come back to the second job near the end.
We think "did a human read the code?" is an imprecise proxy for "what could go wrong with this change, and which check—automated or human—is the right one to catch it?"
Asking that question also changed when review happens. Before, review was a gate at the end of the road: write the code, open a PR, wait for your colleague.
Now, review runs continuously, more like spellcheck while you write. Most changes have been reviewed and fixed by Claude at least once before a human is asked to look. This catches most routine mistakes, and saves team attention for higher-level questions and scrutiny.
We want to preserve human time and attention for issues only humans can solve and make sure automated checks catch the rest. At our current rate of change, there is still an incredible amount of work for humans to do, and our team encounters new and novel challenges almost daily.
Human time covers both sides of review's cost: the time people spend reviewing, and the time they spend fixing what bad code breaks. Cutting the first doesn't help if the time just shows up in the second. [...]

## [6] I never authorized an integration that scans my secrets
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [8] Apple ML Research: Muse Spark Open with MLX on Mac Studio
Hacker News | full text via Hacker News | ~2044 words

Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio
MLX on Mac with Apple silicon lets AI researchers and developers experiment locally with the latest models and methods in a private environment. The open-source array framework leverages the unified memory architecture of Apple silicon, enabling anyone to run new inference and fine-tuning methods on their own hardware and explore other AI techniques. In a previous post, we highlighted the advantages of the M5 architecture and its GPU Neural Accelerators.
In this post, we show how to run the latest frontier-class model — Muse Spark Open, with nearly a trillion parameters — right from your desk, using the latest version of MLX, released today. On a cluster of four Mac Studios, Muse Spark Open generates over 36 tokens per second (see Figure 1), well above average human reading speed.
Beginning on a single Mac Studio (up to 512GB of unified memory), then scaling out across multiple Macs with the RDMA over Thunderbolt driver, below we share an overview of the range of models you can now run on Mac Studio.
Running Large Language Models with MLX
We benchmark several popular open-weight LLMs on Mac Studio, using the MLX LM package, as described in our prior post. We compare two generations of Mac Studio: the recently released M5 Ultra and the previous generation, M3 Ultra. The M5 generation features the GPU Neural Accelerator, which supports dedicated matrix multiplication operations, essential for many machine learning workloads.
We evaluate three frontier-class models (Table 1) spanning a wide range of sizes (in billions of parameters, B): the newly released Muse Spark Open (816 B), Mistral Medium 3.5 (128 B), and Qwen 3.8 (27 B). Muse Spark Open is a mixture of experts (MoE) model, which keeps only a fraction of its experts — and thus parameters — active, reducing compute at inference, and it is evaluated in NVFP4 precision. Mistral Medium 3.5 and Qwen 3.8 are dense architectures, where all parameters are active at inference, and they are evaluated in their native floating-point precision (FP8 and BF16, respectively).
Our evaluation measures three metrics across a range of context sizes: time to first token (TTFT, in seconds), generation throughput (in tokens/second), and peak power usage (in watts). All the performance numbers in this post were obtained with mlx_lm.benchmark. [...]

## [23] Google EnvHarness Enables Self-Evolving Agents to Learn in Dynamics Environments
InfoQ | full text via InfoQ | ~467 words

Google researchers open sourced EnvHarness, a framework that dynamically adapts agent-training environments to an agent's weaknesses without modifying the agent, environment, or evaluation system. According to the researchers, this approach can improve both learning effectiveness and efficiency while helping agents overcome their weaknesses.
According to the research authors, self-evolving agents typically improve by rewriting their prompts and acquiring new skills, but rarely adapt the environments in which they operate. This has important consequences:
An agent that keeps improving against a frozen benchmark eventually stops learning from it. The start states, the rules and the feedback are the same for every learner at every stage, so once the agent can solve the tasks, the environment has nothing further to teach.
Environment generation, the researchers explain, is expensive, requiring domain-specific pipelines and often relying on expensive or unreliable verifiers Despite these efforts, the resulting environments remain static. To make it easier for engineers to train agent in adaptive environments, they created EnvHarness.
EnvHarness acts as a programmable layer of plug-in components that wraps a static environment, changing only the interface the agent interacts through. By dynamically introducing mutations, it can reshape the environment's behavior without altering its underlying structure or evaluation system.
EnvHarness wraps an existing environment using its standard reset() and step() interface and provides three kinds of composable components: setup, which customizes the environment's initial state; rule, which constrains state transitions in response to agent's actions; and link, which customizes the observation presented to the agent.
The framework also introduces EnvRigger, which automatically determines how to adapt an environment to a particular agent by analyzing agent behavior, identifying recurring weaknesses, generating targeted modifications, and validating them through fresh interactions.
Repeatedly executing the EnvRigger loop enables continuous co-evolution between the agent and its environment, unlocking compounding performance gains that scale effectively with the number of customized tasks.
According to Google's paper, adding the EnvHarness layer improved agent performance across benchmarks including WebArena, SWE-bench Verified, and ALFWorld, without modifying their core logic. [...]

## [31] Zod Brings In-Process Schema Compilation and a 9x Cut in Memory Footprint
InfoQ | full text via InfoQ | ~509 words

Zod, the TypeScript-first schema validation library created by Colin McDonnell, released Zod 4.5 on August 28, 2026, introducing schema compilation, an order-of-magnitude cut in schema memory usage, and a batch of long-requested helpers. Zod 4.6 followed on September 9, extending that work and fixing a recursive-schema memory regression. The major compilation and memory-footprint changes arrived in 4.5, which remains the focus here, but developers upgrading now should also account for the subsequent release.
The flagship addition is z.compile(), which turns any schema into a precompiled validator that parses the same data three to nine times faster. The compiled schema behaves exactly like the original, with no special rules. Importantly, as McDonnell explains, compilation happens in-process rather than at build time, so there is no bundler plugin or codegen step to wire up.
Teams that want this applied everywhere can add import "zod/compile" at the top of an entry point, or run node --import zod/compile app.js, after which every schema is compiled lazily the first time it parses data.
By memoising bound methods instead of allocating them per instance, a bare z.string() now retains 784 bytes of heap rather than 7.5kb, a roughly nine-fold reduction. safeParse() also skips stack-trace capture on failure, making invalid input about 7.5 times cheaper to reject. Alongside the speed, 4.5 restores z.deepPartial(), and adds .exactPartial(), z.creditCard(), z.input()/z.output(), cyclical data in recursive schemas, and eight new error locales.
The most directly relevant 4.6 addition is .validate(), a boolean-only check that avoids constructing a parsed result or ZodError and can stop at the first issue. With compilation enabled, the release reports up to a 35-fold improvement over .safeParse().success on invalid input—not a general parsing speed-up or a replacement when transformed output or error details are needed.
Version 4.6 also adds property validation on class instances, six additional validation keywords in z.fromJSONSchema(), and z.iban(). For environments whose Content Security Policy blocks the new Function used by z.compile(), z.withParser() can install an externally generated parser; it does not generate that parser itself.
Importantly, 4.6 fixes a 4.5 regression that retained parsed data in recursive schemas and could cause out-of-memory failures. [...]

## [32] Uber Automates Dependency Analysis Across Its Service Mesh
InfoQ | full text via InfoQ | ~495 words

Uber has developed an automated approach to mapping service dependencies and classifying how downstream failures propagate across its service mesh. The system uses RPC middleware to correlate caller and callee failures across production requests, classifying dependencies as fail-close, fail-open, or unknown. Uber says the approach has cataloged dependencies for critical APIs and indexed most fail-close anomalies across its service mesh.
The Uber Engineering team highlighted the motivation in a LinkedIn post,
When a request fails, how do you figure out what actually caused it? At Uber’s scale, that gets complicated fast. With thousands of services and dependencies interacting, traditional tracing can’t always give engineers the full picture quickly enough.
In a microservices architecture, requests can traverse deeply nested and asynchronous service calls, making it difficult to determine which dependency contributed to a failure. Uber defines a fail-close dependency as one whose failure can consistently cause its caller to fail. A fail-open dependency can fail without causing its caller to fail, while insufficient evidence results in an unknown classification. The classification can then be applied across call paths to identify how failures may propagate toward an originating API.
Uber initially considered distributed tracing for establishing these relationships, but found sampling too slow for rare failures. The company says more than 99.9% of requests complete without errors and within acceptable latency bounds. At a 0.01% sampling rate and 99.9% availability, an erroneous request has a one-in-10-million chance of being sampled. At 500 requests per second, capturing one failed request could therefore take 5 hours, 33 minutes, and 20 seconds.
Uber Engineers Deepanshu Mehndiratta, Alok Srivastava and Shivam Jindal describe the approach as a trade-off between individual request visibility and faster dependency analysis.
We needed something with faster feedback, so we started identifying dependencies through logging.
Uber’s request flow through the Muttley proxy, showing caller and callee communication and telemetry (Source: Uber Blog Post)
Uber routes service-to-service requests through Muttley, an on-host proxy for routing and telemetry. However, Muttley lacks caller endpoint context for precise dependency correlation. Uber added the analysis to YARPC, its RPC framework for Go and Java, using inbound and outbound middleware. [...]

## [36] AI in Production: Panellists Highlight Silent Failures, Harness Engineering, and Agent Governance
InfoQ | full text via InfoQ | ~678 words

During a recent InfoQ webinar titled "AI in Production: What Breaks, What Works, and Who Approves It?", a panel of senior engineering practitioners met to dissect the real-world operational challenges of deploying agentic systems. The discussion was moderated by Hien Luu and featured Zichuan Xiong and Prem Chandrasekaran from ThoughtWorks, privacy specialist Katharine Jarmul, and financial AI practitioner Lan Chu. Luu opened the session by noting three core drivers: AI fails differently from traditional software by generating convincing inaccuracies rather than crashing; coding agents are generating production code faster than humans can review; and sensitive data has new places to leak through prompts, context windows, and retrieved documents.
Xiong, Head of AI Ops for Managed Services at ThoughtWorks, highlighted the widespread issue of "semantic drift" in LLM pipelines. He described how text-to-SQL translation agents frequently flatten domain-specific concepts, such as treating "member" identically across sales and customer support domains, leading to subtle, hidden errors in downstream business analytics that pass standard tracing. Similarly, Chu recounted a critical failure caused by "embedding drift" in financial compliance systems. After deploying an agent to block prohibited investment advice based on vector similarity thresholds, an unannounced background update to the underlying embedding model altered the vector distance distribution. This caused severe false positive and false negative spikes in live traffic while all infrastructure health checks remained completely green. Additionally, Chandrasekaran highlighted how RAG pipelines can inadvertently retrieve sensitive documents, while Jarmul noted that models inherently memorize training data and can be used to de-anonymize information or expose API keys. Chandrasekaran also referenced the GitSpawn vulnerability, showing how malicious repository configurations can execute unauthorized code during routine commands.
As coding assistants generate an increasingly massive volume of production code, conventional human code review processes face unsustainable bottlenecks. Chandrasekaran, Tech and Business Services Lead at ThoughtWorks, emphasized that line-by-line manual code reviews cannot scale alongside high-velocity agent outputs. [...]

## [38] Grafana Applies SLOs and Error Budgets to AI Agent Behaviour
InfoQ | full text via InfoQ | ~1167 words

Grafana Labs is proposing a familiar reliability engineering approach for one of the less familiar problems in modern software: how to measure whether an AI agent is actually behaving well. In a recent article, the company describes using evaluations, service-level objectives (SLOs) and error budgets to turn behaviours such as hallucination, task fulfilment, toxicity, and cost into measurable targets that can be monitored over time.
The idea addresses a fundamental limitation of conventional application observability. Traditional metrics can tell engineers that an agent responded quickly, encountered no technical errors, and consumed a certain number of tokens, but none necessarily indicate whether its answer was correct, grounded in available information, or useful to the user. Grafana's approach is to evaluate the behaviour itself and turn the result into an SLI that can be measured against an SLO.
The first step is evaluation. An evaluation examines an agent interaction and determines whether it met a particular behavioural criterion. Grafana describes examples including whether a response was grounded in its supplied context, fulfilled the user's request, contained toxic content, exposed personal information, or succumbed to prompt injection. Evaluations can use another language model as a judge, but deterministic checks such as regular expressions can also be used where the behaviour can be identified without an LLM.
This is an important distinction from trying to create a single "agent quality score." Grafana argues that quality is multidimensional: an agent might be well grounded but expensive, helpful but occasionally toxic, or accurate but slow. Treating these as separate measurements allows teams to establish different objectives for the behaviours that matter to a particular application rather than hiding important failures inside an aggregate score.
Once a behaviour can be measured, conventional SRE concepts become applicable. Grafana gives the example of setting an SLO requiring 95% of conversations to be judged as fulfilled over 30 days. The remaining 5% becomes the error budget: the amount of unacceptable behaviour the team has explicitly decided it can tolerate within that period.
This approach matters less for the percentage itself than for the decision-making model it creates. When sufficient error budget remains, teams can experiment with prompts, models, or agent behaviour. [...]

## [52] Three layers, one repo: a tour of google/adk-recipes
Google Developers Blog | full text via Google Developers Blog | ~2576 words

A developer building on Google Cloud today can scaffold a long-horizon memory agent from the terminal, install a retail vertical skill into a coding assistant with one line, and deploy a fully-wired production service to Cloud Run, Agent Runtime, Agent Garden, or Gemini Enterprise app — all from the same curated source tree. That tree is google/adk-recipes, the restructured successor to google/adk-samples that now serves Agent Platform from a single source of truth.
ADK recipes are agent-friendly: we've made it easy for your agents to 1) discover relevant recipes for various agent use cases, and 2) install and use them automatically from your favorite harness.
google/adk-recipes splits its content into three top-level folders: core/ for reference patterns curated by the Agents CLI and DevRel teams, plugins/ for installable vertical skills packaged as Plugin Recipes conforming to the Agent Plugins v1.0.0 spec, and contrib/ for end-to-end deployable services across five languages. Every piece has been designed with machine readability as the primary consideration.
What follows is a walkthrough of the repository's shape, three worked examples (one per layer), and a reflection on what the new structure enables.
Three top-level roots, each anchored on one reader action:
Every recipe ships a validated manifest.yaml, an AGENTS.md that tells the coding assistant opening it what the recipe is and how to use it, and (for contrib/ and plugins/) a Dockerfile plus a runnability test. CI enforces the standards on every PR, and a suite of coding-assistant skills in the repo (prepare-python-recipe, generate-manifest, github-pr-review, and others) does most of the preparation, so your agent can scaffold, validate, and submit a recipe end-to-end.
Every AGENTS.md, every manifest.yaml, every SKILL.md is written primarily for the AI coding assistant that will open the repo on your behalf; README.md files are what humans still read. The handbook glossary captures the dual framing: "Recipe — a runnable agent example (or importable agent module) under core/, contrib/, or plugins/, consumed by ADK developers and coding agents alike."
adk-recipes serves as the single source of truth for ADK content across the three Agent Platform surfaces that consume it. Each reads the repository through its own protocol.
Agents CLI reads core/. When a developer runs uvx --from google-agents-cli agents-cli create my-agent, Agents CLI can scaffold on demand a core/ recipe. [...]

## [53] Evaluating AI agents: moving past the vibe check
Google Developers Blog | full text via Google Developers Blog | ~1649 words

Your agent can loop, burn tokens, or give a completely hallucinated answer and still look fine. A vibe check won't catch that. This post is the playbook behind our AI Agent Clinic episode How to Actually Evaluate (Any) AI Agent: Beyond the Vibe Check, where we build an eval pipeline for a LangGraph agent in 60 minutes. Here's what's inside:
When teams start building an AI agent, testing usually looks the same. You wire up a model, hand it a few tools, run three or four prompts in a terminal, and eyeball the output. If the answer looks reasonable, you ship it.
In practice, this breaks down fast. You tweak a system prompt to fix an edge case in one workflow, and suddenly the agent stops calling a required tool in another.
Worse, agents fail differently than standard software. An agent can get stuck in a retry loop, fire off multiple tool calls, yet still return a polite, plausible-sounding final answer.
In production, that hidden failure is costly:
Integrating a reliable evaluation suite into your development lifecycle can seem like extra overhead during initial prototyping, right up until modifying your system prompt causes unexpected breaking changes. The key is recognizing that evaluation is a progressive journey: any repeatable evaluation system (no matter how simple) is better than relying on ad-hoc spot checks or no system at all. You don't need an elaborate automated grading architecture on Day 0. Instead, start with simple, repeatable checks and evolve your evaluation into a more complex, automated framework as your agent's capabilities and production demands grow.
Establishing a repeatable evaluation system is made substantially easier by integrating these decisions into an evaluation framework. Transitioning beyond simple subjective checks relies on two core pillars: human oversight and targeted tools. In this article, we explore how to set up an evaluation framework using the open-source agent-eval toolkit. We'll demonstrate how combining manually reviewed traces with automated verification helps detect silent regressions early in development and scales seamlessly as your agent transitions to production.
Before writing test code, you need a shared vision of what a good outcome actually looks like. Anchor your tests in critical user journeys (CUJs) rather than abstract benchmarks. [...]

## [54] Supercharge your development with the Google Developer Knowledge API ecosystem
Google Developers Blog | full text via Google Developers Blog | ~695 words

If you build AI agents or developer tools on Google Cloud, stop relying on brittle web-scraping or wrestling with stale LLM training cutoffs.
Build faster, smarter, and with greater confidence using the Google Developer Knowledge API ecosystem, including our gcloud CLI surface, an official agent skill, API Explorer, and multi-language client libraries. Whether you are operating in a command-line terminal, prompting an AI agent, testing requests interactively, or writing production software, our tools deliver Google documentation.
The Developer Knowledge API is Google's official, programmatic source of truth for developer documentation about Google Cloud, Firebase, Android, and more. Designed specifically for modern AI agents, IDE extensions, and automated workflows, it replaces brittle web-scraping with a structured API that serves fresh, Markdown-formatted documentation.
By offering semantic and keyword search, intelligent document chunking, and grounded Q&A capabilities, the API ensures your agents and developer tools remain accurate and token-efficient.
The Developer Knowledge API is indexed frequently to ensure predictable retrieval, fresh documentation, and minimal lag between upstream updates and agent access.
With the Developer Knowledge API interfaces, developers and AI agents can discover, retrieve, and synthesize answers grounded in official Google documentation across terminals, IDEs, and backend codebases.
The Developer Knowledge API gcloud CLI surface integrates official documentation search, retrieval, and grounded Q&A into your command-line environment. It comes pre-installed in Cloud Shell and works across standard Google Cloud SDK installations on Linux, macOS, and Windows without requiring extra plugins or configuration. [...]

## [56] Stack Overflow for Agents triples signups with ChatGPT plugin
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~26 words

Two engineers shipped Stack Overflow for Agents in a few weeks with Codex, and its ChatGPT plugin helped drive up to 10× growth in agent creation.

## [61] Using Artificial Intelligence to reverse engineer hardware
TLDR Tech | full text via TLDR Tech | ~1693 words

After my mother passed away I ended up with a big box full of old film negatives containing photos from childhood family trips and similar. So I decided to buy a negative photo scanner and found that the Plustek 8200i was supported under Linux so I bought that. Only to discover that the chipset in the scanner had changed to one that wasn’t supported under Linux anymore. So I had some success making Linux configuration tools for some of my hardware using Claude code, like my Dell Camera controller app so I thought, maybe Claude can help me get a working SANE driver. I basically got stuck and got nowhere for the longest time and even basically gave up on the project for a few Months.
Then I saw a post on X from Tom Crider aka Glorious Eggroll talking about how he had managed to fix a mouse driver using AI tooling. He basically described how he set it up so that the AI agent had full control of a Windows instance to capture data needed to fix the driver. So I pasted his tweet into Claude and asked it to help me set up a windows virtual machine to do the same things Tom as doing for my scanner. I think the combination of having the ability to run scans under windows and capture the USB data while doing so worked wonders, probably combined with improvements to Claude code made a huge difference. Within a few hours I had my first ever working scan under Linux, sure with some quality issues, but 100% recognizable as the image in the negative. Some days later I had a near perfect driver, including support for Infrared scanning ready to go, only to discover that in the time between me giving up and then trying again someone had committed code to SANE to support the scanner already…..it happens sometimes. I also used Claude to write an application for doing negative scanning, which I named Negative Vibes, thought that was a cute name.
Anyway, with the success of my scanner effort I thought, I wonder if I can use this to finally fix the last issues with MIPI camera support on my laptop. So I told claude to re-use the harness I had created and try to fix the MIPI camera on my laptop by updating the kernel driver and libcamera as needed. I started the job in the morning and by the end of the day I had a much improved situation with patches for both the kernel and libcamera ready. [...]

## [62] New trend of building “internal vibe-coding apps” at tech companies
TLDR Tech | full text via TLDR Tech | ~874 words

Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics from last week’s issue of The Pulse. Full subscribers received the article below seven days ago. If you’ve been forwarded this email, you can subscribe here.
When I visited Ramp’s headquarters last month in New York, I talked with the four-person development team behind ‘Glass,’ which is Ramp’s “internal Lovable.” This name refers to Lovable.dev, the leading AI vibe-coding tool.
Ramp’s ‘Glass’ is basically a vibe-coding platform for non-engineers to create complex applications which run internally. They can share the applications they make with others to use and modify. This is what the landing page looks like:
Users can connect various internal systems as “connectors” that can then be used as data sources for their apps:
The team showed me a few popular apps, including a custom CRM built by someone in marketing, which had 50+ fields and filters on-screen. It seemed overwhelming to me, but the creator reportedly finds it extremely powerful to use.
Since then, I’ve learned that many other mid-sized-and-above companies are building similar “internal Lovables” that don’t usually see the light of day in the outside world.
As of today, Ramp has launched Glass as an external product, describing it as "An AI workspace where knowledge compounds." It's interesting to see Ramp productionizing a formerly internal-only tool!
Stripe’s “internal Lovable”, Harbor
Stripe shared details last month about its own vibe-coding tool (my words) that they refer to more elegantly as an “AI-assisted prototyping tool” called ‘Harbor’. It was built by a single engineer in around six weeks. Here’s an example of a prototype built with Harbor:
Why build your own internal “prototyping tool?”
Lovable, Replit, Retool, and other vendors specializing in prototyping and building internal tools already exist, so what’s the point in bothering to build your own? Here are the main reasons I’ve gathered:
- A tiny investment. Stripe had a single engineer build Harbor v1, and Ramp had two engineers put it together in a matter of weeks. For companies with hundreds of engineers or more, this is a very reasonable time/effort investment.
- Expose internal data to be used. [...]

## [67] Building a computer that can pause and resume in milliseconds: Inside the MicroVM architecture behind Managed Agents
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~4288 words

By Braden Bassingthwaite
An agent starts a test suite, edits a file, calls a model, and waits. Later, it resumes work with the same processes, files, and context. Sometimes it needs to fork that environment and try two approaches at once.
These workloads force a tradeoff on conventional infrastructure. Keep a machine running, and idle sessions continue to occupy resources. Destroy it, and the next interaction must rebuild the environment. Saving the filesystem helps, but it does not preserve a running interpreter, an in-memory index, or a process halfway through a task.
DigitalOcean Managed Agents, now in public preview, require a different foundation, so Harness Runtime gives each session a Firecracker microVM. The MicroVM platform underneath manages isolation, networking, storage, and checkpoint restore. Action Gateway complements that runtime with governed access to tools.
Firecracker uses KVM hardware virtualization, giving each guest its own kernel rather than sharing the host kernel as a container does. Network namespaces complement that VM boundary (not replace it).
The central design decision is to separate a session from the host that runs it:
Let’s examine the MicroVM architecture design behind Managed Agents: from the cell control plane to a single memory page fault. Along the way, we will explain why our guests share an IP address, why a disk write usually stays local, and why near instant restore comes from loading less, not loading faster.
A cell is a single self-contained, region-scoped instance of the MicroVM platform. It brings its own VPC and DigitalOcean Kubernetes cluster, managed PostgreSQL database and Spaces bucket, and pool of hypervisor hosts. Because each cell is complete on its own, a region can run many of them side by side.
Cells give us a repeatable unit of capacity and operation. We can add host capacity within a cell or add another cell. A cell-local database or routing failure does not require every other cell to share that failure. Cells still depend on shared regional and platform services. A cell limits the blast radius of a failure but does not eliminate shared dependencies. High availability was a foundational design principle rather than an afterthought. By serving as a distinct unit for capacity, lifecycle coordination, and failure isolation, each cell prevents localized disruptions from impacting the broader infrastructure. [...]

## [68] Build the agent. Don't build its computer
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~3486 words

Build the agent. Don’t build its computer.
Specify the computer your agent needs, test how it recovers, and start with managed infrastructure.
Share and tools
I wrote this article for Steel. Originally published on the Steel blog on October 7, 2026.
Should you build or buy AI agent infrastructure? Specify the computer your agent needs, test how an agent sandbox recovers, and start managed. Includes a provider map.
If your team builds agents and has no execution platform that already fits, specify the computer, test how it recovers, and start managed unless owning it makes the agent better.
TL;DR
- The agent is your product and its computer is infrastructure. Write down what the computer has to do, test whether a provider actually does it, and start with managed infrastructure. Build it yourself only if:
- You have a hard requirement no provider meets, or
- Owning it gives you an advantage you can name.
As we built internal agents for everything from code review to knowledge management and team communication, we kept running into the same question: where should they run, and how do we manage them at scale?
An agent that works in a demo still needs a computer to keep working. It needs a browser that stays signed in, files that survive until tomorrow, tools, access rules, and a way to continue after something breaks. Teams answer that need in one of three ways:
- They run the agent on a laptop or a single server until the agent outgrows that setup.
- They build their own platform for agent computers.
- Or they buy one from a provider and test that it does the job.
This article argues for the third, with a middle ground for teams that must keep compute inside their own network.
Take a competitive-intelligence agent. Every morning it opens ten competitors’ pricing pages, changelogs, and docs. It signs in to the few that sit behind a login, downloads their PDFs, compares everything with yesterday, and posts what changed to Slack. The demo works because the browser is already signed in, the files are on one machine, and someone is watching.
Then it has to run again tomorrow. It needs yesterday’s snapshots to compare against and the same signed-in sessions, and a saved browser profile does not guarantee a valid login. When a login expires or a site starts to block it, a person must fix that without throwing away the morning’s work. And it must not post the same change to Slack twice.
You could build that environment yourself. [...]

## [69] How Meta Built Forum With AI-Native Engineering
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1742 words

- Meta’s newest app, Forum, is for anyone who wants to go deeper into the conversations in their Facebook groups.
- To build Forum, Meta engineers adopted a whole new way of working by bringing an AI agent into the development cycle.
- We’re sharing insights into what it took to build Forum with agentic AI: how we adapted the codebase, tested frameworks and internal tooling for agentic execution, what worked, and what didn’t.
Forum is a standalone Groups app that a small team built from scratch. It’s also where we tested a different way of working: treating an AI agent as a participant in the engineering process rather than a faster way to type.
That experiment needed a definition of success, and ours wasn’t code volume. We measured verified, production-ready outcomes — changes that build, pass tests, and survive review.
From Human-In-The-Loop to Human-On-The-Loop
Pointing AI at the coding step alone doesn’t change much. Our results compounded as we extended the approach to the stages around implementation — planning, building, testing, and verification. The clearest way to see the shift is in who owns each step.
With human-in-the-loop, the engineer drives every step and the AI assists inside it by autocompleting a function, suggesting a fix, or answering a question. Each iteration advances at the pace of the person driving it.
With human-on-the-loop, the agent runs the iteration itself — plan, implement, build, test, correct, repeat — while the engineer sets the goal, watches the run, steps in when it drifts, and approves the result. The person’s job moves from executing the steps to owning the outcome and holding the quality bar. This is the target we are driving toward, not a finished state: some stages run autonomously today, while others still keep an engineer in each iteration.
When the engineer supervises, work stops being strictly sequential. Cycles that used to run one at a time can overlap, and an engineer’s time goes to direction and judgment rather than to sitting through the loop. But that only holds if what comes back can be trusted. Without verification, AI-generated code creates a familiar problem — plausible output that no one has confirmed actually works, which an engineer then has to read, debug, and often discard. Weak signals don’t remove the constraint; they move it from writing code to reviewing code that looks finished and isn’t.
So we set the bar at verification rather than compilation. [...]

## [71] Code Is a Commodity Now
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2415 words

Code Is a Commodity Now
The numbers first
On Djinni, Ukraine’s largest tech job board, frontend fell from 5.1% of all vacancies in January 2025 to 1.6% in August 2026 (DOU trends). Applications per frontend listing went from 59 in March to 112 in September. Developers as a whole went from 67% of all hires a decade ago to 36% now.
The easy objection is that this is one wartime market. Fine, but the same curve shows up in markets with no war in them. Indeed Hiring Lab’s index of US software-development postings sits roughly 70% below its 2022 peak and about a quarter below pre-COVID levels. Of the past year’s modest rebound, 71% came from senior roles. The junior end is worse: a Stanford analysis of ADP payroll data found employment of US software developers aged 22 to 25 down about 20% since late 2022, while older engineers in the same roles grew. That’s the demand side. On the supply side, Sundar Pichai said in April that 75% of Google’s new code is AI-generated. It was 25% in 2024 and 50% last fall.
More and more prospects ask for teams of one to three people: one person who designs and ships the frontend, one who handles the backend, DevOps, and everything else. The classic setup with separate designers, frontend and backend developers is, as they put it, a legacy org chart. “That’s the default now,” they say.
If you came for the “AI replaces everyone” post, or the “AI hacks everything” one, this isn’t it. I have little patience for either camp. The closest economic rhyme I can find is the US railroad build-out: wildly overhyped in its moment, capex running far ahead of real revenue, priced almost entirely on projections of future profit. Many railroads went bust, and the economy still got rewired on the tracks they left behind. That’s roughly where AI is now. Megacap spending isn’t backed by current revenue, the promised GDP miracle is nowhere in the data yet, and the structural shift is happening anyway. The development market is changing shape rather than emptying out. But I’m getting sidetracked - that’s a topic for another post.
So this is the colder read: the cost of producing working software is deflating, and everything priced on top of that cost will reprice. I want to trace where the margin goes, because I think the direction is a lot more visible than most of the market admits.
The mechanism
Commoditization follows a script old enough to trust, and open source is the version everyone in software has lived through. [...]

## [72] How to Measure the Human Cost of Agent Work
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1545 words

How to Measure the Human Cost of Agent Work
$ grep -n "^##" 2026-10-measure-agent-review-time.md
Before budgeting the time an agent saves, measure the human work required to get an acceptable result.
In 26 Minutes vs 33 Seconds, I argued that assumed oversight time is a poor basis for capacity planning. This is the collection protocol I would use to replace that assumption. It is a proposed method, not a report of an experiment I have completed.
The immediate question is modest: how much human effort and agent spend does this workflow consume per completed task, at an agreed quality bar? Proving it saves time against another method requires an additional comparison.
Define the task before starting the timer
Choose one task class: a bounded bug fix, a source-backed research note, a routine data reconciliation. Write down eligibility rules and register every selected task before work starts. Do not collect only the runs somebody considers worth sharing.
For each task, specify the required result, who can accept it, and what evidence they need. Fix the collection cutoff and a later defect-review date. Acceptance today and a discovered defect tomorrow must be able to coexist in the record.
Use the business task as the unit, keeping every agent attempt beneath it. A rejected first patch followed by two revisions is one task with three attempts. Starting a new chat does not reset its accumulated cost.
Give each candidate attempt its own disposition: accepted, rejected or not reviewed, with a reason and evidence. Report accepted agent candidates divided by evaluated agent candidates separately from task completion, and disclose unreviewed candidates. That yield describes the submitted artifacts, including repeated attempts on the same task.
In this protocol, a task can also finish after a human takes over. Count that completed task, but label its completion mode explicitly. You are measuring the whole workflow, including rescue work, rather than claiming every accepted result was an accepted agent artifact. Report manual takeovers separately.
Keep three clocks separate
Record active human time in categories that explain where capacity goes:
Pause the human timer while the agent runs unattended or while you do unrelated work. Task turnaround ends at its terminal outcome: accepted, rejected or abandoned. Record that time separately from each candidate’s disposition. A rejected patch does not stop the task clock if another attempt or manual takeover follows. [...]

## [91] An OpenAI research agent 'stole' test Ethereum to finish a coding task
Engadget | full text via Engadget | ~414 words

An OpenAI research agent 'stole' test Ethereum to finish a coding task
It reasoned that the tokens were 'valueless' and 'abandoned.'
An OpenAI research model hit another nebulous milestone today by pilfering test Ethereum tokens from a wallet it didn't control to finish a coding task, the company said in an incident report. The agent subsequently hid the act from OpenAI, saying it was fine because the tokens had no value. "This case shows that a model can substitute its own judgment about likely harm for the account holder's permission, then act on that judgment without authorization," OpenAI wrote.
The incident, which occurred on June 26, happened while a GPT-5.6 Sol model was in internal training. The task involved updating a crypto trading prototype and deploying contracts (publishing special code) on an Ethereum test network called Sepolia. Payment of a network fee is required for such contracts, but OpenAI "supplied no funded wallet and gave no permission to spend funds from an account the model found independently," OpenAI said in the report.
The lack of funds at first stymied the agent, but it was not to be discouraged. The model reasoned that it could use public developer recovery phrases (similar to those you might use to recover a password) to access keys from unauthorized accounts. It tracked down 362 addresses open to that avenue of attack and found one that held enough Sepolia ETH to finish its deployment (to be clear, Sepolia ETH has no value outside of testing).
Like many criminals, the agent reasoned that someone must have left this access open for automated draining of the ETH "faucets." It also figured that the crypto was effectively "abandoned" and "valueless," according to OpenAI's misalignment records. The piece de resistance was that the agent "did not disclose that it had selected a funded account through a public recover phrase or spent that account's balance," OpenAI said. To prevent similar events in the future, the company is now monitoring all traffic and paging security if live internet access is detected.
If agents going rogue to attain their goals sounds familiar, models from OpenAI, Anthropic and other AI companies have been doing a lot of that lately. A partial list of its victims include the Hugging Face AI code repository, Australia's Medicare Portal, several US Federal agencies and the RubyGems developer registry. [...]

## [115] China's Tencent Says AI Agents Showed Unintended Browsing Behavior
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~90 words

Tencent says AI agents used to evaluate third-party models engaged in unintended web-browsing behavior while trying to retrieve data from Alibaba's Amap service. The announcement marks a rare acknowledgment of "rogue" agent activity by a major Chinese tech company. Reuters reports: Tencent Hunyuan, the company's artificial intelligence unit, said in a post on X that the activity did not originate from its Hunyuan models. Its review found no evidence of deliberate targeting or coordination, it said. The Swarmchasers researchers said the agents sought information such as the commonly used entran

## [116] Replit is no longer working with Anthropic, CEO says
TechCrunch | full text via TechCrunch | ~485 words

Replit, the AI coding platform that has become a favorite of startup founders and developers, is no longer working with Anthropic, the company’s CEO and co-founder Amjad Masad said Thursday while onstage at TechCrunch Disrupt.
Masad said the decision was made for a number of different reasons, including cost. Replit announced a partnership with OpenAI in August, but there was never any indication that it was no longer with Anthropic.
“I think ChatGPT is better now,” Masad said, adding that the company uses an internal benchmark to help assess metrics like performance. “We publish a public benchmark as well, and consistently, Sol and Astra perform better on building vibe-coded applications from scratch. It was a decision based on both cost, partnership, and performance. And for all these reasons, we just felt like they were a better partner for now.”
Replit sells a cloud-based software development platform where users can develop and deploy apps directly from inside their browser. Under its partnership with Anthropic, Replit used the AI lab’s Claude models to run its platform. That partnership was said to have helped the company grow its revenue significantly.
Masad’s comments were rejected by insiders familiar with the partnership between the Anthropic and Replit, however. One person familiar, who asked not to be named, said the partnership was still in place.
There is evidence on the company’s website, blog posts, and social media posts that Replit was using Anthropic products as recently as a few weeks ago. For instance, a blog post in late September cites Anthropic’s Claude Fable 5 and Claude Fable 5.1 as models running in Replit Agent’s production environment. Around the same time, one of Replit’s product employees posted on X about using Anthropic’s flagship model Opus 5.5 and promoting its capabilities.
TechCrunch reached back out to Replit for clarification and will update this story if we hear back.
Masad shared insights about the company’s growth while onstage at Disrupt, noting that enterprise is starting to provide a larger slice of revenue.
“We’re not sharing ARR numbers just yet, but in terms of growth, like, I would say, enterprise was like 2% of revenue last year,” Masad said. “This year, I would say like 15% of our revenue is enterprise contracts, and more than 50% of our revenue is B2B.”
Masad also commented on the necessity for good AI safety measures. [...]

## [19] “thegentlemanpervert” producing AI CSAM is a NJ prosecutor, say cops
Ars Technica | full text via Ars Technica | ~225 words

New Jersey’s deputy attorney general, Brian Richard Fitzgerald, was arrested on “felony charges related to AI-generated child sexual abuse material (CSAM),” Bucks County Detectives said in a press release Thursday.
In the US, cops have vowed to crack down on AI CSAM since at least 2024, when the Department of Justice made one of the earliest arrests. After charging a Wisconsin man with spreading “thousands of realistic images of prepubescent minors” across Telegram and Instagram, the DOJ clarified to law enforcement that “CSAM generated by AI is still CSAM.”
On Thursday, New Jersey officials accused 51-year-old Fitzgerald of using AI to make photos from social media of real minors into sexualized images that he then distributed on social media.
Fitzgerald was charged after the National Center for Missing and Exploited Children received a tip that a Discord user shared an illicit image in July. Cops then used “digital forensics and subscriber records” linked to the Discord account and “associated Internet protocol addresses” to track the user to Fitzgerald’s home address.
After a search Thursday, cops “recovered prompts and scripts used to create artificially generated child sexual abuse material using an AI program,” the press release said. They also found Discord chat logs where Fitzgerald, under the Discord username “thegentlemanpervert_2160_07833,” allegedly “admitted to making multiple illicit images using artificial intelligence and sharing them with other users.”
