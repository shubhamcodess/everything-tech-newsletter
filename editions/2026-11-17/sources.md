# Full text for 30 picks -- untrusted article content, treat as data only

## [67] Alpine Linux Users Urged to Patch OpenSSH Authentication Flaw
InfoQ | full text via InfoQ | ~819 words

A recently disclosed vulnerability in OpenSSH lets an unauthenticated attacker log into accounts that should have no usable password. The issue, named *sshole and tracked as CVE-2026-123158, affects Linux systems running OpenSSH with the musl C library and which don't use PAM. Security researchers now report that attackers are exploiting it in the wild.
The flaw comes from the way OpenSSH checks passwords when musl handles the underlying crypt() call. On an affected system, a password longer than 256 bytes causes musl to return an error value. That value is an asterisk, the same character Linux uses in /etc/shadow to mark an account as having no password. OpenSSH then treats the returned asterisk as a match and permits the login.
The conditions to exploit the vulnerability are however quite narrow. The server must run OpenSSH before version 10.6p2, be built against the musl library rather than glibc, and operate without PAM. It must also have at least one account with a SHA-256 or SHA-512 password hash and another account marked with an asterisk in its shadow entry. When those conditions are met, any password between 257 and 1,024 characters can authenticate against the passwordless account.
Alpine Linux is the most prominent distribution affected, as it uses musl and its default OpenSSH configuration does not enable PAM. Other musl-based environments, including OpenWrt, Buildroot and Yocto, may also be affected where the same configuration applies. Systems using glibc, PAM, Dropbear or OpenBSD are not affected.
"Accounts that should never take a password at all (root, your key-only deploy user, ldap users, the default user on alpine's aws and azure images) take any password longer than 256 characters."
Ozgun Kultekin, *sshole
Ozgun Kultekin, a security researcher at Wakefield, published the technical explanation on the *sshole site. Kultekin traces the problem to two musl changes made in 2012: the first replaced the NULL error return from crypt() with an asterisk, and the second added a 256-byte limit to SHA-512 password hashing, so longer inputs caused an error. Together, the changes produced a value that could be mistaken for a password hash.
The OpenSSH side of the problem dates from a 2016 fix for CVE-2016-6210, which was a timing attack that could reveal whether a username existed. To make responses take a similar amount of time for valid and invalid users, OpenSSH borrowed the salt from another account and hashed the supplied password anyway. [...]

## [18] US moves to cut China’s remote access to AI chips
Ars Technica | full text via Ars Technica | ~1268 words

On the heels of the Nvidia scandal, the Trump administration is preparing to crack down on foreign data centers that are fueling China’s advancements in artificial intelligence by allowing remote access to otherwise restricted high-end chips necessary for AI training.
In a summary of the rule change, the Commerce Department said it was closing a loophole that previously allowed foreign rivals like China, Russia, and Iran to bypass export curbs on certain advanced computer chips by instead renting access to those chips from data centers in Indonesia, Malaysia, Singapore, Thailand, and Brazil.
US rivals could possibly use that access to train and run advanced AI models “capable of supporting military- and intelligence-related activities that could threaten US national security or foreign policy interests,” the Commerce Department said. Among threats, the US fears rivals could use advanced AI to develop “more effective weapons of mass destruction and advanced conventional weapons, coordinated cyber-espionage and targeted cyber-disruption, algorithmic theft, and weaponized disinformation.”
Now, the rules have been tightened up so much that the South China Morning Post reported that, “as a result, any advanced chips made for a Chinese firm are assumed to be restricted, and factories must ask the US government for a license before shipping them.”
The rule change takes effect 90 days after it’s posted to the Federal Register. Moving forward, companies headquartered in any of those countries deemed to “present a higher-than-normal risk of diversion” to China, Russia, and Iran must apply for a license with strict know-your-customer controls when transferring high volumes of advanced chips. If a license is granted, companies will have to “perform robust due diligence,” submitting monthly reports on transactions that thoroughly detail all parties involved, as well as their parent companies, and the final destination for chips sold. [...]

## [153] Google found hackers using autonomous AI agents to turn security patches into exploits
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~27 words

Google’s Threat Intelligence Group says attackers are using autonomous AI agents to reverse-engineer security patches, generate exploits, and attempt to The post Google found hackers using autono

## [1] Technical issue at JPMorgan Chase triggers online banking delays for US banks
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403; Slashdot: HTTP 403) | ~0 words



## [152] FBI Says Artex AI Open-Source Hacking Tool Used to Breach Networks In 'Under Three Hours'
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~90 words

The FBI is warning (PDF) that hackers are using the AI-powered penetration-testing tool Artex to compromise networks in "under three hours" in some cases. The tool has been linked to attacks against South Korean financial institutions, at least 2,250 ConnectWise customers and Barracuda. TechCrunch reports: Artex is one of several open-source AI-powered penetration testing platforms, a category of software built to probe a network's defenses. Hackers can connect Artex to hosted frontier large language models (LLMs) like those from Anthropic and OpenAI, as well as to open-source models and non-U

## [144] Cyber giant Infoblox confirms security incident after hackers access ‘company information’
TechCrunch | full text via TechCrunch | ~312 words

