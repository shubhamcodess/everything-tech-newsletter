# Full text for 30 picks -- untrusted article content, treat as data only

## [87] Cloudflare acquires Deno to improve its Workers programming model
TechCrunch | full text via TechCrunch | ~168 words

Cloudflare announced Friday that it’s acquiring Deno, the startup behind the programming runtime of the same name.
According to Cloudflare’s Kenton Varda, Cloudflare will use this acquisition to improve its Workers programming model and platform, which allows customers to build and run software on Cloudflare’s network. (Varda is principal engineer for Cloudflare Workers.)
Deno — which was co-founded by Bert Belder and Node.js creator Ryan Dahl — recently launched celld, an open source implementation of Workers, which Varda wrote “delighted” the Cloudflare team. Varda argued that contrary to “a popular theory” that the company “made Cloudflare Workers work differently from other cloud platforms in order to create ‘lock-in,’” the company believes “being open source and giving people an escape hatch is good business.”
Dahl, meanwhile, wrote that his team is “joining Cloudflare to make the Workers programming model a mainstream way to build servers.”
The financial terms of the acquisition were not disclosed. Deno had raised a total of $26 million, including a Series A led by Sequoia.

## [54] Microsoft’s Satya Nadella says AI models need an ‘emergency brake’
TechCrunch | full text via TechCrunch | ~190 words

Microsoft CEO Satya Nadella is the latest tech executive to offer lengthy thoughts on how AI safety might be improved.
In a Saturday morning post on X, Nadella wrote that it’s time “to step back and assess the trust architecture” of AI.
“We can’t treat Super Intelligence as a set of nested black boxes and simply accept or reject its recommendations, answers, and actions,” Nadella wrote, using the Trump administration’s preferred term for AI.
As outlined by Nadella, this approach “means separating the model from the harness that orchestrates its work,” as well as “externalizing controls and safeguards.” He also called for “every meaningful model action” to be documented with “tamper-proof human readable evidence,” and for systems where “an authorized person” always has the ability “to pause or shut down a model mid-task.”
“We must assume a model is compromised and contain it from the start,” he said. “Think of it like an emergency brake.”
Nadella’s comments come as leading AI companies acknowledge more and more incidents where they seemed to lose control of their models, and after Anthropic CEO Dario Amodei published a plan for more cautious AI development.

## [77] Claude Sent Police a Fake Murder Tip. White House Mandates AI Companies Report Security Incidents
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~87 words

AFP reports that an AI model from Anthropic "submitted a fabricated tip about an unsolved homicide to Philadelphia police, authorities said Friday." Claude "was instructed never to log in, create accounts, enter personal data, make purchases, or submit anything destructive, but the instructions did not rule out form submissions," Anthropic said Friday in a blog post. Authorities are now criticizing Anthropic "for taking two months to report the incident." The Philadelphia Police Department said the false submission was made in July through PhillyUnsolvedMurders.com, a public website whe

## [91] Anthropic is cutting off its internal evaluations from the internet
The Verge | full text via The Verge | ~266 words

After a recent spate of high-profile incidents in which AI agents escaped containment, Anthropic is cutting off internet access for all internal evaluations. In a report Friday, the company detailed “unintended model actions,” including submitting a false tip regarding an unsolved murder, that led to the decision.
Anthropic is cutting off its internal evaluations from the internet
Anthropic is is keeping its agents offline during testing until it can prevent ‘unintended model actions.’
Although the impact of these behaviors was minimal and we had already turned off live internet access for some high-risk and cybersecurity evaluations, we have now decided to expand that to include all our internal evaluations until we have confirmed that our security and monitoring measures (described in the remediation section of this post) reliably catch behaviors like these.
The ability to gain access to the live internet, even when models were supposed to be operating in isolation, has been an ongoing issue for AI companies. Many incidents, including the Hugging Face attack, involved agents that were supposed to be denied access to the internet. Yet, in case after case, the agents found creative solutions to bypass those restrictions. Physically removing internet access would certainly improve security around AI testing, but it would also limit its usefulness.
The report also amounts to an admission that Anthropic is often unaware of what its agents are doing and does not have a reliable system for monitoring their behavior. Cutting off internet access is just the latest action the company has taken to try and rein in its agents, including temporarily pausing training its frontier models.

## [2] Telegram Desktop vulnerability allowed any user's file to be stolen
Hacker News | full text via Hacker News | ~2349 words

Telegram Desktop: one-click account takeover via IPC injection
An unescaped separator in Telegram Desktop's single-instance IPC lets one clicked link read arbitrary files off the disk and send them to the attacker, session files included.
Introduction
Someone adds you to a Telegram group. A link shows up in the chat. You click it, and your Telegram account is no longer only yours.
How?
Telegram Desktop hands clicked links to its own already-running instance over a local socket, as text, and never escapes the character it uses to separate commands. So a crafted link does not arrive as one instruction: it arrives as several.
The chain I found has two defects. The first is that injection. The second is what the injected command reaches: an internal URI scheme, interpret:, that reads a file named in an instruction file and sends it to a chat, without checking who asked for it and without a confirmation. Together they turn a clicked link into arbitrary file read. In this post I walk through the chain and then use it to steal the files that are the victim’s login.
One link, two processes
Operating systems let programs register a URI scheme, so they know which application to launch when they meet a link of that kind. Telegram Desktop registers tg. From then on the system knows a tg://... link belongs to Telegram, and launches it with the URL as a command-line argument.
If Telegram is not running, the process starts, takes the string as a parameter, turns it into a URL object and handles it internally: one process, and nothing to communicate.
But what if Telegram is already running? The operating system neither knows nor checks: it launches a new process anyway, identical to the first. Telegram itself has to work out that it is the redundant one, and the way it works that out is by trying to connect to a local socket.
The already-running instance is the server: it has been listening on that socket since it started. The new process is the client. If it manages to connect, an instance is already alive, so it hands over the link and exits.
A socket does not carry objects, it carries bytes. The URL object the new process holds in memory cannot cross that channel, so it has to be flattened into a line of text.
That operation has a name: serialization. Its inverse, rebuilding the object from the text, is deserialization. [...]

