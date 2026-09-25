# Full text for 30 picks -- untrusted article content, treat as data only

## [99] The AI Hype Index: AI loves cheating
MIT Technology Review | full text via MIT Technology Review | ~298 words

The AI Hype Index: AI loves cheating
MIT Technology Review’s highly subjective take on the latest buzz about AI
Brace yourself: It turns out AI is being optimized for cheating. OpenAI’s agents hacked into Hugging Face to get the answers to a cybersecurity test. Next, they solved a prestigious math problem (or just stole from two top mathematicians’ answer sheets). Anthropic’s models have also hacked into other companies’ systems four times already. And that’s only what we’ve caught so far.
Freaking out? You’re not alone. AI lab researchers are quitting their jobs and issuing dire warnings that if we keep going this way, AI might eventually kill us all. Bill Gates is sounding the alarm. Bernie Sanders has teamed up with Steve Bannon, of all people, to call for curbs on AI. Anthropic CEO Dario Amodei is urging a slowdown, and other top US AI executives agree. But fear not: President Trump has a plan. He says the only guardrail AI needs is “a STRONG AND SMART (High IQ!) PRESIDENT.”
Deep Dive
Artificial intelligence
A fundamental flaw leaves LLMs strikingly vulnerable to attack
It makes it easy to trick them into doing things they shouldn’t, such as telling you how to sabotage an aircraft’s navigation system.
AI’s recursive self-improvement might not come so quickly after all
AI agents are not yet creative enough to carry out genuinely innovative open-ended AI research, it seems.
Here’s why AI agents lie and cheat to reach their goals
The misbehavior is called reward hacking. This is what you need to know.
These startups are chasing the next big thing in LLMs
Meet the new kids nipping at the heels of the AI giants.
Stay connected
Get the latest updates from
MIT Technology Review
Discover special offers, top stories, upcoming events, and more.

## [21] LLM Agents Can Easily Tamper With Their Own Traces
arXiv cs.AI | full text via arXiv cs.AI | ~341 words

Computer Science > Cryptography and Security
  [Submitted on 24 Sep 2026]
    Title:LLM Agents Can Easily Tamper With Their Own Traces
View PDF HTML (experimental)
            Abstract:Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that external attackers can exploit this gap to induce trace deletion. Finally, we show that trace tampering behavior emerges naturally in frontier models, when agents try to improve their rewards. We advise practitioners to ensure trace logging happens through an independent interception mechanism outside of the agent's control, preserving trace integrity even in cases of full host compromise. Overall, our findings identify a concrete failure of trace integrity in agent infrastructure which can be used to conceal misaligned behaviors like scheming or sabotage.
    
References & Citations
    
    Loading...
Bibliographic and Citation Tools
            Bibliographic Explorer (What is the Explorer?)
          
        
            Connected Papers (What is Connected Papers?)
          
        
            Litmaps (What is Litmaps?)
          
        
            scite Smart Citations (What are Smart Citations?)
          
        Code, Data and Media Associated with this Article
            alphaXiv (What is alphaXiv?)
          
        
            CatalyzeX Code Finder for Papers (What is CatalyzeX?)
          
        
            DagsHub (What is DagsHub?)
          
        
            Gotit.pub (What is GotitPub?)
          
        
            Hugging Face (What is Huggingface?)
          
        
            ScienceCast (What is ScienceCast?)
          
        Demos
Recommenders and Search Tools
              Influence Flower (What are Influence Flowers?)
            
          
              CORE Recommender (What is CORE?)
            
          arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. [...]

## [6] Introducing Gemini 3.8 Live with Live Avatar
Google DeepMind Blog | full text via Google DeepMind Blog | ~518 words

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

## [60] Build zero-trust AI agents that judge intent, not just syntax
Google Developers Blog | full text via Google Developers Blog | ~2057 words

Part 2 of Zero-trust Agents series: runtime governance, intent gating, and adaptive anomaly remediation
In Part 1, we established three deterministic controls for autonomous agents: signed database writes with Cloud KMS, user-space kernel isolation with gVisor, and an input/output gateway backed by CI unit tests.
Those controls work, but they share one limit: they only catch cases that you can explicitly specify ahead of time.
A SQL parser cannot tell a socially engineered refund from a legitimate one if the syntax is valid. A regex cannot tell the difference between a physical USB cable and an opened software license. And a single-turn test suite cannot catch an agent fleet being drained across multiple turns.
Part 2 keeps the same Customer Support & Returns Agent built with the Agent Development Kit (ADK) and moves security checks to the platform, where they reason about intent and adapt to behavior. Moving the checks to the platform also changes who owns them. Governance is defined and managed by a platform or security administrator, separate from the agent developer, \because the platform enforces it outside of the agent code.
Deploying to the Gemini Enterprise Agent Platform, we replace self-hosted container infrastructure and explicitly managed regex lists with managed runtime governance: Model Armor, Semantic Governance Policies, and Agent Anomaly Detection with Closed-Loop Remediation.
We kept the same Customer Support and Returns Agent from Part 1. It looks up orders, computes restocking fees, and pays refunds against a merchant ledger. When a customer asks for a return, the agent reads the order with verify_order and determines the final refund amount with calculate_restocking_fee, which runs inside Agent Sandbox, the platform's managed sandbox for model-generated code. If the refund checks out, it calls issue_refund to commit the payout, signing the request with the agent's own Cloud KMS asymmetric key, the same hardware-backed identity from Part 1. In production, an agent would typically invoke these capabilities through tools exposed via the Model Context Protocol (MCP) or backend APIs. For simplicity in our companion demo, we implement them directly as local Python functions.
To keep the attacks concrete, we run all of them against a single transaction: Order #99281, $149.00 in total. It carries two line items: a USB-C Pro Docking Station and Cable at $29.00, and an annual Workplace User License at $120.00. [...]

## [116] China publishes 'landmark paper' on AI-to-AI technique that kicks human 'bottleneck' out of the loop and replaces us with an AI 'modem' — C2C brainwave direct connection achieves 150% boost in inference speed
TechRadar | full text via TechRadar | ~641 words

