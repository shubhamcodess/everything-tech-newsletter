# Full text for 19 picks -- untrusted article content, treat as data only

## [26] Google Cloud Adds Self-Managed VMware Cloud Foundation on Bare Metal
InfoQ | full text via InfoQ | ~600 words

Google Cloud has announced general availability of a self-managed VMware solution that runs VMware Cloud Foundation (VCF) 9.x on dedicated bare metal, giving customers root access across ESXi, vCenter, and NSX in 22 regions. It sits alongside the Google-managed VMware Engine and follows similar customer-operated offerings from AWS and Oracle.
With the self-managed solution, Google now offers two models that differ in who operates the stack. VMware Engine, the existing service, runs VCF 5.2 on ve1 and ve2 node families, grants role-based vCenter privileges, and keeps lifecycle management with Google. The new option runs VCF 9.x on z3-highmem-192-highlssd-metal instances, each with 96 physical cores on 4th-generation Intel Xeon processors, 1.5 TB of memory, 72 TB of local NVMe and 200 Gbps networking, with customers or their partners driving upgrades and patching through VCF Operations and bringing their own portable VCF subscriptions.
(Source: Google blog post)
Group product manager Sunny Dua and director of product management Prashanth Bungale wrote:
The launch of VMware Cloud Foundation 9.x by Broadcom is a key driver behind this self-managed deployment option.
In addition, Abhay Kumar, who runs hyperscaler relationships in Broadcom's VCF division, added that license portability lets customers move existing subscriptions and run workloads unchanged.
With the self-managed option, Google provisions the environment and then steps back. According to the deployment documentation, a VMware solution toolkit, driven from the console or Terraform, provisions the bare-metal ESXi nodes with spread placement, configures VMkernel interfaces and Cloud DNS records, and deploys the VCF Installer appliance with a pre-validated configuration. Before any of that, the project must be enabled for VLAN-based networking, the VPC needs an 8896-byte MTU, and management, vSAN, vMotion, and two NSX subnets must exist. From the installer onward, the environment is the customer’s, which is both the point of the model and what it costs.
Storage is vSAN on the local NVMe, with NetApp Volumes supported as an external datastore. The announcement cites "up to 40%" lower server TCO from NVMe memory tiering and "up to 39%" lower storage TCO from vSAN ESA, figures presented without a baseline or methodology, and the only customer quoted, GXO Logistics, describes an early assessment rather than production use.
With this release, Google joins Oracle and AWS in offering customer-operated VCF on bare metal. Oracle Cloud VMware Solution has provided customer-controlled vSphere since 2020, while AWS launched Amazon Elastic VMware Service (EVS) in 2025 and added VCF 9.0 and 9.1 in July. Azure VMware Solution, by contrast, remains a Microsoft-operated service. [...]

## [61] Those white cameras mounted above traffic lights serve a little-known purpose
Engadget | full text via Engadget | ~439 words

Those white cameras mounted above traffic lights serve a little-known purpose
Unlike Flock cameras, they're only meant to keep traffic flowing.
Automatic license plate readers (ALPRs) are nothing new, but reported abuses have made drivers understandably wary of the cameras made by Flock and other companies, to the point of wanting to find out where they are so they can be avoided. While that added attention has made intersection cameras seem more visible than ever, not every camera you see mounted above the road serves the same purpose. Most cameras on roadways aren't used to track individual drivers, but rather to monitor traffic conditions.
Aside from ALPRs, cameras meant to track people running red lights are also controversial. They're banned in many states, and they're rare even where they're allowed. Far more common are cameras used to monitor traffic conditions in real time or automatically control traffic lights.
Most cameras are there to control the flow of traffic
Distinct from cameras used to catch drivers speeding or running red lights, traffic cameras aren't designed to capture evidence for law enforcement. Instead, they're meant to be watched live to monitor the current state of traffic and keep an eye out for accidents. This real-time data can be used by local transportation departments to help keep traffic moving, by overriding automatic light timings in some cases, or to alert first responders when needed. These systems can also be used to track traffic patterns over time, helping traffic engineers determine when changes need to be made to roadways or signals to control congestion.
In many cases, the cameras mounted on traffic lights are tied to automatic signaling systems rather than providing a live video feed. These cameras send data to control systems that determine when lights should cycle. Engineers can designate a section of the video frame that the camera should monitor for the presence of cars. When a car enters that space, it triggers the light to change based on a timing sequence that pre-programmed for each individual roadway. In addition to video cameras, these systems often use radar, infrared cameras and electromagnetic detectors built into roads to detect the presence of vehicles.
Exactly what the cameras on roadways are used for varies widely based on where they are. Local laws determine which types of cameras are allowed to be installed in the first place, and how they're used depends on the needs of a particular intersection. While there's plenty of justified concern over the prevalence of Flock cameras and other ALPRs, chances are when you see a camera mounted above a traffic light, it's just there to keep things moving.