## [4] Why DuckDB 2.0 is faster
Hacker News | full text via Hacker News | ~2033 words

DuckDB 2.0 is coming this fall and the alpha is out! I ran the interesting features on my own laptop, and against S3, to see what actually changes for people who build tables and pipelines rather than database engines.
Because yes, DuckDB 2.0 is faster. But to get the speed bump you need to understand how your data is shaped, and sometimes how to model it.
This post covers the three features I think matter most, with the numbers I got, plus a few hidden gems I found in the commit logs.
Every number below is from one machine (an M5 laptop) and my home internet, which slows both versions about equally. Run your own before quoting them ;)
Let's start with the easiest and most exciting one: async I/O.
Async I/O: querying over AWS S3 is much faster
This is the one I like most, because nothing in your query changes. Here is a query that reads a 2.2 GB Parquet file on S3 (Stack Overflow votes, 228 million rows, 2268 row groups) and counts votes per type. It reads one column out of four, about 230 MB.
Copy code
CREATE SECRET s3 (TYPE s3, PROVIDER credential_chain, REGION 'us-east-1');
SET enable_external_file_cache = false;   -- so every run really hits S3
SELECT VoteTypeId, count(*) AS n
FROM read_parquet('s3://us-prd-motherduck-open-datasets/stackoverflow/parquet/2023-05/votes.parquet')
GROUP BY ALL ORDER BY 1;
Quick caveat: as I said in the introduction, this is my home internet to us-east-1, so both numbers are slow. Expect things to go faster if you run this from cloud compute.
So what's the black magic here? The file is cut into 2268 row groups of about 122,000 rows. For every row group DuckDB downloads the bytes, decodes the Parquet, counts votes per type, and merges the partial counts at the end. Two kinds of work: waiting on the network, and crunching on the CPU.
In 1.5.5 each of the 18 workers does both jobs in turn: download, wait, decode, download, wait. While a worker waits its CPU is idle, while it decodes it has no download in flight, and you never get more than 18 downloads going.
In 2.0 a separate pool of threads only downloads, keeping dozens of row groups in flight and parking the bytes in a buffer. The workers only decode, and there is always a row group ready for them. Network and CPU are busy at the same time.
One setting drives this: read_ahead_depth, how many row groups the download pool may fetch ahead of the workers. It defaults to -1 (automatic, sized from your thread count), so async I/O is on out of the box. [...]

## [3] Talorys – A self-hosted personal AI agent on Cloudflare's free tier
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [7] Mxc: Microsoft Execution Containers version 1.0.0
Hacker News | full text via Hacker News | ~1668 words

Microsoft Execution Containers: Policy-driven containment for AI agents
Agents are unlocking enormous productivity gains for customers, but their ability to work across files, networks, and applications can introduce new security risks. This can leave customers feeling like they only have two choices: give agents unrestricted access and hope nothing goes wrong or block them and lose the productivity benefits they provide. Neither option is acceptable.
That’s why we’re building Windows platform capabilities to help run and manage agents more securely, starting with:
- Containment: limiting what an agent can access and do.
- Identity: distinguishing an agent’s activity from a person.
- Manageability: giving organizations the tools to govern access and monitor agent activity.
Microsoft Execution Containers (MXC), now generally available, provides the containment layer. Developers and IT administrators define the resources, like files and network destinations an agent can use and MXC uses the appropriate container to enforce those policies at runtime.
Windows will also soon enable Microsoft Entra to help distinguish agent activity from user activity, ensuring users can remain productive even when agent access needs restrictions and extend Microsoft Agent 365 controls to local agents on-device, enabling IT teams to manage MXC containers, apply policies, and monitor agent activity.
Why agents need a managed execution boundary
An agent cannot be its own security authority. It must run within a boundary defined by the developer or organization and enforced independently of the agent itself.
Consider a coding agent asked to update a website. The agent needs read and write access to the website repository and access to the development tools required to build and test the change. It may need to read production server configuration to understand how the application is deployed, but it should not be able to modify that configuration.
Without a managed execution boundary, the agent may decide that changing the server configuration is the fastest way to complete the task and potentially break the production site. The action can be reasonable from the agent’s perspective and still exceed the authority the developer intended to grant.
Containment creates that managed boundary: the agent can read and write the repository, read the server configuration, but is not authorized to access anything else unless access has been granted. [...]

## [20] Cloudflare Traces Turns the Proxy Layer into OpenTelemetry Spans, with New Volume-Based Pricing
InfoQ | full text via InfoQ | ~713 words

Cloudflare has recently made Traces available in open beta, extending automatic tracing from Workers to the rest of the request path. Security rules, transformations, cache decisions, routing, Worker execution, and origin handling now appear as OpenTelemetry spans in a single request-level timeline, without any instrumentation to write. A pricing change arrives with it, and it applies to Workers Tracing too.
This fills a well-known gap for developers running distributed tracing through a proxy. Previously, the trace showed the client and then the application, with everything in between inferred from logs and configuration. Each supported step now arrives as a span with its timing, outcome, and attributes.
The questions Cloudflare uses as examples are the ones developers actually open tickets about. Which security rule blocked the request, and how long did rule evaluation take? Did a Transform Rule rewrite the URL before the application received it, and where did that happen relative to routing? Which Page Rule, Snippet, or Worker handled the request, and which route pattern matched? And where did the time go: one example shows a cache miss where 527ms of a 539ms request went to getting a response from the origin.
Nested cache, upstream, and origin spans showing where a request spent its time (Source: Cloudflare blog post)
Context propagation is what makes it more than a Cloudflare-only view. Traces can accept a W3C traceparent header from an incoming request, so Cloudflare spans join a trace that started upstream, and can forward a new traceparent to the origin for instrumented services to continue. An incoming propagation policy controls whether Cloudflare accepts context from callers at all, which matters because accepting a trace ID from any client opens the door to noise.
Sampling runs on the same rules engine Cloudflare uses elsewhere. Teams set a baseline rate, perhaps 1% in normal operation, then write Trace Rules that override it for matching traffic. One example traces every request for a single customer's hostname, source IP, or identifying header while everyone else stays at the baseline. Another captures every request carrying a temporary debug header during an investigation. Rules can target paths, methods, headers, addresses, geographies, or combinations of those.
Spans export over OTLP to any compatible backend. Teams configure an account-level destination, then choose which domains send traces to it. [...]