Cybersecurity and automation giant Infoblox has confirmed a cybersecurity incident, during which hackers accessed company information through one of its technology vendors.
Infoblox is a privately held cyber giant that provides companies cybersecurity and networking services, such as domain name resolution and identity and user access management.
In a statement, a spokesperson for Infoblox told TechCrunch that the company is “investigating a security event involving unauthorized access to certain company information through a compromised third-party data migration vendor.”
“We immediately activated our incident response procedures, took steps to contain the incident and are working with leading outside cybersecurity experts to investigate the facts, understand the scope and address any confirmed risks.”
TechCrunch has learned that the data breach involves a vendor that provides SharePoint data migration services, according to a notification sent by Infoblox about the breach, two people with knowledge of the incident told TechCrunch.
One of the people said sensitive customer data was taken in the breach.
According to public internet records seen by TechCrunch, Infoblox hosts much of its files, emails, and infrastructure with Microsoft, including a SharePoint server, which TechCrunch confirmed is accessible through Infoblox’s single sign-on provider. SharePoint is web-based software that companies use to share and host internal files and documents.
Infoblox has not named the third-party migration vendor that was hacked, but one person with knowledge of the incident said that Infoblox has terminated its work with the vendor.
The company’s spokesperson did not comment on this, but added that the company has “no indication that any Infoblox products, cloud services, software updates or build-and-release processes were involved” in the breach.
Infoblox would not say how many customers were affected by the incident, or if the company is aware at this time. The company also did not say, when asked, if it had been contacted by the hackers and if they had made any demands.

## [161] Uber says hackers stole information on close to 150,000 driver’s licenses during data breach
TechCrunch | full text via TechCrunch | ~468 words

Uber is notifying close to 150,000 drivers that their personal and driver’s license information was stolen during an October data breach at one of the company’s tech providers.
In notices filed this week with several U.S. attorneys general, including California and Iowa, the ride-hailing giant said it was notified on October 9 by the provider that hackers broke in and stole internal credentials, which were used to access Uber’s data.
The company said it subsequently began notifying affected drivers that their personal information was stored with the provider.
The stolen data includes affected drivers’ names, addresses, dates of birth, and driver’s license numbers.
TechCrunch has learned that the provider is Fireworks AI, which lets developers access and use open-weight AI models. Fireworks reported a data breach last month in which hackers stole its customers’ information, including billing data and some private AI datasets.
Online productivity startup Notion and AI coding startup Cursor have both confirmed that they had data stolen during the Fireworks hack.
In Uber’s case, the company said it had alerts enabled to detect unauthorized access to its Fireworks environment, but because the hackers used Fireworks’ own internal credentials, “no alerts were triggered.”
When reached for comment, an Uber spokesperson told TechCrunch: “The notices to drivers are in relation to a security incident impacting one of our third-party vendors, Fireworks.ai, which had access to some Uber data,” and deferred our questions to Fireworks.
A spokesperson for Fireworks confirmed that the company identified a security issue involving unauthorized access to some of its systems, which affected customer data, but the spokesperson did not address our questions about the incident.
Fireworks attributed its breach to a financially motivated cybercriminal group whose goals are to sell stolen tokens for accessing large language models, or LLMs. No known cybercriminal group has taken credit for the data theft.
In a notice filed with Oregon’s attorney general, Uber said it notified 149,346 people in total that their information had been taken in the breach at Fireworks.
TechCrunch previously reported that Uber has notified drivers in California, Illinois, Massachusetts, Rhode Island, and South Carolina. We’ve also seen data breach notices filed in Texas and Vermont. [...]

## [65] AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field
InfoQ | full text via InfoQ | ~820 words

AWS has launched Nitro Sandboxes, which run an opted-in Kubernetes pod, ECS task, or EC2 workload inside its own lightweight virtual machine with a separate guest kernel, carved out of a running EC2 instance by the Nitro hypervisor. On Amazon EKS, the whole change is one pod field: runtimeClassName: isolated-sandbox or confidential-sandbox.
The feature is available in all commercial regions at no additional charge, and AWS positions it for workloads where the tenant or the code cannot be trusted, with coding agents named first. In an AWS blog post, Carlos Santana and Trishi Mehta write:
Each pod gets its own operating system, completely separate from the host and from every neighbor.
According to the EKS documentation, a containerd-shim-nitro-sandbox-v2 process on the parent instance launches a Firecracker microVM as a first-level guest with hardware-assisted virtualization, after which an agent inside the VM runs the pod’s containers through its own containerd and the two sides communicate over virtio and vsock. The result is a sandbox that shares neither kernel nor memory mappings with the parent instance or any other sandbox, while the containers themselves start unchanged. How the nodes get there depends on the cluster type: on EKS Auto Mode the two RuntimeClasses ship with every cluster and sandbox-capable nodes are provisioned on demand, whereas on standard EKS a team builds a sandbox-enabled AMI for its node groups or Karpenter.
(Source: Amazon EKS User Guide)
What separates the two modes is which side of the boundary is trusted. Isolated mode trusts the parent instance and not the guest, which is why kubectl exec, logs, and process listing keep working, whereas confidential mode treats the parent as untrusted and moves enforcement inside the VM: a Cedar policy generated from the pod spec pins image digests, arguments, environment, mounts and capabilities, exec and stdin are denied, the Nitro Secure Module measures the image and policy into PCRs, and a KMS key policy can release secrets only to a sandbox whose measurements match. Image layers can be encrypted as well, so the parent moves ciphertext it never reads. [...]

## [24] Enabling the parallel frontend on nightly
Lobsters | full text via Lobsters | ~1258 words

TL;DR: We are enabling the parallel frontend of the Rust compiler on nightly by default, to find remaining issues in preparation for its stabilization.
Context
The Rust compiler has been using multiple threads to compile code in its "backend" part (using LLVM) for a long time. However, its "frontend" part (which includes type checking and borrow checking) has been executing sequentially, on a single thread, which of course limits the performance of the compiler. If you are interested in a more in-depth explanation of parallelism in the Rust compiler, see this previous post.
The compiler frontend actually had support for running in parallel for a long time, but it was not enabled by default due to various issues. Three years ago, we made it possible to opt into the parallel frontend on the nightly channel, with the plan to stabilize it in 2024. Clearly, we did not achieve that goal, but work on the parallel frontend was still slowly progressing in the meantime.
Last year, Vadim Petrochenkov, together with several other contributors, started a coordinated effort to finally get the parallel frontend over the finish line. Since then, many long-standing issues were fixed, and its performance was improved. Now we are at a point where we would like to make it widely available. But before that, we want to find out if people encounter issues with it in the wild, which is why we are enabling it by default only on the nightly channel. Once we will be confident enough that it is working well, we want to stabilize it.
The parallel frontend has been enabled on the nightly channel by default since nightly-2026-11-14.
Benefits
The primary benefit of enabling the parallel frontend is, of course, faster compilation of Rust programs.
We benchmarked the parallel frontend in our benchmark suite, which measures the duration to compile the leaf crate in a crate graph. As usual, the results were varied. In some benchmarks, the parallel frontend barely helped. In others, for example when performing a cargo check of the nalgebra, cargo or diesel crates, the compilation was almost three times faster, using 8 threads.
In the table below, you can find the aggregated wall-time mean change for the real-world benchmarks in our suite, when building a single crate from scratch across several configurations, compared to the same build using a sequential frontend. [...]

