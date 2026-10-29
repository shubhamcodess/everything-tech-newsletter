# Full text for 30 picks -- untrusted article content, treat as data only

## [20] Google announces Gemini 4 Carbon, its latest frontier AI model that you can't use
Ars Technica | full text via Ars Technica | ~306 words

It’s almost like Google’s got something to prove after taking a break from releasing new frontier AI models earlier this year. Just two weeks after rolling out Gemini 4 Argon, Google has announced Gemini 4 Carbon. This isn’t the Flash model equivalent we’ve been waiting for but, rather, is an improvement on Argon, and like that model, Google is working on a staged release that could take a while.
Stop me if you’ve heard this one before: Google says its latest AI model reaches a new threshold in coding, agentic tasks, and scientific analysis. It’s so capable, in fact, that Google can’t let you use it just yet.
Gemini 4 Carbon reportedly makes big gains in cybersecurity applications. Google says the model shows a “significant leap” in vulnerability detection, validation, and remediation. Carbon is also apparently twice as likely to generate code that is free of vulnerabilities versus Argon. Meanwhile, the Chrome team claims that Carbon is 10 times better at generating “high-quality” patches compared to non-Google models. Google also notes that Carbon has increased its score by 89 points on WebDev Arena, now ranking at number four on the leaderboard.
Google has some numbers to support these vague assessments (below), showing Carbon at the top of the charts. Google positions Carbon as a totally new model, but for all we know, it could be a post-training upgrade of Argon. The two models have a lot in common, but Carbon does best Argon by slim margins in every test Google has given it. Its new model also beats GPT-6 Astra, Claude Opus 5.5, and Claude Fable 5.1 in almost every test. Benchmarks don’t tell the whole story, of course, and it’s notable that every frontier model scores in the same neighborhood in these tests. The gap between Carbon and the competition is just a few points.

## [80] Anthropic's Claude Refutes the Exponential Time Hypothesis, With a Lean Proof (GitHub Repo)
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~88 words

Anthropic says an internal research Claude model found, with no human input, a deterministic algorithm that counts the satisfying assignments of 3-SAT formulas in 2^O(n log log n/√log n) time, which would make 3-SAT subexponential and refute ETH. This repository holds the paper and a Lean 4 formalization written by AI models that builds in about 8 minutes, though Anthropic notes no machine checks that the Lean statement matches the paper and the result says nothing about practical SAT solving. It landed hours after OpenAI's own ETH refutation.

## [47] Microsoft's October Security Update Fixes 1,400+ Vulnerabilities, One Exploited in the Wild
InfoQ | full text via InfoQ | ~457 words

Microsoft's latest monthly security update addresses 1415 vulnerabilities across multiple products. One vulnerability affecting Windows Shell has been exploited in the wild, while 85 are classified as critical. Affected products include Windows OS, Office, Exchange, .NET, Edge, as well as potentially Hyper-V and Azure components.
CVE-2026-96951 enables to inject special elements into Windows Shell, "allowing an unauthorized attacker to bypass a security feature over a network", specifically the Mark of the Web (MOTW) defenses. Microsoft notes that a potential attack vector is an email or instant message containing a maliciously crafted file designed to exploit the vulnerability. However,
In any case an attacker would have no way to force a user to view attacker-controlled content. Instead, an attacker would have to convince a user to take action. For example, an attacker could entice a user to either click a link that directs the user to the attacker's site or send a malicious attachment.
Reddit user falconupkid, a moderator of the r/SecOpsDaily community, warned that
With this volume, expect a high number of "wormable" or pre-auth RCEs that will require immediate prioritization. The sheer noise will make it easy to miss the critical few.
They also pointed out that, given the scale of the patch, the window between vulnerability disclosure and exploitation should be considered "effectively zero". They recommends prioritizing all CVEs with a severity higher than 9.0 and planning remediation accordingly, including against potential regressions.
Security expert Brian Krebs highlighted a vulnerability in the .NET Framework allowing a security feature bypass; CVE-2026-108398 "was publicly disclosed prior to today, potentially giving attackers advance time to work out how to exploit the bug". However, Microsoft reported no evidence of exploitation to date.
Reddit user Odd_Round9576 shared their negative experience after applying one of the patches, confirming the importance of deploying updates in stages, rather than all at once, and monitoring for potential regressions:
Be careful with KB5127648 - it broke our WPA-Enterprise Wifi. After installing and rebooting, clients were no longer able to join a WPA-Enterprise network. Uninstalling the update resolves the issue
On a similar note, Appropriate-Pipeline6575 reported that the update broke their IPSec VPN on some laptops, preventing coworkers from connecting. [...]

## [26] GitLab security incident: attempted exploitation of CVE-2026-97229 | Alpine Linux
Lobsters | full text via Lobsters | ~1040 words

GitLab security incident: attempted exploitation of CVE-2026-97229
On October 20 and 21, an attacker tried to exploit a GitLab vulnerability (CVE-2026-97229) on our instance, a week after the fix was released. The attack came close to working. We have found no evidence that it succeeded, but we cannot rule it out, so we treated the instance as compromised and rebuilt it from scratch. Our checks show that the aports repository, packages, and the October 21 releases were not tampered with.
GitLab is being tested before we open it to the public again. All passwords have been reset, so when it is back you will need to set a new one with “Forgot your password?” on the sign-in page. We will post exactly what you need to do when it reopens. In the meantime: if you used the same password for your gitlab.alpinelinux.org account anywhere else, change it there. We have seen automated login attempts against our GitLab with passwords leaked from other sites.
If you have questions or concerns please reach out to us at infra@alpinelinux.org.
What happened
The vulnerability: CVE-2026-97229 is a critical (CVSS 10.0) vulnerability in how GitLab evaluates regular expressions in CI configuration. The underlying bug is in Onigmo, the regular expression engine built into Ruby. GitLab published fixed releases on October 12, but the fix itself is a set of patches to the Ruby that GitLab bundles in its own packages and container images. Upstream Ruby shipped the fix on October 23, in Ruby 3.3.13, 3.4.12 and 4.0.9.
The attack: On October 20 and 21, a newly registered account sent crafted CI configurations to our GitLab instance, which was still running 19.3.4 and did not have the October 12 fix. This crashed GitLab worker processes 8 times. In 4 of those crashes the attacker got partway through the exploit and failed at the next step. The attacker also downloaded our GitLab container image, which suggests they were tuning the exploit to our exact build. We have found no evidence that the attacker ran code on the server, but we cannot rule it out.
Our upgrade didn’t fix the vulnerability: Upgrading to GitLab 19.3.6 on October 22 didn’t fix the vulnerability. The fix isn’t in GitLab’s own code but in a patch to Ruby, which GitLab applies only in its official packages. Our image used standard Ruby, so it didn’t get the patch. [...]

## [128] Hacker stole personnel data about thousands of Homeland Security employees, including CBP and ICE agents
TechCrunch | full text via TechCrunch | ~1105 words

