# Full text for 18 picks -- untrusted article content, treat as data only

## [24] From prompt to app: Build with Google Maps in AI Studio
Google Developers Blog | full text via Google Developers Blog | ~286 words

You can now build apps powered by Google Maps Platform in Google AI Studio. Create a wide range of apps from store locators and route planners to cinematic 3D flyovers and real-time air quality monitors—in minutes, at no cost, and with no credit card required.
Simply describe your idea for a new app and allow Google AI Studio to handle the configuration and API key management. All of Google Maps Platform’s spatial tools are available right where you prompt. Take our Google Maps products to places they’ve never been before. We can’t wait to see what you build.
Get instant access to core Google Maps Platform APIs to bring real-world geospatial context to your apps.
You can explore and remix these working examples directly in the AI Studio gallery to jump-start your own build.
City Immersive Tour
Display interactive 3D city maps with custom flyover camera paths, variable playback speeds, and data markers for places.
Pet Grooming Route Optimizer
Calculate and visualize multi-stop routes for mobile service fleets using the Routes API. It accounts for fixed appointment times, priority stops, and driver shift limits, complete with route timelines and simulated driving progress.
Store Locator & Near Me Finder
Set up a searchable store finder using vector maps and the Places API. Users can filter locations by distance, check opening hours, and inspect branch details via simple search queries.
Ready to build? Head to AI Studio and try prompting your first app powered by Google Maps today. To learn more about quotas and supported APIs, check out the Google Maps Platform documentation.
Try for free up to the daily quota limits. Quotas automatically reset daily (every 24 hours). Learn more. Paid Cloud billing account required for production.

## [23] On-Device Speech Recognition and Text-to-Speech in Google AI Edge Gallery
Google Developers Blog | full text via Google Developers Blog | ~883 words

Today, we are introducing on-device Automatic Speech Recognition (ASR) and Text-to-Speech (TTS) capabilities in Google AI Edge Gallery. Voice is often the most natural way to interact with AI on phones and wearables. Recent advances in compact speech architectures now make it possible to run accurate, multilingual ASR and expressive TTS models entirely on device, all within a small memory footprint, with low latency, and completely offline. By pairing these lightweight speech models with on-device small language models (SLMs) like Gemini Nano and Gemma 4, developers can build apps that stream live transcriptions as the user speaks and synthesize natural spoken replies locally.
This release brings together major advancements across both Google’s system speech models and the open-weight ecosystem:
Below, we’ll explore how this local voice pipeline powers the new XR (Extended Reality) Language Teacher showcase, upgrades AI Chat in Google AI Edge Gallery, and how you can build with these APIs and models today.
Learning a language while traveling happens in the real world, often in underground stations, busy markets, or abroad where Wi-Fi and roaming data may not be available. To show how vision, language, and speech models can work together 100% locally on your phone with no network connection needed, we built the XR Language Teacher showcase in Google AI Edge Gallery. Simply point your camera at an unfamiliar object or menu, ask "What is that, and how do I ask for one?", and immediately hear an explanation in your language alongside authentic pronunciation in the local language.
Link to Youtube Video (visible only when JS is disabled)
With inference running locally on a paired phone, the same experience works standalone on a phone and extends naturally to hands-free smart glasses. To see how we adapted Language Teacher for intelligent glasses check out our recent talk at Android Dev Summit: Building Audio-First Experiences for Intelligent Eyewear with Gemini Nano.
Beyond the XR Language Teacher showcase, we also built ASR and TTS directly into Google AI Edge Gallery’s main AI Chat feature, giving on-device SLMs like Gemini Nano and Gemma 4 a natural, offline voice interface while on the go.
While multimodal models like Gemma 4 can process audio inputs directly, we provide a modular solution for cascading language models with separate, lightweight voice models for latency optimization and flexibility. Depending on your target devices and model requirements, our open-source code on GitHub shows you the optimized and recommended solution for Android using ML Kit, as well as MediaPipe Tasks and LiteRT for cross-platform coverage and open model support. [...]

## [52] Web search for agents is here: Why ranking still decides the answer
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403; The New Stack: HTTP 403) | ~31 words

AI agents have had a URL problem for a while. When an agent needs current information but has no search The post Web search for agents is here: Why ranking still

## [54] nginx 1.31's json_set directive rejects a bad webhook payload about 13 times faster than forwarding it
Dev.to | full text via Dev.to | ~1343 words

