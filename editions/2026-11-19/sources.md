# Full text for 24 picks -- untrusted article content, treat as data only

## [164] OpenAI spent $1.2 million finding nearly 1,000 Linux security flaws. Sam Altman says this is just the beginning.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~40 words

OpenAI spent approximately $1.2 million in API costs to generate working exploits for 948 Linux kernel vulnerabilities. At The New The post OpenAI spent $1.2 million finding nearly 1,000 Linux security flaws. Sam Altman says this is just the begi

## [131] Anthropic reportedly prices IPO at $83 a share, above projected range
TechCrunch | full text via TechCrunch | ~416 words

Anthropic has reportedly priced its long-awaited IPO at $83 per share, above its initial range of $70 to $78, signaling strong investor appetite for one of the companies at the center of the AI boom, despite market jitters following the departure of Nvidia CEO Jensen Huang, which shook confidence in the industry.
At the IPO price, Anthropic is reportedly valued at $1.5 trillion on a fully diluted basis, a significant increase from the $965 billion the company reached in May when it raised $65 billion in its last private market round, but below the $2 trillion it was reportedly aiming for several months ago.
Anthropic will begin its life as a public company on Thursday, trading on Nasdaq under the ticker symbol “ANT.” A strong first day of trading would signal that investors remain optimistic about AI adoption, despite recent volatility in AI-driven stocks.
The company’s performance is expected to set expectations for private AI companies, including Anthropic’s main rival OpenAI, which was last reportedly valued at $1.25 billion but has yet to announce plans for an IPO.
Although none of Anthropic’s venture capital investors holds more than a 5% stake in the company, the IPO is a massive windfall for its numerous backers. Investors that own approximately 1% of the company reportedly include Sequoia and former Google CEO Eric Schmidt. Singaporean sovereign wealth fund GIC also holds about a 1% stake in the company, according to a person familiar with the matter. Other backers set to make billions are Iconiq, Menlo Ventures, Coatue, and Sound Ventures, a firm launched by Guy Oseary and actor Ashton Kutcher, and Spark Ventures, the only VC firm known to hold a board seat at the company.
Some of the company’s existing investors, namely Sequoia, Iconiq, Lightspeed, Accel, and Altimeter Capital Management, are so enthusiastic about Anthropic’s future that they were reportedly planning to buy billions of dollars’ worth of the company’s shares in the IPO.
Yet the investors’ holdings in Anthropic pale in comparison to those of the Claude maker’s strategic partners, Amazon, which owns nearly 15% of the company, and Google, which holds almost 14%. A group of major tech companies, including AMD, Broadcom, Google, Micron, Microsoft, Nvidia, and TSMC Partners, have also agreed to purchase $26 billion worth of non-voting shares through a private placement alongside the IPO.
The company’s seven co-founders, including CEO Dario Amodei, each sold nearly 3.4 million shares in the IPO, according to the S-1 filing, bringing in about $282 million for each.

## [7] Unauthenticated remote code execution in Nginx
Hacker News | full text via Hacker News | ~2408 words

Wiz Research, Ikotas Labs, Metnir, Rapid7, and Xint independently uncovered two critical remote code execution vulnerabilities in NGINX, software used to receive and route traffic to production applications and APIs.
Successful exploitation could let attackers take control of affected NGINX servers, steal sensitive data, tamper with websites, or disrupt services.
The vulnerabilities, tracked as CVE-2026-123633 and CVE-2026-123007, are both rated Critical, with a CVSS 4.0 score of 9.2. The flaws are in NGINX itself. Websites and APIs can be exposed even when their own application code is secure. Both vulnerabilities require HTTP/2 to be enabled on the affected NGINX server. Additional conditions are described below. CVE-2026-123007 affects versions dating back to NGINX 1.9.5 in 2015.
We reported our findings to F5, the company behind NGINX, and collaborated with its security team on remediation and coordinated disclosure. Organizations should identify affected deployments and apply the security updates when released.
We recommend updating affected NGINX deployments to the latest release which includes multiple security fixes.
Responsible disclosure timeline
October 21, 2026: Wiz reports the HTTP/2 use-after-free vulnerability, later assigned CVE-2026-123633, to F5, including confirmed remote code execution with an ASLR bypass and a proposed fix. F5 confirms that another research team had previously reported the same vulnerability.
November 10, 2026: F5 supplies a patch for CVE-2026-123633 for review.
November 16, 2026: Wiz reports the second HTTP/2 vulnerability, later assigned CVE-2026-123007, to F5.
November 17, 2026: F5 confirms that the second report matches CVE-2026-123007 and is included in the planned November 18 security release.
November 18, 2026: F5 security release and coordinated public disclosure.
Overview
Wiz Research, Ikotas Labs, Metnir, Rapid7, and Xint independently uncovered CVE-2026-123633 and CVE-2026-123007, two critical unauthenticated remote code execution vulnerabilities in NGINX, and reported them to F5, the company behind NGINX. Successful exploitation can compromise the server running NGINX, allowing attackers to execute code, steal sensitive data, tamper with websites, or disrupt services.
NGINX often handles traffic for several applications, so a single affected deployment can put multiple services at risk. The flaws are in NGINX itself and can affect websites even when their own application code is secure. Both vulnerabilities require HTTP/2 to be enabled on the affected NGINX server. Our testing of CVE-2026-123007 demonstrated code execution on NGINX serving ordinary static files, without a backend application or third-party modules. [...]