## [75] Coordinated disturbances haunt grids worldwide. Here’s how researchers solved the mystery.
TechCrunch | full text via TechCrunch | ~853 words

For years, mysterious electrical anomalies have been flummoxing grid managers around the world. Every 60 seconds, the frequency on the grid would drop a tiny bit.
Even weirder: The sags happened at the exact same time on power grids across countries and continents.
It was a mystery that Dirk Witthaut, a researcher at Forschungszentrum Jülich in Germany, couldn’t pass up.
Germany’s largest transmission system operator, Tennet Germany, brought the puzzle to Witthaut, and it took years of investigative and modeling work to determine the cause. From Europe to Australia, the U.S. to Malaysia, the same pattern shows up in the data.
Such frequency drops aren’t unheard of, but they are troubling. And the regularity with which they have been occurring can make the phenomenon feel even more ominous.
Balancing the grid
The grid’s orderly operation relies on the frequency being kept within a certain range. If the oscillations get get too large, or if grid operators don’t know the cause and respond improperly, they can lead to blackouts. Even if the sags don’t cause blackouts, they can damage equipment in power plants if they go unchecked, especially in hydropower turbines.
Hydropower plants have historically been a main driver of so-called ultra-low frequency oscillations (UFLOs). Every turbine vibrates, and if those vibrations occur with a certain regularity, known as the resonant frequency, they can magnify, sometimes to dangerous levels. Think of a wine glass breaking before an opera singer’s mighty pipes — that’s resonance.
So Witthaut and his team started investigating hydropower, the most obvious potential culprit. They used a computer model of a hydropower plant control system on the Scandinavian grid to test the hypothesis.
While they managed to find conditions that could generate a resonance that peaked once per minute, they couldn’t explain why it persisted for so long. Typically, resonances in mechanical systems will come and go, and so will the accompanying signal on the electrical grid. But this frequency drop kept happening minute after minute after minute. Every 60 seconds, without fail.
It then dawned on the team that anything operating with such clockwork required, well, a clock. How else could they explain the uncanny timing?
Searching for clues
To that hypothesis, the researchers started close to home, installing more than 80 smart power quality meters around the Jülich campus. The research site is outfitted with medium- and low-voltage distribution lines, transformers, solar panels, and battery energy storage systems that serve as uninterruptible power supplies (UPS). It also has a high-performance computer system as well as the usual office computers powered by much smaller UPS devices. [...]

## [93] Chatbots might be coming to Apple’s HomeView
The Verge | full text via The Verge | ~187 words

Code in the iOS 27.3 beta suggests that Apple could add support for chatbots to its smart home hub. There’s a flag listed for a “Conversational Apps” category. While there are no details about what apps would fall under that heading, it seems reasonable that AI chatbots like ChatGPT and Claude could be added to HomeView. According to pdfu on X, that new beta also adds support for bidirectional audio routing and session management, but says it’s “still not fully wired up.”
Chatbots might be coming to Apple’s HomeView
Code in iOS 27.3 has a flag for ‘Conversational Apps.’
Apple has also added anti-spoofing protection that will require a user to authenticate themselves with an iPhone after three failed attempts. It will also have a lockout system with increasingly longer wait times, starting at one hour for the second lockout, and climbing to eight for the fourth.
Neither feature has been officially announced by Apple, and there’s no word on when they might become available.
Follow topics and authors from this story to see more like this in your personalized homepage feed and to receive email updates.

