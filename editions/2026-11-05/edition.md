---
date: 2026-11-05
edition: 44
schema_version: 1
generated_at: 2026-11-05T01:37:46+00:00
sources_ok: 43
sources_total: 47
fetched: 401
candidates: 237
full_text: 15
---

# The Brief

- Security leads the day: a suspected Russian intelligence campaign using patched phone flaws, residential proxy traffic found on a White House network, and a $6.3 billion Binance heist that Binance says began with a tampered Homebrew download.
- AI is turning old code into both a target and a tool: an AI-assisted audit turned a 2024 PHP crash bug into a critical flaw, and OpenAI's pipeline generated patches for 948 Linux kernel privilege-escalation bugs.
- Languages had a split day: Go makes its stricter JSON package generally available, C++26 failed its ISO ballot over contracts, and a Zig C library change slowed SQLite badly.
- Business and infrastructure: AMD projects it will pass Intel on Q4 revenue, Meta buys the Conductor agent startup, Waymo ends its Uber exclusivity, and Render removes its sandbox time cap.

# Stories

## PHP2Shell: an AI-assisted audit turned a 2024 PHP crash bug into a critical flaw
- ids: 6
- topic: Security
- signal: must-read
- url: https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability
- event: php2shell php ai audit
- original title: AI is forcing us to pay off 40 years of technical debt
- source: spectrum.ieee.org | https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability | via Hacker News
- author: Dina Genkina
- image: https://spectrum.ieee.org/media-library/image.jpg?id=68544156&width=1200&height=600&coordinates=0%2C312%2C0%2C313
- read: 5 min
- discuss: https://news.ycombinator.com/item?id=50364336 | Hacker News | 1057 points | 631 comments
- full text: yes

> The patch arrived before any known exploitation, but the same method could surface similar bugs across decades-old code.

PHP2Shell is a critical flaw in PHP, the language behind a large share of older websites, including sites built on WordPress and Drupal. The underlying bug was reported to the PHP Foundation in 2024. It was an out-of-memory error, the kind of fault that usually just crashes a program, so it sat in the queue as a low-priority crash for a long time.

The turn came when Calif, a cybersecurity firm, offered to audit PHP independently, with OpenAI as the sponsor. Within about two weeks, a Calif researcher using AI tools showed that the memory error could be used to run arbitrary code on a host server, which would let an attacker install malware or read sensitive data. The reporting says the flaw put sites such as NASA, Wikipedia and the White House at risk, and the team alerted the PHP Foundation so a patch could be built.

Exploiting the bug is still hard work. An attacker has to reach a specific point in a running program's memory and work out which bits to overwrite, and in what order, to take control. Suman Jana, a Columbia University computer scientist quoted in the piece, says that kind of detailed reasoning is what AI does well, which is why old crash reports deserve a second look.

The patch shipped before any known attacker used the flaw, so there is no incident to respond to yet. The open question is how many other crash bugs in decades-old C and PHP code could now be turned into working exploits by the same approach.

**Takeaways**
- Confirm that PHP servers and WordPress or Drupal installs run a patched PHP release, and check hosting panels for pending updates.
- Reopen any memory-error crash reports in C or PHP code that touch network-facing input, since those are now worth a fresh look.

## Residential proxy services exited through the White House network 236 times in a month
- ids: 5
- topic: Security
- signal: must-read
- url: https://layer3intel.com/blog/residential-proxies-white-house-network
- event: residential proxy white house network exits
- original title: Residential proxies detected on White House network
- source: layer3intel.com | https://layer3intel.com/blog/residential-proxies-white-house-network | via Hacker News
- author: Layer
- image: https://layer3intel.com/eop_proxy_activity.png
- read: 3 min
- discuss: https://news.ycombinator.com/item?id=50371246 | Hacker News | 622 points | 199 comments
- full text: yes

> The pattern of activity points to one person's device rather than a public Wi-Fi network, and that device may be carrying a proxy software kit.

Researchers who launched a public Residential Proxy Observatory noticed traffic exiting through AS2650, a network registered to the Executive Office of the President, which hosts the White House network. Residential proxy services sell access to ordinary people's devices, so a customer's traffic appears to come from that home or office connection. Between October 5 and November 3, the researchers' own probes exited through the network 236 times, from six addresses, on 26 of 30 days, and 28 separate services were able to use it.

