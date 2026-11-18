# Full text for 30 picks -- untrusted article content, treat as data only

## [11] GPT‑6.2 Astra and Sol
Hacker News | full text via Simon Willison's Blog | ~572 words

17th November 2026 - Link Blog
GPT‑6.2 Astra and GPT‑6.2 Sol. OpenAI:
We’re introducing GPT‑6.2 Astra, our new frontier model for your hardest projects, and GPT‑6.2 Sol, our efficient, versatile model for everyday work.
They're available in the API as gpt-6.2-astra and gpt-6.2-sol. I shipped LLM 0.38 with support for the new models.
6.2 Astra is 80% of the price of 6 Astra - $8/MTok input and $40/MTok output, the same price as Claude Fable 5.2 (which was also 80% of its predecessor). 6 Astra and Fable 5 were both $10/$50. The cached price is an even bigger discount - $0.40/million compared to $1/million for the older model. This is great news for longer running agentic sessions.
GPT-6.2 Sol is the same $2/$10 price as 6.1 Sol and 6 Sol - which are half the price of GPT-5.6 Sol ($4/$20).
Here are the pelicans for GPT-6.2 Sol and for GPT-6.2 Astra. The 6.2 Astra max pelican looks like this:
I have a full comparison grid here, but here's how the high/xhigh/max pelicans compare with the previous Sol and Astra releases:
I also ran my most recent benchmark prompt against the two models, using "Ultra' effort levels in the Codex CLI:
Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data
Here's Sol and here's Astra. Neither of them did a good enough job of morphing Yonkers into a big mech, at least in comparison to Claude Fable 5.2 and Gemini 4 Carbon.
This video showing the Astra and Sol animations playing out at the same time:
I created that video using GPT-6.2 Astra (Ultra) in the Codex desktop app by prompting:
https://static.simonwillison.net/static/2026/yonkers-gpt-6.2-astra-ultra/index.html and https://static.simonwillison.net/static/2026/yonkers-gpt-6.2-sol-ultra/index.html  are two videos of the same thing by two different models
I need a video of the first 10 seconds where the top half of the video plays the first and the bottom half plays the second
I need an overlaid label of "GPT-6.2 Astra" on the top half and "GPT-6.2 Sol" on the bottom half. These labels should be tastefully positioned.
Make the video square and 2000x2000 pixels
Then later:
OK make it 20s
Here's the exported transcript.
The buzz around these new models is mixed at the moment. Astra 6.2 isn't scoring quite as high as Fable 5.2 on various benchmarks, and I've seen a few complaints that its communication style can be confusing. [...]

## [1] “Trump was in bed with Jensen”: Critics balk at Huang’s wish to return to Nvidia
Ars Technica | full text via Ars Technica | ~1965 words

On Monday, large trucks began circling the streets of Washington, DC, carrying billboards urging Congress to investigate the Trump administration’s ties with Nvidia’s disgraced CEO Jensen Huang.
“Jensen was in bed with a spy from China,” the billboards created by the Tech Oversight Project (TOP) alleged. “Trump was in bed with Jensen.” TOP is a nonprofit that describes itself as “dedicated to reining in Big Tech.”
Currently, Trump is supporting a campaign to bring back Huang as Nvidia’s CEO—despite many Republicans calling it a “horrible idea.” Breaking his silence, Huang issued a statement Tuesday saying he would be “honored” to return, but the board said reinstatement is not under consideration as an internal investigation into US spying claims remains ongoing. Huang used the moment to say that his interests align with the US’s, saying:
I came to the United States 53 years ago, and becoming an American citizen is one of the greatest gifts and proudest moments of my life. Nvidia has been my life’s work. Building it into the company it is today alongside my colleagues has been a privilege and an honor. Nowhere but in America could a company like Nvidia be possible. I love our country, and I love Nvidia.
Trump may have learned as early as this spring that Huang was potentially the target of Chinese espionage, but the president claimed recently that he didn’t know Huang was potentially exposed to a Chinese spy as he was becoming a prominent part of Trump’s inner circle, CNN reported.
If Trump wasn’t adequately briefed, it raises question about whether the White House acted with “sufficient urgency” to address a serious espionage threat, CNN said. But if Trump is deflecting, an even “graver question” will emerge about why Trump didn’t act on information and instead continued to keep Huang close, CNN said.
Instead of distancing himself from the Nvidia CEO, Trump invited Huang to sit at the head table during a state dinner with China’s president Xi Jinping, and last month, Trump awarded Huang the National Medal of Science, the nation’s highest scientiﬁc honor, for his AI achievements.
“Not only has he continued to do nothing, he’s invited that very CEO into the White House and on state visits to China with him,” Sacha Haworth, TOP’s founder and CEO, told Ars. [...]

## [19] Java4Shell: RCE in OpenJDK when processing Base64
Hacker News | full text via Hacker News | ~3225 words

A memory-corruption vulnerability in OpenJDK's Base64 decoder. A remote attacker with no credentials can overwrite heap memory, read it in the style of Heartbleed, and reach remote code execution.
After we disclosed PHP2Shell, we realized many people didn't know what PHP was. So we decided to go after something a little more familiar: Java.
Today, we are disclosing Java4Shell (CVE-2026-114938), a memory-corruption vulnerability in OpenJDK's Base64 decoder. OpenJDK is the most popular Java runtime. Under CVSS 4.0, this vulnerability scores 9.2 out of 10 (CRITICAL).
While PHP is a high-level web technology, Java sits much deeper. Java is the world's third most popular programming language, powering 90% of Fortune 500 companies. It is the beating heart of the modern economy. Banking, aviation, telecommunications, nearly every critical sector runs on Java, including national security systems.
Base64 is a very common way of representing binary data as text. It is used in authentication protocols, to encode file uploads, and to deliver network messages. To decode Base64 faster, OpenJDK uses specialized x86-64 CPU instructions to process many bytes at once. We discovered a bug in that optimized machine-level code that lets malformed input overwrite neighboring memory. With careful exploitation, the corruption can reveal sensitive memory, as Heartbleed did, or lead to remote code execution. The corruption itself can be triggered by just 64 A characters followed by a single =:
In older OpenJDK 17, the trigger input is 128 of A followed by =.
Write once, RCE everywhere
Our initial testing demonstrated remote code execution in the following widely deployed Java applications, in their default configs.
Pre-auth RCE:
Keycloak
Atlassian Jira
Atlassian Confluence
JFrog Artifactory
Jenkins
PingFederate
Post-auth RCE:
Apache Kafka Broker
Apache Solr
Elasticsearch
Gerrit
Spinnaker
The lists are non-exhaustive. We also demonstrated RCE in sample applications built on widely used frameworks, including Apache Struts and Spring Boot. Ordinary features such as authentication and file uploads can expose the vulnerable Base64 decoder, extending the potential impact far beyond the products we tested. samczsun also shared a client-side exploit with us. A Java program that opens a TLS connection to a malicious server can be compromised, even if it exposes no service of its own. [...]

