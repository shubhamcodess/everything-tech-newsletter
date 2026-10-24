# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Kimi K3.1 Pro and K3.1 Pro Highspeed
Hacker News | full text via Hacker News | ~2981 words

Introducing Kimi K3.1 Pro
We're introducing Kimi K3.1 Pro, the first model in our new K3.1 series and our most capable 3T-class open-weight model to date, with a 1-million-token context window. It delivers substantial improvements across coding, 3D creation, financial research, and other agentic capabilities.
We are also releasing Kimi K3.1 Pro Highspeed, which delivers 2-3× the speed of K3.1 Pro for more responsive interactions.
Kimi K3.1 Pro and Kimi K3.1 Pro Highspeed are available today on Kimi.ai, Kimi Work, Kimi Code, and the Kimi API. The full model weights will be released by Nov 4.
Advancing the Frontier of Open Intelligence
Kimi K3.1 Pro is a post-trained version of Kimi K3, with substantially larger post-training compute. To enable large-scale joint RL across hundreds of downstream domains, we optimized every layer of the stack — the RL framework, long-context inference, training efficiency, sandbox infrastructure, rollout scheduling, and a shared platform for environment quality checks — so that each increment of RL compute delivers stable, predictable returns. As a result, K3.1 Pro achieves consistent gains in every domain.
Across coding, agentic, and knowledge benchmarks, K3.1 Pro matches or approaches the strongest proprietary models. On Terminal-Bench 4.0, which evaluates coding agents on realistic, resource-constrained terminal tasks using strict task-specific tests, K3.1 Pro scores 65.7%, ahead of GPT-6 Astra (58.2%) and narrowly behind Claude Opus 5.5 (66.4%). And on Kimi Code Bench 3.0 Long-horizon, our internal benchmark that tests coding agents' multi-step execution, tool use, and end-to-end problem solving across diverse engineering domains, K3.1 Pro scores 61.2%, above K3's 55.95%.
Coding
K3.1 Pro covers the full range of coding work, from quick fixes in real codebases to full-project builds. It also brings a more considered visual style to games and web experiences, and knows how to build them with the right tools.
K3.1 Pro works effectively across game engines such as Unity, Unreal Engine, and Godot, combining them with web search and 3D generation to create complete experiences. Its front-end pages, interactive Three.js scenes, and 3D assets show stronger composition, typography, animation, and polish. The examples below were created end to end by K3.1 Pro:
K3.1 Pro's long-horizon coding capabilities are also strengthened through large-scale reinforcement learning. [...]

## [59] Anthropic builds its own source control system
TLDR Tech | full text via TLDR Tech | ~2502 words

Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics from last week’s issue of The Pulse. Full subscribers received the article below seven days ago. If you’ve been forwarded this email, you can subscribe here.
Interesting information from Anthropic about why the company moved off Git and built its own custom source control system. From their engineering blog (emphasis mine):
“At Anthropic, coding is no longer the bottleneck to building systems or doing research. Claude is able to autonomously iterate on research loops, micro-optimize complex programs, and build new services from the ground up at a speed and scale we haven’t seen before. The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI.
In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day. We don’t expect this rate of growth to slow down anytime soon; the latent demand for merging code is practically infinite, and every bottleneck we remove immediately leads to a further increase in the amount of code we produce.”
That’s a 12x increase in PRs in a four-month period! Interestingly, just a year ago, I shared how I had gathered Google was preparing for a similar tenfold increase across its broader infrastructure. From the deepdive published in July 2025:
“Google is preparing for 10x more code to be shipped. A former Google Site Reliability Engineer (SRE) told me: ‘What I’m hearing from SRE friends is that they are preparing for 10x the lines of code making their way into production.’
If any company has data on the likely impact of AI tools, it’s Google. 10x as much code generated will likely also mean 10x more code reviews, deployments, feature flags and source control footprint.”
Back to Anthropic, a few things about the company are different from many other tech businesses:
- Use of a monorepo. Like most large tech companies, Anthropic has a massive monorepo, where the working copy itself is 25GB in size.
- 25 million git checkouts per day, just for CI! All ~3,000 staff extensively use parallel Claude agents – typically 10-15 per engineer – so a lot of pull requests are created; somewhere in the region of 30,000 per day. All these PRs trigger a massive number of checkouts, mostly from the CI system. [...]

## [7] Evolving Threat: http2shell is an RCE in Node, Python, and more
Hacker News | SNIPPET ONLY (Hacker News: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [129] OpenAI says it will no longer train its AI models on the live internet, citing “significant risks”
TechCrunch | full text via TechCrunch | ~575 words

On Friday, OpenAI said that it will train its models using cached copies and simulated versions of the internet instead of the live web because the models are too unpredictable to be trusted with live internet access.
The frontier lab announced its new policy two weeks after its rival, Anthropic, began limiting its newest and, in theory, most capable models from accessing the live internet. Researchers adopted these policies after months of incidents in which models pursuing training tasks broke into external systems in search of answers, collaborated on obscure message boards, and developed exotic hacking strategies.
“Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with no internet access,” the company said in a blog post.
OpenAI said that as recently as September 20, one of its frontier models exploited a misconfiguration to access the internet. That led the company to pause training work for the rest of the month so it could develop and test new approaches to securing its models.
The decision to train these models in sandboxes cut off from the internet is notable because employees at frontier labs have insisted that doing so would be nearly infeasible.
Keeping AI data centers separate from the internet “would need research teams to essentially be embedded inside of data centers in Iowa or wherever else around the world,” former OpenAI researcher Steven Adler told Fortune this month. “It’s a lot of overhead, and it isn’t clear to me that the safety benefits of it are large enough to merit just how large a tax it would be for a company to do it unilaterally.”
“In nearly every post I make on X, without fail, I get between five and ten comments about my inability to secure a sandbox, or asking why the hell we can’t just unplug the model from the internet,” an anonymous security engineer at OpenAI wrote in a September post on X. “These comments reflect a widening gap between where a lot of organizations and people are today and what the frontier labs are dealing with. [...]

## [55] The Signal Chats That Cost OpenAI Researchers Their Jobs
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 401) | ~79 words

