---
date: 2026-11-22
edition: 61
schema_version: 1
generated_at: 2026-11-22T01:36:48+00:00
sources_ok: 43
sources_total: 47
fetched: 398
candidates: 160
full_text: 12
---

# The Brief

- An Anthropic mathematician says he has a Lean-checked proof of the Riemann hypothesis itself, and early checkers report the file compiles while the argument remains unexplained.
- Security news centres on speed and trust: the FBI is investigating a breach of a national law-enforcement database, and attackers' AI agents exploited an open-source zero-day in about 11 minutes.
- Production failures hide between layers: a GKE timeout traced to three interacting faults across cloud networking and the Linux kernel, and an Uber cache rebuild that began as a garbage-collection problem.
- Across AI, more capability is not the same as better agents: METR's updated time-horizon plot shows weakness on judgment tasks, and T-Mobile's agents got worse after receiving more documentation.
- Tooling standards keep moving: the C++ committee completed C++26 a second time after objections to contracts, and Meta is giving Triton kernels explicit control over GPU execution.

# Stories

## Anthropic mathematician claims Lean-checked proof of the Riemann hypothesis
- ids: 130, 44, 41, 1
- topic: AI
- signal: must-read
- url: https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/
- event: generalized riemann hypothesis proof lean ai
- original title: AI claimed a solution to the 167-year-old Riemann hypothesis — and a human did, too
- source: TechCrunch | https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/
- source: Simon Willison's Blog | https://simonwillison.net/2026/Nov/20/levent-alpoge/
- source: leanprover-community.github.io | https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ | via Hacker News
- author: Tim Fernholz
- image: https://techcrunch.com/wp-content/uploads/2022/08/GettyImages-1219382595.jpg?resize=1200,750
- read: 3 min
- discuss: https://news.ycombinator.com/item?id=50589618 | Hacker News | 825 points | 668 comments
- full text: yes

> Early checkers report the formal file compiles, but nobody yet understands the argument well enough to confirm it.

Levent Alpöge, a mathematician who works at Anthropic, says he has a Lean-compilable proof of the Riemann hypothesis, the 1859 conjecture about how prime numbers are distributed and one of the Millennium Prize problems. Lean is a proof assistant, so a file that compiles has been checked by software against its stated axioms, and the remaining question is whether the formal statement matches the conjecture mathematicians care about. Alpöge also says the method extends to the generalized Riemann hypothesis. Our 21 November edition covered a Lean-formalized proof of that generalized version by Alessandro Masullo, so this is a second claim on the same thread, and a bigger one, because it targets the original conjecture. TechCrunch's reporting, as its headline notes, also points to a competing human-produced solution, which gives the week two claimants.

The checking so far is social as well as formal. Several participants in a Zulip chat, including MIT mathematician Andrew Sutherland, say they compiled Alpöge's file successfully. Chris Birkbeck, a number theorist at the University of East Anglia, is among those working through the argument, which reportedly rests on an automorphy-lifting approach that draws on Galois representations and base change. Most participants appear confident the formal result will hold, but following the argument well enough to vouch for it is a slower job.

Alpöge has said he feels uneasy releasing the proof without a human-readable explanation, and he has committed to pursuing one. Until that exists, the result is a compiled file that few people can read, which is a different kind of claim from a proof mathematicians can check line by line. The next useful signals are the promised write-up and whether anyone finds a gap between the formal statement and the published conjecture.

**Takeaways**
- Compare the statement in the Lean file with the standard wording of the Riemann hypothesis before treating the compiled file as settled.
- Follow the Zulip thread and Alpöge's promised explanation, since the verdict depends on people understanding the argument, not only on the file compiling.
- Name which version you mean when citing the result, because the claim covers the Riemann hypothesis and, by Alpöge's account, the generalized version too.

