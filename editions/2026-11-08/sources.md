# Full text for 30 picks -- untrusted article content, treat as data only

## [103] Why a new report on Anthropic automating AI development is alarming researchers
The Verge | full text via The Verge | ~2098 words

Anthropic is using AI to build more powerful AI. And it appears to be working remarkably well, with the company’s models improving roughly twice as quickly as a year ago, with little indication of slowing down.
Why a new report on Anthropic automating AI development is alarming researchers
AI is dramatically speeding up Anthropic’s research, even as the company calls for slowing down AI development.
That’s according to a new report published Thursday by the AI safety research organization METR, following an 11-week investigation inside the company, as part of a report evaluating its AI research and development. The probe is separate from a program offering safety researchers “employee-like” access to systems in the wake of high-profile hacking incidents over the summer.
The findings offer some of the clearest evidence yet of AI accelerating its own development, raising questions about how quickly the technology could advance toward a future in which AI systems can improve themselves with little or no human involvement. They also come at a pivotal time for Anthropic, which is preparing to go public even as its CEO, Dario Amodei, has publicly called for labs to pump the brakes on AI development.
But while the report offers a rare glimpse into the inner workings of the world’s leading AI labs, what it leaves out is just as revealing. Anthropic was permitted to redact portions of the final report as part of its agreement with METR, and it appears to have exercised that power liberally, raising questions about how much the public really knows about the pace — and risks — of frontier AI development.
Here are some of the biggest takeaways.
AI is dramatically accelerating Anthropic’s research and development
One of METR’s most noteworthy findings is that Anthropic’s AI models are improving roughly twice as quickly as they were a year ago, with benchmark scores suggesting “that Anthropic has made roughly two years of historical progress over the last year.” Crucially, METR’s researchers said they “are confident” that the acceleration was not simply due to scaling up the computing power used to train the models, which historically has been a major driver of AI progress.
Instead, the researchers said that the majority of the acceleration as of October “is due to AI,” with its contribution growing over time. That finding was supported by informal Slack polls and interviews with Anthropic employees, which pointed to sizable productivity gains. [...]

## [139] Kubernetes, mark II? Why Google’s giving away gVisor, a code sandbox used by Anthropic and OpenAI
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~30 words

Google wants to emulate one of its biggest ever open-source success stories, donating three core AI agent infrastructure projects to The post Kubernetes, mark II? Why Google’s giving away gViso

## [116] Microsoft's Azure Linux 3.0.2022 Ships With More Than 470 Security Fixes
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~49 words

Microsoft released Azure Linux 3.0.2022 on Friday night as the newest version of their in-house Linux distribution. Given the rampant AI/LLM-fueled bug reporting and security research, Azure Linux 3.0.2022 ends up incorporating more than 470 security fixes for different CVEs across the many open-source projects making up Azure Linux...

## [4] The end of Microsoft Research's AI Frontiers group
Hacker News | full text via Hacker News | ~915 words

In 2023 after the ChatGPT release, it was clear to me that research needed to be more organized to succeed than was typical within Microsoft Research. The amount of support and focus which other research groups were applying was great enough that even with a clever idea pursued by one person it was likely to arrive late and unconvincing because one person could not move fast enough and the baselines which one person could assemble just were not strong enough to really show that an idea was worth taking flight. Several other folks thought similarly and we organized to create the AI Frontiers sub-organization within MSR.
In AI Frontiers, we actively tried to organize coherent research efforts. This was not precisely “top down” or “bottom up”, but rather mostly somewhere in the messy middle. There were disagreements of course, and resolving them was sometimes quite challenging. Compute availability was also an often-severe bottleneck. But at a high level I was under the general impression that the organization was succeeding in doing pioneering things, particularly given the small size of AIF (~50 people) and relative to what we could do previously. Much of the work of AIF was figuring out how to make agents work, for example the Autogen orchestration framework and the Fara computer use agent. In NYC however, several of us were interested in developing new fundamental capabilities such as the Next Latent objective which enables extrapolation, Dion3 which creates an optimized/improved Muon, or the Full Bandwidth Transformer which efficiently makes models function substantially more powerfully via recursion.
We also actively tried to share with the rest of MSR. For example, AIF decided to develop a monorepo that was shared by default with all of Microsoft Research. In this monorepo for example was the proven-capable edge scale pretraining codebase I talked about in the COLM keynote last month. This might seem like a minor detail, but the amount effort required to create a well-formed model creation pipeline is substantial and I’m aware of at least 4 efforts (the other 3 not in public-within-MSR repos) trying to develop model building pipelines.
In early September we were reorged into Microsoft AI. On the surface this could make sense, because putting two different AI organizations together creates opportunities for better concentration of effort, and there were places where AIF was ahead of MAI and of course vice-versa (MAI is much larger). [...]

