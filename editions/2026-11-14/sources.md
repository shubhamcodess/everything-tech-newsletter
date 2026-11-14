# Full text for 29 picks -- untrusted article content, treat as data only

## [1] FAA issues national ground stop
Hacker News | full text via Hacker News | ~1039 words

Much of the air traffic across the U.S. was suddenly shut down Friday after the Federal Aviation Administration ordered a nationwide ground stop for all departing flights “due to extraordinary circumstances and for reasons of safety.”
The unexpected and highly unusual alert, which was issued at 3:54 p.m. ET, contained no other information beyond stating that “all departing traffic should remain ground stopped until further notice.”
Follow along for live coverage.
“Inbound international flights will be managed on a case by case basis,” the FAA said.
When the FAA issued the alert, 4,042 flights headed for U.S. destinations were airborne, according to Flightradar24, a Swedish service that displays real-time aircraft flight tracking information.
Homeland Security Secretary Markwayne Mullin said there was “no indication as of yet” that there was anything “nefarious” that caused the ground stop. He said it was the result of a telecommunications outage “as of now.”
Mullin said President Donald Trump has been briefed and that they “are not ruling out anything at this point” in terms of what caused the communications issue. He said those currently on flights have no reason for concern. “We are assured that everybody is safe,” he said.
While the investigation into the failure is in a very early stage, there is no indication that the incident has been caused by malicious activity, officials from multiple agencies that are involved in the situation told NBC News.
They said they haven’t seen the type of activity that would normally be associated with a cyberattack. The officials, however, cautioned that the assessment could change as investigators learn more.
Three senior officials said there’s nothing that indicates a connection between Friday’s incident with the FAA’s systems and the Microsoft outage the day before.
Several hours after the ground stop was announced, a top aviation expert estimated that anywhere from 300,000 to 400,000 passengers were stranded — and it was anybody’s guess when they would get to their destinations.
“Daily we have about 25,000 flights in U.S. domestic markets,” Vikrant Vaze, a Dartmouth professor who specializes in commercial aviation logistics, wrote in an email to NBC News. [...]

## [68] Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs
TLDR AI | full text via TLDR AI | ~4716 words

Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs
Executive Summary
Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models. Six models released by these companies since April 2026 contain numerical patterns matching Blackwell hardware, whereas earlier models from the same companies match NVIDIA’s older Hopper generation. The findings suggest that several leading Chinese AI developers have begun using Blackwell to train their newest models. U.S. officials and press reports had already alleged that DeepSeek and Moonshot AI were using Blackwell chips, without publishing technical evidence.
The evidence comes entirely from the models’ own published weights, rather than from leaks or insider accounts. We recover traces of the models’ initial values, and then search for the hardware configurations and initial configurations that reproduce them; for DeepSeek-V4-Flash and Kimi K3, we also confirmed the match on physical Blackwell chips. The fingerprint identifies how the weights were created and supports, without proving, the inference that Blackwell also performed the training. Specially configured AMD hardware, which is also restricted from export to China, is the only alternative we have identified; we have excluded it for DeepSeek-V4-Flash, and consider it very unlikely for the other five models. Notably, our findings provide technical evidence of access to advanced computing hardware, but do not establish where the chips were located, how access was obtained, or whether export controls were violated.
Table 1. Hardware fingerprints in successive models from DeepSeek, Moonshot AI, MiniMax and Ant Group Link ↗
• Requires a U.S. license for export to China; none have been reported.
A Hopper fingerprint cannot distinguish an H800 from an H100 SXM or H200; the H800 identifications above are lab disclosures, not findings of this method.
Full list of models in Appendix 2 ↓
Main Findings
- Six models from four Chinese labs read as Blackwell-trained. DeepSeek-V4-Flash and MiniMax-M3 match NVIDIA’s Blackwell-class B200 or B300 chips, which have 148 processor cores (called streaming multiprocessors, or SMs). DeepSeek-V4-Pro, Kimi K3, Kimi K3.1-Pro and Ling-3.1-flash match the GB200 or GB300 chips, also Blackwell-class, which have 152 processor cores. [...]

## [29] Windows 0-day dropped by disgruntled researcher hands hackers System rights
Ars Technica | full text via Ars Technica | ~282 words

Nightmare Eclipse, the pseudonym of a researcher with an ongoing, very public beef with Microsoft, has dropped yet another Windows zero-day.
On Tuesday, Nightmare Eclipse disclosed SignDrop, a vulnerability that gives local users full System rights on some versions of Windows. The vulnerability resides in the Common Log File System, which Microsoft describes as a “general-purpose logging service used by software clients running in user-mode or kernel-mode.” By forcing a privileged process such as Windows Defender to open a crafted CLFS container, an attacker with ordinary user rights can abuse the privileged file creation to elevate privileges to System.
Turning a Windows defense against itself
The attack exploits the interaction of CLFS, Windows Defender, and Windows file permissions. The exploit uses Windows Defender to open a log file created by a standard user by calling ServerMpUpdateEngineSignature, a legitimate Defender function for processing antivirus signature updates.
By manipulating Windows Object Manager symbolic links, the attacker causes Defender to open the CLFS container in the security context of the antimalware engine. If an associated authentication file is missing, CLFS creates it using Defender’s System privileges. Because CLFS assigns the newly created file the Discretionary Access Control List of the original file, the attacker may gain access to a file created with System privileges, allowing the file-creation operation to be abused as part of a privilege-escalation attack.
Ironically, the vulnerability stems from a security measure Microsoft introduced in October 2025 to prevent attackers from exploiting other vulnerabilities in CLFS.
“If everything is chained correctly, funnily this legit security mitigation can be used against itself and allow an elevation [of] privileges,” Nightmare Eclipse wrote. “Everything is done properly by Microsoft here but the logic allows abuse.”

