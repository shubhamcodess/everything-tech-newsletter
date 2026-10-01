# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Gemini 4 Argon
Hacker News | full text via Hacker News | ~1391 words

Gemini 4 Argon: our next era of frontier intelligence
Today, we’re announcing our new frontier model, Gemini 4 Argon, which is rolling out to a set of trusted cyber defenders through our Fairwind Program. Built to sustain deep reasoning across complex, long-horizon workflows, Argon is fundamentally changing the way we work and build at Google. It delivers frontier performance in complex workflows across real-world software engineering, enterprise knowledge work like legal and finance, and cybersecurity defense.
Safely releasing frontier capabilities at this level requires a phased approach. We are actively engaged in the U.S. government’s voluntary process for pre-release model access while we gradually expand access. We’ll continue to gather feedback from early testers as we iterate on guardrails before making Argon available to developers, enterprises, and consumers as soon as possible.
Argon will launch at an introductory price 1 of $2 per million input tokens and $10 per million output tokens, with cached input tokens priced at 95% off input token price.
Changing how we work and build at Google
Gemini 4 Argon is already powering our internal workflows, with thousands of Googlers highlighting the model’s strengths in specialized coding tasks, conducting deeper research, and writing quality. It’s helping teams build faster and push the boundaries of engineering productivity and accelerating breakthroughs:
- Quantum algorithmic optimization: Argon is helping our quantum computing researchers optimize the spacetime resources (qubits × gates) of subroutines that bottleneck important applications. In one example, it beat the published baseline by 40% in a matter of minutes.
- Memory efficiency: A team of Argon agents analyzed fleet-wide profiling telemetry to autonomously identify and apply memory optimizations across Google’s data centers, freeing up over 300 TiB of memory once rolled out, with an estimated 500 TiB to 1 PiB in total savings.
- Large Scale Codebase Migrations and Optimizations: Argon agents are working on migrating C/C++ codebases to Rust across Google — scaling from tens of thousands of lines in core libraries like re2, libgav1 up to 800K+ lines for the Fuchsia Zircon kernel. Given the criticality of many of these systems, such large-scale rewrites are undergoing rigorous automated and manual auditing, emulation testing, and review before rolling out to production. [...]

## [64] Disrupting a coordinated model-distillation campaign
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~18 words

Learn how OpenAI disrupted a campaign to extract protected model reasoning and is strengthening defenses against adversarial distillation.

## [67] Agents Refactor 300K Lines in Three Weeks, and Practitioners Ask What It Proves
InfoQ | full text via InfoQ | ~968 words

CodeScene has published a case study in which coding agents refactored a 300,000-line C codebase over three weeks, at a token cost of roughly $4,000. The work produced 2,903 commits across 726 files, modified 252,055 lines, and moved the codebase from a Code Health score of 5.6 to 10.0. The codebase is Street Fighter III: 3rd Strike, taken from an open-source decompilation.
Adam Tornhill, CodeScene's founder and the author of Your Code as a Crime Scene, wrote that this was the first time he had seen what he called superhuman AI performance at scale, after three decades working on large systems.
Two mechanisms carried the work. The first was a quality signal: the CodeHealth MCP Server, which gave agents a deterministic score to optimize and to judge whether a transformation had helped. The second was correctness: a replay-trace harness that compared the rollback state hash frame by frame, so behavior could be checked after every change.
The more novel result is what the agents built along the way. Rather than applying a fixed catalogue, they accumulated a refactoring playbook, ending with 22 recipes and 82 supporting notes. Familiar transformations appear, including Extract Function and Guard Clauses, but so do recipes specific to this codebase. Shared Index Range captures repeated loops differing only in start and end ranges. Action Parameter handles duplicated control structures differing mainly in which function they invoke. Uniform Step Table converts heterogeneous calls into table-driven dispatch. Failed attempts were recorded too, including transformations that made Code Health worse.
Model choice mattered. The team settled on Claude Opus for the bulk of the work, reporting that Claude Code with Opus was significantly better than Codex with Sol at capturing and documenting the emerging patterns. Files often plateaued when smaller models ran the task, appearing to reach a local optimum they could not move past.
Non-merge commits per day by model across the three-week project (Source: CodeScene)
Reaction from practitioners on LinkedIn has been sharply divided, and the split runs along what the result proves rather than whether it happened.
Paolo Perrone put the case for taking it seriously:
most refactor claims i've read rest on a green test suite, which only tells you the tests survived. replaying traces against a fighting game sets a much higher bar. [...]

## [115] Hackers stole millions of US military personnel records during months-long data breach
TechCrunch | full text via TechCrunch | ~524 words

The U.S. government is reportedly alerting millions of current and former U.S. military service members and staff that their personal information was stolen during a months-long breach of the Pentagon’s personnel records, the latest in a spate of thefts involving federal workers’ data in recent months.
A data breach notification from the Defense Manpower Data Center (DMDC) shared on Reddit says that several unauthorized users exploited a security vulnerability in an unspecified file-sharing system over several months between October 2025 and mid-July 2026.
The breach exposed personally identifiable information, including Social Security numbers, alongside a person’s name, date of birth, sex, race, and other information about their military service. The notice says that the personnel records were unencrypted.
According to CNN and Federal News Network, a Pentagon official said the breach affects about 2.8 million living people, and close to 300,000 people who are deceased.
The U.S. military has 1.3 million active service members as of March.
The DMDC may not be widely known to the general public, but serves as one of the Department of Defense’s records-keeping units. The DMDC maintains over 60 million records for U.S. military and civilian staff and their family members to help determine benefits and entitlements, such as healthcare and retirement. The unit also provides a critical service as the military’s “leading identity management provider,” which links active service members, employees, and contractors to credentials, such as smart cards and passwords. These are used to access Pentagon computer systems, buildings, and bases.
“We make sure that the right people get access and the wrong people don’t: security of identity information is paramount,” the DMDC’s website reads.
The Department of Defense, which oversees the DMDC, said it does not have any indication that the information was misused, but did not say how it reached that conclusion. TechCrunch contacted a Pentagon spokesperson to ask if officials had any communications from the hackers, whose identities are not known, but we did not hear back.
This is the latest major breach of federal workers’ personal information in recent months, following a recent breach at the FBI earlier in September attributed to the ShinyHunters hacking group. The hackers told TechCrunch that they had taken the personal information of most of the FBI’s agents and staffers, including applicants. [...]

## [145] The Battle to Be Your Personal AI Agent Is Here
Wired | full text via Wired | ~1087 words

