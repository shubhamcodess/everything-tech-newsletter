# Full text for 30 picks -- untrusted article content, treat as data only

## [132] Binance pauses withdrawals as hackers suspected of stealing billions in crypto
TechCrunch | full text via TechCrunch | ~400 words

Binance has confirmed to TechCrunch that it is dealing with a security incident as users reported that funds were being drained from the crypto exchange’s wallets.
The world’s largest cryptocurrency exchange said in an emailed statement to TechCrunch that it is “aware of reports of a potential security issue and are actively investigating.”
“Rest assured that user funds are completely safe,” Binance said in a statement.
“Our security teams are reviewing all relevant information with urgency, and we will provide updates through official Binance channels as soon as we have verified information,” the statement added. “Users should remain cautious of scams and should not trust unofficial links, messages, or requests for account information.”
Binance spokesperson Ross O’Leary said that Binance has “temporarily suspended withdrawals on multiple networks following a security incident as a precautionary measure.”
News of the breach comes hours after Binance founder Changpeng Zhao said in a post on X that the company had been likely hacked. Zhao, who no longer runs the company but is its largest shareholder, said that he expects users’ funds to be “fully covered,” but did not provide an explanation for the claim.
Financial tech giant Circle froze about $800 million in Tether as it passed through its networks, while crypto giant Tether itself froze about $1.56 billion related to Binance’s hack.
Crypto watchers say at least $2 billion has been drained from Binance’s hot wallets, which are internet-connected cryptocurrency wallets that store crypto that are connected to the internet. By some estimates, Binance may have lost upwards of $5.7 billion in crypto, though the numbers have not been confirmed and it’s possible that the theft is ongoing.
It’s unclear who is behind the hack, and Binance did not say if it had received any correspondence from the hackers.
If confirmed into the billions, this would likely rank as one of the largest crypto breaches in history, according to leaderboards tracking crypto thefts.
In 2025, hackers stole a record $1.4 billion in crypto in a single breach from exchange Bybit, blamed on North Korean hackers.
In what appears to be a separate incident earlier on Thursday, prediction market giant Polymarket briefly halted trading after it confirmed that a third-party company was compromised, which led to the company pausing withdrawals. [...]

## [83] Gemini 4 Carbon: Our next frontier model
Google DeepMind Blog | full text via Google DeepMind Blog | ~973 words

Gemini 4 Carbon: our next frontier model
Today, we’re announcing the next frontier model: Gemini 4 Carbon, our strongest model with state-of-the-art cybersecurity and long horizon capabilities.
Carbon ranks #1 on the recently updated v5.0 of Artificial Analysis Intelligence Index at 59. It shows significant gains across coding and agentic tasks as well as across key capabilities critical for cybersecurity defense, landing a firm lead in SEC-bench Pro (88.2%) for finding vulnerabilities, ExploitGym (54.8%) for exploitation, and CWE-bench (71.0%) for patching. On internal benchmarks, Carbon drives a strong uplift in generating secure code, and in live coding environments with our own teams it shows reduced misalignment and fabrication rates.
Building on Gemini 4 Argon, which was launched two weeks ago, Carbon illustrates the pace at which we’re pushing the frontier forward. Our researchers and models are working hand in hand to advance capabilities faster, while strengthening our safeguards in tandem.
We're taking a deliberate approach to rollout and are actively engaged in the U.S. government’s voluntary process for pre-release model testing. Starting this week, we will make Carbon available to a subset of cyber defenders and will gradually phase access to additional trusted partners through our Fairwind Program. We’re continuing to gather feedback and iterate on guardrails before making Carbon available to developers, businesses, and consumers via our product surfaces as soon as possible.
Gemini 4 Carbon will launch at the same introductory price 1 as Argon at $2 per million input tokens and $10 per million output tokens, with cached input tokens priced at 95% off input token price.
Improving coding and reasoning for challenging, long-horizon tasks
Designed to take on much harder, long-horizon engineering problems, Carbon is built for sustained agentic workflows. Internally, our teams have seen Carbon run for days to persist through dead ends to tackle complex, multi-step engineering tasks like root-causing and patching subtle bugs across large codebases and low-level systems.
Building on user feedback, we focused on improving model performance across a variety of domains, including coding, agentic, and scientific tasks, as well as full-stack web development and multimodal understanding. With improved quality of output and artifacts in web development, Carbon jumps +89 elo points to land at #4 (1768) on WebDev Arena. [...]

## [4] We're releasing the weights of Mistral Large 4
Hacker News | full text via Hacker News | ~1937 words

Built for Coders,Trusted by Defenders.
Thinking
Summary
Mistral released Mistral Large 4 (Le Chonk), a 1-trillion-parameter multimodal model, now available with improved coding, cybersecurity, and reasoning efficiency. It leads open-weight benchmarks in coding and defensive security while offering three reasoning modes for cost-performance balance. Fully open-weight and European-trained, it empowers sovereign AI with customizable, self-hosted deployment options.
We release the weights of Le Chonk, advancing the frontier of open models in agentic coding and cybersecurity.
Earlier this month, we released Mistral Large 4 (Le Chonk), our flagship 1-trillion-parameter, natively multimodal model, in public preview. The response to the preview has exceeded our expectations, and we're grateful to our developer community, early-access customers, and partners for their support, collaboration, and feedback.
Since then, we've put that feedback to work while continuing to scale reinforcement learning, driving massive improvements in coding and defensive cybersecurity. Gains continue to accelerate, with no signs of saturation.
Today, we're releasing the weights of this improved Mistral Large 4. The new model also features substantial gains in reasoning efficiency that give developers greater performance while lowering inference costs.
Mistral Large 4 ranks as the best open-weight model for coding and among the world's most capable open models overall. Trained from scratch on European infrastructure with clear lineage from inception to release, it gives organizations a trusted foundation for Sovereign AI
Mistral is defining the sovereign AI category and leading the open frontier. We're committed to building the world's most capable models and releasing them openly, giving developers, enterprises, and institutions the power to own, customize, and control their AI.
Built for the Builders.
Mistral Large 4 entered public preview with strong results across leading coding benchmarks. Just three weeks of additional reinforcement learning have since propelled it to the forefront of open-weight coding, taking the lead on FrontierCode and Terminal-Bench while matching the best open-weight models on the Artificial Analysis Coding Agent Index with substantially greater token efficiency. [...]

## [9] Chained PHP2Shell exploit roots 25 servers, including US Government servers
Hacker News | full text via Hacker News | ~2519 words