## [36] Scheduling the removal of the kube-proxy IPVS backend
Kubernetes Blog | full text via Kubernetes Blog | ~1503 words

Scheduling the removal of the kube-proxy IPVS backend
The ipvs backend for kube-proxy was an experiment in providing a
service proxy implementation with better performance than the
iptables backend. While it succeeded in that goal, the kernel IPVS
API has turned out to be a bad match for the Kubernetes Services API,
and the ipvs backend was never able to implement all of the edge
cases of Kubernetes Service functionality correctly.
In Kubernetes 1.29, the project introduced the nftables backend for
kube-proxy, which became GA in 1.33. Part of the plan behind adding
the nftables backend was the idea that it would eventually replace
both the iptables and ipvs backends. Because the ipvs backend in
particular is complex, not 100% feature complete, and architecturally
quite different from the other two backends (and thus more work to
maintain), Kubernetes SIG Network decided to officially deprecate it
as of Kubernetes 1.35. Although it currently remains available in
kube-proxy (with a warning about its deprecation), we (Kubernetes SIG
Network) now plan to remove it in Kubernetes 1.40. All ipvs users
should therefore be planning to migrate to either the nftables or
iptables backends.
Why was the ipvs backend written?
The ipvs backend was originally designed to fix two different kinds
of performance problems in the iptables backend:
- First, iptables had problems with data plane latency (the speed
at which clients could establish new connections to services),
because kube-proxy would write a separate iptables rule to match
each service IP, so every new connection would need to be matched
against a long series of rules that was O(n) in the number of
services in the cluster.
- Second, it had an even larger problem with control plane latency (the speed at which kube-proxy could process changes to services and endpoints and update the data plane rules), because kube-proxy would rewrite the entire iptables ruleset every time any service or endpoint changed. While the list of rules itself was only O(n) in the total number of endpoints, the amount of time, RAM, and CPU that it took to process the updated ruleset grew faster than that. In very large clusters, kube-proxy would use 100% of one CPU all the time just to process iptables updates. [...]

## [72] Migrating from GitHub to Codeberg
Lobsters | SNIPPET ONLY (Lobsters: HTTP 403) | ~0 words



## [42] TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient
Microsoft Research Blog | full text via Microsoft Research Blog | ~873 words

At a glance
- Developers use AI coding agents in the same codebases day after day, yet agents often start each session from scratch: rediscovering familiar facts, loading unused tools, and repeating unsuccessful approaches.
- TokenEconomizer is an open-source plugin that learns from an agent’s past sessions in a repository to reduce waste in future sessions, without modifying the agent or its underlying model.
- Across 277 real bug-fixing tasks, TokenEconomizer reduced costs by 18.4–30.9% across multiple AI coding agents. Costs fell in every repository tested, while task success rates remained broadly stable.
AI coding agents are increasingly helping developers fix bugs and build features largely on their own, but every interaction with their models consumes tokens. In each session, an agent sends instructions, tool descriptions, and session history to its model. Most efforts to reduce this cost focus on individual tasks. Yet developers return to the same repositories, giving agents an opportunity to learn from previous work. Without that learning, an agent may repeatedly rediscover how to run tests, load tools it never uses, or spend dozens of turns revisiting the same error.
In our paper, TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents, we ask a simple question: can experience in a repository help an agent solve future tasks more efficiently? TokenEconomizer, an open-source plugin from UC Berkeley, Microsoft Research, and Microsoft Security, turns completed sessions into guidance for subsequent ones. It reduces waste without changing the agent or its underlying model, so developers can use it alongside the coding agents they already rely on.
Where the tokens go
We first profiled Claude Code on 60 tasks from SWE-Bench, a benchmark of real bug fixes in open-source Python projects, running each repository’s tasks in sequence. Three kinds of waste recurred:
- Rediscovering the same facts. After a repository had accumulated at least five completed tasks, 30% of tool calls repeated an action from an earlier task in that repository. Only 7% matched an action in another repository’s history.
- Paying for unused tools. The agent received 23 tool descriptions on every turn, but 16 were never called.
- Getting stuck on failures. The 17% of tasks that failed accounted for 32% of the spending.
We also tested three popular open-source plugins, each built around a fixed cost-saving strategy. [...]

## [64] GitHub Rebuilds the Copilot App's Diff Surface to Open Million-Line Pull Requests Without Jank
InfoQ | full text via InfoQ | ~549 words

GitHub engineering has published a detailed account of how it rebuilt the diff surface in the GitHub Copilot app to open a pull request with 2,200 files, over a million changed lines and more than 400 inline review comments without turning the review into a waiting exercise.
The post, by Principal Design Engineer Alberto Gimeno, lands at a moment when AI coding agents are producing far more pull requests than reviewers can digest, and the bottleneck has moved from writing code to reading it.
At the heart of the rebuild is a decision to stop pretending a pull request is a single uniform list. Code rows have a known height at a known font size, so their geometry can be computed up front and never rebuilt. Comments do not. A markdown body wraps differently at different widths, <details> sections can be toggled in place, reply composers grow as a user types, and images change height when they load. Rather than force one variable-height virtualizer to absorb both, the team split the document into two independent domains:
total height = deterministic code height
 + Σ dynamic block effective heights
 + scroll padding