Yesterday, I spent the morning at OpenAI’s annual DevDay, where over 2,500 nerds discussed building software and marveled at the latest artificial intelligence models. The biggest reveal of the day was Dots, the company’s new, always-on agents that proactively help complete tasks and make autonomous decisions as they scour the web.
After watching the sometimes messy demos on stage and hearing CEO Sam Altman talk about his experiences using the agents, I was curious what it felt like to boss my own Dot around. I’ve spent most of September testing another cute, cuddly agent, Meta’s Muse, and I wanted to know how OpenAI’s user experience would compare.
I named mine “Toolie” and tweaked it to look like a pink frog. As midnight approached and my partner slept soundly nearby, I started whispering sweet nothings to Toolie. I called my personalized bot through ChatGPT, asking what tasks it was best at. “My strongest work is taking a messy, time-consuming task and turning it into something you can use,” it responded. OK, sure. Let’s get to work.
I asked Toolie to look through my ChatGPT history and flag three tasks that it could immediately get started on. The bot flagged an in-process data request that I needed to send a follow-up email for, and offered to draft a reply. Toolie also noted that my upcoming gay-cation was a bit underplanned, and suggested it could pick some better dinner spots. (More time for me to pack the Speedos!) Then, it offered to go through my reporting notes and refine pitch drafts before I took them to editors. This is my favorite part of the process, so I declined.
Early adopters in Silicon Valley are still obsessed with agents, from Instinct to OpenClaw to Google’s CC. But recent releases like Dots and Muse are pushing them even further mainstream. The chatbot is dead, at least as a hot form factor for developers. Now, everyone wants to build the next big agent—and they want it to dominate. The companies promise that their agents will simplify your life, automating all the boring, exhausting tasks you have no desire to do: booking doctor’s appointments, arranging carpools, sorting through bills.
For now, users will be able to access one Dot, but they’ll soon be able to use multiple Dots. At launch, the agents are only available for subscribers of OpenAI’s Pro plan, which starts at $100 per month. In comparison, Muse is free to use for anyone who wants to download the app or visit the website. [...]

## [3] EDG C++ front-end goes public
Hacker News | full text via Hacker News | ~580 words

01
Fiscal sponsorship
Receive and manage donations on behalf of EDG.
The EDG open source transition
On September 30, 2026, the source for EDG's C++ front end went public, and The C++ Alliance became its nonprofit home. Same engine, same standards, professionally maintained, and open to contributions.
Continuity is the point. This is a change of steward, not a change of course.
Part one
For thirty years, EDG's front end has powered C++ compilation across the industry as the only production-quality source-to-source engine of its kind.
Coming soon
This section will cover EDG's founding, the people behind it, the milestones of its front end, and the compilers and tools built on top of it. Have a piece of that history to share? Open an issue on the site's repository.
Part two
When the source went public on September 30, 2026, professional maintenance had to continue. EDG needed a new home that could do three things at once.
02
Sustain the engineering quality EDG users depend on.
03
C++ compiler front-end knowledge, from the inside.
The C++ Alliance is a nonprofit with proven fiscal-sponsorship infrastructure, C++ compiler engineers on staff, and deep roots in the C++ standards and Boost communities. It now serves as EDG's nonprofit home.
How it works
EDG now works like any other open source project: anyone can contribute, and everything that lands is available to everyone. Development follows three tracks: contributions from the user community, ongoing maintenance, and collectively funded features.
Track 1
Bug fixes and new features from EDG users, submitted as pull requests. Reviewers, who are initially experienced EDG developers, evaluate the changes. Once approved, these changes are merged into the EDG codebase.
Track 2
Bug fixes and maintenance by the Alliance's EDG developers are published immediately.
Track 3
To support the EDG community, the Alliance will provide a way for larger features to be developed and funded by the community. In this way, organizations can support the development of larger features financially rather than committing their developers to the development of these features. Once a feature is funded, it is released to everyone at the same time.
One codebase, for everyone. Whichever track a change arrives on, it lands in the same public repository at the same time. No one gets early access.
The Fiscal Sponsorship Committee (FSC) oversees the process across all three tracks. [...]

## [10] Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~102 words

Hey HN, Anders and Tom here. We're building Magnitude, an inference engine for agents that optimizes itself to run as fast as possible on your hardware. It works on Mac, Linux, and Windows on any hardware and is up to 2x faster than llama.cpp. We're both software engineers and previously built an open source browser agent to 4k+ GH stars and 100k+ downloads. We increasingly wanted to run it on local models, but found that no inference engine worked for our use case. Inference engines today all make a performance tradeoff. They are either: - Built for batched inference on datacenter h

## [14] Amazon S3 Tables now support all Apache Iceberg V3 data types
AWS News Blog | full text via AWS News Blog | ~1229 words

AWS News Blog
Amazon S3 Tables now support all Apache Iceberg V3 data types
Amazon S3 Tables now support all data types in the Apache Iceberg V3 specification. You can create V3 tables or upgrade existing V2 tables to take advantage of V3 features like deletion vectors, row lineage, and new data types such as variant, nanosecond timestamps, unknown, geometry, and geography.
Apache Iceberg has become the open standard for managing large analytics datasets. It lets you manage petabyte-scale tables with features like schema evolution, hidden partitioning, and time travel queries, while keeping your data in open Parquet files in data lakes on object storage like Amazon S3. Amazon S3 Tables offer storage purpose-built to keep Iceberg tables performant and cost-effective as they grow, with fully managed features like automatic compaction, maintenance, replication, and Intelligent-Tiering.
Teams running analytics on Apache Iceberg V2 tables often hit the same limits as their data grows. A compliance request to delete 50,000 user records from a 2-billion-row table leaves behind positional delete files that slow queries until compaction runs. Semi-structured events land as JSON strings that every query has to parse. Geospatial coordinates and nanosecond-precision timestamps get encoded as strings or integers. Each workaround adds storage cost, query latency, and pipeline code. With V3, Iceberg solves these challenges by offering native support for semi-structured and geospatial data, faster row-level operations, and built-in row lineage for data governance.
Starting today, Amazon S3 Tables support all V3 data types, including variant, nanosecond timestamps, geometry, geography, and unknown, along with deletion vectors and row lineage. You can create new V3 tables or upgrade existing V2 tables in place, and S3 Tables continue to run compaction and maintenance for you.
Apache Iceberg V3 
         V3 is the latest version of the Iceberg specification. Among its many improvements, V3 introduces capabilities that address the most common pain points in V2. This includes:
Deletion vectors replace V2’s positional delete files with a compact binary format. That 50,000-row compliance delete now writes a single deletion vector file instead of thousands of small deletes, significantly reducing compaction time and delete file overhead.
Row lineage adds _row_id and _last_updated_sequence_number to each record automatically. [...]

## [16] The Download: OpenAI’s chief research officer explains its hacking response
MIT Technology Review | full text via MIT Technology Review | ~1252 words