## FBI investigates suspected hack of NCIC, the database police use for warrant checks
- ids: 87, 90
- topic: Security
- signal: must-read
- url: https://techcrunch.com/2026/11/21/trump-says-reported-fbi-database-hack-is-not-good/
- event: fbi ncic database hack
- original title: Trump says reported FBI database hack is ‘not good’
- source: TechCrunch | https://techcrunch.com/2026/11/21/trump-says-reported-fbi-database-hack-is-not-good/
- source: The Verge | https://www.theverge.com/tech/1039543/fbi-usda-hacked
- author: Anthony Ha
- image: https://techcrunch.com/wp-content/uploads/2026/09/fbi-edgar-hoover-building-2288940613.jpg?resize=1200,800
- read: 1 min
- full text: yes

> The larger worry is whether tampered records could mislead officers, not just whether data leaked.

The FBI is investigating an apparent intrusion into the National Crime Information Center, the online database that federal and local officers use to share warrant and background-check information. CNN and the Associated Press reported the investigation, and the scope of the breach is not yet clear from public reporting.

A former FBI official told CNN the concern goes beyond whether hackers read sensitive files. The worse case is an attacker changing records that officers act on, which would make accuracy the problem rather than confidentiality. President Donald Trump, asked about the reports in a Fox News interview, said it was "not good," and suggested the episode might reveal things that would otherwise stay hidden.

The report also lands on an agency that has had security trouble before. Back in September, the bureau reportedly informed its employees that a cyberattack had exposed their personal details. The Verge reported that the Department of Agriculture was reportedly hacked around the same time, so the two incidents are being discussed together.

**Takeaways**
- Watch for an official statement of scope: whether the concern is stolen data or altered records changes what partner agencies need to check.
- If your systems pull data from law-enforcement feeds, review access logs for the period in question and confirm which credentials connected.

## GKE API timeouts came from three interacting bugs, one of them in the Linux kernel
- ids: 26
- topic: Infra
- signal: must-read
- url: https://www.infoq.com/news/2026/11/gke-kernel-network-bug/
- event: gke tcp kernel timeouts
- original title: How Google Traced GKE API Timeouts to a Linux Kernel TCP Bug
- source: InfoQ | https://www.infoq.com/news/2026/11/gke-kernel-network-bug/
- author: Renato Losio
- image: https://res.infoq.com/news/2026/11/gke-kernel-network-bug/en/headerimage/generatedHeaderImage-1794082671635.jpg
- read: 3 min
- full text: yes

> Google's engineers needed several teams and weeks of work to trace intermittent Kubernetes API failures that blocked about 800 developers.

In January, a customer running several GKE clusters with Private Service Connect for private control-plane access began seeing intermittent timeouts when pods tried to reach the Kubernetes API server. Packet captures showed the control plane answering new connection requests with acknowledgements that belonged to connections it had already closed. The symptom looked the same at every layer, so each team could find a plausible cause in its own part of the stack.

Google's write-up identifies three causes working together. Private Service Connect was reordering packets. Envoy's half-close behaviour kept some TCP connections from closing properly. And a Linux kernel bug discarded certain reordered FIN packets, which left sockets stuck indefinitely in the FIN_WAIT_2 state. Each cause alone would have been survivable, but together they produced failures that resembled ordinary networking faults.

The fix came in three stages over several weeks. Google started by reverting a recent Private Service Connect modification to get traffic flowing again, then fixed how the proxy handled the protocol and wrote tests to guard against a repeat. The underlying TCP problem was fixed by a Linux kernel patch written by Eric Dumazet, who is a former Google engineer. The write-up does not say which kernel versions carry the patch or when managed node images will include it, so that remains open for anyone running affected clusters.

**Takeaways**
- If pods see sporadic I/O timeouts to the Kubernetes API from clusters using Private Service Connect, check for half-closed Envoy connections and reordered FIN packets.
- Confirm which kernel version your node image runs once the provider ships the upstream TCP patch, because the write-up does not name a version.

