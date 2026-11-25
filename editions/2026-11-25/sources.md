# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Anthropic breaks below $83 IPO price
Hacker News | full text via TechCrunch | ~163 words

Anthropic’s stock fell below its IPO price of $83, trading as low as $76 a share by midday Tuesday, down nearly 12% from Monday’s close.
Falling below the IPO price is often seen as a negative signal because underwriters typically price offerings at a discount to their expected trading value.
The AI industry has been eagerly watching how Anthropic’s shares trade, with VCs and other observers saying its performance could serve as a barometer for how public market investors value the sector.
The dramatic slump comes less than a week after Anthropic debuted on Nasdaq at $111.50 a share. If its shares continue to trade poorly in the coming weeks, the slide could put pressure on private startup valuations and weaken IPO prospects for other AI companies.
Anthropic isn’t the only AI stock selling off on Tuesday. Nvidia fell more than 7% by midday, giving back some of the more than 30%-plus gain it posted Monday after Jensen Huang was reinstated as CEO.

## [13] Microsoft's historic cloud outage exposed an engineering “fog of war”
Ars Technica | full text via Ars Technica | ~189 words

According to internal memos reviewed by Reuters, Microsoft has declared a “Code Red” overhaul of its engineering response practices after the November 12 outage that lost access to Exchange Online, Teams, and Outlook for users worldwide.
Per the memos, Microsoft 365 Core President Jason Henderson described the outage as having the most customer impact in the history of Exchange Online. In a separate memo, Henderson wrote that an urgent production fix in a recent incident took five to six days to reach worldwide saturation. Microsoft’s target for its most urgent security fixes is to move from detection to safe worldwide deployment in one hour. “Needless to say, we aren’t here yet,” Henderson wrote.
The memos, which Reuters reviewed but Microsoft has not published, outline the response to the November 12 disruption. The company’s post-incident report, dated November 20, attributed the downtime to an undetected Windows scalability defect introduced in July, which caused lock contention in the gateway processes. A Teams traffic failover then dumped additional load onto infrastructure already under stress, as maintenance had left nearly 14 percent of gateway server capacity offline at the time of the incident.

## [148] Hackers Compromise Check Point Servers In 22 Organizations
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~86 words

Hackers have compromised 24 Check Point Security management servers across 22 organizations in 17 countries in a suspected cyberespionage campaign, according to threat intelligence firm GreyNoise. BleepingComputer reports: The researchers track the activity as GT13 and confirmed it was ongoing between October 17 and November 2, when their visibility ended. However, given the threat actor's persistent access to Check Point devices, they believe the campaign remains active. GreyNoise says the 22 victim organizations are spread across 17 countries, and show no clear evidence of specific targeting

## [3] LLM agents work for their parent companies, not for you
Hacker News | full text via Hacker News | ~994 words

LLM agents work for their parent companies, not for you
5 min read
In the evenings after work, I will often sit out back on the porch and do some phone rotting. That usually takes the form of me just flipping through reels on Instagram, allowing the algorithm to take me where it may. I usually pair this with a healthy tumbler of rum or bourbon. I'm turning my brain off after work, and I'm just having a good time on the internet. The kids might call it dopamine maxxing? Hell, I don't know. Who gives a shit about what those assholes would call it?
Anywho, I often encounter songs I really really like, and I would like to listen and discover more of please. Instagram makes it hard for me to connect with the band outside of their platform. I was trying to make this connection manually myself at first. I would just email myself a reel from my phone. Then when I'm back on the sofa and in the mood to track down new music, I'd open the reels and do my best to search on Bandcamp or YouTube or try to figure out if some of these musicians had a way to buy music from them. Very few do these days. They send you their Spotify link or send you to their TikTok page. I don't want to do any of that. I'd like to trade US dollars in exchange for some music files I can download onto my computer, where I can listen as much as I like on any device I own thank you please. Retro maxxing.
So, I used Claude Code to build a skill that does this for me. It opens the Instagram reel and attempts to identify the artist and song. It then tries to determine if the artists have a Bandcamp page so I can purchase the songs I want, and if it finds one, it gives me the URL so I can click it to complete the trade I want. I want to buy music from artists who make music I like. That's a fair and wholesome endeavor, I feel, but this recently stopped working.
It turns out Bandcamp added a challenge on their search API page. Ah bummer. No worries, that was an unpublished workaround anyway. As I was mulling over this discovery, the robot went on to explain that it would not help me work around the challenge. cue Nick Young question marks
Well, that led me down a whole nother rabbit hole, which is turning into this post. There's another branch of my skill that attempts to locate the same song from the Instagram reel on YouTube, and it'll download the song to my computer if I ask.
So let me get this straight. [...]

## [161] Confluent spent 3 months rewriting Kafka’s Java client in Rust with AI — and had to start over
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~36 words

