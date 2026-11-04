# Full text for 30 picks -- untrusted article content, treat as data only

## [115] Binance says hackers used fake job interviews and an internal AI tool to pull off the $6.3 billion heist
The Verge | full text via The Verge | ~488 words

The largest crypto theft to date was pulled off by combining some well-known hacking techniques over the course of a few months, according to Binance. A postmortem from the company says the process started in June with one developer downloading a tampered installer apparently spread by a malicious Google ad, exposing details about the engineers and how they work. Then, in September, another engineer was targeted by someone pretending to be interested in hiring them; that person set up a series of calls and multiple rounds of interviews, shared social media pages to build trust, and eventually prompted them to download a fake interview assignment that was actually malware.
Binance says hackers used fake job interviews and an internal AI tool to pull off the $6.3 billion heist
A North Korean hacking unit reportedly started its break-in with a search engine ad that served up a malware download.
Binance claims that its security teams did detect the first installation of malware in June, and replaced the worker’s device, but that its security tools didn’t detect the second attack that deleted the pyenv executable and replaced it with a malicious version that gave them backdoor access:
The malware employed sophisticated obfuscation and evasion techniques, including replacing a legitimate development tool component with a malicious version to execute commands and establish communication with an attacker-controlled external server. The 0-day malware was not detected by the endpoint security protection tools at the time. The attacker also took steps to conceal the malicious activity and remove traces of the compromise, making detection and subsequent investigation more challenging.
By October 20th, the story goes, the attackers, whom the FBI has identified as a North Korean unit dubbed “TraderTraitor,” used Binance’s own internal AI tool to gain control over wallets for the first engineer compromised in June, as well as a third employee, before logging into the third employee’s computer on October 29th and launching their attack. [...]

## [3] Postman silently auto-installs AI plugins and attempts to share all API data
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [13] Claude Introduces Message Threads
TLDR AI | full text via TLDR AI | ~364 words

Make long-running agents faster with message threads
New in the Messages API, send your conversation once, and the API receives only what’s new with every turn.
Message threads is now available in public beta on the Claude Platform. With message threads, agents no longer need to resend the full conversation history on every turn, reducing latency for long-running sessions.
How message threads works
A coding agent might make hundreds of requests in one session, and each request resends every earlier message and tool result. Once a conversation reaches hundreds of thousands of tokens, resending all of it adds time before Claude starts responding. With message threads, agents send only what’s new since the last turn, which reduces time to first token (TTFT).
With message threads on by default for most Claude Code users, requests with 500k to 1M tokens see median TTFT drop by about 35%.
To use message threads, add the thread parameter to Messages API requests. The first request includes the full conversation and starts a thread. Each request after that includes only the new messages and the ID of the previous response. Between turns, we hold each thread in memory, where it’s encrypted and not written to disk. A thread expires 5 minutes after its last request and your client then resends the full conversation to start a new one. While each request is smaller with message threads, Claude still reads the full conversation on every turn, so token usage stays the same.
Message threads is best for active sessions where latency matters, including:
- Long-running coding agents, where each tool result or file edit adds to the conversation.
- Computer use agents, where screenshots stay with the thread instead of being re-uploaded on every turn.
- Document and image-heavy workflows, where requests are made smaller.
The more context an agent carries, the more message threads can reduce time to first token.
Getting started
Message threads is available now in public beta on the native Claude Platform, and on Claude Platform on AWS, Claude in Microsoft Foundry, and on Claude Models on Google Cloud (Anthropic managed). Standard Claude token rates and existing rate limits apply. See the documentation to get started.

## [79] Porting 287,000 lines of React in 3 days. The hard part was proving nothing changed.
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1844 words

Porting 287,000 lines of React in 3 days. The hard part was proving nothing changed.
How Claude ported every screen of Maple's React app to Foldkit, and the pixel, behavior and accessibility harness that decided when each screen was done.
On this page
In October we moved Maple’s web app off React. It was 287,000 lines across 131 routes, and Claude did the port in three days. The review rounds and the fixes after our first deploy, both covered further down, came on top of that. Writing the new code turned out to be the easy part. Most of our own work went into a tool that compared the two apps and told us whether the port was right. The port and the harness are in PR #1539, and the cutover that deleted the React app, and the harness with it, is in PR #1589.
Why we left React
The React app worked, but changing it had gotten expensive. Data on a page came from atom hooks, each with its own cache key and lifetime, and there were about 520 of those hook calls spread over 208 files. If you wanted to know what happens when someone switches org while a query is still running, you had to read every component on the page and work out the order they render in.
In August the errors page crashed in production with React error #301. A helper created a new wrapper atom on every render, a hook compared it by identity and set state during render, and the two kept triggering each other. We fixed that one in a day, but nothing stopped the next one from being written.
Everything else in Maple is built on Effect, and more and more of the frontend is written by agents, which make the same hook mistakes we do.
Why Foldkit
In our React app, state lived all over the place: in hooks, in atoms, in components, and it changed whenever something happened to render. Foldkit is The Elm Architecture on top of Effect, and it works the other way around. All state sits in one Model, and only one function is allowed to change it. A click, a response or a timer shows up as a Message with a past-tense name like ClickedRow or SucceededLoadLogs. update takes the Model and a Message and hands back the next Model, plus any Commands it wants run. Commands are the only code that gets to talk to the network, and whatever they get back comes in as another Message. If you’ve written Elm or Redux, none of this is new. Honestly, that was the appeal. I love how explicit it is and how easy it is to reason about, and it fits the way I build software these days a lot better than React did. [...]

## [77] How we halved DNS build delay and cut memory use by 85%
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~3548 words

