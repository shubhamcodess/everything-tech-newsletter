# Full text for 28 picks -- untrusted article content, treat as data only

## [56] Anthropic IPO raises over $81 billion in largest offering on record, topping SpaceX
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~58 words

Anthropic sold about 980 million shares priced at $83 per share at its IPO on Wednesday. The AI lab raised $81.3 billion and now has a fully diluted market cap of around $1.5 trillion. The stock is expected to begin trading on the Nasdaq on Thursday under the ticker symbol 'ANT'. OpenAI's IPO will likely debut in 2027.

## [3] UK government forced to admit it issued Apple a secret encryption order
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [152] JPMorgan, Visa, Mastercard Disclose Cyberattack On Third-Party Vendors
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~84 words

JPMorgan Chase, Visa and Mastercard have disclosed cyberattacks involving third-party service providers that exposed customer marketing data, including names, email addresses and, in some cases, phone numbers and postal codes. All three companies said their core systems or payment networks were unaffected, while JPMorgan emphasized that the incident was unrelated to the banking disruptions earlier this week. Reuters reports: A cyber extortion group called "n0n" claimed on November 16 to have obtained cardmember engagement records that included "hundreds of thousands of campaign interactions fo

## [7] Ruby2ßhell: Pre-authentication RCE on stock Rails
Hacker News | full text via Hacker News | ~376 words

ruby2ßhell
Ruby2Shell is a one-byte heap overflow to remote code execution in Ruby's string case conversion. Reachable without authentication in the default configuration of common Ruby web frameworks and self-hosted software.
- Severity
- Critical
- Fixed in
- 3.3.14, 3.4.13, 4.0.10
- Access needed
- Network, no authentication
Affected software
Ruby versions
Frameworks
The bug is reachable from the following frameworks in their default configuration. Other frameworks are not exposed by default, but application code that upcases strings received in a legacy encoding may also be vulnerable.
Self-hosted software
These products bundle their own Ruby, so the fix has to come from the vendor. Products marked Vulnerable have no fixed release yet: every current version is vulnerable.
Updated .
Remediation
Your deployment
Upgrade Ruby to a fixed release: 3.3.14, 3.4.13 or 4.0.10.
Self-hosted software
Install the vendor's fixed release. See Self-hosted software for fixed versions of popular products.
Technical details
Root cause
Most of Ruby's single-byte encodings have no capital
ß. Upcasing it writes two bytes, SS, but
              the loop only bounds-checks one (to < to_end).
The output buffer is allocated as the input length plus 20
              bytes. Each ß adds one byte to the output, so an
              input with 21 of them overflows the buffer by one byte.
The same loop is in several ISO-8859 and Windows-125x encodings
              and has been there since Ruby 2.4.0. It is reached by
upcase, swapcase,
downcase(:fold) and casecmp?.
UTF-8 strings take a different code path and are not affected.
Fixed upstream in
ruby/ruby@d582f8f.
Primitive
A one-byte heap overflow. The byte written is S
(0x53) when upcasing or s
(0x73) when case-folding, and it lands directly
              after the output buffer. The attacker controls the size of the
              buffer through the input length.
Copying the result out of the buffer then reads one byte out of bounds.
Proof of concept
We'll be publishing a proof of concept demonstrating remote code execution on stock Rails on , or later if major vendors have not shipped a fix by then.
Credits
Veria Labs found this vulnerability independently and was the first to demonstrate remote code execution.
The Ruby security advisory also credits Stephan Lipp (Ada Logics) and Anthropic with reporting the underlying primitive. Additional discoverers include Moritz Sanft in collaboration with OpenAI.

## [10] PostgreSQL 19 Released
Simon Willison's Blog | full text via Simon Willison's Blog | ~386 words

19th November 2026 - Link Blog
PostgreSQL 19 Released (via) Most years PostgreSQL ships a new release in September, but this year's release came two months later thanks mainly to the flurry of issues that the PostgreSQL team needed to address as part of the ongoing AI-reported vulnerability apocalypse.
This release was definitely worth the wait. My favorite new feature is this one:
For applications that send reads to standbys, PostgreSQL 19 adds "read-your-writes" consistency with the new WAIT FOR LSN command. A session on a standby can use WAIT FOR LSN to wait until the standby has replayed the write-ahead log (WAL) up to a specific log sequence number (LSN) before running a query, so the application can read data it just wrote on the primary.
In practice, that looks like this:
UPDATE movie SET genre = 'Dramatic' WHERE genre = 'Drama';
SELECT pg_current_wal_insert_lsn();
That returns a value like 0/0306EE20. Store that somewhere (a signed cookie would work) such that on a subsequent request your application can do:
WAIT FOR LSN '0/0306EE20' WITH (TIMEOUT '0.1s');
SELECT * FROM movie WHERE genre = 'Drama';
The timeout is optional - if you provide one you'll get an error if the replica you are talking to doesn't catch up within the specified time.
I first encountered this pattern in Wikipedia, which has a hand-rolled version of this built against MySQL replication:
In addition to this, MediaWiki attempts to ensure that the user sees events occurring on the wiki in chronological order. A few seconds of lag can be tolerated, as long as the user sees a consistent picture from subsequent requests. This is done by saving the primary binlog position in the session, and then at the start of each request, waiting for the replica to catch up to that position before doing any reads from it.
Here's the relevant MediaWiki code, which these days uses MySQL's WAIT_FOR_EXECUTED_GTID_SET() function and falls back to SOURCE_POS_WAIT().
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026

