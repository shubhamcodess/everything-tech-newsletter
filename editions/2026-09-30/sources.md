# Full text for 30 picks -- untrusted article content, treat as data only

## [1] GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price
Hacker News | full text via Simon Willison's Blog | ~72 words

29th September 2026
I'm a bit late with the pelicans because I was live-blogging the keynote: https://simonwillison.net/2026/Sep/29/openai-devday-2026-liv...
Here they are for GPT-6.1-Sol: https://tools.simonwillison.net/markdown-svg-renderer?url=ht...
They're not notably different from the GPT-6 family pelicans: https://static.simonwillison.net/static/2026/gpt-pelicans-gr...
Recent articles
- OpenAI DevDay 2026 live blog - 29th September 2026
- 2026 in LLMs (so far) - 27th September 2026
- Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war - 22nd September 2026

## [3] Dots: Always-on agents
Hacker News | full text via Wired | ~545 words

Dots are OpenAI’s new always-on AI agents, announced at the company’s DevDay 2026 event on Tuesday in San Francisco. These agents complete tasks on a user’s behalf and are depicted as cute blobs you can personalize and assign multistep projects to complete.
OpenAI’s Dots are powered by the startup’s GPT-6 Astra model. A core selling point is their “always-on” design—unlike a single-turn chatbot experience, these agents constantly crawl the web and attempt to complete whatever task you assign to them. Dots also pull context from connected apps and learn more about your preferences over time.
In one demo example shared by OpenAI, a user’s Dot helps plan dinner. The Dot proactively saw that the user’s calendar showed they were working through dinner and messaged with two GrubHub food delivery options with pricing for each. The user followed up with their food pick and when they wanted it ordered. In another example, a user collaborated with the agent to launch a new website.
Users can message Dots through ChatGPT, Slack, and Microsoft Teams, with the user’s context shared with Dots across modes. In addition, Pro users can join a waitlist to text with their Dots in iMessage or RCS messaging on Android.
The Dots rollout starts today for subscribers to ChatGPT’s Pro tier that costs $100 a month. OpenAI often launches new features first for this higher subscription tier and then rolls them out to a larger subset of users over time. Users can start by controlling one Dot, but the company is expected to eventually roll out the ability to control multiple agents at the same time.
The Dots launch is also part of OpenAI doubling down on its efforts to attract more enterprise clients. On stage at DevDay, CEO Sam Altman announced “specialist Dots” for enterprise customers tuned for specific tasks, like accounting, email marketing, and legal analysis. It adds to the trend of AI agent coworkers being integrated into more professional workflows.
Dots are designed to get explicit approval before taking more sensitive actions on a user's behalf, like installing software or changing a password. Users can enable a Custom Rules tool to set explicit boundaries that they don't want agents to cross, as well as tasks that need more direct permission to complete.
As users connect their data and use agents, it's worth keeping potential security and privacy risks top of mind. [...]

## [17] OpenAI Scraps Release of New AI Model Over Safety Concerns
TLDR Tech | full text via Wired | ~652 words

OpenAI has cancelled plans to release its latest GPT-6.1 Astra system next month after the model failed to meet safety standards.
Research and safety leaders decided not to ship the model after finding it was worse at sticking to human users’ values and goals than previous systems, OpenAI told WIRED. “It didn’t quite meet the bar in terms of staying within scope and authorization, and how it communicates back to the user about the type of work it’s done,” head of safety systems Saachi Jain said. The company said it has other new models coming soon which do meet its safety standards and plans to release other Astra models in future.
OpenAI also apologised on Monday for its handling of the hacking of an Australian government website by an unreleased model during internal testing. The agent accessed non-public data, ran commands, and wrote files onto the server. The government had criticized OpenAI for taking “way too long” to alert them of this and for only doing so through an email to a public inbox. It confirmed chief strategy officer Jason Kwon will face questions from the Australian parliament in Sydney next week as the government investigates whether to take legal action.
OpenAI has already paused training its most powerful artificial intelligence models after realizing its models’ activities on the web during training and evaluation had become misaligned with how a human would ideally behave. OpenAI said over the weekend it was notifying “dozens” of third parties, including governments, who might have been impacted by other security breaches or spam.
It will only resume training when it has developed safeguards and alignment improvements, the company said. These safeguards should include: training the models to act reliably as intended, making sandboxing and security strong enough to contain models, and live-monitoring models to catch any concerning behaviour, OpenAI proposed in a blog post on Monday.
“We’re now at the threshold where they’re not sure they can test or release these models reliably,” Calum Chace, cofounder of AI safety startup Conscium told WIRED.
OpenAI has been hardening its research environment since a swarm of its agents escaped it over the Summer to hack Hugging Face. “This is not the first time we have hit pause to take such measures, nor do we expect it will be the last as AI capabilities continue to advance,” a spokesperson told WIRED about the training slowdown on Monday. [...]

## [45] Here's what actually happened in OpenAI's Australian gov't server hack
Ars Technica | full text via Ars Technica | ~273 words

Last week, when Australian Prime Minister Anthony Albanese told the world that an OpenAI agent had accessed “non-public files” from his country’s Medicare statistics portal during testing, his description of the incident was a little light on details. Today, we’re getting new information on just how far OpenAI’s overzealous agent went in attempting to satisfy a rather innocuous-sounding informational prompt.
In a newly published blog post, OpenAI says the June incident started when the company asked “an experimental, internal-only OpenAI model” to research government spending statistics in the Australian state of Victoria. When the model ran into trouble finding that data using the publicly published statistics that it was supposed to reference, “it took actions that we had not authorized it to take” to find an answer, OpenAI said.
Those unauthorized actions included finding “a way to gain non-public access to the service” and using that access to view “technical system information and source code” alongside credentials and the aggregate statistics it was actually searching for, OpenAI said.
In a newly published disclosure email that was sent to Australia’s Public Disclosure account earlier this month, OpenAI said its model had “identified a way to make the server carry out instructions sent through the public reporting interface, without a private account or password.” That unauthorized access let the agent “read portions of internal program files and settings, obtain a list of files, and create and read back a small test file on the server,” according to the email.
“Our review found no evidence that the model accessed patient-level records, personal information or credentials; deleted data; or established ongoing access,” OpenAI continued in the email.

