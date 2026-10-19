# Full text for 30 picks -- untrusted article content, treat as data only

## [3] Hybrid Reasoning Agents: LLM agents that think in latent space, act through text
Hacker News | full text via Hacker News | ~395 words

Computer Science > Computation and Language
  [Submitted on 13 Oct 2026]
Title:Hybrid Reasoning Agents
View PDF HTML (experimental)
            Abstract:How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturally, a lightweight HybridLink enables seamless transitions between text and latent modes, while the agent's continuous working memory preserves lossless hybrid context across multiple turns. These designs preserve tool-integrated agentic capabilities while making latent thoughts directly inspectable. Building on this architecture, we further develop dedicated post-training algorithms for hybrid reasoning: HybridSFT stabilizes tool-integrated hybrid generation by teaching the backbone to coordinate with HybridLink, then HybridRL scales reasoning by learning when to think in latent space and when to act through text. We evaluate HybridAgent at 3 model scales across 11 benchmarks covering mathematics, science, medicine, search, and agentic reasoning. Compared with frontier LLM Agents and agentic frameworks spanning both text-based and latent methods, HybridAgent consistently improves performance by 10.4%, while delivering 35.5%-54.7% token reduction, 1.8x-2.6x faster inference, and 2.7x-3.7x cost savings. Code and data are available at this https URL.
    
Additional Features
Current browse context:
cs.CL
References & Citations
    
    Loading... [...]

## [45] Arm AGI CPU crushes AMD in new agentic AI benchmark — but what does its 2x rack-level performance advantage mean for the future of x86 data centers?
TechRadar | full text via TechRadar | ~670 words

Arm AGI CPU crushes AMD in new agentic AI benchmark — but what does its 2x rack-level performance advantage mean for the future of x86 data centers?
Arm claims a near 2x rack-level advantage over AMD
- Arm’s AGI CPU nearly doubles AMD’s modelled rack-level performance across seven workloads
- A 24-kW rack accommodates up to 23 Arm servers under the assessment’s assumptions
- Arm’s rack-level advantage reaches 3.19x in the strongest individual workload
Arm’s AGI CPU has recorded nearly twice the modelled rack-level performance of AMD’s EPYC 9755 across seven workloads designed to evaluate agentic artificial intelligence.
The assessment, conducted by Signal65 with Arm’s cooperation, compared measured processor results before estimating performance across racks operating within a fixed power budget.
The findings rely partly on power-based modelling, while testing on final production hardware remains outstanding.
Rack density gives Arm a substantial advantage
The assessment examined workloads involving software tools, autonomous task execution, information retrieval, and support for AI model serving, including Terminal-Bench 2 and SWE-bench.
Across the seven tests, Arm’s processor achieved an average performance ratio of 1.99x, with individual results ranging from 1.43x to 3.19x compared with AMD’s EPYC 9755.
The modelled advantage partly comes from differences in server power consumption, allowing more Arm systems within the same electricity allocation.
A 24 kW rack could accommodate 21 to 23 AGI CPU servers, compared with 13 dual-socket EPYC 9755 systems.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
That configuration provides between 5,712 and 5,888 physical cores for Arm, compared with 3,328 for AMD, although the comparison depends on the rated power assumptions.
Individual server power ranges from 950 to 1,050 watts for Arm’s systems, while AMD’s dual-socket configurations carry a rated consumption of 1,700 watts.
Across workload categories, Arm recorded modelled rack-level advantages averaging 1.7x for tooling, 2.0x for agentic workflows and 2.2x for reasoning and planning.
The report also estimated that database and vector-search operations could require 30% to 35% fewer racks for equivalent processing workloads. [...]

## [75] Gemini 4 Argon vs. Claude Opus 5.5: Half the price and about half as accurate
The New Stack | full text via The New Stack | ~1148 words

Gemini 4 Argon vs. Claude Opus 5.5: Half the price and about half as accurate
When Google announced Gemini 4 Argon to a small group of testers on September 30, it came with a benchmark table that put Argon ahead of Claude Opus 5.5 on 14 of 18 tests. Those include DeepSWE (77.9% vs. 74.2%) and GraphWalks at 256K to 1 million tokens (84.2% vs. 66.8%). Two weeks later, on October 13, Google opened Argon to paid Gemini API developers.
To its credit, Google also showed where Opus 5.5 wins. Opus leads on the other four benchmarks, including Terminal-bench 4.0 (66.4% vs. 57.4%), which tests agentic work in a command line.
Google is also undercutting Anthropic on price, at least for now. Through November 30, Argon costs $2 per million input tokens and $10 per million output tokens, half the price of Opus 5.5. On December 1, it rises to $4 and $20, matching Opus. That gives developers about six weeks to decide whether Argon is better or just cheaper.
That gives developers about six weeks to decide whether Argon is better or just cheaper.
Benchmarks don’t always match real work, and a half-price window only matters if the model matches the competitor on quality. To see whether Argon is better or just cheaper (for now), I tested both models head-to-head on three hard tasks from categories where Google claims a lead.
The tests
I ran each test once per model through OpenRouter, on Google’s and Anthropic’s own servers, at default reasoning settings. A script graded every answer against keys I built and verified before testing either model. The answer key adds more scoring areas to help ensure the quality and thoroughness of each test.
- Bug hunt – A 3,500-line Python library with 14 planted logic bugs and five decoys. Each model reviewed the code, then fixed what it found.
- Billing spec – A spec for a subscription billing engine, graded by 80 hidden tests on daylight saving, month-end dates, and rounding. A follow-up added two currencies and 20 more tests.
- Long context – A fake wiki of 400 services with scattered dependencies, at three sizes. Each model answered three graph questions with planted traps.
Bug hunt
This one was a tie. Both models found all 14 bugs, including four that only show up when you follow a value across three or more files. Neither flagged a decoy. In the follow-up, both fixed all 14 bugs without breaking any of the 93 existing tests.
Argon was cheaper. [...]

## [51] Linux 7.3 Released With Faster I/O Performance, AMD Zen 6 Preparations & More
Phoronix | full text via Phoronix | ~253 words