Personally identifiable information belonging to thousands of U.S. Department of Homeland Security employees has been published online after a hacker stole reams of data in a previously undisclosed breach at the government department earlier this year.
The breach includes names, job titles, and work contact information, such as email addresses, cell phone numbers, and office locations, of more than 40,000 people who work for the federal department, including border and immigration agents, cybersecurity staffers, and senior department officials.
A hacker who goes by the handle Department of Peace claimed they obtained the data from an Okta single sign-on system used by Homeland Security to allow employees and contractors across its various agencies to log in to its central network. The Okta system also contains IT and log-in records associated with the employees’ user account, including details about which systems and internal apps they are permitted to access.
More than half of the dataset — some 21,000 records — relate to employees with U.S. Customs and Border Protection (CBP), who work at airports and other ports of entry.
The data also contains records associated with another 10,000 employees of Immigration and Customs Enforcement (ICE) and its Homeland Security Investigations (HSI) unit, and just under a 1,000 employees who work at U.S. cybersecurity defense agency CISA.
Thousands of additional records relate to staff who work at the department’s headquarters and its other agencies, including U.S. Citizenship and Immigration Services and the Federal Protective Service.
“They have our information, so it’s only fair that we have theirs,” said Department of Peace in a note left with the data, which TechCrunch has seen. The hacker did not respond to TechCrunch’s email requesting comment and with questions about how the breach was carried out.
This is the latest data breach to hit the U.S. government in recent months, following earlier hacks involving the theft of thousands of FBI agents’ personnel records and the personal information of millions of serving and former military service personnel from the Pentagon’s human resources unit. It’s also the second breach involving Homeland Security this year, after the same hacker claimed to have taken thousands of contracts between the department and the private sector, including defense contractors and surveillance vendors. [...]

## [179] GitHub debuts Copilot Fusion, a new model selection & orchestration system that beats Claude Code for half the API cost
The New Stack | full text via The New Stack | ~746 words

GitHub debuts Copilot Fusion, a new model selection & orchestration system that beats Claude Code for half the API cost
GitHub has debuted GitHub Copilot Fusion, a new system that handles model selection and orchestration for coding tasks so developers don’t have to.
Combining the advanced runtime model orchestration from Project HydraFusion with Copilot Auto Model Selection, Copilot Fusion can now handle both model selection and orchestration. GitHub says Fusion Max delivered comparable benchmark performance to Claude Code with Opus 5.5 Max at about half the average API cost and in about 40% less time per task.
Generally available now, GitHub Copilot Fusion is part of GitHub’s new vision to make GitHub “the most comprehensive software delivery system in the world,” with developers delegating model choices while retaining responsibility for the direction and outcome of the work.
GitHub announced the news on Wednesday at GitHub Universe in San Francisco, the company’s flagship developer event.
GitHub Copilot Fusion is the decider now
For tasks involving reasoning, code generation, debugging, or tool use, GitHub says developers can delegate decisions about which models to use and how they work together. Its instructions: “choose Copilot Fusion and let Copilot intelligently route and orchestrate which models it uses for you.”
That sounds like a time-saver, since different tasks benefit from different models based on capabilities and cost. With Copilot Fusion working as the “model picker,” developers don’t have to weigh performance and price for every task.
More compelling is the idea that developers can use Copilot Fusion to strategically switch models mid-workflow, letting the system jump between models based on what best suits each step.
After analyzing what the task requires and choosing a model, the system orchestrates the next steps based on what makes the most sense. That may be a single model doing everything, a “cascading” workflow where a quality check evaluates one model’s response and then decides to accept it or escalate it, or a “critique” workflow where one model reviews another’s work.
That could reduce the mental load for developers who may inadvertently choose inefficient models when their attention drifts. [...]

## [53] Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope
InfoQ | full text via InfoQ | ~732 words

Cloudflare recently made Quicksilver available to customers for the first time, as a new mode for Workers KV called KV Instant. Reads resolve in 1.62 ms at the 99th percentile, compared with 287 ms for classic KV. What determines whether a team can use it isn't the latency, but the envelope around it.
Quicksilver is Cloudflare’s own configuration store, introduced in 2020. Nearly every request to Cloudflare looks up at least one key in it, Rob Sutter writes, and it has never been a customer-facing product. Brendan Irvine-Broque, who works on Cloudflare’s developer platform, announced the change on X:
we have this crazy key-value store at Cloudflare called Quicksilver
instantly updates keys across our whole network. microsecond reads from every location. stupid fast
our customers have asked us for years to make it available
we finally did – in a way we think is quite simple - as a new mode for Workers KV
The published figures, measured to over 300 edge locations:
Cloudflare notes it has no sub-second fidelity for replication lag in classic mode, so the classic median and p95 figures are upper bounds rather than measurements. p95 reads in Instant mode are reported in microseconds.
The API is the Workers KV one, with three differences. Mode is set at namespace creation with a "mode": "instant" attribute, and cannot be changed afterward. Metadata is unsupported, so getWithMetadata always returns null. And list returns every matching key with no pagination.
Then the limits. A namespace holds at most 10,000 key-value pairs and one megabyte in total, with keys up to 300 bytes. Writes are capped at one per namespace per second, which Cloudflare contrasts with classic KV’s one write per key per second, on the grounds that a single system of record "makes it easier for you to reason about update order in your application." That difference is the one most likely to catch a team migrating: a pattern classic KV permits across many keys concurrently becomes a single serialised queue.
Pricing points the same direction, and Cloudflare says so plainly: "storage and Class A operations are significantly more expensive than Workers KV."
Reads cost 60% less. A write costs ten cents, against five dollars per million in classic mode. Storage runs $100 per megabyte per month, and since a namespace tops out at one megabyte, that is also the ceiling. Multi-key reads bill per key, so requesting three keys in one get costs the same three Class B operations as three separate calls. [...]

## [35] Octoverse: Commits, pushes, reach new highs in 2026 as developers build with agents
GitHub Blog | full text via GitHub Blog | ~3147 words

GitHub Staff
GitHub is the world's best developer experience and the only AI-powered platform with security incorporated into every step, so you can innovate with confidence.
See how a record year of growth reached every industry, every field, and every kind of builder in the 2026 Octoverse report.
Developers pushed code to GitHub 17.9 billion times in the past 12 months, more than in 2024 and 2025 combined.
Behind that number are developers building what interests them and what their communities need. In Nepal, one developer built a flood bulletin on GitHub Pages with verified information on roads, rescue, weather, and power. It has since grown into Gati, a Nepali-first relay of official disaster alerts that runs on GitHub Pages and Actions. Elsewhere, developers at NASA’s Jet Propulsion Laboratory are creating software designed to run programs aboard spacecraft, and fans built open-source firmware that lets people customize their e-readers. Curiosity, aimed in every direction, at a scale GitHub hasn’t seen before.
That growth happened quickly. Partway through the year, activity on GitHub bent sharply upward, just as agents went from something developers were trying out to something they were working alongside. Developers picked from more models than ever and built in industries we are highlighting in this report for the first time, from health care to agriculture.
Octoverse is our chance to step back and look at the whole picture. This year, that picture is bigger than ever. Here is what stood out most:
Underneath it all, AI models and the harnesses built around them have advanced over the past year, and developers have more to choose from. Growth is moving quickly: one year into last year’s five-year developer growth projections, every country we projected has already closed at least a fifth of its distance to 2030, and our own forecasting models no longer agree on where it will go next.
This year was all about momentum. Developers pushed code changes to GitHub 17.9 billion times in the past 12 months, more than 2024 and 2025 combined. Commits across all repo types (public and private) climbed even faster to 34.3 billion, more than three times where they stood two years ago. Merged pull requests more than tripled to 1.3 billion over the same period, an average of 3.5 million a day.
Agents were one of the tools developers leaned on hardest this year, pulling them deeper into daily work. [...]