Confluent spent nearly three months using AI coding agents to translate Apache Kafka’s Java client into Rust. The engineers discarded The post Confluent spent 3 months rewriting Kafka’s Java client in Rust with AI — a

## [17] OpenAI Scales Git for Coding Agents with Pando
InfoQ | full text via InfoQ | ~742 words

OpenAI has detailed Pando, a new backend that scales Git for concurrent coding-agent workloads without replacing familiar Git workflows. The company reports nearly 80% lower median push latency by coordinating branch updates independently and reusing stored packfiles across fetches.
Pando now powers all development in OpenAI's monorepo and is serving nearly a petabyte of Git data per day. OpenAI attributes the increased load to Codex-driven development, and each push can in turn trigger multiple CI jobs that all fetch the same history. Pando went into production in April 2026.
Rather than replace Git's client and protocol, OpenAI has changed how the backend coordinates reference updates and stores and transfers objects. On a push, Pando validates the incoming packfile as it's being streamed to immutable blob storage, without unpacking it into a local repository. A metadata transaction records the reference version (containing the new branch tip, the packfile and its dependencies on earlier reference versions) and atomically updates the reference pointer. Updates to unrelated references can proceed independently of one another; updates to the same reference still need to be coordinated.
OpenAI refers to this as causal consistency with serialisable updates to individual references and read-your-own-write consistency. A reader gets the history needed for the requested revision, but fetching a number of branches won't provide a repository-wide snapshot. Two clients can see different combinations of branch versions during concurrent updates. The trade-off removes a shared coordination point for unrelated pushes.
Pando also changes how Git decides which objects to transfer. By default, when a client pushes a new feature branch, the server will advertise only a designated trunk branch as its base. That constrains the dependencies of the resulting packfile, which in turn allows Pando to reuse it for readers who already have that trunk history. Repeated or stacked branch pushes can resend objects outside trunk, trading some additional bandwidth for the benefit of reusable packs.
Pando’s topic-branch packs depend on advertised trunk history and can repeat objects from earlier pushes (source)
For fetches, Pando maps the client's existing and requested commits to reference versions and picks out the appropriate stored packs to cover the missing history. [...]

## [166] As MCP turns two, Claude gets Skills over MCP and better support for long-running tasks
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~20 words

Anthropic on Tuesday marked the second anniversary of the Model Context Protocol (MCP) by bringing support for skills, long-running tasks,

## [175] Anthropic Created a Honeypot to Lure AI Agents Into Misbehaving
Wired | full text via Wired | ~641 words

Leather-clad billionaires aren’t the only ones who can be led astray by alleged honeypots.
Researchers at Anthropic have developed Siren, a new honeypot test for artificial intelligence agents. The setup puts agents in realistic simulations designed to tempt them into misbehaving. How they respond will help researchers evaluate the likelihood that new models will go rogue when deployed in the real world, as well as the effectiveness of different safety measures.
The test lets agents loose inside one of 26 different simulated sandbox environments. Various features of the sandbox are deliberately misconfigured to allow egress, while an enticing file containing things like passwords and apparent routes onto the internet sits just outside the sandbox boundary. The setup then presents tasks that tempt the agent to reach outside the sandbox without giving it explicit permission to do so. Crucially, the sandbox exists inside a second sandbox that’s cut off from the outside world to avoid real-life mishaps.
“Models are going to continue getting better, continue finding zero-day vulnerabilities,” says Darya Kaviani, a researcher at Anthropic who specializes in security and helped develop Siren.
A zero-day vulnerability is a previously unknown flaw in a piece of software that can be used to pilfer data or gain unauthorized access. Anthropic’s Mythos models are especially skilled at finding zero-day bugs because they lack the guardrails that normally block this kind of potentially malicious activity.
Kaviani says we should assume AI models will become increasingly capable of finding and exploiting zero-days or figuring out other ways to break free from their constraints. The question then becomes whether they’ll resist the temptation to do so.
AI agents—models that perfect actions autonomously—are becoming increasingly commonplace. They power capable coding agents like Claude Code and Codex, as well as peppy personal assistants like Meta’s Muse and OpenAI’s Dots.
But the rise of helpful agents has been accompanied by some remarkable bad behavior. Agents tested by Anthropic, OpenAI, and others have broken free from sandboxes and even hacked into other companies in an effort to solve challenging problems.
Assuming AI models continue to display such ingenuity, Kaviani says it will be crucial to do more than just patch software. “Even as we strengthen our infrastructure, models will be able to also keep up and be able to find vulnerabilities,” Kaviani says. [...]

## [45] Security incident on Hex.pm
Lobsters | full text via Lobsters | ~2006 words