## [5] Every Mac comes with an (undocumented) family member classifier
Hacker News | full text via Hacker News | ~2831 words

What if I told you that every Mac since 2022 ships a pair of daemons whose only purpose in life is to build a graph about you and the people around you: who you are, who you know, how those people are related to you and to each other, how you communicate with them, where you go, with whom, what you do and when. This graph is built on device by cross-referencing pretty much everything on the machine: Contacts, Calendar, Photos, Messages, Mail, location, Screen Time and a long tail of behavioral signals. And, more importantly, it is held as a queryable store that LLMs retrieve from (allegedly). Would you believe me?
Well, that's what is happening, and interestingly enough, there is little documentation of how this whole mechanism works on your Mac. The closest thing to an official description is the man page (man 8 knowledgeconstructiond), and this is all you get:
Previous work: To be fair, Apple's own researchers did publish a paper on the techniques behind this graph construction, back in 2023. But there is next to nothing on how it is integrated into macOS: which versions run it, and the exact list of what is collected and inferred. And not a word about the "kinship" inference discussed below. Also, we personally ran into it while doing some security research on the Apple Intelligence bundle in macOS 26 in August 2026; but a few months before, Nic Lydon came across the same database and wrote it up in I Built a Personal Knowledge Graph. Apple Had Already Built One on My Laptop. And even more recently, a forensics tool went looking on the phone: in September 2026, Alexis Brignoni taught iLEAPP to read the same store on iOS, where graph.db and the ontology.db that decodes its predicate codes sit under /private/var/mobile/Library/IntelligencePlatform; he writes it up in Reading the iPhone Knowledge Graph, and Checking Its Work.
But we go a bit deeper.
This blog post is an account of some analysis work we carried out on what the knowledge graph actually does, so that you (the user) can get a better understanding of how this mechanism works, and some clarity on what the graph holds about you and your family and friends. Everything in it was collected on macOS 26 (26.6.2 at the time of writing).
To this end, we open-source a local dashboard (iKnow) you can use to read the content of your personal knowledge graph on your Mac.
Finally, we derail a bit and look into what we do best: weaponizing and exploiting. [...]

## [48] Partnering with Hacktron to find vulnerabilities in OpenAI’s systems
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~19 words

OpenAI is partnering with Hacktron to find vulnerabilities, test connections with third-party services, and strengthen defenses with frontier AI.

## [104] The Fridge-Hacking Spree Is an Internet-of-Things Wake-Up Call
Wired | full text via Wired | ~689 words

Welcome to Kernel Panic, a weekly newsletter by Lily Hay Newman and Matt Burgess from inside the new world of privacy and digital security. To receive this newsletter in your inbox each week, sign up here.
Amid an onslaught of AI vulnerability discovery and AI-assisted hacking, some of the most consequential critical infrastructure attacks this year may have little to do with the technology at all—instead providing a stark reminder that cybersecurity fundamentals are still key to digital defense.
Three sites in France that handle blood and plasma bags were briefly impacted this week by widespread attacks on vulnerable internet-connected refrigerators. On Wednesday, the Établissement Français du Sang (EFS) confirmed that cold rooms storing blood were “raised to very high temperatures” on November 2. The blood samples, thankfully, weren’t altered or damaged, the EFS said, because the organization’s alarm facilities and staff quickly detected the changes and implemented fail-safe measures.
The incident, however, comes amid a wave of cyberattacks in recent days affecting supermarket chains in at least 11 European countries that also drastically increased the temperatures of their refrigerators. Pictures from across the continent show huge volumes of food being trashed following the spikes. Similar fridge attacks in October affected hundreds of French stores that were forced to throw away food. And in August, roughly six commissaries and grocery stores on United States military bases suffered similar incidents resulting in spoiled food. The Pentagon is investigating the incidents and is collaborating with French law enforcement, Reuters reported last week.
“It's been true for more than a decade now that our dependence on connected technology is growing faster than our collective will to protect it, which has exposed us to accidents, adversaries, and now potentially agents,” says longtime critical infrastructure researcher Josh Corman, who is currently the executive in residence for public safety and resilience at the nonprofit Institute for Security and Technology. “These fragile cold-chain systems are too critical to fail, but we keep experiencing hard lessons.”
It is still unclear who is behind the incidents and whether the attacks are all connected or being carried out by multiple actors. [...]

## [95] The US let Nvidia sell chips to an empty office in China
The Verge | full text via The Verge | ~289 words