## [41] Airbnb Cuts Recommendation Staleness from 2 Days to Seconds with Chronon
InfoQ | full text via InfoQ | ~489 words

Airbnb has extended its open source Chronon feature platform with Push Mode and Near Real Time (NRT) Model Transform to update sequence based recommendation embeddings within seconds of guest activity. The change reduced embedding staleness from nearly two days to less than a minute, with typical updates arriving within 10 to 30 seconds. Airbnb also reported a 1.67% improvement in offline NDCG and an approximately 0.33% increase in uncancelled bookings in online A/B testing.
The work builds on Airbnb’s JourneyFormer based sequence recommender, which uses a Transformer encoder to represent a guest’s booking, review and browsing history. Previously, the encoder ran as a daily batch job, generating embeddings that were stored in a low latency store. During a search, the ranking system retrieved the latest embedding and combined it with the live query, keeping the Transformer outside the latency sensitive serving path. However, activity occurring after the daily batch could remain absent from the embedding until the following run, with processing delays bringing effective staleness close to two days.
Airbnb’s initial architecture showing the daily batch sequence encoder, embedding store and online ranking path. (Source : Airbnb Blog Post)
Airbnb addressed the freshness problem by adding two capabilities to Chronon. Push Mode causes a streaming job to publish a notification when a feature value is committed, allowing downstream processing to react to updated guest activity rather than polling or waiting for a scheduled job. NRT Model Transform allows an already deployed model to run inside that streaming pipeline. Airbnb uses the same Transformer sequence encoder for the near real time path, avoiding a separate inference implementation for the streaming workflow.
The resulting pipeline captures events such as searches and listing views, combines them with the guest’s existing short and long-term sequence data, and triggers model inference when the updated feature state is available. The generated embedding is then written to the same low-latency store used by the batch system. Consequently, the online ranking path remains largely unchanged while the representation it retrieves becomes more current.
Pengyu Hou, Senior Software Engineer, Infrastructure at Airbnb, described the platform change as addressing the gap between event-driven data and model inference:
NRT Model Transform lets Chronon call an already deployed model ... [...]

## [172] Amazon Finds 'Tokenmaxxing' Lacks Productivity Gains
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~97 words

Ancient Slashdot reader Gilmoure shares a report from Tom's Hardware, adding: "Huh. Looks like consuming one's own slop does not turn the wheels of industry." From the report: Amazon wants its engineers to quit chasing token counts, warning that heavy AI usage does not automatically mean better work. In updated engineering guidelines published on October 27, the company laid out how developers and managers should gauge AI's real impact -- and the takeaway is blunt: consuming more tokens is not the same as delivering more value. [...] According to the memo, metrics such as AI adoption rates,

## [135] Upwind raises $400M after walking away from Datadog acquisition offer
TechCrunch | full text via TechCrunch | ~385 words

Upwind, a San Francisco startup that uses AI to secure cloud infrastructure, has raised a $400 million Series C round at a $3.8 billion valuation led by Bessemer Venture Partners, with participation from existing backers including Greylock Partners and Craft Ventures.
The round comes nine months after Upwind closed its previous $250 million financing at a $1.5 billion valuation.
The fresh funding, which has been in the works for months, nearly fell apart after Datadog attempted to buy the company, according to a person familiar with Upwind. Datadog is a publicly traded company that sells tools for monitoring how software runs, known as observability. It didn’t offer a premium above the $3.8 billion valuation set by venture capital investors, the person said, so Upwind decided to stay independent.
Four-year-old Upwind has grown rapidly amid rising AI-driven cybersecurity threats. The startup has been adding $20 million to $30 million in annualized recurring revenue (ARR) each quarter and is projected to end the year at roughly $90 million, according to a person familiar with Upwind’s financials. That means that VCs and Datadog valued the startup at more than 40 times its forecast ARR, a common yardstick for pricing software companies. The high multiple is also well below the 80x ARR fetched by Cyera, another fast-growing cybersecurity startup, according to TechCrunch reporting from earlier this year.
Cybersecurity is poised to be the third big wave of AI software that companies will pay for after AI coding tools and customer support, Theory Ventures general partner Tomasz Tunguz recently wrote in his widely read blog.
By walking away from an acquisition offer, Upwind clearly believes that the company will ultimately be worth more than the $3.8 billion that Datadog was ready to pay for it. However, given how few cybersecurity companies have gone public in recent years, an eventual sale remains the most likely outcome for the startup.
Upwind continues to draw acquisition interest, according to a person familiar with the company.
The startup was founded by Amiram Shachar, who sold his previous company, the cloud spend management startup Spot.io, to NetApp for $450 million. Upwind calls its approach to thwarting threats “runtime” security, which means it alerts and remedies attacks and vulnerabilities in active services in real time.
TechCrunch has reached out to both Upwind and Datadog for comment.

## [124] Microsoft just shared Azure’s actual revenue in dollars: $33.2 billion
TechCrunch | full text via TechCrunch | ~315 words

Microsoft has never disclosed Azure’s quarterly revenue in dollars. It has typically only shared a growth percentage or described revenue dollar milestones in vague ways. But on Wednesday, when it posted another record-breaking quarter, it reported that Azure brought in a healthy $33.2 billion in revenue for the July-September quarter, up 48% from a year earlier.
The disclosure lets investors line up Azure’s performance more directly against Amazon Web Services and Google Cloud, whose parent companies already report cloud revenue in dollars every quarter.
Alphabet, which also reported earnings on Wednesday, said Google Cloud brought in $30.7 billion in the same quarter, putting Azure slightly ahead. But Google Cloud, which also includes Google’s Workspace subscriptions, roughly doubled its revenue from a year earlier, growing about twice as fast as Azure, according to TechCrunch’s calculations.
Azure, where businesses rent computing power to run applications, SaaS, and to build and run AI models, is now Microsoft’s largest and fastest-growing product line by the company’s own figures. It accounted for roughly 36% of Microsoft’s $92.3 billion in quarterly revenue.
Azure’s revenue was also about $850 million more than the $32.3 billion analysts expected. Azure’s 48% growth rate also topped the 44% to 45% that Microsoft CFO Amy Hood forecast on the company’s July earnings call.
Azure sits inside Agents and Infra, one of two new business segments Microsoft introduced this quarter. Microsoft previously reported three segments, Productivity and Business Processes, Intelligent Cloud, and More Personal Computing. The new Agents and Infra segment, which groups Azure with Microsoft 365’s cloud business, brought in $76.8 billion, up 25% from a year earlier.
Amazon reports its earnings on Thursday. Analysts also expect its cloud, Amazon Web Services, to grow. It’s been the largest cloud since the beginning of time and no one expects Microsoft to best it right now. But with all of them reporting actual dollars, the race is on.

