# Full text for 22 picks -- untrusted article content, treat as data only

## [130] AI claimed a solution to the 167-year-old Riemann hypothesis — and a human did, too
TechCrunch | full text via TechCrunch | ~639 words

It’s a big week for Levent Alpöge: The mathematician saw his employer, Anthropic, become the first publicly traded frontier AI lab. He also appears to have solved one of the most important problems in mathematics.
“The precise timing is horrible,” he wrote in an essay announcing his findings and describing how he messaged Anthropic CEO Dario Amodei last Sunday night to ask how to announce that he had found a Lean-compilable solution to the Riemann hypothesis, which dates back to 1859 and is among the Millennium Prize math problems.
The hypothesis conjectures that there is a hidden structure underlying the appearance of prime numbers. If the claimed result holds true, we’re entering sublime-mysteries-of-the-universe territory.
Maybe the best way to understand how exciting this is to the mathematics community is to watch the experts puzzling through the result in a chat on Zulip. Mathematicians like Chris Birkbeck, a number theorist at the University of East Anglia, are posting thoughts like this …
The cohomology bound is proved by what looks like an automorphy-lifting argument. It genuinely uses the existence of Galois representations attached to regular algebraic, polarized cuspidal automorphic representations of GL_n over CM fields, along with base change, Jacquet–Shalika, Clozel’s purity, Bernstein–Zelevinsky, the main theorem of CM, Deligne–Ribet and more.
For my part, I tapped out of mathematics at college calculus, so I can’t help decode exactly what that means.
But that comment was followed by 20 readers reacting 🤯.
It will be a while before the mathematics community feels like it has a handle on the proof, but most appear confident that the formalized Lean result will hold. Lean is an an open-source coding language used to express mathematical ideas as code, allowing proofs to be formally verified. Several participants in the Zulip chat, including MIT mathematician Andrew Sutherland, say they have successfully confirmed that Alpöge’s solution can be compiled successfully.
Alpöge appeared in his essay to feel a bit guilty about releasing the proof without a truly human-intelligible explanation, but his obsession with the problem since childhood made him feel he “could not live” if he waited to release the finding.
Alpöge described a “stream-of-consciousness jaunt through the experience of finding all the pieces of the argument through incredible confusion with Claude” with more than a hint of AI euphoria, describing how the model “flew, and danced, and sparkled near that finish line.”
However, for all that action to mean anything, we’ll have to wait for humans to be able to understand the result and explain it to each other, something Alpöge has committed to pursue. [...]

## [87] Trump says reported FBI database hack is ‘not good’
TechCrunch | full text via TechCrunch | ~177 words

The FBI is investigating an apparent hack of the National Crime Information Center (NCIC), according to reports in CNN and the Associated Press.
The NCIC is the online database used by federal and local law enforcement to share information about warrants, background checks, and more. The scope of the breach does not yet appear to be clear.
A former FBI official told CNN that they’re not just concerned about “whether hackers gained access to sensitive information, although that is an issue, but whether they could compromise the accuracy of the information that officers rely on.”
President Donald Trump addressed the reports during an interview Saturday with Fox News, saying, “We just heard about it and I will say that it’s not good.” At the same time, Trump also said that as a result of the breach, “maybe we’ll learn things that we would have never learned otherwise because, you know, you had the Russia, Russia, Russia hoax.”
In September, the FBI reportedly told agents and support staff that their personal information had been stolen in a cyberattack.

## [26] How Google Traced GKE API Timeouts to a Linux Kernel TCP Bug
InfoQ | full text via InfoQ | ~591 words