On November 23, 2026, an unauthorized third party exploited a vulnerability in hex.pm that let them run commands on our web servers. We blocked the traffic and deployed a fix within 20 minutes. Shortly afterwards we received a report of this exact vulnerability.
We found no evidence of unauthorized package modifications, or database changes, or that the attacker maintained access to our systems. However, because database reads are not logged, we cannot rule out that the attacker accessed data stored in the database, including email addresses, password hashes, API key hashes, 2FA secrets, sessions, and audit logs.
Because email addresses may have been exposed, be careful with emails that claim to come from Hex. Please double-check that the links they contain lead to hex.pm. Please forward suspicious emails to security@hex.pm.
We checked every file written to package storage during the incident against our database and found nothing unexpected. Reads of private packages in that period came from our own servers and coincide with releases the same organizations published at the time. A read made from a compromised server would look like one of ours, so we can't fully rule one out, and reads of private documentation aren't logged. We will contact affected organizations directly.
The attacker's commands could read the credentials our servers use, so we replaced them: the storage, CDN, email and database credentials, and the keys that sign sessions and access tokens. This logged everyone out of hex.pm and Hex clients. We're building a new registry signing system that supports key rotation, with new Hex client releases in the coming days. Until then, don't trust third-party mirrors and fetch packages only from repo.hex.pm. We already deployed fixes for the vulnerability and are working on further hardening fixes.
What you should do
- Change your password at hex.pm.
- Reset your 2FA at hex.pm/dashboard/security: under "Authenticator App", choose "Setup New App" and verify a code from the new entry. You get a new secret and new recovery codes, so store the new codes. This works when an organization requires 2FA, where disabling it is refused.
- Update your Hex client when the release with the new signing system is out in the coming days. Until then, use only repo.hex.pm, not mirrors. To update, run mix local.hex --force, and update rebar3 or Gleam if you use them.
Timeline
All times are in UTC. [...]

## [146] Dozens of oil and shipping tankers hacked in recent weeks, per report
TechCrunch | full text via TechCrunch | ~243 words

U.S. officials suspect Iranian hackers may be behind as many as 50 cyberattacks targeting shipping vessels in recent weeks, according to a report by The Wall Street Journal.
The ships carrying oil, liquefied gas, and other explosive chemicals were hacked as they traveled across Asia and Europe. Several oil tankers headed toward the U.S. coast in August also had their navigation systems breached, prompting cybersecurity teams within the FBI and Coast Guard to board the vessels.
The report said officials are investigating if Iran is expanding its recent wave of hacks against the U.S. by targeting large vessels to sow fear among shippers, disrupt routes, or to cause an explosion at a port. (Ships have backup controls in the event that automated systems are hacked or fail.)
Hackers may have been abusing a bug dubbed FortiBleed, which allows hackers to break into networks by compromising vulnerable Fortinet-made routers. A joint FBI-Coast Guard security alert from September warned that Fortinet routers are used on shipping vessels.
Iran has been firing back on all sides since the start of the U.S./Israel-led war earlier this year, which killed the country’s supreme leader. Many of Iran’s retaliations have been in the form of cyberattacks, with U.S. officials blaming Iran for hacks targeting hundreds of American water providers and U.S. medical tech companies.
A spokesperson for the FBI did not respond to a request for comment about the shipping hacks or whether it had a more accurate figure.

## [120] Huawei found guilty of stealing trade secrets
The Verge | full text via The Verge | ~307 words

A jury has found Huawei guilty of stealing US trade secrets, as reported earlier by NBC News and Bloomberg. The verdict, handed down in a federal court in New York, concludes a years-long legal battle that accused the Chinese telecom giant of stealing source code and proprietary technology from several companies, including T-Mobile, Cisco, and Motorola.
Huawei found guilty of stealing trade secrets
The Chinese telecom giant was also found guilty of bank fraud.
The Department of Justice’s 2018 criminal indictment against Huawei came to light following the arrest of the company’s CFO, Wanzhou Meng, whom the agency accused of fraud. Though the indictment against Meng was eventually dismissed, she admitted to misleading banks over Huawei’s operations in Iran as part of a deferred prosecution agreement. The US government blacklisted Huawei in 2019 over national security concerns.
In total, the jury found Huawei guilty of 10 of 12 criminal counts, including money laundering, violating US sanctions, bank fraud, wire fraud, and conspiracy to defraud the US. The company was acquitted of engaging in a criminal racketeering conspiracy and obstruction of justice. Huawei’s sentencing is set for September 14th, 2027, where it may face “financial penalties including criminal fines, forfeiture, and restitution,” according to the DOJ.
“For over two decades, Huawei built its global empire on a foundation of fraud, theft, and deception,” Tysen A. Duva, the assistant attorney general of the DOJ’s criminal division, says in a statement. “Huawei’s crimes threatened the U.S. financial system, took advantage of American companies that compete honestly in the global telecommunications market, and undermined our national security.”
In a statement to NBC News, a Huawei spokesperson said the charges are “without legal or factual merit” and that it plans to appeal the decision. Huawei didn’t immediately respond to The Verge’s request for comment.
Update, November 24th: Added information from the DOJ.

