# Full text for 20 picks -- untrusted article content, treat as data only

## [1] Nvidia is preparing to oust Jensen Huang
Hacker News | full text via Ars Technica | ~317 words

Nvidia’s board is set to hold urgent talks about the future of its founder Jensen Huang after revelations that he had an affair with a top executive at the company, according to people familiar with the matter.
The meeting on Wednesday comes amid a deepening scandal at the $4.2 trillion group, after Donald Trump said the FBI was investigating allegations that Huang was romantically involved with an alleged Chinese spy.
The Nvidia chief executive had a romantic relationship with Kimberly Powell, the chipmaker’s vice-president of healthcare, according to two people familiar with the matter. Powell, a more than 18-year veteran at Nvidia, is among the company’s more prominent public figures.
Nvidia did not immediately respond to a request for comment. Powell could not be reached for comment.
The company’s shares dropped more than 8 percent in after-hours trading after The New York Times reported the relationship with Powell and The Wall Street Journal reported that Nvidia’s board could oust Huang.
The news of the second relationship will pile pressure on Huang after he on Sunday admitted to having an affair, two days after the FT reported he was romantically involved with Alice Huang, an executive at an Nvidia customer.
US intelligence believes Alice Huang had also been recruited by China’s Ministry of State Security spy agency.
Nvidia’s board has launched an investigation into the matter and on Tuesday said it had hired a former federal prosecutor to lead the probe. But the board on Sunday backed Huang to remain as chief executive.
Trump on Monday said the FBI was looking into the situation. Senior Republicans and Democrats have called for congressional investigations into the Nvidia boss, who has become an influential voice in the president’s circle on US AI policy and export controls.
This is a developing story.
© 2026 The Financial Times Ltd. All rights reserved. Not to be redistributed, copied, or modified in any way.

## [37] Test your applications against AWS locally with AWS Emulator
AWS News Blog | full text via AWS News Blog | ~1776 words

AWS News Blog
Test your applications against AWS locally with AWS Emulator
Today we’re announcing AWS Emulator, a local emulator for Amazon Web Services (AWS) that you run on your machine. The AWS Command Line Interface (AWS CLI), the AWS SDKs, and your coding agents speak to it over a local HTTPS endpoint using the same AWS APIs they would use in the cloud, from your laptop. AWS Emulator has no additional service fee. You pay only for AWS resources when you deploy on AWS. Its source is on GitHub. You install it from an RPM or Debian package on Linux, and on macOS and Windows you run it in Docker.
How it works
You install the emulator, start it, and point your tools at the local endpoint. When AWS Emulator starts, it generates its own credentials, a config file, and a certificate, and writes them to ~/.aws/emulator/9297/. You set environment variables so the AWS SDK talks to your laptop instead of AWS, and your application code stays unchanged.
From there, your existing tests, CLI scripts, and coding agents keep working the way they already do. A unit test that creates an Amazon DynamoDB table, writes an item, and reads it back is the same test, and it runs on your machine without a deployment. A coding agent can create resources, check the result, and iterate again without waiting on a deployment in a Region.
The emulator is implemented in Rust so that it stays light on CPU and memory on a laptop. It supports the APIs of AWS services that have an API model in the AWS API models repository on GitHub, and because it’s built from those models, the same ones the AWS SDKs use, your requests and the errors you get back have the same shape as on AWS.
If you are a developer, especially one working with coding agents such as Kiro or Claude Code, you can use that loop to test AWS interactions of real complexity locally.
Let’s try it out
To get started, I installed the package on Amazon Linux 2023. The package adds the aws-emulator command to /usr/bin/, so it’s on the path.
PKG=https://downloads.aws.com/aws-emulator/packages/aws-emulator/LTS/latest
sudo dnf install -y $PKG/aws-emulator-x86_64.rpm
aws-emulator -v
On macOS and Windows, you build a Docker image from the short Dockerfile in the documentation and run the emulator in a container. We don’t publish a ready-made image.
I started the emulator with aws-emulator. It serves HTTPS on 127.0.0.1:9297, so only my own computer can reach it, and it writes its log as JSON lines that show the address, the config file, and the certificate file.
aws-emulator
In another terminal, I set the environment variables that point the AWS CLI at the emulator, and unset any variables that could supply real AWS credentials. [...]

## [44] GitHub Makes Agentic Workflows Generally Available with Isolation and Budget Controls
InfoQ | full text via InfoQ | ~561 words