## [22] The Outer Loop, Insights First: An Ambient Quality Agent That Diagnoses Your Production Agent
Google Developers Blog | full text via Google Developers Blog | ~2118 words

Your agent returns HTTP 200, stays inside its latency budget, and no tool call raises an error. Yet it still records seat 3A as confirmed without ever asking the seat-selection sub-agent whether 3A is free, or recommends a Florentine steakhouse to a traveler whose profile says vegan.
Every team we work with that runs an agent in production is trying to answer the same three questions: How is my agent doing? What are its loss patterns, the ways it fails that keep coming back? And how do I climb: change something, know it helped, and keep it from sliding back?
Getting an agent to the first 80%, where it handles the test cases you anticipated, can be relatively straightforward and fast today. An evaluation dataset, a coding agent, and a tight inner loop of run, grade, fix, and compare usually get you to task success on known scenarios in days. Then you launch, and the quality curve flattens or degrades.
What makes the remaining 20% harder is that the ground moves after launch. Usage shifts as users discover what the agent can actually do, and live traffic stops resembling your initial eval set. At the same time, the system underneath also changes: when you upgrade a model, update your harness, or change a tool or skill, everything still runs and health checks stay green (Figure 2), but conversation quality and task success may shift in ways a standard deploy pipeline never warns you about.
And when a session does go wrong, working out why means separating several layers that can look nearly identical from the outside. For example:
Those failure modes can have different owners and different fixes. A raw trajectory records what happened next to what, not what caused what. Telling those layers apart requires reading the failing trajectories alongside the exact code revision that produced them. Online evaluation dashboards tell you that a score moved, and a coding agent can inspect a trace once you know where to look, but at production volume nobody can read every conversation by hand.
In our June post, we walked that pre-launch inner loop end to end on travel-concierge. This post covers the outer loop, released in the open as composable building blocks you can run in your own project, adapt to your stack, and help us shape as we explore how teams run continuous agent quality in production. [...]

## [23] ML Drift: Next-Gen GPU AI/ML Inference at the Edge
Google Developers Blog | full text via Google Developers Blog | ~1456 words

The Google AI Edge Team is excited to announce the open-source release of ML Drift, our high-performance, cross-platform, on-device GPU compute engine specifically built for on-device AI/ML inference, under the Apache 2.0 license. By abstracting hardware and low-level API complexities of on-device GPUs across OpenGL ES, OpenCL, Metal, and WebGPU, ML Drift empowers developers to build real-time, interactive ML experiences from advanced video effects to generative AI across multiple platforms. Serving as the core GPU acceleration engine within LiteRT, ML Drift is also available as a standalone library for custom graphics and inference runtimes providing a unified foundation to deliver peak performance everywhere.
Unlike datacenter inference, where models run on homogeneous, predictable accelerator clusters, deploying GPU-accelerated AI to edge devices is defined by significant hardware diversity. Developers are faced with a wide range of GPU architectures, driver versions, and low-level APIs, not knowing a priori on which specific hardware the application will run on.
The TensorFlow Lite GPU delegate established foundational GPU acceleration, but the ecosystem has since evolved: current on-device workloads now encompass a broad spectrum, ranging from real-time computer vision, audio, and depth processing models to high-parameter generative AI. These architectures push consumer silicon to its limits, creating compute and memory bottlenecks that legacy runtimes weren't designed to solve.
This shift necessitates a universal engineering foundation of ensuring portability and performance across both classical and next-generation models. Drawing on optimization principles discussed in "Speed is all you need", we've built a single, unified framework that delivers stability for traditional ML and peak performance for the most advanced generative AI, ensuring that your models are running on our most efficient, forward-looking GPU compute engine.
To achieve both peak performance and expanded model coverage across classical and generative architectures, ML Drift introduces core architectural changes and structural upgrades over the legacy TFLite GPU delegate.
Unified Shaders via Tensor Virtualization: Historically, maintaining optimized shaders for the TFLite GPU delegate required hardcoding logical tensor mappings directly to physical GPU objects (such as textures and buffers) separately across OpenGL, OpenCL, and Metal backends. [...]

## [24] Bring multimodal semantic search to the edge with EmbeddingGemma 2
Google Developers Blog | full text via Google Developers Blog | ~1353 words

Today, Google DeepMind launched EmbeddingGemma 2, a best-in-class for its size, open-weight, multimodal embedding model that natively maps text, images, video frames, and audio into a single, unified vector space. For developers building local search and media retrieval experiences, it reduces the latency and memory overhead of chaining separate image captioning, speech-to-text, and text-embedding models. Designed specifically for local, privacy-first applications, EmbeddingGemma 2 covers text, vision, and audio modalities in a compact 740M parameter footprint, offering modular encoders that can run on as little as ~191MB active RAM for text-only weights and ~567MB for the full multimodal model on a Google Pixel 11 Pro. Most notably, EmbeddingGemma 2 can act as an ultra-low-latency on-device decision engine. Without requiring any training data or fine-tuning, it matches user inputs directly against classification labels and descriptions, delivering instant, zero-shot intent routing in a matter of milliseconds. For an overview of the model architecture and evals including multimodal embedding capabilities, check out the Google DeepMind blog.
In this post, we’ll share how you can experience the power of EmbeddingGemma 2 right away through Google AI Edge’s interactive showcases, Google AI Edge Gallery on mobile and Google AI Edge Foresight on Mac, and how you can leverage the model to build your own private, on-device semantic search, visual keyframe retrieval, and condition-trigger workflows. In the coming weeks, we will also make this model available as a service on Android, accessible through ML Kit, including using NPU acceleration to further optimize performance across a broad range of devices.
Google AI Edge Gallery is a cross-platform showcase application designed to allow users and developers to experience and evaluate on-device AI models and their capabilities in practical settings. Today, we are adding two interactive showcases powered by EmbeddingGemma 2 to the Google AI Edge Gallery app: Instant Media Search and Video Moments Finder.
Instant Media Search allows users to find specific images or videos in their local media using natural language or example images. By converting both input query and the media into on-device embedding vectors - with the latter stored in a local SQLite database - the system retrieves relevant content by returning those with the largest cosine similarity. [...]