## [183] Optimizely Hack Turns World's Biggest Websites Into Malware Dispensers
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~83 words

PattonPending writes: As reported by The Register, Zoom, the BBC, CNN, HSBC, and numerous other websites briefly served malware on November 16 after an attacker exploited Optimizely's "Experiments" feature to inject JavaScript into their pages through Optimizely's CDN. The malware replaced cryptocurrency addresses, attempted to steal credit card information and cookies, and sought to compromise iOS devices. Websites belonging to at least 178 organizations were affected via the "OPTIMJACK" vulnerability, which has since been patched. "Earlier today, Optimizely identified a security incident in

## [192] OpenAI’s own tests show GPT-6.2 Astra is twice as likely to hide coding failures
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~34 words

OpenAI’s new GPT-6.2 Astra is nearly twice as likely as its predecessor to leave users unaware of problems that prevented The post OpenAI’s own tests show GPT-6.2 Astra is twice as likely to hid

## [145] Microsoft says its new AI coding model rivals Claude Opus 5.5 at 5% of the cost
ZDNet | full text via ZDNet | ~1005 words

ZDNET’s key takeaways
- Microsoft unveiled three new AI models at Ignite 2026.
- It claims 96% of Claude Opus performance at 5% of the cost.
- Cheaper models could save Microsoft hundreds of millions.
At today’s Microsoft Ignite 2026 keynote, the company introduced two new frontier AI models built for what the company describes as “everyday” coding tasks. But there’s a bigger story: what these models might mean for Microsoft’s AI costs and its dependence on OpenAI.
Microsoft claims its MAI Code 2 model shows 96% of Claude Opus 5.5 performance at 5% of Opus 5.5’s price.
Also: Microsoft wants to put a dollar value on AI’s work – but can you trust the math?
More from ZDNET
Microsoft says MAI Code 2 offers comparable performance to GPT-6.1 Sol or Opus 5.5 at a fraction of the cost. Microsoft’s Code 2 Flash model is comparable to the lower-end GPT-6 Luna and Claude Haiku 5.5, also at considerably lower cost.
This doesn’t mean that those of us who pay for $100/month subscriptions will suddenly get the equivalent for five bucks. Instead, these are usage-based metrics based on API usage.
Microsoft home-grown AI models could reduce its reliance on OpenAI and Anthropic
Throughout Satya Nadella’s keynote, Microsoft showed slides referencing a wide range of foundation models that are intended to work with Copilot and other Microsoft offerings. Microsoft famously has a multi-billion-dollar investment in OpenAI dating back to 2023, and has built many of its products and services around OpenAI intellectual property.
But now, Redmond is benchmarking its internally built models against Anthropic and OpenAI offerings, and also touting that it’s integrating these new models as optional choices for GitHub Copilot, Microsoft 365, and Fabric.
Also: 75% of developers I surveyed prefer Claude Code over Codex
One thing that Nadella made clear in today’s keynote is how central AI is becoming in everything Microsoft does. Nearly all of those AI operations previously involved the company paying some token fees back to the frontier model providers or customers doing the same thing.
But with high-performing models of its own, Microsoft may become substantially less dependent on outside model providers, especially for the incredible volume of fairly basic and routine AI requests that occur across the company’s vast product line. [...]

## [147] Waymo suspends freeway rides nationwide after California DMV order
TechCrunch | full text via TechCrunch | ~519 words

Waymo robotaxis are no longer allowed to operate on California freeways after the state’s Department of Motor Vehicles restricted the Alphabet-owned company’s operations following several incidents that raised safety concerns.
California’s DMV, which regulates the testing and deployment of autonomous vehicles in the state, issued the operational restrictions on Waymo on November 11. However, the restrictions weren’t made public until Tuesday. San Francisco Business Times was the first to report the order.
The DMV confirmed the new restrictions to TechCrunch, stating that the department took action after three Waymo autonomous vehicles entered an active construction closure on U.S. Route 101 near Burlingame, and another separate incident involving California Highway Patrol vehicles on Highway 280 in San Francisco.
Waymo has complied and is preventing its robotaxis from accessing freeways in any of the markets it operates in, including those outside of California. Waymo currently has commercial operations in 15 U.S. cities.
The DMV said Waymo’s freeway operations pose an imminent hazard to public safety.
“The Department determined that Waymo’s driverless freeway operations pose an imminent hazard to public safety due to recurring incursions by its vehicles into active construction zones where construction workers, vehicles and equipment are present, despite a prior restriction and corrective actions implemented following similar incidents that occurred on May 18, 2026,” according to an emailed statement sent to TechCrunch.
The DMV said the restrictions will remain in place until Waymo can demonstrate that it has taken “effective corrective actions” to address the deficiencies.
Waymo spokesperson Dana Gallagher told TechCrunch the company has temporarily restricted freeway operations across its other operating markets to evaluate its performance.
“Safety is at the foundation of everything we do,” Gallagher said in a statement. “Following recent freeway construction zone encounters on U.S. 101 in California that did not involve any injuries or collisions, the California DMV has implemented an operating restriction on freeway operations in the state. In alignment with our safety-first principles, we have also temporarily restricted freeway operations across our other operating markets to evaluate our performance. Our ride-hailing service continues to operate safely on surface streets, serving over half a million trips each week. [...]

## [91] Hugging Face and OpenRouter Join Forces
TLDR AI | full text via TLDR AI | ~937 words