GitHub has made GitHub Agentic Workflows generally available. The open-source project runs coding agents inside GitHub Actions for repository tasks such as issue triage and continuous integration (CI) failure analysis. Agents start with read-only permissions, and any changes they propose are applied by separate jobs that hold their own write tokens.
That separation has limits. The project's FAQ says the protections do not automatically extend to direct write permissions or to custom jobs a workflow author adds, so the safety of a workflow depends on how it is configured. Authors can also add a GitHub Environment protection rule to require a reviewer before a write job runs.
Developers describe the work in natural-language Markdown, with YAML frontmatter for configuration. The project compiles that definition into a standard Actions workflow, which reuses existing runner groups and policy constraints, and teams can use Copilot or bring another coding agent. According to the general availability announcement, agents run in a sandboxed container behind the Agent Workflow Firewall, and a threat-detection job scans proposed changes before they are applied. The project entered public preview in June 2026.
Since the preview, GitHub has added support for Actions Runner Controller (ARC), its Kubernetes operator for self-hosted runners, with Docker-in-Docker (DinD). DinD runs a Docker daemon inside the runner pod so the agent can start its sandbox containers. The project's guide notes that ARC runs the DinD sidecar as a privileged container by default, a privileged component sitting alongside an agent designed around least privilege.
Spending is capped by default. GitHub's documentation prices AI Credits (AIC) at $0.01 each and sets a cap of 1,000 AIC ($10) per run. The project's enterprise controls reference adds defaults of 5,000 AIC a day, 400 AIC per threat-detection run and a 20-minute timeout on the agent step, all of which organisations can override. The gh aw forecast command, no longer experimental, estimates monthly AI credit spending, including threat detection.
In the announcement, Ben Alton, senior manager in Accenture's Strategy, Architecture & Innovation team, said: "One of our leads saved an estimated 29 hours a week on his development work alone." The announcement does not explain how that figure was measured.
Engineers testing the project have taken a more cautious line. In a walkthrough of an issue-triage workflow, Sascha Mirow-Stanitzok, team lead for middleware at freenet, judged the default budget far too generous for triage and capped his runs at 100 AIC, 15 turns and 10 minutes. [...]

## [16] A false smoke alarm almost drowned Jane Street's only NYC datacenter
Hacker News | full text via Hacker News | ~1585 words

How a false smoke alarm almost drowned Jane Street's only NYC datacenter
AI disclosure: this story was written entirely by human hands, with AI doing proof-reading and light edits. Some tasteful imperfections kept to heighten Wabi-Sabi effect.
Everyone’s heard of how awesome Jane Street is. Fewer people have heard about the times something stupid nearly put it out of business and it was saved by grit and dumb luck. I was on the systems team for some of those. Jane Street didn’t do titles, and we on the systems team weren’t above getting our hands dirty. You could think of us as the firm’s blue-collar OCaml programmers: when something broke, we were the ones running through the corridors to fix it. Call this story a Star Trek: Lower Decks view of Jane Street.
For the longest time Jane Street insisted on having its machine room close to its trading floor. When it was 10 people it was cute. When it was 150 people it was starting to feel… odd. Part of the reason for this was intellectual property concern: they didn’t want to risk having their servers stolen by spies who would learn their precious trading strategies. Another reason was technology risk: they wanted to make sure out-of-control automated trading systems could always be shut down by running across the hall and pulling power cables.
Yes, tools existed to mitigate both of these fears. But Jane Street moved irritatingly slowly on this stuff, and they still wanted the last-resort option of yanking power cords. Their risk culture didn’t exclusively come from reading heady thinkpieces. A lot of it was instilled by a partner who’d served on a nuclear submarine, and it showed, mostly in a good way! On a sub, you don’t trust the automation unless there’s a big red-painted, mechanically connected lever you can pull to turn it off.
As the company grew this humble machine room was built out into a respectably sizable datacenter, complete with an online UPS, Computer Room Air Conditioner (CRAC) units, refrigerator-sized network switches, a subterranean diesel backup generator and about 10 rows of server cabinets, 10 cabinets deep. Oh, and it was all crammed into the middle of a skyscraper called 1 New York Plaza, which was otherwise just a normal office building.
When I first landed my job at Jane Street I was commuting to the southern tip of Manhattan all of the way from Queens, an hour or more each way. I’d gone to a magnet high school in the city, so I’d been doing commutes like that since I was a teenager, and I was tired of it.
Now that I was making big Wall Street money I decided I’d get an apartment. A real estate agent kept trying to show me what they called “panty droppers”, but I was only interested in one thing: proximity to the office. [...]

## [71] Gemini 4 Carbon is now available
TLDR Tech | full text via TLDR Tech | ~1893 words