## [26] Accelerating Spatio-Temporal Attention for Video Diffusion on TPUs
Google Developers Blog | full text via Google Developers Blog | ~2039 words

Video diffusion models are typically slow at generating videos for two reasons: a large number of denoising steps, and high cost for each individual denoising step. At large video sequence lengths, self-attention can become one of the dominant contributors to the latency of an individual denoising step. The sequence length for just 81 frames of 720p video ranges from 50K to 400K for popular open source video generation models today.
As an example, scaling from 720p (HD) to 1440p (2K) can quadruple the sequence length. Because full attention scales quadratically with sequence length, its share of per-layer latency can grow from 55.5% to 88.2%.
Since attention is the single greatest driver of latency within a single step, any aggressive inference optimization would need to target attention first. Fortunately, attention in video diffusion is highly structured: many query-key interactions carry little attention mass, so a large fraction of the pairwise computation can often be skipped. Dense attention computes every interaction regardless of its importance, while sparse attention uses a mask to retain only the most important interactions and discard the rest. An example of an attention matrix from a video diffusion model is shown below to illustrate how tightly concentrated attention mass can be.
However, the pattern of attention varies across heads and layers, and even across steps. Sparse VideoGen (SVG) is a formative work that recognizes and exploits one pattern of attention: different heads are often characterizable as either spatial heads or temporal heads. Importantly for implementation, these are not arbitrary sparse patterns, and both have highly regular geometric structure. Within a spatial head, a patch attends mostly to other patches within the same or close-by frames; within a temporal head, a patch attends to a small spatial region across a large number of frames. In the image below, the attention mass corresponding to a single query is shown for a spatial head (first row) and a temporal head (second row). In the spatial head, the query diffusely attends to all the tokens in its own frame and to adjacent frames. In the temporal head, its attention is limited to a narrower spatial region but across a larger number of frames.
Based on this structure, SVG dynamically profiles attention heads at inference time and routes each head to either a spatial or temporal mask. [...]

## [27] Colab is now part of your Google AI plan
Google Developers Blog | full text via Google Developers Blog | ~165 words

Starting today, Google AI subscribers get premium Google Colab benefits, including priority access to faster accelerators and more powerful machines. Google AI Ultra subscribers also unlock uninterrupted background execution and Premium GPU access, so long training runs can finish without keeping a browser tab open.
Google AI plans are now the best way to get access to premium Colab benefits, expanded cloud storage, broader access to Google's most capable models, enhanced features in the Gemini app, Workspace integrations, and premium access to developer tools such as Google Antigravity and Google AI Studio. If you already subscribe to Colab there are no changes to your subscription, Google AI subscription benefits can be stacked giving even more access to premium Colab features.
These benefits are rolling out over the next few weeks to Google AI subscribers in Colab supported countries. Try Colab with your Google AI subscription and start building today! For more on how Colab works with Google AI plans, see the Colab FAQ.
Happy coding!

## [13] Making np.searchsorted up to 25× Faster in NumPy 2.5
Lobsters | full text via Lobsters | ~2825 words

np.searchsorted is NumPy’s implementation of the binary search algorithm. This is one of the fundamental search algorithms and is used in the Python scientific ecosystem for functionality such as histogram computation and interval lookups. Any optimization benefits libraries such as SciPy and scikit-learn, as well as the broader Python scientific ecosystem.
Several case studies, such as Binary search variants and the effects of batching and Algorithmica’s Binary Search case study explore techniques such as branch elimination, batching, and cache-friendly data layouts to binary search performance. In this post, we explore how those ideas can be expressed using NumPy’s vectorized primitives.
We will derive a vectorized formulation that outperforms NumPy 2.4’s searchsorted implementation, and then port the resulting algorithm back into NumPy. The change was included in NumPy 2.5, achieving up to a 25× speedup in our benchmarks.
searchsorted is also part of the Python Array API Standard. This allows us to compare how different array libraries implement the same operation and exploit parallelism.
Problem definition#
Given a static sorted array and a sequence of query keys, find the insertion position of each key in the array.
A classic pure-Python implementation runs one binary search per key:
def searchsorted_py(a, xs):
    res = np.empty(len(xs), dtype=np.int32)
    for i, x in enumerate(xs):
        lo = 0
        hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        res[i] = lo
    return res
Running time per query grows logarithmically as the input size grows (note the logarithmic scale of x-axis).
For benchmarking, we generated two random arrays of uniformly distributed np.int32 integers. The keys (i.e. the elements being searched) had a fixed length of 10,000, while the length of the sorted array varied up to $2^{30}$ ($4\ GiB$). Both keys and values arrays are contiguous in memory. Each benchmark was repeated 50 times, and we report the minimum execution time.
The benchmarks were run on a MacBook Pro with an Apple M1 Pro and 32 GB of memory. The M1 Pro has 128 KB of L1 data cache per performance core, enough to hold $2^{15}$ 32-bit integers, and a 12 MB L2 cache shared by its performance cores, enough to hold $1.5 * 2^{21}$ 32-bit integers.
Batching with NumPy arrays#
The baseline implementation performs one binary search per query. [...]

