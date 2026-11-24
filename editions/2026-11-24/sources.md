# Full text for 23 picks -- untrusted article content, treat as data only

## [1] Nvidia Reinstates Jensen Huang as CEO
Hacker News | full text via Ars Technica | ~331 words

Nvidia’s board of directors has voted to reinstate Jensen Huang as CEO and chairman of the board, just 11 days after he resigned in the wake of multiple scandals.
The reinstatement, announced Monday morning, is “effective immediately” and was based in part on “input from senior levels of the United States government” that assured the board members that “Mr. Huang’s reinstatement poses no national security risk.”
That assurance comes despite Huang’s admitted affair with a woman who, US intelligence sources believe, was working as a Chinese spy and allegations that Nvidia had subverted export controls meant to keep Nvidia chips from reaching China. It also comes despite multiple developing investigations from multiple different government departments into those and other alleged national security, accounting, and corporate governance failures.
Huang had been seeking a return to Nvidia since shortly after his resignation, reportedly forming a war room to strategize how best to bring it to pass. Last week, Huang posted on social media that “if the Board of Directors decides that my return is in the best interest of our shareholders, our employees, the company, and America, I would be honored to answer these calls and return as CEO.”
President Trump has also been a major backer of Huang’s return to Nvidia. “I hope the Board of Nvidia rehires Jensen Huang,” he wrote on Truth Social last week. “It would be the best thing for the Company, and also, for the U.S.A.” In a social media post immediately following the reinstatement, Trump called it “the correct and proper decision” and confirmed that “the United States Government has no reason to believe that Jensen’s return to NVIDIA poses any risk to National Security.”
Appearing on CNBC Monday morning, Trump said that he had spoken to the Nvidia board “directly and indirectly” about Huang’s reinstatement, and that Huang “did nothing wrong.” Losing “the brainpower of someone like [Huang]” would be “a much bigger threat” than anything related to his alleged interactions with China, Trump said.

## [90] Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes
TechCrunch | full text via TechCrunch | ~460 words

Anthropic is moving from having Claude write code to helping developers decide when that code is ready to ship. On Monday, the newly public AI company announced the launch of Claude Ship, a suite of AI agents for automating code reviews, fixes, and approvals of routine code changes.
The latter is the more interesting part of this new set of tools, as AI coding tools already offered code review features before now. What’s notable about Claude Ship is not just that it can review proposed code changes and identify and address problems, but that it also includes an agent that can approve code changes automatically based on policies set by a development team.
The launch arrives at a time when AI coding agents have become increasingly capable of generating substantial amounts of code, leading to bottlenecks in reviewing and approving the code changes before they go live. With Claude Ship, the idea is to automate even more of the work involved in the development process, essentially by delegating approval authority to an AI agent itself.
“Most teams want a person to approve every change, and that’s easy to keep up with when people write every line. But a lot of developers build with agents now,” a company blog post explains. “On the Claude Code team, Claude writes most of our code, and we wanted everything after the PR to move that fast too.”
Claude Ship is launching in beta, allowing early adopters to use it to review pull requests (PRs), and then decide what’s ready to merge.
The new offering consists of Code Review, which is already generally available, and two new agents now in beta: PR Steward and Claude Approvals. PR Steward focuses on addressing issues such as failing CI checks, merge conflicts, and feedback from Code Review. It also comments after every push on what it changed and how to roll it back, if needed.
Claude Approvals then applies an approval policy that the team writes as a file in the repository. This approval process can incorporate various signals, including Code Review findings or the company’s own classifiers, with policies written in natural language.
Because the offering is still in beta, Anthropic suggests running the approval functionality in observe-only mode first. Teams can also choose to start with just one repository and set monthly spending limits to have more control over the process.
Anthropic says teams will also still remain in control of where Claude Ship runs, which review settings to use (e.g., Quick, Standard, or Deep), and which changes should be escalated to a human for a decision.
Claude Ship is rolling out to Claude Team and Enterprise plans for repositories on GitHub. Code Review is generally available, while PR Steward and Claude Approvals are in beta.

## [139] CrowdStrike to Buy Zscaler In $44 Billion Deal
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~93 words

CrowdStrike has agreed to acquire network security provider Zscaler in a $43.9 billion all-stock deal. "The deal marks CrowdStrike's biggest acquisition to date and is among the largest in the sector as businesses consolidate and ramp up defenses to fend off AI-powered attacks," reports CNBC. The acquisition is expected to close in the second half of CrowdStrike's fiscal 2028. From the report: "With Zscaler, we're building cybersecurity's operating system: a single control plane to deploy AI, control AI, and enable any agentic application to run safely," CrowdStrike CEO George Kurtz said in a