## [6] AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems
Hacker News | full text via Hacker News | ~1261 words

The Austrian logician Kurt Gödel was one of the most original thinkers of the 20th century. His two incompleteness theorems, published in 1931, transformed mathematics and paved the way for the digital age.
After his seminal results of the 1930s, Gödel published only a few papers. His unpublished work, however, runs to tens of thousands of pages, and is of great interest to historians of science.
Since 2017, the Finnish logician Jan von Plato has led a project at Helsinki University to understand the contents of 16 notebooks that Gödel wrote in the early 1940s. This material – the “workbooks” – is 1,009 pages of densely written text about maths and logic. Much of it is written in a German shorthand, Gabelsberger, that was obsolete even when Gödel was using it.
Progress in the mathematical understanding of the text was painfully slow – about a page a week – until September, when von Plato enlisted the help of the AI model Claude. Within a couple of days, Claude had provided a comprehensive digest of the entire material, revealing Gödel had proved hundreds of theorems that no one knew about.
The most famous logician of modern times had, in fact, discovered significantly more than anyone had thought.
“I was flabbergasted,” said von Plato. “The workbooks not only contain dozens of anticipations of results not known until the 70s and 80s, but they also contain 14 themes in logic that have not been pursued. Gödel was far ahead of his time.”
Gödel changed the course of logic because he revealed the limits of mathematical knowledge. His incompleteness theorems show that in all mathematical systems there are true statements that can neither be proved or disproved. Yet while this result was a blow to previous generations of logicians, who had hoped that all truths were verifiable, Gödel’s work pushed the field in new directions, inspiring Alan Turing to write his 1936 paper that began the theory of modern computation.
In 1940, Gödel fled Austria under the Nazis. He settled in Princeton, New Jersey, and became a close friend of Albert Einstein at the Institute of Advanced Study. Increasingly paranoid in his later years, he refused to eat food that was not cooked by his wife, and died of starvation in 1978.
Von Plato said he had started his Gödel project in 2017 because he was facing mandatory retirement from Helsinki University. “What should I do to make myself indispensable? [...]

## [14] Microsoft’s global outage may be worse than Amazon's or CrowdStrike's, expert says
Ars Technica | full text via Ars Technica | ~360 words

A global outage taking down a wide range of Microsoft 365 services remains ongoing Friday morning.
The outage started midday Thursday, impacting users of Microsoft email, cloud, and AI services. Microsoft has documented the full list of services impacted by the error, while moving early Friday morning to protect customers around the world from losing emails during the extended disruptions.
“Recovery actions are ongoing,” the Microsoft 365 Status account confirmed on X. “To help preserve delayed mail during this event, we’ve extended email timeout to 48 hours.”
Similar to recent world-shaking outages of widely used tech like Amazon Web Services and CrowdStrike, the Microsoft disruption looks like “one of the biggest outages of all time,” Ciaran Martin, the former head of the UK’s National Cyber Security Centre, told NBC News. Possibly even “worse,” he suggested.
Businesses, hospitals, police departments, and schools were among those scrambling to work around the outage. In Japan, it disrupted government IT infrastructure, according to deputy chief cabinet secretary Masanao Ozaki. NBC’s report documented various harms, noting that “few public bodies were immune from the outage.” In some cases, doctors couldn’t send patients “important” updates on medication changes or follow-up care.
The financial sector suffered, too, with people blocked from making bank transfers since they couldn’t receive verification codes.
Justice systems were also hobbled. The Supreme Court in the Philippines saw its legal work derailed, NBC reported. And one US sheriff’s office in Colorado reported that the outage made it difficult for people to post bond for prisoners’ immediate release.
It’s unclear how many users were affected, but Microsoft estimated in January that the total number of paid Microsoft 365 commercial subscriptions exceeded 450 million.
Microsoft blames failed server health checks
On a status page, Microsoft said “we have no evidence of malicious activity associated with this incident” and promised to “share a full Post-Incident Report with root cause and defense-in-depth actions after mitigation is complete.”
“We’re aggressively pursuing all pathways to reduce impact,” Microsoft said on X.
But Microsoft’s public statements make clear that the tech giant was blindsided by the outage and struggled for hours to find mitigations that could reliably restore user access.

## [137] Anthropic now lets you self-host Claude Managed Agents. The catch? 8 hours to act if it flags a safety risk
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~29 words

Anthropic has unveiled a self-hosted version of its platform for building and running AI agents. Self-hosted Claude Managed Agents, as The post Anthropic now lets you self-host Claude M

## [169] Uber confirms hackers stole thousands of drivers’ license information in data breach
TechCrunch | full text via TechCrunch | ~393 words