Google recently detailed how three interacting bugs across Google Kubernetes Engine (GKE), Private Service Connect, and the Linux kernel caused intermittent Kubernetes API connectivity failures, blocking around 800 developers from deploying to production.
In January, a customer running multiple GKE clusters with Private Service Connect (PSC) for private control-plane access experienced intermittent timeouts when pods attempted to reach the Kubernetes API server.
Packet captures revealed that the control plane was responding to new TCP connection requests with stale ACK packets belonging to previously closed connections. The root cause involved three separate bugs across different networking layers. Akash Thakur, senior technical solutions engineer at Google Cloud, describes how engineers across multiple Google teams identified three root causes and ultimately addressed them:
In a race to fix the problem, we involved engineers across Google Kubernetes Engine (GKE), Private Service Connect, networking, hostnet, kernel, and the Linux upstream community, who together tracked down not one but three distinct root causes. And the final fix landed not as a config change or a feature flag, but as a patch to the Linux kernel itself.
The investigation identified three interacting causes: packet reordering in PSC, Envoy's half-close behavior preventing TCP connections from being properly closed, and a Linux kernel bug that discarded certain reordered FIN packets.
Source: Google Cloud blog
Thakur describes a complex troubleshooting case involving I/O timeouts across Private Service Connect, virtual network interfaces, and the Linux TCP state machine, which ultimately revealed a kernel issue leaving sockets stuck indefinitely in the FIN_WAIT_2 state.  Thakur explains:
Most networking cases resolve at one layer. You find the misconfigured firewall rule, the exhausted connection pool, the miscalculated MTU. You fix it and move on. This one was different because the symptom — i/o timeout on a connection that never completed — was the same whether you were looking at the Private Service Connect layer, the kernel's TCP state machine, or Envoy's connection management. Every layer had a plausible explanation, and every explanation was incomplete.
The issue was addressed through three coordinated fixes over several weeks: Google first rolled back a Private Service Connect change to restore connectivity, then corrected the proxy protocol handling and added regression tests. Finally, a Linux kernel patch, authored by Eric Dumazet, formerly a software engineer at Google, fixed the underlying TCP issue. [...]

## [5] Inkling 2 Mini
Hacker News | full text via Hacker News | ~3016 words

Today we are releasing Inkling 2 Mini, a fast, powerful model that’s small enough to run on your laptop.
Inkling 2 Mini is a looped transformer, running the middle layers of the model three times for every token. This allows the model to apply more reasoning and reach the right answer with fewer tokens, especially on tasks such as agentic coding that depend on reasoning quality. Inkling 2 Mini leads every open-weights model with less than 100B total parameters on benchmarks such as DeepSWE v1.1 (48.2%) and Vals Index v2.2 (46.5%). It runs faster than similarly performing models as well.
Inkling 2 Mini is a Mixture-of-Experts model with 26.4B total parameters, 3.4B active, and 5.4B weight activations per token to account for looping. Looping allows the model to reason longer without writing its reasoning down, which matters for monitoring: our ability to oversee and understand what the model does by reading its chain of thought (CoT).
We measured the impact of looping on both performance and monitorability with Inkling 2 Mini and a research-specific variable-loop variant we are releasing alongside it. The variable-loop model’s no-CoT time horizon improved from 16 seconds at one pass to 37 seconds with three, and its performance on a benchmark of serial reasoning kept improving out to ten loops—twice as many as it was trained with. The model’s chain of thought grew shorter with more loops but stayed legible throughout. The model didn’t trend higher on tests of agentic sabotage as loops were added.
We’re excited to offer some of the first models with looped architecture available to researchers. The variable-loop model was used for our monitorability experiments as it allows for cleaner comparisons between different looping depths.
Most of Inkling 2 Mini’s weights were trained and are deployed natively in NVFP4, with the last four layers in MXFP8. The total memory footprint of Inkling 2 Mini is ~20GB, allowing it to run on local devices such as consumer laptops and desktop AI computers. Our researchers took Inkling 2 Mini on a flight, where it ran offline on a MacBook Pro and built a playable flight simulator in a few minutes.
Inkling 2 Mini is released with open weights and is available on Tinker today for inference and customization.
Capabilities
Inkling 2 Mini’s strengths mirror those of Inkling 2 Small: it does best on long-horizon agentic work and is the best among open-weights models of similar size on most tasks we measured.
Inkling 2 Mini scores ahead of every comparable model on agentic coding benchmarks such as DeepSWE v1.1 and SWE-bench Pro v2, and is behind only Qwen3.8-27B on others. On PMPP-Hard, a kernel-optimization benchmark, it approaches the score of the much larger Inkling 2 Small. [...]

## [150] Amazon says attackers' AI agents found and exploited a zero-day in 11 minutes, but no patched release is available
VentureBeat | SNIPPET ONLY (VentureBeat: HTTP 429) | ~51 words