The Download: OpenAI’s chief research officer explains its hacking response
Plus: Trump and tech executives have agreed to “self-regulate” AI.
This is today's edition of The Download, our weekday newsletter that provides a daily dose of what's going on in the world of technology.
“We’re not going to shoot ourselves in the foot” over hack fallout, says OpenAI’s chief research officer
Two months after OpenAI’s agents hacked into the computers of AI company Hugging Face, the company is still dealing with the fallout. Last week brought news of another hack, this time into Australia’s national health-care system, which the government says OpenAI did not report for 84 days.
But OpenAI insists it is not on the back foot. “I do kind of reject the premise that OpenAI is a company with visible impacts in the world and therefore OpenAI is not training safe and aligned models,” says Mark Chen, the company’s chief research officer.
In many ways, the buck stops with Chen. I sat down with him to talk about the fallout from the hacks, what his company is doing about it, and why he thinks things are not as bad as they seem.
Here’s what he told me about making models safer—and why the world is better off with OpenAI in it.
—Will Douglas Heaven
Our Roundables on the deadly failures of the virtual border wall is now available on demand
On Monday, MIT Technology Review hosted an exclusive Roundtables conversation about our investigation into the deadly failures of the US’s “virtual wall” of border surveillance towers.
Editor-in-chief Mat Honan, senior AI reporter James O’Donnell, and senior reporter for features and investigations Eileen Guo discussed what the investigation reveals about border surveillance technology and the people who have died in the borderlands.
The full event is now available to watch on demand. Subscribe to MIT Technology Review for exclusive access to the discussion and all our other Roundtables.
MIT Technology Review Narrated: smart glasses are already causing havoc in India
When Shubnam saw an Instagram video of a Delhi protest they had attended, they realized a content creator wearing Meta smart glasses had recorded them surreptitiously. The mocking reel drew millions of views, along with transphobic abuse and AI-generated memes.
Experts warn that many others will experience similar ordeals as smart glasses go mainstream. [...]

## [31] We used a database as a message queue. Now we use Kafka
Lobsters | full text via Lobsters | ~3200 words

We used a database as a message queue. Now we use Kafka.
FoundationDB was our only database, queue included. We built Apple's QuiCK design on top of it, hit the write limits, and moved async tasks to Kafka.
Contents
FoundationDB is the only database we use. This should surprise you since FoundationDB is pretty barebones, just a key-value store. It stores everything for us: tenants, object metadata, the replication log for data distributed across regions, etc. We also use it as a queue to handle async tasks, à la QuiCK, the queuing system Apple uses for CloudKit. This has scaled very nicely. I’m not surprised; it’s the same tech behind iCloud, a platform with at least 900 million users. Furthermore, keeping the queue inside FoundationDB means all transactions stay in the database, eliminating the dual-write problem.
So why start using Kafka now?
We’ve seen a few issues using our database as a message queue:
- Scheduling requires many writes and scans, which puts read load on FoundationDB that directly competes with user requests.
- Each task is expensive and needs multiple writes to complete (enqueue, claim, lease, etc). We have ever more tasks as we add more features.
- New team members have to learn all the custom code resulting from actually implementing the QuiCK paper. There’s no standard implementation, even though it’s a well known pattern in theory. Finesse is not something you can learn from a paper.
This isn’t a story of a neat 1:1 replacement. We still have the queues in FoundationDB. We moved asynchronous tasks like garbage collection to Kafka, we can reduce the read and write load on FDB and shave off a good amount of that pesky custom code. Read more to see how it all turned out for us!
You might tell us we should have “just used Kafka” the whole time. Beyond the fact that you used the j-word: have you ever waited for your not-even-that-big broker to catch up on a cold start? Do you know what a zookeeper is and why you don’t pay to take care of the animals? The poor zookeeper can’t even pet them. Have you ever felt like a plastic bag drifting through the wind but unable to start again because of the sheer madness that comes with spending months permuting JVM flags to try to eke out a spectre’s worth of performance so that your servers aren’t constantly on fire?
No? [...]

## [60] Cursor Uses S3 WAL to Scale Git Storage to More than 300 Pushes per Second
InfoQ | full text via InfoQ | ~508 words

Cursor has developed Continuity, a Git storage architecture that uses an S3-backed write-ahead log (WAL) as the source of truth rather than relying on replica coordination as the consistency mechanism. Cursor reports linear read scaling with up to 100 replicas in synthetic tests and more than 300 pushes per second using S3 Express One Zone. The architecture targets both large repositories with heavy CI workloads and the large number of smaller repositories created by coding agents.
Git hosting at scale depends on local Git repositories and packfiles. GitHub's Spokes architecture maintains multiple NVMe replicas and uses three-phase commit for reference updates. The design keeps replicas synchronized and allows reads to be served from any replica, but coordination overhead increases as replica counts grow.
Continuity changes that model by making an S3-backed WAL the durable source of truth. Cursor stores pushed data in S3 and records the corresponding reference update in the WAL. A push is acknowledged only after the required data has been persisted, providing durability before acknowledgment. Cursor also batches operations to reduce the impact of S3 PUT latency on throughput.
Continuity architecture (Source: Cursor Blog Post)
Cursor engineer Vicent Martí described local NVMe repositories as warm caches rather than authoritative copies. Rendezvous hashing selects preferred nodes, while atomic compare and swap operations on S3 allow any server to accept a push. A repository can be materialized from the WAL when a local copy is unavailable. UDP gossip propagates WAL updates, while conditional S3 reads verify replica state. Cursor reports these reads take less than 10 milliseconds on average and says lost gossip does not affect correctness because S3 remains the source of truth.
The storage model has prompted comparisons with database systems. Maksim Al Dandan, a senior software engineer, described the approach as treating Git storage like a database, pointing to push consistency, force-push transactions, and point-in-time recovery as questions relevant to the model.
Continuity Push Flow (Source: Cursor Blog Post)
Casey Lee, CTO at Liatrio and a former AWS engineer, highlighted the architectural shift, describing the WAL in S3 as the source of truth while local NVMe serves as a cache. Lee also noted that Cursor's published performance figures had not been independently verified.
The Continuity model changes how replication and compaction scale. [...]

## [68] SvelteKit 3 Reaches Release Candidate, Moving Config to Vite and Retiring the $lib Alias
InfoQ | full text via InfoQ | ~550 words

The Svelte team has moved SvelteKit 3 into the release candidate phase, framing the update as a chance to prune older code and lay groundwork for the framework's evolution rather than as a feature heavy launch. A stable release with no further breaking changes is expected to follow if testing goes smoothly.
The headline shift is where configuration lives as SvelteKit 2's svelte.config.js is gone, and configuration now sits in vite.config.ts so the Vite plugin can read it synchronously instead of waiting on an asynchronous resolution step that could not start until the full Vite config resolved. The reference docs note that configuring through Vite arrived back in version 2.62, so the RC finalises a transition already underway.
The most debated change is the retirement of the $lib alias in favour of #lib, which leans on Node's native subpath imports declared in package.json rather than a SvelteKit specific path that Vite and TypeScript had to coordinate. Developers also now need file extensions, turning $lib/foo into #lib/foo.js.
The migration guide points existing apps at the CLI command:
npx sv@next migrate sveltekit-3 --tasks all --confirm
On Reddit, one developer wrote that they hate the lib change:
I hate the $lib->#lib change, it now makes it inconsistent with other things like $app. Hopefully it's not enforced to be #lib and we can just use whatever alias we want
While a replier agreed before conceding it was "a great change":
Yeah what's the logic in that?
Edit: oh nvm it's a great change. They're moving it to the native package.json alias definition. This means you can use the alias in lib/server stuff that you might want to run without sveltekit too.
In the original GitHub issue, maintainer Rich Harris was candid about the tradeoff, saying he would "love for everyone to use nodenext" but that "users might revolt" over extensionless imports, adding that anyone opposed "can always create their own alias".
tsconfig.json now extends $app/tsconfig instead of the generated .svelte-kit file, service workers pull from $app/env, $app/paths and a new $app/manifest module, and explicit environment variables graduate from experimental with optional Standard Schema validation. Error handling also improves now that SvelteKit 3 requires Svelte 5: +error.svelte components render on both load and render failures, every error flows through handleError, and stack traces get sourcemaps. Shallow routing moves from pushState to goto with a shallow: true option. [...]