Uber is notifying thousands of drivers that their personal and driver’s license information was stolen during an October data breach at one of the company’s tech providers.
In notices filed this week with several U.S. attorneys general, including California, the ride-hail giant said it was notified on October 9 by the provider that hackers broke in and stole internal credentials, which were used to access Uber’s data.
The company said it subsequently began notifying affected drivers that their personal information was stored with the provider.
TechCrunch has learned that the provider is Fireworks AI, which lets developers access and use open AI models. Fireworks reported a data breach last month in which hackers stole its customers’ information, including billing data and some private AI datasets.
Online productivity startup Notion confirmed its data was also stolen in the Fireworks hack.
“The notices to drivers are in relation to a security incident impacting one of our third-party vendors, Fireworks.ai, which had access to some Uber data,” an Uber spokesperson told TechCrunch, deferring our questions to Fireworks.
Uber did not say how many customers are affected by the breach, nor how many drivers it was notifying about the incident.
When reached by email, a spokesperson for Fireworks confirmed that the company identified a security issue involving unauthorized access to some of its systems, which affected customer data, but the spokesperson did not address our questions about the incident.
According to data breach notices seen by TechCrunch, the stolen data includes driver’s licenses of 2,567 individuals in Massachusetts, 3,430 people across South Carolina, and 1,873 residents of Rhode Island. A filing with Illinois showed that some state residents had their driver’s license information stolen, but that the number of affected people was pending. Uber also notified drivers who live in California, but did not say how many had their information stolen.
The number is expected to rise as more data breach notifications roll in.
Fireworks attributed its breach to a financially motivated cybercriminal group whose goals are to sell stolen tokens for accessing large language models, or LLMs.
No known cybercriminal group has taken credit for the data theft.
This is Uber’s second known data breach this year. The company reported a security incident at its Uber Freight truck shipping unit, for which an extortion gang took credit for stealing data.
Updated with a response from Fireworks.

## [136] US Seizes $1.2 Billion In Crypto Stolen From Binance
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~89 words

U.S. authorities have seized or restrained more than $1.2 billion in cryptocurrency stolen during Binance's $6 billion October hack, which the FBI attributes to North Korean military-linked hackers known as "TraderTraitor." The DOJ also said it disrupted infrastructure behind the "FaceStealer" deepfake scam, blamed for stealing more than $400 million in cryptocurrency. CNBC reports: Collective efforts between the U.S. government and private sector have resulted in more than $2.7 billion of that amount being frozen. [...] The DOJ said it was taking coordinated action against what it called the

## [33] Introducing ChatGPT Wallet
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~24 words

Introducing ChatGPT Wallet, a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections.

## [160] Advocacy Groups Sue AI Giants to Freeze New Models, Warning of 'Catastrophic' Risks
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~86 words

A coalition of online safety and consumer advocacy groups has sued five of the world's leading artificial intelligence companies, asking a California judge to halt the development and deployment of new AI models until the companies can address what the plaintiffs describe as potentially "catastrophic" risks. The lawsuit alleges the companies are violating California unfair competition law by endangering public health and computer systems, arguing that increasingly autonomous AI could ultimately escape human control. The Associated Press reports: The filing, first reported on by The Associated

## [202] Chainguard defends its choice to break the PHP security embargo: “We own the decision.”
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~24 words

At KubeCon + CloudNativeCon North America 2026 this week, Chainguard co-founder and CTO Matt Moore defended the company’s decision to The post <a href="

## [11] Reverse engineering my Coway air purifier to ditch the cloud
Hacker News | full text via Hacker News | ~3060 words

The year is 2017. A string of annual wildfires rocks the West Coast. The sky looks like this in the daytime:
My home, like many in the Bay Area, has no insulation and isn’t really air sealed. To avoid choking on soot, a lot of people started buying air purifiers like this one:
It’s an overpriced box fan with a HEPA filter and an air quality sensor. It has some controls for the fan speed, and it can also automatically ramp up if the air quality is bad. It’s ugly, but they’re so ubiquitous around here that I feel like no one even notices them anymore. Also, FWIW, the device works. It really does improve air quality.
This device became a staple item in our household when my wife eventually started cranking up the fan at night for white noise (a dual purpose!). Over time, I have become accustomed to it and now also require it to sleep.
The Good Night button
Our home also has smart lighting, and it’s all integrated with Apple Home. At night, I always press the “Good Night” button, which shuts off all the lights. I really wanted to tie the fan into that. I’d press Good Night, the lights would shut off, and the fan would crank up to my wife’s preferred white noise volume.
The old Airmega didn’t have Wi-Fi, so there was no easy way to integrate it with Apple Home. When it eventually broke, I bought the now-discontinued Coway Airmega IconS (for non-discontinued Wi-Fi models, check out the Airmega 250S or Airmega MightyS). It’s still just a box fan with a HEPA filter, but it’s considerably more expensive, aims to look like a piece of fancy mid-century furniture, and most importantly, can be controlled over Wi-Fi (sort of).
The existing Home Assistant integration
Coway’s iPhone app is an absolutely classic IoT affair. It takes forever to load, and it asks me to change my password nearly every time I launch it. Thankfully, a brave soul reverse-engineered the app and wrote an integration for Home Assistant. The integration more or less pretends to be the phone app. It polls the Coway cloud service for status updates and sends commands through it to control the fan. Home Assistant bridges that to Apple Home and… voilà!
Why ditch the cloud?
The downside of this approach is that you’re still at the mercy (or lack thereof) of the Coway cloud service. It seems like at least once or twice a year, it breaks.
Here are some of the reasons I have seen it break:
- Coway didn’t like the integration hammering their servers and banned it. After a protracted argument with the community, they eventually settled on allowing it. [...]