## [182] FCC Approves Amazon Leo's $11.5 Billion Acquisition of Globalstar
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~87 words

The FCC has approved (PDF) Amazon Leo's $11.5 billion acquisition of satellite operator Globalstar, giving the Starlink rival additional infrastructure and spectrum to expand into direct-to-device satellite connectivity. Engadget reports: You may not know Globalstar but have possibly used its services, as the company provides Apple's emergency satellite connectivity for compatible iPhones and Watches. Interestingly, Apple also held a 20 percent stake in Globalstar prior to its takeover. As part of the deal, Leo will power satellite services for supported iPhone and Apple Watch models. Leo, a

## [49] Chrome Opens Trial for the Email Verification API: Letting Sites Verify Without Sending Emails
InfoQ | full text via InfoQ | ~538 words

Google has opened a Chrome origin trial for the Email Verification API, a WICG proposal that lets a browser confirm a visitor owns the email address they typed, without sending a single message. The trial began in Chrome 150 on desktop, with Gmail taking part as the first participating provider.
The idea replaces the familiar one-time code or magic link. Today a user enters an email, leaves for their inbox, copies a code, and returns, a context switch that often loses them. The proposal uses a three-party model where the browser sits between the site (the "verifier") and the mailbox provider (the "issuer"). If the user is already signed in to their provider, the browser quietly fetches a signed token and drops it into the form, and the server validates that token on submission. Google notes the issuer never learns which site made the request.
For developers the front end implementation is fairly straightforward. The email field needs an autocomplete hint, plus a hidden input carrying a session-bound nonce:
<input id="email" name="email" type="email" autocomplete="email">
<input type="hidden" name="token" nonce={nonce} autocomplete="email-verification-token">
The heavier work sits on the server side, where the token's signature is checked against the provider's keys. Resend's Phil Nash, who wrote a walkthrough of the flow, published an npm package and a Next.js example to handle that parsing and validation.
On Hacker News a developer said there is "literally no worse context switch" than hopping to an inbox mid sign-up, and that email verification had cost them "dozens, maybe hundreds" of registrations they never finished. Another pointed out that verification mail is frequently blocked or filtered to spam, with no visible difference between delayed and lost messages, so removing it is a genuine win.
One commenter argued the privacy claim is thin:
Make everything what works complicated.
There is no advantage.
"User privacy is enhanced as the issuer does not learn which web application is making the request as the request is mediated by the browser." Every web application nowadays send you a welcome, onboarding, reminder after the verification. (No user privacy enhancement)
So we get a new process that solves nothing, but makes everything complicated. (And complicated helps the big and hurt the little in th long run)
Not verified but feels like a Google draft that closes the web. [...]

## [81] How Meta Built Forum With AI-Native Engineering
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1742 words

- Meta’s newest app, Forum, is for anyone who wants to go deeper into the conversations in their Facebook groups.
- To build Forum, Meta engineers adopted a whole new way of working by bringing an AI agent into the development cycle.
- We’re sharing insights into what it took to build Forum with agentic AI: how we adapted the codebase, tested frameworks and internal tooling for agentic execution, what worked, and what didn’t.
Forum is a standalone Groups app that a small team built from scratch. It’s also where we tested a different way of working: treating an AI agent as a participant in the engineering process rather than a faster way to type.
That experiment needed a definition of success, and ours wasn’t code volume. We measured verified, production-ready outcomes — changes that build, pass tests, and survive review.
From Human-In-The-Loop to Human-On-The-Loop
Pointing AI at the coding step alone doesn’t change much. Our results compounded as we extended the approach to the stages around implementation — planning, building, testing, and verification. The clearest way to see the shift is in who owns each step.
With human-in-the-loop, the engineer drives every step and the AI assists inside it by autocompleting a function, suggesting a fix, or answering a question. Each iteration advances at the pace of the person driving it.
With human-on-the-loop, the agent runs the iteration itself — plan, implement, build, test, correct, repeat — while the engineer sets the goal, watches the run, steps in when it drifts, and approves the result. The person’s job moves from executing the steps to owning the outcome and holding the quality bar. This is the target we are driving toward, not a finished state: some stages run autonomously today, while others still keep an engineer in each iteration.
When the engineer supervises, work stops being strictly sequential. Cycles that used to run one at a time can overlap, and an engineer’s time goes to direction and judgment rather than to sitting through the loop. But that only holds if what comes back can be trusted. Without verification, AI-generated code creates a familiar problem — plausible output that no one has confirmed actually works, which an engineer then has to read, debug, and often discard. Weak signals don’t remove the constraint; they move it from writing code to reviewing code that looks finished and isn’t.
So we set the bar at verification rather than compilation. [...]

## [73] Formalizing the Enormous Theorem
TLDR AI | full text via TLDR AI | ~4099 words

Today, we are releasing the first complete computer-checked proof of the Classification of Finite Simple Groups (CFSG). One of the major achievements of twentieth-century mathematics, the classification identifies the basic building blocks of finite groups. Widely considered to be the longest mathematical proof ever written by humans, the original proof of CFSG extends across roughly 15,000 pages in more than 500 articles by about 100 mathematicians, earning CFSG the nickname “the enormous theorem.” For his crucial work on the classification, John Thompson was awarded the Fields Medal (1970) and the Abel Prize (2008). Over 24 days, engineers and mathematicians at Axiom Math directed swarms of dozens of AI agents in a project that produced approximately 43.1 million lines of code in the Lean proof assistant.
Groups are fundamental objects that describe symmetry, introduced early in undergraduate mathematics. Take a cube. There are 24 ways to rotate it so that it looks exactly as it did before: any of its 6 faces can end up on top, in any of four orientations. Applying two of these rotations gives another of the 24, and any rotation has an inverse. A group is a collection of transformations with these two properties. The permutations of a deck of cards provide a much larger example of a finite group.
Finite groups can be broken down into indecomposable factors, in a sense given by the Jordan–Hölder theorem. These factors, the “atoms” of finite groups, are the finite simple groups. The classification gives a complete list of these building blocks: a periodic table of finite symmetry.
To formalize the proof, we rewrote it in Lean, a programming language in which mathematical definitions, statements, and proofs can be written precisely enough for a computer to check every step. The process of translating the work leading to CFSG into Lean exposed problems in the published arguments. Most were minor, such as typographical errors, errors in tables, or dropped hypotheses. However, there were 34 noteworthy deviations from the published record that needed to be resolved, the most substantial of which related to the Unbalanced Group Theorem. The work also produced a new result in group theory, whose statement and role in the proof are discussed below. In consultation with several expert group theorists upon whose work the classification rests, we will make the lengthy errata list available for the benefit of all. [...]