Dynamic blocks are keyed by identity (file, line, side) rather than pixel position, with a fingerprint tracking content, open state and measurement width. A single idle-gated measurement pass reads mounted blocks in one batch, scoped to roughly 2,400 pixels around the viewport, and corrections are anchored to whatever the reader is looking at so the surface never fights an active scroll.
Gimeno is open about an early mistake, the team's first instinct was one ResizeObserver per block writing heights back into the layout, a classic feedback loop whose cost grows with every mounted block. The shipped design keeps the observer but defaults it to flagging rather than writing, with a deliberate frame-synchronous exception when the user toggles a <details> or expands a reply composer, so the code below moves in the same frame.
The work builds on an April 2026 post from the main github.com files-changed team, who reported that unified-view diff lines previously rendered as roughly eight React components and ten DOM elements each, and cut both roughly in half. [...]

## [13] Hyperscale data centers use 2% of US electricity
Ars Technica | full text via Ars Technica | ~314 words

One flashpoint for the tech industry’s all-in push on large language models has been the sudden rush to turn investment money into hyperscale data centers. The rush hasn’t allowed anyone to plan how to supply the required electricity cleanly or with minimal impact on ratepayers. Instead, it has been difficult to even collect information on what’s being built.
A new study has tallied energy use and estimated emissions for hyperscalers operating in the United States between May 2024 and April 2025. They weren’t able to differentiate between AI compute and more traditional data services, but it provides a clear point of reference to track moving forward.
Finding the centers
The team started with a list of 675 facilities from a commercial database based on news reports, company statements, and satellite imagery. They dropped any that didn’t have a reported electrical capacity or that they couldn’t verify was a suitably large building with the expected cooling and electrical connection equipment. That reduced the list to 403 data centers with an average electrical capacity of about 40 megawatts.
In a way, that makes this a very conservative estimate, since 272 facilities believed to be large data centers were left out. But if you’re interested in AI data centers, specifically, it’s also true that some of the facilities included may not fall in that category.
That fact also introduces some uncertainty in the actual power usage of these data centers. Relying on other research, they use a range—some conventional data centers run at an average of about 48 percent of capacity, while AI training loads have been running higher, at around 70 percent.
Putting that together, the total power usage for the year by these 403 data centers was estimated at 68 to 99 terawatt-hours. That amounts to 1.5 to 2.2 percent of total US electricity use, on par with the total used by Wisconsin or Indiana.

## [135] Russian hackers target Romanian servers to steal NATO, EU emails
TechRadar | full text via TechRadar | ~623 words

Russian hackers target Romanian servers to steal NATO, EU emails
Turla hackers breached Romanian government email servers
- Cereal malware secretly searched Romanian government emails for NATO and EU connections
- ESET discovered previously undocumented software linked to Russia's Turla hacking group
- Hackers exploited Microsoft Exchange systems to conceal their email collection activities
Cyberespionage hackers allegedly linked to Russia infiltrated the Romanian government email servers, seeking correspondence involving NATO and European Union institutions.
The operation relied on previously unseen malicious software ESET researchers named Cereal, according to the cybersecurity company's published investigation.
Rather than sending stolen messages immediately to an outside server, the intruders exploited the victim's own email environment to conceal their activity.
A covert toolset searched institutional correspondence
ESET said the intrusion began on December 23, 2025, after investigators had identified the same software in Kazakhstan the previous month.
The malicious package contained several .NET components capable of receiving instructions, executing code in memory, and examining an infected organization's internal structure.
One module, called CerealBox, searched messages for addresses associated with NATO and European Union bodies, then applied filters to identify selected correspondence.
Emails containing Microsoft Word documents or PDF files were among those selected, after which the software packaged and encrypted copies for collection.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
This approach allowed the operators to obtain specific material without indiscriminately copying every message stored within the compromised organization's mail environment.
ESET described the software as unusual because its methods relied on detailed knowledge of Exchange systems and unconventional .NET execution techniques.
The researchers said the malicious code also used legitimate server functions, reducing the need for communications with infrastructure controlled directly by the attackers.
That arrangement could make detection more difficult because security teams might see activity occurring through systems their organizations already depend upon. [...]

## [124] California state AG sues OpenAI over rogue agent incidents
TechCrunch | full text via TechCrunch | ~523 words

OpenAI is facing a new lawsuit from the California Attorney General’s office, alleging that the company’s training practices and lax security pose an ongoing danger to the public.
At the center of the case is the July 2026 Hugging Face compromise, in which a pre-release model within OpenAI compromised both companies’ security systems to complete a training benchmark. In its official report on the incident, OpenAI called it “an outlier scenario involving a rare and unexpected confluence of events.”
The California lawsuit represents one of the first attempts by a government regulator to hold an AI lab legally accountable for a rogue agent incident, with significant implications for both OpenAI’s competitors and its clients.
The complaint centers on the Hugging Face incident, but also cites similar incidents involving RubyGems, DseWiki, the Wikimedia Foundation, and Australian government websites as evidence that the underlying behavior is ongoing.
The complaint also alleges that dozens of similar incidents have occurred without public disclosure.
“OpenAI has recently sent notices to dozens of additional third parties whose websites or internal systems have been infiltrated by OpenAI agents,” the complaint reads. “In some cases, OpenAI agents were able to access sensitive personally identifiable information, such as employee records containing names, birth dates, addresses, and more. The vast majority of these incidents have not been disclosed or discussed publicly by either OpenAI or by the affected third parties.”
The central allegation is that OpenAI’s ongoing testing practices constitute a public nuisance because the lack of safety controls present an ongoing risk to the public. A secondary claim alleges unfair competition stemming from the marketing of an unsafe product. If the lawsuit succeeds, OpenAI could face an injunction “to abate the ongoing public nuisance,” leaving broad discretion in the hands of the court.
It’s the first regulatory case targeting OpenAI specifically over rogue agent incidents, although public endangerment claims have been considered by other states. In June, the Florida attorney general sued the company over allegedly harmful effects on users, particularly children and teenagers. In August, the Alabama attorney general launched a probe into deceptive practices related to the breach, but no case has been filed. [...]