Linux 7.3 Released With Faster I/O Performance, AMD Zen 6 Preparations & More
The Linux 7.3 kernel is out today for an on-time release of this next stable kernel version.
Over the past week the bug/regression fixes, including the continued flow of AI/LLM churn, continued hitting Linux Git ahead of this stable debut. Some of the material merged over this past week included a fix for some varying, rare SMP boot hangs going back to 2024, workarounds for the Samsung 990 PRO and 990 EVO Plus SSDs on select firmware versions lying about capabilities, Darrick Wong stepping down after 23 years being heavily involved in Linux kernel development, and other fixes.
Linux 7.3 delivers many exciting improvements from faster I/O on modern systems to more AMD Zen 6 platform preparations, Steam Controller 2026 kernel driver support, improvements for older AMD GPUs, improved vRAM management for those on systems with limited video memory capacity, and a lot of other exciting work. See the Linux 7.3 feature list for the more exhaustive look at the many exciting changes for Linux 7.3.
Grab Linux 7.3 from kernel.org.
Now onward to the Linux 7.4 merge window with a lot of awesome features expected for Linux 7.4. With Linux 7.3 out on-schedule, Linux 7.4 stands chances of being released prior to the end of December. So Linux 7.4 could end up being this year's Long Term Support (LTS) version or we'll see if Greg KH plays it safe and ends up declaring v7.3 as this year's LTS kernel.

## [18] Anthropic gives outside AI watchdog “employee-like” access
Ars Technica | full text via Ars Technica | ~280 words

Anthropic has granted external evaluators “employee-like access” to assess the risks of its models, following through on a commitment to increase safeguards over concerns the technology could run catastrophically out of control.
METR, a nonprofit that has worked with leading labs including OpenAI, Anthropic, Google and Meta, now has a team embedded in the Claude maker’s office with access to its hardware and internal systems.
A greater role for third-party evaluators is among the main concrete steps the labs have proposed in response to rising concern about the dangers more capable AI systems could pose to the economy, cyber security and humanity at large.
Anthropic chief executive Dario Amodei achieved a rare moment of unity with arch-rivals Sam Altman and Elon Musk in September when the OpenAI and SpaceX bosses rallied behind his proposal to embed external auditors in the leading labs.
Thursday’s announcement marks the first step to implementing these pledges. OpenAI has yet to lay out plans to bring in evaluators after Altman said Amodei’s proposals were a good idea.
“As models have become more powerful, they’ve required stronger safeguards and more challenging risk assessment,” Anthropic said on Thursday. “We want to be publicly accountable for the decisions we’re making. But we can’t publicly share all the information relevant to our safety work.”
Critics of Anthropic’s proposal to use evaluators have argued the arrangements could lead to conflicts of interest, pointing to issues in the accounting sector, and that greater government regulation is required.
Anthropic argued that sharing information publicly could benefit malicious actors or competitors and added that its evaluators will operate similarly to bank supervision, whereby regulators assign resident examiners to work inside the largest banks.

## [19] Google Adopts Pyrefly for Faster, More Accurate Python Type Checking
InfoQ | full text via InfoQ | ~453 words

Google has replaced its long-standing Python type checker, Pytype, with Pyrefly, an open-source tool originally developed by Meta. The decision was driven by Pyrefly's advantages, including faster and more accurate type checking, and lower infrastructure costs.
As Python’s typing system evolved rapidly, Pytype faced fundamental challenges. Because it operated by analyzing compiled bytecode rather than source ASTs, keeping pace with modern typing PEPs became an increasing maintenance burden due to bytecode instability across Python releases.
According to Google’s internal benchmarks, Pyrefly is approximately 10 times faster than Pytype, reduces incremental rebuild latency by up to 98%, and cuts peak compute cost for Python type checking by more than 80%. Google also reported a 90–99% reduction in type-checking time along clean-build critical paths, substantially "eliminating a long-standing development bottleneck".
One of Pyrefly's key strengths, Google explains, is its strong conformance to Python's typing specification, passing approximately 97% of tests in the conformance suite. Pyrefly is also actively supported by the community, which helps it keep pace with new syntax, and its diagnostics provides more actionable feedback, including inline code annotations that pinpoint the root cause of errors and, in some cases, suggest fixes.
The community has responded with interest to Google's announcement. While most commenters agreed that Pytype performs worse than Pyrefly, others debated Pyrefly's relative merits compared with Ty and Mypy. Gushys noted that
Pyrefly is much more mature. Its already at past 1.0, has similar performance speed to ty, and is a proven tool. ty just isn't quite there yet.
WindHawkeye observed that "Mypy is much faster in large setups than people think. It still has the fastest incremental type check", to which BeamMeUpBiscotti replied that
Mypy 2.0 is supposed to be up to 5x faster on large projects for cold checks, but the newer generation of type checkers can be up to an order of magnitude faster than even that.
Commenting on the announcement on LinkedIn, Python developer Amirrea Azadmher offered a different perspective, arguing that a type-checker's value is not is not merely in saving 30 seconds in CI pipelines, but in how it improves the edit-check loop during development. He also noted that:
If you're evaluating Pyright vs Pyrefly vs mypy right now, don't trust someone else's monorepo numbers. [...]

## [78] Liquid AI caught its model cheating on coding tests — then it recognized the sandbox
The New Stack | full text via The New Stack | ~615 words