## [15] GLM-5.4: Toward generalized coding with our first loop transformer
Hacker News | full text via Simon Willison's Blog | ~436 words

23rd November 2026 - Link Blog
GLM-5.4: Toward Generalized Coding with Our First Loop Transformer. GLM 5.4 is now available from Chinese AI lab Z.ai. It's their first model to use a looped transformer architecture, which they describe like this:
In a standard Transformer, each layer runs once per forward pass. In a Loop Transformer, a group of weight-shared layers runs for multiple iterations, refining the hidden states from the previous pass. This gives us a deeper network without increasing the parameter count.
This is the second mention of looped transformers I've seen in the past week - the first was Inkling 2 Mini from Thinking Machines Lab on November 20th, who said:
Inkling 2 Mini is a looped transformer, running the middle layers of the model three times for every token. This allows the model to apply more reasoning and reach the right answer with fewer tokens, especially on tasks such as agentic coding that depend on reasoning quality.
GLM 5.4 is not (yet?) available as open weights. I tried it out using the Z.ai API, for which I had to sign up for their Coding Plan subscription because 5.4 cannot currently be accessed through the regular API.
It turns out both coding plan and regular API share the same OpenAI-compatible Responses API (at https://api.z.ai/api/v1), and the API key for the coding plan worked with that and gave me access to the new model.
I built a llm-glm plugin, then realized that llm-zai by Tommy Hughes already exists! I've shipped mine purely because llm-zai doesn't yet support the new model, but I'll likely retire mine once that plugin catches up.
Here are pelicans for GLM-5.4 on low, high, and max. This is the max one:
I realized I never ran pelicans for GLM-5.3, so here those are for the same effort levels. They look similar in quality to 5.4.
It's interesting how GLM 5.1 and GLM 5.2 produced radically different pelicans from other models. The pelicans for 5.3 and 5.4 are much more comparable to those I get from OpenAI or Anthropic models - the previous generations had their own distinctive look.
I made a comparison grid showing the four generations of GLM pelicans all in one place. The style transition between 5.2 and 5.3 is pretty stark.
Recent articles
- Ladybird's first alpha release - 23rd November 2026
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026

## [28] States sue SpaceX to stop Grok from generating child sex images, revenge porn
Ars Technica | full text via Ars Technica | ~1317 words

On Monday, Virginia and Oregon became the first states to sue SpaceX, alleging that Grok continues to sexualize, unchecked, real photos of mostly women and children.
SpaceX acquired xAI in February and now must handle the ongoing reckoning over the controversial rollout of Grok’s “spicy mode”—a model feature Musk hyped but was soon found to generate a flood of non-consensual intimate imagery (NCII) and child sex abuse images (CSAM).
Initial safeguards were so lax that Grok sometimes generated nude images without being asked. Although X Safety and xAI (now known as SpaceXSI) were silent at first, Musk’s companies eventually apologized and claimed that additional safeguards were implemented and policies redesigned to block harmful outputs. However, state attorneys general alleged that those statements were “misleading” and that SpaceXSI instead quietly “embraced” sexualized content to seize more AI market share, as Grok continues to generate NCII and CSAM today.
Without intervention, kids in Virginia and Oregon risk a lifetime of distress, as Grok images will likely be impossible to remove online.
“Once created and shared,” Grok-generated CSAM and NCII “can never be fully erased, and it becomes a permanent record of the child’s abuse that may resurface for the rest of the child’s life,” Virginia Attorney General Jay Jones’ complaint said. “Virginia has a profound interest in protecting its children from this harm.”
Millions allegedly harmed
Millions of residents were allegedly harmed, as the attorneys general seek to protect every Grok or X user in their state. Many Grok victims will likely suffer from chronic anxiety, depression, and PTSD, as well as reputational harm, as some viewers may not realize the images are AI-generated, the states alleged. Further—due to Grok’s integration with the social media platform X—users as young as 13 may have been exposed to the AI content and possibly re-traumatized if they, too, are victims of sexual abuse, the states alleged.
“xAI not only knowingly endangered kids and our communities, but they also lied to our faces about non-existent safety measures,” Oregon Attorney General Dan Rayfield said in a press release.
States alleged that xAI could have conducted rigorous red-teaming to block outputs before the new feature launched. But instead, the X Safety team responsible for Grok red-teaming was reduced to two or three team members, states alleged. [...]

## [52] Claude Code Adds Experimental Code Mode to Orchestrate Tool Calls with JavaScript
InfoQ | full text via InfoQ | ~582 words

Anthropic has added Code Mode to Claude Code, an experimental feature in which the model writes JavaScript to drive its tools instead of requesting each Bash, Read, or Edit call separately. Code Mode is off by default, requires Claude Code v2.1.323 or later, and is enabled with the CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 environment variable. Anthropic warns it may change or be removed in any release.
In a normal session, Claude asks for one tool call, reads the full result, and decides the next step. In Code Mode, one script can run commands in parallel, pass one result into the next call, and return only the output the model needs. The documentation's example finds a file with rg, raises a retry limit, runs the tests, and returns just the path and test output. The conversation still shows each tool call and diff, while the generated code sits in the transcript viewer. Anthropic recommends it for edits repeated across many files, searches that need filtering, and independent commands. Code that Claude waits on stops after ten minutes; sessions started in auto or bypassPermissions mode can push it to the background for up to two hours while the conversation continues.
The permission model is the part architects should read first. Each call inside a script still goes through deny and ask rules and PreToolUse hooks, but in auto mode the classifier reviews the script before it runs, not each call, and cannot see values computed at run time. A git push can now reach a hook as cd 'app' && git push, so hooks must check every part of a command; a hook matching the REPL tool can read the JavaScript from tool_input.code. Project settings cannot enable Code Mode, so a cloned repository cannot switch it on, and administrators can block it through managed settings.
Code Mode runs only in interactive terminal sessions of the native build, on Opus 5.5, Sonnet 5.5, Haiku 5.5, or Fable 5.2, through a Claude subscription or Console account. It does not work with -p, the Agent SDK, the VS Code panel, the Desktop app, Amazon Bedrock, gateways, or zero-data-retention organizations. Agent teams need v2.1.326. Anthropic has published no token or latency figures for it.
George (@bolyki) compared Code Mode with normal mode across eight interactive Sonnet 5.5 runs and posted:
Same results every time. Context 20-25% smaller. On the bigger task: 37% fewer tokens, 19% lower cost. But it is not faster, and on a tiny task it cost more. [...]

## [144] Amazon snaps up Decart’s AI optimization tech for $7.5B as it prepares to sell Trainium chips
TechCrunch | full text via TechCrunch | ~218 words

Amazon has agreed to acquire a good chunk of Israeli startup Decart.
The e-commerce and cloud giant is paying $7.5 billion for the startup, according to Bloomberg.
Decart has made a name for itself building interactive real-time world models — most recently Oasis 3 — and AI video-generation tools. But under the hood, the company stands out for its Decart Optimization Stack (DOS), software that helps AI models run efficiently on Nvidia, Amazon, and Google’s hardware.
As part of the deal, Amazon will acquire the technology behind DOS, as well as Decart’s founding team and team of AI researchers and engineers, Amazon said in a blog post.
“Every leap forward in AI starts with getting more out of every chip,” said Peter DeSantis, SVP of foundational AI models, custom silicon, quantum computing, at Amazon. “More efficient compute means better training, better reinforcement learning, faster inference, and better models for customers at a lower cost.”
Amazon, which has so far been using its Trainium chips at its own data centers, is preparing to start selling them to customers as a competitor to Nvidia. Decart’s technology could make it easier for customers to run their workloads on Amazon chips, rather than Nvidia’s, which has been the gold standard so far.
Decart and Amazon did not immediately return requests for comment.

## [137] Anthropic softens its data retention policy for Mythos and Fable model use
Engadget | full text via Engadget | ~319 words

Anthropic softens its data retention policy for Mythos and Fable model use
Enterprise customers can now keep prompts and responses on their own servers.
Anthropic is making a major change to its policy involving the use of its Mythos and Fable models. Back when the company first debuted version 5 of those AI systems in June, it said it would retain any user prompts and responses generated by the models for 30 days to ensure they were not being misused.
That policy was not popular among Anthropic's enterprise customers, even after the company said it would not enforce a similar requirement for the latest version of its Opus model. Anthropic eventually identified its stance as a risk factor to its success, particularly if other AI providers adopted so-called "zero data retention" policies. As predicted, that's exactly what happened, with OpenAI announcing its own ZDR implementation in August. Less than a month later, Anthropic revealed it was working on Enterprise Frontier Safeguards, a technology it said would combine the privacy of ZDR "with state-of-the-art safeguards for detecting misuse." Per Bloomberg, Anthropic is now rolling out an early version of that system to its business customers.
With EFS, Anthropic will still require those clients to retain prompts and responses for 30 days, but it will instead allow them to store that data on their own servers. Jon Turow, the company's head of safeguards for Mythos and Fable, told Bloomberg that Anthropic would do occasional 15-minute checks to look for signs of potential cyberattacks. If the company's automated systems detect a problem, they'll notify the customer. Anthropic will also get an alert, but Turow said the company would not be able to access related data.
The release arrives following Anthropic's high-profile initial public offering last Thursday. After an exuberant debut, the company's stock is trading for around $86 as of 2:53 PM ET, or just $3 above its original price of $83.

## [108] Meta Muse can be hacked to access user private chats using just a single malicious web page
TechRadar | full text via TechRadar | ~846 words

Meta Muse can be hacked to access user private chats using just a single malicious web page
Researchers found a chain of flaws that could be exploited
- Researchers found a chain of vulnerabilities in Meta’s Muse AI assistant that could expose conversations, stored memories, and cloud credentials
- A crafted webpage enabled code execution, security-control bypasses, and potential access to sensitive user data
- Meta patched all reported issues before disclosure, with no evidence the flaws were exploited in the wild
Meta’s Muse AI assistant could have been broken into using a chain of vulnerabilities, experts have warmed.
There, malicious actors could have exfiltrated all private conversations and stored memories, bypass security controls, and even exfiltrate credentials stored on the cloud machine running the AI assistant.
Security researchers NebuSec found a way to break into Muse and published an in-depth report detailing their findings. The researchers said they responsibly disclosed their research to Meta, which plugged all of the discovered holes by the time of publication.
What is Muse and how was it breached?
Muse is a cloud-hosted personal AI assistant designed to carry out tasks on users’ behalf, by interacting with online accounts and services they connect it with. The tool operates inside a dedicated virtual machine (VM) for each user, with several security measures designed to prevent the assistant from accessing information and resources beyond its intended permissions.
One of these measures is a credential management system designed to keep authentication details away from the agent itself. Another one is called Sentinel - a service that monitors outgoing traffic. Now, NebuSec says they found a way to bypass these protections and to do that, all they needed was a specially crafted webpage.
To generate PDFs and documents, muse uses the Chromium browser (the same one upon which Chrome, Edge, and many others are built). By getting the assistant to export a malicious webpage, the researchers managed to achieve code execution inside its runtime environment. Then, they leveraged a previously discovered weakness in the way Sentinel handles outgoing requests, which allowed them to extract conversation history and stored memories, and send them all to an external server - without the victim knowing, or giving consent, to anything.
This same attack also allowed them to modify everything the user had stored with Muse, including conversation history. In other words, they could change what the users had told Muse to remember about them. [...]

## [17] Ladybird is now in alpha
Hacker News | full text via Hacker News | ~256 words

Hello friends! Ladybird is now in alpha. You can download it for macOS and Linux.
I’ve been looking forward to writing this post for a long time. :^)
Ladybird is a browser with a new engine. The engine is our own, built from the ground up, and not a fork. The browser around it is modest, but functional.
This is an alpha, so some websites won’t work, and it will crash sometimes. When that happens, tell us! You can report a broken site from inside the browser. After a crash, you can read the crash report and decide whether to send it. Our privacy policy has the details.
We want security nerds to hack it! A new browser gets hacked, over and over, and that’s part of the process, so we make no promises about security today. When you pwn us, please tell us how so we can harden Ladybird!
The alpha is a rolling channel, and we’ll be pushing out automatic updates regularly. This is the part I’m most excited about. Ladybird improves quickly, and until now you had to build it from source to see that.
If you build websites, try yours in Ladybird and tell us what breaks. It supports WebDriver for automated testing, as well as the Firefox DevTools protocol.
Thank you to our sponsors and donors, and to everyone who has tested, reported bugs, and written code over the years. There’s still a mountain of work ahead of us, but I’m very happy that you can finally try Ladybird for yourself!