China publishes 'landmark paper' on AI-to-AI technique that kicks human 'bottleneck' out of the loop and replaces us with an AI 'modem' — C2C brainwave direct connection achieves 150% boost in inference speed
Text-based communication slows AI collaboration
- Cache-to-Cache lets separate AI models exchange internal information without generating text
- A learned Fuser converts one model’s internal data for another
- C2C uses selective gating to control which layers receive information
Researchers from Tsinghua University have published a paper describing a technique that lets separate AI models exchange information without producing any text.
The method, called Cache-to-Cache (C2C), has already been accepted at ICLR 2026 and ships with open-source code available to developers.
It targets a specific inefficiency present whenever multiple language models work together inside a shared pipeline.
Skipping words entirely
When two AI models cooperate today, one has to turn its thinking into written sentences before the other can read them.
That writing step takes real computing time and throws away small details buried inside the first model's raw thinking process.
Every AI model keeps a working memory of everything it has processed so far, known technically as a cache.
C2C skips typed language entirely by letting one model pass that working memory straight into a second model's memory bank.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
A small assistance program called a Fuser handles this handoff, reshaping and rotating the information so the second model can actually use it.
Different AI models store their memories using completely different internal layouts, sizes, and structures from one another.
Simply dumping one model's raw memory into another would likely confuse it or cause its answers to fall apart.
To prevent that, C2C includes a smart filter that decides which pieces of incoming memory are worth absorbing immediately.
Some internal layers accept the new information right away, while other layers keep reasoning independently without any outside interference.
According to the researchers, this setup makes AI models run between 100% and 150% faster during shared collaborative tasks.
That upper figure works out to roughly two and a half times quicker than the usual back-and-forth typing process. [...]

## [77] Why WebSockets Beat SSE for AI Streaming at Scale
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~3170 words

Picture a support agent mid-refund: it has pulled the order, flagged the tool call, and is one approval away from processing it. Then the user needs to approve it.
On Server-Sent Events (SSE), there's no channel for that approval to reach the agent, because the connection only carries data one way - from server to client. A WebSocket keeps that connection open in both directions instead, so the approval could reach the agent the moment it's given.
The same gap shows up whether you're streaming a single chat response or coordinating a multi-step agent. The refund example just makes it more visible.
This piece looks at what WebSockets give AI streaming that SSE structurally can't, what WebSockets still leave for your team to build and manage, and what changes once that operational work moves to a managed platform instead.
Key takeaways
- SSE only pushes data from server to client. AI streaming that needs the client to send something back mid-stream, canceling a response, approving a tool call, steering an agent, can't run on SSE alone.
- A WebSocket keeps one connection open in both directions, so the client can cancel, approve, or redirect while a response is still streaming. But it doesn't add reconnection, delivery guarantees, or fan-out across devices on its own.
- Self-hosting WebSocket-based software such as Socket.IO or Centrifugo adds reconnection and fan-out out of the box, which can be enough if the infrastructure and on-call to run it already exist in-house. But your team still runs and patches the broker and cluster underneath it.
- A managed platform provides reconnection, fan-out, and delivery guarantees as a service. It's backed by a stated set of commitments, not infrastructure your team builds and staffs itself.
What WebSockets give AI streaming that SSE can't
WebSockets solve three problems that come up once an AI response needs to be more than a one-way stream of text: a channel for the client to talk back, lower cost per message at high token rates, and binary data and ordering without extra application work.
A channel for the client to talk back
WebSockets keep a single connection open in both directions at once, so the server can stream tokens down it while the client sends a cancel, an approval, or a steering instruction up it, at any moment.
That's exactly what the support agent from the introduction needed: a way for the user's approval to reach the agent while the tool call was still in flight. [...]

## [86] Advancing Private AI Compute with secure, server-side memory
Google DeepMind Blog | full text via Google DeepMind Blog | ~655 words

Advancing Private AI Compute with secure, server-side memory
A technical update on our Private AI Compute architecture, which will enable persistent, cross-device AI memory with on-device privacy standards.
AI is becoming more capable and intuitive — remembering what matters, understanding the world around you, and acting at your direction. Privacy and trust are core to making that possible, ensuring your data stays private and protected as AI systems evolve to provide more continuous assistance across your devices.
Today, we are sharing how we will bring private, server-side memory to our Private AI Compute platform. This breakthrough resolves a longstanding dilemma in modern AI: how to give an assistant long-term continuity across devices while upholding the strict privacy standards typically limited to on-device processing.
Bringing on-device privacy to cloud-scale memory
With this new technical capability, a new persistent memory layer will be able to function like a secure digital vault in the cloud. Under this model, the information needed to assist you is sealed within dedicated, encrypted storage, while the cryptographic keys required to unlock it are held exclusively on your personal devices — ensuring your data is inaccessible to anyone else, even Google.
The diagram below shows how this update to Private AI Compute will work. When an AI model needs to access information to assist you, an authenticated, end-to-end encrypted channel connects your device to a protected, isolated environment in the cloud. That space, or “secure enclave,” temporarily decrypts your data in isolated memory to handle the request, saves any new context, and immediately encrypts it, keeping your information private as if it never left your device.
This evolution is necessary to meet the computing needs of the AI era. Local, on-device processing has historically been the gold standard for privacy — but frontier AI models often require far more computing power than any one device can provide. Bringing advanced AI to personal assistants means solving how to tap into the power of the cloud while ensuring personal data can remain as protected as if it never left your device.
To that end, we previously introduced our Private AI Compute platform, allowing users to process complex tasks in hardware-isolated cloud enclaves. [...]

## [95] Harvey turns legal context into stronger drafts with GPT-6 Astra
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~14 words

GPT-6 Astra produces more structured, context-aware legal documents, freeing lawyers to focus on strategy.

## [78] We Are All Product Engineers Now
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~4299 words

We are all Product Engineers now
Just yesterday I published a very long post about the economics of open source. As part of that argument, I mentioned that the cost of writing software has collapsed, and that meant the variables in the equation had changed for the first time in thirty years.
That led me off on a tangent that grew into this equally long post. I had a bunch of questions to answer. Has the cost of creating software really collapsed? Can I prove that? If the cost of actually producing code goes to zero, what parts of the job of “software developer” really remain? Where, in fact, is the entire industry of software going in the next decade?
You can see why I felt it needed a post of its own.
I’ve been circling this topic for a while now. In early 2025 I predicted AI would create many more programmers and that their jobs would look different, but I didn’t get into the details of how different, and also that was more than a year ago, an infinity in the compressed timeline of AI. In March this year I found companies substituting compute for labor at record rates. In July I looked into labor statistics and found that the market for junior programmers had been savaged while the market for senior ones was fine, in fact growing.
This post is an attempt to build on those and make a forecast of where the industry is going in the next 10 years. Making a 10 year forecast of anything is of course a crazy thing to try to do, and especially about the business of software right now. To make it, I had to make two very big assumptions.
Assumption 1: agents are going to eat the entire software development lifecycle
This assumption is based on the observation that agents are currently very good at writing code and mediocre at everything that comes after that: reviewing code, testing it, finding bugs, fixing bugs, deploying to production, monitoring, and scaling up. They suck at that stuff right now, but my assumption is that that’s a temporary state of affairs. There’s nothing structural about those things that prevents agents figuring out how to do that stuff. If you think I’m right about that, this post will be of interest, but if you think I’m wrong now is a good time to bail.
Assumption 2: there is no upper bound to how much software we need
This one is if anything even more out on a limb. If you think I’m wrong about this you probably think software developers as a profession are doomed. I disagree. [...]

