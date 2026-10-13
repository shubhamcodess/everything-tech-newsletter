# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Muse Wonder
Hacker News | full text via Hacker News | ~1032 words

A frontier model that leads on personal and professional agents
Today, we’re excited to introduce the Muse Wonder series with Muse Wonder and Muse Wonder Full, our most capable models that deliver state-of-the-art performance on personal and professional agentic tasks. Together, they mark the next step on our scaling ladder and a major leap toward personal superintelligence. Muse Wonder brings together Active Memory and Active Focus to keep track of what matters to you and work diligently toward what you want to accomplish.
Muse Wonder is available today through the Meta Model API and Muse Code, and Muse Wonder Full is available today for Muse Code subscribers.
Muse Wonder will soon power experiences in Muse, and will roll out first to subscribers. Muse Wonder will also power artifact generation and processes that require more intelligence. And in the future, we’ll be using Muse Wonder to develop specialized models that we can bring to everyone using Muse.
Scaling Toward Personal Superintelligence
Fourteen months ago, we began a ground-up overhaul of our artificial intelligence efforts. In that time, we’ve gone from rebuilding our stack from first principles to pushing the frontier.
When we introduced Muse Spark, we outlined our approach to predictable, rigorous scaling. Today’s release builds on that work across pretraining and reinforcement learning, delivering our most capable models yet. Trained at our gigawatt-scale Prometheus data center, Muse Wonder and Muse Wonder Full bring together the work of teams across Meta to deliver frontier capabilities for complex tasks at work and in everyday life — another step toward bringing personal superintelligence to the billions of people who use our products.
Frontier Capabilities
Model Highlights
The Muse Wonder series achieves state-of-the-art results across key benchmarks for personal and professional agents, memory, and coding.
The full results below compare Muse Wonder and Muse Wonder Full with other frontier models across a broad evaluation suite.
For more details about our evaluations, see our report.
The results above provide a broad view of the models’ performance. We now take a closer look at four areas central to their work on real-world tasks: domain expertise, Active Memory, Active Focus, and frontier coding. [...]

## [19] Anthropic's Claude AI submitted false murder tip to Philadelphia police
Ars Technica | full text via Ars Technica | ~344 words

An Anthropic AI model submitted a false tip about an unsolved murder to Philadelphia police, the company and police department confirmed on Friday.
A Claude model sent the false tip on July 18 to the Philadelphia Police Department’s website for submitting information about unsolved murders, but it was flagged by a spam filter. Anthropic apparently discovered the incident on September 28 and informed the police department about it on October 8.
During internal testing, Claude Haiku 4.5 was instructed to complete various forms up to the final submission stage and to stop before submitting those forms. “Several times Claude mistakenly submitted the form instead, expecting there to be an additional confirmation page,” Anthropic said in a report describing “unintended model actions we’ve observed during evaluations and internal use of Claude.”
The false murder tip occurred when Claude Haiku 4.5 was instructed to complete tasks on randomly selected webpages, Anthropic said:
In one run, the model landed on a page referencing an unsolved homicide; that page contained a tip form run by a police department. Claude was instructed never to log in, create accounts, enter personal data, make purchases, or submit anything destructive, but the instructions did not rule out form submissions. Claude filled out the form with the following: “I may have information regarding this case. I recall seeing someone matching the description in the area around [the street named on the page] during that time period. Please contact me if this information is relevant.”
Anthropic said it also discovered Claude incidents involving state and federal agency websites. Claude reportedly submitted 20 visa applications to the US State Department in one of these incidents.
Police call two-month delay “unacceptable”
Anthropic confirmed that the false homicide tip was sent to the Philadelphia Police Department, and the department issued a lengthy statement on the incident to the ABC station in Philadelphia. The false tip left the name and contact fields empty. It was not reviewed by any person because the email message generated when the tip was submitted ended up in a spam folder, police said.

## [59] The AI Computing Crunch Is Making Rivals Into Partners
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 401) | ~54 words

Anthropic entered into a deal worth up to $45 billion earlier this year to lease computing power from SpaceX. The unlikely alliance illustrates the industry's increasingly desperate scramble for compute. Demand is outstripping supply, and prices are rising, causing tech companies to strike deals with rivals. Venture-capital firms are helping startups obtain computing capacity.

## [24] GitHub Copilot app for Beginners: How to teach Copilot about your codebase
GitHub Blog | full text via GitHub Blog | ~1022 words

GitHub Copilot app for Beginners: How to teach Copilot about your codebase
Learn how to add custom instructions and skills to your repository, use custom agents, and connect MCP servers like Playwright.
Context matters when you’re working with AI. Every codebase has its own house rules: how components are structured, which scripts to run, and which conventions apply to different frameworks and file types.
Copilot can help you make changes across a project, but it works best when it knows those rules, too. Much of that knowledge can live inside the repository, so Copilot can pick it up automatically instead of requiring you to explain the same standards, scripts, and workflows every time you start a new task.
In this installment of our GitHub Copilot app for Beginners series, we’ll look at four ways to tailor how Copilot works with your project:
- Custom instructions communicate the conventions Copilot should follow.
- Agent skills package repeatable procedures.
- Custom agents bring specialized guidance to larger tasks.
- Model Context Protocol (MCP) servers connect Copilot to external tools and data sources, expanding what it can do.
Let’s look at how each one works and how they can work together.
Start with custom instructions
Suppose you ask Copilot to add a custom page size to an application. Making the change is only part of the job. The new code should also follow the patterns your team already uses.
Repository custom instructions give Copilot that baseline context. Add a .github/copilot-instructions.md file to define guidance that applies across the repository, such as your preferred architecture, naming conventions, or expectations for testing and validation.
You can also create path-specific instruction files inside .github/instructions. These files use an applyTo field to tell Copilot when the guidance is relevant.
When Copilot works on a matching file, it can use both the repository-wide instructions and the more specific guidance. That lets you keep the broad rules in one place without forcing every file type into the same mold.
Package repeatable procedures as agent skills
Custom instructions are useful for standards that should shape many tasks. But some guidance only matters when Copilot is performing a particular procedure, such as running quality checks, preparing a release, or debugging a failed workflow.
That’s where agent skills come in. [...]