Concerns are being raised that neither the Commerce Department nor Nvidia are doing their due diligence when it comes to vetting Chinese firms cleared to handle the company’s H200 AI chips. According to The New York Times, New Matrix is on the list of approved firms, yet its offices are empty, “a hollow gray shell with wires dangling from the ceiling where lights should be.” In fact, the paper could find little evidence that the company exists in any meaningful way:
The US let Nvidia sell chips to an empty office in China
The government is approving sales of Nvidia’s AI chips to Chinese firms with ties to blacklisted companies.
Only scant information can be found online about New Matrix, which was created 17 months ago. At the building that New Matrix lists as its address, a company directory does not include the firm. At the nearby property management agency for the industrial park, a receptionist and a manager both said they had no record of the company.
What little information can be found about New Matrix is concerning. Its owners have ties to a Chinese private equity firm that has been blacklisted by the US government since 2024. And according to the Times, this is not a rare lapse in oversight, but a troubling pattern of companies connected to entities with national-security-related trade restrictions being approved to purchase Nvidia chips.
Nvidia had been restricted from selling chips to China during the Biden presidency. But the Trump administration relaxed those limits after Nvidia agreed to give the government a 15-percent cut of all sales. The company’s CEO, Jensen Huang, also launched an intense lobbying campaign and was apparently targeted by China’s Ministry of State Security in a spying plot.

## [1] Asahi Linux Progress Linux 7.3
Hacker News | full text via Hacker News | ~3105 words

Progress Report: Linux 7.3
Well here we are again. Linux 7.3 is out and it’s been an eventful few months, so let’s get stuck in to another Asahi Linux progress report!
Upstreaming continues
As always, upstreaming work continues to progress. Aside from the usual patches for low-level SoC blocks, two major drivers made it on to the list this cycle: macaudio and avd. Getting macaudio ready for submission has been a challenge. The audio subsystem on Apple Silicon devices is rather special, and required quite a number of core ALSA changes to properly support it. Apple also uses special variants of speaker and headset amplifiers that were already supported upstream, and these drivers also needed some pretty significant modifications. We have previously discussed a lot of this work at length, and we are finally in a position where we can submit the main driver for review. The driver and Devicetree changes represent a hefty chunk of our total patchset, about 3100 lines.
AVD is a whole different beast. The AVD driver has spent barely 3 months in our downstream tree and is already on the list. This is our shortest turnaround time yet for a major SoC component and bodes well for a transition to upstream-first development some time in the future. This is fantastic news, as the AVD driver and related Devicetree changes are around 13000 lines of code.
Also making an appearance on the list this cycle are initial Devicetrees not only for M4 Pro and Max devices but also M5 thanks to Yureka’s tireless efforts. As usual these initial Devicetrees are barebones and only sufficient to boot the SoC to a TTY, however work is progressing on further enablement. Watch this space!
We have also begun shifting to an upstream-first approach where practical. Changes to the TI USB-PD and SPMI drivers required for new devices, as well as initial support for Thunderbolt, were all developed upstream-first. We are so thrilled to see our focus on upstreaming starting to pay off!
M3 goes GA
Last time, we announced initial support for M3 series machines via the EXPERT flag on the Asahi installer. We are pleased to announce that we received almost no issues from early adopters, so M3 support is now generally available without the EXPERT flag!
We have also made a number of improvements to M3 support, most notably enabling DCP. On top of performance and battery life improvements, this also allows us to enable sleep on M3 series devices and make the area around the notch useable on the MacBooks! [...]

## [128] Cognition turned an open model into a coding beast. But it won’t release the weights.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~38 words

Cognition built its newest coding model on a foundation that anyone can download, yet the company is keeping its own The post Cognition turned an open model into a coding beast. But it won’t release the weights. app

## [135] “Most apps never make it off localhost”: Cursor takes on Lovable and Replit with fully managed app deployment
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~26 words

AI coding agents have certainly made it easier to transform an idea into a working application. However, getting that application The post “Most apps never make

## [89] How we review 4x more AI code without reading every line
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~30 words

Do you need to read every line of AI-generated code to trust it? Not necessarily. Instead, check five things: the The post How we review 4x more AI code without

## [123] Alpine Linux and OpenSSH patch flaw that’s as bad as it can get
ZDNet | full text via ZDNet | ~930 words