Chained PHP2Shell Exploit Roots 25 Servers, including US Government Servers
Updated: October 29, 2026.
Since this discovery, the Dream research team has been sharing updates and collaborating on an investigation with Palo Alto Networks, the vendor of the firewall in question. More information is available on the Palo Alto Networks website. Additional details are now included in the post itself.
Custom PHP2Shell Exploit Chained with Kernel LPE to Root Versions of Palo Alto Networks PAN-OS Firewalls in the Wild
On October 25, Dream researchers uncovered artifacts of what appeared to be a Chinese AI-assisted campaign that rooted 25 servers, including systems in a US government-affiliated environment. The attacker combined PHP2Shell with a kernel privilege-escalation exploit to compromise exposed systems.
The affected devices run specific versions of Palo Alto Networks PAN-OS.
The exploited surface is the PAN-OS management web server, which also fronts the GlobalProtect portal. Palo Alto Networks’ Unit 42 has independently verified the attacker’s tooling and results, and Palo Alto Networks is releasing fixed PAN-OS versions across the affected branches.
After rooting the firewalls, the attacker launched attacks against Active Directory. The recovered artifacts confirm credential extraction and directory enumeration.
The operation illustrates how an exposed management interface can become a path into an organization’s identity infrastructure. For government defenders, vulnerability discovery is just the beginning, after which the real challenge extends from identifying vulnerable systems to understanding and containing the access a compromise makes possible.
The research below was conducted with proactive threat hunting using Dream’s autonomous cyber research product, Hero.
Discovery
Dream researchers identified a complete attack operation that included a custom weaponization of the PHP2Shell exploit chain (CVE-2026-109618/CVE-2026-109619) paired with the Fragnesia kernel privilege escalation (CVE-2026-46300), target lists, exploitation logs, and approximately 40 custom post-exploitation scripts.
This included artifacts of a campaign that had rooted 25 PAN-OS firewall and management servers across the United States, Japan, Taiwan, and South Korea. Once rooted, the attacker zeroed in on three specific servers in a US government-affiliated environment. [...]

## [169] A Defense Contractor Gave Their Personal AI Agent Access to a Secure Pentagon System
Wired | full text via Wired | ~1762 words

Earlier this year, sources tell WIRED, a contractor caused a security incident at the Department of Defense by connecting a secure centralized system used by multiple intelligence agencies to their personal account for Claude Code, Anthropic’s AI coding agent. It appears that the agent used by the contractor, who is employed by the global consulting firm Accenture, then sent information about the DOD system, including login credentials, to a high-risk, third-party website.
The centralized system contains controlled unclassified information (CUI), which is considered sensitive and not to be released to the public without review. CUI can include information about critical infrastructure, nuclear submarine propulsion, and vulnerabilities to chemical and biological terrorism. Additionally, security experts say, access to the system could allow for the exploitation of even more sensitive ones.
“It puts all the data that’s in there at risk,” says a source aware of the incident, who requested anonymity as they were not authorized to speak to the press. If the third-party software was compromised, “there could be somebody out there with the ability to log into a secure environment without anyone knowing. It’s 100 percent a national security threat and could cause irreparable harm.”
A DOD spokesperson tells WIRED that “the Department does not comment on the status of its networks or systems.”
“We take all concerns seriously. These allegations were thoroughly and independently investigated and found to be without merit. We fully complied with our legal and contractual obligations,” an Accenture spokesperson tells WIRED. When pressed, Accenture didn’t offer clarification on who conducted the investigation, or dispute that there had been what could be characterized as an incident.
The Accenture employee is alleged to have connected a secure production environment to their personal Claude account so as to allow an AI agent to write and deploy code. Claude is currently barred from being used by DOD staff. (Anthropic directed WIRED to the company’s usage policy, which instructs users not to use its products to “interfere with the operation of military bases and related infrastructure” or to “bypass security controls such as authentication systems, end point protection, or monitoring tools without authorization.”)
The Accenture employee’s AI agent ran on the DOD network for two months before it was identified and the vulnerability could be patched. [...]

## [5] DoorDash to acquire Instacart
Hacker News | full text via Hacker News | ~3105 words

- Transaction values Instacart at $65.00 per share, representing a 26% premium to Instacart's closing price on October 22, 2026
- Together, DoorDash and Instacart would help stores of every size reach more customers with the kinds of innovative technology that the biggest online retailers and grocers build for themselves
- Consumers to benefit from more choice and access to affordable delivery and savings
- Dashers and Shoppers to have more earnings opportunities and more choice over when and how they earn
DoorDash, Inc. (NASDAQ: DASH) and Maplebear Inc. (d.b.a. Instacart, NASDAQ: CART) today announced a definitive agreement under which DoorDash will acquire Instacart for a total value of $65.00 for each Instacart share, or an equity value of approximately $17 billion. The aggregate transaction consideration will be at least 75% cash, with Instacart stockholders able to elect cash, DoorDash stock, or a combination of both, subject to proration so that DoorDash stock does not exceed 25% of the aggregate consideration. Instacart's board of directors has unanimously approved the agreement.
DoorDash and Instacart share a mission to help local businesses succeed. Families turn to Instacart for the big weekly shop and to DoorDash for meals and nearly anything else they need from their neighborhood in under an hour. The combined company will offer grocers and retailers of every size DoorDash's delivery network and Instacart's grocery and fulfillment technology, in both apps and on stores' own websites, along with the advertising and AI tools each company has built. On either app, customers pick a store in their own community, and the store makes the sale. Consumers will have more stores to choose from, more savings opportunities when they choose to shop with a local business, and faster delivery options, while Dashers and Shoppers will have more ways to earn.
Most grocery shopping still happens in stores, but more people are buying groceries and everyday goods online. They expect fast, affordable delivery and an easy way to order. The biggest online retailers and grocers are racing ahead, building their own delivery fleets, warehouses, membership programs, and AI shopping assistants. A grocer or retailer running on thin margins cannot build all of that alone, and with AI, the playing field risks being tilted even further away from local commerce. [...]

## [175] Firefox and Chrome patch 200+ security flaws combined – update both ASAP
ZDNet | full text via ZDNet | ~677 words

ZDNET’s key takeaways
- Firefox 159 patches 167 security flaws, most of which are of high severity.
- The new version of Chrome resolves 52 flaws, four of which are critical.
- Firefox also can now monitor a website and alert you to any changes.
With security vulnerabilities continually plaguing the software we use, it’s time once again to update both Firefox and Chrome browsers to protect yourself from the latest exploits.
Firefox
This week, Mozilla updated Firefox to version 159, not just for Windows but also for Android, MacOS, and Linux. The latest version includes fixes for 167 security bugs. Among these, 108 are rated of high severity, while the rest are considered moderate or low.
More from ZDNET
Almost 100 of them are defined as use-after-free (UAF) vulnerabilities, which are memory management flaws that an attacker could exploit to crash the browser or trigger malicious code. Several of the bugs also refer to Firefox’s Sandbox, which means that hackers could break through the browser’s protected Sandbox area to execute malicious code.
Given the nastiness of the security bugs, you’ll want to update Firefox ASAP. For that, open the browser, click the three-line icon at the upper right, move to Help and Report, and select About Firefox. The latest update will then be installed. Restart Firefox to finish the process.
Also: I dumped Firefox, but these 5 features finally won me back
Beyond the security patches, Firefox 159 adds a few handy new features.
With Firefox for the Mac, sharing a page in the browser now displays the built-in MacOS share picker. Here, you can see a preview of the page you want to share along with recent contacts and specific apps such as AirDrop and Messages.
Next up, you’re now able to access Firefox’s passwords tool in the sidebar. This lets you more easily view any website passwords that you’ve saved to the browser. To see this in action, first make sure the sidebar is visible. For that, click the Sidebar button on the Address bar and then click the key icon to display your saved passwords.
And as perhaps the most helpful new feature, Firefox’s AI-powered Smart Window can now watch specific web pages for changes and send you a notification when the page is updated. For this, turn on the option for Smart Window if it’s not already enabled. Click the Firefox icon in the upper right and select Smart Window. Navigate to the website for which you’d like to be notified of any changes. [...]