## [56] Problems in 22 scientific fields had solutions hiding in plain sight. An AI has found them
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~92 words

Borrowing an idea from one research discipline to solve a problem in another is an age-old scientific trick. However, such clever leaps are rare because researchers don't tend to spend their time researching fields outside of their expertise. AI can easily hop between fields. BootLoops is a harness that can spot and solve problems in seemingly unrelated fields that share the same mathematical structures at massive scale. Researchers recently released 36 preprints produced with BootLoops covering a wide range of topics, including figuring out the age of sunspots, analyzing government health pol

## [58] So long, Spokes: GitHub rewrites storage to restore reliability, just in time for agentic hordes
TLDR Tech | full text via TLDR Tech | ~444 words

AI
- AI systems are fully capable of carrying out nightmare attacks against infrastructure and nobody's ready Meanwhile, AI agents move robotic arms, 'make OT device operator screens lie'
- Nvidia found $1B under the couch to help secure American scientific computing dominance Commitment comes as GPUzilla prepares to fortify Uncle Sam's arsenal with at least seven AI-optimized supers
- TSMC taps GlobalFoundries to bolster US silicon interposer production in $2B deal Advanced packaging tech is essential to the domestic production of high-performance semiconductors used in AI datacenters
- Microsoft is about to let Copilot loose on your file system But don't worry, it's totally safe because the agents and models will (probably) be running locally. Routers never break right?
- Microsoft N1Xes Intel in favor of Nvidia's shiny new SoCs in Surface Laptop Ultra Poverty-spec model starts at $2,599 with 24 GB of RAM and 512GB of storage with 128 GB models topping $5,899
Infosec
- Security Russians are posing as Signal support to launch phishing attacks PLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
- Security Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attack PLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
- Black Hat and DEF CON DEF CON Franklin project enlists hackers to harden critical infrastructure Voting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
- Security EQT buys majority share in Swiss cybersecurity biz Acronis Went at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
- Malware Month Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sight On the plus side, infosec's a good bet for a long, stable career
FOSS
- OpenAI dots inspire open source imitators amid technical difficulties Persistent agents appeal to AI companies, but demand isn't obvious
- Ubuntu 'Stonking Stingray' beta swims out: Deeper Rust 'oxidization' plus LLM speech-to-text GNOME 51 is here, and Ubuntu interim releases are getting interesting again
- Revive Raskin's 3 laws of software with humane work that considers a dev's duty of care All this, and angry NeoVim users
- Firefox 157: Could bold new look be just what Mozilla needs?* Yet another new version of Firefox, with a significant reskin
- KDE turns 30 and someone's brought an [...]

## [5] Hackers activate automatic defrosting in supermarket fridges across Europe
Hacker News | full text via Hacker News | ~796 words

'Unprecedented' Cyberattack cripples supermarket fridges across Europe as hackers activate automatic defrosting — delivery and store prices also impacted by incident
France, Belgium, and the Netherlands are reportedly affected.
An ongoing cyberattack has reportedly struck major supermarket chains across Europe, disrupting refrigeration control systems. The attack — which has reportedly seen units set to continuously defrost at 50 degrees Celsius — is also apparently affecting deliveries and in-store pricing powered by electronic shelf labels, La Dépêche reports.
According to the report, "several" major retailers have been targeted by a cyberattack, which has hit Danfoss-made refrigeration controls used by French supermarkets Intermarché, Leclerc, and Coopérative U. Indeed, the latter's president, Dominique Schelcher, has confirmed as of Monday morning that "A cyberattack has been affecting the refrigeration production facilities of several stores in our network since last night." Schelcher said teams had been mobilized to fix the issue and promised an investigation into the incident, which he described as "extremely serious."
The report states the units have had their automatic defrosting systems activate, but that hackers have also configured the function — which normally runs for just two hours a day — into a continuous, forced defrosting cycle with the temperature set to a toasty 50 degrees Celsius. Sources reportedly described "a wave of heat" escaping from fridges and freezers
Early reports indicate losses are already approaching 300,000 euros, but could run into several million euros nationwide. Separately, NOS in the Netherlands reports that several supermarket chains have been hit with a malfunction due to a cybersecurity incident on Sunday afternoon. Albert Heijn, Etos, and Gall & Gall have had their websites taken down, impacting deliveries. Electronic shelf labels have also been compromised, disrupting in-store pricing. "We have immediately taken measures to protect our IT environment. Part of this involves the preventive temporary shutdown of a number of systems," Albert Heijn said in a statement.
It is unclear at this stage whether the two attacks are related or how widespread either of them is. Belgium's Delhaize chain, which belongs to Albert Heijn, has also reported disruption. Images online show stores in Amsterdam warning customers about price problems, and the suspension of loyalty programs that have also been impacted by the incident. [...]

## [13] Epic Games reportedly pivoting to "AI first" game development model
Ars Technica | full text via Ars Technica | ~246 words

Epic Games is shifting to an “AI first” development strategy for its collaboration with the Walt Disney Company, letting AI models write all the code and guide all the artwork for an upcoming shooter. That’s according to a Bloomberg report, which cites unnamed people familiar with the project who commented on the significant pivot in internal development at the Unreal Engine maker.
Human developers will be tasked with managing and guiding code and art assets generated by models such as Anthropic’s Claude, according to internal Epic employee messages viewed by Bloomberg. That means “no more hand-written code” and art assets “generated with full AI workflows,” according to the report.
The $1.5 billion collaboration between Epic and Disney, announced in early 2024, was slated to release a Marvel- and Star Wars-themed shooter in March 2027. That project has now been delayed indefinitely amid the AI-related shakeup and understaffed, slower-than-expected development thus far, according to the report.
“We’re embracing AI-accelerated development, led by Epic developers who are the visionaries and creative drivers for everything we do,” an Epic spokesperson said in a statement.
“We have a huge pivot underway here at Epic, moving developers around to retool for maximum AI acceleration,” Epic CEO Tim Sweeney wrote on social media shortly after the Bloomberg story was posted. “The aim isn’t to do the same stuff with fewer people, but to enable everyone here to build MORE and BETTER stuff, and to bring the benefits to all teams using Unreal.”