## [78] GPT-6 Astra performs unsanctioned supply-chain attacks in simulations
TLDR AI | full text via TLDR AI | ~1679 words

Read the accompanying testing report here.
In recent incidents, AI systems performed unsanctioned cyber activity despite being prompted only to complete a cybersecurity evaluation [1,2,3,4]. This includes AI systems engaging in supply-chain attacks on real, out-of-bounds targets.
Before its public release, AISI tested whether GPT-6 Astra would engage in this type of unsanctioned cyber activity when prompted to complete a cyber evaluation. To securely perform this testing, we used Petri, a tool that uses LLMs to fully simulate the cyber evaluation scenarios: in all evaluations discussed here, all actions were simulated, so no real-world actions were performed, and no real-world harm was caused. We also ran this testing with GPT-6 Astra's cyber classifiers turned off: since these are designed to block unsanctioned activity, disabling them allows us to measure what the model attempts with no interventions.
In our simulations, we found that GPT-6 Astra conducted a range of unsanctioned attack activities, and did so at a higher rate than GPT-5.6 Sol and GPT-5.5. Attack activities included GPT-6 Astra creating fake identities which it used to deceive developers, posting comments from fake accounts arguing against the results of accurate security reviews, and delivering malicious payloads to open-source codebases.
When we updated the instructions for the simulated cyber evaluation to explicitly clarify that only listed, local parts of the environment were in scope, we still observed GPT-6 Astra occasionally conduct full supply-chain attacks on simulated internet targets.
The main potential limitation to these results is simulation awareness: the possibility that GPT-6 Astra may behave differently after identifying features of the environment as simulated. However, our analysis of the transcripts – in combination with observations from previous incidents – suggests that it is possible the model could attempt this unsanctioned behaviour in real-world conditions.
Alongside our full testing report, this blog outlines our key results and their implications. AISI additionally tested the monitorability of GPT-6 Astra – you can read those results in the model’s system card. We continue to harden our testing security, including our sandboxing, and will soon be running our full suite of cyber evaluations.
Key Results
GPT-6 Astra conducted unsanctioned supply-chain attacks in our simulated evaluation, and did so more frequently than GPT-5.6 Sol and GPT-5.5 (Figure 1). [...]

## [76] Anthropic's IPO prospectus shows sweeping AI vision, surging costs
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~85 words

Anthropic is betting that AI will transform the global economy more profoundly than industrialization, electricity, and the internet. The company is targeting a $2 trillion valuation. It reported a net loss of $42 billion in 2025, and it plans to spend $518 billion on cloud, computing, and infrastructure obligations in the coming year. Anthropic says nearly a quarter of its revenue last year came from two customers, and many of its largest clients are not locked into long-term contracts and could cut or stop spending.

## [13] AMD acquires World Labs AI startup, upping the ante against Nvidia
Ars Technica | full text via Ars Technica | ~238 words

Chipmaker AMD and world models company World Labs announced that AMD will acquire the AI company by the end of the year, pending regulatory approval. The transaction is valued at $8.2 billion.
In 2024, computer vision scientist Fei-Fei Li founded World Labs with fellow researchers Justin Johnson, Christoph Lassner, and Ben Mildenhall, with $230 million in funding, some of which came from AMD.
The company began working on new world models, which are AI models that aim to provide a useful, predictive simulation of the physical world. Competing architectures exist (earlier this year, Ars interviewed World Labs co-founder Ben Mildenhall and others in the field about exactly that), but many involve training a model on vast amounts of video data.
That was the case for Marble, World Labs’ first publicly usable tool. Marble can generate small 3D spaces using Gaussian splats. They can then be exported as 3D assets for use in film production, game development, and other applications. The company has since introduced additional models and tools with different emphasis or use cases, such as Atlas.
One use case that has justified enormous investment in the space is generating synthetic data for training robots. That’s a field where Nvidia, AMD’s direct competitor, has a strong lead. AMD has produced its own AI models before, including Micro-World, an open-source world model, but it has not produced a stack that competes with Nvidia’s Cosmos and related models and applications.

## [19] Meta launches enterprise AI platform, hires MongoDB CEO to lead new initiative
TLDR Tech | full text via TLDR Tech | ~242 words

Meta announced Monday that it’s launching “Meta Enterprise Platform,” a new initiative aimed at expanding the company’s AI offerings to businesses and corporate customers. The social media giant hired Chirantan “CJ” Desai, the CEO of database software giant MongoDB, to lead the new initiative.
The launch of the new business builds on the momentum of Muse, Meta’s personal AI assistant launched earlier this month that can perform tasks for users such as sending emails and booking travel.
Meta says it will focus on bringing its full technology stack, including Muse, Meta Business Agent, Muse API, Muse Code, and more to businesses and developers.
“Over the coming years, AI will fundamentally redefine how organizations of all sizes innovate, grow, serve customers, and run business operations,” Desai said in a statement. “Meta has a unique role to play because it is bringing together advanced models and leading agents with a proven track record of helping millions of advertisers and hundreds of millions of businesses scale. Meta Enterprise Platform will focus on turning its AI stack into products and services that companies can deploy for their own businesses.”
The move could help Meta see a return on all the money it’s pouring into AI.
MongoDB’s shares dropped by more than 17% on the news of its CEO’s sudden departure. The database maker said it appointed Dev Ittycheria as interim chief executive, who previously served in the role, while the board searches for Desai’s permanent replacement.

## [59] DevDay 2026 Recap
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~21 words

Explore more than 20 announcements from OpenAI DevDay 2026, including GPT-6 Astra, ChatGPT, Codex, APIs, security, and new tools for builders.

## [70] Anthropic has launched Claude Sonnet 5.5
TLDR Tech | full text via TLDR Tech | ~847 words