## [10] Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use
Hacker News | full text via Hacker News | ~1496 words

7 minutes
Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use
I recently asked AI to help me look through the latest Windows binaries for undocumented features and functionality. Among the leads it turned up, one list immediately caught my attention: coding agents such as codex.exe, claude.exe, copilot.exe, and cursor.exe, alongside familiar developer tools such as python.exe, dotnet.exe, gcc.exe, and code.exe.
Why would a Windows system DLL need a list of coding agents and developer tools?
The names were in MissionControlAggregator.dll. I asked the agent to follow the references and dig into what the DLL actually does. That led from a handful of string comparisons to a running Windows component that records which coding agents and developer tools have been used, saves that information locally, and reports it to Windows Diagnostics. And unless you have opted out of the “optional” diagnostic data (which is enabled by default), the data is uploaded to Microsoft.
I shared the initial finding on X. This post includes more details about the investigation behind it.
Following the names
Opening the DLL in Binary Ninja made the first lead easy to see. These were explicit executable names embedded in a Windows component:
Following the references showed that the names were used in comparisons. There are four CLI-agent slots checking copilot.exe, claude.exe, codex.exe, and agy.exe, with extensionless equivalents on the WSL route. Five desktop-agent slots check github.exe, claude.exe, codex.exe, cursor.exe, and antigravity.exe.
Here is one of the comparisons against codex.exe:
The compiler-generated C++ names are unwieldy, so I will call these functions executable-name matchers. For reference, one related matcher is std::_Func_impl_no_alloc<<lambda_340dfe7e962ab225b6ac33bc664bd54f>, bool, std::basic_string_view<wchar_t, std::char_traits<wchar_t>> const&, Microsoft::Diagnostics::MissionControlAggregator::Utils::AppType>::_Do_call. The screenshot shows another lambda instantiation performing the same kind of name comparison.
The feature guarding the new agent checks has a particularly direct name: CLICodingAgentUsage, feature ID 62580080.
And the list extends beyond AI agents. The same component checks for node.exe, python.exe, dotnet.exe, gcc.exe, clang.exe, gdb.exe, javac.exe, devenv.exe, and code.exe, among others. Those checks feed broader developer-tool categories. [...]

## [173] Dax Raad rebuilt his browser tool in Rust for $60. Then memory use fell 97%.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~39 words

OpenCode developer Dax Raad says he rebuilt the project’s browser automation tool in Rust for $60, replacing the parts of The post Dax Raad rebuilt his browser tool in Rust for $60. Then memory use fell 97%. appeared fir

## [120] PostgreSQL 19's pg_plan_advice turned a 28ms query into 264ms under load
Dev.to | full text via Dev.to | ~1632 words

A ten-client pgbench run against a plain indexed lookup averaged 28ms a query. The same run, with one SET command telling PostgreSQL to use a sequential scan instead of the index it already wanted, averaged 264ms. Nothing else changed: same table, same data, same hardware, same query.
That SET command is PostgreSQL 19's new pg_plan_advice, a contrib module that lets you hand the planner a hint string and watch it comply, or tell you exactly why it didn't. PostgreSQL 19 is still at RC2 as I write this, pulled from Docker Hub as postgres:19rc2 on 14 November. It isn't GA yet, so anything here could still shift before release.
I went looking for a case where the hint would help. I didn't find one. What I found instead was a precise, well-documented way to make a healthy query slow, and a feedback system that is more honest about its own limits than most planner-hint tools I've used in other databases.
The setup
I built two tables: 50,000 customers and 2,000,000 orders, with status skewed so that 0.5% of orders are 'refunded' and the rest are 'shipped'. An index on status makes the refunded lookup cheap. This is the kind of table every production database has one of.
CREATE INDEX idx_orders_status ON orders (status);
ANALYZE;
EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF)
SELECT c.region, count(*), sum(o.amount)
FROM orders o JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'refunded'
GROUP BY c.region;
The planner picked an index scan on orders feeding a hash join against a sequential scan of the small customers table. Three repeated runs: 24.8ms (cold), 16.5ms, 18.0ms. That's the baseline for everything below.
pg_plan_advice works in two halves. EXPLAIN (PLAN_ADVICE) tells you the advice string that would reproduce the plan you just got:
 Generated Plan Advice:
   JOIN_ORDER(o c)
   HASH_JOIN(c)
   SEQ_SCAN(c)
   INDEX_SCAN(o public.idx_orders_status)
   NO_GATHER(o c)
And SET pg_plan_advice.advice = '...' feeds a string back in, which the planner then tries to honour, with feedback on how well it managed.
Forcing the wrong plan
I took the advice vocabulary (SEQ_SCAN, INDEX_SCAN, HASH_JOIN, NESTED_LOOP_PLAIN, and a dozen others for merge joins, partitionwise plans, and parallel workers) and used it to force the one plan the planner had already rejected: a sequential scan on orders instead of the index scan.
Forcing just the scan method cost roughly as much as forcing the scan method and the join method together. [...]

## [94] Quark: our whole training stack, end to end, for $4,200
TLDR AI | full text via TLDR AI | ~1411 words