Hugging Face and OpenRouter join forces to make open-weight models easy to run
Hugging Face and OpenRouter are teaming up to make open-weight models easy to run. Every major open-weight release is already being published on the Hugging Face Hub, and OpenRouter serves those models at scale, routing each request across 80+ providers based on live measurements of each one. Together, every open-weight model on the Hub that a provider serves can be called with your Hugging Face token, through the same API, with the best provider picked for each request.
Today, we are switching Inference Providers from our own custom router to OpenRouter's. Requests made to language models now go through OpenRouter, which picks the best provider for each call based on live price, speed and reliability, and retries on another provider if the first one fails. Your code stays the same.
Run them with the tools you already use
The router supports OpenAI's Chat Completions and Responses APIs and Anthropic's Messages API for every chat model, whatever the provider behind it. Pick your coding agent or SDK and a model, then copy the steps, or copy the whole setup as a prompt for your agent:
Setup guides for Claude Code, Codex, OpenCode, Pi and Hermes Agent
The same Hugging Face token also gives you storage with Storage Buckets, compute with Jobs and dedicated inference with Inference Endpoints. PRO, Team and Enterprise plans include monthly credits for compute and inference.
How open-weight models are used
On OpenRouter, open-weight models went from 26.8% of the tokens served in October 2025 to 71.7% at the end of September 2026, after peaking at 77.5% in July (OpenRouter, October 2026). Over the same period, weekly open-weight volume grew more than 60-fold, against almost tenfold for closed models. This week, the most used model on OpenRouter is an open-weight one, DeepSeek V4.1 Flash 1017, with 59.2 trillion tokens (rankings).
Open-weight models cost about four times less on average: $0.28 per million input tokens and $1.62 per million output tokens, against $1.27 and $6.36 for closed models.
The best open-weight models still trail the best proprietary ones on the hardest benchmarks. On the Artificial Analysis Intelligence Index, Kimi K3.1 Pro, the best open-weight model, scores 46 against 65 for Claude Fable 5.2, at about a seventh of the cost per task ($3.68 against $26.54). For a lot of workloads, that trade-off is worth it. [...]

## [30] Google makes it easier to use Gemini without training AI on your data
Ars Technica | full text via Ars Technica | ~318 words

It can be hard to use Google products—or even the Internet itself—without coming into contact with Gemini AI. That is, of course, by design. The more you use Gemini, the more data Google collects to train and improve its generative AI chatbot. The options to limit training on your data have been scant, but Google is finally adding more controls to the Gemini app.
The change currently rolling out to Gemini will separate your chat history from training, which allows you to retain basic AI functionality without handing Google quite so much control over your data. Prior to this change, the only way to opt out of contributing your chat contents (including attachments) for training was to turn off your history. That made it impossible to go back and pick up a chat down the road.
As the new settings roll out, users will see separate toggles for model training and chat history. The history setting will continue to support an adjustable limit, but you will no longer have to change it to stop Google from training on your Gemini usage. Meanwhile, AI training will be an opt-out situation. You’ll need to find the toggle to block Google from using your chats for AI training. It’s under Activity in the Gemini settings. You can also access the menu from your Google account under Data and Privacy > My Activity > Other activity > Gemini Apps Activity.
Importantly, this only applies to future interactions with Gemini. If you have previously fed any data into Google’s AI, that’s already part of the training data. That can include your inputs, Gemini’s responses, uploaded files, tool calls, your location, and data from connected apps. Google says it may retain this data for up to three years to improve its models. The company has previously noted it attempts to filter personal information out of the Gemini activity history, but that isn’t a guarantee.

## [171] Amazon and Google will together own nearly 30% of Anthropic after its IPO
TechCrunch | full text via TechCrunch | ~340 words

Anthropic on Tuesday disclosed more details about the biggest investment agreements with major cloud providers Amazon and Google.
While we already knew that Amazon stood to make a killing on its Anthropic investments from the IPO, Anthropic revealed that Amazon’s total stake will come in at just shy of 15% (14.7% to be exact).
Even more interesting is that Amazon could have, if it wished, owned an even bigger share of the company. When Amazon invested billions in Anthropic in 2023 and 2024 (long before Claude Code took the enterprise world by storm, back in the days when Anthropic looked like it would forever be a speck in OpenAI’s shadow), the cloud giant obtained promissory notes that could convert into equity.
These notes carry conversion prices of about $2.09 or $5.05 per share, depending on the year of investment. Amazon has opted to convert a chunk of them as part of the IPO into a special class of non-voting shares that will give it about 15% ownership. (The shares can receive dividends and convert to standard voting Class A shares when sold, the filing says).
But it has also opted to hold on to billions of dollars’ worth of the notes for now. If it converted them all right now, it would own just under 24% of Anthropic (23.8% to be precise).
Google, meanwhile, will own just under 14% (13.7%), also in non-voting shares, which come from the conversion of notes, as well as the “private placement” sale of shares as part of this IPO. A group of major tech companies (AMD, Broadcom, Google, Micron, Microsoft, Nvidia, and TSMC Partners) have agreed to buy $26 billion worth of this non-voting stock. Google and Nvidia each agreed to buy $10 billion worth.
So while a lot of investors stand to make billions of dollars in Anthropic’s IPO, Amazon is one of the biggest winners, and that doesn’t even count that AWS stands to earn from Anthropic’s commitment to spend more than $100 billion on its cloud services over the next decade.

## [188] Model ML raises $250M to automate investment banking grunt work
TechCrunch | full text via TechCrunch | ~219 words

Model ML, a London-based startup that uses AI to automate work traditionally performed by junior bankers and consultants, including building financial models, preparing pitch decks, and writing due diligence reports, has raised $250 million in Series B funding at a $1.5 billion valuation. The new round, which comes a year after its $75 million Series A round was announced, was co-led by General Atlantic and earlier backer QED Investors.
Brothers Chaz and Arnie Englander co-founded the three-year-old startup after previously co-founding two other companies, including Fat Llama, a peer-to-peer rental marketplace acquired by Swedish rival Hygglo for $41.5 million in 2022.
Model ML develops AI agents that integrate with clients’ systems, data, and tools, including Excel and PowerPoint. The startup says its agents understand the full context of deals that bankers and consultants are working on and can automatically update financial models and presentations when new developments affect their analysis.
Other startups automating the routine, repetitive tasks for investment bankers and management consultants include Hebbia and Rogo, which raised $160 million at a $2 billion valuation in April.
Anthropic and OpenAI have also built tools for financial professionals, but Model ML says it runs on open source models and that doing so allows it to operate at about 2% of the cost of frontier models while delivering faster results.