## Thinking Machines releases Inkling 2 Mini, a 26B open-weights model for laptops
- ids: 5, 149, 3
- topic: AI
- signal: must-read
- url: https://thinkingmachines.ai/news/inkling-2-mini/
- event: inkling 2 mini looped transformer
- original title: Inkling 2 Mini
- source: thinkingmachines.ai | https://thinkingmachines.ai/news/inkling-2-mini/ | via Hacker News
- source: VentureBeat | https://venturebeat.com/technology/thinking-machines-wows-with-inkling-2-mini-looped-transformer-model-that-runs-locally-on-laptops
- source: github.com | https://github.com/ShinMegamiBoson/lookatmyquant | via Hacker News
- author: Thinking Machines Lab
- image: https://thinkingmachines.ai/news/inkling-2-mini/images/cover-social.png
- read: 14 min
- discuss: https://news.ycombinator.com/item?id=50581260 | Hacker News | 1385 points | 281 comments
- full text: yes

> The model reruns its middle layers three times per token, betting that reasoning done inside the forward pass can replace long written reasoning traces.

Thinking Machines Lab, the startup led by Mira Murati, has released Inkling 2 Mini with open weights. It is a mixture-of-experts model with 26.4 billion total parameters and 3.4 billion active per token. Most of its weights are stored in NVFP4 with the last four layers in MXFP8, which brings the total memory footprint to about 20GB. The company says researchers ran it offline on a MacBook Pro during a flight and built a playable flight simulator in a few minutes.

The architecture is what sets it apart. Inkling 2 Mini is a looped transformer, which runs the middle layers three times for every token. In the company's variable-loop research variant, the no-chain-of-thought time horizon rose from 16 seconds at one pass to 37 seconds at three, and performance on a serial reasoning benchmark kept improving out to ten loops, twice the depth it was trained with. The chain of thought got shorter as loops increased but stayed legible, and the model did not trend higher on agentic sabotage tests as loops were added. That last point is the claim that matters for oversight, since it suggests looping does not simply hide reasoning from readers of the trace.

The benchmark claims are the company's own. It reports that Inkling 2 Mini leads open-weights models under 100 billion total parameters on DeepSWE v1.1 at 48.2% and on Vals Index v2.2 at 46.5%, and that it is behind only Qwen3.8-27B on other agentic coding measures. Independent replication is the next thing to watch, along with whether the looping gains hold on tasks outside the company's test suite.

**Takeaways**
- Run Inkling 2 Mini on your own agentic coding tasks before adopting it, because the headline benchmark figures come from the vendor.
- If you monitor models by reading their chain of thought, test whether shorter looped traces still show what you need to see.
- Inference and customization are available through Tinker, so check the license terms of the open weights before using them commercially.

## METR's updated time-horizon plot shows AI still improving exponentially, but weaker on judgment
- ids: 42
- topic: AI
- signal: must-read
- url: https://www.technologyreview.com/2026/11/20/1149399/the-most-misunderstood-graph-in-ai-just-got-a-major-update/
- event: metr time horizon plot update
- original title: The most misunderstood graph in AI just got a major update
- source: MIT Technology Review | https://www.technologyreview.com/2026/11/20/1149399/the-most-misunderstood-graph-in-ai-just-got-a-major-update/
- author: Grace Huckins
- image: https://wp.technologyreview.com/wp-content/uploads/2026/11/metr2a.jpg?resize=1200,600
- read: 7 min
- full text: yes

> The new report adds longer and open-ended tasks, and the models do noticeably worse on work with no automatic check of success.

METR's time-horizon chart circulated widely and was often misunderstood, partly because it compares models against how long human testers took on each task. The first version suggested that the task length a frontier model can finish doubles roughly every four months. The updated plot adds tasks that take humans far longer than the original suite, along with more open-ended ones. The new report finds that some capabilities keep improving along an exponential curve.

The weak spot is judgment. Models are noticeably less capable on tasks that require judgment than on coding. The reason is structural: reinforcement learning works well where success can be checked automatically, as with code that passes tests or a math answer that is right, and it works much less well where success is slow to measure or vague, such as choosing a research direction. That gap matters because automating research and development depends on exactly those fuzzy tasks.

The report lands in the middle of a debate. Earlier this month a separate, heavily redacted METR report claimed that AI may be speeding up progress at Anthropic by roughly a factor of two. The time-horizon update does not settle that question, but it sets a clearer test: whether gains on verifiable tasks carry over to open-ended work. The new open-ended tasks in the suite are where that answer will come from.