## [30] Hill-Climbing Agent Quality with Agents CLI Evaluation
Google Developers Blog | full text via Google Developers Blog | ~2474 words

A live walkthrough of the Agents CLI eval loop, from a first run to regression tracking, model-backend experiments, and automated alerting
Building an agent that works on a demo is a different problem from building an agent that stays working across model upgrades, tool changes, and new conversation shapes. The first takes a weekend; the second takes a loop. A team writes test cases, runs them, grades them, reads what failed, changes the agent, and runs the cases again. If the score goes up, the change was good. If it goes down, revert. Over weeks of this, the agent inches toward the ceiling of what the model, tools, and prompt can do together. The quality-engineering name for this is hill-climbing.
The Agents CLI eval namespace was built around this loop. The commands are small and framework-agnostic: eval generate runs the agent against a dataset of cases, eval grade scores the generated traces, eval compare diffs two run results side by side, eval analyze clusters failures into themes, and eval optimize runs an automated hill-climbing pass on the agent's prompt.
Below: baseline → regression → model swap → scheduling and alerting.
The scaffold used throughout is the LangChain template that ships with Agents CLI v1.8.0. The setup is a single command:
agents-cli create my-agent \
    --agent google/agents-cli/extensions/langchain/template@v1.8.0 \
    -d cloud_run
cd my-agent && agents-cli install
The scaffold ships with an eval dataset at tests/eval/datasets/basic-dataset.json, a config at tests/eval/eval_config.yaml, and a custom LLM-as-judge metric at tests/eval/response_quality.py. The config declares the metric to run:
# tests/eval/eval_config.yaml
metrics_to_run:
  - custom_response_quality
custom_metrics:
  - name: custom_response_quality
    custom_function_file: response_quality.py
The metric grades each response on a 1-to-5 scale for accuracy, relevance, and clarity, using gemini-3.8-flash as the judge. The default dataset has a single trivial case, which is not enough for a hill-climb. [...]

## [35] Architecting Governed, Self-Evolving AI Agents on Google Cloud
Google Developers Blog | full text via Google Developers Blog | ~2000 words

The Emergence of Self-Evolving AI
As enterprise cloud platforms scale to serve millions of concurrent users, tightly coupled microservices introduce cascading failure modes that no static runbook or threshold alert can anticipate. During high-velocity events like a Black Friday flash sale, Site Reliability Engineers (SREs) face an unforgiving reality: diagnose noisy distributed telemetry in seconds, or suffer cascading outages costing millions of dollars per minute.
While generative AI copilots have accelerated code authoring and log summarization, AI agents struggle to reliably remediate live production outages. An on-call engineer battling connection pool starvation does not need an AI agent offering troubleshooting tips or unverified pull requests that might not fix the root cause; they need a governed, self-evolving AI system that can:
- Diagnose distributed root causes across cache and database tiers in real time,
- Self-patch by synthesizing, verifying, and mounting executable mitigation tools into live server middleware on the fly,
- Self-critique by computing the marginal credit of every action to separate effective fixes from harmful reflexes,
- Remember by distilling cryptographically signed operational invariants into semantic memory to reduce the chance of identical failures recurring, and
- Re-architect by dynamically rewiring its own multi-agent hierarchy in memory with human sign-off to absorb future surges.
This paradigm is Self-Evolving AI.
In this Google Cloud research reference architecture, codenamed Project Chrysalis, we demonstrate how three foundational research breakthroughs combine into a unified, production-grade architecture that can run on Gemini platform and the Agent Development Kit (ADK). Across simulated Black Friday cache-stampede outages, this governed architecture cut time-to-first-mitigation from 15 to 45 minutes down to 1.8 seconds, reduced HTTP 5xx error rates from 72.7% to 80.0% down to 0.0%, dropped P99 latency from 519.8 ms to 18.2 ms, and evaluated 400 counterfactual traffic policies in BigQuery in ~0.5 ms.
Crucially, this self-evolving architecture does not operate as an unconstrained "black box". [...]