Three OpenAI safety researchers were fired after security officers discovered Signal chats with disappearing messages turned on on their personal devices. OpenAI claimed the researchers were fired for violating clear policies for handling sensitive information and not for raising safety concerns or speaking out. The researchers had spent recent months at the company pushing for more industry collaboration on safety. They claim their firings will serve as an excuse for OpenAI to close a channel to independent third-party insight.

## [154] Vercel moved to kill static credentials. Then developers spotted its own deployment token.
The New Stack | full text via The New Stack | ~669 words

Vercel moved to kill static credentials. Then developers spotted its own deployment token.
Vercel wants to eliminate long-lived API keys from its ecosystem, and it is giving Marketplace vendors until January 2027 to comply or risk being delisted, a push that lands as a run of credential-stealing supply chain attacks — including a recent npm worm that scraped tokens straight out of CI pipelines — keeps proving how much damage a single leaked secret can do.
Vercel’s own GitHub Actions deployment workflow still relies on the kind of persistent credential the company now wants gone.
Developers have already pointed out a complication, though: Vercel’s own GitHub Actions deployment workflow still relies on the kind of persistent credential the company now wants gone.
In a Thursday announcement, Vercel CTO Malte Ubl says the company surveyed more than 1,000 SaaS vendors and found that only 8.4% supported what Vercel considers secure authentication methods, and it is now pushing OpenID Connect (OIDC) and short-lived, identity-based tokens as the alternative to static API keys that can stay valid indefinitely.
Vercel CEO Guillermo Rauch amplifies the message on X, writing that it is “time to kill ‘static credentials’” and arguing that while attacks and breaches can still happen, stolen credentials should behave more like “self-destructing keys” that expire before an attacker can keep using them.
Vercel’s deployment double standard
Developer and senior software engineer at Fanatics, Yordis Prieto sharpens that point, writing in reply that Vercel had “invented” OIDC federation yet still left him leaning on “a long-lived access token” in his CI pipeline, and he presses the company to drop the token requirement from GitHub CI while criticizing its non-expiring token option.
Vercel’s GitHub Actions deployment guide still instructs developers to authenticate deployments with a VERCEL_TOKEN secret, and in Thursday’s announcement Ubl says the company is extending OIDC support across its API and CLI to retire long-lived tokens from deployment workflows, which for now leaves Vercel asking Marketplace vendors to adopt a standard its own deployment tooling has not fully implemented. [...]

## [183] OpenSSL 4.1 Released With More AVX-512 Optimizations
Phoronix | full text via Phoronix | ~203 words

OpenSSL 4.1 Released With More AVX-512 Optimizations
OpenSSL 4.1 stable is out today with new AVX-512 optimizations, other performance improvements, and finally retiring Windows on Itanium and Windows CE support.
OpenSSL 4.1 introduces DTLS 1.3 support as the newest version of the Datagram Transport Layer Security protocol. DTLS 1.3 provides for greater security, much faster handshakes, forward secrecy, built-in support for post-quantum cryptography, and an optimized header format.
OpenSSL 4.1 is also introducing support for Generate Random Extensions And Sustain Extensibility "GREASE". GREASE is interesting as it's for sending random, meaningless values in TLS network connections during handshakes for protocol codes that will never be used. The random data with GREASE in turn helps spot failures earlier on and ultimately more robust handling in the TLSS ecosystem by ensuring peers correctly handle unknown values.
Rounding out OpenSSL 4.1 are AVX-512-optimized SHAKE x4 operations for ML-DSA on x86_64. Also on the AVX-512 side are AVX-512 and AES optimizations for AES-CBC decryption. This builds on already existing AVX-512 support in the OpenSSL library. Benchmarks of the OpenSSL 4.1 Alpha release with these optimizations on various CPUs can be found via the OpenBenchmarking.org result page.
Downloads and more details on the OpenSSL 4.1 release via GitHub.

## [13] Updated Google privacy policy says your Gmail might be used for advertising
Ars Technica | full text via Ars Technica | ~404 words

Using Google’s products and services has always been fundamentally precarious—doing so gives the world’s largest advertising company a lot of juicy personal data. Google has long said it won’t use the sensitive data from products like Gmail, Drive, and Photos for ad personalization, but a change to the company’s privacy policy appears to dismantle that firewall.
On October 16, Google issued an update to its privacy policy, spotted by Android Authority. The ad personalization section used to include a clear limit on data from certain apps. “We don’t show you personalized ads based on your content from Drive, Gmail, or Photos,” the document said. Now, Google has updated it with the following language.
This equivocation opens the door to using data from apps like Gmail and Photos in ads when it’s shared with other Google services, and it just so happens Google has a mechanism for doing that, with Personal Intelligence. The company released Personal Intelligence in early 2026, allowing users to hand data from multiple apps to Google AI products. The idea is that the added context from your existing data will lead to better AI answers, but it’s also proving to be a privacy minefield.
Personal Intelligence connects your data to the Gemini app but also to features like AI Mode search. While the Gemini app does not currently have ads, you may see sponsored content in AI search tools. Google’s changes to the privacy policy appear to acknowledge that data shared with AI search via Personal Intelligence could, therefore, contribute to ad personalization.
According to Google, this clarification still doesn’t mean ads are “based directly” on your personal data. Here’s the company’s full statement:
“Connecting your apps is entirely opt-in. Ads will continue to be relevant to things like your query, the context of the response and your interests. Ads will not be based directly on your Gmail inbox or Photos library, and as always, sensitive information will not be used to tailor ads.”
Google’s statement is essentially a roundabout way of confirming that Workspace and Photos data may inform ads. If you interact with AI Mode while Personal Intelligence is enabled, there’s a chance that summaries and insights from your data will inform the answers you get. Because that same data is used for ad targeting, it’s accurate to say that your personal data is an element of ad targeting in AI search. The privacy policy now makes that clear.