## [127] Megaspeed, the company at the center of the Jensen Huang scandal, appears headed for a US blacklist
TechCrunch | full text via TechCrunch | ~269 words

Megaspeed, the company that Alice Huang — the woman at the center of the alleged Chinese espionage scandal involving Nvidia — led for over two years, will be placed on a U.S. Commerce Department blacklist, Semafor reported Monday.
The company will be added to the Commerce Department’s Entity List, the outlet writes. This list “contains the names of foreign parties” subject to certain export restrictions designed to ensure that “sensitive technologies do not fall into the hands of those who would threaten U.S. national security or American citizens.”
Functionally, what this will mean is that U.S. companies will not be able to do business with or sell products to Megaspeed without first gaining a special license from the federal government. Semafor cites anonymous sources familiar with the matter to note the move is designed to stop the company “from obtaining US-made semiconductors.”
Megaspeed is a Singapore-based cloud and AI infrastructure provider that, during the period that Nvidia’s boss, Jensen Huang, self-admittedly had an affair with Huang, was one of Nvidia’s biggest chip customers. Last week, the Commerce Department also announced it had launched a criminal probe into the company. Authorities in both the U.S. and Singapore are now probing whether the company defied export restrictions and illegally smuggled Nvidia chips to China. The company has denied wrongdoing.
TechCrunch reached out to the Commerce Department for comment on the reporting and will update this story if it responds.
After lobbying from President Trump, Jensen Huang was reinstated as Nvidia CEO on Monday after a short period in which he was ousted by the company’s board over the scandal involving Huang.