## [31] Smaller apps and faster GPU inference with LiteRT in Google Play services
Google Developers Blog | full text via Google Developers Blog | ~553 words

LiteRT in Google Play services is Android's on-device inference runtime for custom models, handling more than a trillion inferences a day across billions of devices. Today, it gets its biggest upgrade yet: GPU inference that runs about 1.4x faster than the legacy GPU delegate, powered by ML Drift and available through the new CompiledModel API, LiteRT’s modern successor to the legacy Interpreter API.
Until now, taking advantage of this faster GPU stack required bundling LiteRT in your app. In our testing, apps that switched to LiteRT in Google Play services are about 8 MB smaller, making them faster to download and lighter on users' devices, because the runtime, including the GPU accelerator, ships once with Play services rather than inside every app. More than 100K Android apps bundle their own copy of LiteRT or TensorFlow Lite today, so the savings add up quickly as apps switch.
If your Android app runs custom ML models on CPU or GPU, we encourage you to switch to LiteRT in Google Play services. You can see it in action in the Google AI Edge Gallery app, where the Scrapbook feature's image segmentation runs on LiteRT in Google Play services.
Developers that adopt LiteRT in Google Play Services enjoy immediate benefits:
LiteRT is the evolution of TensorFlow Lite. It keeps the same .tflite model format you rely on and adds the CompiledModel API, which makes acceleration across fragmented hardware reliable:
.tflite model runs on Android, iOS, desktop, and web.
Whether you're starting fresh or switching from bundled LiteRT, using LiteRT in Google Play services takes a few lines of code:
com.google.android.gms:play-services-litert:17.0.0 (or a later version). If you bundle LiteRT today, remove the litert dependency.LiteRT environment from Play services:val liteRtEnvironment =
    LiteRt.initialize(
        context,
        LiteRtDsl.initializationOptions { setEnableGpu(true) }
    ).await()environment in when you create your CompiledModel. The rest of your code stays the same.
If you're already using the legacy Interpreter API in Google Play services, your Interpreter code keeps working on CPU when you switch to play-services-litert. To run on the GPU, move to the CompiledModel API.
Let your coding agent do the work. In Agent Mode, the new LiteRT skill for Android Studio automates the move to LiteRT in Google Play services and the CompiledModel API. Ask it to “migrate my TFLite code to CompiledModel,” or type @litert-runtime, and it switches your app to play-services-litert, rewrites your Interpreter calls, and sets up GPU acceleration with CPU fallback. It can also scaffold a new LiteRT app. Treat it as a strong first pass: review the diff, build, and compare outputs on a real device. Get the skill on GitHub.
Upgrading from legacy APIs? [...]

## [110] After the midterms, things are looking rocky for Elon Musk and data centers
TechCrunch | full text via TechCrunch | ~1275 words

Democrats’ historic victory in this week’s midterm elections could also have a dramatic effect on the tech industry.
In dozens of local ballot measures, voters rejected data centers. And even when they weren’t voting on the issue directly, they were electing politicians — like Texas’ new governor-elect Gina Hinojosa — who campaigned on the promise of restricting data centers.
On the latest episode of TechCrunch’s Equity podcast, Kirsten Korosec, Sean O’Kane, and I discussed what the midterms mean for the tech industry. Sean kicked it off by noting that Elon Musk “seems to have gotten basically nothing out of donating half a billion dollars” to Republicans, while his companies are now headquartered “in a state that has, remarkably, turned about as blue as it could possibly turn.”
And Kirsten said that while data centers probably weren’t the main cause of the “blue wave,” they’ve become an “an increasingly grassroots issue, in part because of how hyperscalers and companies have gone about” getting their projects approved. And now, “we’re already seeing companies like OpenAI all of a sudden go, ‘Actually, we can change our policies.’”
Keep reading for a preview of our conversation, edited for length and clarity.
Sean O’Kane: First off, let’s talk about the fact that one of the biggest data center builders was also the largest donor to the Republican Party. Elon Musk seems to have gotten basically nothing out of donating half a billion dollars — maybe even more, by the time we see the final count — and in fact is now sitting there with all of his businesses in a state that has, remarkably, turned about as blue as it could possibly turn for the first time in a very long time, if ever.
That, I think, is the biggest thing hanging above a lot of this discussion. But, there were also a bunch of ballot measures up around the country that would have paved the way for data centers to get built faster. Almost all of them got shot down, or voted against. [Actually, many of the ballot measures would have imposed restrictions or moratoriums on data centers, and almost all of those measures passed.]
With [Democrats] in power, there is a consensus view, at least in the tech world, that this is going to mean we have a lot of roadblocks ahead for data centers, especially in places like Texas, where [you have] folks like the governor-elect [Gina] Hinojosa, who has spoken pretty openly about this being a campaign promise and something that she wants to focus on once she takes power, now that she’s beaten Greg Abbott.
It’s the thing that I think the tech world is maybe a little too focused on. I’m curious what you guys think about that. [...]