## [110] Uber Moves beyond CPU Cores with Performance-Aware Scheduling for Stateful Workloads
InfoQ | full text via InfoQ | ~652 words

Uber has introduced Normalized Compute Units (NCUs) to make CPU allocation more consistent across its highly heterogeneous server fleet. The approach, implemented in Uber's Odin stateful orchestration platform, accounts for differences in processor performance rather than treating every CPU core as equivalent.
Odin manages around 5 million CPU cores across on-premises data centres and public clouds, including multiple generations of x86 hardware and ARM processors. Uber found that single-threaded performance can vary by almost a factor of two between the fastest and slowest cores. Consequently, the same workload can require significantly different numbers of physical CPU cores depending on where it runs.
The problem creates two competing risks. Allocating resources according to the slowest hardware can waste capacity on faster machines, while allocating according to average usage can leave workloads under-provisioned when they move to slower servers. For stateful workloads, where moving traffic to another machine is often not possible, the latter can become a reliability problem.
Uber's solution is to separate the amount of compute performance a workload requires from the physical cores used to provide it.
Odin assigns each server type a performance factor, using an older server generation as a baseline of 100. Newer hardware can have considerably higher values; Uber reports factors approaching 190 for some servers. These factors are initially determined during hardware qualification and then refined using production workload data.
CPU usage is converted into normalized units using these factors. Odin can then determine that a workload requires a particular amount of compute capacity and translate that requirement into a different number of physical cores depending on the server hosting it.
A workload on faster hardware may therefore receive fewer cores, while the same workload on slower hardware receives more. The objective is not to make the number of cores identical, but to make the computational capacity more comparable.
Uber also found that performance factors differ between technologies. Its measurements for Kafka, for example, showed substantially different performance between ARM, older on-premises hardware, and newer x86 systems. The company therefore updates factors using production measurements rather than relying exclusively on synthetic benchmarks. [...]

## [131] Nvidia wants to turn old nuclear power plants into huge AI data centers — but says it draws the line at turning them back on
TechRadar | full text via TechRadar | ~636 words

Nvidia wants to turn old nuclear power plants into huge AI data centers — but says it draws the line at turning them back on
Could decommissioned nuclear sites really host data centers?
- Nvidia wants to turn Germany's retired nuclear sites into AI data centers
- Germany's nuclear shutdown leaves dozens of former power stations awaiting dismantling
- Nvidia and PreussenElektra are investigating new uses for Germany's retired nuclear facilities
Nvidia has agreed to examine whether shuttered German reactor sites could become computing hubs, though the company rules out restarting any idle units.
The US chipmaker signed a preliminary agreement with PreussenElektra GmbH (PEL), a utility from Germany, to study the idea at decommissioned locations.
The arrangement does not involve generating electricity from fission for any future facility, since the work concentrates on existing grid links and water access.
Reusing sites without reviving reactors
Following the Fukushima incident, Germany permanently closed its final operating reactors in April 2023 and is now dismantling about 30 atomic stations nationwide.
PreussenElektra oversees the closure and teardown of eight of those stations, and these are probably the locations that will receive scrutiny.
Neither company has named the sites under review, so the eight locations managed by PreussenElektra remain an assumption rather than a confirmed list.
“Our former power plant sites have valuable industrial infrastructure and offer opportunities for new, future-oriented uses,” said Guido Knott, chairman of PEL’s management board.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
“Together with NVIDIA, we intend to conduct a sound assessment of whether and how these conditions can be leveraged for AI factories.”
The assessment will review grid connections, open land and industrial infrastructure to judge whether each site satisfies the strict operating requirements of AI factories.
The two companies say they will test whether the sites can meet engineering and running needs while supporting Germany's computing capacity for AI.
Cost savings and an unproven case
New data center facilities normally need well-located land, industrial zone approvals, access to water for cooling, and powerful grid connections, which former atomic stations already possess. [...]

## [175] Google just handed its rivals the keys to Android
The New Stack | full text via The New Stack | ~742 words

Google just handed its rivals the keys to Android
Google is giving coding agents like Anthropic’s Claude Code and OpenAI’s Codex deeper access to its Android development tools, including devices, performance profilers and production crash reports; now, agents can now investigate bugs, test changes, and verify their own fixes.
The push spans Android Studio and the terminal-based Android CLI, with Google opening both to third-party agents rather than steering developers toward Gemini. Matthew McCullough, vice president of product for Android, has emphasized giving developers the freedom to choose their own models and coding agents.
In a Wednesday post, Adarsh Fernando, senior product manager for Android developer tools, describes the goal as giving developers and their agents “the tools and knowledge to build high-quality Android apps faster.” The updates were announced Wednesday at Android Dev Summit.
Bring your own agent
The company’s Bring Your Own Agent feature now supports more than 40 coding agents that speak the open Agent Client Protocol, among them Anthropic’s Claude Agent, OpenAI’s Codex, and Google’s own Antigravity, and Google says the feature is now stable in Wednesday’s release of Android Studio Rabbit 2.
A developer can install several and switch between them without leaving the IDE, and connected agents inherit the IDE’s own read on a project — its structure, build configuration, symbols, and tools such as Compose Preview, the emulator, and Logcat — context they would otherwise have to rebuild through code searches and terminal guesswork.
Alongside it, a new Change Review feature scans an agent’s pending changes for common issues and can walk a developer through a large set of modifications before anything is applied, and Google is pushing the same reach beyond the IDE with official Android CLI plugins for Claude Code, and Codex that cover project creation, emulator management, UI inspection, and its Android documentation.
Compose previews from the terminal
Another announcement includes the new android preview command that lets coding agents render Jetpack Compose previews directly in the terminal without launching an IDE or emulator.
The company says agents using it completed UI tasks 77% faster while using up to three times fewer tokens, though it shared little about how it measured those results. The CLI also adds android device remote, giving agents access to physical devices in Google’s lab for testing. [...]

## [83] The five components of building a "company harness"
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1013 words