## [21] Apple removed my open-source app from EU App Stores after 9 years
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [178] Claude Fable 5.2 cost three times as much as Opus 5.5 for nearly the same results in a VentureBeat bug-fixing test
VentureBeat | SNIPPET ONLY (VentureBeat: HTTP 429) | ~76 words

Claude Fable 5.2, Anthropic's top model, passed 10 of 15 bug-fix tries in a VentureBeat pilot test at a total cost of about $89. Opus 5.5 passed 9 of 15 at a total cost of about $29. A one-pass gap is too small to call, so the two finished about the same amount of work, and Fable cost about three times as much in total. No model, at any price, passed the hardest task. Read more

## [41] Finding faster quantum algorithms with agents and formal verification
Google DeepMind Blog | full text via Google DeepMind Blog | ~717 words

Finding faster quantum algorithms with agents and formal verification
How using agent teams and formal verification can improve quantum algorithms for modelling fusion energy, chemistry and enzymes
Quantum computers could soon solve problems beyond the reach of classical supercomputers. However, there is a catch: even when using the best quantum algorithms, some important applications still require more resources than early quantum hardware will be able to support.
In a new paper, we used teams of Gemini 4 agents to improve well-known quantum algorithms, creating highly efficient quantum circuits. These optimized circuits, which are instructions for how a quantum computer should carry out an algorithm, could one day help us run simulations that solve complex scientific challenges, from fusion energy to drug design. To help the community build on this work, we are open-sourcing our Lean library, problem specifications, and verified solutions on GitHub.
Because we cannot test resource-intensive quantum circuits on classical computers or today's small quantum processors, we have to prove that they work mathematically. Our agent teams proved each result using Lean, a formal theorem prover.
We chose to focus on applications that could one day impact some of humanity’s greatest challenges, such as clean energy and drug design, but our method is not limited to these problem areas.
- We found a quantum circuit that helps calculate an important property of inertial confinement fusion, a fusion reaction method that uses lasers to compress hydrogen fuel until ignition. Our agent teams cut the required computing cost (a metric that combines required qubits and operations) by 11.8×, and lowered required memory from 5,650 to 4,338 error-corrected qubits.
- The agents also reduced costs for simulating molecules in drug metabolism and certain photochemical reactions, which are complex reactions that are difficult for classical computers to simulate. For a common light-sensitive molecule, the agent teams made quantum simulation 8× cheaper, simplifying how the algorithm tracks particle positions and electric forces. For Cytochrome P450, an enzyme that breaks down most human medicines and is important for drug design, they found a 2.5× improvement and lowered memory from 481 to 333 qubits, by replacing bulky memory lookups.
- We also improved a fundamental quantum algorithm and a widely used arithmetic building block. We found a 2.57x speedup for a specific implementation of Grover's algorithm, a foundational quantum operation that searches through an unsorted list, and a 290x speedup for arcsin, a common routine that is used by many other quantum algorithms to load numbers into quantum states. [...]