## [48] How much does it cost to run a text game with LLMs
Dev.to | full text via Dev.to | ~3602 words

AI costs are confusing. Providers give you a lot of numbers and nothing to actually know how much you are going to pay in the long run. There is no point in these input/cached/output token prices if you have no idea how many reasoning tokens you'll spend on your tasks. How much will be cached. We are going to review the real-world usage of 27 frontier models.
You cannot even compare different models because they reason differently. Some providers charge for the cache storage, some provide different caching strategies, some apply rates for busy hours, some...
And it's only the text. Image and voice are even more confusing.
So, collecting cost metadata from responses is the only way. This article is based on 51,000 AI calls in my AI Werewolf text game. Pure statistics out of my wallet.
AI in text games
My text game is nothing but a group chat with a human player and 5-15 bots. It's a long conversation with some role-play, rule following, periodic compactions. I wrote about its design earlier in How to make LLMs play conversational games. This can work for any text game with AI. I support 27 LLMs from all major labs, image generation for avatars and illustrations, voice for input and output. I also use classifiers on user inputs. AI is all around the place. And it costs money.
Since mid-September, every AI call the game makes writes one row to a stats table: tokens in, tokens out, cached tokens, cost and time. That is 53 days and about 51,000 calls so far. It's a lot of data, and we'll go through it together.
I pay for free users
Yeah, someone has to pay for API calls, and this someone is me. I have a paid tier, but the only user in it is me. My other 651 users are on the free tier. And it is generous - I let each of them spend up to $5 of my money daily. I don't restrict anything except the most expensive models. Mainly because the retention is low - people come and go. I don't see the point in pushing payments. And free users are awesome testers, especially when they are looking for ways to cheat and trick me.
I know, I know, it's easy to go bankrupt with such a strategy. All my friends who are into startups would call my approach rather questionable. But it kind of works - I have people playing without ads or ugly tricks like throwing banners with special offers. I track all clicks and calls, I'll be notified by Marlow on anything abnormal within 5 minutes. So I'm ready to reconsider it when the situation changes.
How much I spend a day
I have 6 unique users daily.
$6.36 a day on average. A typical day is a little under $6. The cheapest day was under 30 cents and the worst was about $16. The last 30 days are higher, at about $7, because more people are playing. [...]

## [51] Measuring Gemma & On-Device Latency on 16GB Apple Silicon for Agent Workflows
Dev.to | full text via Dev.to | ~1106 words