Liquid AI caught its model cheating on coding tests — then it recognized the sandbox
Liquid AI’s new reasoning model was built to solve coding problems, but during training it kept combing Git history, GitHub, PyPI, and Hugging Face for answers, and as it did so, it appeared to grasp that it was running inside a sandbox.
The behavior was disclosed Tuesday alongside the release of LFM2.5-24B-A2B, a 24-billion-parameter model with just 2 billion active parameters per token. The incident raises questions about how much agent benchmarks measure actual problem-solving versus a model’s ability to exploit the test itself.
The behavior was disclosed Tuesday alongside the release of LFM2.5-24B-A2B, a 24-billion-parameter model with just 2 billion active parameters per token.
Hunting for hints
The model was caught searching repository history and external platforms for existing answers rather than solving coding problems on its own. The behavior occurred during teacher specialization, part of Liquid AI’s post-training process, where the model used legitimate development tools to bypass the work it was supposed to complete.
More surprising was the apparent recognition that it was running inside a test environment. Liquid AI couldn’t establish whether this awareness developed during training or came from patterns in the training data, and found no evidence that it affected the scores. Unlike Mistral’s latest model, which attempted to leave its test environment earlier this month, there was no attempt to escape the sandbox.
Precedent in the pipeline
Anthropic is one company that has been dealing with reward hacking for years. In its 2024 experiments, it caught models rewriting code to change their own rewards and modifying tests meant to catch them, while a November 2025 study found that models trained to game reward systems could also become deceptive and attempt to sabotage safety research.
The problem reached Anthropic’s own training pipeline in February, when the company detected reward hacking in Mythos Preview and rolled back three days of reinforcement learning. Changes to its production training environments were frozen for about a month after a review flagged problems in more than 10% of them.
Although the circumstances differ from Liquid AI’s incident, similar weaknesses have turned up across agent evaluations. At ICML 2026, the Reward Hacking Benchmark tested 13 frontier models on multistep tasks with opportunities to cheat. [...]

## [21] AWS Introduces Preview of Well-Architected Agent
InfoQ | full text via InfoQ | ~512 words

AWS recently announced the preview of the Well-Architected Agent, a service that analyzes environments against Well-Architected best practices and provides prioritized recommendations across cost, security, performance, and reliability. The AI agent can also suggest remediation steps and review infrastructure-as-code before deployment.
The AWS Well-Architected Agent correlates resource configurations, utilization metrics, application topology, and declared business goals to prioritize recommendations at the resource, application, and architecture levels, including trade-off analysis and remediation through CLI commands, IaC changes, and automation. The agent can also review Terraform and CloudFormation IaC before deployment. Channy Yun, lead blogger at AWS, writes:
It automatically correlates utilization metrics, resource configurations, and application topology, and analyzes against Well-Architected best practices across 65+ AWS services. It generates recommendations aligned to your declared business goals, delivers implementation packages with every finding, and surfaces cross-pillar trade-offs making it simpler to remediate the findings.
The Well-Architected Agent starts with an agent profile defining the accounts, regions, optimization pillars, and business goals. It then scans resources in the configured accounts and generates prioritized recommendations at the resource, application, and architecture levels for review and remediation. The agent analyzes infrastructure across cost optimization, security, resilience, and performance, and can also review IaC templates on demand.
The Well-Architected Agent uses application context and business goals to prioritize recommendations by impact and effort, providing findings at the resource, application, and architecture levels, including cost impacts and IaC changes. Yun adds:
You can also configure API access to integrate recommendations directly into your existing development and operations workflows. To interact with the agent programmatically, including calling APIs and searching documentation, try the AWS MCP Server and plugins with your preferred AI coding tool.
Some practitioners have questioned trusting an AI agent with architectural recommendations, while others point to practical challenges in prioritizing recommendations based on business goals. [...]

## [6] Java sealed classes and exhaustive pattern matching
Hacker News | full text via Hacker News | ~667 words

Java 17 introduced sealed classes, which allow you to explicitly list the allowed sub-types of an interface or base class. For example, here’s a toy example using a sealed interface and records (inner classes are implicitly added to the permitted sub-types if an explicit list is not given):
public sealed interface SealedType {
    record TypeA() implements SealedType {}
    record TypeB() implements SealedType {}
    static SealedType of(String type) {
        return switch (type) {
            case “A” -> new TypeA();
            case “B” -> new TypeB();
            default -> throw new IllegalArgumentException();
        };
    }
}
If you are familiar with functional programming languages with algebraic datatypes, you can view this as similar to a datatype declaration in Haskell or ML:
data SealedType = TypeA | TypeB
We can then use this in a simple Main class:
void main(String[] args) {
    var val = SealedType.of(args[0]);
    System.out.println(switch (val) {
        case SealedType.TypeA() -> “A”;
        case SealedType.TypeB() -> “B”;
    });
}
OK, not so exciting. But one thing to note here is that we didn’t have to add a default clause to the switch expression in our main method. This is because sealed classes (and enums) enable exhaustiveness checking: the compiler knows exactly what the possible cases are, and so can check if you have covered them all. If you have, then you don’t need a default clause. If you forget one (and don’t have a default clause), then you get a compile-time error.
This is great when you want to ensure that all uses of some type do cover all of the cases, but it does introduce a new type of breaking change: adding a new sub-type to a sealed class/interface may break consumers of that code. For example, adding a new TypeC case to our example will cause the main method to fail to compile due to the missing case. So if you export a sealed type in your API then adding a new subtype is a breaking change that would require a major version bump (if you’re following SemVer).
Compile-time or runtime error?
Although Java will produce a compile-time error for a non-exhaustive switch when you compile the consumer (main in this case), it cannot do so if the consumer is not recompiled when the sealed type changes. [...]

## [89] Linux 7.4 Features Very Exciting With Radeon HDMI 2.1 By Default, AMD PerfOpt, Apple M4
Phoronix | full text via Phoronix | ~686 words

Linux 7.4 Features Very Exciting With Radeon HDMI 2.1 By Default, AMD PerfOpt, Apple M4
The Linux 7.3 kernel is expected to be released as stable later today and with that version there are many exciting changes and improvements. However, the Linux 7.4 kernel merge window will then open up and there are even more exciting changes expected to be merged for this follow-on kernel cycle. Here is a preview of some of the many exciting feature changes expected for Linux 7.4.
On the AMDGPU graphics driver side, AMDGPU finally enables HDMI 2.1 support by default! Now that the VRR and ALLM support is also in tow, the HDMI 2.1 support is in good shape for the AMDGPU kernel driver after those patches were finally open-sourced later in the year. With Linux 7.4 should be a nice AMDGPU HDMI 2.1 experience with modern Radeon graphics.
On the AMD iGPU side there is a very nice improvement with the AMD PerfOpt IOMMU feature. This AMD PerfOpt feature being enabled by default can yield big AI/LLM performance improvements for AMD iGPUs, including prior generation hardware too.
Linux 7.4 is also bringing more AMD Zen 6 support additions and improvements like the new BTB CTX isolation feature, AMD RMPOPT optimization, and AMD P-State driver improvements for Ryzen Zen 6 CPUs.
Linux 7.4 is also adding support for the NPU of the Ryzen AI Max 400 series (Gorgon Halo) with that device ID mistakenly missing from the AMDXDNA accelerator driver until now.
Over on the Intel side is preparations for Rugged Panther Lake and merging the Intel BFF driver. Intel also has a nice improvement on the graphics side for Battlemage of CPU binds and ULLS on the migration queue. The Intel graphics driver is also introducing a vRAM health check and degraded memory handling.
There also continues being a lot of work heading into the NVIDIA Nova driver.
Also exciting is Linux 7.4 upstreaming support for a few Qualcomm Snapdragon X2 laptops. More work there continues to materialize from Qualcomm.
On the Apple side, Linux 7.4 is slated to add initial Device Trees for the Apple M4 and the A18 Pro for the MacBook Neo. But as with the current Apple M3 upstream Linux kernel support, it's not yet usable for end-users. More enablement work is still happening for Apple M3 and newer before all the hardware functionality is wired up and working, but at least the mainline kernel can boot. Apple Silicon for Linux 7.4 is also seeing audio support going upstream. [...]