How we halved DNS build delay and cut memory use by 85%
When I last wrote about our DNS propagation pipeline in 2022, the Zone Builder received about 250 DNS record changes per second. Today it receives about 700, nearly three times as many, plus about 100 other events, such as zone setting changes. However, the number of events was never the real problem. The problem was the kind of work some of those events needed, and how that work grows with the size of a zone. Some zones now hold more than 20 million records, and we expect them to keep growing toward hundreds of millions.
Each event starts a clock that measures how long it takes us to turn that change into data our authoritative DNS servers can use. We call that work a build. A build reads the current database state, converts it into the format used at the edge, and writes any changes to Quicksilver.
In 2022, per-record builds were 150 times faster than full builds on average. On a test zone with one million records, per-record builds were 4,250 times faster. We ended that post with the obvious next step: do the same thing for zone settings.
Why doesn't the Zone Builder just rebuild the setting that changed?
It should, and that is where we ended up. However, proving when it was safe took most of the work. A record event identifies what changed. A zone event can come from many Cloudflare products, may not say why the zone changed, and can alter data shared by several zones with the same name. Choosing too much work wastes capacity. Choosing too little can leave stale or incorrect DNS data at the edge.
We built a targeted build planner that chooses the smallest build we can prove is safe, and a new scheduler that combines work for the same zone. Zone setting changes no longer rebuild zones with tens of millions of records. Together, they cut peak memory by 85%, and the extra headroom let us safely shorten waits the pipeline has always needed for resilience, halving the time from a DNS change to its data being written to Quicksilver.
How DNS changes reach the edge
A DNS zone is the collection of records and settings for a domain. Cloudflare uses a multi-stage pipeline to turn a change to that zone into data available across our global network.
- A customer changes a DNS record through the DNS Records API or dashboard, or another Cloudflare service changes a zone setting.
- The change is stored in a database.
- The database change or another system produces a Kafka event. [...]

## [32] UEFI bootkit infected fully patched Windows machines. Is Microsoft to blame?
Ars Technica | full text via Ars Technica | ~360 words

In 2023, malware tracked as BlackLotus became the first publicly documented in-the-wild UEFI bootkit capable of bypassing Secure Boot on fully updated Windows 11 systems. With the industry-wide chain-of-trust mechanism subverted, the malware was able to run malicious code before Windows was fully loaded and many security defenses were operational.
Microsoft had already patched the vulnerability that BlackLotus exploited in 2022. In 2023 and 2024, Microsoft issued additional updates. The first added a new certificate that no longer trusted the vulnerable boot managers. The second provided the means to revoke trust in the digital certificate used to sign older vulnerable Windows boot managers. The organizations infected by the new bootkit, which is tracked under the name BlackX, had installed all of these patches. So how did they fall victim?
UEFI bootkit refresher
Before discussing the incident further, a brief review of BlackLotus and UEFI malware is in order. Short for Unified Extensible Firmware Interface, UEFI is firmware that runs immediately after a computer is turned on. One of its main jobs is to load system configuration settings, identify and initialize hardware components, and prepare the computer to start its OS.
Another important UEFI function is Secure Boot, a security feature that establishes a chain of trust by verifying the digital signatures of each piece of boot software before allowing it to execute. Its purpose is to prevent attackers who gain control of a device, either physically or through a malware compromise, from running unauthorized boot code in place of legitimate software.
One item that must be digitally signed is the boot manager, a component stored on a small dedicated partition on a drive. The boot manager is responsible for the initial loading of the OS. Both BlackLotus and BlackX exploit “Baton Drop,” a logic flaw in the Windows boot manager that allows attackers to bypass Secure Boot (and, under certain conditions, extract BitLocker encryption keys). The vulnerability, tracked as CVE-2022-21894, came to light in 2022. Microsoft fixed the vulnerability that same year, but it didn’t revoke trust in the certificate used to sign older vulnerable boot managers. BlackLotus exploited this gap and went on to load a malicious kernel-mode driver.

## [25] Google will let schools skip AI tools, but they have to give up search, too
Ars Technica | full text via Ars Technica | ~219 words

While Google is trying to move beyond Chromebooks, the ubiquity of these devices has made the company’s education products huge in schools. Now, Google says it will let educators choose whether to allow its AI tools in the classroom. However, blocking AI tools also means giving up search, leaving schools with a difficult decision.
Google’s new overarching approach to AI in K-12 classrooms sounds good on the surface. After consulting educators, researchers, and lawmakers, Google has decided that schools using its education products will be opted out of AI tools by default. It will be up to administrators to manually enable them when these changes roll out in the coming months.
When you look at what Google considers to be an AI tool, the nature of the Faustian bargain becomes clear. The affected products are Gemini, Gemini Notebook, Gemini in Classroom, and Google Search. There’s no picking and choosing—you either allow all the AI or none of it.
This is actually consistent with Google’s approach in the consumer space. Google executives have said in no uncertain terms that Google Search is AI search. Most searches now provide an AI Overview at the top, and the company is constantly coming up with new ways to nudge people toward the conversational AI Mode chatbot function. Google sees this as the future.