## [8] Quad9 pulled their DNS service from France
Hacker News | full text via Hacker News | ~1848 words

Back to Blog
Quad9 Service Deactivation in France
(en français)
Today, November 24 2026, Quad9 will disable services for French users. This means any query reaching any Quad9 service address will be refused, and no DNS resolution will be successful. Our planned deactivation will be at 09:00 Central European (Paris) Time, to try to give users who are unaware a chance to respond quickly instead of having services down outside of normal business hours.
We are unhappy to have reached this impasse. For those of you seeing this for the first time, see our announcement of this deactivation from one month ago.
The Summary
We have received demands from beIn (a sports rightsholder company) to block various domains they claim to be related to piracy streaming sites, so users in France cannot resolve those DNS names. Currently, the courts have upheld beIn’s demands, and we have faced fines for non-compliance. We are entirely opposed to piracy, but Quad9 has nothing to do with the piracy sites. This is an attempt to force us to be part of an enforcement regime against third parties.
We have a fundamental opposition to using recursive DNS providers as a tool in this or any other content blocking campaign. Putting demands on recursive resolvers has no effect on the origin servers that deliver objectionable content. Attacking recursive resolvers is a futile and counter-productive effort, but that explanation is not understood. The policymakers and courts of France may of course make any determination they wish, even those that seem ineffective or damaging in our view. We wish to remain within legal requirements where it is necessary. We have our own strict views of what we do and what services we deliver. Because there is a mismatch between the case outcome and our mission, we must withdraw from France to remain in compliance with both law and our internal guidelines.
This is a terrible outcome, but it imposes the least amount of harm viewed over time longer than the duration of this case. We understand this will cause harm in the short term: users who do not know of our withdrawal will find our services unexpectedly unavailable. Users who have to move to different resolvers will not be protected by our cybersecurity capabilities, and they may choose to use resolvers that are less privacy-focused than Quad9. [...]

## [81] Legacy Modernization with LLMs: Is a Large Translation Consistent with Itself?
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~5404 words

Legacy Modernization with LLMs: is a large translation consistent with itself?
When we translate 600,000 lines of RPG, DDS, and CL into more than one million lines of Java code using LLMs, we want to know whether the resulting Java application will be consistent or it will look like a collection of incoherent code. We answer this question in this article.
We describe the experiment setup in article 1. We have seen that an application of this size does not fit in one agent session, so we divided the work into 49 phases following a plan of the dependencies, and each phase was a separate session that could only see the files already written by the previous ones.
This raises a question that does not exist for a small application: are all those sessions writing the same kind of code? In article 2 we saw that three independent translations of the same code take different design decisions, and 49 sessions working on the same codebase are, in a way, 49 translators who never talk to each other. Is this an additional issue to consider? To answer our question, we measured the entire codebase, using the snapshots taken after each phase.
This series
- Article 1: the experiments, the costs and the answers in short
- Article 2: what changes when we translate the same code three times, and the decisions behind it
- Article 3: whether the translations behave like the original
- Article 4 (this one): whether a large translation is consistent with itself
- Article 5: how I would approach a migration now
The experiments and their labels
- 1A, 1B and 1C are the three translations of five selected programs from Large, with access to all of Large’s source.
- 2A, 2B and 2C are the three translations of all of Small.
- Large was translated once, in separate sessions following a dependency plan produced by Strumenta’s tooling.
All runs used Claude Code with Opus 5.5. Our prompt said “Organize the project as you see fit”, and the agent ran headless: it could not stop to ask a client. We had no running IBM i, so when I say that a run agrees with the RPG, that comes from analysing the source, not from running the original.
Names are masked with asterisks or replaced by neutral names like Row, FIELD and ChildProgram. You know, privacy and all. The code shown is excerpted; … means omitted code or declarations joined from different locations.
Is the Java code consistent with itself?
At first sight, the answer is yes. [...]

## [76] Building a Continuous Software Engine the Hard Way
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): no readable article text (paywall, bot check, or not an article)) | ~46 words

After an overnight coding agent kept getting stuck, its orchestrator was rebuilt to manage state, retries, and independent review in code. The new engine landed 137 verified commits across three repositories in roughly 24 hours, including benchmarks and diagnostic writeups, and still hit a scheduler deadlock.

## [107] Netflix at QConSF 2026: Retrofitting the SDLC for AI Coding Agents
InfoQ | full text via InfoQ | ~746 words