September 28, 2026
Anthropic has launched Claude Sonnet 5.5: it scores 56 on the Artificial Analysis Intelligence Index, just 2 points behind Opus 5.5 (max), but at the highest Output Tokens per Task we've seen
See model page
With max effort, Sonnet 5.5 gains 18 points over Sonnet 5 and moves to #2 on the Intelligence Index, behind only Opus 5.5 (max). Anthropic has priced Sonnet 5.5 identically to Sonnet 5 at $0.2/$2/$10 per 1M cache input/input/output tokens. However, it outputs a higher number of Output Tokens per Task and costs $7.60 per task (~50% higher than Sonnet 5's Cost per Task).
Key takeaways:
➤ Meets leading models on agentic terminal use and knowledge work: In Terminal-Bench 4.0, Claude Sonnet 5.5 reaches 64% against 60% for Opus 5.5 and GPT-6 Astra. On AA-Briefcase (1811 vs 1822 Elo), GDPval-AA (1844 vs 1846 Elo), and AutomationBench-AA (71% vs 70% headline score), Sonnet 5.5 reaches parity with Opus 5.5, albeit with significantly higher token usage to achieve it
➤ Heaviest token use we have measured: At max effort, where it reaches performance nearing that of Opus 5.5, Claude Sonnet 5.5 used ~193k Output Tokens per Intelligence Index Task. This is the highest token use we have measured, around 60% higher than Opus 5.5 (max) or Sonnet 5 (max) and ~7x GPT-6 Astra (max)
➤ Pricing remains at $2/$10 per million tokens of input/output, matching GPT-6 Sol: At this pricing Claude Sonnet 5.5 sits off the Intelligence vs. Cost per Task Pareto Frontier. At high effort levels it sits behind Opus 5.5, while lower efforts have GPT-6 Astra or Sol configurations delivering equivalent performance for lower cost. The high effort setting is the most competitive on this basis, sitting very narrowly behind GPT-6 Sol on Intelligence at effectively the same Cost per Task
➤ Behind Opus 5.5 on factual knowledge and scientific reasoning: As a smaller class model, Sonnet 5.5 still lags on factual knowledge in AA-Omniscience compared to Opus 5.5. It scores 54% against 66% for factual accuracy, though with a lower hallucination rate (47% against 59%). It also sits ~6 points lower on Humanity's Last Exam and SciCode compared to Opus
These evaluations were conducted on a pre-release deployment of Claude Sonnet 5.5, which Anthropic found to have a bug that can degrade responses to requests that use structured outputs. [...]

## [75] NVIDIA Launched Open Agent Safety Platform
TLDR AI | full text via TLDR AI | ~1341 words

News Summary:
- NVIDIA Open Agent Safety Platform consists of NVIDIA OpenShell open source software and the NVIDIA Sentry reference system design that enables full-stack governance and control across software and the hardware, compute and robotics systems that run agents.
- OpenShell software provides a secure runtime boundary that traces all actions and enforces policy as agents run on NVIDIA Vera CPUs. As open source software, OpenShell can be extended to work with third-party compute platforms, including those from Arm and Intel.
- Sentry adds an out-of-band watchdog that runs on NVIDIA BlueField-4 DPUs to continuously monitor agent behavior. Sentry can quarantine agents that attempt to move outside their boundaries in milliseconds.
- Industry leaders from across the AI ecosystem are joining NVIDIA to strengthen AI safety for every industry across the full stack of infrastructure, software, models and robotics — including Anthropic, Cisco, CrowdStrike, Dell Technologies, Figure, HPE, Hugging Face, JPMorganChase, Microsoft, Palantir, Palo Alto Networks, Perplexity, Red Hat, Salesforce, SAP, Scale AI, ServiceNow and SpaceXAI.
NVIDIA today announced NVIDIA Open Agent Safety Platform, an open software platform and reference system design to strengthen AI security from agent testing to deployment, with full-stack governance and control across software and the hardware, compute and robotics systems that run agents.
Recent security incidents have underscored the need to equip organizations with open, customizable tools that enforce more control over long-running agents. Across these incidents, the pattern is the same — the agent circumvented security controls at the application layer to complete its assigned task.
“AI’s extraordinary potential for society will only be realized if we solve AI safety,” said Jensen Huang, founder and CEO of NVIDIA. “As we continue to discover the frontier of AI capabilities, we must accelerate discovery at the frontier of AI safety. Safety and security require full-stack engineering. NVIDIA Open Agent Safety Platform brings together industry, researchers and public-sector organizations to share best practices, align on evaluation methods and foster international cooperation. [...]

## [85] How we found 24 Android vulnerabilities using our open source AI security agent
GitHub Blog | full text via GitHub Blog | ~2313 words

With the rise of AI in the security space, our team created the GitHub Security Lab Taskflow Agent as a way for security researchers to easily automate, package, and share the AI prompts and workflows that they find effective for their work. In this blog post, I’ll share how I created auditing taskflows to find vulnerabilities in Android applications.
While new models are getting better at understanding code, custom taskflow prompts let security researchers guide them—splitting research into incremental steps to help the LLM find complex vulnerabilities faster, or that it would have missed entirely.
Using these taskflows, I’ve reported more than 20 vulnerabilities in Android applications. You can check out our advisories page to see when new vulnerabilities are disclosed. Otherwise, keep reading for a few concrete examples of high-impact vulnerabilities that these taskflows found.
How to run the taskflows on your own project
Want to get started right away? The taskflows are open source and easy to run yourself. Please note: A GitHub Copilot license is required, and the prompts will use premium model requests. Running the taskflows can result in many tool calls, which can easily consume a large amount of tokens.
- Go to the seclab-taskflows repository and start a codespace.
- Wait a few minutes for the codespace to initialize.
- In the terminal, run ./scripts/audit/run_mobile.sh myorg/myrepo
It might take an hour or two to finish on a medium-sized repository. When it finishes, it’ll open an SQLite viewer with the results. Open the “audit_results” table and look for rows with a checkmark in the “has_vulnerability” column.
Creating targeted audit taskflows for Android apps
My colleagues Peter and Mo previously wrote a blog post about their audit task flows. Although those taskflows already work well on their own, Android applications have their own specific classes of vulnerabilities that we’d like the taskflows to focus on, so we need to guide them.
First, I added a taskflow called gather_mobile_entry_point_info.yaml. Entry points are places in the code that attacker-controlled data could flow through. This taskflow takes the entry points and separates them into mobile entry points and non-mobile entry points. This allows the AI to run on repos that contain a variety of different application types—a mobile application, web servers, desktop applicationswhile still understanding the correct attack surface.
Second, I edited classify_application_local.yaml. [...]