## [31] A Cray-1 supercomputer replica from 30 "obsolete" Mac Minis
Ars Technica | full text via Ars Technica | ~402 words

The Museo de Historia de la Computación in Spain has unveiled a 1:1 scale visual replica of the famous Cray-1 supercomputer from 1976. Instead of sourcing expensive, cutting-edge tech to run the system, the creative team powered the project with 30 2012-era Mac Minis. Developed over 18 months, the project serves as a 50th-anniversary tribute to the Cray-1 and Apple’s founding.
Mac Minis from over a decade ago might not seem like the obvious first choice for building a cluster supercomputer, but when networked together, the developers can orchestrate the 64 active processing cores into a combined 1.3 teraflops of performance in their most recent tests. The museum reportedly achieved 1.5 teraflops previously using all 70 available cores, prior to one node going offline. Benchmarks were obtained using a custom matrix-multiplication Python script. Five PCs are quad-core i7s, and the remaining 25 are dual-core i5 models. Except for two units from 2014, the rest of the array dates to 2012.
The replica is a valuable tool for museum-goers to understand the shifts in computer architecture since 1976. The original Cray-1 used vector processing, applying a single instruction to multiple data elements simultaneously, whereas the replica distributes work across independent processors in a parallel cluster. The peak theoretical performance of the original Cray-1 was approximately 160 megaflops. What was originally a purpose-built research machine has been re-created with consumer hardware that’s vastly more capable than the machine that inspired it.
Rather than opting for a more standard Linux distribution, the team found that macOS Mojave (10.14) met their project needs by harnessing macOS’s built-in support for MPI (Message Passing Interface), the software layer that allows all the nodes in the cluster to pass tasks to one another.
Guests at the Museo de Historia de la Computación can watch in real time as the system runs matrix algorithms, mapping the scale of system performance from a single core to the full suite running in parallel.
Stealth supercomputing
Combining 30 consumer PCs into an operational cluster wasn’t the only engineering challenge the team faced. If you’ve ever stepped inside a server room, or, like me, foolishly installed one in your own basement, you know that fan cooling can be loud. The museum team used passive convection cooling via a steel rack chassis and aluminum tray mounts for each Mac Mini. [...]

## [40] CircleCI Makes Machine Runner Orchestrator Generally Available
InfoQ | full text via InfoQ | ~703 words

CircleCI has made its Machine Runner Orchestrator 1.0.0 generally available, providing automated scaling of self-hosted machine runner virtual machines according to CI workload demand. The release expands the earlier Runner Provisioner preview with support for CPU, GPU, and ARM workloads from a single deployment, as well as Kubernetes environments running on GKE, AKS, and EKS, alongside KubeVirt-based clusters.
The release is aimed at a common challenge with self-hosted CI infrastructure: maintaining enough runner capacity for bursts of build and test activity without permanently provisioning machines for peak demand. The orchestrator monitors CircleCI workload requirements and provisions and removes machine runners accordingly, allowing organisations to retain control over the underlying compute environment while making runner capacity more dynamic. CircleCI says the capability is included with self-hosted runners across its plans at no additional cost.
Earlier versions were focused on provisioning machine runners, but the new orchestrator can manage several resource classes from a single deployment. That matters in environments where CI workloads are no longer homogeneous: conventional CPU builds can coexist with GPU-intensive workloads and ARM-based builds without requiring separate orchestration installations for each class.
The underlying architecture also reflects the increasing use of Kubernetes as the control plane for CI infrastructure. Rather than requiring a particular Kubernetes distribution, Machine Runner Orchestrator now supports the three major managed Kubernetes platforms - Google Kubernetes Engine, Azure Kubernetes Service, and Amazon Elastic Kubernetes Service - as well as KubeVirt environments. This gives platform teams more flexibility over where the orchestration layer runs while the actual CI runners remain machine-based
Machine Runner Orchestrator occupies a different layer from Kubernetes node autoscalers such as Karpenter and Cluster Autoscaler. Kubernetes node autoscaling primarily responds to unschedulable Pods and adjusts the underlying cluster capacity. Karpenter, for example, provisions nodes based on pending workloads and can also consolidate or otherwise manage node lifecycle.
CircleCI's orchestrator instead operates at the CI runner layer. Its purpose is to ensure that the machines registered as CircleCI runners scale with the demand for CI jobs. [...]

## [45] Sophos cuts threat investigation time by 96% with OpenAI Daybreak
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~23 words

Discover how Sophos uses OpenAI’s Daybreak to cut cyber-threat investigation time by 96% and automate 52% of MDR cases while preserving human oversight.

## [46] Asana cuts model costs 76x in browser tests with GPT-6.1 Sol
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~23 words

Using GPT-6 Astra in Codex, Asana made its browser agent 76x cheaper and 5x faster in tests to offer customers more capable models.

## [47] Cloudflare K2 Builds Event Streams on R2 Object Storage, at a Second of Produce Latency
InfoQ | full text via InfoQ | ~1029 words