The researchers say they did not target this network. They were requesting rotating access through public proxy services, and anyone can buy the same access for a few dollars. Two other detection services, Spur and Synthient, independently flag the same addresses as residential proxy exits.

The timing points at a person rather than a visitor network. About half of the activity falls between 5 p.m. and midnight Eastern, and almost none happens in the early morning. The researchers read that as someone who regularly uses the network in the evening, on a device with a proxy SDK installed. Their data shows the exits, though, not the device or its owner.

The concern is what that software can reach. Weakly secured proxy SDKs have been used to move laterally inside networks, and the researchers cite the Kimwolf botnet, which spread through proxy networks to at least 2 million devices, most of them Android devices left with an ADB service open. If a proxy SDK on this network has a similar flaw, anyone who buys proxy access could reach internal systems.

**Takeaways**
- On corporate and government networks, search managed devices for unknown proxy or bandwidth-sharing apps, and block known residential proxy ranges where you can.
- On Android fleets, confirm that ADB is not exposed to the network, since that is the weakness the Kimwolf botnet exploited.

## Binance says its $6.3B heist started in June with a tampered Homebrew download
- ids: 36
- topic: Security
- signal: must-read
- url: https://arstechnica.com/information-technology/2026/11/binance-says-hackers-who-stole-billions-in-crypto-spent-months-planning-heist/
- event: binance wallet hack withdrawals
- original title: Binance says hackers who stole billions in crypto spent months planning heist
- source: Ars Technica | https://arstechnica.com/information-technology/2026/11/binance-says-hackers-who-stole-billions-in-crypto-spent-months-planning-heist/
- author: Dan Goodin
- image: https://cdn.arstechnica.net/wp-content/uploads/2026/10/binance-1024x648.jpg
- read: 2 min
- full text: yes

> Since we last covered the heist, when the FBI blamed North Korean actors and withdrawals reopened, Binance has published its first account of how the attack unfolded, and the new detail is that it ran for months and combined several methods.

The operation stretched across the summer. The earliest compromise likely happened in June, through a poisoned package-manager tool that an employee installed. Internal security did flag the infected machine, yet the report says that happened only after the intruders had learned who on staff handled wallet systems. Last Thursday, they took over a staff laptop and moved funds out of several wallets.

The report lists a mix of tactics, from fake recruitment interviews and tampered downloads to abuse of internal AI tooling, endpoint intrusion and a more advanced way of signing off transactions. Binance describes a sophisticated, multi-stage operation rather than one breach or an ordinary phishing scam. The FBI and the TRM Security firm both attributed the theft to North Korean actors.

The attack targeted $6.34 billion in cryptocurrency from Binance wallets, and the exchange says it has frozen or intercepted $2.85 billion of that. It has set aside funds to cover the loss and published a proof-of-reserves page. The update does not say where the remaining $3.5 billion went, and that is the main open question.

**Takeaways**
- Verify checksums or signatures for package-manager tools on engineer laptops, and alert on installs that do not match the expected version.
- Route any recruiter-led interview that asks candidates to run code or download tools through a separate, verified channel first.
- Require a second approval path outside the engineer's own laptop for large wallet withdrawals.

## AMD guides to $17B in Q4 revenue, putting it ahead of Intel for the first time
- ids: 1, 2
- topic: Infra
- signal: recommended
- url: https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections
- event: amd quarterly revenue intel outsell
- original title: AMD expects to outsell Intel in Q4 for the first time in history
- source: tomshardware.com | https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections | via Hacker News
- source: Slashdot | https://news.slashdot.org/story/26/11/04/1825235/amd-expects-to-outsell-intel-for-the-first-time
- author: Anton Shilov
- image: https://cdn.mos.cms.futurecdn.net/9RbcgLQz2F5o3E3DkoVzeG-1920-80.jpg
- read: 9 min
- discuss: https://news.ycombinator.com/item?id=50367125 | Hacker News | 466 points | 171 comments
- full text: yes

> The data center business is doubling, while the client and gaming businesses are expected to decline by double digits going into 2027.

AMD reported record third-quarter revenue of $13.4 billion, up from $9.25 billion a year earlier, with a 54 percent gross margin. Net income rose 95 percent to $2.43 billion, and diluted earnings per share were $1.46, against $0.75 a year ago.