## [1] Gemini 4 Neon
Hacker News | full text via Hacker News | ~1617 words

Introducing Gemini 4 Neon
Today, we’re introducing Gemini 4 Neon — bringing frontier-level intelligence with fast end-to-end task completion across complex software engineering, knowledge work, and science workflows.
Neon ranks ahead of comparable models and #3 overall with a score of 61 on the Artificial Analysis Intelligence Index at its xhigh thinking level, landing just behind larger, slower models. On the Vals Index, Neon ranks #2 and lands on the Pareto frontier. Beyond just pushing on raw model capability, we’re continuing to make our models better to work with, Neon ranks #2 on steerability (adapting cleanly to mid-task user corrections) on the new Agent Arena Index. Neon also excels at multi-step instruction following and builds on our ongoing progress to curb fabrication, recording our lowest fabrication rate yet in internal Google Antigravity testing.
The model is priced at $3 per million input tokens ($0.15 per million cached input tokens, a 95% discount) and $15 per million output tokens, with a 1 million-token context window.
Gemini 4 Neon is rolling out today in the Gemini API in Google AI Studio, Gemini for business (via API and model dropdown), for paid Google AI Pro and Ultra subscribers in Google Antigravity, and for Pro and Ultra subscribers in the Gemini app.
Delivers across enterprise, analytical, and scientific work
Enterprise work lives in spreadsheets, PDFs, charts, audio, and video. Neon can synthesize across all of these inputs in a single 1 million-token context window and turns inputs into structured deliverables. Independent evaluations rank Neon as one of the top models and on benchmarks like the Vals Index, it ranks #2 (70.9%), and reaches #1 on both the Legal Research Bench and Tax Agent Bench.
Neon also shows strong wins across categories on Surge AI, ranking #1 on most benchmarks across finance, accounting, spreadsheet modeling, and complex constraint following. It also scores 73.5% on Chartography for reading dense professional charts and performs on par with leading models on Agents' Last Exam v1.1 (75.8%). It achieves #1 overall on both Zapier’s AutomationBench (56.3%) and Andon Labs' Vending-Bench 2 ($16,843), a long-horizon simulation of running a business. Finally, it debuts #2 globally with a score of 1336 on Arena's new Agent Arena Index across 4,200+ real-world agent sessions.
On scientific and mathematical reasoning, spanning quantitative analysis, mathematics, and technical research problems, Neon is best in class on Terminal-Bench Science (70.5%), RiemannBench (84.0%), and HLE-Diamond (71.3%). [...]

## [64] Making sense of Recursive Self Improvement
TLDR Tech | full text via TLDR Tech | ~2865 words

There’s a whiff of an imminent RSI in the air. The theoretical possibility of AIs recursively improving themselves autonomously until we hit singularity has always existed but the recent METR report seems to have spooked a lot of rationalists and AI insiders about how soon it can arrive.
The report that triggered the fear and paranoia is this one, and the chart to pay attention to is the following:
It effectively shows how the rate of progress in AI R&D has roughly doubled at Anthropic since October 2025, and METR attributes most of the acceleration to Anthropic’s own use of AI in R&D. Before moving on to making sense of what’s driving this and its potential implications, keep two caveats in mind:
- This report redacted many important datapoints as Anthropic didn’t let METR share them
- Anthropic is soon going public, so it is in their best interest to project an acceleration (Keep this in mind for the other Anthropic charts below too: they’re from their IPO roadshows)
Despite these caveats, I will make the case that a crude form of recursive improvement in AI models is already happening and it’s simply going to become more sophisticated and significantly scaled up. And whatever we call ASI at the end of it is likely to be jagged.
Current self-improvement: AI models accelerating AI models releases
Well, models are releasing faster lately. There are several factors driving it and perhaps the biggest one is the sprawling data-generation industry that’s $10bn now, growing rapidly and perhaps could be $100bn in a few years. These data generation companies make RL environments to sell to labs on as many economically useful tasks as they can codify.
What does a typical RL environment look like? Imagine slicing the entire economy into sectors and then sub-sectors and sub-sub-sub sectors, and then hiring an expert to design context, task and success rubrics for each one of them. As an example, imagine Finance → Private Equity → Leveraged Buyout → Crossborder LBO as one of the workflows needed to be automated. To automate this, a data generation company would hire an actual expert at it who’d design a simulated but faithful work environment for an agent comprising of data room, Excel sheets, and success criteria. Frontier labs buy these environments by the thousands and do rollouts in their post-training in order for the agent to get better at this task.
The RL-driven improvement has been known for years, but what’s changing rapidly is how AI agents themselves are improving all parts of the RL process. Consider how currently capable AI agents could help speed up the process:
- Interviewing the human experts to elicit their knowledge 
  - Asking them about edge cases, finding inconsistencies, suggesting rubrics, etc. [...]

## [5] Genie 4 is now available
Hacker News | full text via Hacker News | ~730 words