Gemini 4 Carbon is now available
Today, we’re making Gemini 4 Carbon available to developers, enterprises, scientists, and consumers. Carbon is our strongest model with frontier performance in cybersecurity capabilities and long-horizon agentic workflows across complex knowledge work, software engineering, and scientific reasoning.
Two weeks ago, we released Carbon to a set of cybersecurity defenders via our Fairwind Program. Following our recent launch of Gemini 4 Argon, Carbon pushes the frontier even further. Argon remains the ideal choice for the majority of software engineering and knowledge work, while Carbon is built for tasks that test the limits of a model’s intelligence like complex, multi-step coding and debugging and open-ended scientific research and discovery — using more tokens than Argon to explore thoroughly, reason deeply, and run extended verification loops.
Across independent benchmarks designed to test model performance in real workflows, Carbon pairs frontier accuracy with practical production economics. It ranks #1 on CursorBench 4.0, Perplexity’s WANDR, and Zapier’s AutomationBench at more than 2X lower cost per task compared to the next best external model.
To put Carbon’s capabilities to work on larger and complex projects, we’re previewing /swarm in Google Antigravity, turning a single prompt into a coordinated team of agents you can track in real time. Developers can assign Carbon to roles that demand the deepest reasoning, like architectural design, coordination, and auditing, while pairing it with faster, lighter models across parallel isolated workspaces and adversarial verifiers that test every change.
Gemini 4 Carbon is available via the API in Google AI Studio and Gemini for business for all paying developers and enterprises, at the same introductory price 1 as Gemini 4 Argon ($2 per million input tokens and $10 per million output tokens). It is also rolling out to all Google AI Ultra subscribers in Google Antigravity, the Gemini app, and AI Mode in Search.
Higher-precision knowledge work, artifact generation, and data analysis
Across legal, finance, and enterprise operations, Gemini 4 Carbon combines frontier visual understanding, reasoning, and exhaustive retrieval to synthesize grounded insights across large sets of dense documents and data. It follows strict schemas and formatting to generate polished and precise spreadsheets, presentations, and reports.
Existing benchmarks don’t adequately capture how agents reason natively over dense files with charts, images, blueprints, schematics, and tables, so we partnered with Artificial Analysis to launch the new Multimodal Knowledge Agent (MKA) benchmark that tests a model’s multimodal performance in agentic workflows. [...]

## [8] United Airlines bans AI agents from booking flights on behalf of travelers
Hacker News | full text via Hacker News | ~391 words

United Airlines bans AI agents from booking flights on behalf of travelers
United Airlines said on Wednesday that it is banning artificial intelligence agents from making flight reservations on behalf of travelers, citing security risks and the possibility that such actions could violate federal rules.
Many consumers are turning to AI agents such as Meta's Muse and OpenAI's dots to complete tasks ranging from researching products and tracking down deals to making purchases.
To make an airline booking, an AI agent requires access to a customer's personal information, including credentials like payment information. United has a problem with that, saying that "sharing account credentials with personal, third-party, AI assistants can expose sensitive information, and actions taken by these tools may result in unintended purchases, account changes, or use of MileagePlus miles."
The carrier also said that using an AI agent to, for example, check in for a flight could violate federal regulations, including rules requiring travelers to verify in person that their luggage does not contain banned substances.
"As a result, United is taking steps to restrict access — directly within our digital platforms and indirectly via travel agencies and aggregators — to prohibit use by unauthorized, third-party personal AI agents or assistants," said the airline, which is updating its booking and ticketing policies to reflect the new rule.
United's new policy suggests the company wants to retain control over the customer booking process, said Henry Harteveldt, an aviation analyst at Atmosphere Research Group.
"United is saying they don't want to add yet another, and potentially even more powerful, intermediary than they already face in terms of Google search, price-comparison metasearch sites and online travel agencies," he told CBS News. "Flight searches cost airlines money, and undoubtedly United wants to avoid the expense associated with the surge of AI bot flight searches."
Other airlines are taking a different tack to the emergence of AI agents. For example, Southwest has made its flight inventory viewable to ChatGPT users, who can access the airline's website through the AI app.
United fares will continue to be bookable through flight aggregators such as Kayak, Hopper and Google Flights, Harteveldt said, adding that "consumers shouldn't find it any more difficult to find good fares on the airline."
"But by blocking the AI bots, United won't make it any easier to find its fares, either," he said.

## [73] Anthropic to Seek $1.3 Trillion Valuation in IPO
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 401) | ~77 words

Anthropic plans to sell 825 million shares at a range of $70 to $78 a share in its initial public offering, which is expected to start trading on Thursday of next week. The company expects to raise an additional $26 billion from big investors, including Google and AMD. Some Anthropic executives and founding members plan to sell around 23.6 million shares in the offering. At the planned valuation, Anthropic's IPO won't top SpaceX's record-breaking offering in June.