Growth came from the data center unit, which reached a record $8.55 billion, up 97 percent, and now makes up 64 percent of revenue. Demand for Epyc server processors and the new Instinct MI455X accelerators, which power the Helios rack systems, drove it. AMD says Anthropic, Meta, Microsoft, OpenAI and Oracle Cloud are already running workloads on the first Helios systems.

The fourth-quarter outlook is about $17 billion, a figure that would move AMD past Intel for the first time. Within that, data center revenue is pegged at roughly $12.8 billion. Lisa Su said server revenue should double in 2027, and that data center AI sales are now tracking ahead of the forecast she gave three months earlier.

The weak spot is consumer hardware. Ars Technica reports that gaming revenue fell 40 percent, and client sales declined only modestly despite high memory prices. The Q4 forecast leans on the Helios ramp, so the next quarterly report is the real test.

**Takeaways**
- Watch the Q4 data center figure against the $12.8 billion guidance, the clearest test of how quickly the Helios ramp is landing.

## Ripple-65B Preview tops US open-weight models on TerminalBench 2.1 for a $32M build
- ids: 8
- topic: AI
- signal: recommended
- url: https://www.ricursive.com/ripple
- event: ripple 65b terminalbench preview
- original title: Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding
- source: ricursive.com | https://www.ricursive.com/ripple | via Hacker News
- image: https://framerusercontent.com/images/u4OXzV0utwAtaPgcVxQtTXmkg.png
- read: 5 min
- discuss: https://news.ycombinator.com/item?id=50369925 | Hacker News | 217 points | 76 comments
- full text: yes

> The company's own figures put the model ahead of several larger US open-weight systems, but the lead over the nearest one is narrow and the results are self-reported.

Ricursive Intelligence, which builds self-improving AI systems for chip design, released Ripple-65B Preview, a broadly usable version of the closed model behind its design product. The dense 65-billion-parameter model was pretrained on 12 trillion tokens and supports a context window of up to one million tokens. It is available on Hugging Face, Together AI, GMI Cloud and OpenRouter, with Fireworks following.

The headline claim is a score of 80.52 on TerminalBench 2.1, which the company says is the best result for a US open-weight model. That puts it 0.42 points ahead of Reflection Beam 501B at 80.1, and well ahead of Meta's Muse Spark Open at 76.4, Thinking Machines' Inkling at 63.8 and NVIDIA's Nemotron 3 Ultra at 56.4.

The cost claim is the other half. Ricursive says its full R&D spend, including pretraining experiments, data mixing, evaluations, synthetic data and the final training run, came to $32 million, about a tenth of its estimate for the previous open-weight leader on agentic coding. It bought no post-training data and built its own synthetic pipelines and quality filters instead.

Independent verification is still missing. The benchmark is labeled a preview, and the cost comparison rests on the company's own estimate of rivals' spending. The company says the model is light enough to run locally on hardware such as NVIDIA's DGX Spark.

**Takeaways**
- If you evaluate open-weight coding models, rerun TerminalBench 2.1 on Ripple-65B and your current baseline before switching.

## Suspected Russian intelligence hackers used patched phone flaws via a fake America250 site
- ids: 25
- topic: Security
- signal: recommended
- url: https://arstechnica.com/security/2026/11/hackers-exploited-ios-and-android-flaws-to-infect-phones/
- event: darksword ios android russia websites
- original title: Hackers exploited iOS and Android flaws to infect phones
- source: Ars Technica | https://arstechnica.com/security/2026/11/hackers-exploited-ios-and-android-flaws-to-infect-phones/
- author: Dan Goodin
- image: https://cdn.arstechnica.net/wp-content/uploads/2023/05/malware-1000x648.jpg
- read: 2 min
- full text: yes

> The campaign used flaws Apple and Google had already patched, so the exposure is limited to phones that missed those updates.

Researchers assessed with moderate to high confidence that a group linked to Russia's Foreign Intelligence Service exploited previously patched iOS and Android flaws against visitors to several websites. The toolkit is called DarkSword, and the final payload was tailored to whichever platform the visitor was using.

The attack worked in stages. Script injected into the traffic first fingerprinted the visitor's device, and the payload that followed was chosen for that platform. Depending on the case, it went after browser cookies, Wi-Fi passwords, or the full contents of the phone.