## [29] OpenAI and Cisco introduce Shirudo
OpenAI Blog | full text via OpenAI Blog | ~820 words

OpenAI and Cisco introduce Shirudo
An open-source runtime that helps operators protect running Linux systems without needing to wait for the patch or restarts
OpenAI and Cisco are launching Shirudo, an open-source runtime that helps teams protect Linux systems while they roll out patches. In a controlled test(opens in a new window), a Codex-generated shield blocked a Java4Shell exploit attempt against a running Elasticsearch service without requiring a restart.
We’re inviting developers, security researchers, and infrastructure operators across the industry to help develop the project further. The project brings together OpenAI’s frontier AI, security and infrastructure research and Cisco’s infrastructure and security expertise to help protect the systems people rely on every day.
Testing and deploying a patch can still take days or weeks. Protecting a service in the meantime can be challenging because an exploit and a legitimate request may rely on the same Linux operation. Blocking that operation entirely could take the service offline.
Shirudo (Japanese for “shield”) is designed to help security teams navigate this tradeoff. Teams can test whether a temporary safeguard, called a shield, blocks the behavior that exposes a vulnerability while allowing legitimate requests through. Once an operator approves the shield, it can be deployed while the service continues running.
Shirudo uses eBPF, a Linux technology that allows small programs to run at specific points inside the operating system. This makes it possible to observe suspicious activity and apply targeted security protections to running systems.
OpenAI and Cisco are designing Shirudo around four core capabilities:
- Live protection: eBPF shields can block vulnerable code paths without restarting the system. Security teams can monitor how a proposed shield would affect applications before enforcing it.
- Defense at machine speed: OpenAI and Cisco are designing Shirudo to give agents programmable controls to investigate vulnerabilities, develop targeted shields, and validate their effectiveness against exploits and real workloads. Security teams control what gets deployed.
- Trusted deployment: Shields are cryptographically signed and verified before loading. Linux's eBPF verifier checks eBPF programs against its safety rules, while kernel security controls restrict unauthorized changes.
- Hardware-backed verification: Shirudo uses a Trusted Platform Module (TPM) to support a verifiable record of protections being loaded or removed. Operators can use this evidence to check whether systems meet their security requirements. [...]