## [4] How the European Commission rolled out Matrix to more than 40k staff
Hacker News | full text via Hacker News | ~96 words

Element
             
              Neil Johnson
             
              Matthew Hodgson
             
              Panel discussion
             
              Marco Holz, Patrick Weber, Kenneth Edwall, Amandine Le Pape, Mathieu Velten
             
              DINUM, NATO, European Commission, Försäkringskassan, Schleswig-Holstein
             
              Mathieu Velten, Kenneth Edwall, Jeroen Franssen, Sven Thomsen, Fabien Marathée
             
              Patrick Maier
             
              European Commission
             
              Alexandru Vignide, Diana Gheorghe
             
              UNICC
             
              Sameer Chauhan
             
              adesso
             
              Franziska Streidt, Oliver Graml
             
              Försäkringskassan
             
              Kenneth Edwall, Cecilia Spiik
             
              Access Now
             
              Marcel Kolaja
             
              Midhun Suresh R, Kieran Lane
             
              Timo Kandra, Robin Townsend
             
              Forrester
             
              Dario Maisto
             
              David Langley, Half-Shot
             
              RISE
             
              Richard Schlögl
             
              Dutch Ministry of Defence
             
              Manfred Zielinski, Gideon Bleumink
             
Interoperable, sovereign and secure communications, built on the Matrix open standard.

## [13] Google will launch Android app verification requirement globally in January 2027
Ars Technica | full text via Ars Technica | ~309 words

Google announced Android developer verification last year, and despite numerous objections from developers and users, the company is forging ahead. It began blocking the installation of unregistered apps in some countries this fall, and the system is expanding globally soon. Google says it will start rolling out the requirement in all regions in January 2027, and it urges devs who still haven’t registered their apps to do so soon.
The apps you download from the Play Store all come from verified developers, and Google’s new requirement expands that requirement to apps from third-party sources. Once developer verification is live in your region, you won’t be able to sideload apps unless the developer has registered with Google, which is framed as a security measure. Verification requires providing government identification and paying a $25 fee, which will allegedly make it harder for nefarious actors to distribute malware and scammy apps.
In September, Google launched verification in Brazil, Indonesia, Singapore, and Thailand. Apparently, nothing exploded, so the company is now ready to expand. It previously said verification would go global in 2027, and it’s not wasting any time with the January start. It says that verification will reach all devices within “several months.”
So far, Google is getting what it wanted from this initiative, with “millions” of non-Play apps already registered. The company says this accounts for more than 99 percent of global Android app installs.
The verifier system service has already been rolled out to Google-certified devices running Android 8 Oreo or higher, which accounts for just about every Android device in the world outside of China and Russia. Google has also partnered with the biggest third-party app stores to enforce verification: Galaxy Store, Honor, Oppo, Xiaomi, Transsion, and Vivo. The system-level verifier is responsible for blocking installs, but these stores will only list verified apps once Google flips the switch.

## [5] Claude solves two open problems in the physics of black holes
Hacker News | full text via Hacker News | ~4621 words

Claude has solved two open problems in theoretical physics. Both concern black holes and the search for a theory of quantum gravity. In the first, it completed a calculation that physicists set up more than 20 years ago, but which had never been solved. Claude’s result showed that a sudden transition associated with the formation of black holes persists even where spacetime no longer has a definite shape. In the second, Claude found the exact limit of the simplest version of a technique used to test candidate theories of quantum gravity. This post explains both findings, first in plain terms and then in more technical detail. The preprints are available here and here.
Introduction
Modern physics rests on two frameworks: general relativity and quantum mechanics. General relativity describes very large things, like stars; quantum mechanics describes very small things, such as atoms. Both are astonishingly good at predicting how the universe behaves, but they’re mathematically incompatible. Finding a theory that unites them—“quantum gravity”—is one of the field’s biggest goals. Black holes are a natural testing ground, because they’re one of the few areas where both relativity and quantum mechanics matter—they pack immense mass into a very small space.
One of the most useful tools for studying quantum gravity is called holographic duality. The real universe has three dimensions of space and one of time, which relativity combines into four-dimensional spacetime. But physicists studying quantum gravity often work with simpler model universes that they can understand in more detail.
The basic idea of holographic duality is that some of these theoretical universes can be described in two ways: as a complete universe with gravity and spacetime, and in quantum terms, with no gravity at all, “written” on the universe’s outer boundary. Just as a real hologram encodes a 3D image on a 2D plane, the quantum model encodes all the information of the universe in one dimension fewer (a universe with four dimensions of space, for instance, can be fully described by a quantum theory with three). This lets physicists turn hard questions about gravity into questions about quantum physics, which are sometimes easier to answer.
The first problem Claude solved concerns what happens when you heat up one of these theoretical universes. At low temperatures, the universe fills up with a gas of particles. Above a certain temperature, a black hole forms instead. In 1983, Stephen Hawking and Don Page showed that this switch is abrupt: it’s a phase transition, similar to how water suddenly boils at 100°C. [...]