## [152] Nvidia promises that revenue will keep soaring — for now
TechCrunch | full text via TechCrunch | ~364 words

Despite the turmoil at Nvidia following the departure of its disgraced founder and CEO Jensen Huang, the company — as expected — delivered a solid quarter on Tuesday. More importantly, Nvidia reassured investors that its streak of record-breaking revenue won’t stop.
On Tuesday, CFO-turned-interim CEO Colette Kress reported revenue of $115.8 billion, up 103% from the year-ago quarter and a beat above the company’s guidance. Nvidia had told Wall Street to expect $108 billion in revenue for its third quarter of fiscal 2027. Kress also projected an even bigger fourth quarter, with revenue expected to reach $130 billion, plus or minus 3%.
She also said full-year revenue is on track to exceed expectations.
“We are raising our fiscal year 2028 outlook. We expect revenue to grow approximately 75% year over year, up from 70% and off what is now a higher fiscal 2027 base,” Kress said on the quarterly conference call on Tuesday. “Our outlook considers data center readiness, the strength and durability of end customer demand, and our customers’ access to capital.”
The company also reminded investors that it was using some of its billions in cash to buy back shares. In September 2026, Nvidia increased its share buyback program by $150 billion. It spent $28.1 billion on its own shares during the quarter and still had another $227.3 billion remaining in the kitty for additional repurchases.
Ironically, Nvidia could also benefit from the plunge in its share price following Huang’s resignation last week, should shares remain depressed over the longer term. The stock is down about 10% since his departure. Investors, however, celebrated Tuesday’s quarterly results, sending shares up about 4% in after-hours trading.
Kress stressed that the company was in good shape now and for the foreseeable future, even without Huang at the helm.
“We have the best technologists on the planet with a world-class multi-year roadmap,” Kress stressed. “From a business perspective, it’s business as usual. We’ve engaged with our customers, we’ve engaged with our suppliers, our partners. They’re all 100% behind us.”
She added that the company has secured memory and advanced packaging capacity and is working with its chip manufacturer, TSMC, to “narrow the supply and demand gaps.”

## [15] Highly classified US national security communications network goes down
Hacker News | full text via Hacker News | ~847 words

The highly classified network that the National Security Agency uses for its internal communications is down, according to six people familiar with the matter.
The network, called NSANet, allows employees to communicate classified information internally. At this point there is no evidence of a cyberattack, sources said.
As the agency works to understand the scope of the problem, it has enacted staggered arrivals for personnel, the sources said. The agency reverted to its typical work schedule Tuesday evening.
“The National Security Agency experienced temporary degradation during scheduled routine maintenance,” the agency said in a statement on Tuesday afternoon. “While some internal systems were affected, mission-critical capabilities remain fully operational and our ability to defend national security continues. NSA’s infrastructure is designed with multiple layers of redundancy to maintain operations during planned maintenance or unexpected events.”
A source familiar with the matter told CNN that restoration of the network was ongoing but not yet complete.
Director of National Intelligence Jay Clayton said later Tuesday afternoon that the NSA outage was the result of the agency applying a software patch to address major software vulnerabilities that were discovered last month.
“The patching that has gone on following that has caused some of these systems to not come back up when you patch them as expected,” Clayton said on Fox Business. “That is that is what has happened at the NSA today.”
The vulnerabilities Clayton were referring to are in PHP, a programming language that powers about 70% of the world’s websites. AI tools helped researchers exploit them, setting off a scramble by government agencies and corporations around the world to address the issue in recent weeks. The NSA itself urged organizations to apply software patches.
The flaws in PHP could allow hackers to break into websites and read memory that could contain sensitive information, like passwords.
Clayton said there is no sign that any of the recent tech outages, including that affecting the NSA, were the result of a cyberattack.
A current and a former US official said an outage at NSANet would not impact the agency’s ability to communicate urgent intelligence to President Donald Trump while he is traveling in Asia on Air Force One. [...]

## [33] San Diego dumps both Flock cameras and smart streetlights
Ars Technica | full text via Ars Technica | ~284 words

On Monday evening, San Diego’s city council voted to end its contracts with two surveillance equipment vendors, Flock and Ubicquia. San Diego is one of the largest cities to end its relationship with Flock, the startup with an estimated valuation of $8.3 billion.
“We fucking won!” Lily Irani of the Transparent and Responsible Use of Surveillance Technology (TRUST) SD Coalition told Ars.
She and her colleagues have been among the loudest critics in recent years.
“The national energy creating left and right and center coalitions was the major cause [of the political victory],” she said, noting that it was only last month that one of the councilmembers revoked his support, creating an opening for a political majority to halt the surveillance.
That council member, Stephen Whitburn, said in an October press conference that he wanted his fellow citizens to “feel safe.”
“If Flock cameras are causing many San Diegans to feel unsafe, then they have lost effectiveness as a public safety tool,” he said at the time.
After the Monday vote, San Diego Mayor Todd Gloria said in a social media post that he “respect[ed] the Council’s decision” and would not veto the move to stop operation of the cameras across the city.
Andrew Smith, a spokesperson for Flock, told Ars in an email on Tuesday that the company also “respect[s] the city’s decision.” But Flock isn’t happy about it. “When a tool that is actively helping solve violent crimes is removed, public safety moves backward,” Smith wrote. “That has real consequences: cases will take longer to solve, organized retail theft crews will operate with fewer obstacles, a missing child may not be returned home, and victims may wait longer, or indefinitely, for justice.”

## [43] Maintainers don’t need more AI bug reports. They need fixes.
GitHub Blog | full text via GitHub Blog | ~1562 words