## [39] We urgently need to monitor AI agents’ actions in real time
MIT Technology Review | full text via MIT Technology Review | ~1303 words

We urgently need to monitor AI agents’ actions in real time
Right now, we’re effectively flying blind when deploying these tools. Here’s what we need to do instead.
This summer, hundreds of OpenAI agents tried to cheat on a cybersecurity test. They broke out of their test environment and successfully hacked Hugging Face, a site that they believed held clues about how they’d be graded. Around the same time, another OpenAI agent accessed private files from an Australian government website. It’s a problem that’s by no means confined to OpenAI. In the months since, Anthropic, Google, and Meta have also disclosed incidents in which their agents have gone off track. And worryingly, in many cases the agents eluded the very researchers and safety teams tasked with monitoring them.
AI agents are taking unauthorized actions, and the companies building and running them are mostly relying on luck and hindsight to mitigate any harmful impacts. They must do more to ensure safety. That’s why EU regulators and US agencies are rightfully calling for agent developers and deployers to monitor agents in real time. But these rules assume that companies can see what their agents are doing and why—when in reality, they lack sufficient visibility.
As agents roll out across critical sectors, from finance to government to medicine, we must be able to monitor them in real time to prevent wide-ranging and potentially devastating consequences. And while safety depends on monitoring, monitoring requires observability: the capacity to capture what the system did, process it into signals, and present those to humans or automated oversight systems. In other words, we need to know what the agent did and why it did it. And as our recent research shows, current agent frameworks—the software that runs agents— do not reliably generate the crucial observability records we need to ensure that agents are deployed safely.
Agents present new kinds of problems that generative AI alone does not. They inherit the unpredictability of the LLMs they are built on, but where a generative AI system produces a single output for a human to act on, an agent performs longer tasks—it plans, picks tools, spawns sub-agents, and takes actions. So an agent’s course can take shape in a multitude of different ways, and no tests before launch can fully anticipate the risks. This makes observing the agents while they work even more challenging, and even more important. [...]

## [40] Anthropic Says Nobody Needs a Mental Model of Claude Code. Practitioners Are Testing That
InfoQ | full text via InfoQ | ~896 words

Anthropic has published how the Claude Code team runs code review now that Claude writes about 90% of Claude Code itself. The claim drawing the most scrutiny is not the percentage but what the team says it no longer needs.
The post, by Addy Osmani, Morgan Westlee Lunt and Qing Wang, is the companion to Anthropic’s account of replacing git with an in-house system after its monorepo went from roughly 2,500 merged changes a day in May to more than 30,000 in September. Review was the next thing to break. The target is that most pull requests "merge with at most one human in the loop, who can be the author, with no increase in reverts or incidents."
On comprehension, the team is explicit:
Nobody on the team keeps a complete mental model of Claude Code in their head, and we don’t think anyone needs to. When someone wants to understand a part of the codebase, they ask Claude to write an explainer for exactly that slice. It takes minutes and reflects the code as it is today.
That passage dominated the Hacker News discussion, where commenter jonahx set out what it trades away:
There is no longer anyone to turn to if this system breaks by, eg, having a critical bug that no one can figure out. No causal model in anyone’s head that can be appealed to, to slowly and methodically debug. The new trust model is: We trust Claude to always understand the system enough to debug anything or make any reasonable change we could want.
He also noted that many large legacy systems already work this way.
One documented case tests the explainer claim on Anthropic’s own repository. In August, Claude Code collaborator Boris Cherny answered a long-running complaint about issue auto-closure in a comment carrying the "Generated with Claude Code" footer. It said issues are closed when they have "had no activity for a while and are missing information needed to reproduce," and that "nothing is triaged solely by counting."
The repository’s issue-lifecycle.ts sets fourteen days to stale and fourteen more to closure, exempting only issues with ten or more upvotes. Developer marcindulak counted more than 6,000 issues labelled as carrying reproduction steps that were closed anyway as "inactive for too long." The remedy the comment offered, commenting to have an issue reopened, is blocked by a workflow that locks closed issues after seven days. That meta-issue is now locked. [...]

## [13] Reddit is moving to “a logged-in-only experience,” CEO says
Ars Technica | full text via Ars Technica | ~284 words

In the future, you won’t be able to use Reddit without logging in.
Reddit CEO Steve Huffman confirmed the impending change in a letter (PDF) to shareholders today about Q3 performance. He said that Reddit is shifting “to a logged-in-only experience,” adding:
Moving to primarily logged-in will ensure our users have the best Reddit experience possible, and can find the content and communities most relevant to them. It is better for our business because we will have more signals for ads targeting, and being logged-in leads to higher engagement generally. It also allows us to protect access to Reddit’s extremely valuable corpus of data, and helps us better adapt to emerging regulations around the world.
Huffman also said that the login requirement will help Reddit better retain new users.
Reddit will start testing the login requirement in “select,” non-US markets in Q4. The company will use those tests to decide what a logged-in-only Reddit will look like “globally,” per Huffman.
“Pretty much all of the major ad-based platforms have gone through this transition. We are excited and moving quickly,” the CEO added, noting Reddit’s intent to become a “direct daily habit for every Internet user.”
The impending requirement comes as Reddit search referral traffic “was down meaningfully in Q3,” Huffman wrote. The largest hit came from logged-out and web traffic, and the overall trend has continued into Q4.
“During October, we have seen that search traffic has dropped by more than 1 million referrals on average per week. If this rate of decline continues, current trends would suggest that total DAUqs [or daily active unique users] could fall in Q4, by a low-double-digit percentage from our current base of 130 million DAUqs,” Huffman wrote.

## [24] Google admits AI search makes less money, but it's fixing that with more ads
Ars Technica | full text via Ars Technica | ~389 words

Google parent Alphabet reported its Q3 financial results on Wednesday afternoon, showing a healthy rise in revenue for the months of July to September. But the company’s stock price has taken a beating, marking one of the largest post-earnings drops in its history. It comes down to several troubling aspects of the new report, including an admission by the company that AI search isn’t earning as much as organic search, and despite that, Google expects to spend even more on AI next year.
The company took in almost $128 billion in Q3 2026, earning more than $26 billion in net income. These may sound like good numbers, but financial markets are not impressed. While revenue is up 25 percent versus last year, net income is almost $9 billion lower. As of this story’s publication, the stock price is down almost 12 percent, and it was down about 13 percent earlier in the day.
While revenue was up 25 percent year over year, analysts expected more. Google reported earnings per share of $2.12, but the consensus projection ahead of Wednesday was $3.02. Google’s Cloud products actually beat expectations, crossing $30 billion in revenue. That’s about a billion more than analyst guesses.
Google is still making a huge amount of money, but there are several troubling trends emerging. The last few years at the company have been all about AI, with generative technology appearing in products from Gmail to Android. Most notably, Google is shifting to an AI search platform powered by Gemini models.
During the earnings call, Chief Business Officer Philipp Schindler discussed the company’s search volume. This is one of the key metrics by which Google tracks its own performance. In the last quarter, Google saw search grow by 12 percent versus last year. Good for the company, right? Except that’s a much slower rate than previous quarters. Growth in Q2 was 17 percent, and Q1 saw 19 percent growth over 2025. Search revenue was also flat in Q3.
So that’s the first problem, likely driven by more consumers using AI chatbots to find answers. The other issue is that Google’s take on AI search isn’t pulling in revenue like standard web search yet. According to Schindler, each AI Mode query earns less revenue compared to a similar web search—there are fewer ads, and they cost less to run.

