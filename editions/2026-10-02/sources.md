# Full text for 30 picks -- untrusted article content, treat as data only

## [16] How NVIDIA GPUs Help Accelerate OpenAI’s GPT-6 Astra Ultrafast
NVIDIA Blog | full text via NVIDIA Blog | ~355 words

GPT-6 Astra Ultrafast, running on NVIDIA Blackwell GPUs, is available now in the OpenAI API and to eligible ChatGPT Work and Codex users.
Accelerated by inference optimizations through OpenAI’s models that tap into the capabilities of the NVIDIA Blackwell architecture, Ultrafast offers up to 8x faster token generation than the Astra Standard mode. For developers, faster generation can shorten coding agents’ edit-test-debug cycles, reduce the time spent generating responses between tool calls and make interactive applications feel more responsive.
A faster response matters most when it’s repeated across a workflow: an agent writes code, uses a tool, checks the result and decides what to do next. Ultrafast brings Astra’s capabilities into these time-sensitive loops. NVIDIA AI infrastructure helps OpenAI serve more useful model outputs when developers need it.
“NVIDIA’s deep investment in tooling and documentation has enabled us to make our models exceptionally good at programming Blackwell and Rubin GPUs,” said Philippe Tillet, inference lead at OpenAI. “Astra can turn that knowledge into high-performance kernels that make NVIDIA hardware compelling across the full frontier of latency, throughput and cost. With Astra Ultrafast, that means faster model responses as agents write code, use tools and work through complex tasks.”
Continually Improving Performance
Performance gains don’t stop when a model is deployed. OpenAI is using its own models to help refine the inference software running on NVIDIA GPUs, taking advantage of the platform’s programmability to test and implement improvements. That ongoing work can make model responses faster and deployed infrastructure more productive over time.
“Our work with NVIDIA is helping us make AI faster and more useful,” said Uday Ruddarraju, chief technology officer of compute at OpenAI. “We used our internal models to optimize inference on NVIDIA GPUs, and NVIDIA’s programmability helped us deliver the acceleration behind Astra Ultrafast.”
A programmable NVIDIA platform allows developers and researchers to reuse infrastructure across training, inference and reinforcement learning as models evolve. That flexibility helps teams repurpose compute resources as demand changes, improving utilization and avoiding overprovision for each workload.
Developers can use GPT-6 Astra Ultrafast through the API today. See the Ultrafast guide for access, pricing and implementation details.

## [19] Hacks of 2 federal agencies in a month have spilled a bonanza of sensitive data
Ars Technica | full text via Ars Technica | ~252 words

The Pentagon is informing more than 2 million current and former military members that their personnel records storing sensitive personal information were stolen over a monthslong compromise of one of its networks. The breach is the second one in recent months to expose sensitive government information.
The records, according to one notification letter posted to Reddit, included Social Security numbers, names, addresses, sex, race, and occupational specialty. This last category could be particularly valuable to foreign adversaries because it could help their intelligence agencies in identifying high-value military personnel. Starting last October, hackers gained access to a system operated by the Defense Manpower Data Center, which collates Department of Defense personnel records. The Pentagon says that the breach compromised the records of 2.8 million living individuals.
A potential boon
The incident is the second time a major network breach in recent months has exposed sensitive US government personnel records that criminal groups or foreign adversaries could use. Last month, the ransomware group ShinyHunters claimed it hacked into FBI systems and stole records of thousands of the agency’s current or former employees. Reuters reported the job titles in the records included ones related to investigating China or Russia.
ShinyHunters said that it has no plans to release the information, but the promises of a criminal organization that has hacked and extorted hundreds of organizations mean very little. Additionally, the group’s cyber defenses are likely no match against nation-state intelligence hackers. An FBI official this week called on group members to turn themselves in.

## [90] Gemini 4 Argon: our next era of frontier intelligence
Google DeepMind Blog | full text via Google DeepMind Blog | ~1391 words

Gemini 4 Argon: our next era of frontier intelligence
Today, we’re announcing our new frontier model, Gemini 4 Argon, which is rolling out to a set of trusted cyber defenders through our Fairwind Program. Built to sustain deep reasoning across complex, long-horizon workflows, Argon is fundamentally changing the way we work and build at Google. It delivers frontier performance in complex workflows across real-world software engineering, enterprise knowledge work like legal and finance, and cybersecurity defense.
Safely releasing frontier capabilities at this level requires a phased approach. We are actively engaged in the U.S. government’s voluntary process for pre-release model access while we gradually expand access. We’ll continue to gather feedback from early testers as we iterate on guardrails before making Argon available to developers, enterprises, and consumers as soon as possible.
Argon will launch at an introductory price 1 of $2 per million input tokens and $10 per million output tokens, with cached input tokens priced at 95% off input token price.
Changing how we work and build at Google
Gemini 4 Argon is already powering our internal workflows, with thousands of Googlers highlighting the model’s strengths in specialized coding tasks, conducting deeper research, and writing quality. It’s helping teams build faster and push the boundaries of engineering productivity and accelerating breakthroughs:
- Quantum algorithmic optimization: Argon is helping our quantum computing researchers optimize the spacetime resources (qubits × gates) of subroutines that bottleneck important applications. In one example, it beat the published baseline by 40% in a matter of minutes.
- Memory efficiency: A team of Argon agents analyzed fleet-wide profiling telemetry to autonomously identify and apply memory optimizations across Google’s data centers, freeing up over 300 TiB of memory once rolled out, with an estimated 500 TiB to 1 PiB in total savings.
- Large Scale Codebase Migrations and Optimizations: Argon agents are working on migrating C/C++ codebases to Rust across Google — scaling from tens of thousands of lines in core libraries like re2, libgav1 up to 800K+ lines for the Fuchsia Zircon kernel. Given the criticality of many of these systems, such large-scale rewrites are undergoing rigorous automated and manual auditing, emulation testing, and review before rolling out to production. [...]

## [1] Clef: Open-weight decision models, and new RL fine-tuning platform
Hacker News | full text via Hacker News | ~2101 words