## [143] AI agent startup LangChain hits $3B valuation
TechCrunch | full text via TechCrunch | ~230 words

Agent management startup LangChain has raised a $300 million Series C at a $3 billion valuation led by CapitalG, with participation from investors, including Singapore’s GIC, DFJ Growth, IVP, and Sapphire Ventures, the company announced on Friday.
That’s more than double its $1.25 billion valuation when it raised $125 million about a year ago, led by IVP.
LangChain began in 2022 as a popular open source project that handled the kinds of tasks that early-stage LLMs found difficult, like searching the web, calling APIs, and interacting with databases. As the frontier AI labs delivered harnesses that now competently do those tasks, LangChain turned its focus toward managing AI agents. It has apparently found its stride in this highly competitive area with a simple message: letting businesses own their own intelligence.
With its open source roots, the startup says its agent creation and management software, LangSmith, is not trying to lock users into any particular model, cloud, or ecosystem, unlike the major clouds or frontier AI labs. It also promises that LangSmith will contain agent behavior and is easy to use.
True, there are plenty of other startups pitching similar advantages these days and also doing well (case in point is newcomer Mintive). However, LangChain has had a head start and now claims 7,000 LangSmith customers, including big-name startups like Harvey, Rippling, and Clay, and enterprises like Nvidia, Toyota, and Salesforce.

## [58] SpaceX and Tesla Talks on Record Merger Are Said to Progress
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~65 words

SpaceX and Tesla could announce a merger deal as soon as December. The companies' boards and advisers are working out the terms of the deal and the governance structure of the combined entity. The merger will be a major test case for political sentiment following the US midterm elections. The aggressive timeline reflects Elon Musk's tendency to move quickly when it comes to corporate maneuvers.

## [20] Starship flight 15 powers to orbit—setting up a possible catch on Saturday
Ars Technica | full text via Ars Technica | ~355 words

STARBASE, Texas—Starship lifted off right on schedule Friday from South Texas, making its 15th test flight in more than three years.
The largely successful launch took place in the early evening; as the massive rocket rose into the atmosphere, the Sun sank toward the western horizon. Conditions were ideal for the launch, with the atmospheric winds so calm the rocket’s white plume did not dissipate for many minutes. The weather in South Texas is not always comfortable; summers are long and hot. Friday evening was perfect at Starbase.
The first stage ascended toward space flawlessly, releasing the upper stage above the Gulf of Mexico. From there, the Starship upper stage ignited its Raptor engines and powered its way into a nominal orbit. This was the second time SpaceX has flown Starship into low-Earth orbit.
When it came time for the first stage to return to the ground, it dropped like a rock. However, due to an unspecified issue, the vehicle was commanded to divert into the Gulf rather than return to the Starbase facility to be caught by the launch tower. It created a fantastically powerful explosion, even for observers more than 10 miles away.
Primary mission, a success
The primary aim of Friday’s launch was the deployment of 26 Starlink V3 satellites from a narrow door at the base of the spacecraft. This occurred about 40 minutes into Starship’s flight, and all 26 satellites—which have solar panels that stretch 60 meters end to end when fully deployed—safely made it into orbit, where they will now use onboard propulsion to raise their altitude.
This means that Starship is now an operational, orbital rocket. It is the largest and most powerful machine humans have ever launched into space. The challenge for the company now is to make Starship reusable and dramatically increase its flight rate.
In that sense, the first part of Friday’s mission was not a success. SpaceX had hoped to return the first-stage booster, refurbish it, and fly it again. The company has previously landed and reflown Starship boosters but has yet to do so with the latest iteration of the vehicle, version 3.

## [127] Amazon has a plan to index the world’s online shopping data
The Verge | full text via The Verge | ~350 words

Amazon has plans to build a vault of data on every product sold anywhere on the internet, even products Amazon doesn’t sell, and make the information available through its own site, according to Reuters. The project, called the “World Product Graph,” is meant to make it less likely that shoppers leave Amazon to do their product research on Reddit or Google, and make it more likely shoppers end up at Amazon even if they’re searching for a product sold elsewhere. The same goes for AI agents — if Amazon has the largest stockpile of shopping data, AI agents may rely on its index of products over others, so even people shopping with bots will end up on its pages.
Amazon has a plan to index the world’s online shopping data
Listing the details of everything for sale everywhere is meant to make Amazon more useful than Reddit for people and AI agents.
Links to outside retailers’ products have already started popping up on Amazon through the “shop direct” feature it launched last year. The company also has its own AI shopping assistant, Alexa for Shopping, previously called Rufus. The World Product Graph project would also be aimed at fixing issues with the AI by providing it more data. According to Reuters, an internal Amazon document on the project says “Many Rufus answers are factually wrong or incomplete” and running users’ Amazon searches with the AI is expensive. Adding more data is reportedly supposed to make the system more accurate and able to use cheaper models.
Whether this actually ships is still up in the air. The internal document reportedly says the project “depends on discovering how brands organize their products on their own websites,” which could involve Amazon crawling other retailers’ sites. Reuters says it’s unclear “if or when this plan may be implemented,” but said the document on it included an October 1st, 2027 release date.
Amazon said in a statement to Reuters that “Draft, outdated documents often paint an incomplete picture and the existence of a brainstorming document such as this one doesn’t necessarily reflect our current plans.”