**Takeaways**
- Check which suite a time-horizon number comes from, because the updated plot is not directly comparable to the original.
- Judge agent deployments on open-ended tasks separately from coding benchmarks, and expect weaker results there.

## Amazon says AI agents exploited a MONAI Label zero-day in 11 minutes, with no patched release
- ids: 150
- topic: Security
- signal: recommended
- url: https://venturebeat.com/security/amazon-says-attackers-ai-agents-found-and-exploited-a-zero-day-in-11-minutes-but-no-patched-release-is-available
- event: monai label zero day ai agents
- original title: Amazon says attackers' AI agents found and exploited a zero-day in 11 minutes, but no patched release is available
- source: VentureBeat | https://venturebeat.com/security/amazon-says-attackers-ai-agents-found-and-exploited-a-zero-day-in-11-minutes-but-no-patched-release-is-available
- author: louiswcolumbus@gmail.com (Louis Columbus)
- image: https://images.ctfassets.net/jdtwqhzvc2n1/01dpgRIeG7lTnPz4j6KMmp/07e61c09a3188796e5527ece6a777059/final_hero_image_.jpg?w=1200&q=80
- full text: no

> The fix is merged into the source code, but teams that install packaged releases have no update to apply yet.

According to Amazon, attackers deployed AI agents that found a flaw in MONAI Label, an open-source medical imaging tool, and used it to drop files somewhere they should not go, all within roughly eleven minutes. A correction has landed in the project's code repository, yet nobody has published a release that ships it. The details here come from a short standfirst because the full report could not be retrieved, so the technical specifics of the flaw are not known from our reading.

The timeline is the real signal. Discovery and exploitation happened inside a window that is shorter than most organizations' patch cycles, and the vulnerable application is one that hospitals and research groups may run on internal networks. A merged fix in source does not protect a deployment that pins an older release.

**Takeaways**
- If you run MONAI Label, limit the storage directory it can write to and restrict its network exposure until a release ships.
- Track the merged fix in the project's source so you can build and deploy it before the packaged release arrives.

## Nvidia's accounting drew an SEC probe, and its shares fell about 13% on the report
- ids: 91
- topic: Startups
- signal: recommended
- url: https://yro.slashdot.org/story/26/11/21/0445220/nvidias-accounting-practices-now-being-investigated-by-americas-sec
- event: nvidia sec investigation accounting
- original title: Nvidia's Accounting Practices Now Being Investigated by America's SEC
- source: Slashdot | https://yro.slashdot.org/story/26/11/21/0445220/nvidias-accounting-practices-now-being-investigated-by-americas-sec
- author: EditorDavid
- full text: no

> Reuters' sourcing points to accounting, a narrower focus than the general investigation the company had already faced.

Reuters said on Friday that the SEC's inquiry into Nvidia is aimed at how the company accounts for its activities, with the information coming from two sources familiar with the case. The existence of the inquiry was already known. The new detail is its focus, and Nvidia's stock slid roughly 13% that day once the specifics circulated.

The probe is part of a wider set of legal problems for the company. A separate federal review is also examining a $12.9 billion acquisition the chipmaker made of an open-source software platform, per the same account. The coverage we could read does not describe any charges or findings, and the sourcing is to people briefed on the matter rather than to a public filing. The standfirst is the only text available for this story, so the details beyond it are unverified.

**Takeaways**
- Watch for a formal SEC filing or a company disclosure, since the current account rests on anonymous sources.

## Uber cuts translation cache memory by more than 90% and keeps p99 misses under 1 ms
- ids: 45
- topic: Infra
- signal: recommended
- url: https://www.infoq.com/news/2026/11/uber-go-translation-cache/
- event: uber translation cache memory
- original title: Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS
- source: InfoQ | https://www.infoq.com/news/2026/11/uber-go-translation-cache/
- author: Leela Kumili
- image: https://res.infoq.com/news/2026/11/uber-go-translation-cache/en/card_header_image/generatedCard-1793504736709.jpg
- read: 3 min
- full text: yes