## [9] Distributed, high-performance blob storage on SQLite
Hacker News | full text via Hacker News | ~2718 words

TLDR; We built Blobasaur, a sharded, distributed, lightweight blob storage server on top of SQLite to solve our high-throughput blob read/write usecase. JSON blobs varying from a few KBs to MBs are now written and read thousands of times per second on commodity hardware while maintaining single-digit millisecond latency.
On Kite, our trading platform with ~20 million customers, users are able to customize their investment and trading screens heavily. They save multi-chart layouts, financial indicator templates, vector drawings, and various kinds of arbitrary UI preferences. In addition, we offer a Terminal mode that allows users to design their own workspaces by dragging, dropping, and customizing widgets. Under the hood, our backend services store these user preferences and metadata as opaque blobs (mostly JSON) ranging from a few kilobytes to several megabytes.
Many years ago, we stored such blobs in CouchDB, which turned out to be ill-suited for the kind of throughput we were starting to see. We then moved to SSDB (ssdb), a C++ disk-backed store that speaks the Redis protocol. This made it very easy to integrate as well. SSDB solved our immediate performance problems and ran reliably in production for several years.
Over time, two problems forced us to look for a replacement:
- SSDB became unmaintained, which was an obvious operational risk. It is written in C++, which is not a part of our stack or expertise, so forking and maintaining was also not viable.
- Scaling and size limits. SSDB is not a distributed system and can only run on a single node. This imposes significant future scaling challenges, including at one point forcing us to cap blob sizes at 1 MB because latency degrades on larger payloads.
As we added features like the Terminal mode and onboarded more internal services, we needed a robust solution. Our criteria were:
- A key-value blob store with a simple API.
- Designed for multi-megabyte blob read/write ops and high throughput. We sustain loads of thousands to tens of thousands of requests per second reading and writing arbitrary blobs. These are unpredictable and bursty thanks to the volatility in stock markets.
- Horizontally scalable, distributed.
- Disk-space efficiency / compression.
- Easily maintainable and highly economical.
So we investigated FOSS databases optimized for high-throughput blob storage and looked at the following:
- ScyllaDB: We already run ScyllaDB for high-throughput workloads, but in our tests, it turned out to be suboptimal for large blobs. Significantly lower throughput and higher resource usage. We specifically want multi-megabyte blobs. [...]

## [60] AWS announces ExtendDB 1.0
TLDR Tech | full text via TLDR Tech | ~148 words

AWS announces ExtendDB 1.0
Today, Amazon Web Services (AWS) announced version 1.0 of ExtendDB, the first release of the open source Amazon DynamoDB-compatible adapter for production use. ExtendDB is fully compatible with the DynamoDB API and runs on a database backend that you choose, so developers and infrastructure teams can run DynamoDB workloads in on-premises data centers, in private or public clouds, and at the edge without rewriting application code.
ExtendDB 1.0 supports four storage backends, PostgreSQL, SQLite, Cassandra, and MongoDB. For local development and continuous integration (CI), the extenddb-dev container image and the @extenddb/dev npm package run a DynamoDB-compatible endpoint over SQLite, so you don’t have to set up an external database.
ExtendDB is maintained by AWS, released under the Apache 2.0 license, and developed in the open on GitHub. To learn more, see the ExtendDB project page. To get started or contribute, visit the GitHub repository.

## [34] 15 million web servers on one VM - smoltcp, DPDK, AF_XDP
Lobsters | full text via Lobsters | ~2959 words