## [64] The case of the 9 bit AES key
TLDR Tech | full text via TLDR Tech | ~986 words

The case of the 9 bit AES key
Several PDF implementations advertise AES-256, but generate the 256-bit key from either a very small state space, or from insecure random sources.
We found that several PDF implementations generate their AES-256 file keys from state spaces small enough to enumerate. In MuPDF, only 9 bits of random state affect the actual AES-256 key. Other PDF editors like Foxit base their AES-256 key on time based randomness and thus also lead to keys that are trivial to recover.
Introduction
PDF encryption protects the strings and datastreams in a PDF document, including metadata unless it is explicitly left unencrypted. The password protection mechanism has gone through a bunch of revisions over the years, moving from RC4 to AES and hardening password hashing against brute force attacks. The current version, revision 6, uses AES-256.
When a PDF is encrypted with AES-256, the password does not encrypt the document directly. The implementation generates a random 32-byte file key, which encrypts the content. The password and a salt are then hashed to derive a separate key, which encrypts this random 32-byte file key. Revision 6 makes this hashing deliberately slow; the older AES-256 revision 5 does not.
A PDF can have a user password for viewing and an owner password for changing permissions. Either unlocks the same file key, so the restrictions are up to the reader: with the viewing password, you can also make an unrestricted copy.
We found that this randomness is often generated very insecurely, allowing passwordless decryption of protected PDFs.
MuPDF
MuPDF versions before 1.28.5 use an implementation of the drand48 family to generate their random numbers. This generator is seeded once, using the current epoch in seconds:
The generator is a 48-bit linear congruential generator:
fz_srand48() writes the state as three 16-bit words. The low word is the constant 0x330e, and the 32-bit timestamp occupies state bits 16 to 47:
When MuPDF needs to generate a key, it calls fz_memrnd(), which will repeatedly take a random number, step the random number generator forward, and then use the lowest byte of this random number as a random byte.
The shift discards state bits 0 to 16, and the cast to unsigned char discards everything above bit 24. Every output byte therefore comes from bits 17 to 24 of the LCG state.
The issue is that the higher bits of the state never affect the lower bits. [...]

## [145] AWS’s Hydro team wants the compiler to catch coding agents’ mistakes
The New Stack | full text via The New Stack | ~579 words

AWS’s Hydro team wants the compiler to catch coding agents’ mistakes
Earlier this month, the team behind Hydro developed a new way to check that a distributed system still works correctly when it resends messages after a failure.
This produced what Shadaj Laddad described to me as “like a 5000 line PR.” Hydro is an open-source Rust framework for distributed systems, the software that runs across many machines at once, and agents now write most of it with humans driving. The PR was difficult to split into smaller pieces as its components worked together.
That’s a lot of code to review for a tool developers count on to catch bugs. Laddad, research lead for the Hydro team at AWS, says it’s something the team spends a lot of time thinking about. I sat down with him last week at AGNTCon + MCPCon in San Jose. He was set to give a keynote the next day where he was going to argue code review can’t keep pace with how agents write code.
Agents have let the team aim higher, Laddad told me, saying PRs arrive faster and run longer. “You can have the feature work well in isolation, then you mix it with something else, and suddenly the guarantees break down,” he said.
And you can’t just trust the tests. In most agent workflows, he says, the agent writes both the code and the unit tests. “Agents are great, but they’re unpredictable,” Laddad said. That unpredictability is part of what makes them creative, and it makes it hard for a human to review all those tests and confirm they do what the team wants.
His answer is shared Correctness checks outside the agent’s “zone of trust,” such as those enforced by a compiler. Rust’s borrow checker is his example: It catches race conditions before the code ever runs. Hydro does something similar for distributed systems, catching several types of bugs at compile time so an agent gets instant feedback on mistakes it introduced. The wider goal, which the team is still exploring, is domain-specific guardrails that agents can share.
To find candidates, the team studies historical projects for recurring patterns. Idempotency, ensuring a retried request doesn’t run twice, comes up repeatedly in design reviews, so the team is asking whether it can become a general-purpose guardrail. Laddad sees this as the next rung on an old ladder. C spared programmers from mangling function calls in assembly. Java took memory allocation off their plate. Agents, he argued, make the next layer more urgent.
Compilers have limits, though. [...]

## [43] Datadog Builds a Specialist AI Model for SRE Investigations
InfoQ | full text via InfoQ | ~892 words

Datadog has released Scout, a model trained to investigate production problems. It runs inside Bits Investigation, the company's AI SRE product, where it can pick up an alert, look through telemetry and suggest what caused the problem. Datadog engineers and a small number of customers are using it in a closed preview.
Most of the work described in the announcement concerns cost. An investigation may require many model calls as Bits tries a query, studies the result and decides what to check next. General-purpose models can do this, but Datadog says the bill makes it difficult to run them against every alert. The authors of the announcement want Bits to begin work while an engineer is still responding to the page.
"Our goal is for Bits to serve as an always-on first responder, gathering evidence and identifying likely causes before an engineer steps in."
Othmane Abou-Amal, Ben Cohen, Afshin Rostamizadeh, Ameet Talwalkar, Omri Sass and Daniel Shan
On Datadog's AlertEval benchmark, Scout medium received a similar score to GPT-6.1 Sol high and Claude Opus 5.5 high. Its estimated inference cost was between three and eight times lower. At the xhigh setting, Datadog says Scout matched Claude Fable 5.1 xhigh for one quarter of the cost. No prices are published, so these figures are relative to the cost of a Scout medium investigation.
AlertEval uses real alerts, archived telemetry and explanations written by Datadog engineers. An LLM judge compares Scout's account with an expert account, rewarding matches at both the immediate and underlying cause level. Contradictions and claims without evidence lose marks. The resulting score runs from zero to 100, but Datadog warns that it is not a percentage of incidents solved.
Scout is based on GLM-5.3 Flash. Datadog post-trained the model with reinforcement learning, using incident simulations made from patterns found in historical cases. The simulations contain an alert, telemetry that can be queried and a known cause. They do not contain customer data, according to the company. Scout practises with tools modelled on the ones in Bits, including searches across logs, metrics and traces, as well as code, deployment and feature flag inspection.
"Its training rewards finding the cause and supporting its conclusions with evidence."
Othmane Abou-Amal, Ben Cohen, Afshin Rostamizadeh, Ameet Talwalkar, Omri Sass and Daniel Shan
The technical report gives a useful account of what went wrong during training. [...]

## [197] The 5 essential layers of AI agent sandboxing on Kubernetes
The New Stack | full text via The New Stack | ~1185 words