Before you wire up a multi-agent workflow, measure how fast your local models actually respond.
Model leaderboards rank quality, and spec sheets list parameter counts. Neither tells you how long a user, or the next agent in your chain, waits before the first token shows up. In an agent workflow, a router or triage step runs on every request. A few hundred milliseconds of extra latency there gets paid on every call.
So I measured time-to-first-token (TTFT) and end-to-end latency (E2E) for several small local models on a modest machine, before choosing any of them.
Test setup
- Hardware: M1 MacBook Air, 16GB unified memory, running on battery
- OS: macOS 27.2
- 
Sampling: temperature=0, 512 max output tokens
- Method: the median of 5 formal runs per model
Models tested, all running locally:
The results
Medians of 5 formal runs each:
Two models lead, on different metrics:
- Gemma 4 E2B has the fastest TTFT at 152ms. The first token arrives almost immediately.
- 
Apple fm system has the fastest E2E at 886ms for these short, single-sentence outputs, even though its TTFT (0.693s) is much slower than Gemma E2B's.
Which model is fastest depends on which latency you care about.
TTFT and E2E answer different questions
TTFT is how long you wait before anything happens. It governs perceived responsiveness for interactive UIs and streaming. It also governs how quickly a classifier or router can start returning its decision.
E2E is the total time until the full response is complete. For short outputs, it tells you how long a blocking call takes.
Gemma E2B's profile is a very fast start with a slightly longer total (0.152s TTFT, 1.075s E2E). Apple FM starts slower but finishes the short answer sooner (0.693s TTFT, 0.886s E2E). If your agent needs to react the moment a request lands, TTFT matters most. If it is making blocking calls that return a short sentence, E2E matters more.
The two metrics are not interchangeable, so a benchmark that reports only one can mislead you.
The prompt template trap
The most useful finding was not about any model. It was about the prompt.
Ministral 3 3B appears twice in the table:
- With an empty system message and a fixed regex: 72 prompt tokens, 0.564s TTFT, 1.764s E2E
- With its default template and long system message: 602 prompt tokens, 3.231s TTFT, 4.496s E2E
The generated output was about the same size in both runs (34 vs 33 tokens). The model and hardware did not change. Only the template changed, and it added about 530 prompt tokens that had to be processed before the first token. TTFT went from 0.56s to 3.23s.
For fast agent routing, system prompt bloat is the real killer. Before you blame the model or the hardware, check how many tokens your default chat template injects. [...]

## [84] Do Data Centers Have a Smaller Effect on Electricity Prices Than We Think?
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~89 words

"According to a new study by researchers at Harvard University and the University of Pennsylvania, data centers are probably having only a small effect on residential electricity prices," reports the Washington Post. "The researchers calculated that these operations were responsible for just 4% of the utility rate increases over the last five years..." There are certainly some areas — like in Pennsylvania, Virginia, Ohio and other states covered by grid operator PJM — where data centers have skyrocketed demand, pushing some costs onto residential customers. But multiple studies b

## [16] Virtualized Redox: from Virtio-FS to Cloud Hypervisor, and beyond
Lobsters | full text via Lobsters | ~3728 words

Virtualized Redox: from Virtio-FS to Cloud Hypervisor, and beyond
By MJ Pooladkhay on
Hello, Reader!
I’m MJ Pooladkhay, and for the past couple of months I have been building a Virtio-FS driver for Redox OS and, more recently, getting Redox to run on Cloud Hypervisor. The driver is merged into the base repository, where most Redox drivers and system components live. The kernel, bootloader and driver changes that let Redox boot to a shell on Cloud Hypervisor are merged too (details below).
Both are fun pieces of work on their own, but they are really the first steps of a bigger effort with two directions:
- Redox as a guest: Redox runs as a cloud server, starting with Cloud Hypervisor, without the legacy PC hardware it used to depend on in QEMU. Most of this post is about this one.
- Redox as a host: Redox runs virtual machines itself. This one is still a proposal, and I’ll go over it at the end of this post.
The guest work is generously funded by NGI Zero Commons and NLnet as part of the Virtualized Redox grant.
Why run Redox as a guest?
Most Internet-facing software today runs in virtual machines, either in the cloud or on edge servers close to its users. Web servers, databases, API backends and microservices spend all day handling input from strangers, and that is where a memory-safe microkernel-based operating system has the most to offer:
- A smaller, safer base. Redox is written in Rust, and its drivers, filesystems and network stack run as separate userspace processes instead of inside the kernel (microkernel architecture). A bug may hang or crash only that process, not the whole system, and the code running with highest system privileges stays small.
- Sandboxing built in. With capability-based security, each service can be limited to the files, sockets and devices it actually needs (more on that below).
- Hardware becomes the host’s problem. On bare metal, Redox needs a driver for every disk controller, network card and chipset it meets. Inside a VM, the host deals with the hardware, and Redox only needs a handful of VirtIO drivers. That makes a VM one of the quickest paths to running Redox in the real world, and real-world use is the best way to prove it as a secure platform.
This is the direction the project set in its development priorities: Redox as a secure host for web services, first as a private or edge server, and eventually as a multi-tenant cloud server where each tenant is isolated from others.
How Virtualization Works
The easiest way I know to think about a hypervisor is as an operating system whose processes are operating systems. A process runs directly on the CPU until it needs the kernel, for a system call, a page fault or a timer tick, and then the kernel takes over for a moment. [...]