## [79] Scale isn’t one number: three ways a Kubernetes control plane runs out of room
The New Stack | full text via The New Stack | ~1264 words

Scale isn’t one number: three ways a Kubernetes control plane runs out of room
Three clusters in trouble, and they look nothing alike.
The first is a training fleet. It sat at a few thousand nodes for months, then a new run landed, and it’s at fifteen thousand. Kube-apiserver starts eating memory. Etcd starts complaining.
The second never passes a few thousand nodes and is having a much worse day. It’s an agent platform, and its objects are alive: sessions created, suspended, resumed, and destroyed thousands of times a minute, every transition a write.
The third is neither big nor fast: a platform cluster with two hundred operators installed and tens of thousands of objects that mostly just sit there, and every apiserver holds a copy of all of them.
Two of those are AI workloads, and one isn’t, which is the least interesting part. They’re running out of room in three different directions, and fixing one does nothing for the others.
KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12. Register now!
Go looking for guidance, and you find… not much. There’s plenty of advice for getting to 5,000 nodes. Past that, or sideways from it, the internet shrugs.
So you add more apiservers. It’s a documented option in kOps and the standard answer you’ll get from most people. It makes your problem worse, because every apiserver you add replicates the entire watch cache. You bought request capacity and paid for it in memory you didn’t have.
None of these is a research project. Clusters well past 5,000 nodes run in production today on stock upstream components. Nobody got there with a magic fork; they got there by being deliberate about what each store holds.
The scale isn’t the hard part. The assembly instructions are missing.
Three kinds of scale
Ask how big a control plane needs to be and the answer comes back in nodes. That’s how the second and third clusters end up tuned for a problem they don’t have.
“The scale isn’t the hard part. The assembly instructions are missing.”
Node-bound. Training and RL fleets: large, homogeneous, and the pressure is every kubelet reporting in. At 100,000 nodes with a 10-second heartbeat, liveness alone generates about 10,000 writes per second, and in our measurements lease renewals were roughly 70% of write QPS. Most of what that control plane does is nodes politely saying “still here,” forever.
Churn-bound. Agent platforms: modest size, very intense day. [...]

## [80] It Turns Out Intel TDX Doesn't Need So Much Cache Flushing
Phoronix | full text via Phoronix | ~298 words

It Turns Out Intel TDX Doesn't Need So Much Cache Flushing
Intel Trust Domain Extensions (TDX) for confidential computing with VMs has assumed the need to perform cache flushing when transitioning memory between KeyIDs used by the total memory encryption (MKTME) for unique AES encryption keys. But it's turned out to be unneeded and the Linux kernel is working now to reduce the excessive cache flushing.
In what may help Intel TDX VM performance by eliminating unnecessary flushing of the caches, the Linux kernel has a set of patches pending to eliminate the software-driven cache flushes as its being properly handled by the Intel Xeon processor hardware.
Intel software engineer Rick Edgecombe explained of the patch series "Drop unneeded cache flushing" on the Linux kernel mailing list:
"In the early days of TDX it was assumed the HW would need some cache flushing help around transitioning memory between KeyIDs, and so TDX arch was designed to specify how the VMM needed to help the module perform this. But it turned out the HW was able to handle these issues without SW help. For some reason the TDX arch around performing the flushes remained. Now the TDX arch is getting fixed and Linux can remove the code that was helping perform this unneeded cache flushing. The changes will appear in 
a future documentation update."
Apparently all finalized TDX hardware don't require the extra software-driven cache flushing around the KeyIDs but the Intel documentation was never updated to reflect that, but those Intel docs will be updated in the next revision. Intel TDX initially appeared in select Xeon Sapphire Rapids processors but has been supported by all Xeon processors since Emerald Rapids.
This leads to simpler kernel code but no word in the patch messages of any expected performance impact.

## [46] How to use Google's SynthID AI detection website
Engadget | full text via Engadget | ~729 words

How to use Google's SynthID AI detection website
It's a simple way to check whether an image has been created or manipulated, with a few caveats.
With the proliferation of generative AI tools pumping out images, videos and even songs in recent years, it's hard to spend time on the internet without wondering whether what you're seeing or hearing is real. Google, itself one of the largest purveyors of generative AI, is now making it easier to spot its output. With the new SynthID Detector, anyone can check an image, video, or audio file to see if it's been AI generated, with some major caveats.
Google introduced SynthID in 2023, which adds an imperceptible label to AI-generated content, but there was no way for regular users to actually check for one until now. In 2025, it launched a limited version of SynthID Detector for certain researchers and journalists, and now it's available for everyone. While that may be good news for anyone looking for a way to verify whether a piece of content was generated with AI, it's far from foolproof.
How SynthID Detector works
Since the launch of SynthID, Google's Gemini AI model has embedded a watermark in everything it creates. SynthID Detector works by scanning for that watermark and giving users a simple yes or no answer as to whether one was found. To use the newly available tool, you just need to go to SynthID.com, upload an image, video or audio file, and wait a few seconds for Google to return a result.
That's a big improvement over Google's previous process. Before now, users could ask Gemini itself if a piece of content was AI generated. But for anyone who doesn't trust generative AI, it's hard to take Gemini at its word, and it's an immediate no-go for people who are trying to avoid the technology altogether. SynthID Detector also allows users to scan for watermarks embedded in content created by Google's SynthID partners, which wasn't possible before. That means the new tool can tell whether media was made with AI models from OpenAI, NVIDIA and Kakao, in addition to Gemini. Apple also participates in SynthID, but support for the detector to identify its creations is still in the works.
How reliable is SynthID Detector?
Since SynthID Detector is simply checking for a watermark rather than analyzing media for patterns that indicate AI use, it should eliminate the chance of false positives. That simplicity introduces its own limitations, though. [...]