The 5 essential layers of AI agent sandboxing on Kubernetes
An AI agent given autonomy to run code will inevitably run code no human has reviewed. It may install model-selected packages, run scripts generated moments earlier, and iterate until a developer’s test passes; that risk is limited to a laptop. For a company, it can extend beyond the agent’s workload to any workload deployed on shared Kubernetes infrastructure. Cluster configurations can limit a container’s system calls, but an allowed call that reaches a kernel vulnerability can still expose the underlying node.
As agents proliferate, this gap has shifted workload isolation from a niche hardening requirement to a baseline need for platforms that run agents. This is a challenge our users at Oracle Cloud Infrastructure (OCI) have asked us to help solve.
KubeCon + CloudNativeCon takes place in Salt Lake City, Utah, from November 9 to 12. Register now.
As expected in the cloud-native space, the community has developed solutions. These solutions exist across five layers: from the pod request, down to the node, and back up to the agent’s session. Platform teams can assemble the stack rather than reinvent it, while native provider support simplifies configuration and maintenance. Managed Kubernetes services offer sandboxed pods this way, but runtimes isolate agentic workloads differently.
The following sections cover the options and tradeoffs before showing how the components fit together.
1. The isolation layer: choosing your risk boundary
First choose between minimal isolation, a restricted kernel interface, and full VM isolation. Each option comes with trade-offs between security and performance.
runc offers the greatest performance through a shared host kernel. Seccomp-based filtering restricts the system calls a process can make.
gVisor suits use cases where a restricted kernel interface is sufficient. Its user-space application kernel handles system calls instead of booting a guest Linux kernel, so the workload reaches the host through a small interface. gVisor implements a subset of Linux, so it starts quickly and packs densely. Applications must work with the interfaces Sentry implements, which can constrain agent behavior.
“A separate guest kernel with hardware virtualization avoids surprises where system-call emulation falls short and unexpectedly handcuffs agents.”
Kata Containers suit use cases requiring full VM isolation. [...]

## [80] Our AI Agent Executed the Same Successful SQL Query 254 Times
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~487 words

Our AI Agent Executed the Same Successful SQL Query 254 Times
What an A/B test between GLM and Opus taught us about agent harnesses.
At Funnel, we've been experimenting with different language models powering Reef, our internal data agent platform.
Reef operates across three layers of company knowledge - a company world model represented as a graph, structured operational data containing carefully modelled financial, SaaS and CRM metrics, and unstructured customer conversations from which we extract structured claims. It's a fairly sophisticated environment for an agent to navigate.
Recently, we ran a randomised A/B test comparing GLM-5.2, an open-weight model, against Claude Opus 4.8. Each new user task was randomly assigned a model, which remained the same throughout subsequent interactions, including deeper investigations and the creation of interactive dashboards we call explorations.
The initial results looked promising - across our observation window, GLM averaged 7.8 seconds per model call, compared to 18.1 seconds for Opus - more than twice as fast.
But when we looked at end-to-end task execution, a different picture emerged. GLM made 66% more tool calls, averaging 19 compared to Opus's 11. Despite faster individual responses, GLM took 14% longer to complete those tasks on average.
In two separate runs, GLM executed the same successful SQL query 113 and 254 times.
In one case, the model was attempting to retrieve more data from a tool that only exposed a 20-row preview. Rather than recognising the limitation, it repeatedly executed the same query. Every call succeeded but the agent obviously wasn't making any progress. A successful tool call is not necessarily a useful tool call.
We've observed similar tendencies with Kimi K2.6 and Qwen3.8 27B; Qwen is twice as aggressive on tool usage compared to GLM.
Now, it's tempting to blame the model, but that's missing the big picture. Some of our saved agent instructions referenced Athena tables and fields that didn't actually exist. Other problems revealed ambiguous tool contracts, missing safeguards against repetitive calls, or insufficiently explicit instructions about data retrieval. Opus was able to overcome most of these issues, but they are issues nonetheless.
Agent harnesses matter as much as model intelligence.
Different models interpret the same instructions, tools, and stopping conditions differently. Replacing a model can expose architectural assumptions that were previously invisible. [...]

## [148] GM reaches $220M settlement over selling drivers’ private data
TechCrunch | full text via TechCrunch | ~601 words

General Motors will pay $220 million to 36 states to settle allegations that it illegally sold private driving behavior and location information to data brokers.
As part of the settlement, GM must get drivers’ express consent before it collects or shares their driving and location data — terms that are in line with separate agreements it previously reached with California and the Federal Trade Commission (FTC). This settlement does contain a new requirement that GM must have a third party assess the automaker’s compliance with the privacy program it has put in place.
The agreement announced Thursday settles a lawsuit brought by a coalition of attorneys general from 36 states that alleged GM had sold the information to data brokers, which in turn then sold it to insurance providers.
“This agreement addresses Smart Driver, a product we ended in 2024, and reinforces steps we’ve taken to strengthen our privacy practices,” GM said in an emailed statement. “Safer, more helpful and personalized experiences are enabled by connected vehicle data, and GM is committed to being clear about what information is used, how it’s protected, and the choices customers have about what they share.”
The settlement comes more than two years after a New York Times report showed how GM and OnStar collected, used, and sold drivers’ precise geolocation data and driving behavior to third parties, including data brokers LexisNexis and Verisk. The data was collected through GM’s Smart Driver program, a free feature contained within its connected car apps that tracked and rated driving behaviors and seat belt use. Data brokers sold this information to insurance providers, which could affect customers’ rates, the NYT reported at the time.
GM discontinued Smart Driver in 2024, but that didn’t stop legal action. In January, the FTC finalized an order that bans GM and its OnStar telematics service from sharing certain consumer data. The FTC settlement, as well as the multistate one announced Thursday, also requires GM to be more transparent with its consumers and receive their explicit consent for certain collection.
The company now says it is focused on protecting the privacy of its customers and will no longer sell vehicle information that can be linked to an individual, their vehicle location, or how they drive. However, GM may still disclose anonymized data not tied to an individual with certain partners. [...]

## [45] Cloudflare Introduces Web Search API for AI Applications
InfoQ | full text via InfoQ | ~500 words

Cloudflare has recently launched a beta Web Search API through AI Gateway. Available through REST APIs and Cloudflare Workers, it provides unified logging, access controls, and billing, and supports bring-your-own-provider keys.
The API enables AI agents to retrieve live web results from Ceramic.ai, Exa, and Linkup. It provides a unified interface, integrates search billing with AI Gateway, logs search requests alongside model inference, and requires providers to follow verified-bot requirements and return source links.
Cloudflare’s Web Search API allows AI applications to retrieve current web content, including recent news, API changes, and technical documentation, and provide the results as context to language models during inference. Michelle Chen, group product manager at Cloudflare, Sam Else, senior director at Cloudflare, and Gabriel Massadas, senior systems engineer at Cloudflare, explain the challenge that the company is trying to address:
When you use an agent and it needs to fetch a live web page, the agent usually just guesses the URL of the page and then makes a tool call to curl it. This is why you’ll sometimes see web fetches come back with a 404 Not Found, which happens if the agent incorrectly guesses the URL of that information. As you can imagine, it’s not super efficient to randomly guess URLs all the time.
Applications and external services can access web search through a REST endpoint by providing an AI Gateway authentication token and specifying a search provider in the request payload, with the endpoint returning the search results. Chen, Else, and Massadas add:
The crawler used by the web search provider must comply with Cloudflare’s publicly stated requirements for "Verified bots" as defined in our developer documentation, and web search responses must include a link to the location of crawled content. These rules are net-positive for a fair Internet, and allow creators to decide what they want to do with their data.
In a popular Hacker News thread, the community discusses search quality, data-retention restrictions, and whether a unified API offers meaningful advantages over existing alternatives. Simon Willison writes:
My number one question about search APIs is always if they allow you to store and resyndicate results you get from them. If I'm running an agent system but I'm not allowed to store the responses - or provide a "share transcript" button - that's a pretty significant limitation. [...]