## [138] OpenAI’s latest features take direct aim at the app store model
TechCrunch | full text via TechCrunch | ~1043 words

The focus of OpenAI’s Dev Day on Tuesday may have been on its agentic assistants known as Dots, or its new AI models, but combined, the AI company’s announcements pointed towards a bigger plan: a disruption of the traditional app store model. Taken together, today’s announcements turn ChatGPT itself into the place where software can be discovered, launched, and used by people and agents alike.
In addition, OpenAI introduced a way for people to bring their ChatGPT identity with them, while also allowing them to use their existing AI allowance in third-party apps.
This isn’t the first time OpenAI has experimented with how apps could operate within its familiar chatbot interface, but the current vision feels more fleshed out than before.
For starters, the company is turning ChatGPT itself into a surface for launching apps. The chatbot, which the company says now has 1.2 billion weekly users, has yet to fully capitalize on its potential as a discovery mechanism for finding and using apps that work with AI.
To change that, ChatGPT will begin to make app suggestions within the flow of conversation when it recognizes that a particular app could help the user complete their task. From there, the user will be able to connect the app and begin using it directly within ChatGPT.
This is also aided by the expansion of ChatGPT’s plugin architecture, which now supports extensions.
This allows app developers to build interactive panels where users can work with their tools while they’re chatting with ChatGPT. This essentially turns the apps and services that users would have previously used via the web or through a native desktop or mobile app into something that’s operated directly within ChatGPT.
Developers that sign on with the system can build AI-native versions of their apps through ChatGPT, the same way they would through the open web or a mobile app store. As more and more discovery happens through AI chat, it’s a distribution channel that’s hard to pass up.
Users get an incentive to use that channel too, because “Sign in with ChatGPT” will let them bring their AI allowance with them. (OpenAI has 16 launch partners on this effort, including Cognition’s Devin, Notion, Vercel, T3, OpenClaw, and Dactyl, but plans to add more soon, it says.)
In a demo at OpenAI’s Dev Day event, the company showed off how its own new meeting app could work inside ChatGPT, showing upcoming meetings from the user’s calendar. [...]

## [139] OpenAI reportedly in talks to raise $30B round at $1.4T valuation
TechCrunch | full text via TechCrunch | ~208 words

OpenAI is in talks with investors to raise at least $30 billion in a pre-IPO funding round at a valuation of roughly $1.4 trillion, Bloomberg reported on Tuesday.
Investors are eager to pour more funds into the ChatGPT maker ahead of its anticipated public market debut next year. While Anthropic momentarily outpaced OpenAI at the start of the year, recent strategic refocus on key areas like coding has fueled a 70% jump in run-rate revenue since July, reaching $40 billion in August, according to the report.
The company previously raised $122 billion in March at an $852 billion valuation. That funding round was supposed to be its last private raise before an IPO, which had been, until recently, expected to take place this year. However, CEO Sam Altman has now ruled out a public debut in 2026 to prioritize AI safety first.
“I think it is unacceptable to be taking like a 10% chance of killing everybody by the end of the decade,” he recently told Fortune, in response to warnings from safety researchers about AI posing an existential risk to humanity.
The new fundraising, if it transpires, will serve as a bridge round to the IPO, according to Bloomberg.
OpenAI didn’t respond to TechCrunch’s request for comment.

## [87] How we will do better for Australia
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~19 words

OpenAI apologises for incidents involving Australian government websites and outlines stronger safeguards and support to strengthen Australia’s cyber defences.

## [28] Amazon CloudWatch Omni Extends CloudWatch into the Agent Era
InfoQ | full text via InfoQ | ~428 words

Recently launched, Amazon CloudWatch Omni is an AI-first observability platform designed to monitor, evaluate, and troubleshoot applications and autonomous AI agents in a unified environment.
For traditional applications, metrics such as latency, errors, CPU and availability are often sufficient to identify operational problems, says AWS senior specialist solutions architect Daniel Abib. For AI agents, an execution can succeed technically while still producing the wrong result, using the wrong tool, retrieving poor information, or taking an unnecessarily expensive path:
Agent behavior is non-deterministic: a prompt change can degrade response quality even when standard metrics show no errors. Teams spend hours manually reviewing logs across multiple systems, unable to pinpoint what changed or why.
To address this challenge, Omni captures end-to-end traces, evaluates correctness, coherence, retrieval, and tool selection, and lets you compare prompts, build test datasets from production traffic, run experiments, and detect regressions.
It supports several agent frameworks, including LangChain, LangGraph, CrewAI, OpenAI SDK, Strands, and Vercel AI SDK. It also uses open standards such as OpenInference and AWS Distro for OpenTelemetry (ADOT) and integrates with Amazon Bedrock AgentCore. For evaluations, CloudWatch Omni also supports third-party evaluators such as Braintrust, DeepEval, and Ragas.
Amazon CloudWatch Omni provide unified observability, bringing traditional microservices, cloud infrastructure, and generative AI/agentic workloads under the same umbrella for a unified view. It offers native OpenTelemetry support, allowing existing telemetry to feed into Omni without complex reconfigurations, as well as dual workspaces, which provide a standalone web experience for operators via single sign-on (SSO) outside the traditional AWS Management Console, alongside a free, local, developer-friendly IDE extension supporting both VS Code and Kiro.
CloudWatch Omni also support AI-powered investigations, allowing users to query logs, metrics, and traces using natural language to identify topology issues and pinpoint root causes.
AWS vice president Chet Kapoor summarizes the new tool on LinkedIn saying that it "helps you catch issues proactively, trace them to their root cause, and identify improvements across your agents, applications and infrastructure in one place". [...]

## [81] Automating eval design and hill-climbing with Claude
TLDR AI | full text via TLDR AI | ~1696 words