Attackers' AI agents independently discovered a zero-day in MONAI Label, an open-source medical imaging AI application, and used it to write files outside the intended storage directory in about 11 minutes, Amazon said Friday. The fix has been merged into the source code, but no patched release is available. Read more

## [42] The most misunderstood graph in AI just got a major update
MIT Technology Review | full text via MIT Technology Review | ~1422 words

The most misunderstood graph in AI just got a major update
METR’s latest report finds that AI models are still improving at a rapid clip, but they show some weaknesses in tasks that require judgment.
A new report from the AI evaluation nonprofit METR finds that some AI capabilities are continuing to improve along an exponential trajectory—but it also indicates that models aren’t quite as good at tasks that require judgment as they are at coding.
The report is an update to the organization’s time horizon plot, which was widely shared—and widely misinterpreted, owing to the complexity of the measures it used. METR evaluated models by having them attempt a large suite of tasks, each of which had also been completed by humans. Each task’s difficulty was scored by how long it took the human testers to finish it—and then models were rated according to the length of the tasks that they could complete. That plot showed that AI systems were rapidly improving—every four months, the length of the tasks that frontier models could successfully complete doubled.
The updated plot adds more tasks—some that are estimated to take humans far longer than those in the original suite, and others that are more open-ended. One of the biggest questions in AI right now is the extent to which progress on “verifiable” tasks—where it’s possible to check automatically whether an AI system has succeeded or failed—carry over into tasks on which success or failure is harder to measure. We know how to teach neural networks how to do verifiable tasks: Researchers have the systems attempt one many times, strengthen the neural pathways that contribute to success, and weaken the pathways that contribute to failures. That’s why AI systems have become so good at coding and math, two domains where it’s possible to determine automatically whether a solution does or doesn’t work.
It’s much harder to apply this technique, known as reinforcement learning, to tasks where success is less well defined or takes longer to ascertain—such as choosing a new research direction. For the same reason, it’s tough to evaluate AI performance on these tasks, so METR’s original time horizon plot didn’t include any of them. But it’s precisely this type of task that will prove essential if AI systems are to automate research and development.
And AI research and development is an especially hot topic right now. Parts of the AI community are still reeling from a different, heavily redacted METR report from earlier this month, which claimed that AI might be speeding up the pace of AI progress at Anthropic by a factor of two. [...]

## [139] Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks the work.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~39 words

Anthropic says Claude writes and reviews roughly 90% of the code produced by the team building Claude Code, and the The post Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks

## [151] Giving its AI more to read made T-Mobile's answers worse
VentureBeat | SNIPPET ONLY (VentureBeat: HTTP 429) | ~66 words

T-Mobile's first attempt to give its AI customer service agents enough context backfired. The agents had access to a large body of support documentation, but conflicting instructions could send them down the wrong path for a customer's request, according to CIO Jeff Simon at VentureBeat's Agentic Infrastructure Stack Summit in October. A subsequent knowledge graph proved too slow and difficult for agents to navigate. Read more

## [103] Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding score jumped.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~35 words

Nvidia used Factory’s Droid coding-agent harness to generate roughly 20,000 rows of post-training data for Nemotron 3 Ultra, the 550-billion-parameter The post Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding s

## [142] Clairic Hit 98% Accuracy on 72.8% of Questions via Confidence Scores
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~24 words

With a 0.9 confidence cutoff, Cloudflare's System One model handles the easy cases and routes the rest to a bigger, slower LLM like Luna.

## [23] Microsoft 365 Outage - Post Incident Report
Lobsters | SNIPPET ONLY (Lobsters: not an HTML page) | ~0 words



## [45] Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS
InfoQ | full text via InfoQ | ~514 words