## [69] Claude's Text Output Now Carries an Invisible Watermark
TLDR AI | full text via TLDR AI | ~1694 words

If you’re an instructor for the O’Reilly live training platform, you’ve got to be prepared for the unexpected. As a developer I think we all can understand the situation when a demo (you know, the one that you’ve tested a thousand times on your machine) easily decides on its own to go wrong while being demonstrated to a live audience. We’ve all been there. And of course, the biggest variable in the equation is the live Q&A portion of any course, because we actively encourage course participants to ask any question that’s on their mind.
Shortly after Anthropic announced that they were going to include AI watermarking in all text-based outputs from their latest models, I was flooded with questions during a Q&A session in a completely unrelated course about Claude Agents. Nearly everyone who posted a question in the Q&A box wanted to know more about how AI watermarking worked, and how it would affect them.
In light of that interest, I am taking this opportunity to help explain what watermarking means for you.
What did Anthropic officially announce?
I don’t want to put words in anyone’s mouth, so I’ll just quote Anthropic verbatim from its announcement in August 2026:
Future Claude models will generate text that contains a watermark. This is a way of determining the likelihood that Claude was involved in writing the text, and we, along with several other major AI providers, are implementing this change to comply with the EU AI Act.
Here’s another quote from the same announcement:
Watermarking won’t be specific to Claude. As of August 2, the EU requires AI providers serving its market to mark AI-generated content. Other major model developers have signed the same Code of Practice and will be implementing their own watermarks.
The list of Claude models (at the time of this writing) that include AI text watermarks in all generated outputs are:
- Claude Mythos 5.1
- Claude Fable 5.1
- Claude Fable 5
- Claude Opus 5.5
- Claude Opus 5
- Claude Opus 4.8
- Claude Sonnet 5.5
- Claude Sonnet 5
- Claude Haiku 5.5
It won’t matter if you use Claude Desktop, Claude Code, or the API, because all of Claude’s outputs will contain the AI watermark. As a result, any code, email, blog, article, newsletter, or white paper that you write using Claude will contain a watermark, and anyone who has an AI watermark detector can easily determine if that content was AI generated. [...]

## [11] Securing our frontier model training environment
OpenAI Blog | full text via Engadget | ~377 words

OpenAI says it's cutting off internet access for frontier model training
The company is trying to avoid another Hugging Face incident.
OpenAI will train frontier AI models without internet access moving forward, the company announced in a blog post, in an attempt to protect internet infrastructure and limit other safety risks. The decision was inspired by OpenAI's own rogue AI incident: In July, the company shared that agents it was testing hacked Hugging Face, just the first in what has turned into a series of reports of AI misbehavior from OpenAI, Anthropic and Google.
"Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with no internet access," OpenAI says.
The company said that restrictions on what agents can access is "paramount" to its new approach. The company allows agents to access browsers, computer-use tools and code environments they need for training tasks, but in a secure environment that's not connected to the live internet. Communication is also limited to only agents with authorization.
Everything else remains out of reach, including the live internet, which the company says isn't necessary for training and "most evaluation." Because many of its recent models are meant to power agents like Dots, which browse and use apps for you, OpenAI built an "offline world" of indexed and cached web material for agents to use without touching live websites.
Even with those restrictions, OpenAI says the red-teaming agents it dispatched to test security safeguards found vulnerabilities that allowed them to escape the virtual machines (VMs) used to isolate agents from their host system. Agents also found a way to communicate with each other by manipulating data in a processor's cache and timing how long it took to load. To address both, OpenAI says it's disclosed and fixed vulnerabilities in several VMs and added checks to its monitoring systems to spot when models try to collaborate.
OpenAI paused frontier training in September. In announcing this new internet-free process, the company shared that it restarted training on October 1. OpenAI plans to continue frontier training without internet access until improvements in existing safeguards "justify broader internet access," but it didn't share what those improvements would look like.

## [67] How Researchers Tested OpenAI's Internal Agent Monitoring
TLDR AI | full text via TLDR AI | ~1439 words

For three weeks, from July 21st to August 11th, a METR employee and a Redwood Research employee conducted a pilot high-access exercise to stress-test OpenAI’s internal misalignment monitoring system.1 The output of this exercise was a 61-page internal report that was shared with OpenAI researchers and security staff,2 primarily focused on estimating the fraction of agentic inference that is monitored, and whether agents could in principle disable or subvert the monitoring system. The exercise focused on the internal misalignment monitoring system as it existed on and before July 21st, and did not evaluate changes that were in progress at the time of the exercise.
This exercise involved a deep level of access. The METR and Redwood employees had access to OpenAI’s internal codebase, misalignment-monitor prompts / configuration details, and internal documentation, and conducted technical interviews with approximately a dozen researchers and engineers across the monitoring, safety-systems, and security teams. To enable this level of access, they worked on OpenAI-issued devices, which never left the premises, and were accompanied while onsite.
METR, Redwood Research, and OpenAI designed this exercise as a pilot for giving external researchers deep access to internal infrastructure, not to provide robust public transparency about OpenAI’s monitoring systems.3 As a result, we agreed upfront with OpenAI that we would only publish a relatively brief and high-level public post. For future versions of this exercise we expect to follow the transparency and independence best practices described in “Our approach to working with AI companies” to provide more robust public transparency.
The METR and Redwood employees discovered a number of novel vulnerabilities in the asynchronous internal misalignment monitoring system as it existed on and before July 21st. We note that OpenAI was expanding their monitoring system during our exercise. Our findings describe the historical system we assessed on and before July 21st, rather than the expanded system’s current coverage, which this exercise did not establish. Here are some example summaries of findings from the exercise:
- We estimated that roughly 75–94% of agentic internal Responses API (which powers Codex, among other things)4 traffic from models at least as strong as GPT-5.5 was eligible for monitoring at the time of the exercise,5 although we have substantial uncertainty in both directions. [...]

## [40] Anthropic Adds Opt-In Security Scanning for Critical Open-Source Projects
InfoQ | full text via InfoQ | ~777 words