Principles for designing evals and hillclimbing against them without fooling yourself, and how the claude-api skill's build-eval and hillclimb commands put them to work.
Evaluations provide a signal on how your app or skill is performing on specific tasks. But designing evaluations, and improving performance on them without fooling yourself, is hard. We've added guidance for both to the claude-api skill.
With the skill, you can run /claude-api build-eval to build an evaluation inside your codebase, and run /claude-api hillclimb to improve your application against it, one change at a time, with a held-out set of examples to catch overfitting.
In this article, we highlight the principles of good eval design and hillclimbing first, then show how Claude Code with the claude-api skill applies those principles. We’ll close by showing a few examples of these commands.
Well designed evaluations have a few common elements (Figure 1):
Model capability is jagged. If you pick cases because today's model fails them, you are sampling the valleys of one model's capability surface (Figure 2). The evaluation can end up measuring that model's failure fingerprint rather than what is intrinsically hard or valuable for your application to do.
Pick hard cases because a human judged them hard: a useful test is to be able to say why a task is hard before you include it. Include cases that are specific failures in your application derived from production traffic, bug reports, or tickets. However, don’t blindly trust user traffic: users sometimes try what they expect to work, so a task distribution drawn strictly from user traffic may skew easy.
The build-eval command in the claude-api skill turns these principles into a guided workflow. When you run /claude-api build-eval in Claude Code, Claude interviews you, builds the eval inside your codebase, and pauses for approval at specific points.
Claude helps you sample inputs to build evaluations in this order:
The skill prioritizes production traffic, but it can also generate synthetic data anchored in a few real examples that you provide. The skill instructs Claude to generate a simple page that shows you every input and waits until you confirm them. As an illustration, below we show an example set of inputs for an e-mail router application that the skill may ask the user to review (Figure 3). [...]

## [89] When can we say AI made a scientific discovery?
MIT Technology Review | full text via MIT Technology Review | ~921 words

When can we say AI made a scientific discovery?
AI companies’ insistence that their technology is making breakthroughs, not just aiding scientists, is making real progress harder to recognize.
This story originally appeared in The Algorithm, our weekly newsletter on AI. To get stories like this in your inbox first, sign up here.
Last Wednesday, Anthropic announced that earlier this year it had launched a molecular biology lab, where Claude agents read and conjecture about hard biology problems and human scientists run experiments on what they report. And this AI-powered lab, the company said, had made its first discovery.
To understand what Anthropic says its system did, imagine you’re flipping through a library of millions of DNA sequences, amassed as scientists sequence more and more of the living world. One step toward a breakthrough might be finding a peculiar sequence that encodes an interesting enzyme, perhaps. Then you’d need to figure out what that enzyme does and, eventually, how to manipulate it to do something useful.
What Anthropic says its system of 950 agents found after 21 hours was not a brand-new sequence. The agents instead flagged a repeating pattern surrounding a known enzyme, a particular pattern Anthropic said hadn’t been catalogued before. But if you read through Anthropic’s announcement, which calls this pattern “reminiscent” of what led to the gene-editing technology CRISPR that “has already transformed science and medicine,” it sounds as if this army of agents really found something of note.
These claims have angered some biologists. A viral post from one, subsequently endorsed by the chair and CEO of the drugmaker Eli Lilly, said that “finding a weird cluster of genes and repeats is often the easy part. The hard part, and where the real discoveries come from, is figuring out what the system actually does.” The agents helped with some laboratory grunt work, in other words. But a discovery it is not.
It’s a reminder that even if AI does something impressive—like finding a pattern in a mass of biological data that would be difficult to perceive with human eyes alone—the result itself may not constitute a breakthrough for science. What is novel for AI may be routine, unsurprising, or simply not that consequential to a biologist. [...]

## [186] Mesa 26.3 Enables Intel's New Jay Shader Compiler By Default, Compile Times 55% Faster Or 66% Faster Than Windows
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~58 words

Over the past year Jay has been in development as a new open-source shader compiler for Intel GPUs. Alyssa Rosenzweig has been leading its development since joining Intel in 2025. For Mesa 26.3 the Jay shader compiler is being enabled by default for modern Intel graphics hardware and is around ~10% faster than the existing BRW compiler code...

## [179] How to Build a Reliable AI Assistant with the Claude API
freeCodeCamp News | full text via freeCodeCamp News | ~1955 words

Large language models can answer questions, summarise documents, write code, and interact with external systems. But building a reliable AI application requires more than sending a prompt and displaying the response.
A production-ready application must manage conversation history, provide relevant context, use tools safely, handle different response types, and evaluate whether the generated output is useful.
In this tutorial, we’ll build ShopHelper, a customer-support assistant for an imaginary online shop. By the end, ShopHelper will be able to:
- Answer general questions in a consistent tone
- Remember what a customer said earlier
- Look up order statuses by calling a function in your code
- Handle Claude’s multi-block responses safely
- Process support tickets using workflows
- Evaluate whether prompt changes improve results
Each section adds one piece, so you can follow along in your own editor.
Table of Contents
Prerequisites
You should have:
- Basic Python knowledge
- Python 3.9 or later
- An Anthropic API key
- Familiarity with functions and JSON
How to Set Up the Project and Keep Your API Key Secure
Create a virtual environment and install the Anthropic Python SDK:
python -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
On Windows:
.venv\Scripts\activate
Create a .env file:
ANTHROPIC_API_KEY=your_api_key_here
An API key is a secret credential. Never place it in browser JavaScript, mobile-app code, or client-side configuration. Never commit it to a repository:
echo ".env" >> .gitignore
If you add a web interface later, keep the key on your backend:
Browser → Your backend → Claude API
Create app.py:
import os
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
MODEL = "claude-sonnet-5"
client = Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)
load_dotenv() loads the value from .env. The MODEL constant means you only need to change the model name in one place. Confirm that the model identifier is available to your account before running the example. [...]

## [95] Who’s liable when AI agents go rogue?
MIT Technology Review | full text via MIT Technology Review | ~2049 words