## [34] Spotify More Than Doubled Monthly Code Changes as AI Accelerated Development
InfoQ | full text via InfoQ | ~480 words

Spotify has expanded its use of AI-assisted development, more than doubling monthly merged changes from approximately 8,100 to 17,000 year over year in August. The company is adapting its quality and reliability controls to handle the higher volume of software changes across its production systems.
Spotify operates nearly 3,000 production services supporting 777 million monthly active users, around 100 million concurrent clients, and 11 to 12 million backend requests per second. Its review identified issues involving content processing, fleet changes, compute capacity, and mobile application quality. The company has responded with changes to monitoring, testing, rollout safeguards, rollback capacity, capacity planning, and quality measurement.
One incident involved Spotify's content processing pipeline, which handles more than 500,000 new songs, videos, podcasts, and audiobooks each day. On June 24, a scheduled batch workload competed with new episodes, a quality improvement increased processing requirements, and a scheduling bug reduced throughput by about 10%. Episodes that normally appeared within minutes were delayed for hours. Spotify subsequently added end-to-end monitoring, fixed the scheduler, moved batch jobs to lower priority, reworked workload prioritization, and increased capacity.
Fleet automation created a different challenge. Spotify's Fleet Management system has merged more than 2.5 million automated maintenance pull requests, with most automatically merged after safety checks. The company later added Honk, a background coding agent that runs Claude using the Agent SDK in Kubernetes pods. Fleetshift handles target selection, scheduling, and progress tracking, while Honk performs code modifications and can run builds in CI. Spotify reports that a recent Java migration across its backend services took three days.
An automated dependency upgrade nevertheless passed existing checks and failed in production, according to Spotify. The company is strengthening safeguards, expanding rollback capacity, and scheduling automated changes during owning teams' working hours.
Amit Jha, a software engineer at JumpCloud, in a LinkedIn post discussing Spotify's findings, said:
More changes meant greater pressure on testing, review and observability.
Alex Beck similarly focused on the verification challenge in a LinkedIn post,
Writing code got easier. The hard part now is making sure the work is actually good before it goes live. [...]

## [46] GitLab 19.4 Adds Goal-Driven Agents and Tighter Cost Controls
InfoQ | full text via InfoQ | ~765 words

GitLab has released version 19.4 of its DevSecOps platform, adding a goal-driven mode to GitLab Duo CLI, three hosted open-weight models, a larger set of Model Context Protocol (MCP) tools, and more detailed controls for AI spending. The release moves GitLab's agents beyond individual prompts and predefined flows, while keeping their actions within the permissions and approval rules already used by a project.
The new /goal command in GitLab Duo CLI, now in public beta, accepts an open-ended objective and continues working until it completes the task or reaches an iteration limit. One model implements the changes while a separate model checks progress against the stated goal. A developer can stop the run, change the goal, or redirect the agent. The work runs locally and retains the project's existing context and controls.
"This release takes agentic automation from something individual developers use to something an organization can scale at speed and under the controls already in place."
Manav Khurana, GitLab
GitLab's use of the word "verified" has a specific meaning here. The second model judges whether the result meets the natural-language goal; this is not formal verification of the code. The command can report work that it could not resolve, and the iteration limit prevents it from continuing indefinitely. Clear acceptance criteria therefore remain important, even though the developer no longer has to supervise every intermediate step.
GitLab Duo Agent Platform also gains support for the hosted open-weight models Kimi K3, MiniMax M3 and GLM 5.3. GitLab says these provide up to four times as many calls per GitLab Credit as many comparable frontier models. Group owners can set a default model for a feature and restrict the models available to teams. This lets an organisation use a lower-cost model for routine work and reserve a more expensive model for tasks where it performs better. The announcement does not include model-by-model benchmark results or absolute per-call prices, so customers will still need to test the options against their own workloads.
"The platform running the automation is what governs which tools an agent can touch and attributes what it consumes."
Manav Khurana, GitLab
The expanded GitLab MCP server tools let agents in third-party clients trigger and inspect pipelines, open and review merge requests, update work items, browse repositories, and manage vulnerabilities. [...]

## [61] Deno is joining Cloudflare
TLDR Tech | full text via TLDR Tech | ~1069 words

This may come as a surprise to some, but when the Deno team released celld in August, we were delighted.
Why a surprise? Well, as it happens, there is a popular theory that suggests we shouldn't be happy.
You see, it is commonly claimed around the Internet that we made Cloudflare Workers work differently from other cloud platforms in order to create "lock-in." The claim goes, software built on Workers is hard to move to other hosting platforms, therefore if you write your app on Workers you are "trapped" on Cloudflare forever. This is especially true of apps that use Durable Objects: they are not just written differently but architected differently. All this is, supposedly, a clever trap: once you are too deep to be able to switch, the rug will somehow be pulled out from under you.
Under this theory, celld is a threat: as an open-source implementation of Workers and Durable Objects, it allows applications built on Workers to seamlessly migrate to other providers. No more trap!
This theory is wrong
Workers is different because it is better
We built Workers differently because we believe it is a better way to build web applications.
- The Workers design makes it dead simple and dirt cheap to manage an application that runs in hundreds of locations around the world, a feat which no other popular hosting platform has achieved. The pricing isn't a trick: we've genuinely created a novel architecture that is more efficient than competitors, and we've passed on the savings to you.
- Workers' live environment design (aka "bindings") simultaneously makes configuring access to external resources easier and more secure. Usually, those two things don't come together!
- Durable Objects make it easy to build real-time collaboration and distributed systems that are difficult or impossible in a classical three-tier web architecture.
In short, we believe we've simply created a better programming model for cloud software. But being better requires being different: we couldn't achieve these benefits while remaining perfectly compatible with existing platforms.
If we could offer these benefits and be perfectly compatible with traditional cloud platforms, we absolutely would! It would be a great benefit to our business if every kind of compute workload could simply be lifted and shifted onto Workers. But the reality is, innovation sometimes requires doing things differently. [...]