## [7] US tech giants' hidden AI debt swells 90% to $3.2T in 6 months
Hacker News | SNIPPET ONLY (Hacker News: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [172] AI inference startup Fal doubles its valuation to $16B as demand surges
TechCrunch | full text via TechCrunch | ~205 words

Fal, a San Francisco-based startup that hosts and runs AI video, image, and audio models, has raised $1.3 billion in its latest funding round led by Bessemer Venture Partners, with participation from Nvidia, Sound Ventures, and T. Rowe Price. The deal values Fal at $16 billion, double its $8 billion valuation in April, Bloomberg reported.
The startup announced its Series E and F rounds at the same time, noting that a combined $1.65 billion was raised across both. (Sequoia led the earlier round.)
The latest round (Series F) comes amid soaring demand for inference services, the process of running an AI model that’s already been trained to generate outputs, particularly from customers relying on open source models. Fal surpassed $800 million in annualized revenue earlier this year, Bloomberg’s report noted.
Companies providing inference services, including Baseten, Fireworks AI, and Modal, have also been growing rapidly and raising large funding rounds at higher valuations. But their gross margins remain thin because of the high cost of buying or leasing compute, according to several people familiar with inference companies’ financials.
Fal was co-founded in 2021 by Burkay Gur, a former Coinbase machine learning leader and Oracle engineer, and Gorkem Yurtseven, who was previously a developer at Amazon.

## [149] Canva is announcing changes and layoffs affecting 22 percent of its staff
The Verge | full text via The Verge | ~266 words

Canva is making significant changes affecting 1,271 people, which is 22 percent of its staff, co-founder and CEO Melanie Perkins announced today. “For some people, this will mean changes to their roles or being asked to relocate to centralised hubs,” says Perkins. “Sadly, it will also mean saying goodbye to teammates and friends who have helped build Canva into what it is today.”
Canva is announcing changes and layoffs affecting 22 percent of its staff
Some Canva workers may have different roles, be asked to relocate, or be laid off.
In her note to staff, Perkins says that:
After exploring a wide range of alternatives, I’ve come to the difficult conclusion that small changes won’t be enough. To set ourselves up for the next decade, we need to refound Canva, getting back to our roots of small, empowered teams with the freedom to make decisions, take ownership and focus on what matters most for our community.
Canva’s changes include bringing its Product, Growth, and Platform teams together into one product organization, “simplifying layers” and “consolidating overlapping responsibilities,” and making Sydney the “primary home for more of our product teams, as well as roles in other Specialties where shared context and close collaboration are especially important.” Starting in January, Canva will also “expect” most hybrid employees to spend 2 to 3 days in an office each week “depending on what makes sense in your area.”
Employees leaving Canva will get benefits including at least six months of salary, twelve months of healthcare coverage, and career support resources.
Yesterday, Squarespace announced layoffs affecting 19 percent of its staff.

## [187] SUSE To Cut One In Ten Employees Because of AI
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~97 words

SUSE plans to cut roughly 10% of its 1,900-person workforce, with CEO Dirk-Peter van Leeuwen saying "automation and AI" are reducing the need for some roles and allowing the open source software company to operate with less overhead and flatter management structures. "We are announcing a reduction of SUSE's global workforce of approximately 10 percent," said Van Leeuwen in an email. "These decisions are painful for our people, our culture, and our open source community, but they are necessary for us to adapt and build a sustainable, resilient SUSE for the long term." The Register reports: Van

## [30] Vitest 5: Prioritises Performance with a Shared Vite Server, Trace View, and Stricter Test Defaults
InfoQ | full text via InfoQ | ~444 words

Vitest, the Vite-native testing framework maintained by VoidZero, has released Vitest 5.0, a major version that puts raw speed ahead of new surface area while quietly tightening several long-standing defaults.
Using a purpose-built benchmark suite that spans everything from a five-file utility package to a 1,280-module monolith, the team reports gains of roughly 8 to 25 percent across most setups, rising to 53 percent in VM pool scenarios. VoidZero summarised the release on X as "vm pools up to 53% faster, ~18% boost across the board including Browser Mode". The wins come from inline projects sharing a single Vite server, a stabilised on-disk fsModuleCache, fewer round trips between the main process and workers, and VM pools that reuse compiled code. A new vitest doctor command reruns a suite under alternative configurations and recommends faster options.
Browser Mode also gains a built-in Trace View that records each interaction and assertion as a DOM snapshot for step-by-step replay, while the new vi.when API lets a single spy return different values per argument.
clearMocks now defaults to true, unawaited async assertions fail rather than warn, hoisted vi.mock calls placed outside the top level now throw, and toThrow('') matches any error. As the independent OpenReplay breakdown puts it, most of these changes simply "break test code that was already wrong", but the dangerous ones are suites that pass locally on Vitest 4 and "go red in CI with an error that says nothing about why", usually call-count assertions that relied on mock history leaking between tests.
Vitest 5 requires Vite 6.4 and Node.js 22.12 or newer, and Yarn users must now install vite themselves because it became a peer dependency. The migration guide and v5.0.0 changelog document each change, and reporter output, attachments, and blob reports now live under one .vitest/ directory, so CI artifact paths need updating. Ecosystem catch-up is ongoing: Cloudflare's vitest-pool-workers issue notes its peer range pinned to v4 means any project pulling the new release "fails before a single test runs".
Against Jest, a recent head-to-head comparison scores Vitest ahead on performance and future-proofing yet behind on ecosystem and community, reflecting Jest's far larger install base and first-class React Native support. [...]

## [28] kitty 0.50.0
Lobsters | full text via Lobsters | ~37455 words

Changelog¶
kitty is a feature-rich, cross-platform, fast, GPU based terminal. To update kitty, follow the instructions.
Recent major new features¶
Choose an edge when resizing [unreleased]¶
The resize page now offers two strategies: Window retains the usual width/height controls, while Edge lets you choose an internal pane edge in the Splits layout and move its divider in a physical direction.
Switch strategies with 1/2 inside the page. Each strategy remembers its own Alt/Shift modifier and fraction, configurable with M and F. A sole internal edge is selected automatically. In Splits, either strategy uses R to restore the proportions saved when resize mode opened. See Resizing windows for the controls and configuration options.
Custom shaders [0.49]¶
kitty now has official support for Custom Shaders. These can be used for all manner of graphical effects, from animated backgrounds to focus highlighting to animations that change how cursor movements or mouse clicks are visualised.
See the documentation for a video gallery showcasing various custom shaders that ship with kitty.
Performance improvements [0.49]¶
This release saw tons of performance work focused on improving throughput making kitty even faster than it already is. Real world effective throughput should see a 15-35% improvement depending on workload. Some details:
- Improve throughput when processing large amounts of text with a scrollback buffer much larger than the CPU cache by ~35% by prefetching scrollback memory before it is written to
- Improve throughput when processing large amounts of text by ~50% for ASCII and ~15% for Unicode by writing runs of plain ASCII chars to the screen in batches and skipping unnecessary bookkeeping in the scrolling and tab handling hot paths
- Speed up SIMD UTF-8 decoding: ~20% faster for ASCII and ~50% faster for multi-byte text on both x86 and ARM, by processing pairs of vectors of plain ASCII text at a time and compacting decoded codepoints within 128-bit lanes, avoiding expensive cross-lane operations. Also add an AVX-512 based decoder, another ~75% faster for multi-byte text, used automatically on CPUs that support it (Intel Ice Lake+, AMD Zen 4+). [...]

## [76] OpenAI is finally merging ChatGPT's Chat and Work tabs
TLDR AI | full text via TLDR AI | ~219 words

The ChatGPT desktop app can be a confusing piece of software, given that there are ChatGPT and Codex sections, and within the former, there are Chat and Work tabs. With so many options, it’s sometimes easy to forget where you are working and where exactly your project is.
In an apparent effort to address this, OpenAI is now gearing up to merge the Chat and Work tabs within the ChatGPT experience, according to an email sent to users. OpenAI said that initially, this experience will be available to select users for feedback before it is rolled out widely.
“This will enable you to move from exploring an idea to having ChatGPT carry it through, all in one place. You can bring in your files and plugins and ask ChatGPT to build a website, create a presentation, or do things for you on the web, while reviewing and guiding its work. Codex will remain a separate experience in the ChatGPT desktop app,” the email said.
OpenAI also said with this transition, both ChatGPT and Codex will draw tokens from the same allowance pool. It said this change won’t impact most users, but based on usage and model, some folks might need to wait for resets more frequently.
Rival Anthropic merged Claude’s chat and Cowork functions into one screen in September.

## [175] Goldman Sachs restricted Claude Code for bankers — but made one surprising exception
The New Stack | full text via The New Stack | ~734 words

Goldman Sachs restricted Claude Code for bankers — but made one surprising exception
Replit CEO Amjad Masad is warning that AI coding agents running on employee devices are becoming a security risk for enterprises and governments, as financial institutions begin restricting access to tools such as Claude Code.
“AI agents running on employee endpoints are becoming a systemic security risk for enterprises & governments,” Masad writes on X, Tuesday. “Some are responding by restricting tools like Claude Code, as Goldman Sachs reportedly has.”
“Some are responding by restricting tools like Claude Code, as Goldman Sachs reportedly has.”
Why finance restricts coding agents
His comments follow a Bloomberg report that Goldman Sachs has restricted access to Anthropic’s Claude Code and Microsoft’s GitHub coding tools to engineers. The restrictions apply to bankers and traders, but certain quantitative employees known as strats are exempt.
Goldman spokesperson Nick Carcaterra told Bloomberg the bank weighs productivity gains against potential risks when deciding which employees can continue using AI tools.
Masad suggests Goldman Sachs is not alone.
“This is widespread in finance. The ban hammer is coming down,”
“This is widespread in finance. The ban hammer is coming down,” he writes, responding to a post about the bank’s restrictions.
When asked what was driving the crackdown, Masad points to “Supply chain attacks etc.”
The credential exposure problem
Running coding agents directly on employee machines raises concerns about credential exposure, malicious instructions and compromised dependencies, each of which has already surfaced well beyond the finance sector.
The credential question has been pushing vendors toward short-lived tokens for months, a shift Vercel recently forced on its own suppliers by setting a deadline to abandon the long-lived keys that an agent operating on an endpoint could quietly read and reuse.
When asked on X whether banks were more worried about code leaving their environments or a lack of audit trails, Masad says, “So many things.”
He offered no examples of security incidents that prompted Goldman’s restrictions or other financial institutions adopting similar policies.
Isolating agents in the cloud
Alongside his comments, Masad shares a security advisory published by Replit on Monday. [...]

## [64] Why Agents Are Soon Only Going to Have 1 Tool
TLDR Tech | full text via TLDR Tech | ~1289 words

Why Agents Are Soon Only Going to Have 1 Tool
For the past two years, building capable Agents meant designing tools, figuring out which actions help the model complete a task, deciding how granular each tool schema needs to be, or iterating on system instruction templates. This is changing. Agents are moving in the opposite direction by collapsing their entire tool catalog into one tool: exec.
This is called Code Mode (or Programmatic Tool Calling). Instead of forcing the model to trigger tools one at a time across turns, the harness gives the model a single exec(code) tool. The model writes a short TypeScript or Python script that chains, combines, and awaits actions inside an isolated sandbox.
From single actions to chaining workflows in code
To understand why agents are converging on a single exec tool, we should look at how tool calling evolved.
Initially, we only gave agents a handful of tools because they couldn't reliably choose or filter across a large catalog. As models improved, we connected dozens of tools or MCP servers, but ran into context window limits. We solved that with tool search and progressive disclosure, letting agents look up tools on demand.
Even with dynamic tool loading, we still had dozens of individual tools, and were still stuck with the limitation of standard tool calling: one action per turn.
In standard tool calling, the model generates a structured object (typically JSON) that defines a single action (or at best a flat batch of independent calls, like reading three files), waits for the raw output to come back, adds it into the prompt history, reasons again, and decides what to do next.
From my own experience, we made a big jump recently in how reliably models can combine and chain dependent actions in a single pass:
- Research and filtering: Instead of fetching a list of sources in Turn 1, reading them in Turn 2, and cross-referencing them in Turn 3, the model can write a script that queries the sources, filters out irrelevant hits, and extracts the exact answer in one step.
- Multi-file edits and inline verification: Standard edit tools typically operate on one file per tool call. With Code Mode, the model can apply coordinated changes across multiple files, run a verification check, inspect the output, or branch on pass or fail inside the same script. [...]

## [188] Linux 7.4 Features Steam Frame VR Headset, More AMD Zen 6 Enablement & Initial Apple M4 / A18 Pro Bring-Up
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~26 words

The Linux 7.4 kernel is hopefully going to be this year's Long Term Support (LTS) kernel version and is coming jam-packed with new features and changes.

## [159] GIMP 3.2.8 Released With Many Refinements, Numerous Security Fixes Due To AI Reports
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~23 words

GIMP 3.2.8 is out today as the newest stable release of this open-source image editing application that's most popular on the Linux desktop...

## [134] The biggest modding site in PC gaming is taking a stance on AI
The Verge | full text via The Verge | ~484 words

The PC gaming mods repository Nexus Mods is making disclosures about AI mandatory for uploads of new mods, meaning that mod authors will have to declare “whether AI has been used in their work,” the site announced today as part of a big post about AI-generated content on the platform.
The biggest modding site in PC gaming is taking a stance on AI
Nexus Mods says that authors of newly uploaded mods will have to declare whether AI was ‘used in their work.’
“One of the most consistent concerns we’ve heard is that it’s not clearly disclosed when AI has been used to create a mod,” according to the post from site owner Victor “Foledinho” Folmann. “We already have tags for AI-generated and AI-assisted mods, but we recognise that there’s a lot more we can do to make that information more accessible and clear for you all.” Any mods tagged as “AI-assisted” will also be required to include “a public explanation of how and where AI was used.” AI tags will also be “more prominent” on mod pages.
Folmann says Nexus Mods is “pro-human creativity” but “won’t introduce an outright ban on AI-generated mods.” As for why that is:
The answer is simple: AI is currently used throughout the whole process of creation, from script autocompletion to generation of textures, voices, and full assets, and it is difficult to draw a clear boundary between what is acceptable and unacceptable. An outright ban will not eliminate AI from the modding process but will prevent people from mentioning its use. We’d prefer the opposite; it should be out in the open, clearly labelled, and regulated according to the rules that we can implement on our platform.
Folmann notes that Nexus Mods won’t use mods to train AI and “will not sell or license them to anyone doing so.” However, the site is working on “clearer control” over how mods can be reused on others and strengthening attribution for when “a mod uses another Mod Author’s mod with the appropriate permissions.”
Nexus Mods is also making changes to the Recently Added section of the site to address a problem of mod authors uploading many mods at once, which makes other mods fall down down the page. “This is less of an issue related to AI, but it’s becoming much more prevalent as mod production is speeding up,” Folmann says. The changes include trying limits on how many mods from one author are shown at a time and “tighter restrictions” on uploads from new accounts. [...]

## [37] The Ubuntu 26.04 Rust sudo is not compatible with standard sudo
Lobsters | full text via Lobsters | ~471 words

You're probably reading this page because you've attempted to access some part of my blog (Wandering Thoughts) or CSpace, the wiki thing it's part of. Unfortunately you're using a browser version that my anti-crawler precautions consider suspicious, most often because it's too old (most often this applies to versions of Chrome). Unfortunately, as of early 2025 there's a plague of high volume crawlers (apparently in part to gather data for LLM training) that use a variety of old browser user agents, especially Chrome user agents. To reduce the load on Wandering Thoughts I'm experimenting with (attempting to) block all of them, and you've run into this.
If this is in error and you're using a current version of your browser of choice, you can contact me at my current place at the university (you should be able to work out the email address from that). If possible, please let me know what browser you're using and so on, ideally with its exact User-Agent string.
I am not blocking Inoreader's feed fetcher or considering it to be too old, and it routinely fetches feeds from me. I don't know why Inoreader is showing you this page. It is possible that they're periodically trying to fetch feeds or pages with an old browser HTTP User-Agent (or an actual old browser) and taking the results of that fetch (this page) as what they should show people instead of the results of their syndication feed fetcher agents. This is a bad mistake today; the results of modern HTTP fetches depend partly on the HTTP User-Agent used.
Much like Inoreader, Feedly is periodically fetching my syndication feeds with a fake, old browser HTTP User-Agent header, which fails, and is then grimly latching on to the results for their actual feed fetching with their regular Feedly HTTP User-Agent. There is nothing I can do about this; you should contact Feedly support, if you can find them. See this comment of mine in Wandering Thoughts for more details.
Due to an ongoing attack, you may need to change the "User Agent Brand Masking" setting so that your Vivaldi identifies itself as Vivaldi, instead of Google Chrome. This applies to even the current version of Vivaldi.
You may be seeing this through archive.today, archive.ph, archive.is, and so on. Unfortunately, archive.* crawls pages to archive in a way that is impossible to distinguish from malicious actors. [...]

## [148] Data centers are turning to old jet engines as the wait for power grows
TechCrunch | full text via TechCrunch | ~450 words

Stuck in years-long lines for grid connections and new turbines, some AI data centers are making their own electricity with converted jet engines, the New York Times reported Tuesday.
The engines, pulled from retired aircraft and rebuilt to burn natural gas, aren’t anyone’s idea of a permanent power plant. But they’re another sign of how far power supply has fallen behind the AI buildout.
For companies stuck in those lines, the main draw of converted jet engines is how quickly the engines can be up and running. “It’s all about getting power as fast as possible,” Rystad Energy analyst Audun Martinsen told the Times. With jet-powered units, “they can have a data center running in 24 months,” he said.
Hooking up 100 megawatts to the grid in Northern Virginia, by comparison, takes about seven years, according to the International Energy Agency. Most power capacity is expected to come on by 2031, an executive at Mitsubishi Power, one of the world’s top makers of power generation equipment, told Bloomberg last week.
In some cases, these delays are already costing some data center operators business. Last month, Microsoft pulled out as the anchor customer for Nscale’s data center in Loughton, England, after the local utility said it couldn’t deliver enough power until the early to mid-2030s.
Elon Musk’s xAI is among the companies already using the engines, having installed eight converted jet-engine turbines in Mississippi to help power its Colossus 2 data center in Memphis, the Times reported, citing state permits and satellite imagery. The units come from ProEnergy, which rebuilds a GE engine commonly found on Boeing jets.
In 2025, OpenAI followed Musk’s lead with gas turbines at its first Stargate site in Abilene, Texas. Crusoe, a Denver-based startup that builds AI data centers, is constructing that Abilene campus and ordered 13 of ProEnergy’s converted units in April.
In September, Crusoe walked away from a $1.25 billion deal to buy 29 natural gas turbines from Boom Supersonic, a startup developing a supersonic passenger jet that has also begun selling a version of that jet’s engine as a power plant for data centers. A Crusoe spokesperson told TechCrunch at the time that the company still plans to use turbines.
Currently the Trump administration is adding to the pressure by encouraging data centers to generate their own electricity. [...]

## [10] Jailbreaking my car's navigation system just so I can change the time
Hacker News | full text via Hacker News | ~2461 words

Jailbreaking my car's navigation system just so I can change the time
The car that I drive is a 2014 Renault Latitude. It's not a fancy car by any means and is starting to show its age, but it gets me from point A to point B and does everything else reasonably well so I've never really had any reason to complain.
When I bought the car, the previous owner asked me whether I wanted a "navigation map SD card" with it.
They mentioned that the car apparently needs this SD card just to change the time on the clock, but I didn't really find that believable - not that they were lying to me, but perhaps they couldn't figure out how to enter the correct settings menu. After all, videos of similar head units online showed the menu with the clock settings option right there.
Since the maps on the SD card were apparently very out of date and didn't function properly, I decided I didn't need it and the previous owner tossed it.
I didn't really miss it. The dashboard display did show a large "No maps found!" message taking up the majority of the display, but it didn't bother me too much.
Like most other European countries, Estonia uses daylight saving time, and we recently switched from summer time (UTC+3) to "winter time" (UTC+2), which meant that the time displayed on the dashboard was out of sync by an hour. I dived into the settings menu, hoping to easily find the "Set time" option in there.
That never happened.
The menu where the "Set time" option should've been simply didn't have that option. I compared the menus with the ones in online videos, and the option was simply missing. There were two "Settings" buttons on the dash, and one of them worked but only let me change various Bluetooth and phonebook settings, with no time & date settings in sight. The second Settings button did not work whatsoever, instead showing a "No maps detected!" pop up message every time I pressed it.
I must've spent an hour going through various menus, pressing various buttons or button combinations hoping to land in the correct menu, searching the web for information on this particular unit simply because I refused to believe that there was no option to change the time and I clearly must've been missing something obvious.
Just RE it
Still in denial, I decided to fetch the firmware and dig into it, hoping to find some indication on how to open the correct settings menu. [...]

## [83] CheerpJ 5.0
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2192 words

CheerpJ 5.0: Java 21/25 in the browser, full OpenJDK, and a new WasmGC engine
Today we are proud to release CheerpJ 5.0, the latest major release of CheerpJ, a full distribution of OpenJDK for the browser in WebAssembly, designed to run Java applications and libraries in the browser.
This release brings countless improvements, with the headline being support for Java 21 and 25. Together with Java 8, 11 and 17, which CheerpJ already supported, this completes the roadmap we first published in February 2025, whose goal was parity with the latest Java LTS by the end of 2026. CheerpJ 5.0 also now ships the full JDK, not just the JRE, for every supported version, making it possible to not just run, but also compile modern Java in the browser.
But, as strange as it might sound, modern Java is not the most impressive technical achievement in this release. CheerpJ 5.0 also includes experimental support for a completely new execution engine based on WasmGC. Stabilizing this engine will be our main focus over the next few months, and it will become production-ready with CheerpJ 6.0, in early 2027. We expect the WasmGC engine, together with several other lines of work, to make it practical to run large-scale modern Java applications in the browser, including modern versions of Minecraft and IntelliJ IDEA.
How does CheerpJ work?
CheerpJ is a full JVM in WebAssembly, first released in 2017 and engineered from scratch to make Java a first-class language in the browser. Its current architecture, introduced with CheerpJ 3.0 in 2024, was rebuilt around a JIT compiler compiled to WebAssembly. This allowed us to remove preprocessing steps and greatly increase compatibility with real-world code.
Unlike other solutions, CheerpJ is not limited to Java code written specifically for the browser. From day one it was designed to run existing, large-scale Java applications fully unmodified. That means full support for reflection, runtime class generation, custom class loaders, multithreading and synchronization. CheerpJ works exclusively at the Java bytecode level, so source code is never required. Proprietary or legacy applications whose source code is not available work with CheerpJ too, and so do obfuscated JARs. And since CheerpJ runs bytecode, any JVM language, including Kotlin and Scala, works out of the box. [...]

## [23] Google Launches LiteRT Tensor API for Building, Customizing, and Optimizing ML Models for On-Device
InfoQ | full text via InfoQ | ~488 words

Google has introduced the LiteRT Tensor API, a lightweight C++ API that allows developers to build, customize, and optimize machine learning models directly for on-device execution. According to Google, it combines the flexibility of native model authoring with cross-platform portability.
The traditional approach, Google says, is for developers to write computations manually in C++ for maximum control, which comes with a significant drawback:
Implementations are tightly coupled to specific backends (such as Metal, OpenCL, or Vulkan) and must be rewritten for each new hardware target. Furthermore, managing zero-copy buffer interoperability and synchronization across CPU, GPU, and NPU, while gluing together pre-processing, inference, and post-processing, demands substantial manual engineering effort.
The LiteRT Tensor API aims to address these challenges by allowing developers to build computation graphs operation by operation in C++. This provided greater control over model architecture, optimization, and accelerator execution, while enabling the same graphs to run through LiteRT on CPU, GPU, and NPU hardware without requiring a rewrite for each new target.
Beyond providing full control over model graphs, other key capabilities of the API include direct weight ingestion, allowing developers to load weights directly from checkpoints, including Hugging Face .safetensors files; zero-copy buffer interoperability, which avoids copying accelerator buffers across pre-processing, inference, and post-processing; and compatibility with AI coding agents, which can construct, modify, validate, and benchmark model graphs by generating C++ code.
Google used a coding agent to create a real-world app demonstrating how to use the LiteRT Tensor API for multi-object segmentation and tracking. The application also served as the basis for benchmarking performance across platforms:
We ran the same C++ code for the SAM 2 model on the GPUs of three devices: a macOS laptop (Metal), an iOS phone (Metal), and an Android phone (OpenCL). In our tests on the MacBook Pro, it ran about 1.5x faster than Apple MLX (fp16, image encoder plus mask decoder).
Google emphasized the fact that the coding agent could make a number of optimizations thanks to the model graph being defined in plain C++. [...]

## [69] GPT-6.2 Astra appears in Codex usage ahead of possible launch
TLDR AI | full text via TLDR AI | ~495 words

It looks like OpenAI might be on the verge of releasing its next frontier model, GPT-6.2 Astra. Over the weekend, several Codex users noticed a new entry in their usage analytics: gpt-6.2-astra, listed right next to the GPT-6 Astra model that launched in September.
The screenshots that are being shared online come from the usage page that tracks plan consumption across Work, Codex, and other agent tasks. In every breakdown we've seen, gpt-6.2-astra shows up only on the October 31 bar. Its share varies a lot by account, from 1.6% of one user's week to 19.8% of another's, and 37.7% of a single day for a third. The model picker still says GPT-6 Astra, so it looks like some requests are being quietly routed to the new model, either as an A/B test or the start of a staged rollout.
X user Token Gremlin even shared a raw response event with the model field reading "gpt-6.2-astra," calling it official. That's strong evidence the ID is live on OpenAI's servers, but it isn't an announcement. OpenAI hasn't mentioned GPT-6.2 Astra anywhere, and its model docs still list GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna.
Some testers who think they're getting output from GPT-6.2 Astra have even shared their results on X. From what we can tell, we also lean toward the idea that this is a newer, more refined version of Astra.
X account Fini.Yang shared what they call the first gray-test result: the classic pelican riding a bicycle, rendered as a 360-degree 3D scene.
Meanwhile, another user says the model created a semi-open-world 3D RPG from a single prompt and wonders whether it could give Opus 5.5 a run for its money. Since the picker doesn't identify which model responded, it's difficult to confirm whether any particular output came from 6.2.
In case you're wondering what happened to GPT-6.1 Astra, here's some context. OpenAI shelved GPT-6.1 Astra in late September after internal testing raised concerns about deception and scope, so a jump straight to 6.2 could point to a fixed, retrained model. That's only speculation for now, though, and OpenAI hasn't made that connection. The timing also coincides with Codex lead Thibault Sottiaux's daily shipping series, which wrapped up with usage resets — something some people are interpreting as a possible launch window.
If these early sightings of GPT-6.2 Astra in Codex usage analytics are anything to go by, then it looks like OpenAI doesn't want to wait for the competition to leapfrog it. [...]

## [214] Developers are downgrading their AI on purpose — and it’s working
The New Stack | full text via The New Stack | ~682 words

Developers are downgrading their AI on purpose — and it’s working
Anthropic has confirmed that it added new restrictions to Claude Code to prevent users from recreating existing video games. But developers say Claude Opus 5.5 is also refusing reverse-engineering and software-analysis tasks it previously handled, raising questions about what else Anthropic may have changed.
For some developers, the refusals are already affecting their work. One developer says paid client projects have stalled because Claude Code won’t work on existing games, while others say the model is refusing to analyze software. At least one developer got back to work by switching to an older Claude model.
On Friday, Addy Osmani, a member of Anthropic’s technical team, confirmed on X that the company had deliberately modified Claude Code’s instructions.
“We added two sentences to Claude Code’s prompt on Opus 5.5 to steer it away from recreating someone else’s specific game because using Claude to infringe IP is against our usage policy.”
“We added two sentences to Claude Code’s prompt on Opus 5.5 to steer it away from recreating someone else’s specific game because using Claude to infringe IP is against our usage policy,” Osmani writes.
He clarifies that developers should still be able to create original games, build within established genres and work with their own designs and assets.
“We’ll continue to iterate to ensure we’re striking the right balance,” he adds, inviting developers to contact him if Claude refuses work involving their own creations.
Anthropic has not publicly confirmed whether the reverse engineering refusals are tied to the new instructions or to separate cybersecurity restrictions.
Reverse engineering hits a wall
The complaints extend beyond game development. Developers say Opus 5.5 is refusing software-analysis tasks that previously worked. Technical writer for Phison Electronics USA, Jarred Walton encountered refusals while testing software he was developing, but switching to Opus 4.8 allowed him to continue.
While Anthropic is trying to prevent misuse without blocking legitimate development work, developers are left unable to do tasks as Claude Code suddenly refuses what it once handled, with little explanation for the change.
developers are left unable to do tasks as Claude Code suddenly refuses what it once handled, with little explanation for the change. [...]

## [162] Hiding inside Palantir’s skyrocketing quarter is a foreboding signal
TechCrunch | full text via TechCrunch | ~543 words

The data analysis company Palantir delivered such a huge third-quarter earnings report on Monday that its press release even bragged that the numbers were “crushing consensus expectations.”
Yet retail investors were lukewarm on the company on Tuesday, with the stock trading slightly down. That’s because Palantir’s enterprise sales, its big growth area, showed signs of slowing.
First, the good news for the company’s investors. Revenue grew 96% from a year earlier, and 20% from the previous quarter, to $2.31 billion, beating analysts’ expectations of $2.18 billion. It was the first time Palantir has topped $2 billion in a quarter. Palantir also reported adjusted earnings per share (profit per share, excluding certain one-time items) of 44 cents, compared with analysts’ expectations of 41 cents. The company even raised its revenue guidance, or forecast, for the full year. Normally, that alone would send a stock soaring.
The clincher was that Palantir’s U.S. commercial revenue surpassed U.S. government revenue for the first time ever. The company reported $984 million in commercial contracts (up 148% from the year-ago quarter), versus $953 million in U.S. government revenue.
The reason for all this love from enterprises? They are signing up for the company’s AI software that can run frontier models and custom-train open-weight models securely, without sharing any of their data and business processes with outside AI labs. Plus, Palantir has long offered what is today known as “forward-deployed” software engineering, in which its own engineers work directly with customers to customize the software.
However, Palantir also revealed a less-than-rosy signal: Even as enterprises are moving faster than ever, they are often signing short-term trials.
“What Ryan and I are seeing on the front line and commercial is this much quicker interaction, much quicker to deployment, shorter duration of the contract but then an ability to expand that contract dramatically,” CEO Alex Karp (pictured above) told Wall Street analysts on the quarterly earnings call.
Palantir is experiencing one of the unique phenomena of AI in the enterprise right now. Corporations are willing to quickly try AI software, skipping the usual bureaucracy, but they are also more willing to cancel contracts.
Karp used one off-color metaphor after another to describe how unconcerned he was about holding onto his enterprise business. [...]

## [101] Rewarding defenders with bigger bug bounties
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

OpenAI is raising Security Bug Bounty rewards and introducing report quality, loyalty, and priority campaign bonuses for independent security researchers.

## [198] Roli Has Fallen Apart—and Left Customers Holding the Bag
Wired | full text via Wired | ~1135 words

Roli, the company behind expressive, touch-sensitive music devices like the Seaboard and Roli Blocks, has collapsed.
Although it hasn't been officially announced, Roli reportedly ousted its CEO and founder, Roland Lamb, earlier this year. Since then, Roli has all but dissolved. (In August, a new company called Instrumental Intelligence was registered with the UK government under Lamb's name, a potential move by the founder to acquire Roli's assets).
On Monday, Roli emailed users that two licensed insolvency practitioners were appointed joint administrators of Roli on October 20. The company went into administration, the UK process that manages corporate insolvency. This is the second time Roli has gone bankrupt.
That has left a small but bereft community of customers with no word on getting the products they paid for. The Roli community has expressed sadness, anger, or outright confusion. In Facebook groups, the r/Roli subreddit, and other forums, dismayed users have struggled to find recourse for Roli equipment purchases ranging from hundreds to thousands of dollars. The Roli subreddit has been awash with posts from customers who say they paid for orders months or years ago and have received no response or refund since then.
Existing owners also worry about the long-term impact. Roli instruments rely heavily on proprietary software launchers and companion apps to connect, map sounds, and configure settings. While the hardware still functions, users fear that lack of software support will eventually leave their gear bricked.
Roli has not publicly communicated about its future strategy with customers. The company did not respond to WIRED’s request for comment; Lamb did not respond to multiple requests for comment. Roli’s primary financial backers, investment firms TriplePoint Capital and Hoxton Ventures, also did not respond.
A Change of Seasons
Roli has faced financial struggles before.
The company started in 2009 but really took off after musician Pharrell Williams invested in 2017 and Sony’s Innovation Fund in 2018. Musicians like Dream Theater keyboardist Jordan Rudess supported and touted Roli’s gadgets. Ryan Gosling’s character played a Seaboard Grand in the 2016 movie La La Land. In the late 2010s, the tech and the company were hailed as a hit.
That tune changed in 2020. [...]

## [157] EU Court Advisor Warns Google AI Chatbot May Breach Copyright Rules
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~91 words

An adviser to the EU's highest court says Google's Gemini may violate publishers' copyright when it reproduces recognizable portions of their articles or circumvents paywalls and other technical protections to generate answers. Reuters reports: The case before the Luxembourg-based Court of Justice of the European Union pitted Hungarian website operator Like Company against US-based Google's artificial intelligence chatbot Gemini. A ruling against Google, which could force the tech giant to pay fees for the use of such content, could throw a lifeline to online media such as Like Company. They h