How do you build a company harness?
We've built internal agents at LangChain across marketing, sales, and engineering, and they have completely changed how those teams work. They weren't easy to get right. We spent a lot of time solving the problems that come with a multiplayer harness, and every team landed on the same core primitives:
- It lives where people already work (for us that's Slack)
- It knows who's asking and acts OBO that person for some services and with its own identity for others
- It has memory, scoped globally and/or at the user level
- Code runs in a sandbox and can make requests to services which require auth
- Large % of its runs are scheduled rather than explicitly invoked by someone (ambient agents!!)
Thank you to @caspar_br for help on this blog
LangChain Internal Agents
To ground this discussion, a brief overview of the three main agents we have at LangChain:
GTM Agent: a proactive, always-on agent that assists with GTM activities. Monitors and responds to emails, to new qualified leads, sends daily briefs, can answer questions about accounts, can run outbound motions
OpenSWE: our engineering agent, can work on and draft PRs, but also runs code review over all PRs
Content Studio: our marketing agent, can draft assets (blogs, images, PowerPoints, videos) in our style and with knowledge of our positioning
All of these agents are built in the same way. We think this is a general recipe for building company harnesses.
Problem: User Experience
All our agents live where people already work, which for us is Slack. They each have their own Slack apps, and can be DM’d or tagged in a channel. One benefit of working with these agents in channels is that others can see how people use it.
One nice thing we added was the concept of “breaking” out a conversation in Slack. Oftentimes, a great conversation would be happening and you’d want to add in your agent to get their opinion or get them to do something. But if they ran in that thread it would pollute the human conversation and distract. So we added an easy way for agents to “breakout” into their own thread in the channel.
There are some user experiences that are best NOT done in Slack. For example, when reviewing emails GTM Agent wants me to send, it's fine to do that in a one-off way in Slack, but if there is a big backlog it's not a fun experience at all to track those from Slack messages. For experiences like that, we did end up building a custom UI. [...]

## [209] Google built AI agents a world to practice in. The physics still aren’t quite right.
The New Stack | full text via The New Stack | ~519 words

Google built AI agents a world to practice in. The physics still aren’t quite right.
Google DeepMind introduced Genie 4 on Tuesday, a world model that renders interactive environments in real time with simulated physics, human motion, and native audio. The photorealistic demos are seriously impressive, but arguably the real draw for anyone building AI agents is that Genie 4 gives them somewhere to run multi-step tasks before it counts.
Tejas Kulkarni, a research director at Google DeepMind, describes the approach at a press briefing as a move toward “these hybrid world models,” with Gemini writing the code and text and Genie turning it into a running scene. It gives developers a way to generate test environments on demand, although how closely those simulations reflect real-world conditions remains an open question about reliability.
It gives developers a way to generate test environments on demand.
How Gemini steers Genie 4
Genie 4 uses several Gemini models to keep its simulations running. Gemini Omni helps shape the environment, while Gemini 3.8 Flash follows what’s happening, plans the next steps and adjusts when something changes.
Instead of producing a finished video, Genie 4 lets users interact with the world as it’s generated. They can move through it with a keyboard, change the camera angle or use text prompts to alter the environment without restarting the simulation.
Instead of producing a finished video, Genie 4 lets users interact with the world as it’s generated.
Rehearsing robots in simulation
Google’s clearest example puts Apptronik’s Apollo humanoid through a game of checkers, with Gemini 4 Argon planning each move and Genie 4 rendering the results as captions steer the scene.
The company is also exploring how the technology could support its Gemini Robotics research, which gives developers the ability to test agents in changing environments without having to rebuild each simulation from scratch.
Where the physics breaks down
The catch is that Genie 4 can’t always keep those environments consistent. Objects can shift position or behave unpredictably during longer sessions, and Google acknowledges that the physics isn’t always accurate.
That complicates agent evaluations, particularly when tasks involve remembering locations or returning to earlier states. A failed run could reflect a problem with the agent or the simulation itself, and Google hasn’t demonstrated that Genie 4 can replace traditional physics engines in high-stakes testing. [...]

## [156] Anthropic just launched tools to show companies what their AI spending is buying
TechCrunch | full text via TechCrunch | ~700 words

The financials Anthropic shared with investors this week suggest that its AI coding tool, Claude Code, is every bit the business success the frontier lab wanted. The company recorded an operating profit in the second quarter, and 900% net revenue retention — that is, spending from the same customers in Q3 2025 grew nine times in Q3 2026.
Anthropic has focused on getting enterprise users to stick around and Wednesday announced a new suite of reporting tools designed to give those customers a more granular understanding of the value they get from their token spend.
Using internal analytics and employee surveys, managers can view a team’s work over a given date range, what the team produced, how much it cost, and where its workflows broke down. Anthropic says it won’t use this data for model training by default. The reports will also offer recommendations on how to improve the results.
This is a clear attempt to demonstrate the return on investment of Anthropic’s tools and to show customers how to improve it — a major concern among large customers. Anthropic is also creating pooled group budgets to allow teams to better manage token spending.
Businesses have been hunting for that kind of information as they figure out how best to deploy AI tools. While usage among venture-backed firms is driving token spend, most of the Fortune 500 are not seeing major gains from deploying AI.
Jellyfish, a company that makes tools for software developers, released a new report yesterday based on the use of agentic coding tools by 276,000 of its customers. Claude Code and other tools built on Anthropic models remain the most widely used in the survey, responsible for nearly a third of all proposed code changes submitted for review. More importantly, spending on those tools has grown 10x since the beginning of the year, with their cost now equal to about 2% of total engineering cost.
“Even if you’re saying 2% is still small, that 10x growth is growth that most CFOs didn’t plan for,” Nicholas Arcolano, the chief scientist at Jellyfish, told TechCrunch. We’re certainly getting to the point where people are realizing, okay, it’s not enough to just spend a bunch. You now have to optimize it, make it work.”
Anthropic’s new reports speak to that challenge. Anthropic leads among enterprise customers, but what makes an agentic coding tool truly sticky is difficult to identify. [...]

## [189] Nvidia launches a promptable transcription model
The New Stack | full text via The New Stack | ~527 words

Nvidia launches a promptable transcription model
Nvidia on Wednesday launched Nemotron 3.5 Transcribe, its latest multilingual transcription model. The new open-weight model, the company says, ranks first on Hugging Face’s Open ASR open model leaderboard for English, with an average word error rate of 5.33%, and also sits at the top of two speaker-attribution benchmarks.
But what’s maybe even more interesting is that this is a promptable transcription model. Being promptable here means that the user can give the model specific instructions before it listens. Typically, that means setting the context for the transcription by telling the model that a given audio file is a medical discussion in English, for example, and giving it a list of medical terms.
Users can also tell the model to label each speaker or ask it questions about the audio. They can request a verbatim transcript or a cleaned-up version, and tell it how to format numbers, for example.
Nvidia bundles these capabilities, along with translation, into a single checkpoint, which could simplify the work of building applications around them.
Ideally, setting this context reduces the error rate. The trade-off is that these models are much larger than traditional transcription models, which are often under a billion parameters in size. Nemotron 3.5 Transcribe is a 30B mixture-of-experts model with 4 billion active parameters.
This isn’t a completely new concept, though. We’ve recently seen some other promptable speech-to-text models like Mistral’s Voxtral models and AssemblyAI’s Universal 3 Pro.
Nvidia, though, is able to rival Voxtral’s error rate with far fewer active parameters. On Artificial Analysis’s benchmark, Nemotron scores a 2.81% word error rate, compared with Voxtral Small’s 2.77%, while using about 4 billion active parameters versus 24 billion. That comparison measures accuracy against active parameter counts, though, rather than runtime or memory requirements.
The model can transcribe 40 languages — and translate 31 of those to or from English. Speaker attribution works for 13 of those languages, and it can distinguish between up to eight speaker voices. Audio Q&A was trained in English.
The model handles recordings up to an hour long. It’s built for recorded audio, though, and doesn’t support live streaming.
Developers can serve the model with vLLM or run it locally with NeMo-Speech.cpp. [...]

## [142] Elon Musk's SpaceXAI hit with multi-million dollar fine for building Mississippi data centers without the right permits
TechRadar | full text via TechRadar | ~660 words

Elon Musk's SpaceXAI hit with multi-million dollar fine for building Mississippi data centers without the right permits
SpaceXAI faces massive daily fines over unpermitted data center constructions
- Mississippi regulators say three SpaceXAI sites began work without required stormwater permits
- SpaceXAI could face $6.1 million in penalties across three Mississippi sites
- State officials are seeking daily penalties of up to $25,000
Elon Musk's SpaceXAI faces potential penalties reaching $6.1 million after Mississippi regulators identified alleged construction permit violations involving three data center facilities in the state.
State environmental authorities claim construction activities began before the company obtained the necessary stormwater authorization, exposing its subsidiary to substantial financial penalties.
It is now seeking penalties of up to $25,000 daily, with the company's preliminary financial exposure calculated across all three affected facilities.
Three Mississippi data centers face regulatory scrutiny
The Mississippi Department of Environmental Quality issued the enforcement notice to MZX Tech LLC, a subsidiary responsible for the company's local infrastructure.
The affected facilities include Macrohard and Macroharder, both already operational, while construction continues at a third computing complex known as Minihard.
Although the three facilities support operations around Memphis, Tennessee, their locations across the state boundary place them under Mississippi's environmental regulations.
A fourth computing facility sits within Memphis itself, where the company began developing its artificial intelligence infrastructure during 2024.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
The alleged violations were disclosed through a regulatory filing submitted to the Securities and Exchange Commission as part of the company's financial reporting.
SpaceXAI confirmed that it is cooperating with state environmental officials and discussing a possible settlement covering the alleged violations at all three locations.
The proposed arrangement would consolidate the regulatory matters into one agreement, although the company has not disclosed any finalized settlement terms. [...]

## [12] Emacs Turns 50
Hacker News | full text via Hacker News | ~1248 words

EMACS turns 50
How the MIT AI Lab’s text editor gave birth to the free software movement.
Programming used to be a very different experience from the one we know today. In fact, the first programmers didn’t write code at all; the six women who worked on the ENIAC, one of the world’s first computers, at the University of Pennsylvania in 1946 did it by physically configuring switches, cables, and plugboards.
A few years later, MIT engineers programmed the Whirlwind by punching code onto paper tape that was then loaded into the computer’s memory—making it among the first “stored-program” machines. Later, they and others moved on to punch cards, one for each line of code.
By the early 1960s, programmers with interactive computers could use a “line editor” to type their code on teletypes—large, noisy keyboard-and-printer machines. They’d type one line of code at a time, and their work would be saved on a spinning hard disk the size of a modern washing machine. But there was still no such thing as the now-familiar full-screen text editors that allow programmers to see and modify many lines at a time on a display.
One of the first such tools, EMACS, turns 50 this year, and it is still widely used.
EMACS first ran on the early video terminals at the MIT Artificial Intelligence Laboratory in 1976, but its core concepts were so powerful that it was rewritten for many operating systems in the decades that followed. Apple even distributed it with Mac OS X. Beyond that, the software-sharing community that started around EMACS helped give rise to the modern-day free software movement and the GNU/Linux operating system.
EMACS’s roots begin with the TECO text editor (originally the “Tape Editor and Corrector”) that Dan Murphy ’65 created in 1962 for the pioneering PDP-1 computer at MIT. The program’s commands were uppercase letters: A user would type “I” to insert text, “D” to delete a character, and so on. When tape gave way as a storage medium to files on a huge shared disk, the “T” in “TECO” came to stand for “Text.” And as years passed, TECO became a full language that programmers could use to create new commands, called macros, for editing their code.
In the fall of 1971, Carl Mikkelsen ’76 created Control-R, an add-on program for TECO that took advantage of “glass teletype” terminals with video displays. Control-R immediately displayed changes to the file being edited on screen; the programmer no longer needed to reprint each line to see the changes. [...]

## [183] Canonical Reviving Their Immutable Ubuntu Core Desktop
Phoronix | full text via Phoronix | ~372 words

Canonical Reviving Their Immutable Ubuntu Core Desktop
Canonical engineers back in 2023 outlined plans for Ubuntu Core Desktop as their immutable Linux desktop. They made some good initial progress but since 2024 it went rather silent. Now they are reviving Ubuntu Core Desktop as their immutable desktop  OS offering and with grand plans for the future.
Jon Seager, the VP of Engineering at Canonical, shared the plans today for accelerating Ubuntu Core Desktop development while acknowledging their 2023 preview of it "fell short" of their vision. For the Ubuntu 27.04 cycle, they will focus more on Ubuntu Core Desktop and target three use-cases of browser centric machines, developer workstations, and gaming machines. 
Key challenges expressed to the Ubuntu Core Desktop come down to application availability with what's offered in Snap form being one of their main blockers. This application availability is also why they are initially targeting the three use-cases. Other key challenges include around modularizing the desktop, dealing with permission prompting, and supporting KDE Plasma well in addition to GNOME.
They recently established a new Ubuntu Core Desktop team at Canonical to revive their 2023 preview and getting pipelines re-established for producing the immutable images and understanding the current state.  Daily images of Ubuntu Core Desktop are expected during the Ubuntu 27.04 cycle.
Seager ended today's announcement with:
"Ubuntu Desktop in its present form is not going away. However, this might be the most exciting thing I’ve been able to announce since taking the lead of Ubuntu. I’ve believed that Ubuntu Core is the future of Ubuntu for some time, but we’ve not been in a position to execute on the Desktop part of that.
We have a long road ahead of us, and a lot of technical challenges to overcome, but the result will be a safer, more resilient, more trustworthy and future-proof Ubuntu that I think you’ll have a blast using.
My long-term mission is to make Ubuntu Core the de facto target for Linux applications and workflows, and the default Ubuntu experience on the desktop, in the data centre and at the edge, and pushing the desktop agenda will further all of these use cases."
All the details in full can be read over on the Ubuntu Discourse.

## [39] Hoot 0.10.0 released
Lobsters | full text via Lobsters | ~1169 words

Hoot 0.10.0 released!
Dave Thompson —
We are excited to announce the release of Hoot 0.10.0! Hoot is a Scheme to WebAssembly compiler backend for Guile, as well as a general purpose WebAssembly toolchain. In other words, Scheme in the browser!
This release contains new features and bug fixes and since the 0.9.0 release back in May.
Use Hoot in the upcoming Lisp Game Jam!
On Friday (October 30th 2026), the autumn edition of the Lisp Game Jam will begin! It's a 10-day long game jam where participants make games using their favorite flavor of Lisp.
Does making a small web game in Scheme using Hoot sound appealing to you? Well, then we have just the thing to get you started: the Hoot game jam template! This template project has everything you need to start making an HTML5 game with Hoot quickly.
The template repository includes:
- Bindings to the necessary web APIs to make an interactive game with HTML5 canvas
- A Makefile for compiling, running a development web server, and generating a .zip bundle for uploading to itch.io
- A very simple Breakout-like example game that demonstrates how to put all the pieces together
For more inspiration, here are some games made with Hoot for past jams:
Now, onto the release notes!
Compiler changes
- Added module name to contextualize duplicate import errors.
- Added support for library versioning for R6RS compatibility.
- Fixed default version for define-module libraries.
- Fixed locate-library not respecting configured load extensions.
Previously, we were using Guile's load extension parameter instead
of Hoot's own.
Runtime changes
- Added %struct-ref and %struct-set! primitives for accessing
record types defined using the interpreter.
- Stopped raising errors when importing an undefined symbol in the runtime module system. Guile is lax about this so Hoot being strict caused compatibility issues.
- Fixed optional argument parsing in primitive-eval.
- Fixed keyword argument parsing for procedures with both optional and
keyword arguments in primitive-eval.
- Fixed error messages regarding runtime module registry to include
the correct CLI flag: -fruntime-modules.
Scheme changes
- Added partial implementation of SRFI-13: String Libraries. It's just a set of re-exports, very similar to Guile, but Guile's SRFI-13 module is not declarative and is thus rejected by Hoot's compiler.
- Added partial implementation of SRFI-60: Integers as Bits.
- Added define-macro, defmacro, delete, list->symbol, and symbol to (guile). [...]

## [200] Provenance Time Proposed As A New Timestamp For Linux
Phoronix | full text via Phoronix | ~291 words

Provenance Time Proposed As A New Timestamp For Linux
While the Linux kernel and various file-system drivers already support the notion of the birth time for tracking a file/directory's birth/creation time, a slightly different provenance time "ptime" is now being proposed for the Linux kernel.
Provenance Time is a new timestamp proposal for indicating when a file/directory is created. How it differs from birth time is  tracking the original creation date of file contents across file-system boundaries.
The proposal for Provenance Time goes on to explain:
"The semantics of this new timestamp should be at least these:
- it should be the same as btime on a newly created file
- it's user-settable, so it can be preserved for backups, filesystem conversions, archives and any similar operation
- it should be preserved every time mtime gets preserved
and the correspondence with the other timestamps is as follows:
ctime <-> btime
mtime <-> ptime
Examples:
1) a .zsh_history file created in 2019, then after a few years the user decides to switch to another filesystem, copying the .zsh_history to the new home, in that case btime would have the timestamp of the copy and ptime would have the 2019 timestamp (just like mtime would have been preserved)
2) a symlink created in 2020 from the home directory to a /path going through the same process as the .zsh_history, in this case it would also make sense to sync the ptime to the 2020 timestamp instead of keeping only the btime (so the inode creation time)."
The request for  comments patches on Provenance Time enable it in the Linux kernel VFS layer and an initial file-system implementation for Btrfs. There are also proof-of-concept Coreutils patches for PTIME usage with stat and cp commands.