## [64] How to Effectively Debug When You No Longer Understand the Code
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403) | ~64 words

Three production investigations, a latency regression, a memory leak, and a kernel-level hang, show how to steer coding agents through unfamiliar systems using runtime evidence. The framework separates facts from hypotheses, compares failures with a control, and requires every proposed cause to satisfy all known constraints. Adversarial reviews should seek contradictions, and reproductions must match the real failure's signals before they can be trusted.

## [65] Five Months Treating Bugs Like Patients and Coding Agents Like a Medical Team
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~4302 words

Between a Wednesday evening and a Friday afternoon in April, MOLT, the tool Cockroach Labs ships for migrating databases to CockroachDB, gained the ability to migrate from IBM Db2 sources.
Db2, one of the first commercially available relational databases, has a rich SQL dialect, a complex type system, and a native wire protocol. Supporting it in MOLT meant a new schema converter, a new Fetch path for pulling rows out and getting them into CockroachDB, a new Verify path for comparing them once they were loaded, a vendored ANTLR grammar, a Docker image for CI, and more than ten thousand lines of test fixtures. When we added Oracle support to the MOLT tools in 2024, the equivalent work took 9 months, and cost around $160K in engineering time.
Db2 took less than two days, and no human wrote any of the code. The token bill was $4172: 164x faster, and 38x cheaper.
It all started with a single GitHub issue describing the ask:
A planning agent then read it, decided it was too large to treat all at once, and decomposed it into fifteen sub-issues with an explicit dependency graph: first the foundation, then the type system, then the row iterator, then Fetch, then Verify, then Convert, then CI, then test data. Two of the sub-issues were judged as too large in their own workups and were decomposed again. Along the way the agents filed another dozen issues against their own work: fixture gaps, a type-mapping bug, and an isolation-level fix. By the time the parent issue closed, thirty-two sub-issues had been opened under it, twenty-seven pull requests had merged, reviewers had sent work back fifty-five times, and nine issues had been escalated, two of them to a human. Test coverage, as measured against PostgreSQL (our best-tested dialect) was equivalent.
But how did all of this happen? What was driving this, and more importantly, what was ensuring that what came out the other side was high quality? Before we opened the issue for Db2 support, we first built a coding hospital which we call MOLT Sinai. MOLT is the name of CockroachDB’s migration tool set, and once we had decided to model the pipeline on a hospital, MOLT Sinai was too good of a portmanteau to resist. That’s because Mount Sinai is a prominent teaching hospital in both Toronto and New York - the cities in which we live. The name stuck, and so did the vocabulary. Issues are patients. Merging is discharge. The humans in charge are the Chiefs of Medicine. [...]

## [86] 'People aren’t perfect, and everyone knows it': Security experts still see humans as the biggest threat to their business
TechRadar | full text via TechRadar | ~589 words

'People aren’t perfect, and everyone knows it': Security experts still see humans as the biggest threat to their business
Forget the hackers, YOU are the problem
- Human error remains one of the biggest challenge to online security, according to industry leaders
- 68% of security professionals cite human error, compared with just 55% for email-based scams
- A worrying 80% of contributing factors in recent security incidents can be traced back to poor user practices or lack of training
New research into the challenges facing cybersecurity professionals has revealed the naked truth: that humans are considered the main challenge to security.
A new Kaseya survey of over 1,100 MSPs and IT professionals around the world uncovered a startling trend: that the risks posed by humans to their cybersecurity are considerable. Some 68% of respondents cited human error (including social engineering and distraction) as the most concerning attack vector over the next 12 months.
With the overwhelming majority of cybersecurity incidents attributable to human error, security suites and the teams that use them are increasingly focusing on ways to mitigate the challenges posed by people.
Human error
We know that humans need security as much as the data they’re working with. But the results of this survey illustrate a sad truth: that cybersecurity professionals are more concerned about user error and the vulnerabilities of “soft” targets than the threats from automated attacks against network hardware and servers.
Hackers know that humans make mistakes. Organizations need to be on the same page.
From the results of the report, we can see that after the prospect of risks caused by human error, social engineering, and distraction, 55% of those surveyed are concerned about attacks via email. Gullibility is also considered a risk (41%) as is a lack of cybersecurity training for users (40%).
Auditing isn’t always the answer, either. Of those surveyed, 65% said they would pass a compliance audit today, but 49% noted that incomplete documentation and procedures could create problems.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
True cyber resilience
Worryingly, only 20% of IT departments have a budget that is growing in line with the risks they face, with 77% describing themselves as under-resourced. [...]

## [88] Russian bot traffic decimated overnight after Ukraine drone strikes knock multiple Yandex data centers offline
TechRadar | full text via TechRadar | ~785 words