ZDNET’s key takeaways
- An ancient bug is affecting Alpine Linux and a few other Linux distros.
- It’s about as bad as it can get.
- You must patch ASAP, and then restart the patched software.
The perfect nightmare scenario for a Linux server is when all an attacker needs to do is reach the server’s Secure Shell (SSH) port, waltz right in, and take it over. That’s what happened to Alpine Linux, the popular, lightweight Linux server. Adding insult to injury, this happened only days after Alpine Linux dodged a security hole-sized bullet to its GitLab implementation.
Also: Linux Mint 27 arrives next month, and I like it already: What to expect
How the attack works
As security engineer Gregory Bryant explained in his LinkedIn post:
Most authentication bypasses come from complex logic chains, but yesterday’s Alpine Linux OpenSSH vulnerability (CVE-2026-123158) comes down to a single character: *.”
If you run Alpine Linux (or another musl-based distro) with the default openssh-server package (no Pluggable Authentication Modules (PAM)) and PasswordAuthentication enabled, an attacker can log into password-disabled, or key-only accounts simply by sending a password between 257 and 1024 bytes long.
That’s it. That’s all.
Alpine Linux isn’t the only operating system that uses musl, a lightweight version of the standard C library (libc). Other operating systems that use musl and are potentially vulnerable include Adélie Linux; Void Linux; Sabotage Linux; OpenWrt, an Android variant, and the Yocto Project, which is used to build embedded Linux distributions.
Also: This clever banking scam keeps phishing by faking its own demise
Wind River, which produces the commercial embedded Linux distro, Wind River Linux, is also looking into the issue. A company representative told me, “Wind River takes security seriously. We are actively reviewing the reported vulnerability and assessing its potential impact. We will take appropriate action as needed.”
Behind the scenes, when OpenSSH is built without PAM, it verifies passwords by hashing the password attempt using the C library’s crypt() function. It then compares the result to the account’s stored password field. So far, so good.
But when a key is longer than 256 bytes, musl’s crypt() function returns the string * as an error indicator. That is also what the password field holds for any account with no password, such as a key-only account. Thus, the “hash” matches and the login succeeds, and the attacker walks in. [...]

## [118] Sequoia shutting down its Scouts program marks the end of an era
TechCrunch | full text via TechCrunch | ~734 words

Sequoia this week announced a broad overhaul in a memo posted to X, a move that includes closing its London office and shutting down its scout program. Observers warn that it would be a mistake to read too much into the London closure, since the British capital has a thriving AI scene. On the other hand, the decision to end scouts says more about where venture investing is headed.
That’s partly because 17 years ago, Sequoia pioneered the scouts model, in which select founders and operators write checks on the firm’s behalf. Amid increased competition for deal flow, many VC firms followed suit. But a consensus now seems to be emerging that the model has reached its limits in its current form.
Not everyone was sold on the model in the first place. “They pioneered the scout program but [to be honest] it never made sense to me!” VC Sheel Mohnot wrote on X this week. “The scouts themselves don’t really care that much about the investments, you can still miss (like they did with Uber), not sure what it gets you. I suspect other firms will shutter theirs too,” he added.
To be clear, Sequoia didn’t make a case against scouts in the memo. Instead, it framed its decision as part of a broader need for more focus. But its goal of “putting more energy behind fewer people and things” is likely to resonate with others who’ve questioned the ‘spray and pray’ approach to scouting.
Rival firm Andreessen Horowitz (a16z), for instance, rolled out a global scout network aimed at spotting opportunities in the U.S. and also in smaller European hubs. But a16z partner Gabriel Vasquez told TechCrunch earlier this year that the firm had revamped its program to double down “on the best people.”
Under this new approach, Vasquez explained, scouts get more resources but are also expected to be more active, such as by co-hosting dinners with the firm. “They get more budget, but we have reduced the number,” he said.
This also seems to indicate that it is VC firms that have been driving an overhaul of the model. For founders, being a scout is attractive: it brings them closer to firms they may want checks from someday, or even a partner role with, and being seen as someone who can write a check can raise their standing among other founders.
Some scouts will undoubtedly mourn the end of Sequoia’s program. [...]

## [41] FAA to finally ditch floppy disks in what it calls "historic" tech upgrade
Ars Technica | full text via Ars Technica | ~368 words

While you might be pondering whether to replace a smartphone with one that has a slightly better camera or a second screen, the Federal Aviation Administration is planning a much bigger leap in technology for the country’s air traffic control system.
The FAA said yesterday that it will stop using floppy disks as part of a long-awaited upgrade that will give air traffic controllers faster access to data needed for crucial safety alerts. The new Enterprise Information Display System (E-IDS) will be installed in 435 facilities, replacing several information display systems dating to the 1980s.
The FAA “is continuing its historic modernization of America’s air traffic control system by replacing outdated floppy disks that contain vital weather and other critical information with a streamlined, 21st-century system,” the agency said. E-IDS will be “deployed to operational control positions at more than 400 facilities across all air traffic control domains,” and “provide operationally essential information for controlling aircraft,” the FAA said.
The change has been in the works for over six years. “No more floppy disks or paper strips,” then-Acting FAA Administrator Chris Rocheleau told the House Appropriations Committee last year.
The FAA said E-IDS will replace older tools that have “technical end-of-life issues” and address two of the aviation agency’s top safety concerns: distribution of weather alerts to pilots (known as PIREP for Pilot Report); and timely distribution of Notices to Airmen (NOTAM), which include information on abnormal statuses and hazards.
“E-IDS gives air traffic controllers the information they need to make timely decisions and keep the flying public safe,” FAA Administrator Bryan Bedford said. “We’re moving away from outdated, manual processes and replacing technology that once relied on floppy disks with a modern system that allows controllers to instantly share critical flight alerts, restricted airspace schedules and pilot reports across the National Airspace System.”
Upgrades will take a year
It’ll take a year or so to make the upgrades at every facility. The first sites to get E-IDS will be Atlantic City International Airport, Nashville International Airport, Greater Rochester International Airport, and data processing hubs in Atlanta and Salt Lake City. The FAA said it plans to complete the upgrade at 435 sites by the end of 2028.