## [156] Ukraine Strikes Cause Permanent Data Loss at Russia's Yandex Cloud
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~91 words

Russia's Yandex says 2.84% of customer data has been permanently lost following Ukrainian strikes on data centers in the country. "According to the company, recovery is impossible because of critical damage to equipment and the lack of backup copies on the platform," reports UNITED24 Media. From the report: Yandex clarified that customers who had previously enabled the platform's backup tools did not experience any data loss, as their information remained fully preserved. The incident has prompted the company to revise its approach to data protection and disaster recovery, particularly the def

## [107] NVIDIA Expands Open Source Commitment With OpenShell Donation and New AI Infrastructure
NVIDIA Blog | full text via NVIDIA Blog | ~805 words

Kubernetes, the open source system that manages how applications run across thousands of AI factories, has become the foundation for AI, and the demands on it are only growing.
To help meet them, NVIDIA is deepening its commitment to open source at KubeCon + CloudNativeCon, the flagship conference for the Kubernetes and cloud-native communities.
NVIDIA is contributing NVIDIA OpenShell, an open source runtime for securing and governing autonomous agents, to the Cloud Native Computing Foundation (CNCF), a nonprofit that is part of the Linux Foundation and the host of KubeCon. As a CNCF Sandbox project, OpenShell will be governed by the organizations building it into their products and strengthened by the expertise of security professionals worldwide.
NVIDIA is also contributing to Agent Substrate, an open source Google-led framework for operating long-running agent workloads at scale on Kubernetes that has been accepted into the CNCF Sandbox.
Additionally, NVIDIA announced new components of the NVIDIA DSX AI Factory Platform: NVIDIA Kubernetes Engine, NVIDIA Kubernetes Recipes and NVIDIA Snapshot. These tools help teams deploy, manage and scale GPU infrastructure on Kubernetes for AI factories.
Together, these advancements mark a step forward in making Kubernetes the leading foundation for AI workloads at scale — empowering developers to build safer, more efficient AI infrastructure for the future.
Securing AI Agents in the Open
NVIDIA’s contribution of OpenShell to CNCF puts security infrastructure for autonomous agents in the community’s hands to build, inspect and improve — accelerating development and hardening its safeguards.
“The cloud-native community has a new infrastructure challenge: giving agents secure environments in which to operate,” said Jim Zemlin, CEO of the Linux Foundation. “NVIDIA’s contribution of OpenShell to CNCF gives developers a shared foundation to build on and an opportunity to shape how agent security evolves. Bringing this work into the community enables broader collaboration on infrastructure that will be critical to the next generation of cloud-native applications.”
OpenShell gives organizations control over what AI agents can do. It applies deterministic controls to agent activity, so teams can enforce policies as agents use tools, access inference services and execute workloads. Its extensible architecture lets teams connect their own compute, inference providers, credential storage and monitoring tools. This allows organizations to apply governance across different deployment environments while integrating OpenShell with their existing enterprise systems.
Hundreds of organizations have put OpenShell to use, and the project has received tens of thousands of contributions in less than a year since launch. [...]

## [106] Google Finds That Technical Debt Can Derail Coding Agents through "Agent Distraction"
InfoQ | full text via InfoQ | ~539 words

In a recent article, Google senior staff software engineer Sam Saccone and senior staff data scientist Madhuri Garikapati highlighted the cost of agent distraction, where AI coding agents get derailed by stale technical debt, such as old TODO comments, obsolete bug references, and outdated specs, leading them to embark on unrequested "side-quests".
Obsolete specs, long resolved bugs, and lagging documentation no longer rest in long forgotten corners of the codebase, but rather are unintentionally ingested as context indirecting and misdirecting the next wave of coders - the agents.
According to the authors, at best, agent distraction increases token consumption and execution time; at worst, it can lead agents to "incorrect logic and decisions". To investigate this impact, they focused on TODO(bug/...) comments, which, as they note, "tend to be left behind long after the underlying bug is resolved or abandoned".
By cross-referencing every TODO an agent encounters against the TODO's bug status and the user's prompt, we can automatically separate valid work from wasted detours at scale.
Using distributed traces from thousands of engineers and hundreds of millions of agent steps, Google found that approximately 13% of sessions exposed agents to inline TODO/FIXME references, leading agents to take action targeting the reference bug in 6% of those cases. In most cases, the prompt did not even mention the referenced bug. Furthermore, in 41% of these unprompted detours, the agent worked on tickets that were already closed; in 57% of them they worked on bugs that were still open, but fell outside the scope of the developer's request, which the investigators classified as "scope creep".
Using a multi-way fixed-effects regression with developer-clustered standard errors, the investigators found that these detours add substantial overhead per session, with 70% more steps, 77% more tokens, and 105% more wait time.
To address this issue, Google developed scanner agents to identify and clean up obsolete TODOs across the codebase. In some cases, the agents had to inspect years of git history to be able to confirm that both the TODO and the intent behind it were obsolete. However, only once confirmed this, they submitted a PR to remove the outdated reference from the codebase.
As a result of this multi-layer approach, our todo cleaner has been able to remove thousands of actually obsolete references over the last 6 months exceeding 95% acceptance from human reviewers.
The investigators conclude that tools such as presubmit analyzers, codebase scanners, and automated agents can help mitigate "agent distraction" and thus improve the effectiveness of AI coding agents. [...]