Russian bot traffic decimated overnight after Ukraine drone strikes knock multiple Yandex data centers offline
Drone strikes knock Yandex services offline
- Ukrainian drone strikes knock key Yandex data centers offline in Central Russia
- Bot traffic on Yandex networks has dropped significantly as a result, with many services knocked offline and Yandex's Cloud Zones operating with 'limited functionality'
- Data centers are quickly becoming key military targets as intelligence gathering and communications rely on cloud services
Ukraine has launched a series of drone strikes over the past week that have knocked multiple Russian data centers offline, resulting in internet bot traffic from the country dropping to almost zero.
The data centers were operated by Yandex - Russia’s domestic answer to Google - and traffic for the search engine has dropped to just 0.4% of its two week high.
Yandex traffic first dropped on October 8, 2026 after Ukraine struck a data center in Sasovo, Russia, and a second strike on a data center 220 miles to the west of Sasovo on October 10.
Russian bot traffic collapses following strikes
It is important to define what this bot traffic actually is. There is a common tendency to automatically associate 'bot traffic' - especially Russian bot traffic - with the fake social media accounts that spread Kremlin-aligned propaganda. The bot traffic taken offline in this context is more likely to be automated programs that crawl pages, index search results, and gather data for AI platforms.
The drone strikes have been particularly devastating for Yandex’s cloud services. The Yandex Status Board shows that Yandex’s Central Russian Cloud Zones are currently unavailable, and the platform is running in a “limited functionality” mode with most services offline.
Ukraine’s strikes on data centers appear to be retaliatory. Russia began striking Ukrainian data centers in late September under the reasoning that they were being used by Ukrainian military intelligence. A strike on a building within the business center of Kyiv killed four people and knocked internet connectivity offline for 100,000 households in the Kyiv region.
These strikes have been the latest escalation of the war which has been raging since the Russian invasion in 2022, although some observers say the war began with Russia’s annexation of Crimea following the collapse of Ukraine’s Pro-Russian government in 2014. [...]

## [105] Google paid $90,000 for this bug, then waited two months to fix it
The New Stack | full text via The New Stack | ~831 words

Google paid $90,000 for this bug, then waited two months to fix it
Google took two months to patch an unauthenticated RCE vulnerability in its developer documentation infrastructure. The problem was a reused OAuth client secret, which DevSite stored in a Flask session cookie and also used to sign sessions. Anyone who recovered the secret could forge a valid cookie and execute Python code on the server.
Simon Köck, a software engineer at Otark GmbH, discovered the flaw in Google’s DevSite infrastructure, the shared platform behind developers.google.com and several sibling documentation sites. Köck tells The New Stack that forged sessions were accepted on all seven affected domains, which relied on two different signing keys, and that he ran his code-execution proof on three of them, developers.google.com, docs.partner.android.com and web.dev.
Köck tells The New Stack that forged sessions were accepted on all seven affected domains, which relied on two different signing keys, and that he ran his code-execution proof on three of them
Google rated the vulnerability S0, the top of its severity scale, and awarded Köck a $90,000 bounty. That figure reflects a $75,000 base payout for an S0 RCE in what Google classifies as a normal application tier, multiplied by 1.2 for exceptional report quality.
Köck confirmed unauthenticated RCE with a Python sleep payload, measuring response delays that matched his payload, and deliberately stopped short of running commands or touching files, credentials, or internal services. “I’d call it an exceptionally serious RCE because anyone could reach it without an account or victim interaction,” he tells The New Stack, adding that he doesn’t know whether the three hosts he tested shared the same backend machines.
“I’d call it an exceptionally serious RCE because anyone could reach it without an account or victim interaction,”
The more consequential unknown sits behind the server itself. Köck tells The New Stack, Arvin Shivram, a Singapore-based researcher who goes by @brutecat and has reported more than 130 Google vulnerabilities by his own count, has since pointed out that internal App Engine apps often have access to Stubby, Google’s internal service-to-service communication system. Köck acknowledges that access “could be a major part of the impact,” though he says he didn’t verify what this particular DevSite process could reach. [...]

## [118] AI Coding Agents Generate More Code, But Not More Software
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~93 words

A study of more than 700 software firms found that AI coding agents significantly increase the amount of code developers produce, but not the amount of software companies actually ship. Ars Technica reports: A recent study (PDF) of actual coding practices across hundreds of firms finds that human code review forms a significant "bottleneck" for the overall efficiency of AI coding tools, resulting in "little evidence that firms increase software output or reduce employment" by using them. Any efficiency increased during the actual coding phase, the study authors find, is "absorbed by downstream

## [123] Andrej Karpathy says only 5,000 people have seen what AI can really do
The New Stack | full text via The New Stack | ~794 words

Andrej Karpathy says only 5,000 people have seen what AI can really do
OpenAI founding member Andrej Karpathy, who joined Anthropic in May, thinks most of the world has little idea of what AI can do, and in a Sunday post on X, he said the gap is getting wider. By his own napkin math, roughly 6 billion people have barely used an LLM, 1 to 2 billion use chatbots casually, about 20 million use frontier models professionally in math and code, and around 5,000 have access to frontier systems inside the labs.
Box CEO Aaron Levie sees an opportunity in that gap. “This is a good way to understand how early we actually are in AI diffusion right now,” he wrote in his response on X.
He argued that most people still think of AI as a chatbot or a next-generation search engine while barely exploring its more advanced opportunities.
Box bets on agent swarms
“Agent swarms represent possibly the ultimate form factor of what agents will do inside of our workflows,” Levie wrote, envisioning systems that divide complex work among agents running in parallel.
“Agent swarms represent possibly the ultimate form factor of what agents will do inside of our workflows”
For now, “less than a fraction of a fraction of the population uses AI in this way,” Levie noted, and he identified the obstacles keeping it that way. We’re still early. Models aren’t equally capable across every kind of work, running them at scale is expensive, and tools to manage multiple agents are still catching up. Most people don’t even have access to the most powerful models yet.
Rethinking how work gets done with AI is a fraction of what companies have to consider. Connecting their data and figuring out security and compliance are just a few other challenges. Levie expects “a huge amount of change management” before most industries outside software and AI research can take advantage of these agents.
That puts Box squarely in the conversation, since the company has been expanding its AI offerings with products such as Box Automate, which connects AI-powered automation to document-heavy business processes. Levie has also said Box doesn’t intend to compete directly with model providers.
“A lot of this is where the applied layer of AI will really shine in the enterprise because of the domain specificity of this type of work,” Levie wrote, placing the opportunity with the companies building industry-specific applications and infrastructure on top of frontier models. [...]