Quark: our whole training stack, end to end, for $4,200
Before we scale up, we wanted proof that every part of our stack works. Quark is that proof: a 165M-parameter model with 128K context that we took from raw data through pretraining, long-context training, reinforcement learning, evaluation and release for about $4,200 of compute. One version learned simple agentic tasks from reinforcement learning alone, and all four checkpoints are out today under Apache-2.0.
Before we spend serious money on a large model, we want to know that every part of our stack works: data, architecture, pretraining at scale, context extension, reinforcement learning, evaluation and release. Quark is that test, run end to end. It is a language model with about 165M parameters (140M without embeddings), and we took it through every stage, from the first data-generation job to the last reinforcement-learning step, for about $4,200 of compute, about 1,300 H100-hours. That total includes a discarded first design, failed attempts, data generation and every evaluation. Compute for this work was partly sponsored by lium.io.
It reads up to 128K tokens, it has the best benchmark average among open models of its size trained on similar token budgets, and one version learned to answer, think and call tools from reinforcement learning alone, with no supervised fine-tuning stage and no distillation. All four checkpoints are on Hugging Face today under Apache-2.0.
The technical report has the details: the architecture, the training stages, the full cost breakdown, every evaluation and its limits.
The stack, stage by stage
Architecture. Most of what a language model does is local, so most of Quark's 16 layers only look nearby. Twelve local layers combine attention over the last 256 tokens with a short convolution, and every fourth layer is global and attends to the whole context. Each attention after the first layer also reuses the first layer's values through a learned gate, the multi-head gated value residuals from our MGVR work. The design pays off at inference: only the four global layers keep a full key and value cache, so at 128K tokens the cache takes about 0.5 GiB in bf16, a quarter of the 2 GiB the same model would need with every layer global.
Pretraining. A warmup-stable-decay schedule on 500B tokens on a single 8×H100 node: a short warmup at 1K context, 470B tokens at 4K context with a constant learning rate, then a 28B-token anneal at 32K context. [...]

## [96] End-to-End 4-Bit AI Training
TLDR AI | full text via TLDR AI | ~3283 words

Training large language models involves calculating and storing a lot of numbers. Using fewer bits for each value reduces memory usage and allows GPUs to perform calculations faster. However, there is a tradeoff: fewer bits also mean fewer representable numbers, leading to more aggressive rounding. Lower-precision representations ultimately hurt accuracy by adding error to the calculations.
For example, suppose we want to store the number 3.2, but the nearest values our numerical format can represent are 3 and 4. Rounding to 3 introduces a quantization error of \(-0.2\), the difference between the actual value and the one that can be represented in the quantized format. A single error like this may seem small, but these errors accumulate over training as rounding happens repeatedly across layers and optimization steps, which can impair the learning process.
This is the central challenge of low-precision training: how can we benefit from faster arithmetic without introducing errors that interfere with learning?
We manage this tradeoff through our use of three key numerical formats during training: BF16, MXFP8, and NVFP4. Each format’s precision is fixed, but its speed depends on the hardware being used. We train on NVIDIA’s Grace Blackwell Ultra platform, the GB300, which is designed to optimize matrix multiplications with NVFP4. Notably, NVFP4 is stored with 3.6x fewer bits than BF16, but it runs up to 6x faster on GB300s.
The NVFP4 acceleration on GB300s is very useful in high-volume inference, where the tradeoff leans in favor of speed. But compared to BF16 and MXFP8, the format greatly increases quantization error. This error matters more at different stages of training, and the tradeoff must be considered for each one separately: forward and backward passes in pretraining and supervised fine-tuning (SFT), sampling and training in reinforcement learning (RL).
Speed matters most in high-volume steps: pretraining, which runs on trillions of tokens, and RL sampling, which generates tens of thousands of tokens in each rollout. Each sampled token also requires loading the model’s weights from global memory, the cost of which scales with the number of bits needed to store the weights.
The backward passes that update the weights average over many tokens in a batch, which dilutes the impact of randomly distributed rounding errors. [...]

## [186] AI finds zero-day flaws for just $4 now – even mediocre hackers can cash in
ZDNet | full text via ZDNet | ~766 words

ZDNET’s key takeaways
- As AI advances, so does its ability to find zero-day vulnerabilities.
- Only three of seven AI models found a privately reported Google V8 bug.
- Finding a zero-day now costs as little as $4. Can defenders keep up?
AI is getting better and cheaper – and that’s impacting cybersecurity
Every major AI developer is working at breakneck speed to improve model effectiveness. At the same time, token prices continue to fall, with studies showing that the average cost of tokens, which varies by domain, has dropped by about 47% per quarter since 2023 and 15% last month alone, due to intense competition among companies including OpenAI and Anthropic.
This is good news for businesses trying to harness AI for productivity and new services, but as token prices fall, it has also become cheaper for attackers to launch AI-assisted attacks, including software breaches caused by exploiting unknown vulnerabilities.
More from ZDNET
Also: How AI security failures are endangering your supply chain
A report published by Xint.io examines how popular AI models have evolved over the past year to the point where cybersecurity tasks that would have failed only months ago now succeed. The team analyzed seven models launched since February 2026: two from OpenAI, three from Anthropic, and two open-source models from DeepSeek and Z.ai. The team tracked, over time, how they performed in finding a target vulnerability.
The $4 breakthrough: How AI’s hacking capabilities changed in 2026
The target of this research was a security flaw in Google’s V8 engine. Tracked as CVE-2026-102321, the type confusion bug leading to remote code execution (RCE) was disclosed to the Google Vulnerability Reward Program (VRP) by Xint researcher Taisic Yun and so was not present in the AI models’ training datasets.
The research scope was limited to a set of source files, including the file containing the vulnerability, and each model was instructed to search for security issues within these files.
Xint’s first test was conducted in February. After 25 hours and $350 of scanning, the best models then available still couldn’t find the critical vulnerability.
In July, GPT 5.6 Sol found the zero-day flaw for $22 in 44 minutes.
Also: Finding Linux bugs is easy – fixing them is another story
By September, GPT 6 Sol discovered the bug in 13 minutes for only $4.24 with its first guided prompt. [...]