## [211] A Session-Start Hook Raised Claude Code Skill Firing From 15% to 62%
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~25 words

A software tester ran six testing skills on Haiku, Sonnet, and Opus; pushy descriptions added only 5 points, and near-miss requests never fired a skill.

## [39] For the first time, a C++ standard failed to pass the national bodies
Lobsters | full text via Lobsters | ~3328 words

*Pops cork*.
It looks like it happened! A historic first, for better or worse.
This is a sign that C++ is (still) struggling with its governance (see a previous article on cultural issues within C++ here). This is a big deal even if you do not care about programming languages. C++ is arguably the most important programming language in existence.
Your computer runs on C or C++. The web browser you are using to read this is written in C++. ~All programming languages depend on C++ (often through LLVM). Likewise, ~all websites with performance requirements (e.g. YouTube) depend on C++, ~all data storage, game engines, finance, etc.
In a world that is drowning in exciting new vulnerabilities in ~all software, the ability of C++ to change and adjust to changing times affects you.
Let’s take a step back and get an overview. The initial source was a post by Robert Seacord on LinkedIn:
In a comment, J. Daniel García adds: “There were 12 countries that abstained. In several cases because they could not reach to a common position. That is another signal of a contested draft.”
Now, before we get into the facts: This is not a good look for C++.
There have been multiple fights over the future direction of the C++ language, but no C++ standard ever failed to be signed off by the national bodies.
The national body vote is considered to be a formality. By the time the vote reaches the national bodies all disagreements should’ve been sorted out by WG21 (Working Group 21, i.e. the C++ Standards Committee).
Truly controversial features should never make it this far, since they should never be added to the C++26 working draft in the first place. This is a sign of division in the C++ community, in some form or another, and completely independently of whether you agree with this result or not.
Here, “Added to the C++26 working draft” is essentially accepting the pull request. Everyone is working towards the C++26 release, and people contribute to it with papers. Papers lead to votes, which then lead to amendments of the draft. Finally (this is where we are) wording passes happen, and it gets signed off, rubber-stamped and released. Phrased like this, the ISO process sounds sensible enough, but trust me, it’s actually kind of a nightmare.
Needless to say, the debates are raging, with comments on all sides: So many discussions.
Wait, how did the voting break down? What are P-members???
Quick explanation: The national bodies execute a single vote. To pass the national bodies, the draft has to meet two bars:
- At least two-thirds of the participating voting members have to vote Yes.
- At most one quarter of all voting members may vote No.
If the above posts are correct, then the draft failed to meet both bars. [...]

## [57] Angular's TypeScript 7-Powered Compiler Enters Beta with Rust-Based Preprocessor
InfoQ | full text via InfoQ | ~551 words