## [59] Anthropic says it’s committing 5% of its shares to a ‘public benefit fund’
TechCrunch | full text via TechCrunch | ~187 words

Anthropic announced today that it’s creating a “public benefit fund” that will give the company “increased flexibility and scale” to support projects for societal good.
Anthropic said that it will commit 5% of its shares to the fund — structured as a wholly-owned entity within the company — with the option to contribute an additional 2% for every 50% increase in Anthropic’s value. And it offered some broad-strokes ideas for how this money might actually be used, such as “large donations to traditional nonprofits or direct distributions to specific populations.”
There’s also the impact that AI might have on the job market, which Anthropic has already committed $200 million to study. But the company said, “Given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them.”
Anthropic’s announcement comes as the AI industry faces increasingly negative public sentiment, which CEO Dario Amodei has described as “fundamentally a crisis of trust.”
If you’re wondering who will actually decide which public benefits are worth funding, Anthropic said it will share more information about structure and governance in the coming months.

## [22] A New Way to Think About Borrow Checking (In Reverse)
Lobsters | full text via Lobsters | ~2559 words

Have you ever had a weird idea, and then it worked, but you can't really believe it?
That's what I'm feeling right now, about Valen's borrow checker.
Because it travels backward through time.
Or, to be less dramatic, it walks functions backwards, which is still very weird.
Years ago, if you told me it would be good to iterate a function in reverse, I would have called you crazy.
It turns out, there's actually some really good reasons to do this, and it's fairly common when you're doing e.g. optimization passes. 0 But I don't think anyone's done this for checking memory safety.
If you want a really deep look into the world of borrow checking, read on!
We're about to see some weird things. 1
Or destructor insertion, and now, checking memory safety!
0% of this article was written by AI. More thoughts here.
My stance: if you want someone to take the time to read something, take the time to write it by hand.
Thanks for reading =)
This isn't going to be your normal shared-xor-mutable borrow checking.
This is Valen's borrow checker, the one that makes shared-xor-mutable optional, and can call into Rust functions with memory safety across the boundary.
It's kind of like Rust's borrow checker, but it also has memory-safe mutable aliasing. If you want to know more about that, check out this post, though you won't need to understand that for most of this post.
Green dragons, specifically.
Valen compiles a function in four phases: 3
I'll explain all of this further below.
The weirdest part is that #4 happens in reverse. It looks at the last statement in the function, and then walks backwards until it reaches the top of the function.
This is weird because, as far as I know, it's the only borrow checker whose safety check goes backwards. 5
Further below, I'll explain why we're going backwards (hint: convenience, loops, and speed).
But first, let's see how it works, and what it even means to go backwards.
Let's skip phase 1, and start with phase 2.
There's also a secret fifth phase, where we calculate what attributes to send to LLVM to describe what operations might change what groups. But that's out of scope for this article.
It also figures out all the groups invalidated by any mut effects from any instructions.
For example:
The static typing pass will be familiar to some of you, it assigns types to variables. [...]

## [74] Programming Language Popularity Increases for R, Julia, and Rust (but Not Go)
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~103 words