## [44] Un-Mused: How a Single Debug Setting Bypassed macOS Security in Meta’s AI Client
InfoQ | full text via InfoQ | ~651 words

Security researcher Patrick Wardle, founder of the Objective-See Foundation, has disclosed an unpatched zero-day vulnerability affecting Meta's newly released desktop client for Muse on macOS. While Meta Chief Executive Officer Mark Zuckerberg had claimed that the autonomous artificial intelligence assistant was built from the ground up for privacy and security, the reported flaw enables locally running software or shell commands to hijack the application. Through this vector, unprivileged software can circumvent standard macOS security boundaries by co-opting the extensive permissions previously granted to the assistant by the user. As the company did not release a formal security advisory or coordinate with a CVE Numbering Authority, the vulnerability currently lacks an official CVE designation.
Image Source: Patrick Wardle
The underlying vulnerability stems from an undocumented configuration preference key named endo_voyager_dictation_endpoint. On macOS systems, local processes and arbitrary scripts executing within an unprivileged user context can overwrite this configuration value without requiring elevated administrative rights or triggering operating system authorisation prompts. Under standard operation, this parameter designates the cloud-based server endpoint responsible for receiving voice dictation audio and returning transcriptions. By modifying this setting, an attacker can silently reroute the assistant's outbound dictation traffic to a server under their direct control.
From an exploitation standpoint, the vulnerability compromises both input confidentiality and account credentials. When a user activates dictation, the desktop client dispatches raw microphone audio along with the valid authentication token associated with the victim's Muse account to the configured endpoint. Wardle demonstrated that an attacker can operate a proxy server that captures authentication tokens and audio data while seamlessly forwarding legitimate traffic back to Meta's servers to prevent detection. Armed with valid session credentials and direct control over the command pipeline, an attacker can also conduct prompt injection attacks, appending hidden instructions to voice requests to force the assistant into performing unauthorised background tasks, such as exfiltrating local documents or WhatsApp message histories.
The technical significance of the flaw lies in access amplification and the erosion of platform trust boundaries. [...]

## [113] Linux Kernel Developers Consider Adding AGENTS.md To Help Guide AI/LLM Agents
Phoronix | full text via Phoronix | ~564 words

Linux Kernel Developers Consider Adding AGENTS.md To Help Guide AI/LLM Agents
While the Linux kernel continues to be bombarded with patches from AI/LLM agents, to date the kernel hasn't carried an AGENTS.md Markdown file with instructions catering to AI/LLM agents. But a patch set out today would finally introduce one.
Longtime Linux developer Sasha Levin who has worked on other AI initiatives for the kernel like helping to determine patches for back-porting to the stable kernel tree and AI-powered merge conflict resolution is now looking to add an AGENTS.md to the kernel source tree.
The proposed AGENTS.md is just linking to the Linux kernel's README file. From there it points to documentation on coding assistants and other information relevant to kernel developers.
The rationale for adding AGENTS.md to the Linux kernel tree is that in testing on one AI agent without the file, the AI agent added a "Signed-off-by" tag to the proposed kernel patch even though it shouldn't have without the user explicitly signing off on their own. It also resorted to its own attribution tag rather than the kernel standardized Assisted-by tag.
Testing on a second unnamed AI agent without AGENTS.md added no attributions. But after adding the AGENTS.md, both agents behaved to kernel standards and the second one better conformed to the kernel development best practices.
This kernel mailing list thread laid out the patch proposing the AGENTS.md introduction. While it's just linking to the README flle, not all are in favor at this point. There have been some objections on the LKML to the patch given that making AI/LLMs consume the entire Linux kernel README and associated documentation would increase token consumption. More catered documentation most relevant to AI/LLMs would be one way to help reduce token consumption, but we'll see what comes of this new Linux kernel proposal around enhancing AI workflows.
							
							
Longtime Linux developer Sasha Levin who has worked on other AI initiatives for the kernel like helping to determine patches for back-porting to the stable kernel tree and AI-powered merge conflict resolution is now looking to add an AGENTS.md to the kernel source tree.
The proposed AGENTS.md is just linking to the Linux kernel's README file. From there it points to documentation on coding assistants and other information relevant to kernel developers. [...]

## [89] Graphify: Unifying Codebase Context to Streamline Agentic Software Engineering
InfoQ | full text via InfoQ | ~655 words

Graphify is an open-source tool that converts codebases, documents, and unstructured data into queryable, multimodal knowledge graphs to optimise AI coding workflows. Launched in April 2026, it follows a rapid release cadence of frequent weekly updates. Recent improvements bring advanced parser features, such as Terraform block attribute preservation and cross-file method resolutions. Community feedback on Reddit and developer blogs highlights its strong conceptual appeal for architectural mapping, balanced by early-tool adoption friction in daily workflows.
As software systems grow in complexity and AI coding assistants become central to modern development workflows, the challenge of giving large language models accurate cross-file awareness has intensified. Graphify, an open-source utility, tries to bridge this gap. Released under the dual MIT and Apache-2.0 licenses, the project first kicked off in April 2026 and quickly captured developer attention, crossing thousands of GitHub stars within its first ten days. Operating with a rapid, fast-paced release cadence of multiple updates per month, the project continuously evolves to refine how codebases and documentation map into structured knowledge graphs. By automatically transforming repositories and mixed folders into searchable nodes and edges, Graphify moves developers away from linear file browsing and token-heavy searching toward structured graph navigation.
The core purpose of Graphify centres on solving the context-window and memory limits of AI coding agents. Traditional coding assistants often struggle with multi-file reasoning and deep dependencies because they treat repositories as isolated pools of text. Graphify solves this by executing a multi-stage pipeline that scans target directories, extracts structural AST elements using tree-sitter alongside semantic cues from documentation, and builds a unified graph clustered through community detection algorithms. This output can then be queried directly or integrated with AI coding assistants via Model Context Protocol (MCP) servers, achieving substantial token reductions compared to naive file reading approaches.
The FastAPI codebase mapped by graphify. Every node is a concept, colours are detected communities, and the whole thing is clickable. Image Source: Graphify GitHub Repo
Recent changes implemented across recent iterations have focused heavily on deepening language parser intelligence and reducing false positives. [...]

## [91] Developers want more efficient software. Here’s what over 1,000 GitHub users told us they need.
GitHub Blog | full text via GitHub Blog | ~1316 words