Genie 4 is now available
Earlier this year we introduced Project Genie, an experimental research prototype that lets you generate and explore interactive worlds. Early testers told us they wanted deeper control over what happens inside those worlds, and easier ways to build and share them.
So today, we are rolling out a new Project Genie experience to eligible Google AI Ultra subscribers, making these worlds far more responsive, creative, and social. This update unlocks first-time access to Genie 4, new upgrades to Genie 3, the Project Genie agent which helps users build their vision, and a community gallery to discover, explore, and remix worlds.
Project Genie brings together our most advanced world models alongside our Gemini models, empowering you to generate, step inside, and shape worlds directly from your browser.
Experience Genie 4 in Project Genie
With Genie 4, our most realistic and interactive world model yet, you can now prompt mid-session to change the world you created. Just type a new prompt while you navigate your world and you can edit your environments in real time. Shift the weather, drop in a character, or redirect the action. For the first time, Genie 4 pairs these visuals with real-time native audio that adapts as the scene unfolds, from ambient soundscapes to character dialogue.
Discover new Genie 3 capabilities
While Genie 4 delivers our highest-fidelity visuals, physics, and native audio, Genie 3 remains available in Project Genie’s model picker when you want longer runs or panorama-seeded spaces. Today’s Genie 3 updates include:
- Extended sessions and world chaining: Explore for up to 3 minutes per generation (up from 60 seconds), or link multiple worlds together for longer journeys.
- 360-degree panorama image grounding: Seed new worlds from 360-degree panorama images.
- Real-time in-world events: Dynamically change the environment with natural-language prompts while you explore.
Create new interactive experiences
The new Project Genie agent takes creation beyond a single text or image prompt. Now crafting an interactive universe is as effortless as having a conversation. Simply describe your vision in natural language, and the agent orchestrates Google’s suite of multimodal models to craft initial visuals establishing your world’s signature look, paired with custom background scores tailored to the mood.
You can also bring Gemini models into the session as you explore: it observes what is happening on screen, surfaces context-aware suggestion chips for where to go next, or triggers in-world events automatically as your journey unfolds. [...]

## [82] Higher-Scoring Coding Models Did Not Get More Work Done
arXiv cs.AI | full text via arXiv cs.AI | ~447 words

Computer Science > Software Engineering
  [Submitted on 17 Nov 2026]
Title:Higher-Scoring Coding Models Did Not Get More Work Done
View PDF HTML (experimental)
            Abstract:New coding models advertise themselves on score improvements of coding benchmarks. Yet no study has tested if a model that scores higher on these benchmarks gets more real work done. On June 12, 2026, a U.S. export control directive banned access to Claude Fable 5 for 19 days, which forced users to switch to other models. During this time, most former Fable 5 users switched to Opus 4.8 (11 points lower on SWE-Bench Pro compared to Fable 5). We treat this suspension as a natural experiment, where the people and projects stayed the same and only the model changed, so we could isolate the effect of Fable 5 on user productivity. We tracked GitHub pull requests of 297 Fable 5 users before, during, and after the suspension. We used 8,908 developers who stayed on Opus 4.8 all the time as the control group. We also repeated the comparison across five model upgrades before and after the suspension in 2026 (1,208 developers, 15,442 pull requests). Fitting a difference-in-differences model with developer and date fixed effects, we found that having access to Fable 5 increased the 7-day merge rate of pull requests by only 1.4 percentage points [-1.4; +4.3], which was not statistically significant. Similarly, no significant increases of merge rates were found with the upgrades (weighted mean: -0.9 percentage points [-1.9; +0.2]); all five estimates were negative (95% intervals included 0, did not differ from each other). We also did not observe a significant increase in the number of pull requests merged per week (+2.4% [-4.9%; +10.2%]).
    
Additional Features
Current browse context:
cs.SE
References & Citations
    
    Loading... [...]

## [62] Using a "chaos loop" to harden the Claude Docs launch: 60 server errors across billions of requests
TLDR Tech | full text via TLDR Tech | ~1539 words