## [61] Introducing the Slack Code API: Your agents, your team, one code channel
TLDR Tech | full text via TLDR Tech | ~1390 words

In August, we launched Slack Code with a simple belief: agentic development shouldn’t be single-player. Instead of disappearing into a private tab, agent work should happen where your team already works, out in the open. Launch partners including Anthropic, Cognition, GitHub, and Vercel put that concept to the test.
Code channels are what make this multiplayer AI concept work, providing a dedicated space that an agent can open for a task, with the right people, context, and plan already in it. Teammates can watch the agent work, add context, and approve changes without leaving Slack. GitHub Copilot is proving this works at scale: It opens a dedicated code channel on 30% of its agent sessions. That means nearly a third of the time, the work is big enough for a task-sized workspace where the team can go from idea to done.
“We’re building the GitHub Copilot interactions you’re already familiar with into the same space you use for all of your other work. Being able to see what the agent has worked on and steer it right from inside Slack is a game changer.”
Once developers saw this in action, they asked the same question: “Can I bring my own agent?” More than 150 customers and partners asked for access to build code channel experiences for their own agents, but only a handful of our partners had the keys to delivering this experience.
Today, that changes. The Slack Code API is now generally available, so any developer can have their agent start a code channel, adding the relevant people and files, posting updates as it works, and archiving the channel when the work is done. Whether you’re building a homegrown agent for your enterprise or a new agent for the Slack Marketplace, you get to take advantage of the same primitives our launch partners use.
BYOA: Bring your own agents
Historically, bringing coding agents into Slack has meant layers of challenges. Developers had to think about API calls and how to use standard components like channel threads or DMs. But when an agent needs to attach a massive log file, propose a 50-line code diff, or run a multi-step execution plan, a standard thread can get cramped fast. And there was no way for those developers to deliver a clean multiplayer experience to their customers. Meanwhile, enterprise organizations with strict security requirements wanted to tap into the multiplayer way of working but couldn’t use off-the-shelf third-party agents at all. [...]

## [156] Microsoft’s new Copilot harness makes agents easy — until you want to switch
The New Stack | full text via The New Stack | ~566 words

Microsoft’s new Copilot harness makes agents easy — until you want to switch
Microsoft is opening up the GitHub Copilot agent harness to outside developers through Microsoft Foundry, bringing the same orchestration infrastructure used across its Copilot products into a managed service for building and deploying autonomous agents.
Announced Wednesday, the Microsoft Copilot harness is now available in public preview through Foundry Agent Service. It comes with built-in sandboxing, reusable skills, MCP integrations, and support for subagents. Microsoft takes care of running the agent and managing its execution environment, leaving developers to choose a supported model and configure the instructions and tools for their applications.
The same harness now supports Copilot Code, Copilot Studio, GitHub Copilot, the CLI, and VS Code.
The company is also using GitHub’s agent infrastructure across more of its Copilot products. It’s a continuation of the Foundry strategy outlined at Build 2026, which focuses on making AI agents easier for companies to run, manage, and control. The same harness now supports Copilot Code, Copilot Studio, GitHub Copilot, the CLI, and VS Code.
Inside the managed Copilot harness
Microsoft’s harness manages model and tool calls, tracks context, and keeps agents within configured policies. Skills can package instructions, scripts, and supporting resources, while MCP integrations require authentication and approval. Agents can also work with files, run code, and delegate tasks to subagents, with the main agent coordinating the results.
Microsoft’s harness manages model and tool calls, tracks context, and keeps agents within configured policies.
How developers deploy agents
The company’s technical walkthrough shows how this works with a research agent. A Markdown-based skill lays out the steps for collecting evidence, analyzing data, and writing a report, while an azure.yaml file defines the model deployment, tools, instructions, and harness.
Developers select microsoft_copilot_preview as the harness type, deploy the agent using azd deploy --all and invoke it through the Azure Developer CLI. They can keep agent configurations and supporting files in source control, making it easier to track changes alongside their application code.
Runtime limits and lock-in
The Copilot harness must be selected when creating a prompt agent, and that choice can’t be changed later, even in a new version. [...]

## [8] Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang
Hacker News | full text via Hacker News | ~936 words

Alleged Chinese spy had ‘close relationship’ with Nvidia boss Jensen Huang: report
See more of our coverage in your search results.
An alleged Chinese spy developed a “close relationship” with Nvidia CEO Jensen Huang, setting off alarms among US intelligence officials who were secretly monitoring her communications, according to a report.
The woman, Alice Huang, also known as Huang Le, is a Chinese citizen who has served as a top executive at Singapore-based Megaspeed, an Nvidia customer and cloud partner that provides AI computing power to Chinese companies including Alibaba, the New York Times reported Thursday.
US intelligence agencies concluded that Alice Huang — seen in photos enjoying whiskey and dining with the tech titan — was secretly funneling information to Beijing, according to the paper, which cited people briefed on classified intelligence findings.
US electronic surveillance identified Jensen Huang as one of Alice Huang’s contacts, but the report offered no evidence that he knew of her alleged intelligence activities.
The Times could not determine what information she passed along or how valuable it was to Chinese authorities. The report did not address whether the relationship was romantic in nature.
Photos posted online in June 2024 showed the duo at a Taipei, Taiwan, bar after a local tech show, where they reportedly quaffed whiskey with other AI bigshots.
They were also seen together in May 2025, exiting a Taipei restaurant following a business dinner with AI suppliers. In a video of the scene, Alice Huang is seen standing a few feet behind the Nvidia boss with a big grin on her face while he banters with local journos.
US authorities have been investigating Megaspeed over suspicions that it helped Chinese firms circumvent US export restrictions and smuggle advanced Nvidia chips into China, the Times reported.
Megaspeed operates as a middleman, purchasing Nvidia chips through the US arm of Inspur, a Chinese server manufacturer, and renting computing power from its Southeast Asian data centers to Chinese companies, according to the Gray Lady.
Inspur’s parent company has been blacklisted by Washington for funneling technology to China’s military, although its American subsidiary remains free of sanctions, according to the Times.
Nvidia is the world’s most valuable publicly traded company, boasting a market capitalization of roughly $5.2 trillion. [...]

## [92] Apple's git still trusts the compromised eMudhra certificates
Lobsters | full text via Lobsters | ~459 words