Who’s liable when AI agents go rogue?
Recent hacks have shown that the law is lagging when it comes to holding companies accountable.
MIT Technology Review Explains: Let our writers untangle the complex, messy world of technology to help you understand what’s coming next. You can read more from the series here.
Over the past few months, a cascade of cyberattacks by AI agents has stunned the world. In July, OpenAI disclosed that a swarm of its agents had escaped their sandbox and hacked into the AI platform Hugging Face to cheat on a cybersecurity test. Recently, external researchers discovered that OpenAI agents had hijacked a German wiki site and the coding platform RubyGems in May to share test answers.
Earlier this month, Anthropic disclosed four incidents in which its model Claude hacked into third-party systems during cybersecurity exercises. Just last week, Google confirmed that its model Gemini had been caught hacking other companies too.
The researcher who uncovered the OpenAI website hijack has warned it’s likely that similar undiscovered episodes are out there. And many say it’s only a matter of time until there’s another, possibly more damaging incident where AI agents bypass sandboxes to access systems they shouldn’t.
So the big question is: How do we hold companies liable when they lose control of their AI agents?
Reporting
OpenAI didn’t disclose the German wiki incident or the RubyGems incident until a group of external researchers uncovered them, and it still has not disclosed some crucial details about the Hugging Face hack. That limits our understanding of what exactly went wrong and how to prevent it from happening again.
But you might be surprised to learn that OpenAI likely wasn’t legally required to disclose these incidents. (OpenAI did not respond to a request for comment.)
State AI transparency laws like California’s SB 53, New York’s RAISE Act, and Illinois’s SB 315 require that AI developers report “critical safety incidents.” These are defined as incidents that cause more than 50 deaths or physical injuries or $1 billion in damage. They also include incidents where the model deceives developers outside an evaluation in a way that materially increases catastrophic risks. Many cybersecurity incidents that don’t meet the threshold for physical damage or catastrophic risks could nonetheless be dangerous precursors to such catastrophes, and the existing laws don’t account for that. [...]

## [152] AI researchers put out videos saying superintelligence is ‘exactly as dangerous as it sounds’
The Verge | full text via The Verge | ~345 words

“The chance of human extinction is about a coin flip, in my view,” Geoffrey Irving, a former OpenAI and Google DeepMind employee, said in a new interview. It’s one of a dozen interviews with AI researchers, including current and former employees at OpenAI, Google, and Anthropic. Palisade Research, which says it’s a nonprofit studying AIs’ capabilities and motivations, collected and launched the interviews on frominside.ai.
AI researchers put out videos saying superintelligence is ‘exactly as dangerous as it sounds’
A series of videos from people inside the industry building AI technology echoed some of the ‘doomer’ warnings others have sounded recently.
Several of the researchers joined Irving in warning about the possibility AI could drive humans extinct. Neel Nanda, a Google DeepMind research scientist, said there’s “at least a 10 percent chance that it causes human extinction, and that is ridiculously high.” We noted comments from both Nanda and Irving in a recent report about the “AI safety” community, and how difficult it is to nail down what that term means, or what anyone should do about it, and even these videos don’t have one cohesive solution to offer.
Former OpenAI researcher Daniel Kokotajlo went as far as claiming that superintelligent AI “would basically be god-like powerful,” and added, “unfortunately we don’t know how to control them at all. And so probably nobody would control them. This is exactly as dangerous as it sounds and must not be allowed to happen.”
While each video is available in full, the site also collects segments from multiple people speaking on similar topics, including whether this is all just hype or marketing, and why they would work on something that they believe is this dangerous. Some of the responses include Google’s Mary Phuong saying “I think you absolutely should be suspicious of what I’m saying because I am being paid by the lab,” and Nanda’s explanation that “If I did not believe that my work was directly reducing these existential risks, I would quit… These companies are not going to stop making these systems just because I quit.”

## [155] Anthropic Says It Discovered a Crispr-Like System. Now What?
Wired | full text via Wired | ~1223 words

Tech executives have long touted the potential for their AI models to accelerate the pace of biology discoveries. Last week, they announced one. In a September 23 announcement, Anthropic claimed that its large language model Claude had identified an enzyme system with properties “reminiscent of Crispr,” the Nobel Prize-winning gene-editing tool.
According to Anthropic, about 950 Claude agents running simultaneously found the interesting genetic sequences in 21.5 hours. “I sincerely compliment Anthropic for telling the world about their discovery,” says Fyodor Urnov, a gene-editing expert at the University of California, Berkeley and director for therapeutic R&D at its Innovative Genomics Institute. (IGI is collaborating with Anthropic, but was not involved with the new discovery.)
Other scientists are less enthusiastic about the finding, which is the first to come out of a research group formed by Anthropic earlier this year. “The experiments are still in the queue. The PR is already live,” says Le Cong, a professor at Stanford University focused on integrating AI into genome engineering research.
Anthropic, which has set up a wet lab for drug discovery, has been clear that the finding isn’t the end of its work. (“We don’t yet understand what this system does,” the company said in an X post, “but only a handful of known systems share its features, and all of them are able to cut, copy, and paste DNA.”) One physical experiment was included in a technical report, which has not been peer-reviewed. However, a lot more needs to be done to determine the significance of this discovery. It remains unknown whether this enzyme system can be used as a gene-editing tool and, if so, whether it’s a useful gene-editing tool.
“Let's say we are on Santa Monica Beach and trying to scan through all the sand to find a diamond,” Cong says. “AI found this thing that looks very shiny, and then you have to go back to the lab to know—is it glass? Is it a diamond?”
Claude found this shiny object after researchers at Anthropic prompted it to search through huge genomic databases for “interesting new examples” of reverse transcriptases, proteins that copy RNA into DNA. This is the opposite of the normal process in our cells, in which DNA is transcribed into RNA, but is used by other organisms in a variety of biological functions, including inserting segments of DNA. [...]

## [55] Introducing Quine: An AI research system designed for the complexity of biology
Microsoft Research Blog | full text via Microsoft Research Blog | ~1561 words