The lure is the most telling part. A clone of america250.org, the site for the 250th anniversary of American independence run by a non-partisan group, was served from a lookalike domain ending in .holiday, which proxied the real site and added malicious script. The researchers suspect the anniversary was used as a pretext for invitation-themed spear phishing. A second site proxied a luxury London hotel close to some of the UK's most sensitive government buildings.

The article does not say how many visitors were affected, and it gives no count of compromised devices or accounts.

**Takeaways**
- Keep iPhones and Android phones on current OS releases, since these flaws were already fixed.
- Be wary of event invitations that send you to a lookalike domain, especially one using a different top-level domain from the real organization's.

## DreamHost breach exposed customer emails and session tokens over a months-long attack
- ids: 165
- topic: Security
- signal: recommended
- url: https://techcrunch.com/2026/11/04/hackers-stole-dreamhost-customer-files-and-inboxes-during-months-long-attack/
- event: dreamhost customer files breach session tokens
- original title: Hackers stole DreamHost customer files and inboxes during months-long attack
- source: TechCrunch | https://techcrunch.com/2026/11/04/hackers-stole-dreamhost-customer-files-and-inboxes-during-months-long-attack/
- author: Zack Whittaker
- image: https://techcrunch.com/wp-content/uploads/2026/11/GettyImages-2249547675.jpg?w=1024
- read: 1 min
- full text: yes

> The breach began in August and went unnoticed until a multi-day outage led to password resets, and the company has not yet named the vulnerability.

DreamHost has confirmed that hackers stole customer emails and credentials in a months-long attack. A data breach notice filed with California's attorney general says the intrusion began in August and let the attackers obtain session tokens, which keep users logged in after they enter a password. With a stolen session token, an attacker can act as that user without knowing the password.

The entry point was an unspecified vulnerability in DreamHost's file manager, the tool customers use to store files. The company says the flaw is unrelated to the recent PHP vulnerabilities. The breach came to light after an outage that lasted several days, during which DreamHost reset some customers' passwords. A spokesperson declined to say why the attack went undetected until last week, citing an ongoing investigation.

The scale is unclear. The spokesperson said affected customers are well under 10 percent of the company's roughly 400,000 paying customers, but gave no precise figure.

**Takeaways**
- If you have a DreamHost account, change your password, end active sessions if the host offers that option, and check for email forwarding rules you did not create.

## Anthropic's FlashProve can prove which model served a response, at 70 to 95 times the GPU cost
- ids: 153
- topic: AI
- signal: recommended
- url: https://thenewstack.io/anthropic-flashprove-model-verification/
- event: flashprove zksnark model verification
- original title: Anthropic found a way to prove which AI model answered you — but there’s a costly catch
- source: The New Stack | https://thenewstack.io/anthropic-flashprove-model-verification/
- author: Amanda Caswell
- image: https://cdn.thenewstack.io/media/2026/11/caa0e2d8-chloe-f5wzv43ls-0-unsplash-scaled.jpg
- read: 3 min
- full text: yes

> The open-source system is a research prototype, not a feature of the Claude API, and its proofs are too expensive for routine traffic.

Customers of hosted models usually cannot verify which network produced a given reply. Anthropic's Frontier Red Team has released FlashProve, an open-source tool built on zkSNARK proofs, which can show that a reply came from a particular set of weights while keeping those weights private. The aim is to catch providers that quietly swap in a cheaper model, or attackers who tamper with responses.

The proof is only as trustworthy as the commitment to those weights, which has to come from a trusted source. FlashProve is a research prototype, and Anthropic has not made it a feature of the Claude API. The code is on GitHub for anyone to test.

The costs are high. The test subject was Meta's Llama 4 Maverick, a mixture-of-experts model with 400 billion parameters, not Claude. On one H100, proof generation managed roughly 110 prompt tokens per second. A single proof runs about 18.78 MB, and checking it takes roughly 21 seconds on one CPU thread. Generating proofs used 70 to 95 times more GPU time than standard vLLM inference, and they are produced in batches once a request finishes.

Anthropic says FlashProve is substantially faster than earlier open-source systems such as VerInf, which needed 14.3 hours to prove a 1,000-token response. Even so, the design fits audits and spot checks rather than every API call, because the proof arrives after the answer.