At QCon San Francisco 2026, Mark Khuzam, senior software engineer at Netflix, described how the company's Commerce team retrofitted its software development lifecycle so that AI coding agents and engineers could ship together safely.
Khuzam argued that most of the work was not about agents at all, but about documentation, consistency and review.
Much of Commerce runs as server-driven UI, an approach Netflix has discussed at QCon before. A single screen-composition service behind the API gateway builds screens for iOS, Android, web and TV.
Khuzam opened with a mock company email announcing that every engineer now had Claude Code and asking how much faster everyone was shipping. The problem the team ran into next was summed up in one line.
Agents promised speed. But we spent 20 years building for humans.
The team's first attempt was having an agent migrate tests, and it took four tries. The team started with "migrate this file," then added instructions, then the APIs to use, then how to mock data.
The docs were also hard to find, since the agent's context window ran out before it found the right page. And they were inconsistent, because tests were not written the same way across the codebase.
Developers rated the internal framework at a Net Promoter Score of -3. Moving from one test to a whole feature, from screen to data to route to test, meant teaching the agent how the team builds.
Khuzam described the fix as context engineering, "getting what engineers know into what agents see." The team wrote 45 architecture decision records, each "written for people and for agents."
Each record covers the context, the decision, a pattern and an anti-pattern, and AI usage notes on what an agent should do. It also links to related docs and code, and the records now ship inside almost every repository.
To keep those records and more than 300 other documents findable, the team borrowed from how search engines read a site. An AGENTS.md file, the project instructions file that coding agents read before anything else, plays the part of robots.txt.
The second half of the talk followed code after an agent writes it. Khuzam noted that the CI pipeline is still deterministic, running builds, tests, screenshot diffing, merge queues and canaries.
What changed is how agents plug into each phase. A review agent pre-reviews each pull request against the docs and ADRs, flags anti-patterns and looks at what depends on the change. [...]

## [153] Linus Torvalds: "Tell Your AI Companion To Get Its Act Together"
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~61 words

A big EXT4 pull request today intended for the Linux 7.4-rc5 kernel has set off Linus Torvalds. Over 41k lines of new code in this EXT4 pull request going in as "fixes".... Much of that being new KUnit test coverage to make it safer to validate AI-generated patches. And then a lot of AI generated patches themselves for the EXT4 file-system...

## [220] How We Cut DynamoDB Ingestion Reads With an S3 Hash Pre-Filter
DZone | SNIPPET ONLY (DZone: HTTP 403) | ~82 words

The Setup Our team runs a customer data platform: a single source of truth for customer profile data, serving a high-volume read application programming interface (API) and ingesting changes from hundreds of upstream systems. The storage layer is Amazon DynamoDB in an entity–attribute–value (EAV) layout: the partition key is the entity ID, the sort key is the attribute name, and each item holds an attribute value plus a source version—the upstream update timestamp carried on that event. Ingestion runs on <a href="

## [125] Turning on Postgres logical replication without a restart
Dev.to | full text via Dev.to | ~1376 words

PostgreSQL 19 went GA on 19 November, five days before I wrote this, and one line in the release notes stopped me scrolling: logical replication can now turn itself on without a server restart, as long as wal_level is already set to replica. Adding logical replication to a database that's already serving traffic has always meant the same tedious step: ALTER SYSTEM SET wal_level = 'logical', then a restart, then the moment of "sorry, back in a minute" while the server comes back up with a different WAL level. So I pulled the GA image and checked whether that line in the release notes holds up.
The old way, and the new one
I ran two throwaway containers, both with wal_level=replica, nothing special:
docker run -d --name pg18 -e POSTGRES_PASSWORD=test -p 15433:5432 postgres:18 \
  -c wal_level=replica -c max_replication_slots=5 -c max_wal_senders=5
docker run -d --name pg19 -e POSTGRES_PASSWORD=test -p 15432:5432 postgres:19 \
  -c wal_level=replica -c max_replication_slots=5 -c max_wal_senders=5
On 18.7, asking for a logical slot at that wal_level gets you the error everyone who has done this before already knows:
$ psql -c "SELECT pg_create_logical_replication_slot('test_slot', 'pgoutput');"
ERROR:  logical decoding requires "wal_level" >= "logical"
On 19.0, the exact same command, same config, no restart in between:
$ psql -c "SELECT pg_create_logical_replication_slot('test_slot', 'pgoutput');"
 pg_create_logical_replication_slot
------------------------------------
 (test_slot,0/0175F720)
(1 row)
It just works. SHOW wal_level still reports replica - the setting on disk hasn't moved - but there's a new value that has:
$ psql -c "SHOW wal_level; SHOW effective_wal_level;"
 wal_level
-----------
 replica
 effective_wal_level
----------------------
 logical