## [138] Cloudflare Open Sources Kitesurf: Their Web Browser For AI Agents
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~30 words

Earlier this year Cloudflare announced Kitesurf as a stateless web browser for AI agents. After building out its features, they have now made good on their word to open-source it...

## [142] Mozilla to Shut Down Solo, Deleting Users' Websites and Data
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~99 words

Mozilla is shutting down Solo, its AI-powered website builder and hosting service, on November 30. A notice on the Soloist.ai homepage reads: "We've made the difficult decision to close Solo. We have appreciated all of your support building and growing this product, and the feedback we've received from all of you. Solo will cease operations on Nov 30, 2026." The Register reports: Mozilla launched Solo in December 2023 as a "Mozilla Innovation Project," aimed at helping sole traders to build themselves a webpage for their services. Some 54,000 people used its LLM to build pages, and relied on M

## [73] Migrating Our Email API to Go
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1246 words

What it took to move our most critical API to Go.
Rebuilding an API means preserving years of decisions, including the ones that never made it into the documentation.
For Resend, that meant matching error responses, idempotency behavior, rate limits, stored data, and the contents of the emails themselves. A faster implementation would only be useful if developers could continue relying on the behavior they already knew.
Over seven weeks and roughly 140 pull requests, we took a new Go service from an empty project to production traffic.
By October, Go was handling all our email API traffic. While traffic was split evenly between the two services, Go showed roughly half the median latency and about one-seventh the memory usage per task.
The existing Node service had failure modes we wanted to address.
During bursts of large requests, a whole task could become unresponsive. One investigation traced this to parsing and serializing large request bodies, including requests that were already being rejected by the rate limiter.
Parsing and serializing are CPU-heavy synchronous operations in Node.js that block the event loop until they are complete. Work associated with those rejected requests could block the task from handling other traffic.
We also saw S3 timeouts surface as customer-facing 408 and 524 errors.
These problems shaped the requirements for the replacement: more predictable behavior under load, lower resource usage, and better control over how long individual operations could take.
Changing the implementation also meant revisiting request handling, timeouts, connection pools, and capacity. Those decisions became a substantial part of the migration.
Our engineering philosophy calls for predictable behavior and backward compatibility. During a rewrite, that principle becomes a testing problem: how do you establish that two implementations behave the same way?
We built a harness that sends the same requests to Node and Go and compares their behavior. Its coverage includes responses and errors, database rows, S3 objects, idempotency, and rate limits.
Checking the HTTP response alone would leave too much untested. Both services could return a successful response while persisting different metadata or producing different email content.
The existing implementation became a reference for compatibility. We also preserved some Node quirks deliberately. Changing an unexpected behavior can still break an integration that depends on it.
HTML-to-text conversion was a particularly useful example. [...]

## [124] ‘We need more reviewers’: Finding Linux bugs is easy now – fixing them is another story
ZDNet | full text via ZDNet | ~761 words

ZDNET’s key takeaways
- Microsoft found some Linux kernel problems.
- Thanks to AI, Linux and Windows struggle with increasing bug reports.
- Maintainers are stretched but there are signs of hope.
Recently, Microsoft’s FORGE Lab reported that its AI scanning system, MDASH, turned up 59 upstream Linux kernel bug reports, including one flaw at least 21 years old. That’s less impressive than it sounds. For 2026, through Nov. 2, the Linux Common Vulnerabilities and Exposures (CVEs) team reported an average of 27 CVEs a day.
Why so many? Easy: in Linux, any bug can be a security bug. As Linux Torvalds told me in 2024, “Bugs will happen, and anything can be a security bug if somebody is clever enough to just figure out how to abuse it.” Besides, since Linux runs everything from smartphones to refrigerators to supercomputers, what may be a serious bug in one device may not even appear at all on another.
It’s not just Linux, though. In the latest Windows Patch Tuesday security release, Microsoft reported 726 CVEs. The vast majority of these bug reports are coming from AI programmers. Finding bugs on anything is no longer the hard part. But reviewing and fixing them is, and both Microsoft developers and kernel maintainers are struggling to keep up.
More from ZDNET
Also: Microsoft fixes over 1,000 Windows flaws – and one is being exploited
Maintainers breaking under the strain
That’s hurting the overworked maintainers. On Nov. 10, an ARM engineer and Linux kernel maintainer Lorenzo Stoakes gave up reviewing code. He’d been a reviewer for the memory-management core, misc, reclaim, and Rust-related sections. Stoakes, a kernel contributor since 2014, wrote, “Given the current throughput in the kernel resulting from AI-generated series, I unfortunately lack the bandwidth to generally be able to offer review except in those areas I maintain.”
Stoakes added, “Of course the AI wave has been horrible, and is getting significantly worse. At first it was once in a while that I’d see slop. Then it was at least once a week. Then every few days. Nowadays it’s pretty much half of what I see, if not more.”
Also: Filing bugs for open-source apps is a huge help for devs – and easier than you think
He’s not alone. As Greg Kroah-Hartman, the Linux kernel stable maintainer, said in a Q&A session at Open Source Summit Europe, “We don’t have enough people to review them, the onslaught of the LLM-generated patches. We need more reviewers. We don’t have enough. [...]