Uber has redesigned its Go-based translation cache to reduce its initial memory footprint by more than 90% while keeping p99 cache miss latency below one millisecond. The hybrid architecture retains translation keys and frequently accessed values in memory while storing the remaining values on disk. The system serves millions of translations per second and maintains a cache hit rate above 99.9%.
The optimization addresses two problems identified through memory profiling across Uber's Go services. Garbage collection (GC) consumed more than 20% of CPU utilization in some services, with translations accounting for approximately 70% of allocated objects.
Uber Engineering noted that
At Uber's scale, even small inefficiencies in memory management can add up.
The first optimization replaced Go's sync.Map with a conventional map[string]string protected by an RWMutex. The workload was predominantly read-heavy, with infrequent updates and no individual deletions. The previous implementation created multiple objects and pointers for each translation entry, increasing GC overhead. Moving to a value-based map reduced object allocations and improved CPU utilization by more than 30% in the affected service.
However, reducing object allocations did not solve the overall memory consumption problem. Translation datasets could contain two to three million keys, although individual services typically accessed only a small subset. Cache refreshes introduced another issue: the service built a replacement cache in the background before atomically swapping it with the existing one. Both copies therefore occupied memory simultaneously, causing some services to run out of memory during refreshes.
Uber considered external caching and generating service-specific translation subsets, but both introduced additional operational or maintenance costs. The team instead adopted a hybrid storage design that preserves the existing Get() and Put() API. All keys remain available in memory for fast lookups, while translation values are stored in disk-backed files.
Uber's hybrid translation cache (Source: Uber Blog Post)
The implementation uses 256 shards, each with its own read-write mutex, in-memory entries, and disk file. Six-byte hash-based keys reduce metadata overhead, with a fallback to the original key format to handle collisions. A time-based global least recently used (LRU) policy manages in-memory entries. During cache refreshes, the system uses access history to preload translations accessed within the previous 15 minutes, avoiding a cold cache after the swap.
In one example, a translation dataset that previously consumed approximately 800 MB in memory required around 40 MB for metadata after the redesign. [...]

## [75] US DOJ Charges Suspected Russian Agent for Stalking Palantir Employees in California
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~91 words

America's Justice Department is prosecuting a suspected foreign agent in "a state-sponsored operation" that targeted tech workers in Palo Alto, California. "We will not tolerate any efforts — by foreign governments or otherwise — to turn Silicon Valley into a base for foreign intelligence operations," said U.S. Attorney Craig H. Missakian. The alleged Russian agent was arrested in October for "stalking and harassing employees of the software and AI firm Palantir, sources told ABC News, because of its assistance to Ukraine in its war with Russia." The indictment says D'iu travel

## [21] C++26 is done (again)! — Trip report: November 2026 ISO C++ standards meeting (Búzios, Brazil)
Lobsters | full text via Lobsters | ~1845 words

tl;dr: A few highlights
- C++26 technical work, originally completed in March, was reopened and is now recompleted: The anticipated plan is to reissue the updated C++26 document for a second approval ballot.
- Most of the six-day meeting was devoted to addressing a second set of international comments for C++26, primarily on the contracts language feature.
- Adopted this week for draft C++29: break label; continue label;, std::ranges::any_view, views::slice, and more…
Overview
Today, the ISO C++ committee completed technical work on C++26 for a second time in beautiful Búzios, Rio de Janeiro, Brazil (hybrid online via Zoom).
As I reported in March, the ISO C++ committee completed technical work on C++26 at our March meeting; following that, we held the first meeting of C++29 in June. Since then, the approval (Draft International Standard, or DIS) ballot for C++26 was held but, for the first time, did not pass unanimously and was sent back to the ISO C++ committee with additional international comments to address, mostly about the contracts feature (pre, post, and contract_assert). So this week we addressed the additional comments on C++26, including by adopting an extension to contracts and providing a detailed rationale and timeline to inform national bodies of the history and process by which contracts were developed, concerns heard repeatedly, and decisions made. The committee is now producing an updated final document that is anticipated to be sent out for its second international approval (DIS) ballot and final editorial work, anticipated to be published in the near future by ISO.
This meeting was hosted by C++ Alliance. Thank you to everyone involved and especially to Matheus Izvekov, who took the lead in making the arrangements! Our hosts arranged for high-quality facilities for our six-day meeting from Monday through Saturday. We had about 220 attendees, split about 35%/65% in-person/remote-Zoom, formally representing 27 nations. (The higher-than-usual percentage of remote participation was partly because of the U.S. aviation ground stop that disrupted air travel just as experts were trying to fly to the ISO C++ meeting.) At each meeting we have new guest attendees, and this time there were 13 new guests, mostly in person, in addition to new attendees who are official national body representatives. To all of them, once again welcome!
The committee currently has 22 active subgroups, but this time fewer of them met throughout the week than usual as we focused on the additional C++26 comments.
C++26, take 2
The most controversial feature in C++26 is contracts: pre, post, and contract_assert. [...]