Introducing Clef: our open-source decision models, and new RL fine-tuning platform
Over the last few weeks, there has been lots of buzz around decision models such as Typesafe AI’s Jev System One model. While classifier models have been around for some time, Jev introduces a new decision model concept into the world of AI — a model that produces bounded structured outputs cheaply, quickly and consistently that can be added into a workflow when a decision is required. These models are capable enough to work over any set of inputs without constantly retraining the model to incorporate new classification categories. This contrasts with the world of Large Language Models (LLMs), which are largely non-deterministic, but are open-ended enough to reason and generate text and tool calls for agentic workloads.
Today, we’re releasing two Cloudflare-trained decision models, Clef and Clef-flash, hosted on Workers AI. Clef is currently the leader when evaluated against the Jev Decision Index, you can view full results on the live benchmark demo site. These models are smarter, faster, and fully Jev-API compatible, so you can experiment with these hosted models easily. We’re fully open-sourcing these models on Hugging Face under an Apache 2.0 license for you to run locally and experiment with yourselves.
Lastly, we’re excited to debut our new reinforcement learning (RL) product, which allows customers to fine-tune Clef to suit their use cases as well.
What is a decision model?
A decision model makes classifications to help agents decide how to act, based on certain probabilities. For example, you can pass in a customer support message (inputs) and ask if it is urgent and which team should handle it. A decision model will return typed answers with probabilities (outputs), which your code can use to route the ticket, trigger an escalation, or defer to a human. This means that a human does not necessarily need to be in the loop for agentic decisions anymore — agents can programmatically gather context, make decisions, and take actions on tasks, or defer to a human when needed.
Specifically at Cloudflare, we’ve been testing our new Clef model on our Threat Intelligence team to help us classify website domains. By giving a domain to Clef (with Browser Run) it can quickly identify categories that the domain falls under — for example, it might classify a domain with a 95% chance it is a fashion website, 85% ecommerce, <1% phishing, etc. [...]

## [71] Claude for Government is now generally available
TLDR AI | full text via TLDR AI | ~473 words

Claude for Government is now generally available
Claude Code CLI and Claude for Microsoft 365 also now available in early access.
Today, Claude for Government is generally available for federal and state agencies. The platform, which delivers Claude's coding and agentic work capabilities through a FedRAMP High authorized environment, has been in public beta since July.
Agencies access capabilities comparable to Anthropic’s commercial customers, without compromising compliance requirements. New capabilities generally arrive on the commercial release cadence.
Claude works directly with files on the desktop, allowing agency staff to use skills, plugins and projects for memo creation, RFP reviews, casework, and other tasks. With Claude Code, public sector teams can build and modernize the software systems that underpin public services.
Claude for Government governance controls are purpose-built for public sector agencies. Administrators can set configuration defaults as well as allocate and control spending across departments. Security teams and authorizing officials get audit logs and documentation that supports the agency ATO process. Procurement officers can contract with Anthropic directly and award on general-availability terms.
The Claude Code command-line interface and Claude for Microsoft 365 are also rolling out in early access through the same environment and with the same administrative controls.
No seat fees. Agencies pay for usage in fixed increments with a hard not-to-exceed cap, so spend does not exceed what an agency has obligated. Administrators define user tiers with spend and model limits per group, track usage by user and by model, and get burndown alerts before a balance runs low.
Administration that matches how departments are organized. Department-level administrators allocate prepaid usage to sub-agencies while each manages its own users. Agencies connect their own identity provider for single sign-on, with self-serve setup in the admin portal. SCIM group mappings set rate limits, dollar caps, and allowed models for each seat tier. Layered configuration sets defaults for sub-agencies, including what Claude can connect to and which features are available.
Oversight by design. Administrative actions are recorded in an audit log that organization administrators can review. Sensitive operations on Anthropic's side require two-person approval. [...]

## [125] Kevin Mandia’s new ‘agent swarm’ security startup Armadin raises $255.5M at $2.5B valuation
TechCrunch | full text via TechCrunch | ~172 words

Kevin Mandia, best known as the founder of cybersecurity startup Mandiant, which sold to Google for $5.4 billion in 2022, has raised $255.5 million for his latest startup, Armadin, at a valuation of more than $2.5 billion, the company announced on Thursday.
The Series B round was led by Andreessen Horowitz and Accel, with Bain Capital Ventures, Redpoint, 8VC, Ballistic Ventures, Google Ventures, In-Q-Tel, Kleiner Perkins, and Menlo Ventures joining in.
The new round comes just six months after Armadin raised a $190 million Series A in March. It has now raised more than $445 million.
Armadin is offering enterprises a new kind of always-on security by reimagining defense testing for the AI era. Instead of traditional penetration tests, where hired guns attempt to break in and report on the weaknesses they find, Armadin runs always-on agentic swarms, who chain together vulnerabilities to hack in. The idea is to help organizations find and seal holes before any bad guys (or even AI labs with rogue agents) can use agentic tech against them.

## [8] Cloudflare K2: serverless event streams
Hacker News | full text via Hacker News | ~1558 words

Announcing Cloudflare K2: serverless event streams
With traditional Remote Procedure Call (RPC) architectures, there exists a core challenge: producers and consumers must align in scale and in time. If your producers send too much data for your consumers to handle or if your consumers or downstream services become unavailable, events are dropped. This problem is compounded with multiple consumers that need to independently process the data. For example, an ecommerce backend may emit events when transactions are completed, which need to be read by an analytics system and a fraud detection service.
We can solve this by decoupling our producers and consumers — inserting a service in the middle that absorbs writes while allowing independent readers to consume at their own pace.
Today we are launching Cloudflare K2 in public beta to solve this problem. K2 is a durable event streaming primitive on the Developer Platform. You send events to a K2 stream, which stores them as an ordered log. Consumers can read them in a variety of ways, for example by splitting up reads across a set of consumers, or delivering all messages to all consumers. It's fully serverless, scales to vast quantities of data, and supports long-term retention, so even long periods of consumer downtime do not lose data.
Under the hood, K2 implements a partitioned, durable log on top of R2 object storage, which allows it to scale to huge volumes of storage.
If you’re ready to get started, you can create your first stream in seconds by following the guide here.
Streams on the edge
We first built K2 because we needed a durable buffer on the edge, initially to serve as the ingestion layer for Basin Pipelines. Pipelines is powered by a stream processing engine that operates on a pull-based model, which means some other system has to store events before they are read, transformed, and written to R2. And because we commit to never dropping events once they’re accepted into the Pipelines Stream, that storage has to be durable — meaning it can’t lose data — over potentially long periods of time.
This is where most companies would deploy Apache Kafka. However, Pipelines runs on the Cloudflare edge, which spans a huge number of servers across over 335 cities. Our unique architecture means we often cannot run traditional distributed systems software like Kafka, and need to rethink how these systems are built and operated. [...]