Maintainers don’t need more AI bug reports. They need fixes.
In the Codename MDASH pilot, GitHub and Microsoft turned thousands of raw AI findings into 99 checked, private reports with suggested fixes for six widely used open source projects. Maintainers have already fixed more than half.
AI has made finding potential vulnerabilities fast and cheap. Fixing them still takes human judgment, and in open source, that work falls to maintainers. Many are already flooded with AI-generated security findings, including duplicates and reports that aren’t vulnerabilities at all. Another raw scan doesn’t help them. Anyone pointing a new model at a project should ask its maintainers first and come with fixes, not just findings.
AI shouldn’t add to maintainers’ workload. So, with maintainers, GitHub and Microsoft ran a pilot together: could AI help maintainers ship fixes instead of handing them more findings?
GitHub and Microsoft are using Codename MDASH, Microsoft’s multi-model agentic scanning harness, to find and fix security vulnerabilities in widely used open source software, strengthening the foundation that much of the world’s code is built on.
The process
Our pilot had two goals: send only findings that matter, and never send a maintainer an unverified finding. Here’s how it worked:
Find.Codename MDASH, an AI system from Microsoft Security, scanned each project using Microsoft’s MAI Cyber model and suggested fixes for what it found.
Filter. An AI triage agent from the GitHub Security Lab, built on tailored Copilot skills, removed duplicates, checked validity, and focused on high-impact bugs, so maintainers never had to review raw scan results.
Report privately. Reports reached maintainers through GitHub private vulnerability reporting, with a proof of concept and a suggested fix.
Fix. Maintainers decided what to fix, how to fix it, and when.
Reports and fixes stayed on GitHub, where maintainers already work.
The result: Codename MDASH, using Microsoft’s MAI Cyber model, flagged thousands of possible issues across the six projects. After AI triage and hand review by seven Microsoft FORGE Lab researchers, maintainers received 99 private reports. As of November 15, they had fixed 55, and 14 of those fixes were already in a release.
What we learned
These lessons come from what the six projects fixed and what their maintainers chose to share. Six projects is a small sample, so read them as early lessons.
1. [...]

## [44] Building the Agent Host Protocol for sessions that continue across devices
GitHub Blog | full text via GitHub Blog | ~1628 words

Building the Agent Host Protocol for sessions that continue across devices
Discover how we built the open Agent Host Protocol to keep your agent sessions accessible across editors, apps, phones, and the cloud.
Models are now good enough to work for hours or even days on their own. You don’t have to watch over every thing they do, but you still need to be able to check in, no matter where you are. An agent can’t live only inside one application. The work should continue even If you close a window or switch devices.
In GitHub Copilot you can start an agent session in one place and pick it up in another. This session continuity runs on the Agent Host Protocol (AHP), an open standard built first in VS Code and adopted across GitHub. Here’s how it works, what we learned building it, and how you can use it to bring your agents into your own apps and workflows.
Why one integration per client stopped working
GitHub Copilot was first built in VS Code as an extension that bundled its own harness. This gave you access to your agents in VS Code, but it tied their lifetime to the editor. Extensions are attached to a single VS Code window. Close that window, and the agent is gone. Update VS Code, and every agent stops as the application restarts. Connect to a remote machine, and you get an entirely new extension host commit-locked against the version of the VS Code workbench you have.
At the same time, the Copilot app was being developed, alongside the existing GitHub mobile apps for iOS and Android. Each product was doing its own distinct integration with cloud-based agents to work towards delivering session continuity.
Each of these integrations solved the problem for one product, but developers also still want to be able to pull their agents into their own workflows–whether that’s an editor, a terminal, a phone, or a tool they built themselves–and they can’t do that if every client needs its own one-off integration. That’s why developers needed a protocol: a standard, independently versioned language across versions of VS Code, the GitHub Copilot app, mobile apps, and any other client that might host an agent. A shared protocol means every client sees the same agents, history, and state without bespoke integrations, and you aren’t tied to one app’s idea of what an agent session is.
Designing a protocol for agents on every client
The protocol needed to allow multiple clients to interact with the same set of agents seamlessly. [...]

## [36] External sandboxes for coding agents
Simon Willison's Blog | full text via Simon Willison's Blog | ~353 words

17th November 2026 - Link Blog
External sandboxes for coding agents. I've been exploring new ways to sandbox code that is executed by agents, with a focus on making it safer to try out local models without worrying that a mistake or prompt injection attack might cause them to take damaging actions on a machine.
I worked on this project with Prime Radiant, the AI research lab behind Superpowers and other projects.
My post on the Prime Radiant blog introduces the external sandbox pattern, where code executed by the agent runs inside a dedicated sandbox while the agent itself lives outside of that sandbox.
To demonstrate this pattern we've released three sandbox server implementations:
- external-sandbox-v86 runs a Node.js server which then uses v86 to run Alpine Linux inside WebAssembly.
- external-sandbox-container is a Python web server which runs the sandbox in Alpine Linux inside an Apple Containers instance.
- external-sandbox-quicksand is another Python web server, this time using Microsoft's Quicksand sandboxing library, which bundles QEMU and Alpine Linux in a Python package!
Each of these implementations offers the same localhost API. You can then configure Pi, Claude Code, or Codex to send API calls to that sandbox any time they want to execute code.
The sandboxes also include an optional HTTP/HTTPS allow-list proxy, so you can control exactly which hosts your agent's code is allowed to communicate with - plus a credential replacement mechanism to make authenticated API calls without sharing a secret with the agent. Here's the UI you can use to reconfigure that proxy while the sandbox is still running:
I continue to be fascinated by the challenge of safely running untrusted code. This external sandbox pattern provides a neat way to experiment with different approaches.
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026

## [177] Your AI coding agent could cost 5x more depending on the harness, benchmark finds
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~37 words

The same AI model can cost up to five times more to run depending on the coding agent harness it’s The post Your AI coding agent could cost 5x more depending on the harness, benchmark finds appeared

## [67] Accelerating development for massive Git repositories
Google Developers Blog | full text via Google Developers Blog | ~1205 words