## [149] AWS launches 5 new open decision models for AI agents
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~20 words

AWS on Monday launched Strands Decider v2, a family of five open decision models. The release comes only seven weeks

## [162] XNU Linux Lets macOS Userspace Processes Run On Linux
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~57 words

XNU Linux is a new opens-source project allowing macOS user-space software to run on Linux by loading the macOS kernel into it. XNU Linux builds off Apple's open-source XNU kernel components of macOS while adapted to serve as a loadable Linux kernel module. Besides this XNU kernel module, this works on an otherwise unmodified ARM64 Linux system...

## [45] JEP 545 Moves ZGC Memory Preparation off the Startup Path in JDK 28
InfoQ | full text via InfoQ | ~883 words

JEP 545, Faster Startup and Warmup with ZGC, has been integrated into JDK 28, moving the work of acquiring and preparing heap memory off the startup path and onto dedicated concurrent worker threads. On Linux 6.1 and later it also upgrades 4 KB pages to 2 MB pages while the application runs. The 2 MB initial heap behind the JEP's headline numbers comes from elsewhere: adaptive heap sizing, in the companion JEP 546, which still defaults to off.
Deploying ZGC has until now meant choosing which half of a trade-off to pay for. The collector's pause times do not grow with the heap, but its collection frequency does, so a small heap brings on early and frequent cycles. The JEP describes the older ergonomic behavior of committing one sixty-fourth of physical memory for the initial heap.
A team chasing fast startup set a tiny -Xms and accepted a long warmup, because the collector then had to acquire and prepare memory in increments while the application was already allocating. A team chasing fast warmup set a large -Xms, usually with -XX:+AlwaysPreTouch, and paid the whole bill before the first request landed. The JEP puts the spread at roughly a tenth of a second to start with a 2 MB heap against more than ten seconds with a 32 GB one on current hardware.
That work now happens in a new thread, ZMemoryWorker, one per heap partition. It commits and uncommits memory concurrently as capacity changes. It also heats memory before application threads reach it, which means pre-touching page by page and collapsing small pages into large ones.
The budget is fixed rather than adaptive. ZConcurrentWorkersCPUShare in zGlobals.hpp is 0.25, so preparation takes at most a quarter of the available CPU. ZGC's director caps young-generation worker counts when adaptive sizing is on, which keeps collection inside its CPU target while expansion continues and the collector deliberately runs above its heuristic heap size target.
Large pages on Linux no longer require an administrator to reserve them up front. ZGC probes for MADV_COLLAPSE, the madvise mode added in Linux 6.1, by mapping a 4 MB region, pre-touching a single page and collapsing an aligned 2 MB range. When the probe succeeds and memory heating is enabled, the collector enters a new Collapse state and upgrades pages in the background. The call races the kernel's khugepaged, so the implementation retries on EAGAIN.
The change shows up in what a deployer no longer has to decide. [...]