15 million web servers on one VM - smoltcp, DPDK, AF_XDP
Put a web server online and everyone starts trying to hack it. Why? A basic rule of economics. Short supply, big demand - there aren’t enough web servers for everyone. Let’s run a web server for every human on the planet, all 8 billion of them. I couldn’t get funding, so we’re bootstrapping. The goal is to run 15 million web servers on one VM with 10GB of RAM and 1 CPU core. If we succeed, I’ll find some RAM from old microwaves around the house and we’ll scale it up so everyone can have their own web server. Demand will drop to zero and cybersecurity will be solved once and for all.
Web server
Instead of vibe coding it all, let’s use an ancient technique called learning. First of all, what is a web server? There are a few essential syscalls.
- listen - syscall, asks kernel to listen for connections on a socket
- accept - syscall, accepts a connection on a socket
- recv - receives data from a socket
- send - sends data
- close - closes
What is a syscall? A function that is executed by the OS kernel. Whatever fancy language or library you use for HTTP, it all comes down to those syscalls (well, yes, but actually no). Let’s use C to make it all explicit. We start listening, then read from the socket in a loop and always reply with OK.
int main(void)
{
    // We use port 0 which makes OS return any available port
    int server = socket(AF_INET, SOCK_STREAM, 0); 
    if (listen(server, 128) < 0)
        return 1;
    const char reply[] = "HTTP/1.0 200 OK\r\nContent-Length: 2\r\n\r\nOK";
    for (int client; (client = accept(server, NULL, NULL)) >= 0;) {
        if (recv(client, NULL, 4096, MSG_TRUNC) > 0)
            send(client, reply, sizeof reply - 1, MSG_NOSIGNAL);
        close(client);
    }
}
It couldn’t be simpler: listen on a socket, accept a connection, read the data, send a reply, close the client connection, and repeat. It gives us around 65k RPS. Now that we’ve learned everything, let’s finish the article and call it a day:
$ for i in $(seq 1 15_000_000); do echo $i; ./server &; done
...
...
28232
program exited with error 1
Hm, why did listen fail? Ah, we’ve run out of ports! We’re using port=0, so the kernel picks an available port from ip_local_port_range.
$ sysctl net.ipv4.ip_local_port_range
net.ipv4.ip_local_port_range = 32768    60999
Why are so many ports skipped? Historically, port 0 was created for outbound connections. When you call connect('example.com', 80), Linux connects to the remote server (the sending part) and then allocates a random port on the host from ip_local_port_range to receive data (the receiving part). [...]

## [44] Discord Rewrites Desktop and Mobile Clients in Rust Using Zed's GPU-Accelerated Rendering Framework
InfoQ | full text via InfoQ | ~671 words

Discord’s CTO Stanislav Vishnevskiy recently announced rewriting its desktop and mobile clients in Rust, moving away from Electron and React Native. The project (codenamed Phoenix) eliminates layers of abstraction to directly leverage the device’s GPU, native mobile views, and a Rust core shared across platforms. Early results hint at a significant reduction in RAM usage and boot time for chat, voice, and streaming.
Vishnevskiy expanded on the rewrite on X:
We’ve been early adopters of Rust since 2018 and a lot of our infra, voice tech, and even some of the current client is already Rust, the holy grail was getting the whole client there. That means Electron goes away, and so does React Native, mobile keeps native UI but shares app code with desktop via Rust. We hope to get it into testing with users soon™. (And it’s not Tauri, it’s GPUI, so good guess everyone.)
The desktop app thus drops Chromium/Node.js for GPUI, the open-source, GPU-accelerated Rust UI framework built by the Zed team for the Zed editor. Zed is an open-source code editor written in Rust for macOS, Linux, and Windows by a team including the creators of GitHub’s Atom code editor, which was sunsetted in 2022, four years after Microsoft’s acquisition of GitHub. Zed touts a narrow focus on performance and user (i.e., developer) experience:
VS Code won by being good enough for everyone. Zed wins by being excellent for developers who refuse to compromise on speed.
Discord’s mobile app rewrite drops React Native, instead directly leveraging native iOS and Android views and reusing a common Rust core.
The browser client keeps rendering HTML with the application logic layer compiled to WebAssembly. Embedded web surfaces (e.g., YouTube videos and Activities), however, invoke an OS webview, with Electron’s built-in browser no longer available.
Vishnevskiy signals decreasing RAM usage, startup time, and latency as key motivations behind the rewrite:
The new Discord client using less RAM is just part of the story. Clicking around feels instant, I can’t go back. Check out the boot time.
Early internal builds for the desktop app reveal RAM usage at around 290 MB (measured with two accounts logged in simultaneously) and a near-instant cold start versus 5.5 s on Electron.
Vishnevskiy showcased similar improvements on mobile with a load time under 2 seconds for the rewrite versus approximately 5 seconds for the legacy app.
Elias Floreteng, in his master’s thesis at KTH this year (An Empirical Study of React Native’s New Architecture), reported performance gains across several metrics for native Swift and Kotlin over React Native, even with its new architecture. [...]

## [190] PHP 8.6 Released With Partial Function Application, Other New Features
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~25 words