A webhook receiver I built a few years ago always worked the same way: nginx took the connection, nginx forwarded the body, and the application decided whether the payload was junk. nginx 1.31.5 adds a module that lets nginx make that decision itself, by reading fields out of the JSON body before the request ever reaches a location block. I wanted to know what that was actually worth, not just what the changelog implied.
The module is ngx_http_json_module, built with --with-http_json_module (it's compiled into the official Docker image, but not into Ubuntu's 24.04 nginx apt package, which still ships 1.24.0). It adds one directive that matters, json_set, plus a depth limit. Alongside it, 1.31.5 also shipped predicate locations (location $variable) and client_body_early_read, which together let a location match be decided by the request body instead of only the URI.
I pulled nginx:1.31.8 (the current mainline patch, released 21 October 2026) and built the smallest realistic case: a webhook endpoint that only wants two event types, payment.created and payment.failed, and should reject everything else without bothering the application.
The setup
Old way, everything proxied through:
server {
    listen 18090;
    location / {
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_pass http://backend;
    }
}
New way, rejecting at the edge:
client_body_early_read 1;
json_set $event_type $request_body event.type;
map $event_type $is_invalid_event {
    "payment.created" 0;
    "payment.failed"  0;
    default           1;
}
server {
    listen 18091;
    location $is_invalid_event {
        return 400 "unknown event type\n";
    }
    location / {
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_pass http://backend;
    }
}
The backend is a small threaded Python server that parses the same JSON and returns 400 for anything that isn't one of the two valid event types, so both paths enforce the identical rule. I ran everything on loopback, no Docker network between containers, --network host so there's no extra hop to argue about.
What it actually saved
I sent 200 requests, alternating valid and invalid payloads, through each config and counted how many reached the backend:
Every single invalid request was turned away at nginx. The backend never saw it. That's the entire point of the feature in one table: it's not about nginx being faster at HTTP, it's about deciding which requests are worth a backend's time before spending any.
The headline number
At concurrency 1, no contention, I measured the time to reject (or round-trip and reject) 1,000 invalid payloads, three times each:
Averaged, that's about 1,874 req/s against 24,265 req/s — roughly 13 times faster to say no. [...]

## [138] How to Speed Up CI in the Age of AI-Written Code
freeCodeCamp News | full text via freeCodeCamp News | ~1642 words

Coding agents now write code faster than most CI pipelines can check it. In April 2026, GitHub COO Kyle Daigle said that his platform was handling 275 million commits a week, on pace for 14 billion in the year, up from about 1 billion in 2025. In the same post, he put GitHub Actions at 2.1 billion minutes in a single week, up from 500 million a week in 2023.
That second figure shows where all those commits end up: in CI. A 15-minute pipeline is tolerable if a dev pushes a few times a day. When an agent opens ten PRs in an afternoon, that pipeline turns into a queue. You wait for results, agents wait to retry, and the time saved writing code is lost checking it.
Most of that delay comes from a few causes, and each has a known fix. You can speed up CI in five ways:
- measure where the time goes
- cache what you can reuse
- run jobs on faster hardware
- split tests across parallel jobs
- skip work that doesn't need to run.
In this article, we'll walk through each fix in order. You’ll learn how to find the slowest steps in your GitHub Actions workflows, cache dependencies and Docker layers with stable keys, and move heavy jobs to faster runners. You’ll also see how to shard tests across a matrix of parallel jobs, and how to skip unneeded work with path filters, affected-only tests, and concurrency groups.
What We'll Cover:
Measure First, Then Optimize
Most teams try to guess which step is slowing things down, and they're often wrong. A job that feels like a test problem may be 90 seconds of installs and 30 seconds of tests.
Start with data you already have. GitHub shows job execution time for every run, with a timing for each step. Open the last ten runs of your slowest workflow and note the three longest steps. Use the median, not the worst case, since one slow run can be a network blip.
Also separate waiting from working. Queue time, setup time, and run time need different fixes. If jobs sit in a queue for a minute, no test tuning will help.
Cache Dependencies and Build Layers
The fastest work is work you never repeat. Every run starts on a fresh machine, so without a cache you download the same packages again and again.
The dependency caching reference explains how actions/cache works. You give it a path and a key. If the key matches a saved cache, the files are restored. If not, the step runs, and the files are saved when the job ends.
Everything depends on that key. The usual pattern hashes your lockfile, so the key changes only when your dependencies change.
- uses: actions/cache@v6
  with:
    path: ~/.npm
    # Key changes only when the lockfile changes
    key: npm-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      npm-${{ runner.os }}-