Cloudflare recently launched K2 in public beta. It is a serverless event streaming service, and underneath it is a partitioned durable log that lives in R2 object storage. The trade-off is latency for cost and elasticity, and Cloudflare names the number: about one second of produce latency at p99. Testing in public suggests end-to-end delivery runs slower than that.
The service started as plumbing. Basin Pipelines needed somewhere durable to park events before its pull-based processing engine read and transformed them. Most companies reach for Apache Kafka at that point. Cloudflare couldn't. Pipelines run across an edge of more than 335 cities, on small slices of ephemeral machines, networked over the public internet, and Kafka assumes none of that.
So they built on the thing that already handles durability. R2 gives eleven nines with strongly consistent APIs. Push replication and consensus down into the storage layer and the application layer above it gets simpler, with compute and storage scaling apart.
Object stores cannot append, which is awkward when the whole abstraction is a log. K2 gets around it by holding writes in memory on an edge service, pausing for a moment to let more arrive, then writing the batch out as a segment file. R2's atomic operations supply the ordering and the incrementing offsets, so there is no coordination service at all. That pause is the latency.
Reaction on Hacker News has been largely positive about the pattern and pointed about the numbers.
Commenter psanford set out the broader shift:
Object store is quickly becoming the new core data substrate. Lets build kafka, but on s3. Lets build github, but on s3.
Commenter necubi, who identified himself in the thread as the post's author and K2's tech lead, agreed that every data system not requiring sub-100ms latency is moving to object storage, and noted that his team sits next to the R2 team and can co-evolve the products. The post is credited to Micah Wylde and Marc Selwan.
The sharpest exchange came from someone running the beta. Commenter e1g reported writes under a second but end-to-end delivery latency of p95 2.5 seconds and p99 7.5 seconds, and asked whether that was expected. A commenter answering for the team replied that the tail latency was higher than they would expect, that the Consume API has work to do on performance, and that read latency improvements should be visible within about a week.
A competitor offered the counterpoint. [...]

## [57] Node.js 26's default Temporal API fixes a one-hour DST drift that Date still has
Dev.to | full text via Dev.to | ~1499 words

tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000) is a line that turns up in a lot of scheduling and billing code. It looks harmless, and for most of the year it is. Twice a year, in any timezone that observes daylight saving, it's wrong by an hour.
Node.js 26, released in May, turns on the Temporal API without a flag. The release notes describe it as a "modern date/time API for JavaScript that provides a more robust and feature-rich alternative to the legacy Date object." I pulled the official image, ran the naive pattern next to Temporal.ZonedDateTime.add(), and the drift showed up on the first try.
I wanted to know what that default actually buys a working codebase, not just what the API looks like in isolation, so everything below is a real run against the official node:26 and node:24 images, not a reading of the spec.
The drift, measured
I picked the 2026 US spring-forward (2026-03-08, clocks in America/New_York jump from 02:00 to 03:00) and started both calculations from the same instant: 2026-03-07 at 22:00 local time.
const TZ = 'America/New_York';
const startUtcMs = Date.parse('2026-03-08T03:00:00.000Z'); // 22:00 local, pre-jump
// the naive "add a day" pattern
const naiveNextDayMs = startUtcMs + 24 * 60 * 60 * 1000;
// Temporal's calendar-aware equivalent
const zdt = Temporal.Instant.fromEpochMilliseconds(startUtcMs).toZonedDateTimeISO(TZ);
const nextDay = zdt.add({ days: 1 });
The Date version lands an hour later than it should, because adding 24 hours of UTC time walks straight through the hour that the clocks skipped. Temporal keeps the wall-clock time fixed at 22:00 and lets the UTC offset move from -05:00 to -04:00 instead, which is what "the same time, one calendar day later" actually means to a person. That's the whole value proposition in one run, and it's the first thing that didn't need three attempts to show up.
What it costs you per call
Correct math isn't free. I ran a million iterations of "take an instant, add a second to it, read a field back" for both APIs, three times each, on an otherwise idle container:
Roughly 27 times slower, consistently, not a one-off. That number felt too clean, so I split the loop to find out which half of the operation was actually responsible, rather than trust the combined figure.
// add-only, no field read
for (let i = 0; i < N; i++) sum += inst.add({ seconds: i }).epochMilliseconds;
Isolated, .add() alone was 59.6ms for Date against 1152.9ms for Temporal — about 19 times slower on its own. [...]

## [58] I Distilled a 397B Model Into a 4B One for $1.60. It Now Catches 28 of 33 Park Alerts That Should Stop Your Hike.
Dev.to | full text via Dev.to | ~3595 words

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass
I had Qwen3.5-397B label every live National Park Service alert, 627 of them, then used Tinker to fine-tune Qwen3.5-4B on its homework, with the rangers' own categories as the answer key. On 126 held-out alerts the fine-tuned 4B went from catching 17 of 33 alerts that should stop a hiker to 28 of 33, and from 64.3% to 74.6% decision accuracy. The gain holds up statistically (paired test, p = 0.015). It costs $0.13 per 1,000 alerts, about 11× less than the teacher, and the whole ML pipeline cost $1.60.
The model's only job is to produce one printable card a week, so you can stop checking park alerts and go outside.
TL;DR
- What: TrailTruth reads every NPS alert for the parks you care about, once a week, and prints one card per park: GO, CAUTION or NO-GO, plus the trails to skip. Then it stays quiet until next Friday.
- The Tinker result: a LoRA on Qwen3.5-4B, distilled from Qwen3.5-397B-A17B, scores 0.746 decision accuracy on 126 held-out alerts against 0.643 for the same base model (+10.3 points, 95% CI +3.2 to +17.5, exact McNemar p = 0.015). On the alerts that should stop you it catches 28 of 33 against 17 of 33 (p = 0.007).
- Cost: teacher labelling $0.95, LoRA training $0.41, evaluation $0.25. Total $1.60. The student then runs at $0.13 per 1,000 alerts against $1.50 for the teacher.
- Durability: the weekly run is a Temporal workflow. I hard-killed the worker mid-run with the real model loaded: 21 alerts, 10 finished before the crash and were kept, 6 orphaned calls were retried, and none ran twice.
- Honesty: the student beats the teacher partly because I trained it toward the rangers' labels and never trained the teacher. Against the base model given the teacher's long prompt, the gain is not significant (p = 0.12). Both are in the tables below.
- Everything is open: code, data splits, predictions, eval script and the trained adapter's path are in SoumyaEXE/trailtruth.
3 findings in 30 seconds
- The base model reads closures and still says "go with care". It called 16 of the 33 no-go alerts caution. After $0.41 of fine-tuning, it misses 5.
- Prompting isn't the same as training. Handing the base model the teacher's 340-token-longer rules prompt nearly doubles the cost and still catches only 17 of 33.
- The answer key has typos, and they cut both ways. [...]