TechRepublic reports: The TIOBE Index is a monthly indicator of programming-language popularity based on factors including skilled engineers, courses, and third-party vendors. The October 2026 rankings show a largely stable top 10, with R overtaking SQL and Julia returning to the top 20 for the first time in three years. [SQL has risen to #9 from #10 in October of 2025 — back when R ranked only #13.] Python remains No. 1, followed by C, C++, Java, C#, and JavaScript, while Rust holds its No. 10 position. [A year ago Rust ranked only #16.] Outside the top 10, Julia climbs from No. 21

## [88] FSF Criticizes Raspberry Pi DRM Blocking RAM Upgrades
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~91 words

The Free Software Foundation "has never supported Raspberry Pi," writes their deputy directory Sean O'Brien, "as it depends on nonfree software for the boot process, leaving an important part of the computer outside the user's control." But they're now decrying "an even more intrusive restriction on user freedom" — the binary-blob bootloader changes that limit your ability to upgrade RAM: The restriction is not new: the relevant checks were introduced in the device firmware around 2024. However, these hardware handcuffs have only recently received wider attention. Though a user can d

## [52] A Savannah police officer gave her Flock login to her ICE agent husband
The Verge | full text via The Verge | ~195 words

Now, former Savannah police officer Amber Harpe was fired in August following a department investigation that found she had shared her Flock login information with her husband, Tyler Harpe, an ICE agent. SPD does not share its Flock data with ICE and said sharing access to the system violated the department’s security protocols.
A Savannah police officer gave her Flock login to her ICE agent husband
SPD officer Amber Harpe was fired for sharing her Flock access with her ICE agent husband.
While he had unauthorized access to the system, Tyler Harpe conducted 983 searches related to 97 license plates, which were overwhelmingly registered to Hispanic drivers, according to Savannah’s local ABC affiliate, WJCL. The Harpes defended their actions, saying they didn’t use access for personal reasons and that the searches were strictly for “law-enforcement purposes.”
Interim Major Max Nowinsky originally recommended a light eight-hour suspension for Harpe. However, Major Michelle Halford and Assistant Police Chief Robert Gavin disagreed, and they removed her from the force. Harpe was fired, along with five other SPD employees, after an internal investigation uncovered Flock misuse. Four of them were later arrested; however, Harpe was not one of them.

## [102] Here are the engineering lessons we learned when live-streaming sports to 32 million people
The New Stack | full text via The New Stack | ~1673 words

Here are the engineering lessons we learned when live-streaming sports to 32 million people
Live sports involve myriad unknowns, but one thing is certain: the live video feed must play flawlessly, and simultaneously, for all the fans tuning in. If some hear their neighbors cheering or groaning 5 seconds before each score, they won’t have kind words for their streaming platform.
In 2023, Ashutosh Agrawal and his JioHotstar (then JioCinema) engineering teammates prepared for the Indian Premier League (IPL) cricket finals as intensely as the athletes. While the players ran on the pitch, the engineers ran their own training simulations and drills to ensure every fan could celebrate (or commiserate) in sync.
A year ago, he joined us at P99 CONF to share how they built and tested the system behind that record-setting game, plus lessons learned that can help anyone preparing for high-uncertainty events (Black Friday, anyone?).
Watch the complete talk, or read the highlights below. And if you enjoy these types of engineering case studies, join 30K of your peers for P99 CONF 2026, which is free and virtual. Grab a complimentary pass and join us October 21 and 22!
Pre-game
The IPL is the premier cricket tournament and one of the world’s most-watched sports. And Ashutosh is an IPL pro, from the engineering perspective at least. After working on the backend streaming platform since 2018, he’s learned that “with cricket, you never know what will happen.”
In 2023, the final ended up drawing a then-record-breaking 32M concurrent viewers. But they were ready for even more. Just to be safe, the team builds and tests for roughly double the capacity they expect: “a scary number that scares the hell out of everyone on the team,” as Ashutosh put it. That year, they prepped for 50M to 75M. Aiming that high provides the headroom needed to absorb traffic spikes without requests piling up.
Keeping the video feed flawless is their top priority. He explained, “You can sacrifice every other system and component in the line, but anything in the line of video delivery has to be a golden path — it cannot fail. Because if that fails, the entire promise of the platform goes away.”
“You can sacrifice every other system and component in the line, but anything in the line of video delivery has to be a golden path — it cannot fail. [...]

## [101] MeshXFS: AI Adapts XFS Into A Clustered File-System
Phoronix | full text via Phoronix | ~423 words

MeshXFS: AI Adapts XFS Into A Clustered File-System
MeshXFS is a clustered open-source file-system in which "no human wrote any of its own code". Depending upon your views of AI, not necessarily something you want to hear for entrusting your data in an AI-created solution. Instead, Claude Opus was tasked with adapting the XFS file-system driver into a clustered file-system.
Steve Shoecraft who started the MeshXFS project and wrote into Phoronix to highlight the initiative. He remarked:
"MeshXFS began as an experiment to answer one question: can AI write a kernel filesystem driver, and not a simple one, but a clustered filesystem with distributed locking, concurrent access from many nodes, fencing and crash recovery? It is now a working, released, open-source (GPL-2.0) POSIX clustered filesystem, and the answer so far is yes."
XFS was adapted into a POSIX clustered file-system complete with distributed locking, many node concurrent access capabilities, fencing and crash recovery, and other features. Steve further explained of this MeshXFS creation:
"It starts from the upstream XFS code, written by the XFS developers. Everything that turns XFS into a filesystem many machines can mount read-write at once was written by AI:
- two distributed lock managers: one over the network, and one that keeps lock state on the shared disk itself using SCSI COMPARE AND WRITE, with no lock network at all
- cache coherency across nodes, fencing with SCSI persistent reservations, and survivor-led journal recovery
- an on-disk envelope around XFS, plus the userspace tools (mkfs, fsck, resize)
- every change to the forked XFS code since the fork (the xfs/ tree has grown from about 226k to about 314k lines)
- the test harnesses, the test rig automation, and the release validation
Claude Opus, running as an autonomous coding agent in Claude Code, did a large share of the work, consulting Claude Fable, GPT, Gemini and Astra on the hardest problems: lock protocol design, recovery races, fencing correctness. The AI also wrote and ran the tests, diagnosed the failures and fixed them. My part was setting the goal and the bar: data integrity first, never crash the host, and stay within twice the time native XFS takes on the same storage. [...]

## [1] Namecheap just seized and disabled all my domains
Hacker News | SNIPPET ONLY (Hacker News: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [25] AWS Will Run Its European Sovereign Cloud Without the Global Backbone for Several Hours
InfoQ | full text via InfoQ | ~848 words

On Saturday, October 24, AWS will cut its European Sovereign Cloud off from the AWS Global Network backbone for several hours. The region is expected to keep running. What that proves is a narrower thing than the argument now going on around it, and AWS says so itself.
Two systems come out. One is the Global Network backbone, the private network that moves operational data between AWS locations. The other is a dedicated channel for limited data transfers, switched off entirely. Traffic then falls back to the public internet over the region’s own links from European ISPs. Stéphane Israël, managing director of the AWS European Sovereign Cloud, says a team "composed entirely of EU residents working in the EU" will run it on the region’s own hardware and software, out of data centers in Brandenburg that hold a local in-EU copy of the source code. Customers may see short disruptions while routes converge at either end.
The caveat comes from AWS. Neither system is operation-critical. That is why the region survives without them. It is also why the region uses both every other day of the year. Data gets a sharper line. Customer content and customer-created metadata stay in the EU. Some operational data leaves. Israël writes that the exercise is built to line up with the EU Cloud Sovereignty Framework and Germany’s BSI C3A criteria, and that customers can put the results into their compliance packages. Regulators hear about it afterwards too. The post stops well short of claiming certification. It does not pretend the region runs isolated the rest of the year either.
None of that care has settled anything. Fadi Dasus, a senior cloud security architect, split the question in two:
Sovereignty on a US-owned cloud in the EU comes down to two areas. The technical one: does the service stop if the link to the US is cut? The legal one: can US law order it to hand over your data, or to stop serving you? If the test goes as planned, the first area is no longer entirely in American hands. The second still runs through the US parent. So, this is real progress for resilience. It just isn’t sovereignty.
Lars Larsson Lundsten, field CTO at Elastisys, which sells a European alternative to US cloud platforms, put it harder. "You can’t solve legal problems with technical solutions" he wrote, while calling the architecture a marvel of engineering. [...]

## [98] Synchronous Queues For VirtIO-FS Show Huge Performance Potential
Phoronix | full text via Phoronix | ~188 words

Synchronous Queues For VirtIO-FS Show Huge Performance Potential
VirtIO-FS as the shared file-system for transferring data between guest VMs to/from a host server is showing some promising performance results with pending code for allowing synchronous queues rather than always being asynchronous.
Sergio López has been working on supporting synchronous queues for VirtIO-FS. VirtIO typically relies on asynchronous behavior but often times for I/O transfers you are specifically waiting on that to complete. Thus he pursued experimental synchronous queues for VirtIO-FS so the host thread running the vCPU process can complete the request before returning to the guest.
The synchronous queues is showing massive performance potential with the time to build libkrunfw being used as a test, which dropped from 7 minutes and 43 seconds to just 5 minutes and 34 seconds in using synchronous queues.
The sync queues also showed very significant improvements in random I/O performance, lower file deletion latency, and more.
More details on this very promising work for VirtIO-FS via this blog post. There is a pending experimental pull request for libkrun adding the optional VIRTIO_FS_F_SYNC support. Very promising results so far for this implementation.

## [104] AI has lowered the barrier to building. Here’s what that means for engineers.
The New Stack | full text via The New Stack | ~844 words

AI has lowered the barrier to building. Here’s what that means for engineers.
For most of software’s history, building meant writing code. Not just understanding it, but producing it. The entry point was steep by design: fluency in at least one language, working knowledge of system architecture, enough production scar tissue to know what questions to ask before writing the first line. The barrier was real, and both sides of it understood why it existed.
AI coding tools, natural language interfaces, and agentic workflows have started shifting what it takes to go from an idea to working software. A product manager can now prototype a functional application without writing a single line of code. A data engineer can spin up a pipeline in hours that would have taken a team a week to scope and test. Domain expertise that used to be locked inside someone’s head is becoming portable in a way it never was before.
“The constraint wasn’t the knowledge. It was the translation layer between knowing something and being able to build something. AI is removing that layer.”
The constraint wasn’t the knowledge. It was the translation layer between knowing something and being able to build something. AI is removing that layer.
What actually changed
The fundamentals of good software haven’t moved. Clean architecture still matters. Sound data practices still matter. Understanding how a system behaves under load, or what happens when a third-party dependency changes unexpectedly, still requires genuine technical depth. What AI removes is the gatekeeping, the parts of the process that required specific syntax knowledge not because the problem was conceptually hard, but because the tooling demanded it.
The practical effect is that domain expertise is becoming portable. A logistics engineer who understands her company’s routing problem better than anyone in the building can now build a prototype that captures that understanding directly. A security analyst who knows exactly what anomaly pattern to look for can now build the monitoring tool to find it. The knowledge was always there. What changed is the path from knowing to building.
“What AI removes is the gatekeeping, the parts of the process that required specific syntax knowledge not because the problem was conceptually hard, but because the tooling demanded it.”
For platform and infrastructure engineers, this creates a new class of stakeholder. [...]

## [105] AI agents vs. Kubernetes: where each belongs in the control loop
The New Stack | full text via The New Stack | ~1114 words

AI agents vs. Kubernetes: where each belongs in the control loop
Kubernetes has always relied on agents, just not the kind dominating today’s AI conversations. A controller watches the current state, compares it with a declared desired state, and takes action to close the gap. That resemblance makes AI agents and Kubernetes operators sound interchangeable. They are not.
This question is no longer theoretical. Over the past 18 months, agent tooling has moved from a side project to part of the cloud-native stack. CNCF has accepted agent frameworks into its Sandbox, and Kubernetes SIG Apps has taken on Agent Sandbox as a subproject for running agent workloads safely.
Platform teams are already deciding what an agent can change in a live cluster, usually one pull request at a time and without a written policy. By default, the boundary between reasoning and execution is set by convention rather than design.
KubeCon + CloudNativeCon takes place in Salt Lake City, Utah, November 9 to 12. Register now!
A Kubernetes operator is designed to be predictable. It reconciles resources according to encoded rules, retries failed operations, and converges on declared state. An AI agent is useful when the desired outcome is clear but the path isn’t. It can investigate an unfamiliar situation, gather context from several systems, weigh tradeoffs, and propose a course of action.
A safer architectural pattern combines these strengths. The agent supplies reasoning and context. Operators, policy engines, and other deterministic systems retain control of execution.
A reasoning layer for Kubernetes
kagent, an open source CNCF Sandbox project, provides a concrete example of this pattern. It runs AI agents as Kubernetes resources and connects them to Kubernetes, Helm, observability, and custom tools. An agent can inspect resources, retrieve logs and events, query metrics, consult documentation, and coordinate specialized agents.
That does not mean every tool should be freely executable. Non-sensitive read operations can run automatically, while changes such as applying, patching, or deleting resources can require explicit approval. This separation lets the agent conduct a broad investigation without giving an uncertain reasoning process unrestricted authority over the cluster. [...]

## [37] SQLite 3.54's diskused command needs a build flag sqlite3_analyzer never required
Dev.to | full text via Dev.to | ~1356 words

SQLite 3.54.0 shipped on 9 October, and the change list has one line that's easy to skim past: the sqlite3_analyzer utility is now deprecated, replaced by a diskused() SQL function built straight into the command-line shell as a new .diskused dot-command. I wanted to know what that actually buys you, and what it costs, so I built both versions from source and ran them against the same database.
sqlite3_analyzer has been the way to answer "which table is eating my disk space" for as long as I can remember using SQLite seriously. It's a separate program you download or build on top of the library, and it opens your database file cold, walks every b-tree page, and prints a report. .diskused does the identical analysis, but it runs inside the shell you already have open, using a virtual table (dbstat) the engine already exposes internally.
Same report, less than half the time
I built a 20MB test database — four tables, one index, 350,000 rows — and ran both tools against copies of the same file, five times each:
=== .diskused (new, 3.54) ===
0.028s  0.023s  0.022s  0.024s  0.029s
=== sqlite3_analyzer (old, deprecated) ===
0.056s  0.061s  0.058s  0.055s  0.076s
That's roughly 2.4 times faster on the mean, and the gap holds at the fastest runs too. Part of that is architectural rather than algorithmic: sqlite3_analyzer is a 3.3MB standalone binary that has to start its own process and open its own connection to the file from scratch, where .diskused runs a SQL function against a connection the shell already has open.
The two reports agree on every number I checked — page counts per table, bytes of payload, unused bytes per page, b-tree depth — which is exactly what you'd want from a replacement. But .diskused's output is 242 lines and 13KB; sqlite3_analyzer's is 432 lines and 21KB for the same database. The new tool drops some of the older report's redundant subsections (separate "all indexes" and "all tables" rollups that .diskused folds into fewer blocks) without losing any of the figures I actually used.
It fails, and tells you nothing about it
diskused() depends on dbstat, a virtual table that SQLite only exposes when it's compiled with SQLITE_ENABLE_DBSTAT_VTAB. The official binaries on sqlite.org have that flag set, so if you download the prebuilt shell, none of this applies to you. [...]

## [94] Servo Gets CSS Grid Working, Threadboost Offering Big Speed-Ups
Phoronix | full text via Phoronix | ~179 words

Servo Gets CSS Grid Working, Threadboost Offering Big Speed-Ups
Servo's August status report has finally appeared for outlining progress made on this open-source, Rust-based browser engine. This follows the recent release of the Servo 0.6 software, including the Servoshell demo browser.
One of the most notable features to have landed recently for Servo is CSS grid support. In turn many more websites are now rendering correctly on Servo.
Servo also landed other new features like CSS color-scheme, animation-composition, full-width, text-transform, and more. A number of new DOM APIs are also now in place.
On the JavaScript side, Servo pulled in SpiderMonkey 153 for security and crash fixes. Servo also now presents a disk-backed HTTP cache that can be optionally enabled but without any way to clear it at the moment.
Servo also sees more work happening around accessibility, prep work toward AudioWorklet, and more. Performance improvements have also been landing for this engine. An experimental "Threadboost" feature is improving the Speedometer benchmark scores by 50%.
More details on these recent improvements to the Servo engine via the Servo.org blog.

## [5] Free Pascal compiler now supports dynamic packages
Hacker News | full text via Hacker News | ~1123 words

Dynamic Packages
I am pleased to announce the first release of full dynamic package support for the Free Pascal Compiler and the Lazarus IDE. This feature has been a long time coming for the ecosystem, but a complete implementation is now available for download from this website.
Dynamic packages allow users to create and install components, controls, and Lazarus extensions in seconds without rebuilding the entire IDE. They can also be used in your own programs to develop and deploy plugins that expose native Pascal classes and types through dynamic package libraries. To support this functionality, I have made numerous improvements to the compiler, its runtime, and the Lazarus IDE. I have also created additional IDE extensions to improve the experience of working with Lazarus packages.
Dynamic packages are implemented as standard shared library files for Linux, Windows, and macOS. They contain additional metadata generated by the compiler that can be inspected and queried using new RTL units. The runtime also includes mechanisms for safely preserving thread variables and managing dynamic types, such as strings and dynamic arrays, between programs and packages or between multiple packages.
Video: Dynamic Packages Example
When deploying your program, you can still bundle everything into a single executable. Alternatively, you can divide it into multiple dynamic packages that can be replaced while your program is running, providing a plugin system.
Restrictions
Dynamic packages come with a few restrictions. First, a unit contained in a package cannot have the same name as the package itself. I have enhanced the default package system so that the generated Pascal source file automatically appends the word Package to the package name. For example, if you create a package called
ElectroTools.lpk
, the source file listing all the units contained in the package will be named ElectroToolsPackage.pas
instead of ElectroTools.pas
.
Another restriction is that unit names must be unique across packages. If someone else has written a unit named Widgets, you cannot install another package containing a unit with the same name. You must either choose which package to install or rename one of the conflicting units.
Dynamic packages are also larger than ordinary shared libraries because they contain a map of everything inside them. Stripping a dynamic package removes the metadata required for it to function as a dynamic package. [...]

## [111] Linux Lands Fix for Rare, Varying SMP Boot Hangs Affecting Kernels Since 2024
Phoronix | full text via Phoronix | ~272 words

Linux Lands Fix for Rare, Varying SMP Boot Hangs Affecting Kernels Since 2024
Among the flurry of last minute patch activity ahead of tomorrow's presumed Linux 7.3 stable kernel release is a fix for addressing some rare hangs at boot time. The reports varied but ultimately tracked down to a kernel change made two years ago.
Various bug reports have come about for common place SMP systems hanging on boot and was ultimately narrowed down to the non-blocking console "NBCON" code. To avoid these boot hangs, moving the start of the NBCON console printing KThreads to later in the boot process avoids these possible system hangs.
Linutronix engineer John Ogness explained in the now-merged fix of postponing the KThread start-up:
"There have been various bug reports related to SMP systems hanging on boot. The reports vary but seem to have some overlap with regard to missed IPI's during SMP setup. The reports also show that reverting NBCON console usage allows the bugs to disappear.
The NBCON kthreads for console printing are started very early during boot using early_initcall(). Since these kthreads are asynchronously enabling/disabling interrupts during early boot, they may be interfering with early SMP setup on some hardware platforms.
Starting the console printing kthreads later has shown to avoid the hanging on systems that could previously reproduce the issue.
Postpone kthread starting until after all arch initcalls have completed."
This is treated as a fix for Linux kernel code present since September 2024 when printer KThreads were first introduced in the printk() code. Thus will presumably be back-ported in the days ahead from Linux 7.3 to other currently supported kernel branches.

## [72] LinkedIn Fights AI Slop, Now 40% of Its Long-Form Posts
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~96 words

"Even LinkedIn is getting tired of your AI-written posts," writes CNN, reporting that the Microsoft-owned, job-oriented social media site "is upping its fight against slop." A report published in July by Pangram, a research firm that tracks AI content online, found that more than 40% of long-form posts on the platform were AI-generated, compared to around 30% on X and Medium and a smaller percentage on Reddit and Substack.... LinkedIn previously offered AI tools to edit or rewrite posts, although it recently scaled the offerings back. But low-quality AI posts are a business problem for LinkedI