**Takeaways**
- Track FlashProve's GitHub activity for cost reductions, since the GPU overhead is the main barrier to routine use.

## Apple will scan iCloud items shared by link for harmful content starting with iOS 27.3
- ids: 179
- topic: Security
- signal: recommended
- url: https://www.theverge.com/tech/1026604/apple-icloud-links-harmful-content-27-3
- event: apple icloud shared links harmful content
- original title: Apple will check shared iCloud links for ‘harmful content’
- source: The Verge | https://www.theverge.com/tech/1026604/apple-icloud-links-harmful-content-27-3
- author: Jay Peters
- image: https://platform.theverge.com/wp-content/uploads/sites/2/2026/03/STK071_APPLE_E.jpg?quality=90&strip=all&crop=0%2C10.732984293194%2C100%2C78.534031413613&w=1200
- read: 1 min
- full text: yes

> Shared items lose end-to-end encryption under this rule, and Apple has not defined what it counts as harmful content.

Starting with iOS 27.3 and the other 27.3 updates across Apple's platforms, Apple will check items shared with "Anyone with the Link" for harmful content. According to a support document reported by 9to5Mac, making an item available that way makes it accessible to Apple for checking, and it is no longer end-to-end encrypted.

The document does not define harmful content. The change follows calls from protesters for Apple to act on child sexual abuse material stored in iCloud. Apple reserves the right to move, refuse, modify, remove or delete flagged content, and it may block or disable accounts, stop people from opening new ones, or involve law enforcement if necessary.

The first 27.3 developer betas are already out, and Apple plans to release iOS 27.3 in December.

**Takeaways**
- Do not rely on anyone-with-the-link sharing for confidential files, since that content is no longer end-to-end encrypted and Apple can review it.
- Check the iOS 27.3 release notes in December for a clearer definition of harmful content.

## Go 1.27 makes encoding/json/v2 generally available with stricter JSON handling
- ids: 9
- topic: Languages
- signal: recommended
- url: https://go.dev/blog/jsonv2
- event: go json v2 release generally available
- original title: A new Go API for JSON
- source: go.dev | https://go.dev/blog/jsonv2 | via Hacker News
- image: https://go.dev/doc/gopher/gopher5logo.jpg
- read: 14 min
- discuss: https://news.ycombinator.com/item?id=50369106 | Hacker News | 226 points | 95 comments
- full text: yes

> The new package is meant to reject inputs the current one silently accepts, which could break decoders that depend on that leniency.

The new encoding/json/v2 and encoding/json/jsontext packages are now stable and generally available in Go 1.27. They follow an experiment announced last year, and the Go team says feedback drove the refinements.

The problems with the current package are mostly about leniency. encoding/json accepts invalid UTF-8, which RFC 8259 forbids, and passes corrupted text downstream without an error. It also accepts objects with duplicate member names, a case the RFC leaves open. Attackers have exploited that before, including in CVE-2017-12635. The Go team argues the default should reject both.

A third issue is how null interacts with slices and maps. encoding/json can produce nil slices and maps that stricter peers reject.

For services that decode untrusted input, the practical effect is that a payload that parsed under the old rules could fail under the stricter defaults. Teams should test their decoders before moving to the new packages.

**Takeaways**
- Run your JSON decoders against inputs that include duplicate keys and invalid UTF-8 before upgrading to Go 1.27.

## C++26 fails ISO ballot over contracts, the first rejected DIS in the language's history
- ids: 51
- topic: Languages
- signal: recommended
- url: https://andreasfertig.com/blog/2026/11/cpp26-dis-failed-how-does-cpp-survive/
- event: cpp26 disapproved iso ballot contracts
- original title: C++26 Disapproved
- source: andreasfertig.com | https://andreasfertig.com/blog/2026/11/cpp26-dis-failed-how-does-cpp-survive/ | via Lobsters
- author: Andreas Fertig
- image: https://andreasfertig.com/img/2026-11-03-cpp26-failed-li.png
- read: 6 min
- full text: yes

> National bodies have rejected the standard at a stage that has never failed before for C++, and the schedule for C++26 is now in doubt.

On October 23, 2026, national standards bodies voted down C++26 at its Draft International Standard stage, after a twelve-week ballot. That stage needs a two-thirds majority, and it was not reached. The author, a member of the C++ standards committee who represents Germany's vote, says it is the first DIS ballot in C++ history to fail. The only other rejected DIS the author could find was a 2006 C++/CLI specification, whose project was then halted.