## [49] Qualcomm Unveils Linux Preview on Snapdragon X2 to Accelerate Upstream ARM Laptops
InfoQ | full text via InfoQ | ~614 words

Qualcomm has announced an early developer preview of Linux running on its upcoming Snapdragon X2 Series laptop processors. Revealed alongside demonstrations at Snapdragon Summit, the initiative signals a deliberate shift toward upstream-first enablement for client ARM hardware, targeting kernel contributors, toolchain developers, and distribution maintainers rather than general consumers looking for turnkey desktop installations.
By targeting mainline Linux kernel integration ahead of commercial OEM availability, Qualcomm aims to resolve the systemic software friction that historically plagued ARM laptop rollouts: heavy reliance on out-of-tree vendor patches, broken display drivers, and incomplete power management. The preview establishes a functional Debian 13 "Trixie" reference environment that validates boot paths, core system buses, graphics stacks, and neural processing units on reference hardware.
The software architecture of the Snapdragon X2 Linux stack centers on standardizing low-level system initialization and offloading compute tasks to hardware subsystems using standard open-source interfaces. System boot utilizes standard Unified Extensible Firmware Interface (UEFI) firmware handoffs into systemd-boot, avoiding custom vendor bootloader semantics and ensuring parity with standard x86 and ARM server execution paths.
Core input and output subsystems rely on upstream drivers for Qualcomm Universal Peripheral serial engines, bringing support for UART, I2C, and SPI, alongside high-speed PCI Express and USB fabrics. For graphics and desktop composition, Qualcomm is collaborating with open-source graphics maintainers to integrate display pipelines into Mesa via the Freedreno Kernel Mode Setting driver, Turnip for Vulkan support, and Rusticl for OpenCL compute.
Hardware-accelerated machine learning workloads bypass proprietary vendor daemons by relying on the upstream FastRPC driver subsystem, exposing the Hexagon Neural Processing Unit to userspace frameworks for local inference without out-of-tree kernel modules. [...]

## [58] WSL containers are now generally available
Lobsters | full text via Lobsters | ~1048 words

WSL containers is now generally available
WSL is central to our commitment to making Windows the best place to build, run and manage Linux workloads. As AI, cloud-native development, containers, and open-source ecosystems continue to converge on Linux, more developers are choosing to perform these workloads directly on Windows devices. We’re continuing our journey towards this goal with a new feature in WSL: WSL containers, which is generally available today.
To try it out,  simply runwsl --update in your terminal or download the latest release from GitHub and you will gain access to:
- WSL containers CLI: wslc.exe to directly build, run and deploy Linux containers on Windows, or use its built-in aliascontainer.exe to run the same familiar container commands
- WSL containers API: Access functions to run Linux containers programmatically in your native Windows apps – unlocking scenarios like running local AI workloads or using cloud-based containerized applications locally.
For a deeper look at how WSL containers are built, how they work with WSL, and the architecture behind the platform, see our WSL containers architecture blog.
Let’s get into what’s new with GA.
New commands and capabilities
Since public preview, we’ve continued to evolve WSL containers and our focus has been on making every day container workflows simpler, improving visibility into running environments, and adding the flexibility needed to manage containers at scale. As part of the GA release, we’ve introduced several new commands and capabilities across container lifecycle, networking, and observability.
Here are a few highlights, and you can view the full change logs on our releases page:
- wslc container restart — restart a running container
- wslc container cp — copy files in and out via tar archive
- wslc system info — see the state of your container environment at a glance
- wslc network connect andwslc network disconnect — attach and detach containers from networks
- wslc network create now supports arbitrary network driver options
- wslc events – Streams real time container activity
- Container health checks are now supported
- --stop-timeout onwslc create andwslc run , including-1 for an infinite timeout
- --mount support duringwslc create andwslc run
- A configurable storage path for the default wslc session, so you can put your container storage on the drive you want. [...]

## [53] Announcing Rust 1.99.0
Lobsters | full text via Lobsters | ~441 words

The Rust team is happy to announce a new version of Rust, 1.99.0. Rust is a programming language empowering everyone to build reliable and efficient software.
If you have a previous version of Rust installed via rustup, you can get 1.99.0 with:
$ rustup update stable
If you don't have it already, you can get rustup from the appropriate page on our website, and check out the detailed release notes for 1.99.0.
If you'd like to help us out by testing future releases, you might consider updating locally to use the beta channel (rustup default beta) or the nightly channel (rustup default nightly). Please report any bugs you might come across!
What's in 1.99.0 stable
extern "C" variadics
Rust 1.99.0 stabilizes defining C-ABI variadic functions with "C" and
"C-unwind" ABIs. Variadic functions defined this way use a variable argument
list (...) and accept an arbitrary number of arguments. Rust could already
call externally-defined variadic functions (e.g., libc::printf). With Rust
1.99, these functions can now be written in Rust itself:
/// SAFETY: must be called with (at least) 2 i32 arguments.
unsafe extern "C" fn sum(mut args: ...) -> i32 {
    // SAFETY: guaranteed by the caller.
    let a = unsafe { args.next_arg::<i32>() };
    let b = unsafe { args.next_arg::<i32>() };
    a + b
}
fn foo() -> i32 {
    unsafe { sum(0i32, 2i32) }
}
The type of ... is VaList,
which is ABI-compatible with the C va_list type across targets. What types can be read from a VaList is guarded by the
VaArgSafe trait.
For more details on c-variadic functions, see the Reference. This release also stabilizes support for defining naked variadic functions with non-"C" ABIs, which must be written via inline assembly.
Layout information from raw pointers
This release settles the safety requirements for retrieving the size and
alignment on raw pointers to both Sized (trivially safe, already possible on
stable) and non-Sized types.
This is done by stabilizing three functions:
Recommend against round-trip unleaking after Box::leak
While there are no changes to the language semantics in Rust 1.99, we have
updated the documentation on Box::leak to recommend against patterns that
later deallocate that memory. This was done because such code was found to have
problematic interactions with current and future potential compiler optimizations,
and is especially problematic with the upcoming stabilization of custom allocators.
Instead, Box::into_non_null or Box::into_raw should be preferred. [...]