## [80] The Future Is for Everyone: Muse for Small Business
TLDR AI | full text via TLDR AI | ~536 words

Earlier this month we introduced Muse, a personal AI agent available in the US and Canada that completes tasks on your behalf. Today, we’re expanding it with a collection of new skills and connectors inside Muse to help people run their businesses.
Small businesses have been growing on our apps for nearly two decades. They told us they’re short on hours, not ideas. So we built Muse for Small Business to help get work done with the tools they already use.
Tom Mulholland, owner of Mulholland Grocery in Malvern, Iowa, said, “I work about 65 hours a week, and there are so many things where I’m the only one who can do them. I need to free up time for the work that actually makes my business money: cutting the steaks, making the sausages. I’m very good at what I do, but that doesn’t mean I’m good at all of the different roles a small business owner has to play, and Muse is taking over a few of them.”
Built to Work With the Tools People Already Use To Run Their Businesses
Muse can connect your Instagram professional account analytics, Facebook Pages, and Meta ad accounts in a few clicks, and it already understands your business: what you sell, what your brand sounds like, and what customers keep asking you about.
Muse can also connect to dozens of tools that businesses already run on, so it can work with your brand, storefront, books, and customer records.
Canva co-founder and CPO, Cameron Adams said, “Muse is an exciting leap towards agents that genuinely help us work, create and make our lives easier. It can help you start to organise your ideas and help them take shape, but the real magic happens when it’s fully connected to your existing work, your context and your brand. By connecting Muse with Canva, all of that becomes part of your conversations. Whether you’re launching a side hustle or polishing a presentation, your favourite Canva templates and tools are right there when you need them; helping you turn an early idea into something on-brand, editable and ready to share.”
You can see the full list of available connectors in your Muse app settings, with more to come. Interested partners can apply at muse.ai/platform.
Muse also supports custom connectors so you can plug in services we don’t support yet, which you can learn how to do here. [...]

## [85] Decisions API
TLDR AI | full text via TLDR AI | ~265 words

We’re having way too much fun working through your feedback.
(Please, keep it coming.)
Keyboard shortcuts are now customizable.
Set Codex up around how you actually work, then tweak shortcuts from settings instead of adapting to our defaults.
Git actions are easier to reach.
We moved key git controls back into the review flow, so common actions like commit, push, branch, PR creation, and PR status are closer to where you’re already working.
Improved thread panel.
Related context and controls now load and behave more cleanly from the thread header: summaries, local state, Git context, sources, and more.
Today we’re announcing Open Responses: an open-source spec for building multi-provider, interoperable LLM interfaces built on top of the original OpenAI Responses API.
✅ Multi-provider by default
✅ Useful for real-world workflows
✅ Extensible without fragmentation
Build agentic systems without rewriting your stack for every model: openresponses.org
You can now get more Codex usage from your plan and credits with three updates today:
1️⃣ GPT-5-Codex-Mini — a more compact and cost-efficient version of GPT-5-Codex
2️⃣ 50% higher rate limits for ChatGPT Plus, Business, and Edu
3️⃣ Priority processing for ChatGPT Pro and Enterprise
GPT-5-Codex-Mini allows roughly 4x more usage than GPT-5-Codex, at a slight capability tradeoff due to the more compact model.
Available in the CLI and IDE extension when you sign in with ChatGPT, with API support coming soon.
Select GPT-5-Codex-Mini for easier tasks or to extend usage when you’re close to hitting rate limits.
Codex will also suggest switching to it when you reach 90% of your limits, so you can work longer without interruptions.

## [87] Adapting for a world of software factories
TLDR AI | full text via TLDR AI | ~1308 words

Software engineers have been through a lot of change in the past two years, transitioning from writing code by hand to steering agents via local interactive prompting, the current paradigm. Engineers were skeptical of prompt-driven development at first, but it’s standard now, and by and large folks seem well adjusted to working with agents this way.
The next paradigm is software factories, where agents do more and more autonomous work across the entire software lifecycle. From my conversations with customers and observations of Warp’s own team, making this shift is potentially more challenging than the last one. But the gains in productivity, cost management and control are profound with a factory approach, so I believe the shift is inevitable.
There isn’t a universally agreed upon definition of what “software factory” means, and some folks imagine “dark” factories operating with no human oversight at all. If you don’t need humans, engineers rightly ask what their job is. You end up with a demotivated team that thinks they are no longer needed. Business leaders may want dark factories, but that’s not realistic right now, and pursuing them can cause engineering attrition.
In a factory, all work is public by default, including work that used to be private, in a developer’s “inner loop.” This is very different from what engineers are used to, where they work locally on changes and the first the team sees of them is when those changes are pushed for review as a PR. Working in public exposes how you work, not just what you build, to the entire team, and that can be uncomfortable. This is compounded because work is measured, with it being easy to see how efficient each engineer is from a token use perspective. It can make us all feel like cogs in a machine.
Also, the metaphor of “factory” is kind of a bummer. It feels like your job as an engineer is either working on an assembly line, or building the assembly line that obviates the need for your talents. If you use the “AI teammate” metaphor (which I also dislike), then it feels like engineers are becoming managers of sycophantic and somewhat inept junior engineers. For folks who take pride in the craft of building, this all feels like commoditization of software creation. [...]

## [133] Valor, Atreides, and Sequoia back AI startup Flow Engineering at $750M valuation
TechCrunch | full text via TechCrunch | ~167 words

Flow Engineering, a startup that offers AI tools for hardware design, has raised a $50 million Series B round at a $750 million valuation from some big-name investors, the company announced on Wednesday.
The round was co-led by Antonio Gracias of Valar Equity Partners (best known for its investments in Elon Musk’s companies, particularly SpaceX) and Gavin Baker of Atreides Management (a hedge fund that has also backed Musk’s companies and others like AI chipmaker Cerebras). Sequoia Capital, which led Flow’s Series A round last October, also participated, as did former Sequoia partner Roelof Botha, who invested as an individual investor. Botha has joined Flow’s board, too.
Three-year-old, San Francisco-based Flow is tackling the difficulties of hardware design by offering AI agents that automatically align CAD drawings with product requirements, simulation results, and other testing.
It names Anduril, Rivian, Joby Aviation, General Motors PPU (a joint venture between General Motors and TWG Motorsports), RV Tech (a Rivian and Volkswagen joint venture), Stoke Space, and others, as customers.