The stated reason is contracts, a feature several national bodies say is not ready for release. Committee practice has been to hear objections and then respect the outcome, and national bodies have usually voted no only when new information or a process error surfaced. This time several bodies argue new information exists. The author disagrees, saying a new paper that repeats old arguments is not new information.

The author writes in a personal capacity and notes that ISO rules keep some ballot results and breakdowns unpublished. The piece does not settle what happens next, so the outcome is still open.

**Takeaways**
- If your team targets C++26, do not assume contracts will ship, and check the committee's next steps before depending on the feature.

## Zig's libc rewrite made a 40,000-record SQLite insert take minutes of CPU time
- ids: 38
- topic: Languages
- signal: notable
- url: https://dennisforbes.ca/blog/microblog/2026/10/the_accidental_12000x_sqlite_slowdown/
- event: zig libc sqlite shlemiel painter slowdown
- original title: Shlemiel the Painter Is Back: How Zig’s libc Rewrite Made SQLite Slower
- source: dennisforbes.ca | https://dennisforbes.ca/blog/microblog/2026/10/the_accidental_12000x_sqlite_slowdown/ | via Lobsters
- author: Dennis Forbes
- image: https://dennisforbes.ca/include/images/og_dennis_forbes.jpg
- read: 5 min
- full text: yes

> The slowdown is a quadratic pattern that the author traces to the C library Zig's cc compiler uses when cross-compiling SQLite for Linux targets.

The author runs a chess analysis service written in Rust and backed by SQLite. Runners send back large JSON bundles, and the service stores them. Storing about 40,000 records should take milliseconds, but on the first large batch it took minutes and saturated one CPU core.

The cause is what Joel Spolsky called the "Shlemiel the Painter" pattern, a trap where each step gets slower as the work grows. The author traced it to Zig's replacement C library, which zig cc uses when building SQLite for Linux targets.

The build setup explains why that path matters. The author builds Mac ARM64 and Linux binaries from one machine through cargo-zigbuild, without containers or separate build machines. That convenience sends SQLite's Linux builds through Zig's library, which is where the slowdown appeared. The post is a case study in how one library choice can dominate a bulk workload, not a verdict on Zig.

**Takeaways**
- If you cross-compile C dependencies with zig cc, benchmark bulk inserts against a native build before shipping.

## LinkedIn links client taps to backend traces with a page-level ID on OpenTelemetry
- ids: 112
- topic: Engineering
- signal: recommended
- url: https://www.infoq.com/news/2026/11/linkedin-opentelemetry-journey/
- event: linkedin opentelemetry member journey tracing
- original title: LinkedIn Uses OpenTelemetry to Trace the Member Journey from Tap to Backend
- source: InfoQ | https://www.infoq.com/news/2026/11/linkedin-opentelemetry-journey/
- author: Craig Risi
- image: https://res.infoq.com/news/2026/11/linkedin-opentelemetry-journey/en/headerimage/generatedHeaderImage-1793095474316.jpg
- read: 3 min
- full text: yes

> Single-request tracing misses the many requests one page load generates, so LinkedIn added a grouping key above individual traces.

LinkedIn's telemetry platform connects what members do in its iOS, Android and web apps with the backend services that handle those actions. Client analytics can show that a member tapped a button or hit an error, while backend tracing shows what the services did. Connecting the two used to mean engineers correlating separate systems by hand.

Each request keeps its OpenTelemetry trace ID, and a pageForestId groups related requests from the same page context. Telemetry moves through Apache Kafka and is stored in ClickHouse, with the page ID, trace ID and timestamps as the correlation keys. Engineers can start from a member-facing interaction and drill into the backend work behind it.

The stack spans mobile and web clients plus backend services in Java, Python, Go and Rust. LinkedIn wraps the standard OpenTelemetry SDKs so product teams get consistent instrumentation, while the platform handles mobile lifecycle, export and LinkedIn-specific metadata.

Sampling is the hard part. LinkedIn uses coordinated head sampling, with a pseudonymized member identifier, so the client and backend make the same decision. That prevents a client span from being kept while its backend trace is dropped, or the reverse.