## [118] DeepSeek’s coding agent is too tidy for its own good — and benchmarks are punishing it
The New Stack | full text via Stack Overflow Blog | ~1183 words

I lead an engineering team of eight at Momentic that has eagerly adopted background agents. My team frequently awes at the raw intelligence of these frontier models, but they also often complain that their agents will confidently declare that a feature was complete, only for basic functionality to fail when they opened the application for testing.
The problem isn't just that agents make mistakes. It's that their own verification often fails to catch them, leading to overconfidence.
Concretely, our engineering team has found three recurring problems: agents rely on shallow checks, inherit their own implementation blind spots, and become less reliable under the combined pressure of growing context and repeated failures.
1. Shallow checks
Coding agents gravitate toward checks that are easy to write and easy to pass. That usually means unit tests.
Unit tests have their place, but a green test suite doesn't necessarily mean the software works end to end.
At Momentic, we recently conducted a human-reviewed audit of 1,000 AI-authored unit tests in our monorepo. The result: only 9.6% were useful verification checks.
The remaining 90.4% provided little meaningful value. Nearly a third were low-consequence tests checking basic argument passing or formatting. Another 22.8% duplicated existing coverage, while 22.4% relied excessively on mocking that poorly reflected production behavior.
Figure 1: AI-authored unit tests
Our findings aren't isolated. In a recent experiment, AI researcher Kun Chen compared coding agents allowed to write their own tests against agents explicitly prohibited from doing so.
Across 111 coding tasks, the agents that wrote tests achieved a 65.3% success rate, compared with 66.2% for those that didn't.
This doesn't mean unit tests are useless in general. It means an agent can author massive volumes of unit tests, get seemingly reassuring results, and still fail to verify the behavior that matters.
2. Shared blind spots
When an engineer writes a feature, they first form an understanding of what needs to be built. They then make implementation decisions based on that understanding.
On the surface, coding agents work similarly. The problem is that when they write their own tests, those tests reflect the same, possibly erroneous, assumptions that went into the implementation in the first place.
For example, suppose you ask an agent to build a rich text editor. It implements bold, italic and, underline formatting, then creates tests for those buttons. [...]

## [117] Git 2.56's history drop command replays commits 40 to 77 times faster than rebase
Dev.to | full text via Dev.to | ~1712 words

I wanted to remove one commit from the middle of a bare repository without checking anything out. The usual answer is: you can't, not directly. You add a worktree, rebase, then throw the worktree away. Git 2.56, released on 28 September 2026, ships an experimental command that skips all of that: git history drop. I built it from source and measured what it actually saves.
Short version: on a bare repo with 400 commits stacked after the one I wanted gone, the classic worktree-and-rebase approach took 26.5 seconds. git history drop took 0.36 seconds. That's not a rounding difference.
Setting it up
Git 2.56.0 isn't in Ubuntu's apt repositories yet, and I don't have a release binary for it, so I built it from the tagged source:
$ git clone --depth 1 --branch v2.56.0 https://github.com/git/git.git git-src
$ cd git-src
$ make -j4 NO_GETTEXT=YesPlease NO_TCLTK=YesPlease NO_PERL=YesPlease \
    NO_PYTHON=YesPlease NO_CURL=YesPlease NO_EXPAT=YesPlease
$ ./git --version
git version 2.56.0
git history is explicitly marked experimental in its own man page: "THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE." It currently has four subcommands: drop, fixup, reword, split. I focused on drop, which removes a commit and replays everything after it onto the commit's parent.
The benchmark
For each test size, I built a fresh non-bare repo with a root commit, a target commit to drop, and N descendant commits, each touching a shared file and a unique file so the replay has to do real diff work. I then cloned it --bare twice, so the two methods started from byte-identical history:
- 
Old way: git worktree add a linked worktree off the bare repo, run git rebase --onto <target>^ <target> main, remove the worktree.
- 
New way: git history drop <target> --update-refs=branches directly against the bare repo, no worktree at all.
Three trials per size, wall-clock date +%s.%N around each run:
Both methods produced the same resulting tree. I checked the tree hash of main after each run on a smaller repo and they matched exactly, even though the individual commit hashes differed (new commit timestamps, naturally):
$ git -C old.git rev-parse main^{tree}
fadfb2c2c2f23eb52db063920d6e686fb90ea5f2
$ git -C new.git rev-parse main^{tree}
fadfb2c2c2f23eb52db063920d6e686fb90ea5f2
So this isn't a case of the new command cutting corners. It gets to the same place, just much faster.
Where the 70× actually comes from
My first guess was that the saving was mostly in skipping git worktree add and the later git worktree remove. [...]

## [209] I Mutation-Tested 50 Python Libraries. Tests in the Young Ones Missed 41% of Planted Faults.
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~26 words

Across 2,312 planted faults the study also surfaced four real library problems, from a Windows data-loss bug to README examples that do not work as written.

## [205] RAG Retrieval Lost 40 Points When Distracting Passages Grew to 2.68M
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~22 words

A reproducible test of BM25, embeddings, and parent documents shows why author-written evals overrate search, and why answer position in context matters.