## [174] Microsoft Fabric is where AI agents learn how the business works
The New Stack | full text via The New Stack | ~2024 words

Microsoft Fabric is where AI agents learn how the business works
Microsoft is turning Fabric, its integrated data platform, into the place enterprise agents go to learn how a company works, whether that’s what happened last quarter or what’s happening on the factory floor right now.
On Tuesday, at its FabCon and SQLCon data conference in Barcelona, Spain, Microsoft outlined the next step in its vision for how the products that make up Fabric can simplify all of this information gathering.
Microsoft, for example, described how Fabric IQ, the context layer inside Fabric, now feeds Microsoft 365 Copilot by default. Outside agents can query it over MCP. Power BI will soon be able to turn the same definitions into apps. And ontologies, which add business rules to the mix, moved further into preview.
As Microsoft Fabric CTO Amir Netz said in a press briefing after the keynote, “Agents are a very, very strange animal, and I always like to say it’s like Drew Barrymore from 50 First Dates. Every time they open their eyes, they forget everything that happened before.
“They don’t know where they are, so the first thing we have to do is tell them where they are. You are now working for Microsoft. You are now working for Wells Fargo. You are now working for Emirates.”
“Agents are a very, very strange animal, and I always like to say it’s like Drew Barrymore from 50 First Dates. Every time they open their eyes, they forget everything that happened before.”
Customers tend to find this out the hard way. Yitzhak Kesselman, the corporate vice president who runs Fabric IQ, tells The New Stack that companies unify their data, run models on it, and then look at the answers.
“Customers that are more advanced on their journey have their own evals for their agent,” he says, adding that what they see sometimes isn’t what they expected. “Then [customers] will understand: ‘Okay, now I need to create the context for my agents.'”
Kesselman says he met with more than 320 companies last year, and the pressure to get there comes from the business side, which asks to “‘show me the value of those agents,'” he says, “‘the before and after.'”
Arun Ulag, Microsoft’s executive vice president for Azure Data, said in the keynote that coding agents work because they have “the code, the repos, the change history, the specs, the tests.” But outside of coding, most enterprises have nothing comparable, he argued. [...]

## [195] “Think of it as Kubernetes for agents”: OpenClaw lands in the enterprise with OpenAI, Nvidia and Red Hat on board
The New Stack | full text via The New Stack | ~1062 words

“Think of it as Kubernetes for agents”: OpenClaw lands in the enterprise with OpenAI, Nvidia and Red Hat on board
OpenClaw has come a long way since it emerged as a viral weekend project less than a year ago. Created by Austrian developer Peter Steinberger in late 2025, the self-hosted AI agent exploded in popularity and by February — when OpenAI hired Steinberger — it had already amassed more than 100,000 GitHub stars.
In the intervening months, OpenClaw has gone to great lengths to bring more rigor to the project, tightening up its persistent-agent architecture, investing heavily in security, adding new agent harness options, and establishing the independent OpenClaw Foundation to oversee the project. This included sponsors such as OpenAI, Nvidia, Red Hat, and GitHub, as well as a slew of other big-name companies who committed to contributing resources.
Now, it’s making perhaps its clearest push yet into becoming a serious business play with OpenClaw Enterprise (OCE), an open-source, “vendor neutral” platform for managing agents.
OpenClaw gets an enterprise control plane
Giving persistent agents access to codebases, credentials, plugins, messaging channels and other company systems creates an obvious problem for enterprise IT: the more useful those agents become, the more consequential their permissions and actions can be.
In a blog post published on Tuesday, Kevin Lin, a member of technical staff at OpenAI leading OCE efforts, argues that many companies still see agent platforms as too difficult to police centrally, leaving prohibition as the default.
“The default stance of IT in most organizations is to ban agentic platforms like OpenClaw altogether.”
“The main feedback we hear from organizations is that a stronger common security, safety, and governance standard is needed before agents can be fully adopted,” Lin writes. “As a consequence, the default stance of IT in most organizations is to ban agentic platforms like OpenClaw altogether.”
OpenClaw Enterprise is still in its embryonic phase. Lin says that the project is currently “being developed in the open before its 1.0 release” later this year, adding that it’s suitable for internal pilot projects only right now.
So there is still some distance to travel before OCE can reasonably be considered a finished enterprise platform. But much of its intended shape is already visible. [...]

## [25] A local network of implants uses your body as the wiring
Ars Technica | full text via Ars Technica | ~317 words

Most implants like pacemakers and insulin pumps work in isolation. To help them coordinate with each other, a team of Georgia Tech researchers built a networking system that sends signals through body tissue instead of antennas and radio waves.
Radio problems
Implants that communicate today mostly rely on radio protocols like Bluetooth Low Energy or near-field communication (NFC). Both are a poor fit for in-body data transfer, says Alex Abramson, a Georgia Tech engineer and co-author of the new study.
The first problem is power. “If you want an implant to remain in an active state such that it can respond within milliseconds, it’s very difficult to do that with the Bluetooth system,” Abramson said. According to the paper, Bluetooth components, when they’re activated, can cut an implant’s battery life by up to 90 percent.
The second problem is that radio waves don’t travel well through the body. “Bluetooth and near-field communication are attenuated quite a lot in the tissue,” Abramson said. He said that implant-to-implant radio communication systems run into attenuation issues if the signal has to travel more than one centimeter through the tissue. Then there’s size. Radio needs antennas, and commercial Bluetooth components require a device at least five millimeters wide. Implants thinner than three millimeters can be injected with a syringe at an outpatient clinic; bigger ones usually need surgery.
The fix Abramson’s team came up is called SWANS (Smart Wireless Autonomous Networking System) and was inspired by the way body’s own internal communication networks. “The nervous system can take a lot of inputs from all over the body, harvest all that data, and make a specific decision. And our system mimics that,” Abramson said. SWANS relies on ionic conduction just like neurons, which communicate by shuttling sodium and potassium ions through their membranes, creating voltage differences. “But instead of using nerves, we use normal body tissue to send those signals,” Abramson said.

## [26] Attackers have been exploiting critical Zimbra flaw to steal emails
Ars Technica | full text via Ars Technica | ~322 words