Claude Docs is a doc editor that you, your teammates, and Claude all work in together. The interesting part is that a Claude session anywhere, from chat to Claude Code, can open the same doc and read, write, and comment in it live, right next to you. We released Docs on September 16, 2026. This post is about the service that runs underneath it.
Three weeks before Claude Docs opened to the public, it was running as a proof of concept on a single node, used by a few thousand people inside Anthropic. We were racing toward an ambitious launch date, and our own estimate said we'd see millions of docs within the first few days.
We launched on September 16. By September 22, people had created over 4.6 million docs. Across 2 billion requests we saw only 60 server errors, and we never had to roll back. The whole Docs service ran on about 50 memory-optimized pods.
Two decisions got us there:
But honestly, this only worked because our frontier models have gotten much better recently (I used an internal research model roughly comparable to Claude Fable 5.2). In our experience, they can now stick with one goal through a run like this for weeks, which is what helped us hit launch scale in a tight timeline.
A few thousand internal users on one machine told us nothing about whether the service would survive launch, and we obviously didn't have launch traffic to test with.
We wanted real evidence to decide how fast we could roll out. So on September 4, about two weeks before launch, I had Claude drive a staging cluster that mirrored production at over a million synthetic docs a day and break core components on purpose. And then... I just left it running (I've included the full cost at the end of this article).
My setup was pretty simple. The loop was a session in Claude Code that I left running: pick a scenario, run the harness, read the telemetry, propose a fix, ship it to staging, repeat. That session acted as a coordinator and handed most of the work to sub-agents. In the busiest week, that usually meant about 11 sub-agents running at a time, and 30 at the peak. The coordinator also talked to our internal variant of Claude Tag (beta) via the Slack MCP to learn from other infrastructure teams at Anthropic who had scaled similar services. Their agents checked our scaling approach for pitfalls they’d already hit.
The fun part was picking scenarios I thought were paranoid:
Each iteration looked the same. Our testing harness selected a feature like document creation and pushed creation to saturation. Claude then read telemetry using the Datadog MCP and came back with a short menu of options and a recommendation.
If the recommendation was easy to undo, Claude wrote and deployed the change to staging and reran the test. [...]

## [70] Vercel's eve 1.0
TLDR AI | full text via TLDR AI | ~2359 words

Today we're announcing eve 1.0, the open-source framework for building production-ready agents.
Since the public preview in June, we've worked with early adopters to prepare eve for 1.0, shipping 230+ releases and merging thousands of pull requests. With this release, eve is now generally available.
We've made eve faster, expanded integrations, and improved observability. Security controls let you decide which actions need approval and what data gets collected. We've also made it easier for coding agents to build with, measuring that experience with a rigorous evaluation suite.
With eve handling your harness and infrastructure, you and your agent can focus on building instead.
Copy link to headingBuild production agents on a harness you own
The harness in eve is the loop that calls models, runs tools, and delegates work to subagents. You choose the model, add or replace tools, edit instructions, and decide which actions need approval. The open-source Workflow SDK saves progress as the agent runs, so it can pick up from its last completed step after a crash. Multiplayer sessions and agent-to-agent calls are built in.
For managed hosting, deploy your eve agent to Vercel. Vercel Workflows handles durable execution, and Vercel Sandbox runs agent-generated code in isolation.
Build software factories that turn requests into tested pull requests, company brains that answer questions from your business data, or customer-facing agents in your product.
Thousands of businesses already run eve in production for internal and customer-facing agents. Rillet built a software factory on eve that takes in customer requests, converts them into specs, tests the changes, and opens PRs for human review. Rillet tripled its shipping rate in three months. Clay built monty, a data agent that answers employees’ questions in Slack. Just over two months in, 30–40% of the company used it every week.
Lindy's agent framework roundup names eve “Best for durable backend agents”.
Custom agents built with eve plus Vercel workflows. I’m biased but I didn’t mandate this, we felt it was the best solution for us.Mitchell Hashimoto(opens in new tab)
Copy link to headingCollaborate in multiplayer agent sessions
Multiplayer lets several people work with an agent in one shared session. eve keeps track of who said what and directs approvals and sign-ins to the right person. You can set up memory for each user or the whole team.
In the native Slack channel, each thread is one shared session. Approvals appear as buttons that only the right person can answer, and a live task card shows progress and timing. You can follow up in the thread without mentioning the agent again, cancel the current turn, or reset the session from Slack. [...]

## [48] Inside the Codex sandbox
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~22 words

See how Codex runs commands on your machine while enforcing the filesystem and network limits you control across macOS, Linux, and Windows.

## [77] Only the Human Merges
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~812 words

In August I gave my agents a rule: write no comments in the code. Seven weeks later there were about 1,200 new comments. I wrote about that last month.
The same repository has a second rule: an agent never merges. That rule started as a sentence in a file too, and on 24 September an agent merged a change. Four days later the rule became a permission on the server. No agent has merged since.
The first rule is still a sentence in a file. The second is enforced by the server. When an agent asks to merge, the answer is permission_denied.
What the agents do
The first commit in Whelk was on 20 July. One hundred and eight days later the repository had 2,364 commits, and 1,551 of them carried a model as co-author. The agents write the code, open the change, run the checks and answer the review. A panel of reviewer agents reads every change and posts its findings. Native clients for iPhone, iPad, Mac, Android, Linux and the terminal came out of that process, with the server they connect to.
I am the only person in it.
What the agents cannot do
- Merge. I approve a change, and only an approver can ask for a merge.
- Close a task. An agent moves its task to in-review. I move it to done.
- Choose what is next. The ready queue is mine. An agent can file new work in the backlog, and it cannot promote that work.
- Answer its own question. When an agent needs a decision, it puts one concrete question on the task, and the task moves to my queue. The agent may not write the resolution.
- Start a release. Nothing deploys unless a person or a timer starts it.
The verdict of the reviewer panel is advisory for the same reason. An agent can find a problem. An agent cannot decide that the problem is acceptable.
Why rules about how decay
My instructions file is long, and most of it is about how to work: branch size, naming, tone, where a reason gets recorded. I have watched which of those rules hold. The ones a machine enforces hold every time. The ones written as prose hold until an agent has a good local reason to do otherwise, and an agent can usually find one. Each of those 1,200 comments was a small, defensible exception.
So I have stopped adding rules about how in prose. If I care enough about a behavior to write it down, I write a check that fails the build. If I do not care that much, I leave the choice to the agent. Every failure I have traced came from the category in between.
The status that lies
The hardest rule to get right was a definition. An agent that finishes most of a task wants to call the task finished. On a board, “in review” then covers everything from merged and working to a plan and half a branch. I read the board to decide what to check, so a loose status sends me to the wrong place.
The definition is strict now. [...]

## [30] LinkedIn Cuts Daily Spark Shuffle Fetch Failures from 750 to 20 with Apache Celeborn
InfoQ | full text via InfoQ | ~497 words

LinkedIn has deployed Apache Celeborn as a shared remote shuffle platform across the majority of its Apache Spark and Apache Flink workloads, separating intermediate data storage from compute infrastructure. The deployment reduces daily shuffle fetch failures from approximately 750 to 20, lowers compute costs by 10%, and improves application runtimes by 14%, compared with its previous Magnet implementation.
Daily shuffle fetch failures decreased from approximately 750 to 20 (Source: LinkedIn Blog Post)
LinkedIn's offline data platform executes more than 300,000 Spark jobs daily across thousands of production nodes, consuming approximately 200 petabyte-hours of compute. As the company moves toward a unified Flink architecture for real-time and historical processing, large-scale backfills introduce additional shuffle workloads. Shuffle moves intermediate data between processing stages, potentially stressing networks, disks, and application runtimes.
LinkedIn previously addressed shuffle read inefficiencies with Magnet, its push-based shuffle implementation contributed to Apache Spark 3.2. Magnet aggregates shuffle blocks by reducer partition into larger files, reducing random disk reads. However, shuffle storage remained within the compute cluster, where External Shuffle Services shared CPU, memory, disk I/O, and network resources with compute workloads.
With Apache Celeborn, map tasks push intermediate data to dedicated workers, which aggregate and store partitions independently of compute executors. Reducers fetch the data directly from these workers, allowing shuffle storage to scale independently of compute and reducing dependence on executor lifecycles. Unlike Magnet, which uses merger External Shuffle Services within the Spark compute cluster, Celeborn runs as a separate shuffle service with dedicated workers and a replicated control plane. This separation reduces resource contention between compute and shuffle workloads.
Celeborn architecture at LinkedIn (Source: LinkedIn Blog Post)
Aravind Patnam, a staff software engineer at LinkedIn, explained,
Operating it reliably across thousands of nodes and hundreds of thousands of daily applications required substantial engineering beyond the upstream project.
The deployment uses a five-node Raft-based control plane distributed across availability zones, with Apache Ratis providing metadata replication, leader election, and failover. LinkedIn also introduced network-aware replication and integrated Celeborn with its host health platform to deprioritize workers approaching maintenance and exclude degraded workers. These changes contributed to a 20-fold reduction in task failures during infrastructure disruptions compared with Magnet. [...]

## [44] Yelp Migrates Cassandra to EKS by Moving EBS Volumes
InfoQ | full text via InfoQ | ~913 words

Yelp has moved its Cassandra fleet from legacy self-managed Kubernetes clusters to Amazon EKS by re-pointing existing EBS volumes at new pods, rather than streaming data between nodes. A blog post by the site reliability team details a migration. It covered about 90 production clusters. There was zero downtime for customers and no data loss. The largest cluster, a 54-pod user-data store, took about 12 hours end to end.
Yelp had already moved its stateless workloads to EKS through its PaaSTA deployment layer, but Cassandra stayed behind. Kubernetes has no built-in way to migrate StatefulSets and their persistent volumes across clusters. The usual approach is to add nodes to the new cluster and shut down the old ones. This would temporarily double compute capacity but also lead to data transfer costs. For the largest clusters, streaming alone could have taken weeks. Yelp also considered a regional failover and rebuild, and a new Cassandra datacenter in EKS, but rated both as less transparent to customers.
Yelp's "Rolling PV Transplant" relies on the fact that an EBS volume is bound to an Availability Zone, not to a Kubernetes cluster, and that a PersistentVolume is effectively a pointer to a volume ID. The team pre-creates PVs and PVCs in EKS that reference the existing volume IDs, then creates an identical StatefulSet there, whose pods wait in ContainerCreating. The automation then deletes one pod at a time on the legacy cluster, waits for the volume to detach, and lets the EKS pod claim it. The pod rejoins the ring with the same data and token range, and the process repeats for the next pod. Cassandra's replication tolerates the few minutes each node is offline.
Yelp set a skipReconciliation: true flag on the custom resources in both clusters. This was done because two operators managed the same logical ring during the migration. The flag helped prevent them from conflicting over pod state. The flag was cleared on the EKS side at the end.
Across roughly 1,000 pods, about 1,000 TiB moved by pointer rather than over the wire. No node was ever decommissioned from the ring, so rollback was the same operation in reverse. Yelp used it a handful of times, for a missing subnet definition and a certificate mismatch, and restored pods within minutes. After a week of manual dev runs and a week of automation, one engineer ran the production rollout in about three weeks, migrating three to six clusters on a typical day.
The team had Claude generate the orchestration script, roughly 800 lines of bash, from its validated manual runbook, rather than asking it to design the procedure. The script needed minor adjustments after two days of testing.
The approach relies on a previous Container Storage Interface migration by Yelp's Compute Infrastructure team. [...]

## [42] AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account
InfoQ | full text via InfoQ | ~858 words

AWS has published a technical walkthrough of tunnel endpoints, a VPC endpoint type launched in September that lets an application in one VPC reach every address in a CIDR range shared from another account, instead of one resource at a time. The provider shares a CIDR-type resource configuration through AWS Resource Access Manager and the consumer creates a tunnel endpoint against it. From then on, anything inside the range is reachable, including resources that did not exist when the share was made.
Bruce Pinsky and Ashish Kumar of AWS frame it as a vendor-access problem, for "a vendor or service provider whose software must reach applications and resources in a customer's network." Until now, that meant a separate PrivateLink resource configuration per database or host, which breaks down when the resources are ephemeral, or the customer does not want to enumerate them. With a CIDR configuration, the customer defines a perimeter in address ranges, and "resources located outside the perimeter can't be reached by the vendor." Two further properties come with the design: the consumer and provider VPCs can use overlapping CIDR blocks, and connections "can start only from the consumer VPC, not from the provider network."
(Source: AWS Networking & Content Delivery blog)
On the r/aws thread about the September launch, the first question was what this does that VPC peering does not, from a self-described veteran of AWS's advanced networking components. The answers that followed are the use cases: a peering connection exposes the whole VPC in both directions, while a tunnel endpoint shares a subset of the address space in one direction only; one commenter at a bank wrote that "peering with unregulated partners is a massive no-no, the auditors will rip you to shreds for it." Another pointed to clusters that do client-side load balancing, such as self-managed Kafka or Aerospike, which until now needed port-based routing on a Network Load Balancer and a separate port-mapping horizon for connections arriving over an interface endpoint. The same thread drew the line against VPC Lattice itself: Lattice services work at layer 7, tunnel endpoints at layer 4 without a resource configuration per target.
The unusual part is on the consumer side: the application's traffic has to arrive at the tunnel endpoint wrapped in GENEVE, the encapsulation protocol defined in RFC 8926, over UDP port 6081 and in the same Availability Zone. The endpoint strips the header, checks that the inner destination falls inside the shared range, rewrites the source to a resource gateway address, and forwards a plain packet into the provider VPC. Linux can do the wrapping in the kernel. The walkthrough creates an ip link add ... [...]

## [183] S3 vs. ScyllaDB for tiny telemetry: What Red Canary learned the hard way
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~26 words

At Red Canary, storing large amounts of small data is a big deal. Their Linux Endpoint Detection and Response (EDR) The post S3 vs. ScyllaDB for

## [31] Quoting Daniel Stenberg
Simon Willison's Blog | full text via Simon Willison's Blog | ~157 words

18th November 2026
During the time these agents converted 185,000 lines of C code into 340,000 lines of Rust code (I counted), we merged over 300 commits in the actual curl project. We actually improved curl during these a little more than three weeks. A little over 200 bugfixes actually. 200 bugfixes that none of those rust rewrites have. We also fixed a few vulnerabilities. In another month we have done another 200 and maybe fixed a few more vulnerabilities. Will these clones keep up?
— Daniel Stenberg, Actual curl rewrites in Rust
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026

## [45] Codeberg's domain suddenly disappeared from their account, site is unreachable
Lobsters | SNIPPET ONLY (Lobsters: no readable article text (paywall, bot check, or not an article)) | ~37 words

Note: codeberg's servers are up, it's just the domain that's gone. It works perfectly after adding the following line to /etc/hosts : 217.197.84.140 codeberg.org Update: it's now up again, and the above workaround is not necessary. Comments

## [24] Upcoming Critical PHP Security Release (18 Nov 2026)
Lobsters | full text via Lobsters | ~2891 words

A popular general-purpose scripting language that is especially suited to web development. Fast, flexible and pragmatic, PHP powers everything from your blog to the most popular websites in the world.
The PHP security team announces upcoming security releases
scheduled for Thursday, 19 November 2026, between 14:00 and
14:30 UTC.
These releases are part of PHP’s regular four-week release cycle
and will address security vulnerabilities affecting all supported
PHP versions. The highest severity is CRITICAL.
The issues rated CRITICAL require either non-default configuration
or uncommon setups.
Users are strongly encouraged to prepare to upgrade promptly once
the releases become available. Technical details and fixed version
numbers will be published alongside the releases.
The PHP team is pleased to announce the fifth release candidate of PHP 8.6.0, RC7. This continues the PHP 8.6 release cycle, whose rough outline is specified in the PHP Wiki.
Source downloads of PHP 8.6.0 RC7 are available on the download page.
Please carefully test this version and report any issues found in the GitHub Issues.
Please DO NOT use this version in production, it is an early test version.
For more information on the new features and other changes, you can read the NEWS file, or the UPGRADING file for a complete list of upgrading notes. These files can also be found in the release archive.
The next release will be the first GA release, PHP 8.6.0, planned for 19 November 2026.
The PHP team is pleased to announce the fourth release candidate of PHP 8.6.0, RC5. This continues the PHP 8.6 release cycle, whose rough outline is specified in the PHP Wiki.
Source downloads of PHP 8.6.0 RC5 are available on the download page.
Please carefully test this version and report any issues found in the GitHub Issues.
Please DO NOT use this version in production, it is an early test version.
For more information on the new features and other changes, you can read the NEWS file, or the UPGRADING file for a complete list of upgrading notes. These files can also be found in the release archive.
The next release will be the first GA release, PHP 8.6.0, planned for 19 November 2026.
The PHP team announces updated Windows builds:
PHP 8.5.12-1, 8.4.27-1, 8.3.36-1 and 8.2.35-1.
These builds include Brotli 1.2.1, which fixes
CVE-2026-111497,
an out-of-bounds write vulnerability in Brotli decompression.
In PHP Windows builds, the vulnerable decoder can be reached through the
cURL extension when automatic HTTP response decompression is enabled.
This is disabled by default in cURL, but applications and HTTP client
libraries can enable it.
The -1 suffix identifies a Windows package rebuild with updated
dependencies. [...]

## [163] An AI Debt Collection Service Exposed 6.6 Million Accounts and 315,000 Call Recordings
Wired | full text via Wired | ~483 words

Two vulnerabilities in the India-based AI-driven debt collection platform CreditNirvana exposed 6.6 million accounts and about 315,000 call recordings from the company's agentic call center, according to research released on Wednesday. Owned by the Indian fintech company Perfios, the platform is built to “read a borrower’s full context, decide the next best action, and execute it autonomously, continuously, and within policy.”
The bugs were patched in CreditNirvana's systems in June and were disclosed publicly in October. But independent researcher Eaton Zveare, who found and disclosed them, notes that, while the vulnerabilities were active, they exposed personal information on millions of borrowers. Details about financial collections are inherently—perhaps obviously—sensitive, because they relate to unpaid accounts or debts and often involve extensive documentation of people's personal histories.
“They fixed it in one day, which was great, but this is really a pretty significant case,” Zveare tells WIRED. “Some of the largest fintech firms across India use this company to autonomously collect debts, so they naturally hold data, including credit scores, call recordings, transcripts, court records, and other sensitive documents. There’s just so much in there that makes it a very sensitive issue.”
CreditNirvana and Perfios did not return WIRED's requests for comment. Zveare says he worked directly with India’s Computer Emergency Response Team (CERT-In) to get the vulnerabilities fixed. CERT-In categorized one vulnerability as “high” severity and the other as “critical” severity.
The high-severity vulnerability impacted the call center data, exposing hundreds of thousands of calls as well as recommendations for next steps generated by the platform after calls were complete. It could also have been exploited to allow an attacker to manage AI agents within the platform and direct their own agentic campaigns.
The critical severity vulnerability impacted CreditNirvana's main platform, and Zveare says it specifically exposed the data of three corporate customers—all prominent Indian financial services firms—using CreditNirvana for their collections. The data also exposed millions of individuals’ accounts, which contain credit reports, ID cards, case management details, and legal documents, along with certain types of communications, including millions of emails, texts, and call transcripts related to financial services, unpaid accounts, and collections. The vulnerability also could have been exploited by an attacker to track the location of human debt collection agents and for some administrative privileges within the system. [...]

## [59] Uber and Zipline's drone delivery service takes off in Texas, with dozens of cities to follow
TLDR Tech | full text via TLDR Tech | ~513 words

Uber Eats customers in a Houston suburb can now have their food delivered by a Zipline drone, the first commercial launch under a partnership announced earlier this year between Uber and the autonomous drone delivery startup.
The commercial partnership kicks off Tuesday in Spring, Texas, before expanding to Dallas. But the companies have far larger ambitions. Uber and Zipline plan to launch drone delivery services in dozens of additional U.S. cities in their collective bid to make one million deliveries per day using the startup’s drones by the end of 2029.
Zipline’s long-range autonomous delivery drones will be used to shuttle food orders weighing up to eight pounds to Uber Eats customers, flying about 300 feet above the ground at speeds of up to 70 miles per hour. Zipline drones don’t land. Instead, the drones lower the orders, which are encased in a small protective pod, to the customer’s location using a tether.
Uber Eats customers in service areas will be able to tap a new “drone” icon on the app’s home page to view all participating restaurants. Uber said that at launch in the Houston area, several nationwide chains, including Jersey Mike’s and Zaxby’s, along with dozens of local restaurants such as Urban Bird and Abu Omar Halal, will offer drone delivery.
“In partnership with Uber Eats we’re going to create a new expectation for delivery in America,” Zipline CEO and co-founder Keller Cliffton said in a statement that underscores those aspirations.
Those nationwide goals mirror the ambitions of other drone delivery companies, including Alphabet-owned Wing and Amazon’s Prime Air service. And those plans have started to collide with concerns from residents in some locations who complain about noise and worry that the drones will disrupt wildlife and pose a risk to safety and privacy.
Companies trying to scale in this nascent industry have argued that delivery via drone is a net benefit for society, citing advantages such as traffic reduction. Customers won’t need to hop in their cars and drive to the store for that forgotten item or takeout order, instead relying on a drone, industry proponents have said.
And while Zipline and other companies have been developing their drones for years, the industry is still in its early days, as is adoption in the communities where services are available.
Zipline, which was founded in 2014, has developed a drone delivery ecosystem that includes aircraft, launch and landing systems, and logistics software. The California-based company’s initial focus was delivering blood in Rwanda, but it eventually expanded its scope to the United States. Its business in the U.S. [...]

## [53] Unlocking Stable On-Policy RL on TPU with Bitwise-Zero Train–Inference Mismatch
Google Developers Blog | full text via Google Developers Blog | ~1200 words

Reinforcement learning (RL) for large language models is notoriously sensitive to numerical instability: even tiny discrepancies between rollout generation and gradient updates can destabilize training or stall convergence. In LLM RL, the model serves as the policy, π(action | previous tokens), and true on-policy learning requires every action in an update to be generated and evaluated by that exact same policy. While a synchronous loop ensures each rollout batch is scored using the same weights that generated it, a critical numerical requirement remains: the sampler and trainer must evaluate that policy identically.
In practice, production RL stacks run sampling and training through separate, specialized execution paths. The sampler chooses each action token during incremental decoding and records its behavior logprob. The trainer evaluates the same token in batched forward-backward passes to compute its current logprob and gradients. Under the same weights, these differing execution paths can still assign different logprobs to the same token and context. The training schedule is on-policy, but the numerical execution has introduced a hidden off-policy gap that compounds over multi-turn trajectories.
Our zero train–inference mismatch (Zero-TIM) implementation, developed in Tunix and verified at multi-host scale across 64 TPU v5p chips (DP8×TP8), closes this numerical gap. At the same weights, the sampler and trainer assign bitwise-identical logprobs to the same action and token history—bringing state-of-the-art, true on-policy stability to TPU RL training.
A reduction is a tree of floating-point additions. Floating-point addition is not associative, so changing the tree changes where rounding occurs. The effect is easier to expose in bfloat16, which retains less precision than float32.
The following bfloat16 example isolates the effect of reduction order:
The same issue appears in model reductions: matrix products accumulate partial sums, normalization computes statistics, and tensor-parallel shards combine partial outputs. In our original stack, sampler decode and trainer forward used different token-array shapes and forward implementations. JAX specializes computations to their input shapes, and the training forward also runs inside a differentiated program.
Across these paths, reduction order and intermediate precision were not consistently aligned. Floating-point rounding turned those arithmetic differences into different logprob bits. The weights and model equations were identical; the arithmetic was not. [...]

## [198] RBRD: RAM-Backed Linux Block Driver Written In Rust For Better Safety But Slower Performance
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~19 words

Linux kernel patches were posted tonight for introducing RBRD, the RAM-backed block driver written in the Rust programming language...

## [102] Qwik 2.0 RC: Replaces HTML Comment Markers for Faster Reactivity and Out-of-Order Streaming
InfoQ | full text via InfoQ | ~543 words

Qwik, the resumable JavaScript framework originally created at Builder.io, has released its 2.0 Release Candidate, targeting a rewrite of how the framework encodes resumable state in server-rendered HTML and introducing experimental out-of-order streaming. The RC was published on 1st October 2026 as @qwik.dev/core@2.0.0-rc.0, around two years and eight months after the initial Towards Qwik 2.0 design article.
In v1, Qwik propagated state updates by sprinkling HTML comment markers such as <!--qv--> and <!--t=8--> throughout the rendered body to flag component boundaries and the text nodes a signal should update. That approach forced a single ordered write pass, added CPU and memory overhead, and made out-of-order streaming impossible because a slow fetch blocked everything after it. In v2 the comments are gone, with state and virtual node information instead compressed into two <script type="qwik/state"> and <script type="qwik/vnode"> blocks at the end of the document.
On Qwik's internal runs of js-framework-benchmark, v2 posts a weighted geometric mean of 1.23 times slower than vanilla JavaScript, ahead of Vue 3.5 at 1.25x, Angular 22 at 1.42x, React 19 with the compiler at 1.53x, and v1 itself at 2.59x. A detailed classmethod walkthrough that built the same starter against both versions reported server-rendered HTML went from 60 comments to zero, with JavaScript required before interactivity dropping from 59KB to 9KB, though total bundle size grew.
Out-of-order HTML streaming has also been added in experimental mode. Developers can wrap slow regions in <Pending> and <Catch> boundaries so the server sends the rest of the page immediately and streams the real content later in the same response, with a small inline script swapping it into place. The APIs are opt-in through vite.config.ts:
qwikVite({ experimental: ['pendingBoundary', 'catchBoundary', 'blockSSR'] })
useComputed$ now accepts async functions, replacing <Resource>, and route loaders gain their own JSON endpoints with cacheControl and eTag options so the browser can cache them individually and <Link> can prefetch data on hover. Other additions include a worker$ primitive for Web Workers, reactify$ for embedding Qwik components inside React trees, server-only *.server.ts files, and HMR that preserves signal and store values across edits.
In a Reddit discussion predating the v2 RC, one developer called the lack of out-of-order streaming a significant limitation and argued that the Qwik team should be more upfront about it. Another commenter suggested that streaming could be a future feature. [...]

## [11] AI agents ask better questions than KPMG accountants in audit trial
Hacker News | full text via Hacker News | ~746 words

LONDON, November 18, 2026 — Artificial intelligence has taken another significant step into the world of professional services after KPMG revealed that AI agents examining the accounts of a major UK-listed company sometimes investigated financial issues more deeply and asked better questions than its human audit team.
The experiment, conducted by KPMG UK using more than 100 AI agents, marks an important development in the application of artificial intelligence to one of the most labour-intensive areas of the financial services industry. It also raises an uncomfortable question for the accountancy profession: if machines can increasingly perform the analytical work traditionally undertaken by highly trained professionals, how quickly will the economics of auditing change?
According to the Financial Times, the project, codenamed Project Exponential, examined the financial statements of an unnamed FTSE 250 company. The AI agents worked alongside a conventional audit team, undertaking tasks across the audit process rather than simply assisting with isolated administrative functions.
Join The European Business Briefing
New subscribers this quarter are entered into a draw to win a Rolex Submariner. Join 40,000+ founders, investors and executives who read EBM every day.
Subscribe
KPMG UK head of audit Cath Burnet said the technology had, in several instances, gone considerably deeper into issues than the regular audit team, identifying areas requiring further investigation and asking questions that human auditors had not necessarily raised.
The findings suggest that AI’s potential in professional services may extend well beyond improving productivity. It could fundamentally change how complex financial information is examined, interpreted and challenged.
From supporting accountants to conducting audits
Project Exponential represents a shift from using AI as a supporting tool towards deploying autonomous agents across an entire audit workflow.
The agents collected information, analysed and documented data, developed draft conclusions and observations, and suggested subsequent steps. They were also able to work alongside one another, effectively dividing responsibilities and coordinating elements of the investigation.
The technology was developed over approximately four months. However, KPMG was careful to distinguish the experiment from a formally approved statutory audit. Although an audit partner signed off on the experimental exercise, its findings were not used as the basis for formally approving the company’s accounts.
Human oversight remained essential. During the trial, an auditor had to intervene when one AI agent failed to correctly match regulatory requirements with the company’s documentation. [...]