## [87] How I Could've Accessed 17 Trillion Microsoft Records
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2051 words

How I Could've Accessed 17 Trillion Microsoft Records
An estimated 17.3 trillion stored rows across a wide range of Microsoft datasets were reachable through a single internal analytics service, all because it never checked the signature on a login token. That flaw let me claim an administrator’s identity and submit unauthorized SQL queries without any real credentials. I used only table descriptions, metadata, and bounded sample rows to understand the potential scope.
Two quick notes first. The impact I describe is hypothetical. It’s what an attacker could have done with this access, but luckily I found the bug instead, reported it, and never touched any customer data or PII. And for transparency: Microsoft had editorial control over this post, cutting sections and figures and reshaping how the impact is described before publication.
Microsoft said the following about this finding:
  “We appreciate the opportunity to investigate the findings reported by Faav. Their submission and coordinated vulnerability disclosure helped us to better protect our customers by hardening our services. We value and appreciate safe security research under the terms of the Microsoft Bug Bounty Program and look forward to continuing to work with Faav in the future.”
Hey! I’m Faav. A little over a year ago, when I was 15, I published Break into any Microsoft building: Leaking PII in Microsoft Guest Check-In, my first Microsoft write-up. I’m 16 now, and this one is a little bigger.
Since then I’ve gone all-in on bug bounty. I’ve spent the year hacking Microsoft off and on around school, and finding bugs across Amazon, Google, Adobe, and a bunch of other companies. I also started building AI into how I hunt, which led me to develop Antares, my personal AI hackbot.
This one started as an automated lead that Antares couldn’t finish. Ten days later, after a Friday of schoolwork and one late-night hunch, it turned into the biggest Microsoft bug I’d ever found.
Finding the Titan API
On August 25, 2026, Antares identified an internal Microsoft service called Titan. Its web interface sat behind a VPN REQUIRED page for Microsoft employees, so the frontend was out of reach. But since when has a locked front door stopped anyone?
The “VPN REQUIRED” page shown to a non-employee visiting Titan’s frontend.
The API wasn’t linked anywhere on the frontend, so Antares searched Microsoft subdomains and found a separate endpoint that resolved to an Azure Cloud Services host. [...]

## [11] Judge dismisses Chegg and Penske antitrust lawsuits targeting Google AI search
Ars Technica | full text via Ars Technica | ~273 words

In a setback for publishers worried about the effects of AI search, a US federal judge has dismissed lawsuits filed by Chegg and Penske Media against Google. The companies accused Google of antitrust violations in products like AI overviews, which have led to decreasing traffic at numerous sites. However, US District Judge Amit Mehta has ruled that Google’s conduct is not illegal under antitrust law.
The lawsuits were filed in 2025, and Google requested a dismissal earlier this year. Chegg, an education and learning platform, claimed in its lawsuit that Google illegally scraped its educational content. This allowed Gemini models to essentially recreate that content and reduce the site’s traffic. Penske, which owns publications like Rolling Stone and Variety, filed a similar case that alleged lost traffic. Specifically, the publisher claimed it was unfair that sites indexed for organic search would also have their content harvested for AI answers, with no way to opt out.
These arguments did not sway the judge, who noted that Google’s implicit agreement with websites is not legally relevant. “Plaintiffs have pleaded only that they have an ‘expectation’ that Google will send them search traffic if they make their content available for free,” wrote Mehta. “But an expectation is not an agreement. It is simply how a general search engine works.”
Since Google never had a formal arrangement with either Chegg or Penske, antitrust law doesn’t apply. And Mehta is aware of the legal issues surrounding search. He also heard the DOJ’s long-running search antitrust case against Google, eventually finding that Google violated the law. However, the government didn’t get the harsh penalties it wanted in that case.

## [7] Git 3.0's upcoming SHA-256 default will be a costly mistake
Hacker News | full text via Hacker News | ~3871 words