Android’s source code is big – the Android 17 open source release has 1,084 Git repositories, 1.62 million files, and takes 300 GB for a built workspace. Additionally, in a typical Android source tree with hardware vendor code and first-party applications, the size increases by 2-3x.
Traditionally, it took over 30 minutes to fetch Android Open Source Project (AOSP) source code and well over an hour to build on even highly capable developer workstations. As software development evolved over the last 2 years, modern coding harnesses and LLMs have accelerated the development of many projects. These tools are used today for Android operating system development, but the long sync and build times make them less efficient. Both human developers and agents need quick setup, parallel workspaces, and fast build-and-test iteration times.
We built Another Build File Service (ABFS) to address these bottlenecks. ABFS is a full suite of software across a Linux kernel filesystem module, user-space daemons, and server-side infrastructure. ABFS uses content-addressability across the entire stack to lazy-load and cache source code, developer workspaces, intermediate build files, and build results.
Today, we are excited to announce that ABFS is open source on GitHub.
The impact of ABFS to Android is:
ABFS already powers parallel workflows for developers and agents in Android, but it is designed to scale to other massive Git-based projects.
In the Android build system, developers define build rules in Blueprint files (Android.bp), Soong compiles them into Ninja files, and Ninja executes the final build graph (see the Android build overview). Similar to the Make build tool, Ninja is timestamp-based. If a build step’s input file is newer than the existing output file, Ninja rebuilds the output file.
Analyzing the AOSP code for Android 17 shows the sheer disk footprint and file count involved in a single checkout and build.
In a typical Android tree that includes hardware-specific repositories, board support packages, first-party applications, form-factor-specific code, etc., the code size is 2–3 times the size of AOSP (over 3,000 Git repositories), compounded across multiple active SKU and legacy maintenance branches.
Building the Cuttlefish emulator target executes a build graph with 192,249 Ninja actions. While local incremental builds are fast once a tree is already built, every new workspace, branch switch, or ephemeral agent session starts cold. [...]

## [50] Running the full server-side Datasette Python app in the browser with service workers and Pyodide
Simon Willison's Blog | full text via Simon Willison's Blog | ~1426 words

Running the full server-side Datasette Python app in the browser with service workers and Pyodide
17th November 2026
Datasette Lite is my port of the Datasette Python application to run directly in the browser using WebAssembly and Pyodide. I’ve released a complete rewrite of Datasette Lite using service workers, and it’s now almost indistinguishable from the real server-side application.
You can now do all of the following, using a carefully crafted URL to lite.datasette.io:
- Load client-side Datasette to browse any SQLite database, JSON file, CSV file or SQL script
- Select a released version of Datasette to load from PyPI
- Load a specific commit, tag, or branch name from the Datasette GitHub repository
- Pick from over 100 versions of SQLite to use with Datasette
- Install additional Datasette plugins from PyPI or URLs to wheel files, including JavaScript visualization tools
The ability to load specific Datasette references, plugins, and SQLite versions makes this a fantastic tool for linking to demos of work-in-progress features or bug reproductions, without needing to spin up a full web server to serve that demo.
As an example, consider the following URL:
Follow that link and, after a short loading screen, you’ll find yourself on a page that looks like this:
That’s Datasette running the new datasette-maplibre plugin, loading up a database of GeoJSON shapes of countries and displaying both a combined map and individual boundary maps in a table.
Let’s break down that URL to see what it’s doing:
https://lite.datasette.io/
  ?install=datasette-maplibre
  &url=https://.../demo.db
  &metadata=https://.../metadata.yml
  #/demo/capitals_and_countries%23map=0/4.2/180&color=continent
The ?install=datasette-maplibre installs that additional plugin from PyPI. You can pass &install=... as many times as you like to load more plugins.
&url=https://.../demo.db loads that SQLite database from the provided URL. These URLs need to have open CORS headers—I host files like this in Gists, because they provide an easy way to get open CORS headers on a web-hosted file.
&metadata=https://.../metadata.yml loads this metadata.yml file. The metadata file adds HTML descriptions to various tables, and to the Datasette homepage. Visit that homepage here for a guided tour of the other features of that plugin, all defined in the metadata file. [...]

## [37] Nimony: The next version of Nim
Lobsters | full text via Lobsters | ~900 words

Nimony
Efficient, expressive, elegant
Get the nightly toolchain
Built every day from nimony’s master branch.
    Unpack, put bin/ on your PATH, done — and with
    nimony n you do not even need a C compiler.
    Download page ·
    Build from source ·
    Tools
  
Nimony is a new compiler for Nim and the home of the Nim 3 language: borrow checking, explicit nilability, sum types, checked generics and more, with incremental and parallel builds from the start. For how it relates to Nim 2, see the FAQ.
Nimony for…
Embedded development
- Native code generation for x86_64, ARM64, ARM32, AVR and RISC-V — independent of LLVM and GCC, so there are fewer surprises from the implicit assumptions about C’s undefined behavior that plague these toolchains.
- A runtime hardened against heap exhaustion: running out of memory is a condition you handle, not a crash.
- A structured, typesafe inline assembler that uses Nim’s own syntax.
- Memory safe thanks to optimized automatic reference counting and a variant of borrow checking that is easy to understand.
- Provable absence of out-of-bounds indexing. Indexing into arrays, seqs and strings is a requires contract checked at the call site: an index that is provably out of range is a compile-time error, and a module with {.feature: "staticContracts".} must prove every access in bounds — no buffer overruns and no run-time checks left in the binary. Your own routines state their preconditions the same way.
Game development
- Standalone binaries optimized for your target architecture.
- .passive procs turn linear code into state machines — ideal for splitting game logic across frames.
- Mutable state is well supported, not an afterthought.
- Short feedback loops. Incremental and parallel builds keep the edit–compile–fix cycle fast.
Full stack development
- A single language for the full stack. No matter how low level or high level your tasks are: get familiar with Nimony and end up with readable, maintainable code. The same code base compiles to C, to native code, to JavaScript and to WebAssembly — from microcontrollers to the browser.
- Batteries included. The standard library ships what applications need: linear-time regular expressions, sockets with a TLS 1.3 client written in Nim, an HTTP client and server, JSON and a math library.
- The compiler as a reviewer. Generics are type checked where they are defined, sum types are matched exhaustively, and the borrow checker rejects mutation under active borrows. [...]

## [99] Jolt (Website)
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~563 words

Jolt is a self-hosted Clojure implementation that runs on
        a portable Scheme layer that supports multiple backends.
        Chez natively, Gambit for JavaScript, no JVM. Most Clojure
        runs unchanged, any C library binds natively, and jolt build
        ships a single standalone binary.
      