## [106] A fast and secure tar parser for the Rust ecosystem
Lobsters | full text via Lobsters | ~5881 words

Starting with 0.131, uv uses tar-codec to parse source distributions.
tar-codec is roughly twice as fast as our previous tar implementation (astral-tokio-tar) while also reducing uv's exposure to parser differentials and other security risks.
This blog post is about tar-codec itself: what it is, and what compelled us to build and optimize it. Read on if you, too, would like to know too much about tar archives.
Background: uv and tar #
What follows is an extended digression on the tar format. If all you care about is tar-codec,
skip to it.
As a Python packaging tool, uv is in the business of resolving and installing Python packages. uv
requests installable distributions from various sources (principally package indices like PyPI)
and installs them on the user's behalf. This is how you go from uv add urllib3 to something you
can actually import and use in your own Python codebase.
Installable distributions come in two primary forms:
- "Built"2 distributions, also known as bdists or (most commonly) wheels, are essentially ZIP archives containing structured metadata and a fixed layout. Installers handle these by (more or less) plopping their contents into the right destination directory. Many people think that bdist is short for "binary distribution," since wheels often contain compiled native code. This one common way to use wheels, but wheels can also contain pure Python. They're just another (and frequently better) way to package and install a distribution.
- "Source" distributions, also known as sdists, are essentially tar archives. Unlike built distributions, a source distribution is essentially3 just a rollup of a source tree's state at release time. By definition, source distributions execute arbitrary code at installation time. This makes them
very powerful, but brittle (missing build tools or dependencies) and also a security risk (an
attacker who controls the sdist can run code without the user needing to import anything).
Wheels are generally produced by running a build backend on a source distribution. Examples of that include uv's own uv_build, maturin, and flit.
Consequently, at a bare minimum, a Python package installer needs to understand at least two different archive formats: ZIP for wheels, and tar for sdists.
We've already talked a bit before about ZIPs on the Astral blog, and we'll certainly be talking about them again soon enough. But today we'll be focusing on tar.
Why a new tar parser? [...]