## [154] Apple reveals new Mac security controls as AI agents raise privacy risks
TechCrunch | full text via TechCrunch | ~572 words

As promised last month, Apple on Monday announced changes to Mac security controls designed to protect users’ data from the growing popularity of AI agents and their apps’ demand for “full disk access.”
“Before granting an app such extraordinary access, users should understand that it puts all of the data on their Mac at risk,” Apple warned in its blog post aimed at app developers.
Unlike AI chatbots that simply answer questions, agents run on a user’s device where they can take actions across the operating system, files, and apps on the user’s behalf.
While the tools can be useful, Apple has grown concerned about the increased risks to users’ data and privacy that these AI agents introduce. At the same time, the company has been benefiting from sales of Mac minis and Mac Studio computers that AI early adopters have been purchasing specifically to run their local AI models.
To balance these competing interests, Apple said in October that it would revise some of its security settings around Mac apps. The announcement followed two notable incidents involving AI agents. In one, a journalist claimed that Meta’s Muse app read their private messages without consent; a separate report from Wired cited a flaw in ChatGPT’s Mac app that could have allowed hackers to access sensitive data.
Now, Apple is sharing the changes it’s making.
For starters, it’s splitting up Device Control and Data Access into two settings: System & App Protection Override and Accessibility. The changes are designed to help users better understand that selecting the first option means overriding built-in security protections.
To streamline configurations, Apple says there will now also be a single method for granting permissions that involves selecting the requested app from a list. The company will also introduce new guidance encouraging users to grant access only to the specific apps that need it when they enable the System & App Protection Override setting. Similar guidance will appear when users enable Full Disk Access to allow an app to access their folders.
The company will also provide users with “increased visibility into the wide range of data apps will receive access to or control over if full permissions are granted,” the blog post notes.
Another change will give users more granular control over when an AI agent or app can gain access by allowing users to configure their apps to ask for permission every time access is needed. [...]

## [5] Carnegie Mellon is putting computer science courses on YouTube for free
Hacker News | full text via Hacker News | ~196 words

Free lectures now on YouTube. Free courseware coming next.
Watch our faculty teach across AI, robotics, systems, biology, and more, from seven departments that lead their fields.
10-605
William Cohen
15-110
Franceska Xhakaj
17-214
Hammad Ahmad
15-442
Tianqi Chen and Zhihao Jia
17-635
Swarnalatha Ashok and Scott Pavetti
17-643
Jeffrey Gennari and Christopher Timperley
11-768
Daniel Fried and Graham Neubig
17-645
Christian Kästner and Bogdan Vasilescu
15-259
Mor Harchol-Balter, Weina Wang and Feras Saad
11-777
Louis-Philippe Morency
17-619
Jim Berardone
07-280
Nihar Shah
17-627
Scott Pavetti
More courses
Subscribe on YouTube to catch every new course.
1Premieres in November
Full classroom lectures from Carnegie Mellon faculty, free to watch.
2Next
Lessons built from real CMU courses. Get instant feedback and earn a badge.
3Coming to courseware
AI tutoring is coming to the courseware experience to help you work through questions and get unstuck.
Our faculty lead labs in AI, robotics, systems, and more.
Go deeper with graded work and an official credential through CMU Online.
Bring Carnegie Mellon computer science to your team with SCS Executive Education.
Join the Kenneth C. Griffin School of Computer Science as a full-time student at Carnegie Mellon University in Pittsburgh.

## [177] AO3 Is Back. This Is Not a Drill
Wired | full text via Wired | ~394 words

Dust off that Hitachi and put your Slack on “Do not disturb,” because AO3 is back online, baby.
After weeks off the internet due to an unspecified security incident, the Organization for Transformative Works (OTW), the nonprofit that runs the hugely popular fan fiction forum, announced on November 15 that service had been restored.
“We understand that the wait and uncertainty surrounding AO3’s return have been difficult, and we apologize for the inconvenience,” the statement reads. “We greatly appreciate your support during the downtime, and continued patience as our volunteers work hard to return AO3 to its full functionality.”
The news came as a pleasant surprise to AO3’s devoted fans, as the website had announced in late October that restoring service could take between two to four weeks. To that end, the OTW statement says that some of the site’s features, such as user icons and external work importing, have been temporarily disabled in order to expedite the site’s return. It also warned that users “may experience a delay before AO3 loads,” due to “high traffic.”
Founded in 2007, AO3 is one of the most popular fan fiction forums on the internet, boasting more than 11 million users and over 18 million original works. Following its temporary shutdown, many devastated fans started sharing Google Docs of their favorite fanfics, sparking some concerns among authors worried about AI scraping and their work being posted to other websites without their permission. Others resorted to other platforms to get their Dramione or Hollanov fix, such as Tumblr, which reported a 75 percent jump in new sign-ups among users between the ages of 18 and 25, according to data shared with WIRED.
Throughout the 17-day shutdown, AO3 has remained vague about the causes of the security breach. In its statement announcing its return, OTW said that while it has “no reason to believe that the user database was compromised,” it can’t rule out the possibility; the website recommends users change their passwords “as a precaution.” The site is also pairing with a security firm “to help prevent future incidents.”
Though the suggestion prompted some concern on social media, for the most part fans are jubilant about the end of the “AO3 apocalypse,” as some have referred to the shutdown.
“Ao3 returned on a Sunday,” one fan wrote in a tweet that has 1.2 million views. “Just like Jesus.”

## [99] Qwen4-Max: Your New Teammate Has Arrived
TLDR AI | SNIPPET ONLY (TLDR AI: no readable article text (paywall, bot check, or not an article)) | ~87 words