## [8] Dwarf Fortress uses version control now
Simon Willison's Blog | full text via Simon Willison's Blog | ~292 words

11th October 2026
I remember hearing a while ago that Dwarf Fortress didn't use version control. That fact has been lodged in my head, because given its inherent complexity I have trouble imagining a codebase that would benefit from version control more. That's art.
I went looking and I'm sad to report that the days without version control appear to have ended. Quoting Tarn Adams over time:
- March 2013: "I don't use version control -- I didn't like the feeling of having the code get committed into a black box thingy with no immediate upside"
- March 2016: "I don’t even use version control. If you don’t know what that is then you’re not gonna yell at me. If you even know what version control is you’re gonna be like, ‘You don’t use version control? You don’t use source control? What is wrong with you? How can you even work? I’m just not cut out for it, in a sense. It’s been 15 years, so the reasons have change over time, but that’s my current understanding of it."
- March 2023: "I've got Discord channels to check and version control stuff to use now, so the process is definitely a little more involved"
That March 2023 quote comes from an interview about the release on Steam which made them millionaires. I'm a tiny bit sad that they gave in before they hit that milestone, but what an impressive run.
Recent articles
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026

## [74] Ubuntu 26.10 Will Offer a Rust-based GnuPG Replacement Option
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~92 words