The Angular team has shared details of a new version of its compiler, the Angular Preprocessor (ngp), which rewrites the analysis stage of the toolchain in Rust to clear the way for TypeScript 7 adoption. Alex Rickabaugh and Mark Techson announced the work on the Angular team blog in late September, shortly after Microsoft shipped TypeScript 7.0, whose Go-based rewrite removed the ts.Transformer API that Angular's ahead-of-time compiler depends on.
The existing compiler, ngc, wraps tsc and uses the Transformer API to turn decorators such as @Component and @Pipe into runtime instructions. The Go port offers no cross-language equivalent, and crossing the JS/Go boundary at every file would be prohibitive. The Angular team's answer is to decouple compilation from TypeScript's APIs and rebuild it on Oxc, the VoidZero Rust toolchain already powering Vite. The team pointed to the plan on X, framing it as a partial rewrite rather than a fresh start.
ngp runs in three stages. A Rust frontend using Oxc analyses files in parallel to discover Angular declarations and resolve metadata. The existing TypeScript template compiler then emits two artefacts, a runtime file containing the transformed component and a .ngtypecheck.ts file holding the Type Check Block (TCB) for template type-checking. Finally a downstream tool, whether tsgo, tsrs, esbuild or Rolldown, handles type-checking and JavaScript emission independently.
The bulk of ngp landed on 8 October in a single commit of more than 370,000 lines, around 56,000 of them Rust. Cédric Exbrayat of Ninja Squad benchmarked the beta against three projects ranging from 15 to 1,714 components and measured a 2x to 3x speedup on cold builds, with memory use on the largest project falling from 2.8 GB to 1.4 GB. Pairing ngp with tsrs and Rolldown gave the fastest pipeline, with tsgo and esbuild only marginally slower. They concluded there is further gains to be made:
This is already very promising, and there are certainly further gains to be made when the team focuses on performance optimization.
Christopher Holder at push-based.io took a different tack, writing vite-plugin-ngp to compile Angular files on demand. On the Super Productivity codebase (252 components), the dev server reached the first page in 10.5 seconds against 17.4 for ng serve, with template edits applying in 112 milliseconds rather than a 2.6 second full reload. On a generated 5,000-component app the gap widened to 1.6 seconds against 28.4. Holder cautioned that the plugin "is a prototype on a prototype" pinned to 22.3.0-next.2.
On Reddit, a number of developers are excited about the update and write up, with one commenting:
Read the whole article. Impressive. [...]

## [49] JioHotstar Benchmarks Knowledge Bases for AI Coding Agents
InfoQ | full text via InfoQ | ~484 words

JioHotstar evaluated six approaches to helping AI coding agents navigate large codebases, finding that structural code search performed well on clearly defined engineering tasks, while semantic retrieval helped more with ambiguous requirements. The evaluation also found that adding retrieval layers did not consistently improve task completion or reduce token consumption.
Abhishek Bansal, Senior Staff Engineer at JioHotStar, compared filesystem tools, Sourcebot, Graphify, CocoIndex Code, Repowise, and an in-house retrieval-augmented generation (RAG) pipeline. The team evaluated the approaches using subsets of SWE-bench and CodeScaleBench, alongside a custom question-answering harness for JioHotstar's codebase. The experiments used Claude Sonnet as the solving model and measured task accuracy, token consumption, agent turns, and tool usability.
JioHotstar’s benchmark setup for evaluating code retrieval approaches for AI coding agents. (Source: JioHotstar Blog Post)
The filesystem baseline, which relied on locally checked out repositories and standard search and file operations, remained competitive on concrete tasks. Sourcebot, which provides indexed text search, symbol definitions, references, and file reads, performed better than the baseline on harder SWE-bench Verified tasks while also costing less. On simpler SWE-bench Lite tasks, retrieval generally added overhead without consistently improving results.
CodeScaleBench showed a different pattern. Semantic retrieval helped more when agents had to interpret ambiguous problem descriptions and map them to implementation details that were not obvious from exact text or symbol searches. The findings suggest that retrieval approaches should be selected according to task characteristics rather than treated as interchangeable solutions.
The report also highlighted the importance of tool design. Agents frequently preferred familiar developer operations such as searching text, reading files, and locating symbols over higher-level abstractions that required additional verification.
Tool call breakdown by category across coding agent knowledge base approaches. (Source: JioHotstar Blog Post)
Siddharth Vaithinathan raised a broader architectural question in a LinkedIn post discussing the study:
Whether coding agents should understand not only the code but also the company that produced it. He argued that repository indexing alone cannot capture why architectural decisions were made, which constraints shaped them, or what earlier incidents taught the engineering team.
Vaithinathan suggested extending agent knowledge beyond code and documentation to include architecture, constraints, decisions, rationale, incidents, and outcomes. [...]

## [50] AlphaGenome 2: Deciphering how cells read DNA to better understand disease
Google DeepMind Blog | full text via Google DeepMind Blog | ~1673 words