> The team started with garbage collection costs, and then found the bigger memory problem was the cache rebuild itself.

Uber's Go translation cache was consuming too much CPU through garbage collection, which in some services exceeded 20% of CPU, with translations making up about 70% of allocated objects. The first fix replaced Go's sync.Map with a plain map guarded by an RWMutex, which suits a workload that is mostly reads. That change cut allocations and improved CPU use by more than 30% in the affected service.

Memory was still the bigger problem. Translation datasets could hold two to three million keys, while any one service touched only a small fraction of them. Cache refreshes built a replacement copy in the background before swapping it in, so both copies sat in memory at once, and some services ran out of memory during refreshes. Uber rejected external caching and per-service subsets because each added operational cost. The design it chose keeps every key in memory and stores values in disk-backed files, split across 256 shards, with six-byte hashed keys and a time-based LRU policy. During refreshes, the cache preloads translations accessed in the previous 15 minutes to avoid a cold start. In one example, a dataset that used about 800 MB in memory needed about 40 MB for metadata.

Uber says the existing Get and Put API is unchanged, and it reports a cache hit rate above 99.9% with p99 miss latency below one millisecond. Those figures are Uber's own, and the tradeoff is that misses now read from disk.

**Takeaways**
- Profile garbage collection share before rewriting storage, since replacing a pointer-heavy map alone can cut a large share of the cost.
- Check whether background cache rebuilds double peak memory in your service, because building a replacement copy beside the live one is a common source of out-of-memory errors during refreshes.

## C++26 is completed again after a second ballot, with contracts the sticking point
- ids: 21
- topic: Languages
- signal: recommended
- url: https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/
- event: cpp26 contracts second ballot
- original title: C++26 is done (again)! — Trip report: November 2026 ISO C++ standards meeting (Búzios, Brazil)
- source: herbsutter.com | https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/ | via Lobsters
- author: Herb Sutter
- image: https://secure.gravatar.com/blavatar/fe7f5b0b83dba894afe26c42bcab33fe2d1246d9730ef182c72c0bff0dc26acb?s=200&ts=1795311084
- read: 9 min
- full text: yes

> The first approval ballot did not pass unanimously, so the committee reopened work and sent the standard back out for comment.

The ISO C++ committee finished technical work on C++26 for a second time at its November meeting in Búzios, Brazil. The first completion, in March, did not hold. The approval ballot for the draft did not pass unanimously, and national bodies sent it back with further comments, most of them about contracts, the pre, post and contract_assert facility. The committee responded by adopting an extension to the contracts feature and by writing a rationale and timeline for national bodies that explains how contracts were developed and why the decisions were made.

The next step is an updated document for a second approval ballot and final editorial work, with publication expected after that. The meeting ran six days with about 220 attendees from 27 nations, and fewer of the committee's 22 subgroups met than usual because the week was devoted to comments. The committee also adopted several features for draft C++29, including labeled break and continue statements and std::ranges::any_view with views::slice.

**Takeaways**
- Hold off on depending on the contracts wording in production code until the second ballot passes and compilers implement the final text.
- Track the second ballot's outcome, because it decides whether the contracts facility you test today changes before publication.

## Meta's TLX gives Triton kernels explicit control over GPU warps and memory
- ids: 43
- topic: Languages
- signal: recommended
- url: https://www.infoq.com/news/2026/11/meta-triton-tlx-gpu-compiler/
- event: meta tlx triton gpu extensions
- original title: Meta TLX, a Native GPU Compiler Extension Supporting Advanced Hardware Capabilities
- source: InfoQ | https://www.infoq.com/news/2026/11/meta-triton-tlx-gpu-compiler/
- author: Sergio De Simone
- image: https://res.infoq.com/news/2026/11/meta-triton-tlx-gpu-compiler/en/headerimage/meta-java-kotlin-port-1795195032767.jpeg
- read: 2 min
- full text: yes

> Meta says it has run TLX in production for months, reporting 20 to 25% model FLOPs utilization on a large Blackwell training job.