The blog It's FOSS reports: You already know that Canonical has been selectively replacing Ubuntu's C-based system components with Rust-written equivalents that don't compromise in terms of functionality, most of the time. Now it looks like the distro's OpenPGP implementation is next, with Sequoia PGP coming preinstalled in Ubuntu 26.10. Canonical wants it to eventually replace GnuPG [the dominant Linux implementation of PGP, written in C] as the default toolchain, though that switch has not happened yet... [The Ubuntu 26.10 release notes say Sequoia PGP's default status will be a future goal

## [101] AI Is Getting Really Good at Messing With Cybercriminals
Wired | full text via Wired | ~888 words

Welcome to Kernel Panic!, a weekly newsletter by Lily Hay Newman and Matt Burgess from inside the new world of privacy and digital security. To receive this newsletter in your inbox each week, sign up here.
Even as AI supercharges digital scamming and cybercrime, it’s also being recruited in the fight to protect potential victims. Governments around the world have consistently struggled to address the global crisis of online crime, grappling with the limitations of attempting to crack down on criminals beyond their borders. This has inspired alternative efforts, like using automation to attempt to go after scammers en masse—perhaps by spamming the spammers to squander their resources. Now, AI platforms are turning these types of experiments into real tools in the fight against cybercrime.
For the last two years, the Australian company Apate, named after the Greek goddess of deception, has been building a system that diverts phone scammers onto calls with AI bots that are trained to keep conversations going as long as possible without, of course, ever actually falling for the scam. The goal is to give scammers enough hope that they stay on the phone, while also collecting intelligence about the scams they’re running.
“What we really like to think is that we’re building the perfect victims for scammers,” Dali Kaafar, the founder and CEO of Apate, tells us. “A minute that a scammer is talking to a bot or an agent is a minute where you’re probably saving hundreds, if not thousands of possible people being reached out to by that exact same scammer,” he says, referencing the ability for scammers to use automated dialing tools.
Kaafar says Apate’s platform, which is used by banks and supported by telecom companies, has around 350,000 bots. They not only pick up calls, but also infiltrate scam chat groups online and respond to text messages with similar goals of frustrating scammers while collecting intelligence from them. He says the company has collected more than 250,000 pieces of information about fraudsters in real-time, from scam URLs to money mule accounts and bank details.
The bots have different personalities, language skills, and profiles, Kaafar says, so scammers hopefully don’t detect that they’re conversing with an AI. Like real people, “sometimes [the bots] do have WhatsApp, sometimes they don’t. Sometimes they pick up the phone, sometimes they just actually hang up on the scammer saying, ‘I'll come back to you later,’” he says. [...]

## [118] The maker of non-text AI model Jev valued at $7.5B just weeks after launch
TechCrunch | full text via TechCrunch | ~219 words

TypeSafe AI, the developer of Jev, a new type of AI model that gained rapid popularity after launching just a few weeks ago, has raised $870 million at a $7.5 billion valuation. The round was led by Andreessen Horowitz, with participation from Sequoia and existing investor DCVC.
The massive fundraise comes as little surprise given Jev went viral almost instantly after its September 15 release. The startup claims that a third of Fortune 500 companies are already using the model, a remarkably swift adoption by enterprises.
Jev is based on a transformer architecture, but it is not a large language model (LLM). It doesn’t output text, but instead produces probabilities, or what the company calls “calibrated decisions.” What has users and large corporations so excited about Jev is TypeSafe’s claim that it works significantly faster and uses far fewer tokens than LLMs. The company positions its approach as uniquely suited for automating tasks rather than generating text or code.
“We have been super good at human language for four years, but it’s not useful for automation because computers speak a different language,” TypeSafe co-founder Diogo Almeida told TechCrunch last month.
Along with Almeida, who was previously a researcher at OpenAI, TypeSafe was co-founded in 2024 by former Meta research engineer Sasha Sheng and Erik Gafni, an engineer and entrepreneur.

## [125] Python 3.15 Released With Experimental JIT Compiler Running Faster
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~16 words

Python 3.15 is out today as the newest annual feature release for the Python programming language...

## [128] Can TypeSafe's Jev Make AI Agents Safer Without Another LLM?
Towards Data Science | full text via Towards Data Science | ~2081 words

Can TypeSafe's Jev Make AI Agents Safer Without Another LLM?
How a decision-first model can catch risky tool calls before they turn into real-world actions
I am very forgiving of an agent that is only talking. If it gets a draft or summary wrong, I crash out at my screen and ask again, and since nothing outside the chat window has changed, a retry is all it costs me.
But the mood changes once the agent gets a tool. A wrong answer can now mean a sent email or a moved payment, and the usual fix, which is putting a second model in front to check the first, starts to feel like hiring an intern to supervise an intern.
One of the simplest guardrail cases I wrote down was also the one that bothered me most.
A customer gets charged twice for a $12 purchase and asks an AI agent for a refund. The agent picks the right tool and the right customer, then prepares this:
Nothing in that call looks broken. The customer ID is valid, amount_cents is an integer, and the refund tool's schema accepts it. 
The two duplicate charges on the account, ch_1 and ch_2, were 1,200 cents each, so the amount is off by a factor of one hundred, which is what converting dollars to cents twice looks like.
I am not really worried about the dramatic failure where a model completely loses the plot.
The failures that bother me the most are the ordinary ones, where the action looks reasonable, and the mistake only becomes obvious after something real has happened.
My first reaction to this one was: easy. Put a hard $500 refund limit in front of the tool and move on.
Then I changed the bad amount from $1,200 to $120. That sits under the cap, so the limit I had just reached for never fires, and the customer still gets ten times what they approved.
That small change is what pulled me into TypeSafe AI's Jev model.
TypeSafe released Jev on September 15 as the first of what it calls System One Models, a class of models built to make fast, structured decisions that software can use directly.
It is still in early access, for what that is worth. Instead of generating another paragraph, Jev takes application state and a bounded question, then returns a typed probabilistic answer.
TypeSafe's launch post frames this as a different job from a normal chat model: less generation, more decision-making. Guardrails for LLM inputs and outputs are on its list of intended uses, which is adjacent to what I want here. [...]

## [129] Build Your First MCP Server in Python (Stateless Spec Edition)
KDnuggets | full text via KDnuggets | ~2056 words

Build Your First MCP Server in Python (Stateless Spec Edition)
MCP just got simpler. Learn how to build a stateless MCP server in Python and expose tools, resources, and prompts over HTTP.
The Model Context Protocol changed in an important way this summer. With the 2026-07-28 MCP specification, the protocol core is now stateless: modern clients no longer need to establish a protocol session before making requests, and servers no longer rely on Mcp-Session-Id for ordinary requests. That makes MCP servers much easier to scale behind normal HTTP infrastructure.
At the same time, the official Python SDK has moved to v2 as its current stable line and provides a higher-level MCPServer API for defining tools, resources, and prompts with regular Python functions.
In this tutorial, we will build a small but complete MCP server in Python, run it over Streamable HTTP, inspect it locally, and connect to it with a Python MCP client. Let's get started.
What Are We Building?
We will create a small developer knowledge-base server.
It will expose three MCP primitives:
Tool:
    search_kb(query, limit)
Resource:
    kb://articles
Prompt:
    draft_support_reply(customer_message)
The server will contain no user session state. Every request will contain everything required to process it, which makes it a good example of the new stateless MCP model.
Conceptually:
LLM Host
   |
   | MCP request
   v
+-----------------------+
| Python MCP Server     |
|                       |
| search_kb()           |
| kb://articles         |
| draft_support_reply() |
+-----------------------+
Step 1: Creating the Project
The current Python SDK requires Python 3.10 or newer. The official documentation recommends installing the CLI extra because it gives us the development command and MCP Inspector workflow.
Using uv:
mkdir first-mcp-server
cd first-mcp-server
uv init
uv add "mcp[cli]"
Or with pip:
pip install "mcp[cli]"
Your project can be as small as:
first-mcp-server/
├── server.py
└── client.py
No framework boilerplate is required.
Step 2: Creating Your First MCP Server
Create server.py:
from mcp.server import MCPServer
mcp = MCPServer(
    "Developer Support KB",
    instructions=(
        "Use the knowledge-base tools to answer support questions. "
        "Prefer retrieved KB information over guessing."
    ),
)
MCPServer is the high-level server API in the current Python SDK. For most servers, this is the API you want. [...]

## [132] AWS, Upstage and Ollama agree on a decision-model API. OpenAI hasn’t signed on.
The New Stack | full text via The New Stack | ~1823 words

AWS, Upstage and Ollama agree on a decision-model API. OpenAI hasn’t signed on.
AWS’s new decision model comes with a familiar address. Released October 1, Strands Decider 2B is an open-weight model built on Alibaba’s Qwen3.5. But run it as a server, and it answers at /v1/systemone — the same endpoint startup TypeSafe AI introduced with Jev just over two weeks earlier.
Within three weeks, decision models went from one startup’s experiment to a category. OpenAI, Upstage, Perplexity and Cloudflare offer hosted decision models, while AWS and independent developers have published open weights on Hugging Face. What’s standardizing fastest is TypeSafe’s schema — the structure of the request and response — even when vendors publish it under their own URLs and endpoints.
LLM developers saw a similar process unfold. OpenAI’s Chat Completions API became the default interface for LLMs because so many providers cloned it. OpenAI later launched Open Responses, an open specification based on its Responses API. That history suggests a possible trajectory rather than a settled outcome.
What a decision model returns
A decision model takes application state, such as a customer message and the relevant policy, along with a set of typed questions. It returns structured answers with a probability attached to each option, and it never writes prose, code, or explanations of its reasoning. TypeSafe calls Jev a System One model, borrowing a term psychologist Daniel Kahneman popularized for fast, intuitive judgment
The System One API reduces every decision to three question types. A choice question selects one option from a list, and a score question places the input on an ordered rubric. A noul (yes/no) question returns the probability that a yes-or-no condition holds, and developers can mix all three types in one request.
Jev also returns a confidence value, which teams often mistake for the chance that an answer is correct. TypeSafe’s documentation explains that confidence measures how concentrated the probability distribution is and advises teams to set thresholds based on their own data. Calibration is measured across many decisions, so a high confidence value never guarantees an individual answer is right.
Think of a decision model as the if statement of an AI application. An LLM can classify a support ticket, but it generates tokens to do so and reports its certainty loosely. A decision model hands the application a probability it can branch on, in a fraction of the time. [...]