## [53] Announcing Long-Context Training on TPUs with MaxText Context Parallelism
Google Developers Blog | full text via Google Developers Blog | ~1490 words

Long-context training — including pretraining and post-training, has become a foundation of frontier AI models. Longer native sequence lengths give large language models (LLMs) the working memory to read a whole code repository or ingest hours of video, and reason through multi-step agentic tasks. In three years, context windows have grown from 128K–200K tokens to 1M–2M, and models trained toward 10M tokens are arriving. Training at those lengths, not just serving them, is where the system limits show up.
In particular, efficient training at multi-million-token sequence lengths runs into the following bottlenecks:
Today, we are excited to announce long-context training support in MaxText, Google Cloud's open-source JAX training framework. MaxText enables this by supporting four context-parallel strategies on Cloud TPU: All-gather, A2A (DeepSpeed Ulysses), P2P (Ring Attention), and the A2A + P2P hybrid (Unified Sequence Parallelism, or USP), combined with load balancing and sequence packing. All four use the Tokamax Splash Attention kernel. Combined with the 3D inter-chip interconnect (ICI) ( supported on TPUs such as TPU 5p or TPU 7 (Ironwood) ), this lets one sequence span an entire slice while communication overlaps compute and memory per chip stays flat. In our benchmarks, Llama 3.1 8B (25 head dim, 16 query heads) demonstrates exceptional long-context efficiency, achieving 70% Model FLOPs Utilization (MFU) on TPU 5p for sequence lengths up to 4 million tokens. Across both TPU 5p and TPU 7, context can be seamlessly extended to 14 million tokens—with TPU 7 consistently maintaining 50% MFU across all sequence scales below 6 million tokens.
This functionality is available today in MaxText v0.2.4(doc).
Context parallelism splits a long sequence across chips, so no chip holds the activations of the whole sequence. Context parallelism can be combined with data and tensor parallelism, and the smallest context-parallel size that fits your sequence in HBM is usually the right one. This also holds for sparser attention variants which cut attention compute but not the activations of every other layer.
Attention is the one global operation where every token needs the keys and values of every preceding token, so each context parallel strategy has to bring those keys and values back together. Each makes a different tradeoff between memory (how much KV a chip holds), communication (how much moves per layer, and whether it overlaps compute), and model shape (how many attention heads to split). [...]

## [38] Netflix Turns Operational Data Into a Knowledge Graph for AI-Driven Observability
InfoQ | full text via InfoQ | ~594 words

Netflix is developing an ontology-driven knowledge graph to accelerate production investigations and provide AI agents with a shared understanding of its operational environment. The platform connects information about applications, incidents, deployments, alerts, and infrastructure dependencies, addressing a problem that can leave engineers spending hours piecing together information scattered across different systems.
The company claims it handles more than 2 billion requests daily and upwards of 38 million real-time logging events every second. During the November 2024 Jake Paul-Mike Tyson fight, its infrastructure supported approximately 65 million concurrent streams. Yet investigating a typical application regression can take around four hours, with much of that time spent reconstructing relationships between systems rather than analysing the underlying data.
Netflix's solution is to make those relationships explicit through an operational ontology and knowledge graph, creating a foundation for automated root-cause analysis and, eventually, self-healing infrastructure.
Netflix already collects metrics, events, logs, and traces (MELT) across its applications and infrastructure. However, these signals are spread across systems such as alerting, incident management, deployment tooling, and engineering communication platforms.
An application regression might originate from a client release, an experiment, infrastructure load shedding, or a service several dependencies downstream. Although each system contains useful information, engineers must often connect the evidence manually.
Netflix identified the missing capability as a consistent way to describe not just individual components, but how they relate to one another.
Its Observability Ontology provides that common model, defining operational entities, their properties, and the relationships between them. It uses established standards including RDF, OWL, SHACL, and SPARQL, while the resulting knowledge graph is stored in QuipuDB, Netflix's distributed RDF database built on Rust's redb storage engine.
The graph is populated through a pipeline of components Netflix calls enrichers. These consume information from operational systems and transform it into structured relationships, represented as subject-predicate-object triples.
Some enrichment is deterministic, while other stages use LLMs and probabilistic techniques to interpret less structured information. [...]

## [35] Google Open Sources Ambient Quality Agent (AQuA) to Diagnose Production AI Agent Failures
InfoQ | full text via InfoQ | ~460 words