Triton's high-level model simplifies kernel writing, but it hides the execution details that modern GPUs depend on, such as warp specialization, asynchronous memory movement, tensor memory and cluster-level execution. Meta built Triton Low-Level Extensions, or TLX, to expose those controls. It keeps Triton's Python interface, autotuning and blocked tensor programming, and adds a multiple-instruction, multiple-warp execution model that extends Triton across warp-group orchestration, synchronization, memory, cluster execution and optional layout.

Meta's production numbers are its own. For GEM model training on thousands of Blackwell GPUs, TLX reached 20 to 25% end-to-end model FLOPs utilization, with up to a 2x speedup in the forward pass. A linear compression kernel for recommendation inference ran 4x faster on an H100, and in co-designed models it cut compute-intensive net latency by up to two-thirds. The write-up does not say how portable TLX code is across GPU generations, which is the first question for teams that lack kernel specialists.

**Takeaways**
- If you write Triton kernels for Blackwell, compare TLX-style explicit warp orchestration against stock Triton on your own kernels before adopting it.
- Read the 4x figure as a single kernel on H100, not an end-to-end model result.

## Grafana 13.3 lets dashboards share variables and adds Notebooks for investigations
- ids: 20
- topic: Dev Tools
- signal: recommended
- url: https://www.infoq.com/news/2026/11/grafana-13-3-shared-variables/
- event: grafana 13 3 shared variables notebooks
- original title: Grafana 13.3 Adds Shared Dashboard Variables and Notebooks
- source: InfoQ | https://www.infoq.com/news/2026/11/grafana-13-3-shared-variables/
- author: Mark Silvester
- image: https://res.infoq.com/news/2026/11/grafana-13-3-shared-variables/en/headerimage/header-1795209346746.jpeg
- read: 3 min
- full text: yes

> Both features are in public preview, and self-managed installations must enable feature toggles before they can try them.

Cross-dashboard variables let a team define a selector such as environment or region once and use it across several dashboards. Variables can have global scope across an organisation or folder scope limited to one folder. Editors add them from the dashboard sidebar, viewers can still change the selected value, and the variable configuration itself is managed centrally under Dashboards and then Variables. Grafana's aim is to stop the copy-and-drift problem that comes from maintaining the same variable in many places.

Notebooks combine panels from dashboards or Explore with written observations and findings from Grafana Assistant, then can be saved and shared. Teams can use them to record how an incident was investigated or to prepare a post-incident review with the relevant panels already attached. Grafana Cloud is receiving the feature gradually. Self-managed users need the grafana.dashboardGlobalVariables toggle for variables and the dashboard.notebooks toggle for notebooks. The coverage places this alongside Datadog Notebooks and New Relic Notebooks, the latter generally available since August.

**Takeaways**
- Self-managed operators should try grafana.dashboardGlobalVariables on a test instance first, because both features are still previews.
- Teams that copy the same environment or region variable into many dashboards can consolidate them now and avoid the drift that the feature is meant to prevent.

## Nearly all software teams admit merging AI code they do not fully understand
- ids: 81
- topic: Engineering
- signal: recommended
- url: https://www.techradar.com/pro/nearly-all-software-teams-admit-to-shipping-ai-generated-code-as-study-finds-verification-has-not-kept-pace-with-that-shift
- event: ai generated code verification gap
- original title: Nearly all software teams admit to shipping AI-generated code as study finds verification 'has not kept pace with that shift'
- source: TechRadar | https://www.techradar.com/pro/nearly-all-software-teams-admit-to-shipping-ai-generated-code-as-study-finds-verification-has-not-kept-pace-with-that-shift
- author: Christian Cawley
- image: https://cdn.mos.cms.futurecdn.net/QXcBRNeHkzXC6am5m3TXYf-2560-80.jpg
- read: 3 min
- full text: yes

> The survey's sharpest finding is that teams using a second LLM as a reviewer ship code nobody understands at a higher rate.