## [77] Raspberry Pi 5 price hike means the 16GB model now costs three times what it did at launch — and of course, the global RAM shortage is to blame
TechRadar | full text via TechRadar | ~1043 words

Raspberry Pi 5 price hike means the 16GB model now costs three times what it did at launch — and of course, the global RAM shortage is to blame
Raspberry Pi says scarce 16GB DRAM leaves it no choice
- Raspberry Pi has raised the 16GB Pi 5's price by $80 to $385, more than triple its $120 launch price
- Company CEO blames lack of alternative 16GB DRAM supply, compounded by wider component shortages
- Raspberry Pi called the hikes temporary, but memory makers expect tight supply to last until 2028 to 2030
Raspberry Pi has raised the price of its 16GB Raspberry Pi 5 yet again, and the flagship board now sits far from the brand's budget roots.
In a blog post, company CEO Eben Upton confirmed an $80 increase that takes the board to $385, which is more than triple the $120 it cost at launch in January 2025.
The 16GB variants of Compute Module 5 increase by $40 in the same round, while the Raspberry Pi 500+, the company's keyboard computer that also offers 16GB of RAM, remains at its existing price.
A far-reaching memory crisis dictates prices
The threefold figure is cumulative rather than a single jump: The November 2026 increase on its own amounts to roughly 26%, but the rest built up over a run of rises that began in December 2025, when the 16GB Pi 5 went from $120 to $145. February added $60, leaving the board 70% more expensive than at launch, and April added a further $100.
That April 2026 round also brought a new 3GB Raspberry Pi 4, introduced to give buyers a cheaper middle option, with Upton saying at the time that the LPDDR4 memory used in the Pi 4 and Pi 5 had risen sevenfold in price over the previous year.
November's change also comes barely a month after Raspberry Pi raised prices on its 2GB boards by $12.50 each, having decided that shielding those models from earlier price increases was no longer sustainable.
Upton's explanation is more specific than a general complaint about RAM prices. He blamed "a lack of alternative supply for 16GB DRAM, compounded by other ongoing component shortages," which suggests the bottleneck is sourcing at that particular density rather than cost alone.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
Raspberry Pi, for its part, has been qualifying additional memory suppliers through 2026 to widen its options, and the wording implies those alternatives remain thinnest at the top of the range. [...]

## [18] How Grab Improved Mobile App Stability by Safely Handling Surge in AI-Generated Code Changes
InfoQ | full text via InfoQ | ~539 words