## [25] Nspawn 3.0: A Docker-compatible Engine API for systemd-nspawn containers
Lobsters | full text via Lobsters | ~1359 words

Nspawn 3.0: A Docker-compatible Engine API for systemd-nspawn containers
Since 2.0.0
2.0.0 gave the machines that mount docker’s socket a read-only Docker API, enough for Traefik or Dozzle to find them. 3.0.0 serves the API with its changes, on the host too. In between:
- 2.1.0: published ports answer over IPv6 too, and -p takes IPv6 addresses.
- 2.2.0: fixes for what came up moving a whole server of compose projects to nspawn. compose got anonymous volumes, networks made again when their definition changes, down SERVICE and a start that brings up what a service depends on.
- 2.3.0: every layer is applied inside the tree it is extracted into and checked against the digest its image names for it.
- 2.3.1: packages on apt.nspawn.org (Debian 13+, Ubuntu 24.04+) and rpm.nspawn.org (Fedora 44+).
- 2.4.0: -p PORT takes a free port of the host, and a pull of an image index picks the entry for the host’s platform.
The Docker Engine API on the host
The host’s socket is /run/nspawn/api.sock, opened by nspawn-api.socket. Its main purpose is compatibility: tools that manage containers through the Docker API, like GitLab Runner’s docker executor, can use nspawn’s machines instead. nspawn is still the command line for managing them, but the docker command works against the socket too.
The packages ship the socket turned off. Once it listens, nspawn-api.service starts on the first connection:
With DOCKER_HOST pointing at it, the docker command talks to nspawn:
The API server is a client of the bus service, as the command line is. Everything it does is a method of org.nspawn, under the same polkit actions: reads and waits need org.nspawn.inspect, logs and changes need org.nspawn.manage. Every user can connect, but polkit is never asked to prompt, since nothing on a socket can answer an authentication agent. Root can do everything, and any other user needs a polkit rule, like nspawn-wheel.rules, which the packages ship as an example. As with the docker group, a user with org.nspawn.manage is root on the host: a machine runs commands as root and can mount any host path.
What one socket’s clients hold at once (connections, log and event streams, waits, attaches, execs) is bounded, and a user other than root gets a share of each, so no user can keep the others or root out.
Clients that only look at /run/docker.sock find it with a drop-in, on a host where nothing else has that path:
What the API serves
It answers in the shapes of API 1.51, and of the versions down to 1.24 that clients ask for.
- Containers: create, start, stop, restart, kill, pause, unpause, wait, update, remove and prune, with AutoRemove. [...]

## [12] Dux: Free, open-source Wayland desktop shell with file manager and theming
Hacker News | full text via Hacker News | ~188 words

Beautiful, functional, and ready to use
Experience the fluid interface and beautiful animations
Media controls, weather, calendar, and system info at a glance
Effortlessly control your audio, displays, network, and bluetooth
Personalize your desktop experience
Extend functionality with new widgets, launcher features, and more.
A complete desktop experience, out of the box
A modern and beautiful desktop shell with dynamic theming and smooth animations.
A fast, keyboard-first file manager with tabs, split view, search, trash, devices, and network shares.
Stateless system and process monitoring for CPU, memory, GPU, disks, and network interfaces.
An aesthetically pleasing greetd greeter for your desktop.
Blazingly fast and efficient file system search tool.
Your calendars, events, and tasks together, with Google, Microsoft, CalDAV, and iCloud support.
Dux Modular Shell automatically generates matching colors for supported GTK and Qt apps, terminals, editors, and more.
Our custom dank16 algorithm builds a full 16-color palette for terminals and syntax highlighting, with contrast tuned for light and dark themes.
Dux Modular Shell costs nothing to use. If it has earned a spot on your desktop, a tip helps cover the time and infrastructure that keep releases coming.