A TestMu AI report, the State of AI in Quality Engineering 2026, says 81% of software teams have merged AI-generated code they did not fully understand. Verification is lagging behind the volume: 55% of teams rely on manual review, 51% pass changes to a dedicated QA team, and only 41% run automated checks on AI-written code before merging. The report also found that just 13% of teams have an incident-response procedure for errors that reach production from AI-generated code.

The most counterintuitive result concerns reviewing with another model. Teams that use an LLM as a judge report shipping code they do not understand at 29%, compared with 15% for teams that do not. The report's conclusion, from its chief executive, is that verification has not kept pace with the shift to AI-written code. The survey's method was not reviewed here, and it comes from a single vendor's report, so the percentages should be read as directional.

**Takeaways**
- Track how many merged AI-authored changes have a named reviewer who can explain them, since that is the gap the survey points to.
- Do not treat an LLM reviewer as a replacement for automated test gates, because the survey links LLM-only review with more unexplained code shipping.
- Write an incident-response step for AI-caused defects, since only 13% of surveyed teams have one.

## T-Mobile's customer-service AI got worse after it was given more documentation
- ids: 151
- topic: AI
- signal: recommended
- url: https://venturebeat.com/orchestration/giving-its-ai-more-to-read-made-t-mobiles-answers-worse
- event: tmobile customer service ai agents context
- original title: Giving its AI more to read made T-Mobile's answers worse
- source: VentureBeat | https://venturebeat.com/orchestration/giving-its-ai-more-to-read-made-t-mobiles-answers-worse
- image: https://images.ctfassets.net/jdtwqhzvc2n1/6cr9dH7qqD0iG0OzchoMxD/1ebe9d5513a0adff68db0ab4d7442936/VentureBeat102826-2135.jpg?w=1200&q=80
- full text: no

> More context did not help T-Mobile's agents, because conflicting instructions sent them down the wrong path for some requests.

T-Mobile gave its AI customer-service agents access to a large body of support documentation so they could answer better. That backfired. According to CIO Jeff Simon, speaking at VentureBeat's Agentic Infrastructure Stack Summit in October, the conflicting instructions in the documentation could steer agents down the wrong path for a customer's request. A knowledge graph built as the next attempt was too slow and difficult for the agents to navigate.

The story is short, and the account comes from a standfirst because the full article could not be retrieved, so the details beyond these are unknown. The lesson the piece points to is about quality rather than coverage: a larger corpus of instructions can lower accuracy if its instructions contradict one another.

**Takeaways**
- Audit documentation for contradictory instructions before adding it to an agent's context, because the contradictions are what cause the wrong path.
- Measure answer accuracy after each addition to the corpus, not only how much of the support material the agent can reach.

## Nvidia used Factory's coding harness to make 20,000 training rows for Nemotron 3 Ultra
- ids: 103
- topic: AI
- signal: recommended
- url: https://thenewstack.io/nvidia-droid-harness-nemotron/
- event: nvidia nemotron factory droid data
- original title: Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding score jumped.
- source: The New Stack | https://thenewstack.io/nvidia-droid-harness-nemotron/
- author: Amanda Caswell
- full text: no

> The notable part is the pipeline: a coding-agent product is generating training data for a coding model.

Nvidia relied on a coding agent built by Factory to produce about 20,000 examples used to tune Nemotron 3 Ultra, a model with 550 billion parameters. The headline reports that the model's coding score jumped after the data was used to fix its mistakes. The full article could not be retrieved, so the size of the gain and the exact method are unverified from our reading.

The pipeline is what stands out. A commercial coding-agent harness is being used as a data generator for a model that is itself aimed at coding, so the quality of the agent's trajectories shapes the model that results. The evidence available here is limited to the standfirst.

## Startup sues Apple in India over NameDrop, seeking $162 million and an injunction
- ids: 127
- topic: Startups
- signal: recommended
- url: https://techcrunch.com/2026/11/20/startup-sues-apple-in-india-over-tap-to-share-contacts-feature/
- event: gg technologies apple namedrop india patent
- original title: Startup sues Apple in India over tap-to-share contacts feature
- source: TechCrunch | https://techcrunch.com/2026/11/20/startup-sues-apple-in-india-over-tap-to-share-contacts-feature/
- author: Jagmeet Singh
- image: https://techcrunch.com/wp-content/uploads/2026/11/apple-namedrop.jpg?resize=1200,800
- read: 2 min
- full text: yes