Following today's PHP 8.2.36, PHP 8.3.37, PHP 8.4.28, and PHP 8.5.13 security releases to address multiple security issues, PHP 8.6.0 made its official debut today...

## [160] PHP Readies Critical Security Updates to Patch Another RCE Flaw
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~84 words

PHP has released security updates addressing seven critical remote code execution (RCE) vulnerabilities across its supported versions, just four weeks after patches for the widely exploited PHP2Shell flaws. SecurityWeek reports: One of the security defects expected to be resolved is CVE-2026-115560, a remote code execution (RCE) defect in the file-upload progress tracking functionality. The vulnerability was publicly disclosed two days after PHP2Shell made headlines. PHP's maintainers warned at the time that the security flaw can be triggered only under an unusual combination of configuration

## [42] NetWasm 0.10 Speeds Up C# on WebAssembly, Now Faster Than Mono AOT
InfoQ | full text via InfoQ | ~645 words

The team behind NetWasm has published a write-up of its 0.10 optimisation work, spanning releases 0.10.1 to 0.10.8. The changes touch exception handling, array bounds checks, WebAssembly SIMD and integer division. On the project’s own benchmark set, NetWasm now comes out ahead of Mono AOT and gets close to desktop .NET on some workloads.
NetWasm is a compiler and runtime that compiles C# programs ahead of time into small, standalone WebAssembly files. It takes the IL that Roslyn produces and emits Wasm, using its own runtime and a CoreLib ported from .NET. The yardstick is the Mono AOT build for WASI, which runs .NET on the same engine. A new garbage collector had already put NetWasm in front on allocation-heavy code, but plain loops were still slower: a quicksort of 100,000 integers took 77.2 ms, against 58.0 ms for Mono AOT.
Much of the early gain came from exception handling in 0.10.1. Wasmtime adds extra register save-and-restore code around any function that can throw or catch, floating-point registers included. Methods with null, bounds or checked-arithmetic checks paid that price on every call. Throws now go through a shared function and the catching handler releases the frames, which cut UI churn from 17.6 to 7.9 ms.
Version 0.10.2 inlines small straight-line methods in loops, tuple swaps included, and skips checks already performed on the same array and index. The quicksort fell to 54.0 ms. DoomSharp, a C# software renderer for Doom that ships a NetWasm build, served as a second test case. Value-type accessors now compile to plain field loads, and at O3 small branching helpers are inlined inside loops. Together these brought a 120-frame render from 3,595 down to 1,934 ms.
SIMD arrived in 0.10.7. Vector128, Vector<T> and PackedSimd lower to 128-bit Wasm instructions, and element-wise array loops handle four or more elements per iteration, with a scalar fallback. Hoisting loop-invariant Math calls allowed a solver for Burgers’ equation, a fundamental partial differential equation from fluid mechanics, to vectorise: its first test dropped from 497 ms to 71 ms, against 186 ms for Mono AOT and 93 ms for desktop .NET.
Version 0.10.8 targets division and range-checked arithmetic. A remainder that follows a division now reuses the quotient and skips repeated zero-divisor and int.MinValue / -1 checks. A trial-division test fell from 1,376 to 765 ms, while Mono AOT needed 862 ms.
Across the 2,213 cases, 0.10.8 at O3 with NetWasmGC takes 0.41 times Mono AOT’s time as a geometric mean, excluding five cases where Mono’s LLVM removes the work. Against desktop .NET 11 RC3 JIT the ratio is 0.87, down from 2.15 for 0.10.6. [...]

## [162] LLVM Effectively Completes Its Relicensing After Nearly A Decade Of Work
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~80 words

Back around 2017 an effort began to work on re-licensing all of the LLVM code under the Apache 2.0 license with exceptions, moving away from their prior 3-clause BSD-like "LLVM license". Prior updates on the topic included LLVM Developers Are Still Working On Their Massive Relicensing Effort (2018) and then LLVM Is Still Working On Relicensing, Needs Help Locating Some Past Contributors (2021)... Now finally as we approach the end of 2026, this re-licensing effort has been deemed effectively complete...

## [174] Palo Alto Networks Signs $4.5 Billion Deal For Applied Compute
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~90 words

Palo Alto Networks has agreed to acquire AI startup Applied Compute for $4.5 billion as it expands beyond traditional cybersecurity into securing enterprise AI systems, including the training and deployment of open-weight models. The deal is expected to close in the third quarter of fiscal 2027. Reuters reports: Palo Alto Networks has been repositioning itself as an integrated cybersecurity provider, with recent deals, including its $3.35 billion acquisition of cloud management and monitoring firm Chronosphere and an agreement with Israeli startup Koi. The company is looking to tap growing cyb

## [67] Why Antigravity Eats Weekly Quota Fast - and What I Measured
TLDR AI | full text via TLDR AI | ~2353 words