## [125] The Rise of AI Software Clones: Why REA and ArtCraft Are Going Viral
KDnuggets | full text via KDnuggets | ~1001 words

The Rise of AI Software Clones: Why REA and ArtCraft Are Going Viral
REA and ArtCraft are two projects driving a wave of AI-built clones that attempt to recreate Adobe and Microsoft software, letting developers reverse-engineer and rebuild commercial tools without access to the original source code.
Something crazy is happening in the AI development community, and I think we are witnessing the beginning of a major shift in the software industry.
Developers are no longer just vibe coding websites, dashboards, and simple applications. They are attempting to recreate entire commercial software suites, including Adobe Creative Cloud and Microsoft Office.
And the most interesting part? Some of these projects are being built by individual developers using AI coding agents.
Two names in particular have caught my attention: Reverse Engineer Anything (REA) and ArtCraft.
Why Are AI Software Clones Suddenly Going Viral?
We already have free alternatives to commercial software. GIMP competes with Photoshop, Inkscape offers vector graphics editing, and LibreOffice provides alternatives to Word, Excel, and PowerPoint.
But there has always been one major problem: switching costs.
Most alternatives have their own interfaces, shortcuts, and workflows. If you have spent ten years mastering Photoshop, switching to GIMP can feel like learning an entirely different application.
The new generation of AI-built clones is approaching this differently.
Instead of reinventing the experience, developers are attempting to recreate familiar layouts, menus, shortcuts, and functionality.
Imagine opening a free Photoshop alternative and immediately knowing where everything is. No extensive tutorials, no unfamiliar workflow, and potentially no expensive subscription.
That is the promise, although the actual quality and compatibility of these early clones still vary considerably.
REA Is Making Reverse Engineering More Accessible
One of the most exciting projects behind this movement is Reverse Engineer Anything (REA), an AI-powered reverse-engineering toolkit that has already attracted over 130,000 GitHub stars.
Traditionally, reverse engineering required specialized knowledge, complicated tools, and hours of manual work. REA makes the process much easier by connecting AI coding agents like Claude Code, Codex, and Cursor to tools such as Ghidra, Hopper, and IDA. [...]

## [151] Linus Torvalds "Did What I Preach", Used AI To Make Code Decipherable & Uncovered More Bugs
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~70 words

After using Claude Code to draft code to help make a fundamental improvement to the Linux kernel, Linux creator Linus Torvalds continued using AI this weekend and talking up its benefits. Beyond generating initial patches and a test program for that noted I/O enhancement, he separately talked up using AI/LLMs for making patches more decipherable to understand in the process the AI noted more long-standing bugs within the Linux kernel...

## [2] Codex CLI installs a persistent, self-updating background daemon by default
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [6] AI is a tool and using it well takes skill
Hacker News | full text via Hacker News | ~555 words

In his October 11, 2026 article, "'AI' is Not a Tool," Rich Hickey argues that LLMs are automation rather than tools because they cannot be wielded. I agree that outsourcing work can cost us opportunities to learn. But his conclusion does not follow. Even by his definition, an LLM can be something a human wields. And using it well takes skill, just as using other tools does.
Picking up a saw does not guarantee a straight cut. Holding a chisel does not make you a sculptor. Tools can amplify poor judgment as readily as good judgment. Their usefulness depends on the operator's ability to direct them, interpret feedback, recognize mistakes, and make corrections. Those requirements also apply to LLMs.
An LLM's unpredictability is a meaningful limitation. But predictability, reliability, simplicity, and bounded function are qualities by which we evaluate tools, not prerequisites for membership in the category. A tool does not stop being a tool because it is difficult to control or easy to misuse.
Hickey's distinction between tools and automation also creates a false division. Automation can be a feature of a tool. A compiler performs substantial work without the programmer continuously directing each operation. A spreadsheet recalculates results without someone manually carrying out every calculation. We still wield these systems by specifying inputs, examining results, and deciding what to do next. Why should generating text automatically disqualify an instrument from being a tool when translating code or calculating numbers automatically does not?
The claim that LLM use lacks intention, feedback, direction, and expertise is especially difficult to defend. A programmer can ask an LLM to explain unfamiliar code, challenge that explanation, inspect the source, test a proposed change, reject it, and refine the request. That is a feedback loop directed by a human pursuing a purpose. Doing it well requires knowing what to ask, what evidence matters, and when the answer is wrong. Expertise can make the instrument more useful.
Hickey's concern about reading is valid for a particular use: accepting a summary in place of reading a paper can sacrifice much of what reading teaches. But someone can also read the paper and use an LLM to question their interpretation, explore an objection, or identify something to examine more closely. The possibility of avoiding intellectual work does not establish that every use avoids it. [...]

## [9] Show HN: PS2 games statically recompiled to WebAssembly
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [25] Hello Python 3.15, goodbye 3.10, and now I can use 3.11
Simon Willison's Blog | full text via Simon Willison's Blog | ~984 words