Qwen4-Max can take on a wide range of creative and professional work in the fields of 3D modeling, game development, precision manufacturing, finance, law, healthcare, and frontier scientific discovery. It demonstrates strong 3D creation capabilities and can use Blender to carry out geometry modeling, scene assembly, material setup, lighting, and rendering. The model works fluently with leading game engines and can handle scene construction, gameplay logic, integration of external assets, material setup, HUD design, and visual effects, and deliver a playable game. Smaller models in the family

## [162] Trump says ex-Nvidia CEO Jensen Huang’s affair with an alleged Chinese spy did not threaten national security
TechCrunch | full text via TechCrunch | ~371 words

U.S. President Donald Trump told reporters on Monday that he does not believe the country’s national security was put at risk as a result of former Nvidia CEO Jensen Huang’s affair with an alleged Chinese spy.
“It was not put at risk,” Trump said when asked by reporters in light of his own friendship with Huang. “Our country is now stronger than ever before. And you know, China plays games with us, and we play games with China.”
Trump went on to contradict previous findings from U.S. officials by doubting that Huang’s paramour, former Megaspeed executive Alice Huang, is a Chinese spy.
“He probably shouldn’t have been doing on a personal basis what he did … That’s a different story,” Trump added. “But nobody’s proven that she’s a spy. She may not be a spy.”
Last year, U.S. Secretary of State Marco Rubio reportedly oversaw the production of an internal memo, circulated among top policymakers, which warned that Alice Huang was a spy for China’s Ministry of State Security. Trump was reportedly briefed about these intelligence findings at least twice, including once in May aboard Air Force One, shortly before the former Nvidia CEO joined him on a trip to China. But Trump has maintained that he was not aware of these claims.
The U.S. regulates the exports of Nvidia’s top chips to China as a way of maintaining a competitive advantage. But prior to news of Huang’s affair publicly emerging, both the U.S. and Singaporean governments had been investigating Megaspeed for illegally smuggling Nvidia chips into China. Huang has since stepped down from the role he has had for 33 years at Nvidia after more reporting revealed that he also had affairs with two Nvidia employees, at least one of whom was a direct report.
Given Huang’s importance to Nvidia, some prominent figures in the industry — including Elon Musk, Y Combinator president and CEO Garry Tan, and Epic Games CEO Tim Sweeney — have signed a public letter calling for Nvidia to reinstate Huang.
“A lot of people are asking Jensen — they think Jensen should go back. That certainly isn’t a bad idea,” Trump said. Referring to the former Apple chief executive, Trump added: “I recommended Tim Cook.”

## [196] Local LLMs Handle Textbook RAG but Fail on New Research Papers
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~28 words

Five setups, one blind grading pack: textbook scores ran 12 to 20 of 20, but a paper published this year dropped them to 0 to 9 of 15.

## [8] Jiff 1.0: A datetime library for Rust
Hacker News | full text via Hacker News | ~8424 words

Jiff is a datetime library for Rust that encourages you to jump into the pit of success. Jiff automatically handles many common problems related to daylight saving time by putting time zone handling front and center into the API. Jiff has already seen widespread adoption in the Rust ecosystem.
Jiff is pronounced like “gif” with a soft “g,” as in “gem.”
This blog announces the Jiff 1.0 release by giving a tour of its API.
Target audience: Rust programmers who need convenient datetime handling.
Table of Contents
The Jiff 1.0 Commitment
Jiff is already used in production in many projects: uv, Cargo, Starship, fd, Nushell, mise, Jujutsu, uutils/coreutils and even as the basis for a Temporal implementation in AWS LLRT. It is time to call it 1.0.
Unless some significant defect is found in Jiff’s API, my plan is to commit to Jiff 1.0 indefinitely. This is important because the intent is for Jiff to be an ecosystem building block that appears in the public API of other libraries. This makes Jiff an attractive public dependency, which means semver incompatible releases are likely to cause significant pain in the ecosystem. They will not be made lightly.
To see a list of breaking changes between Jiff 0.2 and Jiff 1.0, please consult the CHANGELOG.
Introduction
In programming, a datetime library’s core functionality rests at the intersection of a computer system’s concept of time and a human’s concept of time. The prevailing notion of system time is Unix time. A human’s concept of time is far more complex, but the most popular such model is the Gregorian calendar coupled with either a 12-hour or 24-hour clock. At the core of every datetime library rests some routine for converting between these concepts.
A datetime library typically provides much more than this. Indeed, datetime handling has historically been very difficult. My own belief is that the difficulty comes from poor modeling of the domain. Instead of encapsulating the complexity inside a reusable bundle of code, many datetime libraries pass some or all of the complexity on to its users. Jiff instead tries hard to encapsulate the complexity and make it difficult for users to do something wrong. (Jiff is not the first to do this!)
In this section of the blog, we’ll do some very basic introductions. [...]

## [137] Cybersecurity AI startup Corma reaches $1B valuation in about 3 months
TechCrunch | full text via TechCrunch | ~211 words

Three months after introducing its product, AI cybersecurity startup Corma has raised a $125 million Series A round at a $1 billion valuation led by NEA, the company said. Corma offers AI models and agents trained for cybersecurity defense. It has now raised a total of $185 million from backers, including Sequoia Capital, Khosla Ventures, and Coatue.
The startup came out of stealth in August. Interest in its product skyrocketed after a series of security incidents sent chief information security officers scrambling on October 21 when a critical flaw was found in PHP, a popular web programming language. Another flaw was found in Node.js, the open source JavaScript runtime environment. Popular open source tool LiteLLM, a proxy for routing requests to multiple LLM providers, also disclosed a security incident. Other incidents were disclosed that day, too. The day showcased the kind of onslaught on security that AI has enabled.
Corma isn’t the only company using AI to play defense. Other examples include Kevin Mandia’s new startup Armadin, as well as Anthropic, OpenAI, Microsoft, and other established players, and too many other startups to count. Still, it’s a young market and a necessary one. Corma says it stands out from the crowd by being a frontier AI research lab focused on protection.