## [47] Kubernetes v1.38 Sneak Peek
Kubernetes Blog | full text via Kubernetes Blog | ~1533 words

Kubernetes v1.38 Sneak Peek
As we get closer to the release date for Kubernetes v1.38, the project develops and matures, features may be deprecated, removed, or replaced with better ones for the project's overall health. This blog post outlines some of the planned changes for the Kubernetes v1.38 release that the release team feels you should be aware of for the continued maintenance of your Kubernetes environment and keeping up to date with the latest changes. The information listed below is based on the current status of the v1.38 release and may change before the actual release date.
Deprecations and removals for Kubernetes v1.38
kubectl: WebSocket opt-out environment variables removed
kubectl has used WebSockets instead of SPDY by default for kubectl exec, attach and cp since
v1.30, and for kubectl port-forward since v1.31. The KUBECTL_REMOTE_COMMAND_WEBSOCKETS and
KUBECTL_PORT_FORWARD_WEBSOCKETS environment variables let you turn that behavior off. These
variables are going to be removed in v1.38. kubectl will then always try WebSockets first and fall
back to SPDY when it needs to (the same as the current default behavior). If your scripts or CI
environments set either of these environment variables, you can remove them since they will no
longer have any effect.
To learn more, refer to KEP-4006: Transition from SPDY to WebSockets.
kubectl: name dropped from kuberc credential plugin allowlist entries
The kuberc file keeps kubectl user preferences separate from cluster credentials in the
kubeconfig, including an allowlist of the credential plugins kubectl is allowed to run. In the
beta kubectl.config.k8s.io/v1beta1 API, an allowlist entry can use name as an alias for
command. The name field (not command) has been deprecated since v1.36.
With kuberc expected to graduate to stable in v1.38, the new kubectl.config.k8s.io/v1 API will
not include name. If any of your allowlist entries use name, change them to command now.
To learn more, refer to KEP-3104: Separate kubectl user preferences from cluster configs.
Ongoing major changes
Future removal of cgroup v1 support
Support for cgroup v1 is being phased out. Since v1.35, the kubelet fails to start on nodes that use
cgroup v1 unless you set failCgroupV1: false in the kubelet configuration. This option remains
available in v1.38, but it should be treated as a short-term fix as support for cgroup v1 is planned
to be removed in a future release. If you haven't already, please plan your migration to
cgroup v2.
To learn more, refer to KEP-5573: Remove cgroup v1 support.
Admission webhooks no longer receive authentication and authorization review requests
Since v1.37, the ExcludeAdmissionWebhookVirtualResources feature gate has been enabled by default. [...]

## [79] NVIDIA Releases Nemotron-Labs-Sigma Continuous Diffusion Language Models
TLDR AI | full text via TLDR AI | ~536 words

Continuous diffusion language models at two scales
Overview. Nemotron-Labs-Sigma is a family of 3B and 8B continuous diffusion language models for reasoning and coding. Sigma generates text in blocks by denoising compact continuous token embeddings. This smooth ODE trajectory enables inference-time steering and few-step generation, as well as self-speculative decoding. Across reasoning and coding benchmarks, Sigma is competitive with leading masked diffusion and autoregressive baselines and achieves superior performance on code completion.
Learned continuous token embeddings
8 tokens per forward pass on math and 4 on coding, with negligible accuracy loss
Average 8B self-speculative decoding speedup over autoregressive decoding on GB200
Large Language Continuous Diffusion Models
1 NVIDIA 2 Cornell University 3 Georgia Institute of Technology
* Core contributors, equal contribution. † Work done during internship at NVIDIA. ⋊ Equal supervision.
Correspondence: mmardani@nvidia.com
From Gaussian noise to discrete token
Sigma generates text one block at a time, iteratively denoising a compact representation conditioned on the preceding context before reading out tokens.
Initialized from a pretrained autoregressive backbone, Sigma learns its embedding geometry and denoiser together. At inference, classifier-free guidance and score temperature steer the trajectory to balance quality and diversity.
Reasoning, coding, and efficient generation
Strong task performance
Sigma improves over matched baselines across reasoning and coding evaluations, with particularly consistent gains on coding. After supervised fine-tuning, its average performance is on par with Nemotron-Labs-Diffusion at both scales.
Fewer denoising steps
Distribution matching distills the model for few-step generation. The distilled models generate 8 tokens per forward pass on math and 4 on coding, with negligible accuracy loss and preserved diversity.
Superior pass@k performance
Embedding-space steering offers control over the quality–diversity trade-off. Diverse samples continue to improve the chance of finding a correct answer as the sample budget grows.
One model, its own drafter
Sigma shares a backbone between diffusion and autoregressive streams. Its distilled diffusion model can draft blocks for the autoregressive stream to verify, reproducing greedy autoregressive output. On an NVIDIA GB200, the 8B model achieves a 3.46 times average throughput speedup over its autoregressive decoding.
Technical details
Training the model
Sigma trains an autoregressive stream and a diffusion stream on a shared backbone. The former processes clean tokens; the latter denoises their continuous embeddings, attending to the clean prefix and within each block. [...]