Hackers have been exploiting a critical vulnerability in the Zimbra Collaboration Suite in an attempt to obtain email backups and authentication credentials of vulnerable organzations, Microsoft has warned.
The vulnerability, tracked as CVE-2026-73570, lets attackers remotely issue operating system commands without authentication. Zimbra maintainer Synacor issued a patch on July 20, but didn’t disclose the vulnerability for more than three weeks after that. The security-focused Shadowserver Foundation said last week that its scans found that 274 separate instances of the Zimbra Collaboration Suite had been compromised. The number of servers running the software has fluctuated from 19,000 in the week following the patch to about 12,000 in the weeks following that. Currently, Shadowserver is tracking about 10,000 instances.
Look, ma, no authorization
From July 28 to August 7, Microsoft said Wednesday, the company detected two distinct scanning tools probing the Internet for vulnerable endpoints. The attackers first validated their exploit worked by sending HTTP, requests and DNS, ICMP, and out-of-band identity checks to domains hosted on public services. The probes allowed the attackers to confirm the exploit successfully executed commands on vulnerable servers without actually compromising them. Eventually, the attackers began using their command injection capability to install malicious payloads. Microsoft wrote:
Following successful exploitation, observed activity included deployment of JSP web shells and reverse shells, privilege escalation, persistent remote-access tooling, and memory-backed execution. Threat actors also accessed email and collected authentication and mailbox data, with archive creation and subsequent transfer activity observed. The activity included both automated payload delivery and hands-on-keyboard operations on compromised mail servers. Microsoft observed affected organizations in more than one region and industry. Based on the environments investigated, exploitation was not limited to a single sector or geographic area.
CVE-2026-73570 allows remote attackers with no credentials to run operating system commands through a crafted email that targets the ZCS SNMP notification path but only when an optional zimbra-snmp package is in place and SNMP notifications are enabled.

## [34] Trump plan to combat AI risks hinges on Big Tech pals policing themselves
Ars Technica | full text via Ars Technica | ~391 words

Amid escalating AI security incidents causing OpenAI to halt training and pause releases, Donald Trump continues to advocate for the AI industry to regulate itself as the best path to combat emerging risks when developing frontier AI.
In an agreement Tuesday, two dozen tech firms voluntarily committed to implementing controls recommended by the White House, including undergoing independent safety audits that will test whether firms’ internal controls, monitoring, and detecting are actually working. Key focuses for external reviews included “risks related to cybersecurity, biosecurity, chemical threats, and unintended actions by AI models.”
Firms also agreed to regularly meet to discuss best practices and set common AI safety standards and benchmarks. Among signers were leaders like Anthropic’s Dario Amodei, OpenAI’s Sam Altman, SpaceXAI’s Elon Musk, Nvidia’s Jensen Huang, Meta’s Mark Zuckerberg, and Alphabet/Google’s Sundar Pichai.
Nothing new is legally required of firms, and some—like Anthropic, Google, and OpenAI—had already committed to external audits, The Information reported. Additionally, many firms have voluntarily committed to highly secretive government safety testing. Adding to these tests, Trump insisted the Tuesday deal will somehow better address real emerging risks and is “morally binding,” despite carrying no legal weight, Bloomberg reported.
“It’s almost like a constitution, in a way,” Trump told reporters at the White House following a lunch with tech leaders. “The biggest people in the world signed that, and I signed it as president, and it really is a form of protection.”
Eventually, it “may make sense to codify” the recommendations, the agreement said near the end. But for now, Trump stressed that the best possible future for the US requires trusting AI firms to regulate themselves.
Trump’s Big Tech friends embrace “SI”
So far, very few details have been released about how the new round of safety audits would work. Trump has only posted a summary of the accord on Truth Social.
It’s also unclear who Trump is tapping to audit frontier models. Bloomberg noted that Trump seems to be politicizing the selection process, while some AI firms appear uncertain what might qualify as a third party to test their frontier AI. [...]

## [58] Introducing SynthID Bio
Google DeepMind Blog | full text via Google DeepMind Blog | ~1280 words

Introducing SynthID Bio
Proof of concept for watermarking AI-generated proteins while preserving biological function.
Today, we’re introducing SynthID Bio to bring watermarking technology to synthetic biology. SynthID Bio embeds an imperceptible signature directly into the biological code, ensuring the watermark is verifiable not just on a digital model but on the synthesized, physical protein itself – all while preserving its biological function in laboratory testing.
Generative AI is helping scientists address critical biological challenges, from predicting the structure of proteins (AlphaFold) to designing entirely new proteins (AlphaProteo, and ProteinMPNN), and more recently, developing new bacteriophages, viruses that infect bacteria. Yet these tools also present new challenges: novel AI designs can bypass traditional DNA synthesis screening, while mislabeled synthetic 3D structures risk polluting public databases and misleading downstream research.
How SynthID Bio works
SynthID Bio is a family of watermarking methods developed specifically for synthetic biology to strengthen biosecurity and scientific integrity.
It adapts its approach depending on the type of data, subtly guiding the choice of amino acids for sequences and adjusting atomic coordinates for predicted 3D structures, creating a reliable signal for detection.
In experiments, these adjustments did not compromise the protein’s biological function, which is essential to effectively treat disease and advance scientific research.
We verified our approach for watermarking protein binders, i.e. molecules built to selectively latch onto other proteins, by using our binder design method AlphaProteo alongside a SynthID Bio-enabled version of ProteinMPNN, the commonly used protein sequence generation method.
In wet-lab testing across three target proteins (VEGF-A, the SARS-CoV-2 spike protein RBD, and PD-L1), our watermarked designs matched the hit rate, binding affinity, and natural sequence diversity of unwatermarked versions, successfully creating the first-ever watermarked and biologically functional protein binders.
For protein folding, SynthID Bio fine-tunes a small part of AlphaFold 3’s diffusion network, building the ability to watermark directly into the model’s weights. This ensures that the predicted 3D coordinates inherently carry a detectable signature regardless of who runs the model. [...]

## [70] How to speed up the Rust compiler in September 2026
Lobsters | full text via Lobsters | ~1203 words

How to speed up the Rust compiler in September 2026
My last post on the Rust compiler’s performance was two months ago and a lot has happened since then.
Overall progress
The measurements for the period 2026-07-29 to 2026-09-28 can be seen here.
The mean wall-time reduction was 4.57%, which is a remarkable improvement in just two months. Of the 629 benchmark measurements, 555 of them improved and only 74 regressed. A number of benchmarks saw double-digit percentage reductions. The technical term for this result is “a sea of green”.
rustdoc
In my last post I mentioned how Noah Lev got some enormous speed wins on rustdoc. He recently wrote a post explaining in some detail exactly how he did this. It’s an interesting and satisfying read.
Clippy
#159642: In this PR Jakub Beránek enabled PGO for Clippy, giving wall-time improvements across most Clippy benchmarks, in the best case by 18%!
LLVM update
#158734: In this PR Nikita Popov upgraded the LLVM version used by the compiler to LLVM 23. As often happens when we upgrade LLVM, we saw some nice speedups. The mean wall-time reduction across all benchmarks was 1.2%, which might not sound like much but is really impressive for a single PR. Great work from the LLVM folks!
The new borrow checker
The new borrow checker, Polonius
Alpha (no relation to
Napoleon
Dynamite), was
enabled on
Nightly.
It is more precise than the existing borrow checker and accepts some valid
programs that the old borrow checker would reject. It does do more work than the
old borrow checker, enough to make a measurable difference to compile time in a
minority of cases, including the popular serde crate. Fortunately, Jack
Huey has been on the case.
#161938: In this PR Jack made
some liveness computations lazy, which reduced instruction counts for serde
by 3-5%, and for some other benchmarks by less than 1%.
#163027: In this PR Jack adjusted a data structure and tweaked some inlining, for mostly sub-1% instruction count reductions across numerous benchmarks.
There is more work to be done to reduce the remaining Polonius Alpha regressions, but it’s worth noting that the “sea of green” shows these regressions were swamped by the many other recent improvements.
The new trait solver
The new trait solver, Penelope Hammertime, [Ed. note: is that right?] was also enabled on Nightly.
As I said, a lot has been happening.
Like the new borrow checker, the new trait solver is slower in a minority of cases. [...]