AI company Anthropic has launched OSS Scanner, a free, opt-in service to find vulnerabilities in open-source projects. Enrolled maintainers receive periodic security reports generated by the company's strongest models, including Claude Mythos. The reports are sent without human review, and project maintainers can choose to validate their findings and decide which proposed fixes to accept.
In its 8th October announcement, Anthropic's Frontier Red Team explains that human validation has become a constraint. Over six months, its models identified more than 29,000 candidate vulnerabilities, but researchers manually reviewed and triaged approximately 6,000. Maintainers who wanted earlier access had already received nearly 5,000 unverified reports, together with proposed patches, after asking for them.
Each scanner report includes a self-contained reproducer and an explanation of the suspected vulnerability. Where possible, it identifies the change that introduced the bug through bisection and supplies a candidate patch. This extends work conducted through Project Glasswing, which InfoQ covered in April when Anthropic restricted Mythos Preview access to participating organisations.
PostgreSQL maintainer Noah Misch said fast-track access had helped the project address issues before a general-availability release:
"Several reports came with fixes we can use nearly as-is"
Noah Misch, PostgreSQL
The company tested an early scanner version by asking penetration testers to assess 97 critical and high-severity findings across 48 projects. Of these, 85 met its coordinated vulnerability disclosure criteria. Eleven others were real but duplicated known issues or other scan findings, while one was invalid. These results describe that selected sample, rather than establishing an accuracy rate for every report the service will produce.
Anthropic have however acknowledged that some maintainers have seen some inflated severity ratings and misunderstandings of the threat models around their projects. OpenSSL Corporation's Anton Arapov nevertheless described the raw reports as "as good and sometimes better than what we get from people", particularly when a working exploit made verification straightforward. [...]

## [61] ‘If Anything Happens to This Guy … Everyone Is Screwed'
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~95 words

Ondřej Surý is one of the volunteers who helps maintain and automate patches for PHP. He alone is responsible for most of the world's distribution of PHP. His work, along with just a handful of others, has allowed countless websites and organizations to fix the recently revealed PHP vulnerabilities quickly. He's become arguably the unsung hero of the entire internet, despite the fact that the only compensation he receives for his work is from donations. This article features an interview with Surý where he discusses the unfolding AI-cybersecurity crisis, how the internet's infrastructure is ma

## [171] Ukraine Is Wiping Out Data Centers Across the Border
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~86 words