Google has open-sourced AQuA (Ambient Quality Agent), a reference implementation that analyzes production AI agent sessions, verifies recurring failure patterns, and investigates root causes against deployed source revisions. The tool targets silent quality regressions that conventional infrastructure monitoring can miss, such as agents ignoring user preferences or skipping required tool calls while returning successful responses.
AQuA runs alongside an agent in Google Cloud, outside its request path, reading telemetry from Cloud Trace, Cloud Logging, or BigQuery. It samples up to 1,000 recent sessions per run and processes them through five stages: sampling, reviewing, clustering findings, verifying candidate clusters, and tracking issues. Developers can configure domain-specific quality criteria through a goal.md file and add deterministic custom metrics. AQuA can run on a schedule, after a deployment, or on demand.
For root cause analysis, AQuA compares failing sessions with an immutable source snapshot captured at deployment. Its diagnosis agent identifies relevant code or instructions, cites file and line ranges, and proposes changes when the cause lies in the repository. It can also attribute failures to external dependencies, tool handoffs, or retrieved data. AQuA does not apply fixes or open pull requests automatically.
AQuA sidecar architecture (Source: Google Developer Blog Post)
Google evaluated 32 sessions from a multi-agent travel application, identifying 42 findings grouped into nine candidate clusters. The verifier rejected three unsupported clusters after checking up to three full transcripts per candidate cluster, leaving six verified issues. Two involved bypassing seat availability checks and losing a traveler's vegan preference during delegation.
After developers modified prompts and replayed the sessions, seat-selection bypasses fell from 15 sessions to two, dietary-preference omissions dropped from seven to zero, and sessions passing all checks increased from five to 13. These results came from controlled replay, not production traffic.
The Google blog post states,
An insight is its citations, not a self-reported confidence score.
Findings link to supporting traces, and proposed root causes must reference valid lines in the deployed snapshot. AQuA tracks findings as NEW, RECURRING, or automatically RESOLVED after 14 days without being observed. Sampling can miss rare failures, and replay may not reproduce external state. [...]

## [49] Dropbox Shares How Its In-House Cookie Auditor Tests Consent Behaviour Across 200+ Web Surfaces
InfoQ | full text via InfoQ | ~589 words

Dropbox engineering has published a detailed account of how its in-house cookie auditor validates consent behaviour across more than 200 web surfaces, offering a glimpse into the practical challenges of maintaining privacy compliance at scale. The post, authored by Yasmin McDowell and Lawrence Good, outlines a Playwright-based system that behaves like a privacy-conscious visitor and checks that pages only load cookies consistent with a user's stated preferences.
The auditor runs three separate tests against every page in scope, one simulating a standard US visitor, one simulating an EU visitor, and a third that sends a Global Privacy Control (GPC) signal. Each test begins in a fresh, isolated browser context with no existing cookies, mirroring what a new visitor would see. Before any interaction, the auditor records which cookies have already loaded and verifies they match the expected baseline for that scenario, then locates the page's consent controls, declines non-essential cookies, reloads the page and checks that the preference still applies.
The controls are not identified by text. Dropbox supports 22 languages and the banner may appear as a floating element, a preferences window, or a footer link, so the auditor interacts with the underlying consent elements rather than button labels. A pragmatic design choice is keeping cookie classifications outside the auditor's source code, which allows the Privacy team to update the approved cookie list and known exceptions without waiting for an engineering release. Because the consent banner itself was also built in-house, the auditor plugs directly into existing infrastructure rather than wrapping an off-the-shelf product.
Dropbox built what it calls "an auditor for our auditor," a companion URL detector that uses traffic data to find every live Dropbox web surface. Billions of visit records are filtered down to a manageable list of unique paths, then grouped by consent logic so that representative URLs can stand in for large families of similar pages.
Projects such as @slashgear/gdpr-cookie-scanner ship an open-source CLI that scores GDPR behaviour from 0 to 100 and integrates with GitHub Actions, while ConsentCrawl targets over 25 consent manager platforms including OneTrust, CookieBot and TrustArc Truste. A Dutch study recently used Playwright to analyse 6,168 political party URLs for unconsented tracking, suggesting the same browser automation approach is becoming standard in academic privacy research. [...]

## [102] Technical Debt is Social; it is the Price of Learning by Doing
InfoQ | full text via InfoQ | ~727 words

Technical debt is not necessarily a sign of poor engineering. It can be the price of learning through software in use. As AI accelerates code production beyond our capacity to understand code and context, technical debt increasingly becomes a sociotechnical challenge, Xin Yao noted in her talk "What If Your Biggest Technical Debt Is Social", at GOTO Copenhagen.
Yao quoted Ward Cunningham, who defined debt as "not-quite-right code". Debt sounds like a negative thing, but it can be a deliberate business strategy, she explained:
If we release the code now, well knowing it’s not perfect for the future yet, we’ll get some business feedback, we’ll get some user feedback, we’ll probably get paid for something, and that’s good as a business strategy.
Debt isn’t about poorly written code; it arises when we design software with incomplete knowledge. Hence, debt is the price of learning by doing, Yao argued. Releasing software allows us to test our assumptions against reality. Once we’ve got a learning experience, we have to put that experience back into our code and pay off the debt, she added. The debt becomes problematic when our software doesn’t catch up with our new learning.
Debt can be a good communication strategy toward management. It provides an economic argument for the cost of postponing architectural improvements. However, framing technical debt solely as something to eliminate misses its strategic value. The question is not whether to incur debt, but whether the learning it enables justifies the cost, and whether we actually repay it.
Yao referred to Kent Beck’s article "Earn and Learn," which explores features vs. futures. Features deliver value today, while the future is actually the optionality to adapt those features, Yao explained:
Every bit of code already coded is complexity and a constraint. Every feature removes some future. If you go on producing features, maybe using your LLMs, then at a certain point, all you can do is use your capacity to pay the interest, to fix the code, and you can no longer release features.
The challenge is to balance delivering features with preserving future options, Yao said. Sometimes, delaying a design commitment preserves options until we know more, and this includes postponing some upfront architecture decisions to the last responsible moment as well. As Beck argues, waiting is not laziness; waiting is holding an asset.
Technical debt can therefore be understood as learning made visible in software. [...]