The growing adoption of AI coding assistants has accelerated development and increased the volume of code changes per release, bringing more opportunities for defects and crashes, says Grab. To address these challenges, they implemented a layered defense strategy to prevent, detect, and contain crashes throughout the development and release lifecycle.
Grab observes that "AI is speeding up how fast code is written; the layered defense is what makes that speed safe":
At [Grab's] scale, crashes leaking into production are an ongoing risk. A high volume of merge requests lands every week across many product teams, many shipping features behind flags that are switched on independently of releases. Any one of those changes can introduce a crash.
Beyond degrading the user's experience, a mobile app's crash reduces crash-free session rates and, as a consequence, the app's Google Play ranking. It also has an increased cost because not all users enable automatic updates, meaning that "a mobile crash that ships stays on users' devices" for longer. Furthermore, not all crashes come with clean, symbolicated stack trace, which means that "finding the cause means cross-referencing release timelines, flag rollouts, and session metadata".
Grab's layered defense follows a shift-left strategy aimed at catching crashes as early as possible through a series of safeguards along the development cycle phases: pre-merge through pre-production, release control, and post-release response.
During the pre-merge to pre-production phase, the goal is prevention, which Grab describes as its "primary line of defense". To achieve this, Grab engineers use static code analyzers such as Android Lint and SwiftLint to catch issues before code even merges via platform-specific, community-based, and custom lint rules; automated and manual testing, including unit tests, UI tests, and quality assurance (QA) checks; and Grab Early Access (GEA), a pre-production gate where early builds are distributed to internal users and actively monitored for crashes:
A crash that only a handful of internal users see in GEA would, at production scale, translate into a substantial spike in the crash rate, extra support load, and potentially a hotfix. Catching these crashes before they ever reach production users makes GEA one of our most important stability gates.
During the release phase, Grab uses staged rollout and feature flags to control production exposure to crashes. [...]

## [19] Open Source pg_vectorsearch Brings More Scalable Vector Search to PostgreSQL
InfoQ | full text via InfoQ | ~649 words

Tiger Data has released pg_vectorsearch, an open source PostgreSQL extension for vector similarity search, currently in alpha. Its PRISM index uses data partitioning and compression instead of the graph-based approach used by pgvector’s HNSW index, reducing memory requirements and index build times.
According to the authors, pg_vectorsearch enables faster, more memory-efficient vector search directly in PostgreSQL, reducing the infrastructure required to handle large vector datasets. The extension supports existing pgvector columns, allowing applications to perform vector search without a separate database. To use the new capabilities, developers must install the extension and create a PRISM index on the vector column:
CREATE EXTENSION pg_vectorsearch;
CREATE INDEX ON documents USING prism (embedding vec32_l2_ops);
In Tiger Data’s own benchmarks using 100 million vectors, PRISM built an index in 1 hour and 40 minutes on a machine with 128 GB of memory, while HNSW (Hierarchical Navigable Small World) took 42 hours on a machine with 512 GB of memory. Formerly known as Timescale, Tiger Data is the company behind TimescaleDB, the open source PostgreSQL extension for time-series data and real-time analytics.
Erik Nordström, senior staff engineer at Tiger Data, Matvey Arye, principal engineer at Tiger Data, and Noah Hein, staff product marketing manager at Tiger Data, write:
PRISM brings a partition-based approach to PostgreSQL, similar to the approach used by newer dedicated vector search systems. Instead of connecting every vector to its neighbors in a graph, PRISM groups similar vectors into partitions and stores them as a list in a compressed format that is densely packed into database pages.
While HNSW is an approximate nearest-neighbor algorithm that quickly finds vectors similar to a query in large datasets, PRISM narrows searches to relevant partitions and scans compressed vectors sequentially. This reduces index size and avoids costly random memory or disk access, enabling faster vector search with less RAM directly in PostgreSQL.
Michael Freedman, cofounder and CTO of Tiger Data, published an article describing the architecture of the PRISM vector index. The index in pg_vectorsearch combines hierarchical clustering to narrow the search space, compressed vectors for efficient sequential scanning, and RaBitQ quantization to reduce expensive distance calculations. [...]

## [21] Meridian — an experimental web browser built on Servo and GPUI
Lobsters | full text via Lobsters | ~145 words

Meridian is a web-browser for MacOS built on GPUI and Servo. Meridian is already quite useful to browse websites that are light on javascript and layouting features. The browser is highly configurable: fonts, keybinds, colors, tabs and all.
To try Meridian, you can use nix:
nix run git+https://tangled.org/oppi.li/meridian
The project is developed on Tangled, all contributions are welcome, please do browse the list of open issues if you are looking to contribute!
Meridian supports the following features:
Under the hood, Meridian is written in Rust and built on GPUI and Servo. Web pages and browser state is managed by Servo. The browser's chrome is drawn by gpui, the UI framework behind the Zed editor. The glue code to interface servo with gpui lives in separate library, gpui-servo, which exposes Servo as an ordinary gpui component, so anybody can now write a servo-based browser in GPUI!

## [23] Scriptable GeoDNS: leaving AWS for Bunny
Lobsters | full text via Lobsters | ~1590 words

Scriptable GeoDNS: leaving AWS for Bunny
Vincent Bernat
To optimize the performance metrics of this blog, I relied on Amazon CloudFront to serve the assets,1 and Route 53 for the geo-aware DNS2 to direct readers to the closest host serving the content. But Route 53 is expensive: US$0.50 per zone per month, US$0.70 per million geolocation queries, and US$0.75 per healthcheck per month[1], plus US$1 per month for the KMS key[2] needed to sign zones with DNSSEC. When I discovered that Bunny DNS is almost free[3] for up to 500 domains and features scriptable answers, I made the jump! Plus, it’s a European company based in Slovenia.
Bunny CDN#
Bunny.net[4] started as BunnyCDN in 2015[5]. They added IPv6
support in 2017[6]. Switching was uneventful. I don’t bring a custom domain: I
serve the content from the b-cdn.net domain. As I depend on content
negotiation to serve AVIF and WebP images[7], I configure the CDN to cache
each image format separately[8].
I disable logging[9] to avoid collecting personal information. While the bunny.net GDPR page[10] promises they anonymize data, it is unclear what CloudFront keeps in its own logs when logging is disabled.
The only downside of the bunny.net CDN offering is the lack of HTTP/3. I asked their support: two minutes later, they answered they are working on it but have no ETA to share.
Bunny DNS#
Bunny.net introduced their DNS offering in 2022[11] and recently reduced its cost to almost zero[3]. They support geographical routing[12], but a very cool feature is the scriptable DNS[13]: it runs a piece of user-supplied JavaScript on each query to compute the answer.
I run seven small NixOS virtual machines to host this blog around the world: Paris, Nuremberg, Ashburn, Singapore, San Jose, São Paulo, and Sydney. Bunny’s scriptable DNS lets me return the IP addresses of the two nearest servers. The browser falls back to the second server if the first one is down. [...]

## [58] Containerd 2.4's switch to klauspost's gzip decoder speeds up real image layers by 18%
Dev.to | full text via Dev.to | ~1598 words

Containerd 2.4.0 shipped a one-line-sounding change: layer decompression now uses klauspost/compress/gzip instead of the standard library's compress/gzip. The pull request claimed 1.4 to 1.5 times faster decompression, measured on a 3.4GiB CUDA image and a 7GiB PyTorch image, on arm64. I run neither of those images, and my container host is an Intel Xeon, not an Apple Silicon or Graviton box, so I wanted to know what this actually buys an ordinary python:3.12 pull on ordinary x86_64 hardware.
It buys about 18%, not 40-50%. The allocation story, on the other hand, held up completely.
What actually changed
The change is PR #13560 against containerd/containerd, merged 30 June 2026 and released in containerd 2.4.0 (16 September 2026). It touches exactly one function, gzipDecompress in pkg/archive/compression/compression.go, and only the decoder. Compression still goes through the standard library. The PR description is explicit that this "affects only gzip layer decompression" — nothing about zstd layers changes, because containerd was already using klauspost/compress for those.
My environment runs this code today. Docker Engine here bundles containerd v2.4.2, and strings /usr/bin/containerd | grep klauspost/compress/gzip finds the vendored package compiled into the binary I actually have running.
Getting real layers to test against
Benchmarking synthetic data would have missed the point — gzip's throughput depends heavily on what you feed it, and a container image layer is mostly binaries, shared libraries, and Python wheels, not random bytes or highly repetitive text. I pulled python:3.12 with docker pull, which populates containerd's own content-addressable store, then read the real compressed layer blobs straight out of that store:
ctr -n moby content get sha256:<layer-digest> > layer.tar.gz
That gave me the amd64 manifest's seven layers, 392.8MiB compressed, 1081.3MiB decompressed once I ran them through gzip -t to confirm they were intact. The smallest is a 249-byte metadata layer; the largest is 237MB compressed, 670MB decompressed.
I wrote a small Go program that decompresses each blob with compress/gzip and with github.com/klauspost/compress/gzip in turn, three times each, keeping the fastest run, and reading runtime.MemStats around the final run to get allocation counts.
The headline number, and the one that argues against it
Per layer, the speedup ranged from 1.12x to 1.23x, with the 249-byte layer too small to measure meaningfully either way. [...]

## [73] Microsoft Removes PC-to-PC Migration from Windows 11, Points Users to OneDrive-Based Backup
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~87 words

Windows 11 offered a PC-to-PC Migration feature that "moved files and settings directly between two PCs over Wi-Fi or Ethernet," reports Ghacks. But according to an updated Microsoft support page, the tool is no longer available. "Microsoft's support documentation now redirects users to Windows Backup, a tool that relies on OneDrive cloud storage instead of a direct connection between two computers..." Windows Backup works differently. It requires a personal Microsoft account and backs up supported folders (Desktop, Documents, Pictures, Videos and Music) to OneDrive. Free OneDrive accounts

## [98] Automake 1.20 Brings New Features, Desires To Re-Establish GNU As Leading Build System
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~16 words

Out today is GNU Automake 1.20 with the new --enable-jobserver option and opting for GPLv3+ licensing...

## [8] MaxxBench – "Nice DeepSWE score. But is it true?"
Hacker News | full text via Hacker News | ~2165 words

Introducing MaxxBench: Benchmarking Task Adaptation and Generalization in Frontier Coding Agents
We changed requirements in a coding benchmark and found models talking themselves out of following them.
Sometimes the agent understood the new requirement perfectly. It described what needed to change, considered an implementation, and then decided the hidden tests probably wanted something else. In one run, a model implemented the change correctly, asked another model for the benchmark’s original answer, and removed its own correct code after receiving it.
This is an awkward habit for a coding assistant to have. It is also a habit that a familiar benchmark can reward. If the model has guessed what the tests expect, it gets the same passing result as an agent that worked carefully from the requirements.
We built MaxxBench to examine how much coding performance depends on those expectations. It changes the instructions or starting code of 89 DeepSWE tasks, giving models familiar engineering work with a reason to revise their usual approach.
Methodology: Small mutations...
Once a benchmark becomes popular, it becomes part of the development process. Its tasks can enter training data. Its scores influence checkpoint selection. Developers adjust prompts and agents against its failures. There are plenty of opportunities to get better at that particular exam. We call gains tied to its particular tasks and conventions benchmaxxing.
Then the scores cluster near the top, and the usual response is a harder benchmark. Recent releases such as FrontierSWE v2 have pushed toward engineering projects that can occupy an agent for much of a day.
We chose DeepSWE’s medium-duration feature-implementation tasks because they are closer to the everyday coding work we wanted to evaluate. Before adding more work, we wanted to know how well models would handle changes to the tasks they already scored well on.
For example, one DeepSWE task asks an agent to write a separate test report for each browser. We added a requirement that the filenames be lowercase. The reporting feature still needs to work; Chrome.xml should now be chrome.xml.
Another task adds retirement dates to FastAPI routes. We changed the required timestamps to UTC with a trailing Z, instead of preserving the supplied time-zone offset.
Example mutations
These changes resemble requests a developer might make after reviewing a first implementation. The agent has to keep the feature working while adjusting its behavior. [...]

## [82] Is Mandating AI Use in the Workplace Backfiring?
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~96 words

Some workplaces are holding mandatory AI training sessions, while others "are requiring employees to use a specific number of tokens," reports the Washington Post, "or log a certain amount of time on AI platforms." The article's headline? "Why mandating AI use in the workplace can backfire." [A] lot of employers are going about it the wrong way, said Arvind Karunakaran, an assistant professor of management science and engineering at Stanford University. "You can consume a lot of tokens without creating a lot of value," Karunakaran said.... The adoption of AI is happening faster than the ad

## [149] The Man Who Invented Selenium Also Built Its Replacement
DZone | SNIPPET ONLY (DZone: HTTP 403) | ~80 words

There's a specific kind of credibility that comes from someone destroying their own creation. Jason Huggins built Selenium in 2004. It became the foundation of an entire industry; the WebDriver protocol he helped establish is still a W3C standard, running underneath a huge share of the world's test automation two decades later. So when Huggins is the one leading the charge on Vibium AI, a framework built on the premise that we shouldn't be writing test scripts at all anymore

## [34] Ships loiter near subsea cables amid Iran's warnings to Trump
Ars Technica | full text via Ars Technica | ~309 words

Several tanker ships linked to Iran have been loitering over subsea Internet cables in the Gulf of Oman near the Strait of Hormuz—a possible indication that the Iranian government is preparing to attack such undersea infrastructure in response to any renewed US and Israeli strikes.
The movements of three sanctioned tankers and an Iranian fishing boat have been tracked near major undersea cables by the maritime intelligence firm Windward in October, according to the Financial Times. Six active cables currently cross through the contested Strait of Hormuz, linking the Middle East to Europe, Africa and Asia, with two more cables having segments under construction in the region.
Four countries, including Iraq, Kuwait, Bahrain and Qatar, depend entirely upon such subsea telecommunications connections running through the Strait of Hormuz chokepoint to link with the outside world. But other countries also depend heavily on the region’s undersea cable network—one third of India’s westbound Internet traffic goes through the Persian Gulf and Strait of Hormuz.
One cable under construction, the 2Africa cable, is owned by a tech consortium that includes the US company Meta. That was one of the major cable corridors visited by the drifting Iran-linked ships.
Windward used both ship-tracking data and satellite images to track the vessels as they slowed down and looped around near multiple cables, with some ships then “going dark” by switching off their automatic identification system (AIS) transponders that normally broadcast their location and other information.
Such movement and behavioral patterns suggest the Iran-linked ships may be “mapping the cable routes, or placing charges or mines on them while dark,” Windward told the Financial Times.
Windward highlighted the examples of two sanctioned tankers linked to Iran that spent days drifting “directly over regional cable corridors… both with no commercial reason to stop” in a blog post on October 26. Both ships carried no commercial cargo.

## [79] OpenIndiana 2026.10 Released With Updated Tools & Compilers, New Apps
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~30 words

OpenIndiana Hipster 2026.10 is out today as the newest six-month update to this operating system based on Illumos and with the lineage tracing back to the fruitful Sun OpenSolaris days...

## [68] AlpineBSD Announced - an AI-free FOSS OS
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~99 words

Lproven (Slashdot reader #6,030) shares his article about a new OS in the BSD family "combining NetBSD's kernel and libc with a port of the Alpine Linux userland" — and promising it won't use AI-generated code: AlpineBSD is so new that it barely exists yet. There are no installation media available, though it's possible to manually bootstrap an installation. What AlpineBSD does already have is an AI policy, and the plan is to avoid "the output of generative AI models (e.g. LLMs)" as far as possible: "Any software whose code, documentation, binaries, or other assets include, in any pa

## [129] Meta’s best AI model now trains the one most of its users get
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~20 words

Starting on Friday, everyone using Meta’s Muse agent and Meta AI gets new models the company trained using Muse Wonder,