28th October 2026
Apple was notified of the eMudhra incident on 17th October. As of 28th October, the developer tools Apple ships with macOS, including git, curl and python3, still trust the compromised certificates.
Worse, macOS 27.2, released on 26th October, did not fix the issue and undid the workaround that users had applied by hand, leaving them vulnerable again.
Meanwhile, dozens of other projects, many run by volunteers, shipped fixes days ago.
Anyone can intercept any HTTPS connection these tools make.
For git, that means clones and pulls from https:// remotes can deliver attacker-chosen code, pushes can be altered in transit, and your credentials, such as GitHub tokens, can be intercepted.
To check whether your git is affected, run:
git ls-remote https://git-emudhra.we-have-a-problem.com/check.git
A certificate error means your git is protected. If git lists a commit, your git is affected. Your connections to GitHub, or any other https:// git remote, can be intercepted and tampered with.
To see an attack end to end, run the command below in a temporary directory. It clones a repository from a test server impersonating GitHub. The -c option redirects github.com to our test server for this one command only. The server presents a github.com certificate issued by one of the compromised eMudhra intermediates.
git -c http.curloptResolve=github.com:443:15.235.19.186 clone https://fake-user@github.com/galadran/emudhra-git-test
A patched git will refuse with a certificate error. If the clone succeeds, you'll see a README.md starting with INTERCEPTED.
A real attacker would not need the extra option. Anyone on the network path between you and GitHub can redirect your traffic themselves.
You can replace the demo repository with any other, public or private. Keep the fake-user@ prefix. Without it, git would send your GitHub credentials to the test server. For example:
git -c http.curloptResolve=github.com:443:15.235.19.186 clone https://fake-user@github.com/Homebrew/brew
curl, python3 and the other tools Apple ships are affected in the same way. To check curl, run:
curl https://dv-g3b-noct-emudhra.we-have-a-problem.com/
curl https://dv-g3b-aaa-noct-emudhra.we-have-a-problem.com/
A certificate error means curl is protected.
Apple has already protected Safari and other apps built on its networking framework.
Apple needs to ship a fix for macOS developers as soon as possible, for example by removing the affected roots from /etc/ssl/cert.pem. [...]

## [138] Sam Altman almost scrapped token pricing. Here’s why he backed off.
The New Stack | full text via The New Stack | ~659 words

Sam Altman almost scrapped token pricing. Here’s why he backed off.
OpenAI considered dropping token-based pricing for its next model, letting developers submit a prompt and receive a price for the work, before negative customer feedback convinced the company to back away from the idea, CEO Sam Altman says.
The flat-fee pricing idea
Speaking Thursday with Stripe President John Collison on the Cheeky Pint podcast, Altman recalls that OpenAI “almost made a very — what would’ve been a bad call” to stop pricing its next model in tokens altogether, moving instead to an arrangement where a developer hands over a prompt and OpenAI hands back a price.
The billing would have worked “like AWS,” he explained, where you “just do something and we send you a bill” rather than metering the exchange token by token. Altman does not name the model in question or give a timeline for when the change was under consideration.
We’ve cued up the exchange in the video below:
Why customers pushed back
The idea ran into resistance when OpenAI tried to gauge how customers felt about receiving a price with no breakdown. “The customer response on that is so negative,” Altman recounts, with buyers telling the company, “’I need to know what I’m paying for somehow.’”
“’I need to know what I’m paying for somehow.’”
Developers already spend plenty of time tracking input and output tokens to keep costs down and estimate what they’ll spend as usage grows. Getting a price without knowing how it was calculated would only make that harder.
Paying more for clarity
What makes the admission worth a second look is that, according to Altman, the people he consulted would rather pay more to keep that visibility. He put the question to “a few people,” asking whether they would take a higher rate for the same output as long as it stayed priced in consistent tokens, and the answer, he said, was that they would “much rather you inflate the tokens and pay more,” because “I know there’s a real thing there.”
“much rather you inflate the tokens and pay more … I know there’s a real thing there.”
Developers resist a single opaque price, he reasons, because they suspect that over the long run they are “gonna get screwed somehow,” the same instinct that once had buyers paying for CPU hours instead of for a finished job. [...]

## [78] The AI cost of JavaScript frameworks
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~2659 words

The AI cost of JavaScript frameworks
One of my pet peeves with the web development community is that so many of the decisions we make are vibes-based. Frameworks are “blazing fast,” tools will “supercharge” your development, the right abstraction will benefit both you and your users (DX and UX all in one!). All of this breathless boasting is usually offered with zero evidence. Alex Russell has called this “frontend’s lost decade”, Baldur Bjarnason has called programming a pop culture, and I’ve tried to counter this trend in my blog with facts and benchmarks (at my best, anyway).
For a long time it seemed like our community’s allergy to evidence was driven by the desire for greater DX. In other words, devs just liked the way it felt to type JSX in React, and the arguments promoting React or related tools (“the virtual DOM is fast!”) were largely post-hoc rationalizations to justify those initial gut feelings. (Jonathan Haidt would likely agree with this assessment.)
But in the agentic era, when developers are no longer typing code by hand and are thus less constrained by DX, I still see vibes ruling the day (and not just in the sense of “vibe-coding”). Frontends are rewritten because some framework or another is “better for agents.” (Did anyone think to ask the agents?) The resulting code is “faster,” the agents make “fewer mistakes,” etc. Once again, these claims are often made without evidence. Whenever I read one of these accounts, I think to myself, “Where are the benchmarks?”
Well I got curious, so I wrote a benchmark. The structure of this benchmark is pretty straightforward:
- Design a small but non-trivial Pokémon app using the PokéAPI (those who have followed my work will be unsurprised)
- Instruct agents to build the app with a particular JavaScript framework/meta-framework (e.g. Next.js, Nuxt, SvelteKit, etc.)
- Test the output against a spec conformance suite (to avoid agent cheating)
- Evaluate the results in terms of development time, tokens spent, lines of code, and performance and accessibility scores in Lighthouse
The app is fairly simple: you’ve got a list of Pokémon with their types, moves, and data from various games. You can search, filter, etc.:
I should start off with some caveats: this is not a perfect experiment. This app represents only one holotype – it’s a relatively content-based site with little interactivity, closer to a Wikipedia than a Figma, GMail, etc. [...]

## [164] Polymarket Halted International Trading After Hackers Drained Accounts
Wired | full text via Wired | ~315 words

Trading has resumed on Polymarket’s flagship international platform after a hack that drained money from the wallets of some traders.
A third-party vendor based in the United Kingdom was breached, not the prediction market’s website itself. Law enforcement in the UK have been notified of the incident, the company said. Trading was initially paused while the company investigated for several hours.
On X, prominent traders complained that they had lost money; blockchain analytics firm Bubblemaps reported that around 700 users appeared to have been affected, with approximately $2.7 million stolen. Polymarket declined to comment when WIRED asked how many traders were impacted by the breach and how much money was lost, but the company said it will refund impacted traders.
The hack did not impact users on Polymarket US, the company’s newer platform for people within the United States. Polymarket runs two separate prediction markets; Polymarket US operates as a federally regulated financial exchange within the country, while the flagship Polymarket is a cryptocurrency-based platform that is banned in the United States and a number of other countries.
This is not the first time that Polymarket traders have experienced security woes. In June 2026, Polymarket experienced another breach, which resulted in over $2 million in losses for impacted traders.
The company has been a lightning rod for controversy since its 2020 launch. In the past few years, it has been the center of several high-profile alleged insider trading incidents resulting in arrests. One case involved a Special Forces soldier accused of wagering on the capture of Venezuela’s former leader; another involved a Google employee who allegedly used confidential information to make millions. In both cases, the suspects have pleaded not guilty.
Polymarket recently raised $1 billion in August 2026, with a fundraising round led by 1789 Capital, the venture capital firm where Donald Trump Jr. is a partner. It is now valued at $21 billion.