> GG Technologies wants a court order that could restrict NameDrop and block iPhone and Apple Watch imports into India, not just money.

GG Technologies, the Santa Monica company behind the StayTouch contact-exchange app, filed suit in the Bombay High Court in October. It alleges that Apple's NameDrop infringes its Indian patent on exchanging contact details by bringing two devices together without manual pairing. The company seeks ₹15 billion, about $162 million, and an injunction that would restrict NameDrop and stop the sale or import of iPhones and Apple Watches preloaded with it. The filing runs to 781 pages.

The background matters. StayTouch launched in 2019 and the company first sought U.S. patent protection that year. The Indian patent application followed in 2021 and was granted in July 2024. NameDrop arrived with iOS 17 in June 2023. The U.S. International Trade Commission opened an investigation into Apple in August after a complaint from GG Technologies, and the company also sued Apple in the U.S. in April. Apple did not respond to a request for comment. India is a growing market for Apple, though iPhones still account for less than 10% of smartphone shipments there. The case has not yet been listed for a hearing, and the filing's claims have not been tested in court.

## US charges suspected Russian agent with stalking Palantir employees in Palo Alto
- ids: 75
- topic: Security
- signal: recommended
- url: https://news.slashdot.org/story/26/11/21/212248/us-doj-charges-suspected-russian-agent-for-stalking-palantir-employees-in-california
- event: palantir employees stalking russian agent
- original title: US DOJ Charges Suspected Russian Agent for Stalking Palantir Employees in California
- source: Slashdot | https://news.slashdot.org/story/26/11/21/212248/us-doj-charges-suspected-russian-agent-for-stalking-palantir-employees-in-california
- author: EditorDavid
- full text: no

> Prosecutors frame the case as foreign intelligence aimed at Silicon Valley tech workers, with Palantir's support for Ukraine cited as the motive.

The Justice Department is prosecuting a suspected foreign agent accused of stalking and harassing employees of Palantir in Palo Alto, California. ABC News sources said the suspect was arrested in October. U.S. Attorney Craig H. Missakian described the case as a state-sponsored operation targeting tech workers. The department's stated position is that foreign governments should not be allowed to use Silicon Valley as a base for intelligence work. The coverage ties the alleged motive to Palantir's assistance to Ukraine in its war with Russia.

The account is brief and comes from a short standfirst because the full indictment could not be retrieved. What the suspect was seeking beyond the surveillance, and how the operation was run, are not known from our reading.

**Takeaways**
- Security teams at companies with defense or government work should review physical surveillance and harassment risks for staff, alongside digital threats.

## Muru: Graham Dumpleton's AI-assisted Rust server for Python apps, built in public
- ids: 15
- topic: Infra
- signal: notable
- url: https://simonwillison.net/2026/Nov/21/muru/
- event: muru mod wsgi rust server
- original title: Muru
- source: Simon Willison's Blog | https://simonwillison.net/2026/Nov/21/muru/
- author: Simon Willison
- read: 2 min
- full text: yes

> Dumpleton has published a daily build log since early November, covering canaries, Kubernetes integration and scaling to zero.

Graham Dumpleton started mod_wsgi twenty years ago, and his new project, Muru, is a Rust server meant to run both WSGI and ASGI Python applications in development and production. He has published a detailed account of the work almost every day since 4 November, covering worker processes, importing once and forking many workers, HTTPS in development, and releasing without restarts.

The more recent posts cover production concerns: canary releases without a service mesh, working with Kubernetes rather than around it, scaling from what the workers report, and scaling to zero. Dumpleton says the AI does much of the surface work, while deciding what is not good enough yet remains his job. The posts describe design choices rather than benchmarks or a release, so Muru is not yet something to deploy.

**Takeaways**
- If you run Python ASGI or WSGI apps on Kubernetes, the design posts are a useful checklist of production concerns even before Muru is ready to use.