**Takeaways**
- If you trace across mobile and backend, add a page or session-level ID next to trace IDs so related requests can be grouped.
- Use one sampling key shared by client and server to avoid orphaned spans.

## Render removes its 30-day cap on AI sandboxes; Vercel still limits sessions to 24 hours
- ids: 184
- topic: Infra
- signal: recommended
- url: https://thenewstack.io/render-vercel-ai-sandboxes/
- event: render ai sandboxes runtime limit vercel
- original title: Render just removed its AI sandbox time limit — and Vercel still has a 24-hour cap
- source: The New Stack | https://thenewstack.io/render-vercel-ai-sandboxes/
- author: Amanda Caswell
- image: https://cdn.thenewstack.io/media/2026/11/88af2b32-getty-images-1rdhxhol-xu-unsplash-scaled.jpg
- read: 5 min
- full text: yes

> Render's sandboxes suspend when idle and resume with their files and processes intact, which matters most for long agent tasks.

Render has removed the 30-day continuous runtime limit on paid workspace plans for its AI sandboxes. The launch, announced Wednesday, is aimed squarely at Vercel, which caps individual sandbox sessions at 24 hours. Render says its environments can run indefinitely and suspend when idle.

The resume behavior is the sharper difference. Render sandboxes wake on the next command with files, memory and running processes intact. Vercel's persistent sandboxes can restart, but their running processes start over, so an agent has to rebuild its state.

Render is also adding credential brokering, which injects credentials into requests on their way out of the sandbox, so the secrets themselves never live inside it. Only selected customers get it at first. Networking that keeps sandboxes private is still being built, and the company has not yet decided how shared storage will deal with two writers hitting the same file at once.

On credentials, Vercel already offers scoped credentials for agents through its Connect service, and Render does not claim an advantage there.

**Takeaways**
- Before running parallel agents against Render shared storage, test what happens when two agents write the same file, since that behavior is not settled.
- If you run long agent jobs on Vercel, plan a restart path for the 24-hour cap.

## Meta buys Conductor, the startup that runs parallel coding agents
- ids: 157
- topic: Startups
- signal: recommended
- url: https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/
- event: meta acquires conductor coding agents
- original title: Meta acquires AI coding startup Conductor
- source: TechCrunch | https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/
- author: Lucas Ropek
- image: https://techcrunch.com/wp-content/uploads/2026/09/mark-zuckerberg-ray-bans.png?resize=1200,653
- read: 2 min
- full text: yes

> Conductor's cloud service shuts down on November 20, and its cloud data will be deleted after that, while the core app keeps working until early next year.

Meta has acquired Conductor, a startup founded in 2024 whose software lets engineers deploy several AI agents into parallel workspaces to work on different parts of one project. Conductor launched its core product only last summer. Meta confirmed the deal but did not share terms.

The agents Conductor deploys come from outside labs such as Anthropic and OpenAI rather than from Conductor itself. Founder and CEO Charlie Holtz said the company has something new for customers coming early next year, and he is looking forward to working with Meta's AI leadership.

The deal extends a run of Meta acquisitions and products. Meta launched its own coding agent, Muse Code, in August, and says its Muse agents have passed 10 million users. The company has also bought Moltbook, the agent platform that drew attention earlier.

**Takeaways**
- If you have projects in Conductor's cloud service, export them before November 20, since cloud data deletion follows the shutdown.

## OpenAI to acquire Pierre Computer Company, with Codex as the stated goal
- ids: 3, 4
- topic: Startups
- signal: notable
- url: https://openai.com/index/openai-to-acquire-pierre/
- event: openai acquire pierre computer codex
- original title: OpenAI to acquire Pierre Computer Company
- source: openai.com | https://openai.com/index/openai-to-acquire-pierre/ | via Hacker News
- source: Slashdot | https://developers.slashdot.org/story/26/11/04/1957217/openai-acquires-pierre-computer-to-supercharge-codex
- discuss: https://news.ycombinator.com/item?id=50366863 | Hacker News | 182 points | 56 comments
- full text: no

> The sources available for this story did not include deal terms or details of what Pierre builds.

This story comes from the headline and standfirst only, because the full articles could not be fetched. The reports say OpenAI is acquiring Pierre Computer Company, and Slashdot frames the deal as a way to strengthen Codex, OpenAI's coding product. Price, timing and Pierre's product were not available from the sources reached.