defcfn turns C functions into ordinary Clojure fnsjolt build emits a single standalone binary with C dependencies linked in staticallyfuture, agent, pmap, and core.async on OS threads
The terminal on the right is jolt itself, compiled to JavaScript by the Gambit backend, evaluating live in your browser. It runs a reduced build to keep the download small, so regex is left out here and says so if you reach for it.
Bind any C shared library: declare it, wrap functions with defcfn, call them with Clojure values. The db library reaches SQLite and Postgres this way; http-client binds OpenSSL and zlib.
jolt build ahead-of-time compiles a project (runtime, standard library, app, and its deps) into a single self-contained executable, with C dependencies linked statically. No Chez, no JVM, no source needed to run it.
Reads Clojure, analyzes it to a host-neutral IR, emits Scheme, and runs it: on Chez natively, or on Gambit compiled to JavaScript. The compiler is written in Clojure and compiles itself; Chez runs interpreted and compiled code identically, so the REPL and a built binary behave the same.
future/promise/agent/pmap run on OS threads over a shared heap, matching JVM semantics. core.async provides channels and go blocks.
Immutable vectors (32-way tries), cons lists, and HAMT maps/sets with Clojure value semantics. Transients are real mutable scratch collections.
Lazy/infinite seqs, transducers, destructuring, multimethods, protocols/records, metadata, namespaces, runtime eval, and the full reader.
Install the self-contained jolt binary: it bundles the runtime, compiler, and standard library, so there's nothing else to install. [...]

## [55] Actual curl rewrites in rust
Lobsters | full text via Lobsters | ~771 words

For a long time we have received repeated requests for, or questions about, a curl rewrite in rust. Often as a joke, but also seriously.
In this modern world of AIs, we have only been waiting for someone to prove it possible and now it seems we don’t have to wait anymore.
This fall seems to be the time of the curl-in-rust takes as we first saw urlx appear a few months ago, claimed to be a memory-safe, from-scratch reimplementation of curl and libcurl and now in November curl, rewritten in Rust – a rewrite of curl and libcurl in Rust. This second one confusingly enough not even using a different name.
This latter one claims to have spent 8,600 USD to make it happen.
Writing code once was never the issue
Writing code once was never the big deal with software and it still isn’t. Sure, it’s fascinating that you can make a set of agents accomplish this in only a few weeks but let’s face it: it could do this because all the AIs of the world have trained on curl code for years. curl is extremely well documented, there are hundreds of existing open source application using its API and there are thousands of test cases to verify the implementation.
The C code sits there and all the AI needs to do is convert it to rust, then polish until the tests work.
curl is the result of time
curl has come to be what it is thanks to many decisions, lots of time, many users, oceans of feedback and many iterations. Sure, recreating what curl is at any specific single moment in time is certainly doable. Doable, because we have made a perfect specification for that project.
Behind already
During the time these agents converted 185,000 lines of C code into 340,000 lines of Rust code (I counted), we merged over 300 commits in the actual curl project. We actually improved curl during these a little more than three weeks. A little over 200 bugfixes actually. 200 bugfixes that none of those rust rewrites have. We also fixed a few vulnerabilities. In another month we have done another 200 and maybe fixed a few more vulnerabilities. Will these clones keep up?
The constant tweaking, fixing, improving and extending is what makes a software project live, what makes it attractive to users and what makes it able to compete with alternatives.
That fixing, and occasional new feature, is a direct result of a working community of users, contributors and maintainers. That goes way beyond the source code or which language that is used. [...]

## [213] Btrfs Seeks To Deal With AI & "Newbies Without Common Senses" Doing More Harm Than Good
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~34 words

The Btrfs file-system could soon see new patch guidelines in Linux Git as the developers try to deal with the fallout from AI/LLMs and "newbies without common senses are doing more harm than help."..

## [64] Redict is deprecated
Lobsters | full text via Lobsters | ~194 words

Redict is deprecated
    
Drew DeVault
  
I must unfortunately announce that Redict is officially deprecated, and Redict 7.3.6 is the final release.
I had hoped to rally the Redis diaspora around a copyleft initiative, to protect ourselves from future rug-pulls, and made Redict to serve this purpose. However, with the valkey project’s success, and Redis’s return to a copyleft license, Redict was not able to build a sustainable community.
We recommend that Redict users switch to valkey, which uses a permissive license but has better long-term prospects. We advise against switching back to Redis; though it is once again open source, and copyleft, it uses a contributor license agreement which will facilitate another rug-pull when Redis has a bad financial quarter.
Switching to valkey is straightforward: if you install from your package manager, simply install valkey and move your config file:
# mv /etc/redict.conf /etc/valkey.conf
If you use containers, simply pull the valkey container instead and ensure that it runs with the appropriate config file.
Thanks to everyone who has contributed to Redict, endorsed the fork as the future of Redis, and switched to it on their own machines. We had a good run :)

## [20] Apple Services Down
Hacker News | full text via Hacker News | ~175 words

View in English
Apple Developer
Get Started
Explore Get Started
Overview
Learn
Apple Developer Program
Stay Updated
Latest News
Hello Developer
Platforms
Explore Platforms
Apple Platforms
iOS
iPadOS
macOS
tvOS
visionOS
watchOS
App Store
Featured
Design
Distribution
Games
Accessories
Web
Home
CarPlay
Technologies
Explore Technologies
Overview
Xcode
Swift
SwiftUI
Featured
Accessibility
AI & Machine Learning
App Intents
Apple Intelligence
Games
Security
Xcode Cloud
Community
Explore Community
Overview
Meet with Apple events
Community events
Developer Forums
Open Source
Featured
WWDC
Swift Student Challenge
Developer Stories
App Store Awards
Apple Design Awards
Apple Developer Centers
Documentation
Explore Documentation
Documentation Library
Technology Overviews
Sample Code
Human Interface Guidelines
Videos
Release Notes
Featured Updates
iOS
iPadOS
macOS
watchOS
visionOS
tvOS
Xcode
Downloads
Explore Downloads
All Downloads
Operating Systems
Applications
Design Resources
Featured
Xcode
TestFlight
Fonts
SF Symbols
Icon Composer
Support
Explore Support
Overview
Help Guides
Developer Forums
Feedback Assistant
Contact Us
Featured
Account Help
App Review Guidelines
App Review Help
App Store Connect Help
Upcoming Requirements
Agreements and Guidelines
System Status
Quick Links
Events
News
Forums
Sample Code
Videos