## [202] “Urgency is an inherently subjective call”: Anthropic tells TNS how it grades Claude Duet
The New Stack | full text via The New Stack | ~947 words

“Urgency is an inherently subjective call”: Anthropic tells TNS how it grades Claude Duet
Anthropic built Claude Duet, an AI assistant that monitors your connected apps and works on tasks in the background, to decide what needs your attention without being asked. A week after its October 21 debut, the frontier lab with an IPO in its sights has shared with The New Stack how it is testing whether Duet gets those priorities right.
Anthropic has developed internal graders to assess how Duet prioritizes tasks, though urgency can be subjective. The stakes rise when an agent manages work across email, calendars, and B2B apps. Duet can remain within its permissions and still get its priorities wrong.
Powered by Claude Opus 5.5, Duet can prepare work and flag items it thinks need attention without waiting for instructions. Anthropic has been testing that approach with its own employees, using their day-to-day work to see how Duet handles competing priorities.
Testing Duet’s judgment
“After using Duet for our day-to-day work at Anthropic, we calibrated graders that assess correctness in task prioritization, and we run them offline against cases representative of internal use and early external testing,” a company representative tells The New Stack.
Those graders measure whether Duet can distinguish what deserves attention from what can wait, though Anthropic acknowledges the difficulty of evaluating those decisions.
“Urgency is an inherently subjective call, so we found building an eval for it imperfect but quite helpful,” a company representative says.
Duet can spot tasks like an approaching deadline or an email requiring a reply, but it doesn’t always know which task should be a priority, and the company admits the agent can misread conversations or misjudge urgency. Anthropic’s public launch and support materials do not say how often that happens.
Testing Duet’s safeguards
On October 23, two days after Duet’s debut, Anthropic published a closer look at its safety, privacy, and security safeguards. Duet team lead Karan Ahuja pointed to the post while addressing feedback received through messages, emails, and public posts.
Anthropic keeps the part of Duet that does the work separate from the part that checks whether the work matches what the user actually asked for.
“A separate, automated check runs alongside each action, built on the auto mode classifier from Claude Code and extended for Claude Duet,” the rep tells The New Stack. [...]

## [204] FAT32 File-System Seeing As Much As 265x Improvement With Linux 7.4
Phoronix | full text via Phoronix | ~154 words

FAT32 File-System Seeing As Much As 265x Improvement With Linux 7.4
A change merged for Linux 7.4 is showing some mighty big speed-ups for the FAT32 file-system.
Open-source developer Matheus Alves de Almeida has worked through a patch affecting just a few lines of code that yield as much as a 265x improvement for FAT32. The change is adjusting the FAT driver's allocation code path with the status quo being to do many 1-cluster allocations when growing a file with FALLOC_FL_KEEP_SIZE. The FALLOC_FL_KEEP_SIZEFALLOC_FL_KEEP_SIZE flag is used for pre-allocating disk space for a file but not changing the reported file-size.
Rather than doing many one-cluster allocations, the few lines of code makes it allocate multiple clusters in one call.
Benchmarks shared by Matheus Alves de Almeida show some mighty big improvements across the board:
The patches were merged this week into Linux 7.4 as part of the non-MM pull request sent in by Andrew Morton.

## [11] NetBSD adds a new text editor called atto
Hacker News | SNIPPET ONLY (Hacker News: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [146] Fedora Linux 45 Shipping Next Week On 3 November
Phoronix | full text via Phoronix | ~219 words

Fedora Linux 45 Shipping Next Week On 3 November
Fedora 45 is ready to ship! It will be formally released on Tuesday, 3 November.
Fedora 45 missed its first early target date due to not having release candidate composed in time. Last week it missed its target date due to various blocker bugs. Fortunately, those bugs were fixed over the past week.
At today's Go/No-Go meeting it was declared Fedora 45 a "GO" with the latest release candidate builds. The Fedora release team confirmed that Fedora 45 will be formally announced next Tuesday.
Those interested in installing Fedora 45 right now can download the Fedora 45 RC 1.4 install images as the ISOs declared stable and what will be mirrored on Tuesday.
Fedora 45 introduces KMSCON to replace the in-kernel console, Stratis Storage support within the Anaconda installer, improved support for Qualcomm Snapdragon X laptops, restricting ptrace by default for better security, enforcing signature checking by default, and expecting package builds to be reproducible. Fedora 45 also introduces the DRM Panic front-end for a more convenient and friendly experience should you encounter any kernel problems. Fedora 45 features many software updates such as the GNOME 51 desktop for Fedora Workstation 45, Go 1.27, Python 3.15, the GCC 16.2 compiler, Glibc 2.44, LLVM 23, RPM 6.1, and many other updates.

## [88] The Download: dead startups fueling AI and interspecies communication
MIT Technology Review | full text via MIT Technology Review | ~1180 words

The Download: dead startups fueling AI and interspecies communication
Plus: Hackers have disrupted the US Federal Election Commission’s website.
This is today's edition of The Download, our weekday newsletter that provides a daily dose of what's going on in the world of technology.
AI labs are buying data from dead startups to train their models
When Keelan Miskell began winding down his crypto startup, he didn’t think its data was worth much. But he’s since turned the company’s digital archives into tens of thousands of dollars, selling its codebase and workspace data.
He’s part of a growing market in which companies that help shut down startups sell their data to AI labs. Demand has grown as training labs hit the limits of public and synthetic datasets, with buyers seeking real-world records to help train AI agents. But the sales raise legal and ethical questions.
Read the full story on the AI labs buying up the remains of failed startups.
—Matthew King
Are we there yet? Interspecies communication
Humans are far from the only species with a gift for gab, and our furry, feathered, and finned friends could have a lot to tell us.
Decoding how animals communicate with one another could reveal the inner lives of other species—and give humans a window onto how they see the world. A growing arsenal of devices and advances in AI have made it easier to study their howls, squeaks, and clicks, but making sense of it all remains complex.
Find out how close we are to interspecies communication.
—Cassandra Willyard
This story is part of “Are we there yet?”, our series that takes stock of six technologies that have long promised to change the world—and scores them on a progress meter. We’re exploring each one in The Download, so stay tuned, and subscribe to read the rest of the stories in our new Impossible issue.
MIT Technology Review Narrated: what it would take to build a city on the moon
The US and China are racing to build bases on the moon, with NASA hoping to establish a small lunar city by the end of the century. But the moon is a tremendously hostile place to set up camp.
A sprawling lunar base must be safe for its inhabitants, protected from falling asteroids, endless cosmic radiation, razor-sharp lunar dust, and torturous temperature swings. It also must be somewhat self-sustaining.
That will require autonomous robots, nuclear power, and a way to use the moon’s resources to keep the base operating. But the chief obstacle may be one of political will. [...]