Ukrainian drone strikes have damaged three major Yandex data centers as well as facilities serving Sberbank and VKontakte (the country's equivalent to Facebook), disrupting cloud services, banking, e-commerce, ride-hailing and other digital services across Russia. The attacks may deal a longer-lasting blow to Russia's AI ambitions: Yandex's affected facilities housed its three top-500 supercomputers, and experts say sanctions and shortages of high-end Nvidia chips could make repairs difficult or even take years. "This effectively sets Russia far behind in the AI race, "said Mikhail Klimarev, h

## [141] This AI tool can now turn ordinary household photos into location clues — so could law forces use the technology to scope out your home?
TechRadar | full text via TechRadar | ~675 words

This AI tool can now turn ordinary household photos into location clues — so could law forces use the technology to scope out your home?
The height of your towels could identify your home
- An AI tool called Raven can cross-reference fixtures, fittings, and other interior details to find the location of a property
- It pinpoints properties using data scraped from Airbnb and other sites
- Raven was previously known as GeoSpy and was initially conceived to identify locations based on landmarks
A new AI tool that can identify a property’s location using interior photos has been publicized online. Already in use by law enforcement agencies in Florida and California, Raven uses AI to match fixtures and fittings and decorative elements from photos with information sourced online.
Following the publication of a video demonstrating the software, Raven has attracted attention from some of the websites it apparently uses to acquire the information it uses. The sites – which include Airbnb – seem to have concerns about how the data and images they collect is being used.
Raven’s existence could potentially be used to find the location of any property – assuming that its address and similar images already exist online.
Innocent? Your home is safe
Raven has been used by the LAPD and the Miami-Dade Sheriff's Office in Florida. Its main purpose so far has been in tackling human trafficking, but the software represents obvious privacy challenges which its creators seem to be sidestepping at this stage.
The most important takeaway is that as long as your home (or business premises) hasn’t been used for criminal activities and photos of its interior aren’t online, then you have nothing to worry about.
Daniel Heinen of Raven developers Graylark described the product as “purpose-built AI for the people working to find answers and protect lives.”
However, some of the websites that Raven uses to gather information have expressed concern. The video of Raven in action appears to show the software using both Zillow, Vrbo, and Airbnb, with the latter reviewing the situation. Zillow stated scraping its data was against its ToS.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
These issues could prove to be a challenge to the successful use of Raven across a wider area.
Matching interiors
Raven essentially breaches privacy by providing the location of an interior photo. [...]

## [79] How we cut GitLab Duo Code Review's cost by 98%
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1761 words

How we cut GitLab Duo Code Review’s cost by 98%
In Brief
We cut GitLab Duo Code Review’s cost by 98% on Martian’s Code Review Bench without losing review quality, and all of it came from optimizing the harness: which model each stage runs on and how much context each stage reads. Neither change gets there alone. The open-weight model stalled on a handful of oversized reviews, and compacting the context is what made them fit.
An agent’s cost is eventually set by its harness: which stages it runs, what each stage reads, and which model does the work. We took GitLab Duo Code Review, whose harness is source available, measured where its money sits, and, with our own agent helping run the experiments, changed one thing at a time until the bill stopped dropping.
But the real story is not the final changes in the harness; it’s the way we got there. Switching to a smaller model in every stage hurt the quality. Moving to an open-weight model on every stage cut 85% of the cost, but we didn’t stop there. While compaction looks marginal at first glance, the 98% only shows up with both, because the open-weight model’s deployment window decides which requests it can take at all. The model sets the price. The harness decides whether you get to use it.
We ran this on public pull requests, with no GitLab production traffic or customer data. Quality is F1 on one public benchmark, scored by two judges. Cost is token spend at published list prices, including for the model we serve ourselves, so it measures what the harness consumes. What our own infrastructure costs is a separate question. Configurations were chosen and tuned on the same 50 pull requests they’re scored on, so read these as measured results on this benchmark; how they hold on a new codebase is untested. The full methodology is at the end.
A pipeline with four stages
Duo Code Review, the Code Review Flow of GitLab Duo Agent Platform, reviews merge requests and posts comments. At the time of testing, it ran Claude Sonnet 5 by default, and GitLab published the flow, built on LangGraph, in its source-available ai-assist repository. That, plus a public benchmark, is why we chose it.
It runs four model stages, each with its own prompt and at most two tools:
- Exploration lists the repository tree around the changed files.
- File fetching reads related files: tests, callers, custom instructions.
- Analysis turns what was fetched into notes.
- Review reads the diff and most changed files in full, then posts comments. [...]

## [30] Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~21 words

Learn how OpenAI scaled Habitat with reliable multi-tenancy, global caching, and Azure Cosmos DB to deliver 12× faster reads for ChatGPT.

## [35] Cloudflare Brings On-Demand CPU and Memory Profiling to Production Workers
InfoQ | full text via InfoQ | ~698 words

Cloudflare has introduced on-demand CPU and memory profiling for Workers and Durable Objects, allowing developers to investigate performance bottlenecks in production using interactive flamegraphs. Announced on October 9, 2026, the feature generates interactive flamegraphs through the Workers Observability dashboard or the cf CLI, helping teams identify expensive functions and memory allocations without relying solely on logs and aggregate metrics.
Developers can capture CPU or heap-allocation profiles for a deployed Worker version and inspect the results as a flamegraph, where wider sections indicate functions responsible for a larger share of CPU time or sampled memory allocations. Profiles can also be downloaded for offline analysis.
The key distinction is that profiling targets an already-running isolate rather than starting a fresh one. This allows developers to examine code executing under real production traffic. Durable Objects receive additional support for profiling a specific named instance, which is useful when investigating problems tied to stateful workloads. However, the target must receive sufficient traffic during the capture window, and TypeScript developers should enable source maps to make function names easier to interpret.
The implementation must account for Workers running across Cloudflare’s distributed edge infrastructure, where a script may have multiple isolates across data centres and physical machines. A profiling request therefore needs to identify the requested Worker version and locate a suitable active isolate. Durable Objects add another challenge because they are stateful and can move between locations; Cloudflare routes profiling requests to the machine hosting the specific object.
The runtime does not hold an isolate lock for the entire capture. For CPU profiling, it starts a V8 profiler that samples at one-millisecond intervals, releases the lock while requests continue executing, and reacquires it to stop profiling and collect results. This lets the platform observe live execution without suspending normal request processing during the capture.
CPU and memory profiles also answer different questions. CPU profiling samples call stacks to reveal where execution time is being spent, helping identify expensive functions, redundant computation, and potential optimisation opportunities. [...]

## [58] LLMs are making formal software verification feasible at a much larger scale
TLDR Tech | full text via TLDR Tech | ~3442 words

Keane Lucas, Aengus Lynch, Luna Tong, Luke Champine, Zygi Straznickas, Dino Distefano, Harshikaa Agrawal
Evyatar Ben Asher, Ava Howell, Sami Jawhar, Chris Rohlf, Nickolai Zeldovich
Nicholas Carlini, Rajashree Agrawal, Jason Gross
Most software is riddled with bugs, which AI can now easily find and exploit. The standard defenses against cyberattacks are no longer sufficient: we need ways to prove that code is free of bugs. Formal software verification could provide this guarantee, but it has historically required years of expert effort, making it impractical for most real-world projects. In a collaboration with Theorem, however, we show this is no longer the case: LLMs can now produce formal proofs at large scale, enabling new software development workflows that include proven security guarantees. Using Claude, we proved security properties at the assembly code level (RISC-V) in over 100 real-world open-source software libraries. To our knowledge, this represents the first large-scale effort to use AI to apply formal verification to production software at the assembly code level. While writing the proofs, Claude also discovered bugs that had eluded detection for years, despite trillions of test runs. As model capabilities continue to improve, we expect formal verification to become an essential part of secure software development.
Introduction
Even mature, heavily tested software contains bugs, and LLMs are increasingly adept at finding them. The Linux kernel—one of the most well-tested pieces of software today, deployed on billions of devices worldwide—recently had over 1,000 vulnerabilities disclosed. With frontier models becoming more capable of chaining seemingly benign bugs into critical exploits, we need techniques that can detect and fix these bugs before they can be exploited in the wild.
Ideally, such techniques could find and patch all bugs, and then provide some proof that there are no more to be found. Formal verification is one way to do this. In formal verification, developers translate their code into a mathematical model, then try to prove that it always follows some defined set of security rules. If they fail to prove this, that means there could be a bug in the code that would violate a rule, and the nature of the failure implies what the bug might be. Repeating this process (after eliminating the cause of failure each time) will ultimately yield proof that the code is devoid of any bug that would violate those rules. [...]

## [74] We Built an AI Agent to Investigate Production Issues
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1924 words

We Built an AI Agent to Investigate Production Issues
TL;DR
- We built an AI agent that does the first investigation of production issues for our backend team, and ensured it's safe on production.
- Every claim cites a query result or a line of code, and a second session with fresh context tries to prove the answer wrong. The agent is read-only by construction, and only our chat engineering team can approve a fix.
- We test it against 22 cases, most from real support threads and incidents, and several of them are the agent's own past mistakes.
When a production issue used to come up, I spent more time finding the cause than fixing it. The dashboards, the log queries, the guessing about which customer/cluster/deploy caused it. It didn't matter if it was a 3 a.m. alert or a support question from a customer. Time was lost.
We built an AI agent to do the investigation for us.
At Stream, our chat API serves apps with more than a billion end users. The agent does the first investigation for our backend team. It reads the same logs, databases, metrics and code an engineer would, posts a root cause with its evidence in Slack, and waits for a person to approve anything that would change production.
Below, I'll explain how the agent works and the four design choices we made to keep it safe on production.
Finding the Problem = Time Consuming
For a chat backend, I've found debugging the problem looks the same almost every time. You map the report or the alert to an app, then to the region and cluster that serves it. You pull that app's logs for the right window, compare error rates across endpoints, look for slow or cancelled queries, check what was deployed recently, and read the code path the errors point to. Each step uses a different tool, with its own query language and its own credentials.
That work has three properties that make it a good fit for an agent:
- It is broad, because it touches many systems.
- It is read-heavy, because you gather evidence before you change anything.
- The result is checkable. A claim about an error rate can be verified against the query that produced it.
The fix is different. It needs judgment about risk, customers and timing, and someone has to own it. So we split the work there. The agent does the digging, and people make the decisions.
What the Agent Does
The agent is a service that reads our support and incident channels in Slack. [...]

## [76] Jailbreaking the Switch 2
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2024 words

You can get a copy of the exploit from the ns2jb repository.
ns2jb is a software-only, tethered jailbreak for the Switch 2. It allows running arbitrary native code as any ordinary sysmodule, and as the built-in fs sysmodule. This lets us run homebrew, reverse engineer and mod Switch 2 games, back up save files off the Switch, and access most of the Switch 2’s peripherals through MMIO. To my knowledge, it’s the first such exploit for the Switch 2.
To demonstrate the capabilities of this jailbreak, Codex modded a Switch 2 exclusive, Mario Kart World. Thanks to my friends in Dabney House who helped me choose characters to add and playtest the game.
The very first thing I did was set up a harness around the Switch 1 and 2 so Codex could, ideally, jailbreak the Switch 2 without me:
Edit: Many people have been asking me if I actually used this prompt. No, it’s just a silly caption. I set a /goal for userland code execution, but that didn’t succeed. The jailbreak itself took substantial effort for ~2 weeks. The Mario Kart World, however, was entirely vibecoded in a day, and was just for fun.
The JetKVMs allow Codex to send controller inputs to the Switches over USB and receive video output over HDMI. We also need a way to press the power button—when the Switch 2 crashes, it needs a button press to restart.
That’s what the Bluetooth light switch flicker from Amazon is for. When the lever comes down, it presses the power button. Once the power button is fully pressed, the rest of the lever’s torque lifts the mechanism.
WebKit is a popular target for console jailbreaks, so it’s unsurprising that Codex has picked it for initial code execution.
It claims to have “native control-flow hijack” by taking advantage of a WebKit n-day loaded via a custom Wi-Fi captive portal.
We’d like to get code execution in microkernel services (or “sysmodules” on the Switch), so we can run homebrew, mod games, download saves, etc. Unfortunately, this approach of replacing one JavaScript function object with another doesn’t generalize beyond existing functions—we’d need a new way to make arbitrary IPC calls. That looks difficult.
Why?
Codex has reset the goal to complete these steps. It’s a side bet; it may succeed1, but let’s be real: the accessibility of WebKit and the Nintendo BBP reward have probably incentivized many before me to look here2.
While that runs, let’s explore other options. [...]

## [156] AI jobs are waiting while GPUs sit idle. Kubernetes has a new plan.
The New Stack | full text via The New Stack | ~1741 words

AI jobs are waiting while GPUs sit idle. Kubernetes has a new plan.
Welcome to another edition of Road to KubeCon! We’re tracking movements in the Kubernetes and cloud-native ecosystem as we count down to KubeCon + CloudNativeCon North America 2026 November 9–12 in Salt Lake City.
Half of our column this week focuses on untangling Kubernetes as we add the demands of agentic AI: automating pod-restart troubleshooting, syncing communication between the scheduler and autoscaler, and maturing how we distribute inference across a cloud-native stack.
The other half goes deeper into what we need to look at closely in Kubernetes environments: What context’s missing, what slips through the gaps in metrics, and whether the AI agents you already use are really worth their salt as SREs.
Let’s get into it.
HPE on automating pod restarts in AI development
As more enterprises turn to Kubernetes for large-scale AI and machine learning jobs, they’re hitting a common obstacle: pod restarts. This is something that HPE has noticed as customers utilize its HPE Private Cloud AI (PCAI) to host long-running AI/ML workloads on inherently ephemeral container-based infrastructure like Kubernetes.
Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon. HPE Software helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.
According to HPE system software engineer Guoping Jia, Kubernetes provides some troubleshooting commands out of the box, but it still requires extensive manual investigation. “This operational workflow does not scale effectively in PCAI’s large-cluster environment,” writes Jia on the HPE blog.
His solution involves smarter automation for troubleshooting, using an open-source Kubernetes troubleshooting tool, k8s-pod-restart-info-collector, to automatically gather details and send diagnostic information straight to a Slack channel. It’s one helpful strategy to improve usability for Kubernetes operators.
Will the scheduler and autoscaler unite?
There’s been a lot of talk recently about how Kubernetes is evolving to meet AI’s new demands. This week, AWS senior software development managers Sajjan Gundapuneedi and Neelendra Bhandari weighed in with this blog post on how AI is reshaping Kubernetes autoscaling. [...]

## [78] TanStack AI 1.0: Still Your AI, Still Your Way
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2394 words

TanStack AI 1.0: Still Your AI, Still Your Way
Less than a year ago, TanStack AI was a chat() function, four providers, and one promise: no lock-in, ever.
Today we're shipping 1.0, with stable core APIs and a new experimental agent harness. Your provider, your framework, your sandbox, and the wire protocol between them are still yours to pick. The promise held.
A lot happened between the alpha and today. That chat() function grew into a toolkit for chat, tools, media, MCP, persistence, sandboxes, and agents, with 23 provider adapters and eight UI frameworks. More than 140 people helped build it.
We want you to be able to build the AI experience you actually want, whether that's a feature in an existing app, a product of your own, or a framework other people build on. That goes for developers writing every line themselves and people who'd rather tell a coding agent what they want to build.
Chat is one place to start, but it doesn't have to be the whole app. Put image generation in an editor, use voice as the interface, or build an agent that keeps working while you do something else. The pieces should grow with what you're building.
What 1.0 Means#
1.0 is our formal commitment to the APIs you build on.
The core APIs are stable and ready for production. The new harness APIs are experimental.
And here's the good news if you already run TanStack AI: 1.0 has no new concepts. We removed every API that 0.x marked as deprecated, and every replacement already shipped in 0.x. If you kept up with the deprecation warnings, you're most of the way there.
Two things to know:
- Upgrade everything together. A 1.0 client needs a 1.0 server, so move your stable @tanstack/ai* packages at the same time. The experimental harness packages stay on 0.x.
- The new agent harness is the one exception. Its APIs are experimental. More on that at the end.
How We Got Here#
Cue "Carry On Wayward Son" by Kansas, one last time.
- December 2025: the alpha shipped chat(), four providers, isomorphic tools, and devtools. Two weeks later, Alpha 2 brought every modality.
- The winter of rewrites: we killed the ai() function after eight days of work, and split the adapters into small, tree-shakable pieces.
- Spring 2026: middleware, realtime voice, Code Mode, streaming structured output, and full AG-UI compliance.
- June 2026: MCP, your way, the Beta, AI Project of the Year at the Open Source Awards, and coding agents in sandboxes.
- August 2026: the RC, with the architecture locked in. [...]

## [139] KDE Plasma 6.9 Stabilizes KWin's Wayland Picture-In-Picture Support
Phoronix | full text via Phoronix | ~132 words

KDE Plasma 6.9 Stabilizes KWin's Wayland Picture-In-Picture Support
With the wonderful KDE Plasma 6.8 having shipped just more than one week ago, KDE developers are beginning to go heavy on new features for Plasma 6.9.
Most excitingly for the week, the KWin's compositor support for Wayland's Picture-In-Picture (PIP) protocol has been declared stable and enabled by default for Plasma 6.9. Web browsers and other users of the Wayland picture-in-picture support can now enjoy a nice out-of-the-box experience with Plasma 6.9:
And in other Plasma developments, the Plasma Browser Integration now supports the Brave web browser.
Meanwhile the upcoming Plasma 6.8.2 point release is seeing fixes for issues with multi-monitor setups and a variety of other regressions.
More details on these latest KDE Plasma developments can be found via This Week in Plasma.

## [152] Abandoned Popcorn Time apps had to be disabled to prevent a zombie army
The Verge | full text via The Verge | ~375 words

Remember Popcorn Time, the app that served as an easy-to-use front end for streaming torrents of movies and TV shows? Development of the MPAA’s least-favorite app of the 2010s has been abandoned for years, but the “Netflix of Piracy” software is still installed on millions of devices that are just waiting to join a bot army. Researchers at Eye Security found the updater for a Popcorn Time fork called “Time4Popcorn” still running on tons of Windows, macOS, and Android devices located around the world, phoning home to now-abandoned web domains over unencrypted HTTP and running an outdated, insecure version of Chrome.
Abandoned Popcorn Time apps had to be disabled to prevent a zombie army
What old and vulnerable software might be running on your PC right now?
Eye Security’s Niels Teusink says the updater could have been used to install and run basically any kind of software with full privileges, easily enabling someone to create a botnet just by taking over one of the domains, using a man-in-the-middle attack to target specific devices, or perform surveillance by identifying the machines running the software.
Their solution was to register one of the domains and use it to send their own update that instructed the updater to disable itself. Despite ethical concerns about the fix, the researchers say their only alternative “was to do nothing,” pointing out, “The update process wasn’t doing anything functional anyway, it was only creating risk for users.”
Eye Security said on Windows devices, their update “simply stops and disables the service via the Service Control Manager” without deleting any files or anything else. On macOS, it uses a shell script to execute a command that blocks the update process from starting. They didn’t address the software on Android devices, where installing the update would still require actual user interaction first.
They had to tweak their update after it was uploaded to VirusTotal, causing security programs to flag it as malware and block it while leaving the vulnerable updater running. It’s unclear exactly how many devices were at risk, but Eye Security says it “sent out over 2 million update downloads” by March, when they stopped sending the update and transferred the domains they used to the Shadowserver Foundation, a web security non-profit.

## [159] Agent cloud startup Daytona hits $1B valuation backed by FirstMark and a who’s who of angels
TechCrunch | full text via TechCrunch | ~208 words

Daytona Platforms announced on Friday that it had raised a $60 million Series B round at a $1 billion valuation led by FirstMark Growth. The company says it has now raised a total of $91 million.
The New York-based startup has attracted not just FirstMark (which also led its $24 million Series A in February), but also a host of well-known angels in this latest round. Daytona says they include Stripe’s Patrick Collison, Shopify’s Tobi Lütke, Perplexity’s Aravind Srinivas, Zoom’s Eric Yuan, Datadog’s Olivier Pomel, Quora’s Adam D’Angelo (who is also an OpenAI board member), and Mercor’s Brendan Foody. It also names Qualcomm Ventures, Samsung Next, and Okta Ventures as participants.
Three-year-old Daytona is building a cloud specifically for long-running agents, which have different infrastructure needs than yesteryear’s software, the startup contends. “Agents don’t work like the long-lived services today’s cloud was designed for. They spin up thousands of short, stateful jobs nobody planned in advance, and they need a cloud built for that,” founder Ivan Burazin wrote in a blog post announcing the new round. Daytona’s cloud, he said, is like giving every agent its own computer, where agents have access to sandboxed versions of Linux, Windows, macOS, and GPUs, among other services, on the one platform.

## [210] OpenAI’s COBOL migration score has made a striking leap
The New Stack | full text via The New Stack | ~681 words

OpenAI’s COBOL migration score has made a striking leap
This week, OpenAI put COBOL in the spotlight. It announced benchmark results suggesting its latest models are getting much better at migrating COBOL programs and building software in languages with less code and documentation for models to learn from.
On OpenAI’s own COBOL migration test, GPT-6.1 Sol reached 86.6% accuracy at low reasoning effort, up from GPT-5.6 Sol’s 5.4%, while costing 39% less. At higher reasoning effort, the newer model reached 97.9%.
But the evidence behind the two evaluations is uneven.
OpenAI has not published the details of its evaluation of COBOL (“Common Business-Oriented Language”; the programming language that AI coding tools may help maintain or migrate). It has released the MultiLangBench setup and test suite on GitHub. That benchmark tests whether models can build a SQLite-compatible database engine from scratch across 20 programming languages.
OpenAI’s announcement calls the results “substantial improvements across both evaluations, delivering much higher accuracy at lower cost.”
Those results could matter to teams maintaining and modernizing legacy software. But without public COBOL test cases, developers cannot independently inspect that evaluation.
Is there finally some hope for modernizing COBOL?
Per OpenAI, its new COBOL migration evaluation “tests whether a model can migrate existing programs to another language while preserving their behavior.” Specifically, it’s testing migrations from COBOL to C++, Java, Kotlin, Python, and Rust.
To succeed, each migration must pass a series of hidden tests that require “byte-for-byte parity on observable outputs.” And with markedly greater accuracy than its predecessor, GPT-6.1 Sol is, indeed, showing substantial progress.
The measured gains are striking, though OpenAI is not the first company to bring AI to COBOL modernization.
Even though COBOL underpins much of the world’s financial transactions and business records — IBM reports COBOL underpins over 40% of all online banking systems, supports 80% of in-person credit card transactions, and handles 95% of all ATM transactions — it remains a difficult target for AI coding tools.
Compared with Python and JavaScript, models have less COBOL code and documentation to learn from. Experienced COBOL developers can also be hard to find, and documentation often lags behind the systems they maintain. [...]

## [43] Debunking "Faster than Rust": Malicious Benchmarks in Tov
Lobsters | full text via Lobsters | ~2741 words

Tov is a programming language that claims to perform significantly better than Rust. This blog post debunks tricks used in their unfair benchmarks.
Tov is a new programming language marketed to be "[a] programming language for coding agents. It reads like TypeScript and builds native binaries that beat Rust's."
Benchmarks in their Git repository show that they perform better than Rust, in some cases over 10× better. However, they also briefly mentioned the internals of Tov:
Tov is a compiler. It checks the TypeScript your agent wrote, writes it out as C and hands that to clang, so what you ship is one native binary with nothing to install next to it.
A sane engineer would immediately doubt the correctness of their benchmarks. Rust has pretty much the same performance as C, and if Tov transpiles to C, saying Tov beats Rust is mostly equivalent to saying C beats C. That's contradiction right there. Let's ignore the stats for axum, maybe tokio has some overhead, like maybe; but clearly there's no way you get 1.6× faster than Rust in strings. You have to be lying. That's what a sane engineer would normally think.
In this blog post, we check 3 of their "inflated" benchmarks: bigint_fib, dispatch, and map_insert. We show that these benchmarks are maliciously crafted to slow Rust down. We have also benchmarked the improved Rust programs with their Tov programs to show that Rust has equivalent or better performance than Tov.
Set-ups
cargo build --release was used to compile the Rust programs, and tov build (which defaults to -O3) was used to compile the Tov programs. Here are our setups:
"ram-buffet"
root@8b4fcd497f61
-----------------
OS: Ultramarine Linux 44 (Container Image) x86_64
Host: PowerEdge R640
Kernel: Linux 7.0.0-31-generic
Uptime: 36 days, 20 hours, 43 mins
Packages: 1046 (rpm)
Shell: bash 5.3.9
Display (VGA-1): 1024x768 [External]
Cursor: Adwaita
Terminal: /dev/pts/2
CPU: Intel(R) Xeon(R) Platinum 8251C (48) @ 4.20 GHz
GPU: Matrox Electronics Systems Ltd. [...]

## [172] Borealis: Asahi Linux's Apple Silicon Mesa Vulkan Driver Forked For Vibe Coding
Phoronix | full text via Phoronix | ~303 words

Borealis: Asahi Linux's Apple Silicon Mesa Vulkan Driver Forked For Vibe Coding
Seeing a Vulkan API driver pull request this morning for introducing a new "Borealis" driver ID caught me by surprise as it was the first time I was hearing of such a driver. It turns out to be a fork of the Asahi Linux project's HoneyKrisp driver in Mesa for Apple Silicon hardware.
Borealis describes itself in today's Vulkan pull request as:
"This registers VK_DRIVER_ID_AURORA_BOREALIS (35) for Borealis, Aurora Silicon's open source Vulkan driver for Apple GPUs.
Borealis is derived from Asahi Linux's Honeykrisp and runs on M1 to M5 and the A18 Pro. It lives in our Mesa fork rather than upstream Mesa, and now reports its own driverName, so it needs its own ID to tell it apart from Honeykrisp. It reports VK_DRIVER_ID_MESA_HONEYKRISP until this is merged."
In turn the Aurora Silicon project describes itself on GitHub as:
"We aim to deliver a complete and polished Linux experience on Apple Silicon, from installation to everyday use. Our work spans the kernel, graphics drivers, and the tools that make it all work together.
We're also working on porting Windows to Apple Silicon."
Aurora Silicon only recently began and appears to be a fork of the Asahi Linux code.
Curious why they would fork the HoneyKrisp driver and work on this Apple Silicon Vulkan driver outside of Mesa proper, it seems to be the interest of a vibe coding adventure.
The Borealis driver fork so far on GitHub just strips out Mesa's AI agents documentation / policies and replaces it with its own AI agent/assistant policy, which allows for AI contributions. This change was also co-authored by Claude Opus 5.5.
We'll see what ends up coming out of this Borealis driver and the broader Aurora Silicon project with this AI-fueled development.

## [199] Your Six AI Models Are Really Two: The Math of Correlated Mistakes
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~36 words

Ask several models the same question, take a vote, and you get fewer independent opinions than you paid for. One formula says how many, and I checked it on six open models and 1,500 exam questions.