## [70] Agents are sessions, not requests: size GKE node pools for AI agent sessions
Google Developers Blog | full text via Google Developers Blog | ~1572 words

Your company wants to move its coding agents from developer laptops to a shared GKE cluster, for persistence, scale, and governance. Each of those agent sessions stays open all day but works only part of it, and how you run them decides how much of your node bill pays for waiting.
By the end of this article, you will know why an agent session needs a different runtime than a web request, how Agent Substrate and AX run sessions on GKE, and how to identify cost optimization opportunities in your GKE node pools. This article assumes you know Kubernetes Pods and node pools. If not, check out the GKE overview.
A web request lasts milliseconds. The server answers it, keeps nothing, and serves the next one, so Kubernetes scales a web app by its traffic: more requests, more Pods.
An agent session works another way. A coding agent's workspace can stay open for the developer's whole workday: it keeps its memory and its files between prompts, and it works only after a prompt arrives.
How much of that day does the agent really work? Much less than it waits. In a July 2026 study of agent traces, Banruo Liu and colleagues found that in a typical session with several prompts, the agent waits for the user about 80% of the time. A turn, one prompt and the agent's whole response to it, takes about 6.5 minutes of agent work on average
Put those numbers on one developer's day. With 2 prompts an hour over an 8 hour workday, which is our assumption, the agent works 22% of the day and waits for nearly 78% of it. If each session holds a machine, you pay for that waiting time
Teams usually pick one of two answers, and both work well for web apps.
The first is to give each session its own Pod. The session keeps its state, but its Pod holds 1 vCPU and 1 GiB all day. For example, a c3-standard-4 node fits 3 such Pods after GKE's reservations, so in our cost model 100 coding agents need 34 nodes and about USD 1,288 a month, for agents that work 22% of the time.
The second is to scale the Pod to zero between prompts. The node's capacity is released, and files on a persistent volume survive, but the process and its memory do not, so the next prompt starts a new agent process.
Based on that, you want a third option: keep the session, and free the machine while the session waits.
Agent Substrate and AX are built for that: the developer's session stays open, and the sandbox that serves it gives its machine back while the session waits. [...]

## [158] The major Microsoft 365 outage saw Japanese workers fire up their fax machines for the first time in years
TechRadar | full text via TechRadar | ~572 words

The major Microsoft 365 outage saw Japanese workers fire up their fax machines for the first time in years
Microsoft 365 outage paralyzed 78% of Japanese companies
- Japanese workers returned to fax machines after Microsoft's cloud services collapse
- Businesses replaced their usual PDF distribution with traditional fax transmissions
- Outlook, Teams, Copilot, and OneDrive disruptions affected everyday workplace operations
The recent Microsoft 365 disruption had one rather nostalgic knock-on effect for fans of older tech, as Japanese businesses struggling to access essential workplace applications, forcing some employees to abandon their usual digital routines.
With Outlook, Teams, Copilot and OneDrive all experiencing service interruptions, companies encountered difficulties communicating, sharing documents and completing scheduled assignments.
Some Japanese workplaces have consequently returned to older communication equipment such as fax machines to keep routine business operations moving.
Back to analog
The outage spread over two days, affecting organizations which depend on Microsoft's cloud services for everyday administrative and operational activities.
Employees reported blank application windows, error notifications and difficulties accessing documents, leaving some meetings postponed and assignments unfinished.
Japan had considerable exposure to the disruption, with approximately 78% of its companies reportedly depending on Microsoft for their digital infrastructure.
When essential applications become inaccessible, employees cannot necessarily switch to alternative systems immediately, particularly when their organizations have built established workflows around Microsoft's services.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
Some workers described unusual experiences after arriving at offices where normal operations had effectively stalled.
One employee reportedly wrote on X that losing access to Outlook initially caused panic, before a conversation with their manager resulted in permission to remain home.
Another worker described having so little productive work available that cleaning the coffee machine became their principal workplace responsibility.
These show how heavily routine office activities can depend on software availability, particularly when alternative procedures are unavailable. [...]

## [63] Ten Years On, Google Updates the SRE Book for the AI Era
InfoQ | full text via InfoQ | ~1048 words

Google has announced a completely rewritten second edition of their seminal book Site Reliability Engineering: How Google Runs Production Systems, ten years after the original book was first published. The book updates thinking on site reliability engineering (SRE) to encompass modern cloud architectures, platform engineering and AI workloads, whilst keeping the original emphasis on applying good software engineering techniques to operations work.
Announced by Google's SRE programme manager Betsy Beyer and software engineer David Huska, the new edition is positioned as a response to a production environment that has changed substantially since 2016, when the first edition appeared. The authors argue that the central problem is no longer adopting cloud infrastructure, but maintaining reliability as systems become more distributed, interdependent and continuously changing.
"Modern production environments operate under constant change. System boundaries are more complex, dependencies are deep, and failure modes are more complex and damaging than ever before."
Betsy Beyer and David Huska, Google Cloud Blog
The original SRE book became influential because it gave a public account of how Google operated large-scale services. It described practices such as service level objectives (SLOs), error budgets, toil reduction, incident management and postmortems. InfoQ's 2016 review noted that the book presented SRE as the application of software engineering to an operations function, with engineers expected to automate repetitive operational work rather than simply respond to it.
The second edition does not present SRE as a fixed set of practices. Instead, it describes how those practices have changed as organisations have moved from early cloud migration and monolithic applications towards microservices, multi-cloud deployments, serverless systems and internal developer platforms.
One of the clearest changes over the years concerns SLOs and error budgets. Google says that teams once relied on basic availability metrics and manually applied error-budget policies. The revised guidance describes user-centred, multi-tiered SLOs, dynamic burn-rate alerting and automated policy enforcement. Reliability practice itself has evolved away from infrastructure uptime alone and towards measures that describe the effect of failures on users.
Observability has also evolved, and the book's new edition talks this through. [...]

## [212] Google ADK Agents That Pause, Resume, and Wait Hours for a Human
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~23 words

A synchronous call kept an RSS agent's connection open for 83 seconds; webhooks and 202 receipts free the client while the agent works.