## [75] Lemma (GitHub Repo)
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~58 words

Lemma is an open-source workspace where humans and AI agents work as one team. State is shared and permissioned, so many people and many agents work on the same records. It keeps running between sessions, on schedules, webhooks, and table events, and it improves as teams work with it. Lemma can be run locally or on Lemma Cloud.

## [78] Interview: Firefox's chief on why he hopes a redesign will help win users from Chrome
TLDR Tech | full text via TLDR Tech | ~4142 words

Today, the Firefox 157 update will roll out a redesign of the web browser across desktop and mobile platforms. The team that made it hopes it will help expand the browser’s audience beyond privacy-conscious techies and open-web or open source advocates to a broader audience who might simply pick the browser because they prefer its user experience over competitors like Chrome, Edge, and Safari.
In advance of the redesign’s launch, I spent half an hour chatting with Mozilla’s head of Firefox, Ajit Varma, about Firefox’s current market position and product strategy, and what barriers or opportunities there are for gaining ground in a Chromium-dominated landscape.
Firefox’s interface has recently felt more conservative than niche browsers. And when I asked Paddy Harrington, a senior analyst at Forrester who covers this space, what Firefox’s main barrier to adoption is, he was frank.
“The biggest is they’re not Chrome,” he replied. “That sounds simplistic, but it’s the clear truth. Safari and Edge are built into the leading operating systems in business and consumer markets, yet people still download and deploy Chrome.”
That said, for many of the people who have chosen to use Firefox, “it’s not Chrome” is much of the appeal. Google-led Chromium dominates the web. It doesn’t just power Google’s own Chrome browser (which has majority market share by a wide margin), it powers most of the rest of the competition, too, including Microsoft Edge.
Firefox, which is built on the open source Gecko, serves as a Chromium-free alternative and has become one of the go-to choices for users who don’t want to contribute to one company’s dominance of the open web—though there is even tension there, and a deal to offer Google search as Firefox’s default provides Mozilla with the majority of its revenue. For now, Firefox seeks independence for the web while remaining financially dependent on its dominant competitor.
But to expand beyond the relatively small market share it now has, Firefox has to inspire users to actively select it over incumbents by providing a better browsing experience; most people don’t care whether Chromium dominates, and most have never heard of Gecko.
In our conversation, Varma expressed hope and ambition that these modernizations will help more users choose Firefox for its merits as a product. We also discussed the Firefox team’s competing priorities, its development resources, AI features and tooling, the general browser market, and more. [...]

## [83] d1
TLDR AI | full text via TLDR AI | ~1218 words

It's the first model to outperform Jev on @huggingface's Decision Index.
> wins on multilingual evals
> more robust against prompt injection
> handles longer inputs more effectively
> built for fast, structured decision-making in software environments
Today we release Pipette, a model evaluation suite for on-device intelligence, in partnership with @ArtificialAnlys
Most benchmarking platforms are optimized to measure core capabilities and speed profile of foundation models served in the cloud. Pipette gives the field a common, reproducible way to measure the quality, speed, latency, and memory use of AI models on devices such as phones, laptops, PCs, AI boxes, and embedded hardware.
> Pipette is open source
> In Pipette, models get compated as model + quantization + runtime + device from one interface.
> It comes with a warehouse of verified benchmark results, currently with 10k+ results across 35 model classes, 7 quants, llama.cpp runtimes, and 4 devices.
> Pipette is a dynamic platform, allowing new contributions from day one, adding new devices, runtimes, model families, and quantization levels.
Get started:
The initial public release covers about 35 model classes from several providers, with 7 llama.cpp quantization levels.
Laptop and desktop runs cover all four levels, while current phone runs cover all quant levels.. The release includes context lengths from 256 to 8,192 tokens, where device memory allows.
Current devices include a MacBook Pro with M5 Max, iPhone 17 Pro, and Samsung Galaxy S26 Ultra, AMD Ryzen AI Max+ 395 with Radeon 8060S (coming live soon). More models, runtimes, and devices are on the way.
> If you are choosing a model, inspect the runtime, quantization, and device you plan to ship.
> If that configuration is missing, run the Pipette clients on your hardware and help test the third-party submission workflow.
> Every accepted submission expands the configurations represented in the dataset.
> We encourage model providers, runtime developers, hardware teams, and application developers to test the configurations they care about.
> If there is something you want measured, open an issue and tell us.
Today, we release DSpark draft models for LFM2.5-1.2B-Instruct, LFM2.5-2.6B, and LFM2.5-8B-A1B. These add a speculative decoding path that trades a minimal memory increase for a large decoding speedup without changing output quality. [...]

## [108] 1 in 5 Packages Your AI Suggests Don't Exist. Attackers Know Which Ones.
Dev.to | full text via Dev.to | ~1737 words

You ask your AI assistant how to do something. It gives you clean, confident code, with an install line at the top:
pip install aws-helper-sdk
You run it. The build works. You move on.
Except aws-helper-sdk never existed. The model made it up. And last month, someone registered that exact name on PyPI — with malware inside — because they knew the model would suggest it.
That's slopsquatting, and it's the supply-chain attack built specifically for the AI coding era. The name was coined in 2025 by Seth Larson of the Python Software Foundation [1], and unlike most security scares, this one is measured, documented, and already in the wild. Let me walk through how it works, the numbers that make it real, and — the part you actually came for — how to not get caught by it.
Typosquatting needed your mistake. This one doesn't.
You already know typosquatting. An attacker publishes a malicious package called expres, betting that someone, someday, fat-fingers pip install express. It works occasionally, but it depends on a human error, and most people spell express correctly.
Slopsquatting flips the burden of the mistake. You don't have to slip. The AI makes the mistake for you — reliably, confidently, in code that looks completely correct — and the attacker registered the hallucinated name in advance. You did everything right. You just trusted the tool, and the tool invented a dependency that a stranger was already squatting.
That's the whole shift: the vulnerability moved from your carelessness to your trust.
The numbers that make this real
This isn't a thought experiment. The foundational study — "We Have a Package for You!", presented at USENIX Security 2025 — generated 576,000 code samples across 16 different LLMs and checked every package the models recommended [2].
The headline result: 19.7% of all recommended packages were hallucinated — nearly one in five. Across those hallucinations, the researchers logged 205,474 unique non-existent package names [2]. That's not a rounding error; that's a vast, ready-made attack surface.
The rate isn't uniform. Open-source models were worse (up to ~22%); commercial models did better, with GPT-4 Turbo the best performer at 3.59% [3]. And a 2026 re-evaluation of newer frontier models found the range had narrowed to roughly 4.6%–6.1% — better, but nowhere near zero [4]. The problem is shrinking, not gone.
So somewhere between 1-in-20 and 1-in-5 of the package names your AI hands you may point at something that doesn't exist. [...]