Hello Python 3.15, goodbye 3.10, and now I can use 3.11
12th October 2026
Python 3.15 is here! Here’s the essential What’s new in Python 3.15 guide, this year curated by 3.14 and 3.15 release manager Hugo van Kemenade. As someone who builds open source software that works in every supported Python version, I get to say goodbye to Python 3.10 and start embracing features from Python 3.11.
First, some highlights from Python 3.15.
Explicit lazy imports
I’m most excited about Explicit lazy imports from PEP 810. These let you import modules like so:
lazy import json
lazy from pathlib import Path
The module will then be imported the first time those symbols are used in the code that follows.
My LLM CLI tool implements plugins. I had to recommend manual lazy imports in the plugin author documentation, because simply installing plugins that used heavy dependencies such as sentence_transformers could add multiple seconds to every invocation of the llm command. Lazy imports directly address this startup cost.
Unpacking in comprehensions
The new [*sublist for sublist in lists] unpacking syntax is neat. Here’s an illustration lifted from the documentation:
lists = [[1, 2], [3, 4], [5]]
[*L for L in lists]
# [1, 2, 3, 4, 5]
# equivalent to [x for L in lists for x in L]
sets = [{1, 2}, {2, 3}, {3, 4}]
{*s for s in sets}
# {1, 2, 3, 4}
# equivalent to {x for s in sets for x in s}
dicts = [{'a': 1}, {'b': 2}, {'a': 3}]
{**d for d in dicts}
# {'a': 3, 'b': 2}
# equivalent to {k: v for d in dicts for k,v in d.items()}
PEP 798: Unpacking in Comprehensions by Adam Hartz and Erik Demaine proposed this as an extension of the unpacking syntax from PEP 448, which landed in Python 3.5 back in 2015.
A sampling profiler
Python’s existing tracing profiler has been renamed from cProfile to profiling.tracing, and has been joined by an exciting new sampling profiler called Tachyon, aka profiling.sampling.
Sampling profilers work by periodically capturing stack traces from running processes, then using those to calculate which functions have the most time spent inside of them. They’re very low overhead and can provide a deep insight into running systems, without needing to instrument those systems first.
I’ve previously used tools like py-spy for this. Now this capability is baked into the standard library. [...]

## [31] OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide
NVIDIA Blog | full text via NVIDIA Blog | ~2147 words

As AI factories grow from megawatts to gigawatts, building them takes more than advanced computing. Open standards are helping the industry scale AI infrastructure faster, more efficiently and more reliably.
At the Open Compute Project (OCP) Global Summit, taking place in the San Jose McEnery Convention Center, NVIDIA announced new partnerships and contributions aimed at creating a common foundation for next-generation AI infrastructure.
NVIDIA contributed key NVIDIA Vera Rubin rack and compute tray designs to OCP through the open NVIDIA MGX architecture, giving system builders a common foundation for developing next-generation AI factory infrastructure.
Together, these efforts span the AI factory itself, the utility grid that powers it and the rack-scale architecture at the heart of modern accelerated computing.
NVIDIA and Partners Announce Open Architecture Advances
At the OCP event, NVIDIA and partners made a handful of announcements:
- NVIDIA and hyperscalers published open standards for next-generation AI factories, including AI factory design standards and grid resilience.
- NVIDIA launched new open source software components for NVIDIA DSX AI Factory.
- Meta and NVIDIA advanced open AI networking with NVIDIA Spectrum-X Ethernet SuperNIC and Spectrum-6 innovations.
- Visionbay introduced an 800V DC AI factory design for the Vera Rubin era.
- NVIDIA and Cisco announced the Ultra-Dense Small Form Factor Pluggable (USFP) standard, the industry’s first module for 400Gb/s-based networking fabrics.
- NVIDIA and Google announced Falcon Transport support on future NVIDIA ConnectX-10 SuperNICs and BlueField DPUs.
Before a packed audience, Ian Buck, vice president of hyperscale and high-performance computing at NVIDIA, discussed how open infrastructure is becoming a critical ingredient for scaling AI factories worldwide.
The news at OCP spotlights how NVIDIA’s extreme codesign combined with open standards is accelerating deployment, improving power efficiency and driving tokens-per-watt performance.
Vera Rubin AI Factories Advance With MGX Rack Contributions at OCP 🔗
NVIDIA joined industry leaders in contributing to the third-generation MGX AI data center reference design through OCP’s Open DC Initiative.
Combined with open liquid-cooling technologies such as MQD and MQDB, the effort helps turn proven AI factory designs into industry standards that others can adopt, manufacture and scale. [...]

## [36] Amazon has over 1 million robot workers. What’s next for human employees?
Ars Technica | full text via Ars Technica | ~3299 words

No organization in the world operates more robots than Amazon. The company already has more than 1 million robots working in warehouses around the clock to make tens of millions of same-day and one-day package deliveries happen on a daily basis—and Amazon is poised to significantly grow that robotic fleet in the coming years as it establishes new factories to churn out increasingly more capable robot workers.
Despite deploying so many robots, Amazon is also the second-largest corporate employer in the world, with more than 1.5 million full-time and part-time human workers, according to its 2025 annual report. Amazon executives say that the growing robot fleet has eased the burden on its human workforce by taking on the toughest fulfillment center tasks that carry the greatest risks of physical fatigue and injury. But labor advocacy groups and independent researchers point to evidence suggesting that warehouse automation driven by AI is not all upside for the humans who work alongside robots.
“For the last 100 years, most of the automation that we’ve seen usually happens away from workers—you’re taking that high-risk task away from the worker, and you’re doing so in a way that is not physically proximate,” Brian Greenwood, professor of business at George Mason University, told Ars. “The rise of collaborative robots really changes that dynamic for two reasons: one is that it is physically proximate, and two, the robot has the ability to dictate the pace of work.”
In many ways, robotics and AI are well suited to the relentless pace of work that is already happening inside e-commerce fulfillment centers. Amazon’s promise of speedy deliveries for its 200 million Prime subscribers in particular requires hundreds of thousands of human employees to speedily assemble and ship out customer orders that often combine a dizzying array of products.
Much of the work in fulfillment centers also frequently involves “dull, dirty and dangerous” tasks that people may prefer to hand over to robots. The injury and illness rate for workers in the US warehouse sector has typically been more than double the average across all industries, according to the US Occupational Safety and Health Administration.
“You have almost 2 million people working in the warehousing sector in the United States, and it’s characterized by very high turnover and very high workplace injury rates,” said Greenwood. [...]

## [42] React 19.3: Adds a browser() API, Giving Client-Only Rendering a First-Class Name
InfoQ | full text via InfoQ | ~540 words