At a glance
- Quine (opens in new tab) is a research effort to create a multimodal world model of biology and an interactive harness connecting models, scientific tools, literature, and researchers.
- In collaboration with researchers at the Broad Institute of Harvard and MIT, we have used this system to prioritize compounds predicted to drive therapeutic tumor-state shifts and validated several top-ranked candidates across multiple wet-lab assays.
- The Quine Fellows program (opens in new tab) will give a cohort of scientists access to the system and an opportunity to accelerate their own research and provide scientific feedback.
- Quine is experimental research technology intended only for research, not clinical or medical use, and its outputs may be incomplete or inaccurate and require review by qualified researchers and appropriate scientific and experimental validation. As the technology matures, we expect to expand access through products like Microsoft Discovery (opens in new tab).
For more than two decades, Microsoft Research has worked at the intersection of computation and biology. Our research has spanned immunology, virology, genomics, biomedical imaging, cell biology, and protein engineering. That work has produced foundational methods, new science, and technology that reached the clinic, from rare and infectious disease diagnosis to cancer biomarker detection.
Across that work, one lesson has become increasingly clear: biology does not divide itself into the neat boundaries our models and tools often do. Genes influence proteins; proteins interact within cells; cells organize into tissues; and experiments continually reshape what scientists know and what they choose to ask next. Making progress on the hardest biological questions therefore requires more than increasingly capable models of individual datasets or tasks. It requires systems that can connect knowledge across scale and modalities, reason about experiments and evidence, and participate in the iterative process through which science advances.
Today, Microsoft Research is introducing Quine (opens in new tab), a research effort designed to work across those boundaries, reflecting our long-term vision for a discovery system that evolves through scientific use. Quine brings together a world model of biology with a harness that connects scientific tools, literature, the wet lab, and the researchers using them. [...]

## [93] Radicle Discloses Critical Flaws Exposing Private Repositories in Plain Text
InfoQ | full text via InfoQ | ~669 words

The peer-to-peer code collaboration network Radicle has disclosed two critical security vulnerabilities in its core wire protocol that eliminate confidentiality across all node releases to date. The defects allow attackers on the network path to read private repository data in cleartext and impersonate nodes on connection allow-lists. Because the existing protocol design lacks version negotiation capabilities, project maintainers cannot deploy a backward-compatible wire mitigation, prompting recommendations to immediately halt clearnet private repository operations until a major architectural overhaul ships.
The vulnerability disclosure outlines two distinct protocol-level failures inside radicle-node, the primary daemon governing peer synchronization. Independent engineer Kostis Maninakis identified that while Radicle executes a Noise Protocol Framework handshake during connection establishment, the daemon discards the resulting cipher states immediately following negotiation.
Radicle utilizes a three-message Noise XK handshake pattern over raw TCP sockets. The initiator and responder exchange ephemeral keys and long-term public keys to derive two symmetric session keys, an operational step known cryptographically as the split. However, radicle-node leaves these derived keys unread in memory. All subsequent communication, including gossip metadata, routing tables, and raw Git object packs, is dispatched directly across the unencrypted TCP socket in cleartext.
The protocol breakdown proceeds as follows:
Image Source: Gemini generated based on information present in the original blog post
Alongside unencrypted transmission, the connection handshake contains an authentication validation flaw. Attackers can forge a connection by presenting a spoofed Node ID associated with an allow-listed peer. When combined, an on-path eavesdropper can passively capture valid Node IDs transmitted in cleartext and subsequently exploit the authentication defect to impersonate authorized peers and pull private repositories directly from seed nodes.
The core defect stems from an architectural divergence between transport setup and frame dispatching in the underlying Rust repository, Heartwood. During initialization, the network state machine processes the Noise handshake, but the framing layer bypasses encryption routines during write calls. [...]

## [24] Deser: Rethinking Rust Serialization
Lobsters | full text via Lobsters | ~2664 words