effective_wal_level is new in 19. The server quietly runs at logical the moment something needs it to, and reports replica for everything else. That's the whole trick.
What the restart actually costs
To put a number on what this avoids, I did it the old way on 18.7: ALTER SYSTEM SET wal_level = 'logical', then a restart, while a second process hammered the server with SELECT 1 every 50ms and logged any failures. Three runs, each a fresh restart:
Then the same probe loop against 19.0 while I created a second logical slot in the middle of it - 200 probes at 50ms intervals, so a ten-second window either side:
no downtime observed
Zero failed probes. [...]

## [44] I checked Clojure's core with Lean and found 17 unreported bugs
Lobsters | full text via Lobsters | ~1800 words

I checked Clojure's core with Lean and differential testing and found unreported bugs in HAMT and vector-of
I read Koukyosyumei's article "著名なRust製OSSをLean 4で形式検証してみたら、めちゃめちゃバグが見つかった話" (in Japanese; the title means "I formally verified well-known Rust OSS with Lean 4 and found a lot of bugs"). The author ported well-known Rust projects into a form they could prove in Lean 4, and where a proof failed, they found a bug in the original code.
Many people have used Clojure's persistent data structures since around 1.0, so I expected no bugs to remain. Still, I wanted to see whether Lean would find something there too.
hirosassa/lean-verify describes a procedure for modeling a small function in Lean 4 and checking it for all inputs, so I applied it to the part of Clojure's core written in Java.
I modeled integer and bit arithmetic in Lean and searched for counterexamples.
I checked the collections with differential testing against the java.util collections, and for Java interop I compared the same call with and without a type hint.
I found 17 bugs that I could not find in Clojure's JIRA or on ask.clojure.org.
They include reduce on vector-of, the hash collision node of the HAMT, and calls to functional interfaces without a type hint.
The HAMT itself showed no mismatch in 3 million operations of differential testing, and the vector tree showed none around its boundaries.
The bugs sat in separate code outside the trees, and in places where two mechanisms meet, such as = and hashing.
I used Clojure 1.12.7, released on 2026-11-18, and JDK 21. The links to the source point to the clojure-1.12.7 tag.
How I checked
The lean-verify procedure picks one function and models it as a Lean definition.
You write a property that compares it with a naive specification computed at a wider width, and bv_decide searches for a counterexample.
If you model Java's long and int as BitVec 64 and BitVec 32, the wraparound of addition and multiplication maps onto BitVec operations.
So do the rounding of / toward zero and the sign of %.
When Lean found a counterexample, I turned the value into a Clojure input and reproduced it in the original code. I then modeled the fixed code in Lean and proved the same property. Lean can only take small functions that reduce to integer and bit arithmetic, so I checked the large persistent data structures with differential testing. [...]

## [189] Vercel will make AI providers prove they don’t keep prompts. Here’s why it matters for developers.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~24 words

Since April, developers using Vercel’s AI Gateway have been able to request provider-level zero data retention (ZDR). Vercel says its The post <a href="

## [186] OpenClaw at one: its chief architect on a year of explosive growth, wooing the enterprise, and being Meta’s muse
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~40 words

It’s been a whirlwind 12 months for OpenClaw, the open source personal AI agent used for everything from managing calendars The post OpenClaw at one: its chief architect on a year of explosive growth, wooing the enterprise, and being Meta’

## [173] Prompt Injection Fixes Need Regression Tests
Stack Overflow Blog | full text via Stack Overflow Blog | ~1437 words

A patched injection could come back after, say, a model upgrade with no change to the prompt. And catching it most often lies in simple delivery habits, like having a test that runs on every build.
Most engineering teams would without hesitation size up prompt injection as a security issue. That’s because companies build their security programs in a way that keeps security apart from delivery and doesn’t take into account the stakeholders who ship changes every week, where specialists run an adversarial review once or twice a year, patch whatever that review finds and move on. That kind of cadence made some sense when it was extended from legacy systems, where code changed through planned releases and a closed hole would usually stay closed between releases. But agentic systems have changed the pace, since an agent’s behavior can now shift between two reviews without anyone touching the reviewed code.
This matters because, unlike the slow-moving threats that review cadence was built for, an agent stack keeps shifting under the patch, and a model upgrade, a prompt edit or a new data connector can reopen a gap that was closed months earlier. And so an injection that circles back after it was patched is but a regression, and catching regressions is the job test suites already do. But then there’s also a timing gap, because a scheduled review checks the system at one moment, while a regression suite can run every time any part of that stack changes.
Agent Handoffs Were Never Built to Be Suspicious
Part of the reason these holes reopen is how agentic systems are wired. The output of one model becomes the input of the next. And nothing in that handoff treats what comes through with any suspicion.
Akash Agrawal, Vice President of DevOps and DevSecOps at TestMu AI, an agentic AI quality engineering platform, has worked where delivery pipelines and security controls meet, and in his current role he has spent much of his work on this failure mode. He warns that “a malicious instruction introduced into one model can propagate to others it communicates with, producing a chain reaction where compromised output becomes the next agent’s input.” The spread is hard to see from the outside, because a model can act on a poisoned instruction and still hand something downstream that looks like ordinary output. [...]