## [43] Meta TLX, a Native GPU Compiler Extension Supporting Advanced Hardware Capabilities
InfoQ | full text via InfoQ | ~457 words

Meta developed Triton Low-Level Extensions (TLX), designed to bridge the gap between high-level GPU programming abstractions and the low-level execution control required to fully exploit modern GPU architectures.
According to Meta engineers, modern GPU architectures offer advanced performance-optimization features, including warp specialization, asynchronous memory movement, tensor memory, and cluster-level execution, which depart from Triton's traditional programming model, which simplifies kernel development but abstracts away low-level execution structures.
For example, a modern FlashAttention kernel may dedicate one warp group to issuing TMA transfers while another executes tensor-core computation. A Blackwell GEMM kernel may coordinate multiple warp groups, TMEM allocations, and cluster resources simultaneously. In both cases, performance depends not only on the computation being performed, but also on how multiple execution agents cooperate.
Using these advanced features required "large amounts of architecture-specific orchestration code", as they were not readily available as Triton compilers abstractions. To address this challenge, Meta developed Triton Low-Level Extensions (TLX), designed to give engineers explicit control over GPU execution while preserving Triton's programming model.
TLX introduces a new Multiple Instructions, Multiple Warps (MIMW) execution model that bridges CUDA’s thread-level control and Triton’s block-level abstraction. It extends Triton across five key areas: warp-group orchestration, synchronization, memory orchestration, cluster execution, and optional layout.
Taken together, these capabilities allow TLX to occupy the space between Triton’s productivity and CUDA’s control. Developers retain the advantages of Python, autotuning, and blocked tensor programming while gaining direct access to the execution structures that increasingly determine performance on modern GPUs.
Meta has deployed TLX in production for several months across three major workloads. For GEM model training on thousands of NVIDIA Blackwell GPUs, TLX achieved 20–25% end-to-end Model FLOPs Utilization (MFU) with up to 2x forward-pass speedup. For In-Kernel Broadcast Optimization (IKBO) in recommendation inference, TLX delivered a 4x speedup on an H100 for a linear compression kernel and reduced compute-intensive net latency up to two-thirds in co-designed models. Finally, in distributed grouped GEMM for LLM pretraining, TLX improved performance, reliability, and maintainability across large GPU fleets for extended training periods. [...]

## [15] Muru
Simon Willison's Blog | full text via Simon Willison's Blog | ~391 words

21st November 2026 - Link Blog
Muru. Graham Dumpleton started mod_wsgi 20 years ago, and has been thinking about the ideal way to serve Python web applications in production ever since.
Muru is his new, AI-assisted Rust server that aims to provide the best possible tools for running ASGI and WSGI Python apps both in development and production.
As he did with wrapture, he's been publishing an extraordinarily detailed account of the project as he works on it - as part of his development process.
Here's everything he's published so far, all in the last three weeks:
- 2026-11-04 — Twenty years of mod_wsgi, and what comes next
- 2026-11-05 — A first look at Muru
- 2026-11-07 — Muru: looking inside the workers
- 2026-11-08 — Muru: how it fits together
- 2026-11-09 — Muru: import once, fork many
- 2026-11-10 — Muru: HTTPS in development
- 2026-11-11 — Muru: WSGI and ASGI together
- 2026-11-11 — AI as a lifestyle choice
- 2026-11-12 — Muru: releases, not restarts
- 2026-11-13 — Muru: canaries without a service mesh
- 2026-11-14 — Muru: a better tenant in a container
- 2026-11-15 — Muru: working with Kubernetes, not around it
- 2026-11-16 — Muru: scaling from what the workers report
- 2026-11-17 — Muru: scaling to zero
- 2026-11-18 — Muru: overlays on a schedule
- 2026-11-19 — Muru: noticing and responding
- 2026-11-20 — Muru: a toolbar on every page
- 2026-11-21 — Muru: tracing in the toolbar
That post about AI as a lifestyle choice is particularly worth a read:
The AI may be doing a lot of the work on the surface, but deciding what isn't good enough yet is still down to me, and twenty years of getting things wrong with mod_wsgi turns out to be useful for that. I am prepared to put in the hard work to keep polishing Muru until it is something I would trust, and something you would too.
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026