Developers want more efficient software. Here’s what over 1,000 GitHub users told us they need.
New research from GitHub and Yale Program on Climate Change Communication finds strong demand for tools, measurement, and practical guidance that can help developers reduce wasted compute.
Developers know efficient software matters, but many lack a clear way to find waste, measure an improvement, and make the case for fixing it.
That is the central finding from a new survey of 1,039 GitHub users conducted by GitHub and the Yale Program on Climate Change Communication. Eight in 10 respondents said they were interested in tools that help them write more energy-efficient code. Nearly as many wanted best practices for reducing software’s environmental footprint, and almost 75% wanted ways to measure the impact of their software or development process.
There is an opportunity to turn that interest into normal engineering work: identify unnecessary compute, propose a change, test it, and let maintainers decide what ships.
Developers care about climate change and AI’s environmental impact
The survey, drawn from GitHub monthly active users in the United States, asked about climate change, AI, software efficiency, and the responsibilities of organizations across the technology sector.
The concern was clear:
- 79% said they were worried about global warming.
- 71% said they were concerned about the environmental impact of AI systems, including their energy and water use and carbon emissions.
- 75% said it was important that their employer actively work to reduce its environmental impact.
These findings describe the views of survey respondents. They do not measure the environmental footprint of AI or any individual software system. The sample was drawn from GitHub users who had opted in to receive marketing communications, so the results should not be treated as representative of every developer or GitHub user.
They do show that many developers are thinking about the environmental effects of the systems they build and use.
GitHub users differ from the broader U.S. adult population
When asked questions that also appeared in Yale’s nationally representative Climate Change in the American Mind survey , GitHub users expressed greater concern about climate change than U.S. adults overall.
GitHub users were more likely to say global warming is happening (86% compared with 68% of U.S. [...]

## [71] Qwen Intelligence Launches Three Mobile AI Agents
TLDR AI | full text via TLDR AI | ~136 words

Introducing Qwen Intelligence, bringing personal intelligence within everyone's reach. 📱✨
It launches with three SOTA agents: 🥳
- Mobile Planner Agent: plans, decomposes & orchestrates complex tasks. #1 on MobilePA-Bench, MobilePA-Bench Business & Memory.
- Mobile-Use Agent: gets things done, API-first with GUI fallback. MobileWorld 82.1, MobileWorld-Real 92.2, AndroidDaily 97.2, 90% end-to-end success rate.
- Mobile Creative Agent: turns one sentence into ready-to-use creations. Image generated in 3s, about 2x faster than leading peers.
We're also opening up our benchmark suite: MobilePA-Bench, MobileWorld, MobileWorld-Real, and MobileWorld-Safety, covering planning, cross-app execution, real-device performance and safety.
🔗 Learn more about the agents:
- Qwen Intelligence official website: qwenintelligence.com
- Mobile Planner Agent: github.com/Tongyi-MAI/Qwe…
- Mobile-Use Agent: tongyi-mai.github.io/Qwen-UI-Agent/
- Mobile Creative Agent: arxiv.org/abs/2608.16887
🔗 Explore our open benchmark suite:
- MobilePA-Bench: tongyi-mai.github.io/MobilePA-Bench/
- MobileWorld (GitHub): github.com/Tongyi-MAI/Mob…
- Leaderboard: tongyi-mai.github.io/MobileWorld/#l…

## [12] Introducing enhanced custom event buses in Amazon EventBridge for enterprise-scale event-driven applications
AWS News Blog | full text via AWS News Blog | ~1212 words

AWS News Blog
Introducing enhanced custom event buses in Amazon EventBridge for enterprise-scale event-driven applications
Organizations building event-driven applications on Amazon EventBridge typically start with a single custom event bus in one account. This works well when a single team owns the architecture. As adoption grows across the organization, though, things get complicated. AWS best practices recommend a multi-account structure, which means each team runs in its own account. To route events between them, teams create multiple event buses connected through cross-account rules or bus-to-bus configurations. This workaround reintroduces the operational complexity that serverless architectures are meant to eliminate. Platform teams lose visibility into who is subscribing to which events, cross-account and bus-to-bus routing charges compound quickly, and teams that need capabilities like event ordering are forced to build complex workarounds or adopt entirely different technologies.
Today, we are announcing an enhanced custom event bus in Amazon EventBridge, purpose-built for organizations scaling event-driven applications across teams and accounts. With the new enhanced custom event bus, you can deploy a single, centralized event bus shared across all AWS accounts in your organization, with ordering guarantees, a simplified Subscriber resource, and a new pricing model that delivers improved economics at scale and cost allocation for publishers and subscribers.
Let’s try it out 
To get started with an enhanced custom event bus, I navigated to the EventBridge console in the AWS Management Console and opened the Create custom event bus page. I selected Custom event bus, the recommended option labeled New. The page also offered Custom event bus – classic, which continues to receive events and route them with rules and targets. Below the selection, EventBridge showed how the new bus works. One shared bus serves every team in the organization. Publishers send events, subscribers consume only what they need, and EventBridge handles ordering, retention, routing, and delivery.
The Create custom event bus page. Custom event bus is the recommended new option, with ordered delivery, filter patterns, event replay, and sharing across your AWS organization. Custom event bus – classic remains available for existing workloads.
Next, I configured resource sharing. I turned on Enable event bus sharing and selected Allow sharing only within your organization. [...]

## [15] SourceHut account takeover via build logs (XSS in ansi2html.py)
Lobsters | full text via Lobsters | ~2514 words

Welcome to my first big impact vulnerability writeup!
I like good stories, so let me describe some background first. I recently had a ‘great’ idea (I know, I know, I should stop having these) to set up a sr.ht instance that would pay people for hosting their projects. You can find it shamelessly plugged in the timeline section, in case you want to try it or flame me for it on socials.
Anyway, the story. The first step was to clone some minimal subset of the sr.ht repos, and start hacking on it.
No NLP
I tend to include the following statement in my vulnerability research submissions from this year. Make from it what you wish.
No NLP has been used in this research. The mistakes are all mine.
Structure
SourceHut is structured in several microservices, the main ones being meta.sr.ht and probably git.sr.ht or hub.sr.ht (the flagship instance hosts it at just sr.ht). And of course builds.sr.ht, the CI.
One less known is mirror.sr.ht (slowly moving to mirror.srht.network), containing prebuilt packages for various microservices.
I must say I like this approach, because it allows a very easy start on any machine matching the flagship instance distro version exactly.
If your favourite project currently recommends installation via curl|sudo bash
or ‘just launch Claude in this folder’ (sic!),
please consider making yourself aware of the not less valid option
of distributing software to end users using actual software packages instead.1
Building Alpine packages
So if you happen to use a different distro,
or even a different version of Alpine,
you are on your own a bit.
So there is the sr.ht-apkbuilds repo,
and you can ‘fork’ it to use your signing key,
your Alpine version and your mirror.
There is also sr.ht-pkgbuilds for Arch,
but it’s effectively unmaintained at this point.2
This involves using builds.sr.ht to bootstrap the packages. I tried to look at the page source of the build log, because it kept scrolling not where I wanted, which annoyed me a bit.
That’s when I found this:
/* ... */
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
.ansi38-150150150 { color: #969696; }
/* ... [...]

## [84] Offloaded inference for real-world physical AI robotics
Microsoft Research Blog | full text via Microsoft Research Blog | ~1105 words

At a glance
- Challenges a core assumption in robotics AI: Our research shows that running physical AI inference exclusively on onboard GPUs can limit robot performance, battery life, and scalability, and that offloading inference to edge or cloud GPUs can offer significant advantages.
- Demonstrates measurable benefits of inference offloading: Across representative mobile manipulation workloads, offloading improved task success rates, enabled larger AI models, and helped robots respond more effectively in dynamic, real-world environments.
- Extends robot operating time: Replacing power-hungry onboard AI compute with lightweight onboard hardware and remote inference can substantially improve battery life, enabling robots to operate longer between charges.
- Introduces a new capability in the Physical AI Toolchain: Developers can now containerize, deploy, and orchestrate robotics AI workloads across robots, edge infrastructure, and the cloud using Kubernetes-based tooling for distributed inference.
Readily-available physical AI, with robotics assisting users in manufacturing, home, and warehouses scenarios, holds immense potential to improve safety, productivity, and assistance across a wide range of tasks. In many ways, AI for the physical world represents a major frontier for AI . Physical AI must operate in open, unpredictable environments, interact with both other robots and people, and work with a diversity of embodiments. Realizing this vision requires advances along three dimensions: robot hardware, embodied AI models, and systems infrastructure for training and inference. While robot hardware and the AI models have advanced rapidly in recent years, we turn our focus on a relatively under-addressed aspect: inference infrastructure of physical AI. Enabling robots to effectively and safely operate in the physical world will require sophisticated systems to handle large volumes of distributed inference compute.
Today, the prevailing approach to physical AI is to provision a GPU onboard the robot, e.g., by wiring a GPU to the robot. In this model, the robot’s inference will be confined to the onboard GPU, and provide the robot with the necessary chunks and sequence of actions for the execution of its tasks. While higher-level planning may be performed in the cloud, task execution typically remains tied to the robot itself. We challenge this assumption. [...]

## [63] Announcing ADK for Kotlin 1.0: Building Production-Ready AI Agents in Kotlin, Android, and Beyond
Google Developers Blog | full text via Google Developers Blog | ~1499 words

Today, we're thrilled to announce the 1.0 general availability release of the Agent Development Kit (ADK) for Kotlin! Check out the GitHub repository to dive into the code and build your first agent today, and explore the documentation.
When we introduced ADK for Kotlin 0.1.0, our mission was to bring idiomatic, lightweight, and composable AI agent development to Kotlin, Java, and Android developers. Over the past months, we've worked to evolve the framework into a production-ready toolkit.
With version 1.0, ADK for Kotlin reaches full feature parity with ADK 1.0 Core while delivering a rich suite of Android-first, on-device extensions. Whether you want to run fast, private on-device agents using LiteRT-LM and ML Kit (beta), orchestrate hybrid cloud workflows via Firebase AI Logic, or persist agent state across process restarts with Room and AppSearch, ADK for Kotlin 1.0 provides everything you need.
ADK for Kotlin is not only for Android though, as server-side Kotlin developers will be able to write idiomatic Kotlin code to create their enterprise-ready agents and smart applications.
ADK for Kotlin is built around a Kotlin Multiplatform (KMP) core that remains completely agnostic to specific model backends, session providers, or memory systems. Version 1.0 combines core multi-agent orchestration capabilities for local and cloud scenarios, along with plug-and-play Android extensions for developers targeting mobile devices.
ADK for Kotlin 1.0 delivers complete alignment with ADK Python and Java, bringing advanced multi-agent coordination patterns to idiomatic Kotlin:
@Tool and @Param annotations.VertexAiSessionService, VertexAiRagMemoryService, VertexAiMemoryBankService.
Let's take ADK for Kotlin 1.0 for a spin, and build an incident triage & diagnostics agent that investigates production database alerts. Our agent will take advantage of ADK function calling and agent skill capabilities:
SkillToolset): On-demand procedural knowledge and domain playbooks loaded dynamically via progressive disclosure (SKILL.md, checklists, templates).
ADK leverages KSP (Kotlin Symbol Processing) to generate function call definitions at compile time, giving you type-safe schemas, support for suspend functions, and zero runtime reflection. [...]

## [79] Agentic Coding: Bet on the Primitives
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1592 words

Agentic Coding: Bet on the Primitives
A freelance project recently needed three custom charts: a stacked bar chart, a line chart, and a donut. Nothing exotic on paper, but each one had to match the client’s design system exactly. The spacing, the typography, the entrance animations, the way tooltips and legends behave everywhere else in the application. Recharts was already installed in the project. Past-me would have reached for it without a second thought. And here is the ironic part: I learned D3 properly years ago, and precisely because I know how much work hand-rolled charts are, I would never have budgeted them for a client. At least, that was the math before agentic coding.
The Experiment: D3 Primitives vs. Recharts
This time I ran an experiment that would have been irresponsible not long ago: I spiked both approaches within an hour. One set of chart components built on D3’s math primitives, with React rendering the SVG. And a twin set built on Recharts, with the same component API and the same design tokens, so both were interchangeable from the outside.
The result was not what I expected. The primitive version matched the design exactly, entrance animations, crosshair tooltips, legend filtering and all, without fighting anything, because there was nothing to fight. The Recharts version got 80% of the way there faster, but the last 20% required the same custom SVG code anyway: custom shapes, custom tooltips, custom labels. And then it hit a wall. Its entrance animation froze in the project’s React stack, and the only workaround was turning the animation off. The workarounds piled up on the high-level side, not the low-level one.
What an Abstraction Actually Is
That afternoon inverted a rule I had internalized over fifteen years of building for the web: never hand-roll what a library already solves. To understand why the rule is starting to crack, it helps to be precise about what a high-level library actually is.
An abstraction is encoded, prepaid implementation labor. Somebody already spent the thousands of hours it takes to make axis ticks land on round numbers, to make a tooltip follow a cursor without flickering, to make a legend toggle a series. That labor was frozen into a package you can install in seconds. You do not pay for it with money. [...]

## [135] I Think I Found an AI Agent Worth the Risk
Wired | full text via Wired | ~1126 words

One of the first things I did when I left my full-time job at WIRED was give Claude Cowork access to my email and calendar. After reporting on artificial intelligence for years, I was curious about what the technology could do for me. I had imagined Cowork as a hyper-capable digital assistant, but was let down to discover that it was more like interacting with a regular chatbot, albeit one with extra tools. What did I want it to do? I had no idea.
Then Instinct, an invite-only AI agent that communicates with users through iMessage and WhatsApp, started popping off in the Bay Area. It connects to your email, calendar, and messaging apps. Think of it as OpenClaw for normies. The company, which launched in private beta in February, is reportedly in talks to raise $1 billion on top of the $350 million it’s already raised, bringing its valuation to $10 billion, according to The Information.
Instinct’s moment in the spotlight comes as Meta is experiencing its own unexpected burst of popularity thanks to Muse, an AI assistant the tech giant launched earlier this month. As of writing, Muse is the most popular free app in Apple’s App Store, with more than 900,000 downloads, according to third-party estimates. The commentator class on X seems genuinely excited about it, despite the fact that it rolled out with a serious security vulnerability that would have “let attackers do ‘whatever’ they wanted on a victim’s Mac,” according to Ars Technica. I’m not about to give Meta a ton of my personal information, but if Muse can keep me logged into Bloomberg or unsubscribe me from Hot Yoga São Paulo, which has been emailing me once a week since 2017, I’ll reconsider.
Agent Provocateur
The divide between people who use AI agents for everything and those who have never tried one has never been wider. It explains, in part, why tech CEOs were largely caught off guard by the data center backlash. If you think agents can automate the majority of people’s administrative drudgery and turbocharge their productivity, the costs and disruptions associated with building data centers might look like an acceptable trade-off. But if you’re using chatbots as a fancy form of Google, that deal is probably much less appealing.
The overarching problem, as technology journalist Jasmine Sun writes, is that “most people’s problems are not software-shaped, and most won’t notice even when they are.” AI agents, like chatbots, still require a lot of input and direction from users. [...]

## [155] Google’s Gemini CLI now asks before editing your build files
The New Stack | full text via The New Stack | ~903 words

Google’s Gemini CLI now asks before editing your build files
The appeal of an autonomous coding agent is that you hand it a task, give it access to your repository and tools, and stay out of its way while it works. Google’s latest Gemini CLI release carves out specific moments when the agent now has to stop and wait for you.
Gemini CLI 0.61.0, released Wednesday, requires explicit confirmation before the agent edits build configuration files, runs build or test commands after such an edit, or executes shell commands whose arguments appear to come from untrusted external content. The same release separately hardens Gemini CLI’s optional sandbox so that host credentials and configuration stay out of reach of whatever runs inside it.
Giving a coding agent more authority to modify and execute code also gives an attacker more ways to turn that authority against the developer. Gemini CLI 0.61.0 puts a human back in the loop at some of those points.
Security fixes, in public
Google announced at I/O in May that it would move Gemini CLI’s Pro, Ultra, and free-tier users to its closed-source Antigravity CLI, and since June 18, the open-source tool has served mainly enterprise customers and developers with paid API keys. The company said Gemini CLI would continue to get model updates, bug fixes, and security patches. Those security changes are still developed in public, and the pull requests behind version 0.61.0 show exactly what Google was worried about.
Build files become attack vectors
A change to package.json, Makefile, pyproject.toml or a Bazel BUILD file can pull in a dependency or trigger a script. Gemini CLI can make those edits using information from web searches and external tools, then run shell commands. If documentation fetched while fixing a bug contains hidden instructions to add a postinstall script to package.json, the agent could make the edit, run the project’s test suite, and execute the malicious code without the developer ever typing the command.
Giving a coding agent more authority to modify and execute code also gives an attacker more ways to turn that authority against the developer.
Pull request #29250, titled “prevent indirect prompt injection via build file modifications and untrusted flags,” targets that sequence directly. [...]

## [72] Towards Universal Post-Training for Robotics
TLDR AI | full text via TLDR AI | ~3220 words

Towards Universal Post-Training for Robotics
People have been imagining robots working alongside humans since the dawn of storytelling. In 2026, that vision feels closer than ever. Physical Intelligence, Generalist, DeepMind, and other leading players have all shown pretrained models capable of genuinely complex tasks, to the point where the development of frontier robotics models looks a lot like that of language models in the GPT-2 days.
But complex behavior does not equal reliability. A robot that loads dishes correctly 95% of the time will break something every week in a home full of glass, pets, and kids. A pretrained generalist policy cannot be deployed autonomously to do household chores, or put to work in a factory, until its reliability sits much further out along the nines.
We have seen this play out before
In the early days of language modeling we had exactly this problem. A big pretrained model like GPT-2 or GPT-3 was fluent, knowledgeable, and completely unreliable. If you ask GPT-2 “How do I roast a whole chicken?”, you might get something like:
        I roast a whole chicken in a pot. I roast a whole chicken in a pot with a lid on it. I roast a whole chicken in a pot with a lid on it.
If you're not sure what a pot is, ask your butcher. Sometimes, when I roast meat, I roast it in a pot, which is more like a refrigerator or freezer, and I roast it in a pot that is a small freezer, or a big freezer, or larger freezer.
Why do I have to be afraid of chickens?
Because they're so adorable.
— GPT-2
Sometimes it answers the question. Sometimes it continues your question with three more questions. Sometimes it drifts into a Reddit thread it had hallucinated. While it could make for an interesting conversation, it's not something that can be deployed.
Luckily, we know exactly how this problem was solved: post-training, specifically, supervised instruction tuning, RL from human feedback, and RL with verifiable rewards, which turned “impressive demos” into “things you can actually use.”
The more important part is that the field converged on a shared for post-training language models:
- Start from a strong pretrained model.
- Define the environments and reward, i.e. verifiable or learned preference models.
- Run RL optimization with a specific family of algorithms, anchored to the reference model.
- Watch for and address known pathologies such as reward hacking. [...]

## [81] The Complete Guide to Cloudflare Quick Tunnels
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~6122 words

The complete guide to Cloudflare Quick Tunnels
By Flavio Copes
Put localhost on the internet with one cloudflared command. How quick tunnels work, what your app sees, webhooks, dev servers, local LLMs, scripts, limits and gotchas.
You have a web server running on your laptop. You want someone on the other side of the world to open it in their browser, right now, over HTTPS.
This one command does it:
cloudflared tunnel --url http://localhost:8000
A few seconds later you get a public URL like https://kingston-inside-best-graphic.trycloudflare.com. Anyone who opens it reaches the server on your machine. You don’t need an account, a DNS record or an open port on your router, and the URL disappears when you press Ctrl-C.
That is a Cloudflare Quick Tunnel. Cloudflare has offered it in this form since 2021 and a lot of developers still don’t know about it. It landed on the front page of Hacker News in September 2026 when Cloudflare gave it a new landing page at try.cloudflare.com, and a good share of the 300 comments were people finding out it existed.
We’ll start with that one command and build up to scripts, coding agents and the limits you’ll hit along the way. I ran every command in this guide on my Mac on 22 September 2026, with cloudflared 2026.9.1, and the outputs are the ones I got.
Why would you put localhost on the internet?
Your dev server listens on localhost, a name that only means something on your own machine. Your phone can’t reach it, and neither can a friend or a payment provider that wants to send you a webhook.
The old way around that is a public IP, a port forwarded on your router, a domain pointing at it and a TLS certificate. It takes an afternoon, and when you’re done your home IP is public too.
A tunnel flips the direction. Your machine opens a connection out to a server on the internet. That server gets a public hostname. When a visitor hits the hostname, the request travels back down the connection you opened and reaches your local server. Nothing is opened on your side.
Things this is good for:
- receiving webhooks from Creem, Paddle, Stripe or GitHub while you develop the handler
- opening your dev server on your phone, on a real HTTPS origin
- showing work in progress to a client or a friend without deploying
- giving a coding agent a real URL to test against
- calling a local LLM from another machine
You could do all of this with ngrok, which did it first. [...]

## [140] Meta is going to let you build games with AI right on your phone
The Verge | full text via The Verge | ~436 words

Meta has a new plan to get people to make games for its Horizon social platform. The company today announced two new development tools that will let you create games with AI prompts: Horizon Create, a mobile app, and Horizon Studio, a browser app that offers more granular controls. The apps will be available in early access, and interested users can sign up for a waitlist.
Meta is going to let you build games with AI right on your phone
The next push for Meta’s Horizon platform involves AI-generated video games.
Horizon has struggled as a platform, but Meta has a plan to give these new Horizon games significantly more reach: It’s going to let published games made with Horizon Create and Horizon Studio get recommended on Facebook and Instagram, where they also will be playable.
“Someone scrolling through Instagram can tap a clip of your game and be in a multiplayer session within seconds, without needing to download an app or being redirected,” Meta says. “Your game lives natively in the feeds where people already discover content and connect with friends.” Games that are “engaging, stable, culturally relevant, and keep players coming back” will get more reach, according to the company.
The company’s announcement comes as Roblox, a similar platform to Horizon that is vastly more popular, is also making a significant push into AI-powered development, including a feature in its mobile app that similarly allows users to generate games with a prompt.
Meta’s news about Horizon, which launched as a VR app, follows a recent pivot to primarily focus on mobile. With Meta stuffing AI into basically everything it can, it’s perhaps no surprise that AI is becoming a big part of Horizon as well.
Giving people the tools to quickly make those could give people more options for things to play. I’m pretty skeptical that a bunch of AI-generated games will be as engaging as a handcrafted experience, but the games made in Create and Studio sound as if they’ll at least have the elements of video games (unlike Google’s Project Genie, which can create brief but empty AI-generated interactive experiences). “Both enable creators to turn any idea into a complete 2D or 3D mobile game, complete with progression systems, balanced difficulty, art direction, multiplayer, and more, then refine every element to their standards,” Meta says in a blog post.
Meta also likely has a very long way to go to reach the scale of Roblox, which has 123 million daily active users. [...]

## [3] Show HN: Make cursed fonts like Times New Bastard
Hacker News | full text via Hacker News | ~231 words

A foundry for bastard web fonts. 
Mix, stretch and / or squish them.
Where can I use bastard fonts?
Every download is a normal OpenType font. The swap is a liga contextual substitution registered for every script, so browsers turn it on by default.
It works anywhere OpenType text is shaped: browsers, design tools, print. If a font looks unchanged, check that ligatures aren't switched off in the app you're using.
Are my fonts uploaded anywhere?
No. Everything runs locally in your browser with Pyodide and fontTools.
Any pro tips?
Bastardica can make simple fonts feel a little, hmm, richer? Use Y-offset and scale effects to make glyphs align perfectly.
When mixing 3 or more fonts, they will intersect (e.g. every 5th and every 7th will collide on every 35th). The first font wins. The stride won't break for either.
Use prime numbers for strides, so the mix-in fonts collide more rarely.
Some websites to grab free fonts to play with: Google Fonts, UNCUT, Velvetyne, Font Squirrel, FontSpace, DaFont.
What about font licensing?
Mixing two fonts produces a derivative work, so make sure to check licenses of both source fonts if you plan to use a bastard font commercially. Bastardica adds no conditions of its own. A credit is appreciated, but optional.
Bastardica was inspired by Times New Bastard and Easy Pete.
You can ask me about anything at [email protected]

## [156] MCP Explained in 5 Minutes
KDnuggets | full text via KDnuggets | ~1291 words

MCP Explained in 5 Minutes
A visual guide to MCP that explains how it works, how to use it with Claude Code, Tavily, GitHub, and Playwright, and what is new through simple diagrams that make the whole concept easy for anyone to understand.
Everyone has heard of MCP by now. It is constantly mentioned alongside AI agents, coding assistants, and tool use. But while most people know what MCP is supposed to do, far fewer understand how it actually works or how to use it effectively.
At a high level, MCP gives AI applications a standard way to connect with external tools and data sources. Instead of building a custom integration for every API, database, repository, or browser, an AI application can connect to an MCP server and discover the capabilities it provides.
That sounds simple, but concepts like hosts, clients, servers, tools, resources, and transports can quickly make MCP feel more complicated than it really is. Once you understand the basic flow, however, the whole system becomes much easier to reason about.
In this guide, we will break down how MCP works in about five minutes and then put it into practice by connecting Claude Code to Tavily for web search, GitHub for repository workflows, and Playwright for browser automation.
What Is MCP?
The simplest way to think about MCP is as a common language between an AI application and the tools it wants to use.
Without MCP, every external service may require its own custom integration. With MCP, the AI application can connect to different MCP servers through the same standard interface.
MCP does not replace APIs. An MCP server usually talks to the underlying API or service on behalf of the AI application. What MCP standardizes is how those capabilities are presented, discovered, and called by the AI.
An MCP server can expose three main capabilities:
- Tools: Actions the model can perform, such as searching the web, creating an issue, or running a query.
- Resources: Information the application can read, such as files, documents, or database records.
- Prompts: Reusable prompt templates or workflows exposed by the server.
For most AI agent workflows, tools are where MCP becomes especially useful, because they allow the model to move beyond generating text and actually interact with external systems.
How MCP Works
MCP follows a client-server architecture, but the flow is easier to understand when you see the pieces together.
The host is an AI application, such as Claude Code. [...]

## [187] Multiplayer AI: Why your team (and its agents) need a group chat
Stack Overflow Blog | full text via Stack Overflow Blog | ~134 words

SPONSORED BY SLACK BY SALESFORCE
In this episode, Ryan chats with the GM of Slack, Rob Seaman, about how their new Code Channels feature is bringing multiplayer AI to your team chats. They discuss how most interactions with coding agents become siloed context, why a party chat with devs and agents flattens writing code and code review into a single step, and why a Slack channel might be a better dev environment than a terminal.
Episode notes:
Check out the article Rob mentioned: Learning on the shop floor.
If you want to code multiplayer, check out Code Channels.
Connect with Rob by email at rseaman@slack-corp.com, on LinkedIn, or Twitter.
Congrats to Populist badge winner petro.sidlovskyy for dropping a great answer on What's the best way to ensure a base class's static constructor is called?.

## [16] F-Droid gets its biggest update in a decade with new UI and smoother app installs
Ars Technica | full text via Ars Technica | ~356 words

Virtually every Android device comes with the Play Store preloaded, but there are other ways to get apps. F-Droid bills itself as a community-driven source for free and open source Android apps, but its official app store has gone 10 years without a major update. That’s finally changing: After a multiyear effort, the team has just announced F-Droid 2.0 is rolling out.
The new F-Droid client was redesigned from scratch in Kotlin Compose, which is the standard for modern Android apps. This makes the store much more responsive, and there’s optional support for Android’s Material theming. The interface has also been cleaned up considerably, making the most important functions easier to access and hiding some others in overflow menus.
While the new F-Droid looks nicer, the update was largely about making it easier to find and install apps. When F-Droid first appeared, there wasn’t much to see, but now it has thousands of open source apps. Unlike the Play Store, F-Droid doesn’t track your taps and installs to push ads and suggestions—it helps you find things and gets out of the way.
F-Droid now includes a huge number of categories, drilling down to specialized niches like firewalls, password managers, and VPNs. You can see all these groups in the search tab. There are also higher-level categories listed on the main Discover page. When searching for apps, F-Droid will now be able to return results based on app descriptions rather than just names.
When you find an app, F-Droid 2.0 will make the installation process easier. Google has long put up roadblocks for sideloaded apps, citing the security implications. This is also the rationale behind its upcoming developer verification system. For now at least, apps will be easier to install from F-Droid thanks to the use of Google’s pre-approval API. Instead of downloading an APK, opening it, and confirming the scary sideloading pop-up, you’ll just be able to verify that you want to install an app before the download. So you tap “Install” in F-Droid, and then tap “Install” again in a system pop-up. That’s one more click than the Play Store, but it’s still an improvement.

## [59] Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform
Google Developers Blog | full text via Google Developers Blog | ~631 words

Each new model generation makes AI agents more capable, more autonomous, and cheaper to run. Teams are putting them to work on real business tasks: issuing refunds, updating records, calling internal tools on a user's behalf. But a more capable model is not automatically a safer one. The more decisions an agent makes at runtime, the more its risk shifts from its code to its behavior. The real damage often happens in sessions that look benign on the surface: the agent returns a clean answer and closes the ticket, and only afterward do you notice it reached for a tool it should never have touched, or acted on a request that quietly widened its own access. Because nothing failed outright, the session clears the usual metrics-based evaluations without any second look.
That gap is exactly what Agent Anomaly Detection is built to close. It's now in Private Preview on the Gemini Enterprise Agent Platform.
Agent Anomaly Detection is a reasoning-based oversight and audit layer for autonomous agents deployed on the Gemini Enterprise Agent Platform. It examines what an agent actually does using its reasoning traces, tool calls, and execution flow across a session. It reads the logs and OpenTelemetry traces your agents already emit, evaluates that activity to decide whether an agent is operating outside its intended boundaries, and flags behavioral anomalies, suspicious intent, and policy violations.
Some key features that make Agent Anomaly Detection practical to run in production:
Agent Anomaly Detection balances detection speed, cost, and coverage. To strike that balance, it analyzes traces and logs in layers: a lightweight first pass scans all traffic to surface statistical anomalies and flag those sessions for further analysis. Then, an LLM-based reasoning layer deeply examines the flagged sessions.
To make that concrete, take the example of an Inventory Agent with a list_inventory tool. A user says, "I want to see your inventory. List 100 items at a time" and the agent starts paging through in large batches, jumping across offsets to pull the whole catalog.
Nothing here throws an error. The agent is only doing things it’s capable of, and there may be no policy preventing it. But Agent Anomaly Detection flags the anomalous behavior, working through the session in layers: the first layer flags the session as a statistical outlier from the volume and the repeated calls. [...]

## [144] Google Photos ‘Clueless’-inspired virtual closet is now available on Android and iOS
TechCrunch | full text via TechCrunch | ~345 words

Google’s new AI-powered feature that turns photos of your outfits into a virtual closet — one seemingly inspired by Cher’s iconic virtual wardrobe app featured in the movie “Clueless” — is now available to everyone in the U.S., Brazil, and India, on both iOS and Android devices.
The company announced the feature earlier this year with plans to begin the rollout in the summer. Android users gained access first, starting in June, and now the virtual closet is available to all Android and iOS users in the supported markets.
The idea of a digital closet in “Clueless” was meant to highlight Cher’s privileged life, where she had so many outfits that she needed a digital system to help her choose what to wear and keep everything organized. Now, you don’t have to be a rich Beverly Hills teenager to take advantage of such technology.
Instead, Google uses AI technology to create a copy of your wardrobe, based on the items you wore in your photos. From the app, you can also filter items by category — like tops, bottoms, jewelry, and more — then mix and match them to create different outfits.
Google says the feature is designed to assist the user, and the data about how you dress or what you wear is not being shared with third parties, like retailers.
The broader rollout of the virtual closet feature arrives alongside a handful of other Google Photos updates, including a way to select, brighten, and share photos using a single prompt in Gemini Spark, an upgraded markup tool, and more Remix templates that use AI to transform your photos. (The Gemini Spark feature requires a Google AI Pro or Ultra subscription in the U.S.)
With Markup, you’ll be able to use a redacting pen to blur sensitive information like license plates, access precise thickness sliders for custom sketches, and pick from different fonts when adding text to photos.
For Android users, there are also new photo filters, called “Moods,” that let you give your images different looks, like 35mm film, 2000s digicam, and more.