The restore-keys line is the part that tends to get skipped. [...]

## [143] Agentic search doesn't find pages, it assembles answers
Stack Overflow Blog | full text via Stack Overflow Blog | ~101 words

Agentic search doesn't find pages, it assembles answers
Ryan sits down with Jeff Wang, co-founder at EXA, to talk about the huge scale required to support trillions of agentic searches, the technical complexities of building custom embeddings and performant vector databases from scratch, and the need to dedupe the massive amounts of redundant content on the web to deliver high-trust answers.
EXA is a full search engine built specifically for AI agents, featuring custom extraction models and vector databases designed to handle complex, trillion-scale queries without the AI slop.
Connect with Jeff (through his triage agents) by emailing him at jeff@exa.ai.

## [70] Google turned to AMD Epyc, not its own Axion chips, to secure its first confidential TPU
TechRadar | full text via TechRadar | ~1174 words

Google turned to AMD Epyc, not its own Axion chips, to secure its first confidential TPU
The reason says a lot about where trust in AI hardware really lives
- Google's new TPU 8tx pairs TPU 8t silicon with 5th Gen AMD Epyc "Turin" hosts to deliver confidential AI inference
- The AI juggernaut passed over its own Axion CPU, which hosts the 8t and 8i, likely because its audited confidential stack is x86-only for now
- The confidential TPU joins a growing number of chips even as key security details remain unpublished, even as Google and Nvidia already offer confidential GPUs to cloud customers
Google has added two more systems to its eighth-generation TPU family, and the one built for confidential AI leverages a host processor Google didn't design.
The TPU 8tx, detailed alongside the dual-chip TPU 8i Max in a Google Cloud blog post, pairs Google's accelerator silicon with 5th Gen AMD Epyc CPUs.
AMD also announced that Epyc forms the host foundation for what both companies call the first cloud TPU system with hardware-enforced confidential computing.
The same chip with a new trust boundary in tow?
Google's April 2026 launch split its eighth generation hardware into the TPU 8t for training and the TPU 8i for inference. Google bills this as the first time it has introduced four TPU systems in one year, but as ServeTheHome points out, the two newcomers are system configurations built on existing chips rather than new designs.
As per Taiwanese outlet INSIDE, the 8tx inherits the 8t's 12.6 petaflops of FP4 compute and 216GB of HBM, but swaps in the lower-latency Boardfly network used by the 8i. Google claims up to 2x lower latency than TPU 8t with a near-zero performance penalty, and pitches the system at regulated enterprises and governments that want to fine-tune, distill, and train agents on private data without moving it between clusters.
AMD says Epyc handles orchestration, data preparation, and the high-throughput link to the accelerators. Its Secure Encrypted Virtualization (SEV) works with the TPU to extend the protected environment out to the accelerators, checking each one's identity and security configuration before granting direct access to protected memory
Prompts, model weights, and intermediate data stay encrypted in host memory and in transit, according to AMD, with hardware isolation while the TPU runs. Google, for its part, described the result as "keeping sensitive data and model weights protected and isolated even while in active use."
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
Skipping the homegrown solution?
Google hasn't directly said why it passed over Axion, the Neoverse V2-based chip it unveiled in 2024 as its first data center processor. [...]

## [102] Anthropic wants you to build on Claude. There’s a catch.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~20 words

Anthropic wants developers to build businesses on Claude, but its expansion into enterprise software is raising concerns among founders that

## [103] Basic Support For The Apple M5 Expected To Land For Linux 7.5
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~30 words

Very basic support for the Apple M5 SoC base model is expected to be merged for the Linux 7.5 kernel now that it's been queued into the "apple-soc/dt-7.5" Git branch...

## [125] KDE Plasma 6.9 Finally Allows XWayland To Run On-Demand, New Wobbly Windows Presets
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~22 words

This Week in Plasma is out with its latest issue following a week of exciting developments toward the KDE Plasma 6.9 desktop...

## [83] Manjaro Linux Moves Toward Independent Community Governance
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~95 words