AlphaGenome 2: Deciphering how cells read DNA to better understand disease
Our next-generation DNA sequence model bridges single-cell biology and human genetics, predicting how genetic variants affect hundreds of human cell types.
Today, we are announcing AlphaGenome 2, our next-generation model that predicts how DNA sequences and their variations impact specific human cell types, giving scientists a powerful new tool to uncover the cellular drivers of disease.
Cells are the building blocks of life. Every cell in our body carries the same DNA blueprint, yet each cell type and state—like a heart muscle cell or an immune cell fighting an infection—switches different genes on or off to do its job. Global efforts like the Human Cell Atlas are mapping this gene expression for millions of cells, but it is still an unsolved challenge to predict how subtle DNA variations affect this expression in cells, which is a key driver of human traits and disease.
Last year, we launched AlphaGenome to predict how DNA variants affect molecular activity across broad tissues. We expanded its reach with AlphaGenome Atlas, a platform containing predictions for all 9 billion possible single-letter changes in the human genome. These tools help researchers prioritize and interpret variant effects, driving discoveries in rare diseases, complex traits, and fundamental biology.
By zooming in from broad tissue averages to individual cell types and cell states, and redesigning the model’s architecture, AlphaGenome 2 represents a step-change improvement in variant predictive performance. Importantly, it allows researchers to predict variant effects in disease-relevant cells that would be missed in broad-tissue models, as well as predictions for cell and disease states that the model hasn’t seen before.
AlphaGenome 2 identifies nearly twice as many variants that change gene expression in cells, compared to our previous state-of-the-art model. Trained on more than 100 million individual cell profiles across 68 tissues, the model turns static cell atlases into a predictive engine for human genetics. AlphaGenome 2 is available today for non-commercial research via the AlphaGenome API, and in private preview for commercial research.
Redesigning AlphaGenome for specific cell types
The first AlphaGenome model took a million-letter DNA sequence and predicted properties across thousands of experiments from many tissues all at once. While efficient, this parallel approach spread the model’s capacity thin and made it hard to capture subtle differences between closely related cell types.
To improve this, we fundamentally redesigned how cell types are treated by the model. [...]

## [43] IBM to offer access to a dual-processor quantum system in 2027
Ars Technica | full text via Ars Technica | ~352 words

IBM’s Quantum Developer’s Conference is being held this week, and the company is using the gathering to provide an update to its roadmap: It is aiming to make error-corrected quantum computers before the decade is out.
The changes greatly expand the scope of its next-generation Nighthawk general-use processors by adding a version with over 500 programmable qubits. At the same time, it’s stepping back a bit on its plan to link multiple Nighthawk processors together, dropping the intended number of linked systems from nine to two.
The total number of qubits planned for next year will remain the same; how the company is getting there, however, will be different.
Meanwhile, the company is touting the performance boost achieved via a major change that was made in the generation of Nighthawk processors released in September: hardware-based qubit resets.
Parallel roadmaps
IBM’s most recent roadmap to error-corrected quantum computing has two parallel tracks. One is focused on technical development, with the company testing technologies it will need to build error-corrected hardware, but that may not be useful outside of that context. The other is public-facing, focused on delivering high-performance processors for people interested in testing algorithms on quantum systems today.
The reason for this split is that IBM plans to use an error-correction “code” that requires a specific number of hardware qubits connected in a specific geometry, along with additional hardware qubits needed to perform operations on that code. You could potentially run some algorithms directly on this hardware without error correction, but it wouldn’t necessarily be optimal. So IBM is also offering a more general-purpose processor in parallel, called Nighthawk.
For past generations of its processors, the company has often developed revisions that improve performance in various ways. So while the roadmap lists only one processor labeled Heron, there were two subsequent revisions to Heron after its release. Throughout 2028, however, the company’s public-facing track will see nothing but revisions to the current generation of processors, called Nighthawk, which started with 120 hardware qubits and the expectation of performing about 5,000 gate operations before errors become too likely to rely on its output.

## [195] FreeBSD Working To Establish An AI Policy After Polling Developers
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~29 words

The FreeBSD Project published its Q3'2026 status report on Tuesday that outlines a number of development initiatives to ongoing work around an AI policy for this BSD operating system...

## [149] With $720M round, Britain’s Fractile gets a leg up in the race for AI chips
TechCrunch | full text via TechCrunch | ~313 words

Fractile, a British startup developing AI chips, has raised a $720 million Series C backed by Britain’s Sovereign AI Fund with hopes of “ensuring the U.K. has a greater stake in the hardware that will underpin its future economy,” its government stated.
Alongside the likes of Axelera, Etched, and OLIX, this makes Fractile one of the top-funded startup players in the race for purpose-built AI chips. Such chips are one of several avenues being explored to reduce the cost of inference — aka using increasingly demanding AI models in production.
However, Fractile seeks to go beyond hardware with a full-stack approach that also includes a machine learning compiler to maximize the speed at which LLMs will get executed on its chips.
As a result, the company frames itself as a frontier AI company, and its latest round led by Thrive Capital, Founders Fund, Lightspeed Venture Partners, and Redpoint was priced accordingly. According to the British government, the valuation was “over £5 billion” — quite possibly $7 billion, a figure reported both by the Financial Times and a Reuters source.
Still, Fractile’s main differentiator will arguably be its hardware design. After a pivot, its approach now revolves on DRAM, the most common type of RAM, but stacked on top of each chip in such a way that it is hoping will bypass the usual trade-off between memory and capacity.
This trade-off has become more problematic with the rise of agentic AI, as companies seek to perform longer chains of tasks with large models without compromising on speed. As compute struggles to keep up, hopes are high for AI chips, despite their limited availability to date.
In a LinkedIn post, Fractile CEO Walter Goodwin wrote that “there is still a lot of work ahead” for the company, and that the new funding will enable the startup to “ship [its] first chips and systems next year.”