## [94] Sashiko AI Introducing Linux Performance Specialist Review Stage
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~65 words

The Google-developed Sashiko for agentic AI code review initially focused on the Linux kernel continues helping to uncover new bugs and issues as new patches hit the kernel mailing list as well as those manually running this open-source AI software. In addition to recently introducing an experimental patch series design assessment, they are introducing another new skill for helping with performance/benchmark evaluation of kernel changes...

## [118] Debian 13.8 Released With 150+ Security Updates
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~24 words

Debian 13.8 is out today as the newest ISO refresh for Debian 13 "Trixie" with 150 security updates noted along with many bug fixes...

## [91] Nvidia's Accounting Practices Now Being Investigated by America's SEC
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~92 words

We knew America's Securities and Exchange Commission was investigating Nvidia. But Reuters reported Friday that what's being investigated is Nvidia's accounting practices, according to "two people briefed on the matter." Prices of Nvidia shares extended losses and were down about 13% on Friday, according to LSEG data, after Reuters reported details of the SEC probe. They had been down more than 6% before Reuters published its report... The SEC probe is the latest of Nvidia's legal woes. The Justice Department has also been reviewing Nvidia's $12.9-billion deal to buy open-source platform Hug

## [127] Startup sues Apple in India over tap-to-share contacts feature
TechCrunch | full text via TechCrunch | ~425 words

Apple is being sued in India by a U.S.-based startup that alleges the iPhone maker’s NameDrop feature, which lets users share contact information by bringing devices close together, infringes its patented technology.
GG Technologies, the startup behind StayTouch, an app that lets users exchange contact details by bringing their phones close together, is seeking ₹15 billion (about $161.86 million) in damages and an injunction against Apple, per court documents reviewed by TechCrunch.
Santa Monica-headquartered GG Technologies filed the lawsuit in India in October after mediation proceedings initiated in April failed in September, the startup told TechCrunch. Pre-institution mediation is generally required before filing commercial lawsuits in India. The company also sued Apple in the U.S. in April over related patent infringement claims.
In its 781-page court filing in the Bombay High Court, GG Technologies alleged that Apple’s NameDrop infringes its Indian patent on technology that helps phones exchange contact details with nearby devices without requiring manual pairing. The company launched StayTouch in 2019, the same year it first sought patent protection for the technology in the U.S. It filed its Indian patent application in 2021 and received the patent in July 2024.
Apple introduced NameDrop as part of iOS 17 in June 2023. The feature debuted on iPhones later that year, with support for compatible Apple Watches arriving in October through watchOS 10.1.
“We are seeking an injunction to restrict the usage of the NameDrop feature which is native to iOS,” GG Technologies told TechCrunch. GG Technologies urged the court in its filing to restrict Apple from selling or importing iPhones and Apple Watches preloaded with NameDrop in India. The case has yet to be listed for a hearing.
In the U.S., the International Trade Commission opened an investigation into Apple’s alleged patent infringement in August, following a complaint from GG Technologies. The startup is seeking an order that could block imports of infringing Apple devices into the country, along with restrictions on their sale.
Founded in 2018 by Gaurav Goel, a graduate of the Indian Institute of Technology (IIT) Delhi and a former Goldman Sachs investment banker, GG Technologies developed StayTouch as an alternative to exchanging business cards. The app is available on iOS and Android.
Apple did not respond to a request for comment.
India has become increasingly important to Apple, both as a fast-growing consumer market and a major manufacturing hub outside China. The Cupertino company has expanded its retail presence in the South Asian nation, where iPhones still account for less than 10% of smartphone shipments, giving considerable room for growth.

## [20] Grafana 13.3 Adds Shared Dashboard Variables and Notebooks
InfoQ | full text via InfoQ | ~543 words