Arch-based Manjaro Linux "has announced that Manjaro Project e.V. is now officially registered as a non-profit in Germany," reports Linuxiac, "and is therefore a legally separate entity from the commercial Manjaro GmbH & Co. KG... after months of internal wrangling over who was in charge of the project, who had access to the infrastructure and who didn't, and the relationship between the dev team and the commercial company..." The restructuring goes back to March, when the Manjaro developers released the Manjaro 2.0 Manifesto, which was a very public critique of the way Manjaro was being

## [149] Designing for Hot Keys: When Distributed Systems Stop Distributing
DZone | SNIPPET ONLY (DZone: HTTP 403) | ~91 words

Distributed systems usually spread data by hashing keys across nodes so no one node carries all the load. A hot key breaks that assumption. It is a key whose access volume greatly exceeds the volume of other keys during a given period. A global view counter or a popular item identifier can receive millions of reads or writes each second. Every request targets the same partition, even when the rest of the cluster has spare capacity. The result is uneven load. One node reaches its CPU , network, thread, or connect

## [17] Creating a self booting ZIP archive
Lobsters | full text via Lobsters | ~3207 words

So, after a debugging session the other day, I was having some shower thoughts regarding early userspace and initrd.
Linux initramfs supports unpacking CPIO, a stupid, simple, standardized format. In the discussion on whether to support TAR instead, much emphasize has been put on the fact that CPIO is standardized and less fragmented.
Luckily, Linux (the kernel) includes its own tool to produce the specific variant of the standard that it happens to implement. The standard CPIO tool is possibly the most cursed archiver under the SUN.
In the old DOS/WinDOS world, ZIP was probably the most wide spread and well known archive format, being displaced to some extend by the rise of RAR during the 2000s.
Because of the design of the format, ZIP lends itself to all kinds of polyglot trickery. Way back when, self extracting ZIP archives where a thing, EXE/ZIP polyglots that can be run and unpack themselves, which is useful if you don't have an archiver installed.
I don't think I need to explain where I am going with this, here is the resulting ZIP archive I built:
Download boot.zip
It is a completely normal ZIP archive, containing its own source code needed to build itself from scratch:
$ unzip -t boot.zip
Archive:  boot.zip
    testing: boot/ZIPHEAD.COM         OK
    testing: boot/MESSAGE.TXT         OK
    testing: common/asm.h             OK
    testing: common/multiboot.h       OK
    testing: common/zip.h             OK
    testing: multiboot/console.c      OK
    testing: multiboot/console.h      OK
    testing: multiboot/multiboot.c    OK
    testing: multiboot/string.S       OK
    testing: setup/a20.S              OK
    testing: setup/disk.S             OK
    testing: setup/entry16.S          OK
    testing: setup/entry32.S          OK
    testing: setup/mbload.S           OK
    testing: setup/mem.S              OK
    testing: setup/setup.ld           OK
    testing: util/fixhdr.c            OK
    testing: util/zipglue.c           OK
    testing: util/zippack.c           OK
    testing: mk.sh                    OK
    testing: README.txt               OK
    testing: MESSAGE.txt              OK
    testing: LICENSE.txt              OK
No errors detected in compressed data of boot.zip.
    A particularly interesting file here is boot/ZIPHEAD.COM, that contains executable code that is run when booting the archive.
You need to fix the execute permissions of mk.sh after unpacking, and you will need a copy of Zlib installed for the tools. Running mk.sh from it's directory should leave you with a fresh copy of the bootable ZIP archive. [...]

## [61] One Tool Call Instead of Four Pages: Adding WebMCP to My Site
Dev.to | full text via Dev.to | ~2184 words