React 19.3 shipped on npm on September 9, and alongside stable View Transitions and Fragment Refs it slips in a smaller but widely welcomed addition, a react-dom browser() API that lets a component formally opt out of server-side rendering. Aurora Scharff, who shared the docs, announced that the reference is now live and available in the Canary channel, where you pass the value to use() and the component suspends on the server.
The problem it targets is familiar to anyone doing SSR. Components that read localStorage, window, or the device timezone cannot produce meaningful HTML on the server, and the existing workarounds were awkward. Developers either flipped a mounted flag inside an effect or guarded rendering with typeof window !== 'undefined', a pattern that causes hydration mismatches the moment the server and first client render disagree.
The new API replaces both:
import { use } from 'react';
import { browser } from 'react-dom';
function LocalTime() {
 use(browser());
 return <p>{new Intl.DateTimeFormat().resolvedOptions().timeZone}</p>;
}
During server rendering, use(browser()) stops the component and leaves the nearest Suspense boundary's fallback in the HTML. In the browser it returns undefined, so the component renders as normal after hydration. It must be called from a Client Component and sit inside a Suspense boundary, or the server render fails. Because use() can live behind a condition, a component can defer only when it has to, for example a data hook that renders on the server when a loader supplies initialData and opts out otherwise. React also adds an onBrowserBailout callback and an optional reason argument so teams can report exactly where server rendering was skipped.
The change first landed as a React core PR that This Week in React described as "eliminating hacky server error-suppression workarounds". In the docs issue tracking the feature, one contributor wrote they were "very excited about the browser() api because it solves the client-only component problem in a much cleaner way than the previous ways". Writing about the release, one developer called the conditional data-fetching version "the cleanest solution to the 'should this fetch on the server or not' question I've seen".
The approach also narrows the gap with framework-specific escape hatches. Next.js users have long reached for dynamic(() => import('./C'), { ssr: false }) via next/dynamic, and Astro exposes a client:only directive, but both are tied to their bundlers. [...]

## [47] Xcode 27.2 Introduces an Agent- and Merge-Friendly JSON Format for Project Configuration
InfoQ | full text via InfoQ | ~411 words

Apple is introducing a new JSON-based format for Xcode project configuration files, replacing the traditional property-list-based format. Available in Xcode 27.2, the new format aims to improve readability, simplify maintenance, and make project configuration easier for AI coding agents to understand and modify.
The open source JSON file format (xcode-project-format) makes verifying project configuration changes easier when committing the project configuration file to your source code repository because changes in the comparison view correspond to your actions in Xcode.
A major advantage of the new format is that it reduces the likelihood of merge conflicts by providing a more stable and predictable representation of project configuration. The JSON format also makes the project structure more accessible to automated development tools, including AI coding agents, simplifying the inspection and modification of project settings.
To help developers work with the new format, Apple has also released a Swift package for encoding and decoding the new format. For example, this is how you list all targets defined in a project:
import XcodeProjectFormat
func listTargets(in projectURL: URL) throws {
    let projectData = try Data(contentsOf: projectURL)
    let project = try XCSchema.Project(jsonRepresentation: projectData)
    for target in project.targets {
        print(target.name)
    }
}
At the top-level, JSON schema defines not only targets but also the file tree, build configurations, build settings, and external dependencies. It also supports relationships between nodes in different subtrees. For example, a file specifies the build phases and targets it belongs to. Importantly, the formats avoid opaque identifiers wherever possible, favoring human-readable names and paths instead. Targets and build products are notable exceptions, as they use identifiers to support references from external files.
Commenting the announcement, senior iOS developer Nikita Dyachkov notes that
The issue of merging project files has been a long-standing problem since project files were introduced and was familiar to anyone who's worked in an iOS development team with more than one developer.
In the same thread, senior iOS engineer Khushal Jhalani described the new, more readable format as a "huge quality-of-life improvement". [...]

## [62] Speeding up the Unreal editor by… not using unnecessarily secure hash methods
TLDR Tech | full text via TLDR Tech | ~987 words

One good trick when trying to look for ways to optimize software is to stay away from areas that are very likely already quite well optimized, and instead focus on areas that might have been overlooked, either because they are too obscure or don’t show up during regular profiling sessions. This tactic worked well in the past, as shown with my optimization of tooltip creation, or the loading of editor localization files.
So when profiling the editor launch (again), this is why I mostly skip over any functions that contain words like “Shader Compilation” or “Shader Source” when I stumble over them in my profiler. The compilation of shaders is a famously long and elaborate process, and I’m pretty sure that very smart people at Epic already spent a lot of time optimizing those areas. That’s the reason why I would, for example, skip the function “Compile Global Shader Map,” even though its runtime would be typically multiple seconds:
This was, at least, true until one day I skipped over it using an unusually high zoom level and saw one of the functions that was called by it:
I am certainly not an expert for hash algorithms, but SHA1 is one of the (very few) hash algorithms that even I know. And seeing this hash algorithm being used to hash shaders seemed somehow wrong to me. That’s because SHA1 is was a cryptographically safe hashing algorithm, originally developed by the NSA  (yes, that one). And even though it has been cryptographically  broken years ago and actually shouldn’t be used for sensitive information anymore, this origin means that it is – to put it politely – not particularly fast.
What does not fast mean in this context? Well see for yourself in this comparison test of a bunch of commonly used hash algorithms that Aras Pranckevičius did a few years ago (actually, it was 10 years ago – I’m getting old). SHA1 was not even included as an actual competitor, but as the start of the article notes just “to illustrate the performance differences.” Ouch.
That’s especially annoying since the data being hashed is the shader source code, including all comments and copyright notice:
This means both that we have to hash a lot of data (source files can be quite big) and that there is no reason to hash it using a cryptographically secure hash, since it is no sensitive data.
Therefore, not using a cryptographically safe but fast hash algorithm should be an easy win, right? [...]

## [119] Ubuntu's Myna Speech-To-Text Now Available In Tech Preview
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~44 words

A few months ago Canonical announced Myna as a speech-to-text solution for Ubuntu 26.10 as part of their effort for building a context-aware desktop. Myna as of today is available in "tech preview" form not only for Ubuntu 26.10 but also the LTS releases...