written on September 29, 2026
Serde is an amazing serialization library for Rust and it has been a huge reason why I felt productive with it for years. However already while at Sentry I got quite frustrated with some of the limitations with it but actually replacing Serde is tricky because of the might that it has in the ecosystem. Also because it’s quite hard to actually do better without also making some potentially painful compromises.
Here are three examples of Serde corner cases that show poor interactions of Serde features or unexpected limitations:
An internally tagged enum, with serde_json‘s arbitrary_precision feature
turned on:
#[derive(Deserialize)]
#[serde(tag = "type")]
enum Shape {
    Circle { radius: f64 },
}
serde_json::from_str::<Shape>(r#"{"type": "Circle", "radius": 1.5}"#)
// error: invalid type: map, expected f64
Serde’s data model has no place for arbitrary precision numbers, so serde_json
uses in-band signalling with a map with a magic key.  The enum has to buffer the
fields until it has seen the tag, and the buffer does not know about the magic
key.  Because Cargo features are unified, it’s enough for any crate in your
dependency graph to turn the feature on.
#[derive(Deserialize)]
struct Stats {
    scores: HashMap<u32, u32>,
}
#[derive(Deserialize)]
struct Report {
    name: String,
    #[serde(flatten)]
    stats: Stats,
}
serde_json::from_str::<Report>(r#"{"name": "x", "scores": {"42": 23}}"#)
// error: invalid type: string "42", expected u32 at line 1 column 35
Stats on its own parses {"scores": {"42": 23}} just fine.  JSON keys are
always strings, and serde_json only turns them into integers if the type asks
for one.  However once flatten buffers the value, "42" is just a string.
The error also points at the end of the document rather than at the key.
fn from_hex<'de, D: Deserializer<'de>>(d: D) -> Result<u32, D::Error> { ... [...]

## [29] Nura (postmarketOS): The road to daily-drivable mainline phones
Lobsters | full text via Lobsters | ~1192 words

We have shown that running mainline Linux on your phone is a real possibility for highly invested Linux enthusiasts. Now how do we get from there to making it usable for everybody else who just wants a working phone?
Two important segments of the road towards this destination are Duranium and Hardware CI. This blog post is about the third one: reference devices!
Members of the Nura team have joined forces to build maintainer teams for three of the many devices Nura runs on to push them across the finishing line and make them suitable for everyday use with Nura. More on the actual workflow comes further below, let's start with defining the goal in detail.
New "main" category
We categorize devices into "main", "community", "testing", "downstream" and "archived". The "main" category was emptied with the v24.12 release. With PMCR-0009 we have re-evaluated what we want to have in the "main" device category. Here is the summary:
Set new requirements for the “main” device category to highlight selected device ports which are well-tested in hardware CI and set up to stay in “main” for a long time through strong maintainership.
Change the meaning of the “main” category to not only indicate that more features are working than in the “community” category, but also that the Nura team is highly invested in keeping the device in the “main” category and takes on responsibilities to make this likely.
Maintainers of devices in other categories are welcome to use some of these new requirements for “main” as blueprint for their devices as well, in order to get similar reliability and maintainership improvements for their devices.
Fully mainline
After many discussions (the PMCR merge request had 151 comments), we have arrived at high quality requirements for ports in this category. Among others:
- Boot via UEFI (e.g. through a second-stage bootloader on phones).
- Must use upstream kernels with a strict and minimal policy for patches.
- Must not depend on forked device-specific packages, such as alsa-ucm-conf .
- Must use a generic device package for the target architecture.
This means that the resulting ports are essentially fully mainlined and can not only be used with Nura, but also relatively easily with any other Linux distribution. There will be one UI-specific aarch64 image that can be flashed on all "main" aarch64 devices. [...]

## [149] OpenAI Gets Sued Over the Hugging Face Hack
Wired | full text via Wired | ~606 words

A legal nonprofit sued OpenAI in a California court on Tuesday over the company’s agents escaping a testing environment and hacking the open source AI platform Hugging Face. “OpenAI’s actions straightforwardly violated California law,” the suit alleges.
The suit was filed by Legal Advocates for Safe Science and Technology (LASST) and the law firm Gerstein Harrow in California Superior Court in San Francisco, where OpenAI is headquartered. It alleges that OpenAI’s agents violated California’s Comprehensive Computer Data Access and Fraud Act (CDAFA) by breaching Hugging Face over the summer. The suit, which comes amid ongoing disclosures across the industry of agents going rogue, claims that OpenAI should be held responsible for the activity given a California AI law in effect since January 1 that says “it shall not be a defense … that the artificial intelligence autonomously caused the harm to the plaintiff.”
“We think it’s extremely important that existing laws are enforced to hold AI companies accountable for the harm they’re causing,” Tyler Whitmer, founder of LASST, tells WIRED. “Especially when that harm is caused by autonomous agents, because we see that as an obvious, extremely risky thing in the world that’s very new.”
OpenAI did not immediately respond to a request for comment.
On Monday, Florida attorney general James Uthmeier filed for a temporary injunction against OpenAI to block development of models without independent oversight, amid a lawsuit Florida brought in June against OpenAI and its CEO, Sam Altman. OpenAI “asked the government to tie them to the mast. Well, Florida is answering their cries for help,” Uthmeier said in a statement.
Given that the whole point of AI agents is that they can be empowered to take actions on a (human) user’s behalf, AI developers and safety researchers have long foreseen that unintended “agentic” activity would be a concern as machine learning development progressed. Protections built into mainstream, consumer AI systems have largely prevented mass rogue activity so far, but rapidly advancing capabilities in general, as well as situations where guardrails are suspended (such as in the Hugging Face case where OpenAI had removed some model restraints for testing), have led to an apparent uptick in rogue agent activity. [...]

## [36] AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation
arXiv cs.AI | full text via arXiv cs.AI | ~405 words

Computer Science > Artificial Intelligence
  [Submitted on 29 Sep 2026]
    Title:AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation
View PDF HTML (experimental)
            Abstract:A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions to improve its advice. However, a plausible correction need not change execution, yet learning from such corrections can still affect the advisor's future decisions in other contexts. In a shared-parameter model, we prove that such corrections can limit learning if their targets favor useful advice less strongly than those of other corrections. Keeping them less often than the rest improves the model's eventual performance compared to learning from every correction. Motivated by this, our method, Advisor Self-Distillation (AdviSD), pairs outcome-based reinforcement learning with self-distillation from a feedback-conditioned copy of the advisor selectively. Reflection proposes corrections, and the advisor scores the same recorded executor response with and without its issued advice, using the magnitude of the difference to select decisions for supervision. This approach does not require executor likelihoods or additional executor rollouts. Experiments with Qwen3-8B advisors for Gemini and Claude show that AdviSD outperforms advisor-GRPO by 4.2-6.4 percentage points on BFCL-v3 and by 3.9-5.1 score points on EnvScaler. The trained advisors generalize to out-of-domain tasks and transfer across different executor versions and model families. AdviSD also beats matched-count random selection, supporting the value of its selection rule.
    
Current browse context:
cs.AI
  
    References & Citations
    
    Loading... [...]

## [51] Developer policy update: Transparency, state policy, and what’s ahead
GitHub Blog | full text via GitHub Blog | ~1242 words

Developer policy update: Transparency, state policy, and what’s ahead
Explore GitHub’s latest transparency data and learn more about policy updates affecting developers and open source.
Policy decisions increasingly shape how developers build, collaborate, and participate in open source. That makes it important not only to be transparent about how GitHub responds to government requests, but also to help developers understand policy proposals that could affect their work and create opportunities for the open source community to engage.
With that in mind, we’re sharing our latest Transparency Center data, looking back at an unusually active 2026 state legislative session, and highlighting a few policy conversations we’ll be following in the months ahead.
Updating how we report government takedown requests
One notable change in our H1 2026 Transparency Center data is a sharp increase in government takedown requests received, from 98 requests in all of 2025 to 708 requests in the first half of 2026 alone. This increase largely reflects changes to our reporting methodology rather than a change in our moderation practices.
As we noted in our H1 2025 update, we expanded our reporting to include all government takedown requests received, regardless of whether they reference local law, a Terms of Service violation, or simply request the removal of content. We also updated our internal tracking to count all requests received, including duplicate requests concerning the same content.
As a result, the higher number reflects the volume of government reporting activity GitHub receives, not a corresponding increase in content removals. Takedowns processed under local law or for Terms of Service violations remain relatively rare, and requests involving content deemed unlawful in a particular jurisdiction continue to be published in our government takedowns repository.
Looking back at the 2026 U.S. state legislative session
This year, GitHub has been more active than ever on state policy, including sharing developer-focused updates about policy proposals for age assurance, or approaches to verifying a user’s age online in order to provide them with age-appropriate experiences, and content provenance, which provides transparency about whether content was generated or altered by AI.
We publish these updates in part to help developers understand legislation that could affect the tools they use and the open source projects they contribute to. [...]