## [27] Three LLM inflection points in twelve months
Simon Willison's Blog | full text via Simon Willison's Blog | ~1282 words

Three LLM inflection points in twelve months
24th November 2026
I gave a keynote at the AI Engineer Code Summit a couple of weeks ago, constructed around the idea that there have been three significant inflection points in the abilities of LLMs and coding agents in the past twelve months.
Here’s the video of the talk. In this post I’m going to pull out the major inflection point theme and interrogate it more deeply.
Coding agents in November 2025
Today, November 24th 2026, is the one year anniversary of the release of Claude Opus 4.5. With hindsight, this was a consequential model.
In the Opus 4.5 announcement, Anthropic said:
Testers noted that Claude Opus 4.5 handles ambiguity and reasons about tradeoffs without hand-holding. They told us that, when pointed at a complex, multi-system bug, Opus 4.5 figures out the fix. They said that tasks that were near-impossible for Sonnet 4.5 just a few weeks ago are now within reach.
This held up.
Claude Code was 9 months old at that point, having been introduced alongside Claude 3.7 Sonnet on February 24th, 2025.
Opus 4.5 was the first model I had used with Claude Code where the default result was generally the right thing. I hadn’t been using Claude Code as a daily driver because it didn’t feel reliable enough—I had to correct it often enough that it didn’t feel like a clear accelerant.
The new Opus changed that. For most of the coding problems I faced on a daily basis, Opus would get them right. It was clearly faster than working through the problems myself.
Also in November, OpenAI released GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex, and GPT-5.1-Codex-Max. These had a similar effect on their Codex coding agent: it became reliably useful for many of my coding tasks.
The timing was convenient, because the December holidays were upon us. A lot of people, myself included, spent December tinkering with these new tools to see what they could do. By January we were ready to use them for our actual work.
Fable class models in June/July
We got our first hint of Claude Fable in April, when Anthropic announced Claude Mythos and said that it was too dangerous to release, due to its improved cybersecurity capabilities. Mythos was a model that could not just find security vulnerabilities, it could also figure out how to exploit them. [...]

## [72] Supercharging transformer residual connections
TLDR AI | full text via TLDR AI | ~1288 words

November 23, 2026
Kyriakos Axiotis, Staff Research Scientist, and Thomas Fu, Principal Engineer, Google Research
We present DeepCrossAttention (DCA), an architecture that enhances transformer networks by using learnable weights and depth-wise cross-attention to dynamically combine outputs from previous layers, preventing the information dilution seen in traditional residual connections. Presented in our ICML 2025 paper, this architectural improvement allows models to achieve the same quality up to three times faster with a negligible increase in parameters.
Think of a traditional deep learning model like a giant game of "Telephone": data passes through layer after layer, with each layer changing the information slightly. If a network has dozens or hundreds of layers, the original learning signal can become severely degraded or lost by the time it reaches all layers, which is known as the vanishing gradient problem in AI.
To overcome this challenge and enable the training of networks with dozens or hundreds of layers, transformers rely heavily on residual connections, also known as “skip” connections, which act like an information highway or a shortcut. Instead of forcing the data to pass exclusively through the complicated layer, a duplicate copy of the original input skips right past this layer and is added directly to its output. This ensures that the model always has the original raw data to refer back to.
The standard residual connection implements a simple operation: point-wise summation of a layer's output with its input. While computationally efficient, this simple process has a key limitation: it treats all prior representations with equal weight, leading to information dilution in deep networks. As features propagate through many layers, specific, high-resolution details from earlier layers can be averaged out or distorted, making it difficult for the network to selectively retrieve them. This forces the network to recompute them, reducing learning efficiency.
In our ICML 2025 paper, "DeepCrossAttention: Supercharging Transformer Residual Connections," we studied the shortcomings of the traditional residual architecture and introduced DeepCrossAttention (DCA), which generalizes residual connections by allowing each layer to dynamically select and route features from the history of preceding layers. [...]

## [149] Please don’t give the robot my SSH keys: How to keep AI out of trouble
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~17 words

Say a developer asks an AI agent to find out why a Kubernetes pod keeps crashing. The

## [77] Speeding Up Code Review with small-change
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1497 words