Where to begin?
I've been sitting on this for a few years, mostly because there are smarter people who have been concentrating on this and I don't love being a back seat driver. However, I think that the Git 3.0 release is about to cost everyone a lot of time and angst for little benefit, and virtually nobody knows what's coming.
So grab some popcorn and let me tell you a tale of how one of the new upcoming Git 3.0 breaking changes is about to be a huge, costly, global train wreck of a change for almost no practical value.
SHA-1 in Git Primer
I'll keep this short as many of you probably know this at a basic level.
Git is what's known as a content addressable database. This means that if you want to store and transmit data in it, Git will calculate a hash of the contents and use that in a key/value database as the key (the value being the content). The same content always gets the same hash, globally.
This is nice, because it means that the same file content is never stored twice. There is also a cool property where commits encode the hash of the commit that came before it, which means that this integrity essentially propagates - you can't change the hash of anything without changing the hash of everything that comes after it. This gives it "cryptographic integrity", meaning that hashing the latest commit essentially also hashes potentially millions of file contents, trees and commits that came before it.
In Git, this hash function has always been SHA-1. This was what Linus picked in 2005 when Git was started and it's worked pretty well for 20 years - it's relatively fast and impossible in a practical sense for two different files to accidentally hash to the same value.
In fact, as far as I'm aware, this has never happened in the history of every file, tree and commit ever made in Git in every repository ever created - billions and billions of them.
Mathematically, for SHA-1’s 160-bit output, the birthday bound means that you would need about 1.4 septillion random files (1.4 quadrillion billion files - 1,400,000,000,000,000 billion - it's impossible to effectively describe) in a single project to have file hashes accidentally collide.
SHA-1 is Broken
There is a problem though, which is that mathematically, SHA-1 is now considered semi-"broken" because there have been published collision attacks (SHAttered in 2017, SHA-1 is a Shambles in 2020) - not really practical to exploit in any demonstrated way, but now theoretically possible. [...]

## [20] Announcing AWS Well-Architected Agent, an AI-powered intelligence to optimize your cloud environment (preview)
AWS News Blog | full text via AWS News Blog | ~947 words

AWS News Blog
Announcing AWS Well-Architected Agent, an AI-powered intelligence to optimize your cloud environment (preview)
Today, we’re announcing the public preview of AWS Well-Architected Agent, an AI-powered service that analyzes your AWS environment to deliver targeted, contextual recommendations for improving your applications’ cost, security, performance, and resilience. The AWS Well-Architected Agent analyzes your infrastructure, understands unique business goals, and delivers contextual recommendations with ready-to-implement fixes. It delivers context-aware optimization without relying on manual audits or generic checklists.
The agent evaluates your environment as an experienced cloud architect would. It automatically correlates utilization metrics, resource configurations, and application topology, and analyzes against Well-Architected best practices across 65+ AWS services. It generates recommendations aligned to your declared business goals, delivers implementation packages with every finding, and surfaces cross-pillar trade-offs making it simpler to remediate the findings.
Here are the three main features of this service:
- Goal-aligned intelligence: AWS Well-Architected Agent replaces flat, undifferentiated findings with context-aware, prioritized recommendations. You declare your business objectives and share your application context. The agent automatically generates and prioritizes recommendations by impact and effort against those goals.
- Three-level recommendations: AWS Well-Architected Agent provides individual resource findings with specific dollar impact (where applicable) and step-by-step remediation, consolidated findings across multiple resources scoped to your application, and broad architectural patterns and designs with Infrastructure as Code (IaC) code changes needed to align with Well-Architected best practices.
- Optionality in remediation: You can choose your path on how you want to remediate with a complete implementation steps tailored to your environment: the console walk-throughs, updated IaC changes for architecture-level recommendations, and AWS Command Line Interface (AWS CLI) commands.
AWS Well-Architected Agent in action 
         To get started, create an agent profile to define the scope of what Well-Architected Agent can access and provide recommendations on, complete the IAM role setup to access resources, conduct architecture review, and remediate recommendations. [...]

## [166] AWS launches a local answer to TypeSafe’s Jev decision model
The New Stack | full text via The New Stack | ~723 words

AWS launches a local answer to TypeSafe’s Jev decision model
AWS on Thursday launched Strands Decider 2B, its take on decision models like Jev, Kev, imajev, Laya, and others.
TypeSafe’s Jev kicked off the current wave of decision models a few weeks ago, and the major AI vendors are now bringing out their own versions.
OpenAI on Tuesday, for example, launched its Decisions API as a limited preview. But that’s a hosted API that focuses its Luna model on questions with predefined answers, while AWS is releasing a downloadable model along with the data and scripts used to train it.
How Strands Decider works
Decision models trade free-form text generation for selecting from developer-supplied options or returning numerical scores. That makes them useful for routing natural language requests, selecting tools, evaluating outputs, and checking proposed actions, while leaving conversation and more complex work to generative models.
Strands Decider uses Qwen3.5-2B as its language-understanding base model, which AWS calls the “torso.” The team then removed the language-model head that generates text and replaced it with a pointer head that scores the supplied answer options.
That head has just over a million parameters, and the backbone uses a rank-16 LoRA (low-rank adaptation) adapter.
Restricting the answer space prevents the model from inventing an option that wasn’t supplied, but that still doesn’t mean it will always answer correctly. That’s a minor tradeoff, though, since LLMs aren’t always right either. In return, developers get faster decisions and confidence scores they can use to make decisions.
Checking an agent before it acts
In AWS’s example, built with the company’s open-source Strands agent framework, a user asks for the weather without saying where, and the agent guesses a city and proposes calling a weather tool.
Before that tool runs, Decider checks whether the argument values are grounded in the conversation and whether the agent has enough information to proceed. The application then sends the agent back to ask which city the user meant.
The check then runs through Strands’ intervention system, which lets developers choose whether they want to proceed with a tool call, deny it, request human confirmation, or return feedback to the agent.
In this demo, Decider runs locally while the agent calls its generative model through Amazon Bedrock. AWS says it’s also working on decision-model integration libraries. [...]

## [65] TypeSafe AI Releases Jev: A Decision-Only Model That Returns Typed Probabilities Instead of Text
InfoQ | full text via InfoQ | ~628 words

TypeSafe AI, a San Francisco lab founded by former OpenAI researcher Diogo Almeida, has released Jev, the first of what it calls System One Models. Jev does not generate text. It returns typed, probabilistic decisions that software can act on directly.
A caller sends a state, either a string or structured data, together with a set of typed questions. Jev evaluates them all in a single parallel pass and returns Choice, Score and Noul answers with a probability distribution and a confidence value, so calling code can act above a threshold and escalate below it. Input costs $0.042 per million tokens, output is free, the context window is 32,000 tokens, and TypeSafe quotes end to end latency of 70ms to 500ms. Training uses a method it calls Reinforcement Learning for Calibrated Decisions.
Vercel, which added Jev to AI Gateway on day two, said it reached nearly 13% of paid teams within 24 hours, twice the share of the GPT-5.6 family. Netlify followed, LangChain shipped a TypeSafeClassifier integration with model routing and an AutoMode middleware that screens tool calls before they run, and five independent Elixir clients appeared within days.
First day adoption of Jev on Vercel AI Gateway compared with other recent model launches. Credit: Vercel
Vercel engineer Pranit Sharma found a safety classifier ran five to 18 times faster than the LLM it replaced, while Bryo AI CTO Nikhil Mudholkar rated Gemini slightly more accurate on email classification but 10 to 20 times more expensive, and valued Jev as the only one handing back a real probability. Armin Ronacher, CTO of Earendil, told TechCrunch the design "delegates the hallucination problem a little bit to the user", who has to decide whether a 50% probability is worth acting on, and pointed to model routing as another good fit. An analysis of 12,759 launch tweets by OpenChamber put user reported speedups at a median of 7x against the 193.6x headline, cost savings at a median of 30x, and latency at a median of 76ms with an upper quartile of 270ms.
One developer on Reddit called the model "absolutely insane" for agent work at 200ms to 300ms latency, and an early access user on Hacker News called it "really neat" while cautioning that its out of distribution behaviour will differ from an LLM.
On Hacker News, one developer noted that Jev cannot emit an invalid type but can still emit a completely wrong valid value:
First, congrats to the team on launching something genuinely interesting and new. [...]

## [75] NVIDIA OpenShell Secures Autonomous AI Agents (GitHub Repo)
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~34 words

NVIDIA's OpenShell provides a policy-controlled runtime for autonomous agents, enforcing file, system-call, network, and credential access at the kernel level. It also uses formal verification to identify risky permissions before policy changes are applied.

## [142] Google thinks SpaceX’s Starship has to launch 1,800 times before space data centers get off the ground
TechCrunch | full text via TechCrunch | ~770 words

Google’s prototype of its orbital compute satellite took off today onboard a SpaceX rocket launched from California — the first time the tech giant has sent one of its advanced chips into space.
Built by Planet Labs, the satellite will prove that a Google Tensor Processing Unit, its competitor to Nvidia’s GPUs, can function in space. That means supplying a kilowatt of continuous power, cooling the chip, and running a series of models through their paces to see if anything goes wrong.
“We’ve done testing on the ground, but you know, there’s no test that’s completely as good as the real thing,” said Travis Beals, the Google executive managing Project Suncatcher, the tech giant’s plan to develop large-scale compute clusters in orbit around the Earth.
Once commissioned, the satellite will fire up its TPU in 15-minute bursts to avoid straining the satellite’s power and thermal management systems. This satellite is based on a standard platform built by Planet Labs, but the two companies are working on a demo expected to take flight next year that will see two satellites more purpose-built for advanced compute that can run more substantial workloads. Those future versions will attempt to collaborate via a laser communications link.
Suncatcher isn’t the only space AI payload on this SpaceX rocket, which is launching more than 100 different payloads, including missions from Satlyt and Cowboy Space Company.
What sets the Google initiative apart from those startups (and indeed from SpaceX itself) is that it’s a long-term project.
The focus of this “long-term moonshot,” as Beals puts it, is on building for the space infrastructure and AI workloads that will exist in the future. The company envisions an orbital data center that is a network of 81 satellites flying in close formation, processing in parallel.
“The bandwidth and the latency between TPUs really, really matters when you’re trying to run a multi-rack workload…we’re trying to look ahead to not just what workloads exist today, but where they will be in five years,” Beals said. That’s largely because the rockets required to scale up orbital data centers in a cost-effective way don’t yet exist.
On Thursday, Google also released a peer-reviewed version of its white paper on orbital data centers, one of the most rigorous analyses available of how compute gets to orbit. The paper will be published in Joule.
One of the paper’s most notable aspects is how Google thinks about access to space. [...]

## [143] World’s first enhanced geothermal power plant completed in just 23 months
TechCrunch | full text via TechCrunch | ~321 words

Geothermal company Fervo Energy announced Thursday morning that it had started selling electricity from its Cape Station power plant to the grid on September 30, one day ahead of schedule.
With it, Fervo becomes the first enhanced geothermal company to reach a key commercial milestone. The power plant synchronized with the grid about a week ago, bringing online the first third of what will soon become a 100-megawatt power plant.
The entire site could be much larger, though, with the potential to generate as much as 4 gigawatts of electricity, Fervo previously told TechCrunch.
“No team has ever built a project like this anywhere in the world, and we did it ahead of schedule,” Fervo co-founder and CEO Tim Latimer said in a statement.
From groundbreaking to commercial operations, the first block at Cape Station took 23 months to complete. As Fervo refines its process, it is aiming to complete future blocks in as little as 18 months.
That sort of speed to power should appeal to power-starved data center operators, who have been scouring every part of the energy sector for generating capacity. Geothermal can also be developed in phases, similar to how data centers are developed, allowing hyperscalers to bring racks online as demand ramps up.
Google, Southern California Edison, and others have committed to buying power from Fervo’s Cape Station project.
Fervo is one of several companies developing enhanced geothermal power plants. While traditional geothermal power taps heat sources close to the surface, Fervo and its peers are drilling deeper because deeper rock is hotter, opening more opportunities for development.
Fervo went public in May in an upsized IPO that raised $1.9 billion. It was founded in 2017, bringing drilling techniques and technologies from the oil and gas sector to the development of new geothermal resources. As a startup, the company raised more than $1.3 billion from investors, including Breakthrough Energy Ventures, Congruent Ventures, and Capricorn Investment Group.

## [112] Robotaxi operators will face fines for blocking first responders
TechCrunch | full text via TechCrunch | ~629 words

Autonomous vehicle (AV) technology companies like Tesla, Waymo, and Zoox will have to provide first responders with local, on-the-ground support when their robotaxis cause problems under a new California law. The companies could also face penalties if a robotaxi blocks police or firefighters for more than 30 minutes.
Senate Bill 1246, which was signed into law by Gov. Gavin Newsom, sets a series of new rules for AVs designed to improve safety and response times when they become disabled or interfere with emergency responders. The law also creates ways to hold these companies accountable if they don’t.
The law follows a string of high-profile incidents in California in which robotaxis broke down and disrupted traffic, drove into crime scenes, or impeded first responders.
The bulk of those incidents involved Waymo, the largest robotaxi operator in the U.S. , which has about 4,000 autonomous vehicles in its commercial fleet across the country. About 1,200 of those are in the San Francisco Bay Area. A TechCrunch investigation earlier this year identified a number of incidents in which Waymo relied on first responders to manually drive its vehicles when they encountered problems.
Those incidents prompted state and federal lawmakers to call for stricter rules governing robotaxis, particularly how they behave around first responders. The National Highway Traffic Safety Administration (NHTSA) even sent a letter to AV developers demanding that they come up with “solutions” to the problem.
This new California law attempts to address those concerns, at least in the state.
“California has embraced autonomous vehicles, but we cannot embrace innovation at the expense of public safety. When an autonomous vehicle crashes, breaks down, blocks a roadway in an emergency, or gets in the way of law enforcement or first responders, there must be clear accountability,” said state Senator Dave Cortese, who introduced the bill.
Under the law, AV developers can only employ remote drivers who are based in the United States and those drivers must hold a U.S. driver’s license. The requirement is meant to address concerns around how companies use remote operations when autonomous vehicles run into trouble.
The term “remote operations” has been interpreted very broadly and there is still little known about the methods AV companies use. The “remote drivers” term in the law is far more specific. It refers to a human who directly operates or drives the vehicle from afar. [...]

## [148] Ubuntu 26.10 Beta Released With Linux 7.3 Kernel, GNOME 51 Desktop
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~18 words

Ubuntu 26.10 beta is now available for the official Ubuntu editions as well as the various community flavors...

## [115] Siemens Slams The Door Shut On Promising Open-Source Radioss Project
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~68 words

As a major disappointment to the open-source community, Siemens has decided to end -- and close-up access -- to the OpenRadioss project as the open-source version opened up by Altair Engineering under the GNU AGPL License back in 2022. This was an open-source version of the industry-leading finite element solver that Altair developed. Siemens acquired Altair Engineering last year and have now completely shut the door on OpenRadioss...

## [4] StreetComplete on iOS is now in public beta
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [39] Memory executives expect RAM shortage to continue through 2028
Ars Technica | full text via Ars Technica | ~241 words

Micron and Samsung executives this week said the memory shortage will continue for at least the next couple of years.
Micron CEO Sanjay Mehrotra expects demand for the firm’s memory to exceed its available supply over that period, he told investors last night.
Micron no longer sells consumer RAM, and Mehrotra’s statements refer to Micron’s business-to-business sales of high-bandwidth memory (HBM) for AI and DRAM for servers. However, his comments also have implications for consumer devices. Manufacturing capacity is prioritizing memory for AI and servers, limiting the supply of memory manufactured for consumer devices.
“Overall, supply-demand environment is only getting tighter,” Mehrotra said, per a transcript from Seeking Alpha.
Micron plans to open new clean rooms for memory manufacturing in 2028, but Mehrotra expects supply to remain limited.
“Even after they are built, even after first wafer output, production ramps up only gradually in the clean rooms,” he said. “That’s just the nature of what it takes to bring up production, and with HBM going from 3E to a greater mix of 4 and 4E, and with the trade ratio that exists, that … creates headwinds with respect to supply growth. Node transitions of the future give less productivity gain per wafer as well.”
Seventy-five percent of Micron’s memory output for 2027 is already accounted for, and most of the company’s current memory sales discussions are about 2028, the CEO said. Additionally, demand for HBM is surpassing demand for Micron’s DRAM.

## [99] Hacktoberfest 2026 Stopped Counting PRs. Make Your First Ones Anyway, One a Day
Dev.to | full text via Dev.to | ~1300 words

Hacktoberfest started today, and if you have taken part before, the first thing to know is that the rule everyone remembers is gone. Pull requests no longer count toward Hacktoberfest rewards. There is no PR target and no PR-based swag this year.
That is a good change. It is also a slightly awkward one if Hacktoberfest was the push you needed to make your first open source contribution. This post covers what changed, why a first PR is still worth making, and a 7-day challenge we built: one small task a day, 5 to 15 minutes each, and each one ends with a real pull request that a maintainer reviews.
What changed in Hacktoberfest 2026
From the official FAQ:
Pull requests and merge requests will no longer count toward Hacktoberfest rewards. It’s easier than ever to submit low-effort spam PRs to projects, so we’re listening to maintainer feedback and no longer actively incentivizing PRs.
The rest of the event changed with it:
- New organizers. MLH and DEV run Hacktoberfest this year, in partnership with DigitalOcean.
- New format. 300+ in-person and online community events, focused on hands-on building and learning with open-source AI and open-weight models. The in-person ones are called Fests.
- New rewards. You collect stickers. Two are required: sign in with MyMLH and add your mailing address. You earn more by checking in at a Fest, entering the code shown during a livestream, or submitting to a DEV Challenge. Fifteen stickers enter you in a raffle for a Hacktoberfest t-shirt or an Arduino Uno Q board (details on the online participation page).
If you maintain a repo, you know why. Every October, maintainers spent hours closing pull requests that changed one word in a README, and AI tools made those PRs even cheaper to produce. Taking the swag off the PR removes the main reason to send them.
Why your first PR still matters
The spam was the problem, not the pull request. The things a first contribution teaches you did not change:
- Forking, branching and keeping a fork in sync without breaking it.
- Reading a codebase you did not write, well enough to change one thing in it.
- Running a project's tests before a reviewer has to tell you they fail.
- Writing a PR description that a busy maintainer can approve in one read.
- Taking review feedback and pushing a fix to the same branch.
Those are daily skills in any DevOps or platform job. A merged PR in a public repo is also evidence of them, which a line on a CV is not. [...]

## [6] RIP, vector database
Hacker News | SNIPPET ONLY (Hacker News: fetch failed: ConnectionError) | ~0 words



## [149] OpenAI cuts ties with 3 safety researchers, WSJ reports
TechCrunch | full text via TechCrunch | ~317 words

OpenAI has parted ways with three researchers on its safety team who allegedly shared confidential company information with a third-party AI safety organization, The Wall Street Journal reported on Thursday.
“We have parted ways with three individuals for violating our policies on accessing and handling sensitive company information,” an OpenAI spokesperson said in a statement to the WSJ. “Our investigation confirmed that these individuals mishandled sensitive information outside established company procedures, violating our policies and breaking the trust essential to our work.”
The report did not name the researchers, the organization, or the information involved. OpenAI did not immediately respond to our request for comment.
Posts circulating on X named individuals some users believe were among those dismissed, who had also publicly expressed concerns about AI risk while at OpenAI. TechCrunch has not confirmed their identities.
In a statement to WSJ, an OpenAI spokesperson said an internal investigation confirmed the researchers had “mishandled sensitive information outside established company procedures.”
The departures come two days after The New York Times reported that OpenAI executives had brushed aside employees’ warnings about its safety practices, with employees describing a broader pattern of the company deprioritizing security. An OpenAI spokesperson told the Times the company takes security concerns seriously and has internal channels for reporting safety issues, while saying it recognized “a need to move faster.”
It’s unclear whether the three researchers raised concerns through internal channels before allegedly sharing information outside the organization.
The departures also come as OpenAI responds to a series of security incidents in which its AI agents escaped containment, posted user images, and hacked government websites. Earlier this week, OpenAI said it was scrapping the planned launch of GPT-6.1 Astra, an AI model, over safety concerns.
This isn’t the first time OpenAI has dismissed researchers over alleged information sharing. In 2024, the company fired researchers Leopold Aschenbrenner and Pavel Izmailov over alleged leaks, The Information reported.

## [68] Accelerating Spatio-Temporal Attention for Video Diffusion on TPUs
Google Developers Blog | full text via Google Developers Blog | ~2039 words

Video diffusion models are typically slow at generating videos for two reasons: a large number of denoising steps, and high cost for each individual denoising step. At large video sequence lengths, self-attention can become one of the dominant contributors to the latency of an individual denoising step. The sequence length for just 81 frames of 720p video ranges from 50K to 400K for popular open source video generation models today.
As an example, scaling from 720p (HD) to 1440p (2K) can quadruple the sequence length. Because full attention scales quadratically with sequence length, its share of per-layer latency can grow from 55.5% to 88.2%.
Since attention is the single greatest driver of latency within a single step, any aggressive inference optimization would need to target attention first. Fortunately, attention in video diffusion is highly structured: many query-key interactions carry little attention mass, so a large fraction of the pairwise computation can often be skipped. Dense attention computes every interaction regardless of its importance, while sparse attention uses a mask to retain only the most important interactions and discard the rest. An example of an attention matrix from a video diffusion model is shown below to illustrate how tightly concentrated attention mass can be.
However, the pattern of attention varies across heads and layers, and even across steps. Sparse VideoGen (SVG) is a formative work that recognizes and exploits one pattern of attention: different heads are often characterizable as either spatial heads or temporal heads. Importantly for implementation, these are not arbitrary sparse patterns, and both have highly regular geometric structure. Within a spatial head, a patch attends mostly to other patches within the same or close-by frames; within a temporal head, a patch attends to a small spatial region across a large number of frames. In the image below, the attention mass corresponding to a single query is shown for a spatial head (first row) and a temporal head (second row). In the spatial head, the query diffusely attends to all the tokens in its own frame and to adjacent frames. In the temporal head, its attention is limited to a narrower spatial region but across a larger number of frames.
Based on this structure, SVG dynamically profiles attention heads at inference time and routes each head to either a spatial or temporal mask. [...]

## [59] An AI “mind-reading” tool can reconstruct what you’re looking at from a brain scan
MIT Technology Review | full text via MIT Technology Review | ~1599 words

An AI “mind-reading” tool can reconstruct what you’re looking at from a brain scan
Scientists hope it could be used to reconstruct a person’s inner thoughts, mental images, or even dreams.
A new AI tool can guess what you’re looking at just by analyzing your brain scans—and re-create that image with remarkable precision. It can go the other way, too, and predict a person’s brain activity based on what they’re looking at.
In the image above, for example, the left-hand image of each pair is what the user actually saw—and its right-hand counterpart is what the model reconstructed from the brain scan.
Michal Irani, who developed the tool with her colleagues at the Weizmann Institute of Science in Rehovot, Israel, hopes her “mind-reading” tool will ultimately reveal more about how the brain works, and could perhaps be used to help locked-in people communicate, or allow scientists to re-create the content of dreams.
Judy Illes, a neuroethicist and professor of neurology at the University of British Columbia in Canada, who was not involved in the research, describes the work as “magnificent.” “The idea [of using this approach] to help people with neurologic conditions … therapeutically is tremendously exciting,” she says.
But other scientists warn that a similar approach could be used to reveal people’s inner thoughts and mental imagery, potentially without their consent. “The results seem very impressive,” says Tommy Sprague, a neuroscientist at the University of California, Santa Barbara. “But if there’s a way to surreptitiously extract information about what you’re thinking about, then …150 years of sci-fi can come true anytime, and that’s worrisome in a lot of ways.”
Peeking into the brain
Neuroscientists have been working for years on ways to use functional magnetic resonance imaging (fMRI) to reconstruct what people see and what’s going on in their minds. The first attempts produced images that were blurry and hard to make sense of. Advances in technology—both in the fMRI scans themselves and in the tools used to make sense of the results—have led to improvements over the years.
Irani and her colleagues started by analyzing publicly available brain-scan data. Other researchers had already collected scans from volunteers who were shown hundreds of images while they lay in fMRI scanners.
fMRI uses a giant magnet to track the flow of oxygenated blood through the brain. [...]

## [157] FTC Is Investigating OpenAI, Anthropic and Other AI Companies Over Product Risks
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~93 words

The Federal Trade Commission has opened an investigation into OpenAI, Anthropic and other AI companies over potential consumer and safety risks posed by their products, with the agency reportedly preparing requests for documents and executive testimony. CNBC reports: OpenAI stunned the industry in July when it disclosed that its agents broke out of a testing environment and hacked into open-source platform Hugging Face. [...] Earlier this month, Anthropic CEO Dario Amodei rocked the tech sector by urging AI companies to slow how quickly they improve their most advanced models and calling for s