Why Antigravity Eats Weekly Quota Fast - and What I Measured
Last updated: Nov 19, 2026
Gemini 4 Hydrogen, Gemini 4 Argon, and hy4-flash via OpenCode used for the binary reverse engineering, empirical cache probing, and keep-alive tooling.
Introduction
Greetings! If you use Google Antigravity (agy) with the big frontier models, you have probably noticed how fast your weekly quota disappears during normal coding sessions [1, 4].
My suspicion was simple: a short prompt-cache lifetime. When you are coding with an agent, you don’t send messages every 10 seconds. You wait for a response, read the diff, run a test, think for 5 minutes, and then send your next prompt. If the prompt cache expires during that 5-minute pause, your next message has to re-ingest the entire conversation history at full price.
Instead of just assuming that was true, I decided to actually test it and look inside the Antigravity binaries to see how caching works under the hood. What started as a quick TTL check turned into disassembling a 193 MB Go binary, discovering a dormant keep-alive engine that Google already wrote, binary-searching the exact eviction cliff down to a 15-second window, testing whether /btw side-questions can keep the cache warm, and finally unlocking Google’s built-in zero-trajectory keep-alive engine on a live 6-minute run.
1. Background: Implicit Caching & The Idle Tax
To understand why pauses matter, let’s look at how Gemini models handle context in Antigravity.
Every turn in an agentic coding session carries a massive prefix: the system prompt, tool schemas, connected MCP servers, skill definitions, and all previous turns. On Gemini 4 models, Antigravity relies exclusively on implicit caching [2, 3]. Unlike explicit caching (where you manually place cache breakpoints and pay for a guaranteed storage lease), implicit caching is an automatic, best-effort prefix match on Google’s backend.
When your request hits the implicit cache, cached tokens (cache_read_tokens) get a 90% discount compared to regular uncached input_tokens [2]. When the cache misses, you pay 100% on the entire prefix.
Google does not publish a fixed TTL for implicit caching. If that TTL is shorter than a typical code-review pause, interactive coding turns into a worst-case workload.
2. What the Binary Says
Before running live probes, I inspected the local Antigravity installation on macOS (arm64): the desktop app (/Applications/Antigravity.app, v2.33.0), its core Go agent binary (language_server), and the standalone CLI (~/.gemini/bin/agy, v1.5.11 / 1.5.12) across isolated CLI runs. [...]

## [69] Advancing chip design with OpenAI models
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~43 words

Design changes proposed by OpenAI's models cut the circuit area of key parts of its Jalapeño AI chip by an estimated 10% to 13%. With AMD, the same approach delivered up to 14% improvements on AMD's flagship GPU designs. Discuss on TLDR →

## [173] Meta Muse booked an Airbnb without permission – and that’s not the worst of it
ZDNet | full text via ZDNet | ~763 words

ZDNET’s key takeaways
- Muse took alarming, privacy-violating action on some Meta employees.
- In testing, an iPhone blocked Muse’s requests; an Android and Apple laptop did not.
- Using proper data hygiene may not be enough to mitigate Muse’s behavior.
Meta’s Muse AI agent has only been around for a few months, but already has a track record of user privacy violations. Even Meta employees are reporting concerning incidents, including the agent taking actions they didn’t ask it to and sharing information they didn’t recognize that appears to belong to other users.
Also: Don’t use Muse? Meta’s AI agent can still access your private messages
According to a Reuters investigation, Meta employees testing Muse said the agent messaged them about topics they hadn’t asked it about, including career advice, a follow-up on a request for childcare, products they hadn’t purchased, and, crucially, bank account balances they didn’t recognize.
More from ZDNET
These incidents “prompted unnerved employees to raise concerns it could be mixing up conversations between different accounts and exposing users’ private data,” Reuters said.
What Meta employees found
Reuters said “an employee told colleagues his Muse had randomly added an extra message to its regular chats about fishing-related weather and tide information, saying: ‘BTW, two bank updates, your Capital One balance is $2,722.58, your Charles Schwab balance is $5,899.57.'” In another instance, Muse booked a non-refundable Airbnb for an employee who hadn’t instructed it to.
Muse notified another employee, who was using the agent on her personal phone, about a message she’d received on Signal, though she said she hadn’t given the agent access to the encrypted messaging app.
Also: Meta Muse is the worst AI agent for privacy – and I’ve tried them all
Reuters and the AI Now Institute determined, through testing on an Android phone and a Mac, that Muse used “permissions granted during the bot’s initial setup to pull in the message text, leveraging those authorizations in ways a user might not anticipate.” Because Muse is set up with automatic access to Android push notifications, it didn’t need explicit app access to read messages.
The tests did not work on an iPhone, suggesting better protections against Muse’s prying.
Similarly, in September, a user reported Muse had shared his address with a Facebook Marketplace buyer before checking with him. [...]