## OpenAI's autonomous pipeline generated patches for 948 Linux kernel privilege-escalation bugs
- ids: 52
- topic: Security
- signal: notable
- url: https://openai.com/index/a-thousand-fewer-paths-to-root
- event: openai linux kernel privilege escalation patches
- original title: A thousand fewer paths to root
- source: OpenAI Blog | https://openai.com/index/a-thousand-fewer-paths-to-root
- full text: no

> The post describes the scale of the result, but the method and timeline were not available from the sources reached.

This story comes from OpenAI's post standfirst only, because the full post could not be fetched. According to the standfirst, OpenAI built an autonomous pipeline that found and validated 948 local privilege-escalation flaws in the Linux kernel, then generated patches for them. Local privilege escalation lets someone with limited access on a machine gain root, so these bugs matter most on shared servers and multi-user systems.

## Waymo ends its exclusive Uber partnership in Austin and Atlanta, starting January 2028
- ids: 171
- topic: Startups
- signal: notable
- url: https://tech.slashdot.org/story/26/11/04/2021250/waymo-cuts-ties-with-uber-will-serve-riders-directly
- event: waymo uber partnership austin atlanta
- original title: Waymo Cuts Ties With Uber, Will Serve Riders Directly
- source: Slashdot | https://tech.slashdot.org/story/26/11/04/2021250/waymo-cuts-ties-with-uber-will-serve-riders-directly
- author: BeauHD
- full text: no

> Riders in those cities will be able to book Waymo vehicles directly through the Waymo app once the arrangement ends.

This story comes from a Slashdot summary of a Bloomberg interview, because the full article could not be fetched. Waymo plans to end its exclusive Uber arrangement in Austin and Atlanta in January 2028. Co-CEO Tekedra Mawakana called the current setup a crapshoot, since riders could not count on getting a Waymo when they requested one.

## Synaptics legal threats led to removal of the open-source Vino DisplayLink driver
- ids: 209
- topic: Open Source
- signal: notable
- url: https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver
- event: synaptics displaylink vino driver legal threats
- original title: Synaptics Appears To Use Legal Threats To Block Open-Source DisplayLink Driver
- source: Phoronix | https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver
- author: Michael Larabel
- full text: no

> The standfirst does not describe the threats themselves, so whether the driver can return, and on what terms, is unclear.

This story comes from the Phoronix standfirst only, because the full article could not be fetched. The Vino driver was an experimental, clean-room reverse-engineered Linux driver for newer DisplayLink hardware, written in Rust and developed partly with AI. According to the report, it has disappeared from public view after legal threats from Synaptics.

## djs is a Rust JavaScript engine that can pause and resume agent scripts mid-run
- ids: 13
- topic: Languages
- signal: notable
- url: https://github.com/earendil-works/djs
- event: djs rust javascript engine agent sandbox
- original title: djs (GitHub Repo)
- source: github.com | https://github.com/earendil-works/djs | via TLDR Dev (Web Dev)
- full text: no

> The engine is built for scripts that AI agents generate and run inside a WebAssembly sandbox, and it leaves out common features to stay small.

This story comes from the TLDR Dev summary, because the repository page could not be read. djs is a JavaScript and TypeScript engine written in Rust for scripts that AI agents generate and run inside a WebAssembly sandbox. It stores its whole virtual machine state in a single byte array, so a run can pause between instructions, be saved while it waits on a tool call, and resume somewhere else. The focused runtime leaves out ES modules, Intl and a JIT compiler.

## OpenAI's Pando Git backend cut median push latency by nearly 80 percent
- ids: 84
- topic: Infra
- signal: notable
- url: https://openai.com/index/scaling-git-at-openai/
- event: openai pando git backend scaling
- original title: Scaling Git at OpenAI
- source: openai.com | https://openai.com/index/scaling-git-at-openai/ | via TLDR Dev (Web Dev)
- full text: no

> The tradeoff is weaker consistency across branches and some redundant downloads, which OpenAI accepted to let writes scale out.

This story comes from the TLDR Dev summary, because the full post was not available. OpenAI's new backend, Pando, is compatible with Git and treats pushes to unrelated branches as independent, so they do not queue behind one another. It also reuses cached packfiles across fetches. The summary says median push latency fell by nearly 80 percent, and the service now handles close to a petabyte of Git data a day.