## [148] CoreWeave turns to customer prepayments, shorter contracts to fund AI growth
TechCrunch | full text via TechCrunch | ~588 words

CoreWeave is rewriting how it pays for the AI boom, according to the company’s third-quarter earnings, reported on Tuesday. CoreWeave, a neocloud that rents out the computing power behind AI, said it’s increasingly asking customers to pay up front, borrowing against specific contracts, and even pursuing short-term deals that could lead to higher prices.
The new strategies could help CoreWeave finance its growth more efficiently while squeezing more cash from existing infrastructure. But these bets only hold if today’s demand and pricing power continue.
CoreWeave reported $3.66 billion in revenue, up 168% from the year prior, but it also posted a $709 million net loss and $846 million in quarterly interest expense.
“We will not use the unsecured debt market to fund our business at current yields, nor do we need to,” CoreWeave CEO Michael Intrator said during Tuesday’s earnings call.
Instead, CoreWeave’s plan is to rely on loans backed by specific customer contracts, drawing on funds as needed to finance most of infrastructure it still has to build to deliver on its significant backlog of $132.5 billion.
CoreWeave also said it expects about $9 billion in customer prepayments and deposits over the next three months, including more than $3 billion tied to signing new customer contracts for capacity it has already built, which requires no additional spending on hardware.
Rivals Nebius and IREN have also relied on hefty Microsoft prepayments to pay for computing capacity, signaling that the industry is moving toward asking Big Tech to pay up for their buildouts.
Upfront payments could alleviate CoreWeave’s immediate borrowing needs, but they also commit the company to providing services at a price that might be less attractive down the road if compute demand continues to surge.
CoreWeave is also looking to capitalize on that growing demand by signing more shorter-term contracts that can command much higher prices.
The company raised prices across its offerings by about 25% in July and by another 10% later in the quarter. Prices are still climbing this quarter, in a way that “more than offset[s] cost increases,” said Intrator.
“We are also allocating more capacity to short-term opportunities, where the pricing justifies it, selling capacity at more than $40 million per megawatt annually, while pricing for new infrastructure on four and five-year contracts is moving to $20 million to $25 million per megawatt,” the chief executive said.
CoreWeave’s financing strategy now revolves around those opportunities. In August, the company closed a $2.6 billion loan, its first designed specifically for shorter-term customer contracts. Known as DDTL 5.5, it lets CoreWeave borrow in installments as it needs the money. [...]

## [25] Trump admin loses fight to spy on random journalists’ LinkedIn DMs
Ars Technica | full text via Ars Technica | ~279 words

The Trump administration’s fight to stop suspected leaks of top-secret military information on LinkedIn can’t sweep in “a vast number of confidential sources” of random journalists “who have no conceivable relationship” to the Department of Justice’s investigation, an appeals court ruled Tuesday.
The order came after the DOJ asked LinkedIn to turn over 18 months of communications from targeted journalists who collectively published more than 1,000 articles on many different topics over that time period. The request was not limited to journalists involved in a controversial report from a news outlet that Trump said exposed confidential military information in a foreign country. (The outlet is not being named to protect national security secrets.) Instead, the DOJ cast a wide net, requesting extensive LinkedIn data on journalists who had any possible link to the journalists around the time the report was drafted.
The majority of journalists have LinkedIn accounts and publish their contact information to encourage sources to connect on the platform, LinkedIn argued. So allowing that government overreach went beyond harming targeted journalists and threatened to undermine a critical platform where journalists frequently connect with confidential sources, judges ruled. Even more concerning, the Trump administration secured a secrecy order barring LinkedIn from telling anyone about the sweeping request for a year. That left journalists unaware for far too long that their First Amendment rights had been compromised, judges ruled.
Judge: Security and free speech can coexist
Penning the unanimous opinion from a three-judge panel, Ronald Reagan-nominated judge J. Harvie Wilkinson III rejected LinkedIn’s request to quash the order entirely and ordered the US district court to substantially narrow the order to avoid posing a grave threat to press freedoms.