## [121] Apple may be developing its own AI agent that runs your Mac
TechCrunch | full text via TechCrunch | ~369 words

Apple appears to be working on its own AI agent to conduct computer work on behalf of users — including using apps, accessing websites, and coding, among other things.
The news was originally reported by Bloomberg, which spotted a job listing the iPhone maker recently posted for a senior engineering manager to oversee the creation of an “AI agent that can use a computer.”
“Imagine an AI agent that can use a computer the way a capable person does,” the posting says. “It browses the web, works across apps, runs commands, writes and debugs code, and calls services, and it chooses the right tool for each step. It does all this privately and with the polish people expect from Apple.”
The posting additionally notes that the agents should be able to move “fluidly between tools” and “carry out multi-step tasks across apps, browsers, command lines, code, and APIs.”
TechCrunch reached out to Apple for more information but did not receive a response.
Agents capable of computer work have become one of the hottest commodities in the tech industry over the past year. Major labs like Anthropic and OpenAI have launched such services, while other major tech brands — like Meta, which recently launched its Muse agent line — have also moved into the space. It makes sense that Apple — which is trying to expand its AI offerings in the new John Ternus era — would want to follow suit.
Bloomberg additionally notes that, at the same time that Apple is working on its own digital assistant, the company is making it significantly harder for third-party agents to gain total control over its computers.
The outlet notes that the version of its upcoming macOS 27.3 will deploy warnings discouraging users from granting full access to third-party agents. In October, Apple issued a notification to developers stating that the company planned to “introduce additional controls to ensure that users who genuinely wish to grant an app this extraordinary level of access can only do so with very explicit user action.”
Bloomberg writes that while the iPhone maker “has eyed introducing the service as soon as the end of next year,” progress on its in-house agent “remains in the early stages.”

## [153] Google just gave Gemini the run of your Mac — three days after Apple tightened the rules
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~20 words

Google is adding computer use to its Gemini app for macOS. The assistant can now work across desktop applications and

## [74] Sashiko: Lessons from Building an Agentic Code Review System for Linux
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2273 words

Sashiko: Lessons from building an agentic code review system for Linux
Roman Gushchin
Software Engineer, AI & Infrastructure
Eric Brewer
VP, Infrastructure & Google Fellow, AI & Infrastructure
The speed of development in large open-source projects has always been limited by code review, not code generation. Even as coding agents get better at writing code, they do not accelerate development on their own. This is especially true of patches to the Linux kernel. Without a way to build trust in proposed changes, more generated code simply piles up in front of the same small group of human maintainers. Some of those patches are solid changes, just written faster; many others are plausible-looking "AI slop" sent by contributors who do not fully understand the systems they are modifying. And the influx of AI-generated security reports, many of which are duplicates or inaccurate, only adds to maintainers’ load.
Linux runs billions of Android phones, most cloud providers, and nearly every supercomputer. It spans more than 35 million lines of code, and over 85,000 changes land every year. Automated build bots and fuzzers like Syzkaller catch build errors and crashes, but code review has always been the main way to guarantee the stability and safety of the kernel. Every day, maintainers read hundreds and hundreds of proposed patches by hand to catch memory leaks, deadlocks, race conditions, and security bugs.
To help maintainers handle the load and catch bugs before they land, the Google AI & Infrastructure team built Sashiko, an open-source, agentic code review system powered by Gemini. We named the project after the Japanese word 刺し子, a stitching technique for artistically reinforcing worn cloth, and donated it to the Linux Foundation earlier this year.
In this blog, we cover the problem Sashiko was designed to solve, how it works, what the data shows, and what we learned from building and running it in the wild.
Reviewing code is hard
Reviewing a change in a complex code base is objectively hard, both for humans and LLMs. It often requires a deep understanding of how the system works in general, well outside the proposed change. In fact, it’s pretty common to see patches that engineers claim perfectly solve the problem, but if they were to be merged, would actually introduce even worse problems (albeit subtle). Traditionally, only experienced maintainers have been able to spot and prevent these issues. The same is true for agentically generated code.
To verify the correctness of a change, a potentially large number of invariants should be proven, which is often a much larger and harder task than developing the change itself. [...]

## [193] Debian's APT Removing Some Features Due To Advancements In AI Security Discoveries
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~47 words

Stemming from the recent Debian APT man-in-the-middle attack from a vulnerability in APT's downloading code and ongoing advancements in AI/LLMs around security research, APT is now resorting to disabling and removing some older, complex features that may make the program more vulnerable to finding exploits moving forward...

## [183] Google Built a Giant ‘Mirror Dimension’ Internet to Test Its Chrome AI Agents
Wired | full text via Wired | ~629 words