Speeding up code review with small-change
Imprint’s average engineer is merging 4x more PRs than 2 years ago. Yay. Aggregated behind the average is something even more interesting: we have two teams that are merging 10x their PRs over that period. One engineer is merging 25x the PRs per week of our average engineer two years ago, and a number of others are closing in on that number. That’s pretty neat, and the slope of the line suggests our average in a year is going to look much closer to today’s p90 than today’s p50. Even more importantly, we aren’t just shipping more, our quality has improved: incidents are down 42% half-over-half, and critical incidents are down 78% half-over-half. I think we’ve always known the quality/velocity tradeoff wasn’t a particularly useful construct, but that’s undeniable today.
As we’ve walked this path, we–like everyone else progressing down it–have run into the problem of pull request review. The p50 pull request review took about 33 minutes to complete 2 years ago, but now takes us about 77 minutes. The slope here correlates tightly with the number of pull requests getting merged. Tightly enough that addressing it became one of my priorities for the week.
We solved it! Just kidding, we’ve absolutely not solved it, but I think our current
approach is an interesting one, which we call the small-change.
The work discussed here was shaped and done by many folks at Imprint including Dan, Joy, Daniel, Lenny, Taylor, Ted, and Annie, among many others.
Why review pull requests?
There are four reasons we review pull requests:
- Knowledge sharing between author and reviewer – software engineering is generally learned via apprenticeship, and reviews are a primary mechanism of experienced engineers teaching others what good software looks like. We believe the current volume means that this knowledge sharing will have to move towards operating on clusters of pull requests, rather than individual pull requests
- Preventing errors – review has always been an expensive time to catch errors, and we believe that effective CICD along with harness verification techniques like poteto’s pstack are more effective mechanisms for preventing errors than review
- Preventing malicious behavior – my experience is that even careful code review will generally miss competent malicious behavior, although fortunately most malicious behavior is incompetent. [...]

## [183] TornadoVM 8.2 Released With ROCm HIP Backend For AMD GPUs
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~48 words

TornadoVM is the Java programming framework that allows Java code with OpenJDK 21+ to JIT compile to NVIDIA CUDA, OpenCL C, Apple Metal, and now even AMD ROCm HIP too. TornadoVM 8.2 is out today as the newest feature update for this Java framework for GPU kernel programming...

## [214] After token leaderboards and spending caps, Snowflake has a third idea: Keep the cap, then learn from whoever breaks it
VentureBeat | SNIPPET ONLY (VentureBeat: HTTP 429) | ~41 words

Snowflake sets limits on what its employees spend on AI, and then studies the employees who blow through the limits. The data cloud company treats an overrun as a possible lead on a workflow that other employees could copy. Read more

## [145] Maple raises $5.3M to build AI products that protect your data, even from itself
TechCrunch | full text via TechCrunch | ~1048 words

As AI assistants evolve into more capable agents that can access our files, emails, calendar, browser, and more, the amount of trust we’re expected to place in AI companies is growing. One startup called Maple, co-founded by a former Apple engineer who worked on privacy-preserving technologies, is taking a different approach with its AI app, where users’ data remains private — even from the company itself.
“We wanted to build something that was not only encrypted but also could be proven, and that people could go look at the open-source code, and then they could look at what we call trusted execution environments,” explains Maple co-founder and CEO Mark Suman. “They can look at and verify the code that’s running on our servers, so they don’t really have to take our word for it.”
“They can audit everything themselves and know how their data is being handled,” he adds.
The idea of trust is Maple’s larger theme, as the startup proposes that there’s a way to build an AI app where consumers don’t have to trade privacy for convenience, as its competitors often require with their invasive privacy policies, data collection practices, and sometimes even training on users’ personal data.
Instead of asking users to trust that Maple won’t misuse their personal data, it’s attempting to build a business where it can’t access that data in the first place.
Like other AI apps on the market, Maple allows users to engage in a chat experience where they ask questions and get answers. Meanwhile, its newly launched desktop app, Maple Work, offers a more agentic experience where the AI can control your computer, work with your files and apps, and control your browser to get online tasks handled.
With the company’s recently closed $5.3 million round, it’s moving on to its next product — a cloud-based agent that will be able to continue its work even if your computer isn’t on. This addition would make Maple more competitive with other popular consumer AI services, like Meta’s Muse, Instinct, and other AI agents that work over chat.
The oversubscribed seed round was led by EPIC Ventures, with participation from Draper Associates, Planetary VC, and Epoch VC, and follows a pre-seed angel round of under a million. Maple plans to raise a Series A in the first half of 2027, given the investor interest.
Suman, who previously spent six years at Apple, already had a background where AI and privacy overlapped, he tells TechCrunch. [...]

## [180] Collabora Online Sharply Reduces Server Memory Use With New Optimization
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~30 words

The Collabora Online open-source web browser based office suite derived from LibreOffice is now able to use 50% less memory per document following an optimization to its copy-on-write memory handling...