## [165] Linux Kernel Developers Considering Removal Of KGDB Debugging Functionality
Phoronix | full text via Phoronix | ~356 words

Linux Kernel Developers Considering Removal Of KGDB Debugging Functionality
Merged to the kernel all the way back in Linux  2.6.26 in 2008 was KGDB for improving the kernel debugging experience. KGDB works in conjunction with the GNU Debugger (GDB) to debug the kernel in a similar fashion to user-space debugging. KGDB requires the use of a second computer connected via serial or network cable. KGDB isn't widely used in recent years and a patch was floated today to remove it from the Linux kernel.
Longtime Intel Linux developer Peter Zijlstra posted the patch for removing KGDB from the kernel. Peter argued in the patch message:
"KGDB does some horrible things, and with everybody having access to virtualization these days, there is really no reason to use it over Qemu's gdb-server."
Indeed debugging via VMs with the QEMU gdb-server is a cleaner approach than grabbing a null model cable and a second computer.
The patch would remove KGDB support in its entirety from the kernel. In a response over the proposed removal, Peter elaborated on the issues with the KGDB code:
"(In response to a prior comment: What if the debugging depends on specific hardware?)
Use device pass-through, emulate it, or printk() debug it.
Using KGDB can cause a ton of problems, it more or less stays stuck in NMI context, which can terminally screw up the timekeeping code, it can also cause the watchdogs to fire and there's endless annoyance with code patching and breakpoints.
People have been trying to 'fix' the breakpoint code to be less broken in the face of KGBD, but its all terrible and really not worth it. By fat the sanest option is to just delete KGDB as proposed here.
Also, when was the last time you used KGDB? I think I've tried it once, some 20 years ago, and haven't bothered since -- it was *that* good :-)"
A suggestion was raised to potentially just disable KGDB initially via the Kconfig options and to remove it a few kernel  releases later. We'll see what happens but there is movement for disabling and/or removing the KGDB support from the Linux kernel.