This post is about how I added WebMCP to debbie.codes, how you can try it, and how it compares to the other ways agents read websites.
WebMCP lets a site offer tools in the browser, so an agent can ask the page a question and get a short, structured answer instead of reading whole pages and guessing.
I built it with Cursor cloud agents, coordinated by my Grok Bot site lead, and I reviewed and merged the changes. It already runs for real visitors in Chrome and Edge.
Prefer to watch? Here's the video, where I show the tools in the Chrome DevTools WebMCP panel.
What is WebMCP
WebMCP is a proposed web standard. A page registers tools with the browser. Each tool has a name, a description, a JSON Schema for its inputs and an execute function. An agent working in the browser can then find those tools and call them, instead of clicking around and reading the page. On my site that's document.modelContext.registerTool(). Older examples use navigator.modelContext, but the spec puts it on document now. Playwright's WebMCP docs still use navigator.modelContext. You can read more in the Chrome WebMCP docs.
A few things worth knowing:
- It's being worked on in the W3C Web Machine Learning Community Group. There's an explainer and a draft spec.
- There are two ways to add tools: an imperative JavaScript API, which is what I used, and a declarative API using HTML forms.
- WebMCP doesn't replace MCP. MCP (Model Context Protocol) is an open-source standard for connecting AI apps to external systems. Chrome describes MCP as the backend and WebMCP as the frontend. An MCP server works anywhere, while WebMCP tools only exist while the page is open in a tab. Chrome explains the difference in WebMCP vs MCP.
- Right now it's available through an origin trial, in Chrome from version 149 and in Edge. An origin trial gives a site access to a new or experimental feature for a limited time, using a trial key from the browser. For local work Chrome has a flag, chrome://flags/#enable-webmcp-testing.
- Chrome's docs say it's mainly meant for when a person is there in the browser with the agent, not for scripts that drive a browser with no one watching. Agents also have to visit the page to discover its tools.
Why I wanted it
My content is spread across videos, blog posts, podcasts and courses, each with their own tag pages. When an agent browses my site for someone, it needs a reliable way to answer "what has Debbie done on this topic?".
Videos are the richest part, and the best answer is often "minute 29 of this talk". No page on my site shows that.
What an agent gets from it
When I tried my videos page with ChatGPT, it listed what the tools gave it compared to reading the page. I checked each point against my code:
- 
Precise filters. [...]

## [7] LinkedIn, Monster take down over 1000 fake job postings after CBC investigation
Hacker News | full text via Hacker News | ~1403 words

Canada·CBC Investigates
LinkedIn, Monster take down over 1,000 fake job postings after CBC investigation
Actual opportunity required monthly subscription and incentivized recruiting others
More than 1,500 misleading job postings — offering remote work, no experience needed — have been taken down from LinkedIn and Monster after a CBC visual investigation revealed the listings funnelled unsuspecting applicants to a multi-level marketing (MLM) company that asked for money.
CBC connected a network of travel-related pages posting suspicious jobs — positions like "Work From Home Travel Planner and Virtual Customer Support Representative" — to a U.S.-based MLM called Evolution Travel. Some of the roles promised to pay up to $75,000 US per year.
In reality, there was no job and no salary.
Applicants were quickly directed to join virtual information sessions, where they were asked to pay hundreds of dollars up front, followed by a monthly subscription fee. The program promised to teach members how to make money from booking travel as an independent agent and recruiting others into the program, taking a cut of their commissions.
The companies went by names like Wanderwell Collective, Professional Travel Hub, Remote-Careers, Sky Land & Ocean Travel and Sunkissed Getaways.
The job postings made no mention of Evolution Travel or sign-up fees.
Many of the jobs did not require experience and promised to pay up to $75,000 US. (Illustration: Matthew Hoddy/CBC; LinkedIn)
"This is disgusting," said Jay Jones, a Chicago-based job listing investigator who CBC shared its findings with. "They catch you with the lure of the fake job. The money is great, [successful applicants] get to stay at home. You have to pay to get work — that's not how work works."
Misleading job postings — including ones that require payment or lead to MLMs — are strictly prohibited on platforms like LinkedIn and other job sites.
Jay Jones investigates misleading and fake jobs online. (CBC)
"It feels in so many ways that we're living in a funhouse mirror," said Vass Bednar, managing director of the Canadian Shield Institute, a public policy think-tank that focuses on economic resilience and digital sovereignty.
These postings risk "eroding confidence — confidence in the self and confidence that there is, frankly, meaningful work out there for people that is worth pursuing."
Jobs were 'misleading': LinkedIn
MLMs are not illegal in Canada or the U.S. However, in the U.S., companies and individuals could face fines if they are found to violate the U.S. [...]

## [48] Shield helps technicians hand off legacy portal work with OpenAI
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~27 words

Shield uses OpenAI to help IT technicians hand off work in legacy portals. Its Forge agents navigate systems so technicians can focus on issues needing their judgment.

## [47] Podcast: Doing The Right Thing: Accountability In The Age Of AI Coding Summary
InfoQ | full text via InfoQ | ~4232 words