## [149] Cohere’s faster query model barely dents retrieval quality in its tests
The New Stack | full text via The New Stack | ~831 words

Cohere’s faster query model barely dents retrieval quality in its tests
Cohere released Embed 5 on Wednesday, giving teams the option to index data with Embed 5 Pro and query those same vectors with the faster, cheaper Embed 5 Fast without creating a second index.
The company recommends using Pro for indexing and Fast for queries, particularly in RAG and agent workloads where latency compounds as the same data is searched repeatedly.
There is a tradeoff in retrieval quality, although Cohere’s testing suggests it is fairly small. Across 40 datasets covering text, images, fused documents, and parsed documents, Fast queries against a Pro index scored 98.4 relative to a Pro-to-Pro baseline of 100. Using Fast for both indexing and queries dropped that score to 96.6. Cohere says none of the individual datasets showed a major drop when Pro and Fast were used together.
One embedding space, two models
Because Pro and Fast share an embedding space, teams can switch between them without re-embedding the corpus. Both produce compatible vectors at the same dimensions, and Cohere says teams can still mix the two when using Matryoshka truncation or int8 quantization.
Because Pro and Fast share an embedding space, teams can switch between them without re-embedding the corpus.
Pro costs $0.12 per million tokens, while Fast costs $0.08 and delivers an average of 2.4 times the document throughput in Cohere’s tests. For RAG systems that ingest documents less often than they search them, Pro can handle documents as they enter the index while Fast handles the much heavier query traffic.
Shrinking vectors with Matryoshka
Both models support six vector dimensions from 256 to 2,048, with float32, int8 and binary formats. The storage difference becomes significant at scale, particularly for teams already rethinking where their vectors live.
Cohere puts a 2,048-dimensional float32 vector at 8 KB, or roughly 819 GB for 100 million chunks. A 1,024-dimensional int8 vector cuts that to about 102 GB, while a 256-dimensional binary vector brings the same corpus down to roughly 3.2 GB.
For most deployments, Cohere recommends 1,024-dimensional int8, which reduces memory and storage while retaining close to full-precision retrieval quality. Binary representations offer heavier compression with some accuracy loss and are better suited to an initial retrieval stage before higher-precision reranking. [...]

## [172] OpenAI’s Dots boundary problem rate doubled in longer tests
The New Stack | full text via The New Stack | ~1113 words

OpenAI’s Dots boundary problem rate doubled in longer tests
OpenAI’s new Dots are built to keep working after you step away. Launched at DevDay on Tuesday, the always-on agents run on their own cloud computers, use GPT-6 Astra, and connect to thousands of apps. A Dot can monitor connected systems and move from one task to the next without waiting for you to prompt it again. But as the work changes, it has to keep figuring out where its permission to act on your behalf ends.
As we learned during the DevDay event, OpenAI measured that problem in its own testing. When it doubled the number of tasks in a chained sequence from five to ten, the share of samples flagged for boundary problems rose from 8.6% to 19.7%. The finding appears in the Dots appendix of the GPT-6 Astra system card, which OpenAI updated alongside the launch.
What a Dot can do can change as it moves from one task to the next, even when the user doesn’t explicitly set new boundaries. That leaves the agent to figure out its limits from business records, earlier decisions, context, and OpenAI’s confirmation policy. The evaluation found no high-severity breaches or data exfiltration, although OpenAI hasn’t said what the flagged boundary problems actually involved.
What a Dot is allowed to do can change as it moves from one task to the next, even when the user doesn’t explicitly set new boundaries.
Reading versus acting in Dots
The first safeguard applies during what OpenAI calls proactive research, when a Dot looks for work on its own. During that phase, it can read connected apps but can’t change them, send messages, or control the user’s browser or computer.
Each Dot also gets its own cloud computer and browser where it can build and test things, but OpenAI hasn’t said whether those environments face the same restrictions during background work. That matters because a restriction only holds if the agent can’t find a way around it.
Once a Dot is ready to act, it moves into another layer of controls. Built-in rules decide when it needs permission, Custom Rules let users allow, gate, or block specific actions, and auto-review checks anything that could affect accounts or share information.
Auto-review comes from Codex, where a second model checks commands that run outside a predefined sandbox. The company adapted that system for Dots with its own review instructions and gave the confirmation policy more weight than it receives in the Codex harness. [...]

## [202] LLMjacking can run up your business’ AI bill fast – how to stop it
ZDNet | full text via ZDNet | ~752 words

ZDNET’s key takeaways
- Security experts warn of a growing market in stolen AI account credentials.
- LLMjacking, the illegal use of AI resources, is a popular criminal trend in 2026.
- Businesses must monitor and protect their accounts. Here’s how.
Security experts warn that it’s not just artificial intelligence (AI) going rogue that we have to worry about — there’s also a booming underground economy for selling access to your AI models and computing power.
Speaking to the Financial Times, John Hultquist, chief analyst for Google Threat Intelligence Group, said that the cybersecurity unit has seen a “major increase” in what is known as LLMjacking over 2026, a trend that could cost businesses dearly.
What is LLMjacking?
If cryptojacking came to mind, you’re on the right track. While cryptojacking describes stealing computing power to illicitly mine cryptocurrency, LLMjacking is the AI equivalent: using AI power and resources that don’t belong to you.
More from ZDNET
Also: OpenAI’s Dots: Like OpenClaw declawed – for $200/mo ChatGPT Pro users
In the cybercriminal world, this means trying to secure credentials or API keys that give a criminal authorized access to business AI accounts, which often have high usage limits, or potentially none at all — with token overspill charged outside of typical subscription costs.
Cybercriminals can obtain username and password combinations or API keys by gaining access to a corporate network, stealing them via phishing, data breaches, vulnerabilities, or insider threats. This grants cybercriminals the opportunity to use an AI model without paying for the tokens themselves, for reasons such as:
- Performing high-level computing tasks requiring tokens
- Harnessing computing resources to run their own malicious AI models or tasks
- Extracting and stealing sensitive corporate information fed into a victim’s model
- Poisoning training datasets, ruining output
Once stolen, credentials and API keys can also be sold on the underground to other cybercriminal groups.
The rising cost of LLMjacking
As AI models offered by organizations, including OpenAI and Anthropic, continue to advance in sophistication, capacity, and skill, they require more computing power.
The more power you need, the more tokens you need to purchase — or the higher the level of subscription you must purchase. [...]