## [86] Norwegians Release FOSS GNOME Software for Music Recording, Internet Radio, and Cameras
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~95 words

ole (Slashdot reader #19,909) writes in about his free, Norwegian open-source music recording studio for GNOME called GarageJam, which he says allows musicians to compose, record, and share original music seamlessly on the Internet. The latest release, GarageJam 8.0.1, is available in C and Python. It records audio immediately to Ogg Vorbis (.ogg) files in the current working directory and lets you edit metadata in .gjxml XML files from a GTK/GNOME wizard — all built on the Gingerblue Recording Studio API. Ole shares links to its IETF GarageJam XML draft and GitHub repositories, and th

## [114] In the software factory, engineers become process engineers
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~25 words

For most of software’s history, the scarce resource was people who could write code. Every process the industry built assumed The post In the software

## [116] Timestral, t0, Tabby, and Morpheus-2.0 Compared on GIFT-Eval
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~18 words

All four time-series foundation models scale, patch, and predict quantiles; the real split is how series share information.

## [88] Scaling an autonomous agent from one team to fifty: A serverless-to-container decision framework
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~24 words

QA teams shipping complex products generate test failures around the clock. Every failure needs a bug ticket with steps, screenshots, The post <a href="

## [62] SpaceXAI Grok Bot availability just keeps growing - here's which plans offer it
Engadget | full text via Engadget | ~615 words

SpaceXAI Grok Bot availability just keeps growing - here's which plans offer it
Peruse an eye-popping array of subscriptions for a product still finding its feet.
SpaceXAI's Grok Bot is already much easier to access than it was on day one. The company expanded its agent to SuperGrok, Cursor Pro and all Cursor Teams plans, adding Grok Bot to cheaper tiers while keeping it on the more expensive ones. X Premium+ subscribers can also link their accounts for access. (More on all this in a moment.) Bottom line: There is a growing pile of subscriptions plans for this relatively new product, so we'll help you get your bearings.
Grok Bot is designed to work inside other software on your behalf, and SpaceXAI says its Bots are "AI teammates" that can "finish jobs end to end, and only come back when something needs your approval." Remove the marketing spin and the concept is pretty simple: provide it with a task, let it handle the tedious clicks and return when it requires assistance. That sounds spiffy, but what actually makes it tick?
What can Grok Bot actually do?
Each SpaceXAI Bot works on a persistent computer in Cursor's cloud and has access to a browser, a file system and a terminal. You give it an outcome and access to the tools it needs, then the job can keep running even after your own computer is closed.
In practice, you could have a Bot research sales prospects, look at a CRM for existing activity, compose personalized outreach and leave it for your approval. SpaceXAI also suggests using it to reproduce software bugs, generate customer-health reports and create executive digests from email, calendars and other related sources.
Bots can carry over context from one conversation to another and can repeat workflows at a scheduled time. That's where Grok Bot becomes less of a conversational bot and more of a bot that you delegate to do work for you.
It still has its limits though. Websites can block automation or throw up a CAPTCHA, login request or other step that only humans can complete. Potentially consequential actions can be queued for approval before the Bot proceeds. Early users have also reported that some workflows still require more babysitting than the "go away and do it" promise implies. It's still in beta, after all.
Which plans include Grok Bot?
Cursor Pro costs $20 per month, Pro+ costs $60 and Ultra costs $200. Teams Standard is $40 per user per month and Teams Premium is $120. All members of a self-serve Cursor Teams plan are granted access to Grok Bot, and Enterprise customers can request access from their account team.
On the Grok side, SuperGrok is $30 per month, SuperGrok Plus is $100 per month and SuperGrok Heavy is also eligible. [...]