As the Google Chrome team has worked to develop AI browsing features using the company's Gemini models, they realized they need to go the extra mile to keep things from going haywire. So they did the only thing they could think to do—they built an expansive alternate-universe internet that they completely control.
“Web-use” agents need to be familiar with the open internet, how to navigate real websites and platforms, and how to be hardened against web attacks. So training them in limited test environments is only so effective. Plus, models can develop what's known as “eval awareness,” where they behave differently because they have determined that they are in a test or simulation. On the other hand, setting unrefined agents loose on the open internet is a bad idea. That’s where the alternate-universe internet comes in.
The “Mirror Dimension,” which Google is detailing in a blog post today for the first time, is a sweeping and diverse but isolated web ecosystem that the Chrome team entirely controls. It includes a vast array of websites and platforms—including social media sites, shopping, and bank dashboards—that are built with all the components and attributes of real websites. Browsing assistant agents must interact with the sites and complete tasks in Chrome the way they would on the real internet. And they face resilience tests as they go, like hidden prompt-injection attacks, to test their defenses.
“Agents are not programmed, so you can’t predict every possible thing an agent might see; the exploration space that we have to address is huge, and the web is hostile,” says Charles Qian, a software engineer on the Chrome AI security team. “Any user can ask any prompt on any website, so we really need to explore that space as thoroughly as we can. And we’ve seen the agent start to develop a mature sense of judgment when it comes to knowing what information is actually needed for a task and when to punt back to the user for a confirmation.”
Building out and populating the Mirror Dimension was a challenge in itself, because it needed to be vast and varied enough to represent the scale of the real web while being developed quickly. To construct it, the Chrome team gathered armies of website and web app development agents guided by a purpose-built AI harness to quickly create realistic web services and data flows—down to details like entering promo codes on a shopping site or populating social media pages. [...]

## [184] A “headless Slack”: Vercel’s new message board lets Claude Code and Codex agents work together
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~37 words

For AI agents to work together effectively, they need a way to communicate and divvy up tasks — much as The post A “headless Slack”: Vercel’s new message board lets Claude Code and Codex agents work together

## [145] Nvidia Approaches Arm Boss Rene Haas In Search For New CEO
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~91 words

Nvidia has reportedly approached Arm CEO Rene Haas as it searches for a replacement for co-founder Jensen Huang, who resigned last week amid a personal scandal. According to Bloomberg, Haas is emerging as a leading contender for the job. The 64-year-old previously worked at Nvidia as general manager of its computing products business before joining Arm, giving him firsthand experience with the AI chip giant. The Guardian reports: Heidrick & Struggles, the recruiting firm hired by the company's board, has started contacting potential candidates, according to Bloomberg. It reported that Rene

## [75] We Stopped a Railway Migration Three Weeks Out
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2311 words

We stopped a Railway migration 3 weeks out. How to know to stop or go?
Railway is cheap, fast to set up, and adding thousands of new users a day, so plenty of teams are sizing it up for production right now. Evil Martians got most of the way through one of those migrations before backing out, and along the way we learned what the platform asks of you once real traffic and a real database are involved. This post shares what we found, so engineers weighing Railway, or any cheap and fast-growing PaaS, can decide with the full cost in view.
Earlier this year, Evil Martians started moving a high-load Rails production off Engine Yard and onto Railway. The runbook was written, the date was on the calendar, and we’d already lowered our DNS TTLs (time-to-live values, so the switch would propagate fast).
We called it off three weeks before the switchover.
That said, we like Railway, we’ve put other teams on it, and we’d recommend it again for the right workload. But we stopped because Railway was halfway through a hardware transition, and we couldn’t predict which CPU our database would end up on during the maintenance window: the same MySQL dump had imported in 71 minutes on one Railway service and 382 minutes on another.
Railway sells building blocks rather than a managed stack, and its pricing page prices these blocks, not the work of turning them into something a business can depend on. Below are the five parts of that work we wish someone had priced for us before we started, followed by the questions we now answer before putting anything on a platform like it.
1. For us, “Metal” was a hardware lottery
Railway runs services on physical the hosts it owns and operates. They call this Railway Metal. The pitch is no noisy neighbors and predictable performance. Our first benchmark said otherwise. The same MySQL dump took 71 minutes to import on one service and 382 minutes on another (in the same week, on the same plan).
Here are the four import runs we did during the evaluation:
The two actual-dump runs were on different infrastructure, and the two metal-vs-metal runs used a smaller scrubbed dump, so this isn’t a clean within-tier benchmark. The spread is still the point.
The dump, week, and plan: 71 minutes on one service, 382 on another within one plan.
Why? Railway was mid-migration between two hardware generations. Gen 1 Metal ran on Intel Xeons; this is hardware Railway itself now says wasn’t built for the demand mix it sees today. Gen 2 is AMD Zen 5c EPYC: 96 cores, 192 threads, DDR5, live in US West, US East, and Amsterdam as of June 2026, with Singapore still to come. [...]