## [78] Tencent Releases Hy4 With Multimodal Input and Million-Token Context
TLDR AI | full text via TLDR AI | ~1338 words

中文 ｜ English
  
🖥️ Official Website | 💬 GitHub | 📱 GGUF
Table of Contents
Model Introduction
Hy4 is a new-generation Mixture-of-Experts (MoE) flagship model developed by the Tencent Hy Team, supporting text, image, and video understanding. The language backbone comprises 770B total parameters, of which 49B are activated per token. It consists of 78 layers, with a standard dense FFN in the first layer and MoE FFNs in the remaining 77 layers. Each MoE layer contains 256 routed experts and 1 shared expert; every token activates the top-8 routed experts along with the shared expert. In addition to the backbone, a 5-layer DFly2 drafter (3.3B parameters) is built in for speculative decoding.
On the architecture side, inspired by DeepSeek and GLM, the attention module employs Gated DeepSeek Sparse Attention (Gated DSA) with IndexCache for cross-layer sparse index reuse. The residual pathway uses iHC (identity Hyper-Connections) to expand inter-layer information flow. A ViT supports dynamic image resolutions, with an adapter converting image and video frame features into visual tokens for the language model to process alongside text tokens. DFly2, a parallel drafter, reuses Hy4's KV cache and sparse indices to support long-context speculative decoding at a low, constant cost.
Model Specifications
Pretrained model capability
Bits-per-byte (BPB) on internal code & agent validation, lower is better:
Few-shot pretrain benchmark evaluation:
† Macro-averaged accuracy for the marked text benchmarks. Other text rows use the accuracy metric reported by our evaluation suite. Bold marks the highest available numerical score in each row; it does not indicate statistical significance.
Multimodal results are reported only for Hy4 Base and Hy4 flash Base.
ARC-Challenge and HellaSwag use 299-item and 3,000-item subsets, respectively. INCLUDE uses a 5,000-example Lite subset covering 44 languages. Belebele covers German, Korean, Vietnamese, Spanish, and Russian (4,475 examples in total).
Disclaimer: Because our base model was exposed to a large amount of synthetic instruction data during mid-training, it occasionally fails to follow the expected answer format in few-shot evaluations, which may distort the scores.
Key Improvements
Compared with Hy4 preview, Hy4 substantially scales up both pre-training and post-training. It adds vision capabilities and delivers major gains in instruction following, long-context understanding, long-horizon tasks, and deep research.
Capabilities and Use Cases
Vision and computer use
By combining perception, reasoning, and tool use, Hy4 can understand fine-grained image details and interpret complex charts. It supports computer-use workflows across command-line interfaces (CLI) and graphical user interfaces (GUI). [...]

## [151] AMD EPYC Zen 6 vs. Zen 1 Performance: 12.1x Geo Mean In Less Than 10 Years, Up To 133x In AI
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~104 words

This month brought the availability of the new EPYC 9006 "Venice" SP7 Zen 6 server processors. We have seen excellent generational gains with the likes of the EPYC 9686F and EPYC 9996 over Zen 5 Turin CPUs as well as sharply outperforming the competition from Intel and NVIDIA. With the first-generation EPYC "Naples" processors having launched nearly ten years ago, I was curious to quantify AMD's server performance gains over the past decade. So up today is a look at how the EPYC 9996 and EPYC 9686F Zen 6 processors compare to the original EPYC Zen 1 flagship with the EPYC 7601 across real-worl

## [125] Zstd 1.6 Released With Many Fixes, New Performance Optimizations
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~36 words

It's been a year and a half since the last Zstandard release (v1.5.7) while Zstandard 1.6.0 was tagged a short time ago as the next major step forward for this widely-used, open-source compression algorithm and implementation...