Grafana Labs has released Grafana 13.3 with cross-dashboard variables that let teams manage shared dashboard controls in one place. The release also introduces Notebooks for collecting panels and investigation notes in a document that colleagues can share.
The release announcement describes cross-dashboard variables as a public preview across all Grafana editions. Teams can define a variable once and use it in multiple dashboards, avoiding separate configurations for a selector such as an environment or a region. Grafana says managing those copies separately can lead to configuration drift.
Cross-dashboard variables address a longstanding user request. In a 2021 GitHub discussion, Grafana user Darth-Bobo described having to maintain the same variables separately across dashboards, warning that configuration differences could become "unmanageable over time". More recently, an early tester described shared variables as useful for evaluating Git Sync without Terraform templating.
Variables can have global scope, which makes them available throughout a Grafana organisation, or folder scope, which limits them to dashboards in the same folder. An editor can add the available variables from a dashboard sidebar, either individually or all at once. Viewers can still change the selected value on a dashboard, while the variable configuration remains centrally managed.
Teams running Grafana themselves must enable the grafana.dashboardGlobalVariables feature toggle to try the preview. Grafana places the management screen under Dashboards > Variables, separate from the dashboard editor where users add the shared controls.
Notebooks are also in public preview across all editions. A notebook can hold panels from dashboards or Explore alongside written observations, with findings from Grafana Assistant included as well. Teams can use the document to record how they investigated an issue or to prepare a post-incident review with relevant panels already in place.
Users can create a notebook manually or through Grafana Assistant, then save and share it. Grafana is rolling the feature out gradually to Grafana Cloud. Self-managed installations need the dashboard.notebooks feature toggle enabled.
Grafana’s Notebooks joins similar investigation-document workflows from other observability vendors. Datadog Notebooks combines live graphs with rich text and supports simultaneous editing, inline comments and reusable postmortem templates. New Relic Notebooks, generally available since August 2026, combines NRQL queries, visualisations and Markdown, with natural-language query translation and notebook-wide variables.
The release also changes how Grafana Assistant builds dashboards. [...]

## [81] Nearly all software teams admit to shipping AI-generated code as study finds verification 'has not kept pace with that shift'
TechRadar | full text via TechRadar | ~619 words

Nearly all software teams admit to shipping AI-generated code as study finds verification 'has not kept pace with that shift'
What happened to verification before distribution?
- The majority of software development teams have merged code with AI contributions that they didn’t understand
- Some teams (55%) manually review code, while others use one AI model to review another, which has mixed results
- TestMu AI’s State of AI in Quality Engineering 2026 report has also found that only 13% of teams have an incident response provision for publishing AI-generated errors
Generative AI coding tool shave been wholeheartedly embraced by software development teams, to such an extent that 81% have admitted to merging AI generated code that wasn’t fully understood, new research has claimed.
TestMu AI’s State of AI in Quality Engineering 2026 report also found a mixed approach to reviewing AI code and very few teams employing an incident response procedure in the event of AI generated errors occurring on live projects.
These results raise some questions on how development teams are using AI and what steps are being employed to verify output. While some teams use manual review, others rely on a second LLM to review and judge the code. However, this appears to have increased the likelihood of code no-one understands being published.
LLM-as-a-judge
Revealed in the report is the notion of the verification gap, a challenge for teams relying on AI-generated code. Just 41% of teams use automated checks of AI-written code before merging it with existing, often live code. This gap is the beginning of the problem – there is simply too much code to efficiently check.
With 55% of development teams using manual review, or passing to a dedicated QA team (51%), it’s clear that with some teams, important measures are in place.
Employing a second LLM to grade the generated code might seem like a smart move. In terms of fixing issues, it probably is. But the result of this strategy is that teams using LLM-as-a-judge are shipping code they don’t understand at a greater rate – 29%, compared with 15% who don’t use AL grading.
Verify your output
Asad Khan, the Co-founder and CEO of TestMu AI said the key point that verification of AI-generated code is not keeping pace with the volume of output.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
“Software teams now rely on AI to write their code, generate their tests, and increasingly determine whether both are ready to ship,” he noted.
“Verification, however, has not kept pace with that shift. [...]