In this podcast, Shane Hastie, Lead Editor for Culture & Methods, spoke to Hugo Venturini about who is accountable when AI writes the code, how AI is reshaping code review and traditional engineering roles, and how leaders build a culture of transparency and psychological safety.
Key Takeaways
- AI is a powerful tool, but humans remain accountable for the decisions it makes possible and the code it produces.
- Pull requests have been growing for years; AI didn't create the review-scale problem, and teams should apply the same trust-based judgement about what needs reviewing that worked before AI.
- Merging the software engineer and tester roles at Microsoft in 2014 raised quality by making engineers accountable for the whole product — AI risks reversing that gain if people blame the tool instead of owning outcomes.
- AI collapses traditional role boundaries (PM, architect, tester), pushing engineers to ask better questions — a skill that defines seniority and that organisations need to deliberately teach.
- Cultures of transparency — honest no-blame Q&As, anonymous questions, naming solutions rather than people — let people dare to take accountability, and this can start at any level of the organisation, not just the top.
Subscribe on:
Transcript
Shane Hastie: Good day, folks. This is Shane Hastie for the InfoQ Engineering Culture Podcast. Today I'm sitting down with Hugo Venturini. Hugo, welcome. Thank you for taking the time to talk to us.
Hugo Venturini: Thank you, Shane, for having me.
Shane Hastie: Now, we are sitting in opposite sides of the world. I'm in New Zealand and you are somewhere in Europe.
Hugo Venturini: Yes, right now I'm in Spain, in Valencia.
Shane Hastie: Nice. You've got a beautiful warm summer. I'm sitting in a pretty cold winter, but we'll get past that. My normal starting point with these conversations is, who's Hugo?
Hugo Venturini: So I'm a software engineer. I defended my PhD on the debugging of optimized code in 2008. And after that, I joined the industry as a software engineer and I climbed the ladder one step after the other. Senior then manager. I was a manager at Meta, Facebook at the time. I was accountable for the type checker and the compiler of the hack language. Eventually I decided to try to create my own company, grew it, then joined another organization, was the CTO of Qwant, the search engine, 90 people in the organization from network engineers to AI researchers. And right now, I work in a software company, startup company that deals with tooling for AI, to help AI do the right thing, so to speak.
Defining "The Right Thing" With AI [01:58]
Shane Hastie: The right thing. [...]

## [16] Solving the fox game
Lobsters | full text via Lobsters | ~2085 words

Christoffer Stjernlöf posted about the Fox Game, an old Norse asymmetric board game (seemingly also called “halatafl”) where twenty sheep try to outsmart two foxes and get to the other side. His AI uncovered some interesting insights, but left the question open as of whether the foxes or the sheep actually win with perfect play (the general sentiment in his family was that winning with the foxes was easy). This was too tempting for me to leave on the table, so I set out to make a strong solve.
Since I don't know this game myself, I've stayed with the rules he describes even when they differ from e.g. Wikipedia (in particular, I do not use forced fox jumps, or multi-jumps); the only real change is that I don't have a 40-move draw rule, any position that is a forced win for one of the sides would be a win no matter how long it would take. (I consider this just an implementation detail in his AI, although morally, I consider a draw a loss for the sheep.) You might want to read his post to get the full rules, because I'm not going to repeat them here.
The results first: The sheep win with perfect play, even with only 19 sheep (remove one on the flank), or 18 if they are allowed to go first. Even with only 9 sheep (the minimum possible that isn't an instant win for the foxes), the sheep can force a draw right from the start. With one fox, 11 sheep suffice for a forced win. (The draw margin is seemingly so large because one fox can just camp in the last spot in the pen, and it's hard to force it away without getting harassed by the other fox, unless you have lots of sheep.)
The rest is about the implementation. I'll skip over a lot of wrong turns, and unsurprisingly, there were a lot of bugs to iron out, but hopefully, it got to a good place in the end. :-) I started out trying to make something very simple, and it worked for the first few cases, but then things got more complicated than I would have liked in the end. Still only at ~1000 lines of code, though, with no dependencies.
Board representation
The board has 33 squares. I tried a few different ways of represent the state of the game, and ended up on a simple bitboard representation: There's a 64-bit bitmap representing where there are sheep, and another bitmap representing where there are foxes. Since there's plenty of room in there, I use a spare bit to represent side-to-move. This is compact (which mattered a lot earlier on, but not as much later), easy to iterate over, and has little redundancy, so it's easy to keep valid. You need fast 64-bit population count and bit-scan instructions, but a) that's common now everywhere, and b) I decided fairly early that I wanted to require BMI2 anyway.
The bit order mostly doesn't matter; I just started at top-left and went from there. [...]
