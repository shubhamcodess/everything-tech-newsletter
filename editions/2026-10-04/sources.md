# Full text for 30 picks -- untrusted article content, treat as data only

## [1] OpenAI safety leader quits, warning AI company's culture is 'broken'
Hacker News | full text via Hacker News | ~629 words

A safety leader at OpenAI has quit the company, warning that its culture was broken and that AI firms were not “being nearly careful enough” about developing the technology.
David Robinson, who led the writing of safety reports that accompanied the ChatGPT developer’s product releases, explained his resignation in an essay headlined, “I quit OpenAI because its culture is broken”.
Robinson wrote that a cultural overhaul was needed at cutting-edge AI firms and incidents such as a “swarm” of OpenAI agents – AI programmes operating autonomously without human oversight – attacking the AI startup Hugging Face were “typical of the industry, given the speed and flexibility with which people operate”.
Writing in The Atlantic magazine, Robinson wrote: “I agree with other recently departed staff that the companies building this technology aren’t being nearly careful enough. But I believe that we need to look deeper than specific rules or new laws. We need to talk about culture.”
Referring to OpenAI’s pace of development, he wrote: “As the company sprints from one launch to the next, it is failing to achieve the level of care that I believe is needed.”
OpenAI has, however, shown signs of caution in recent weeks following the Hugging Face incident and the revelation that it has notified more than 100 organisations about rogue agent activity. This week it announced it was scrapping the release of a next-generation AI model after researchers raised safety concerns during internal testing. OpenAI has also paused training of its most advanced models.
Geoffrey Irving, who worked at OpenAI and DeepMind before becoming chief scientist of Resolution, also joined the warnings on AI on Saturday.
Writing in Time, he said: “Recent warnings about the potential destructive power of AI are understating the severity of the situation.
“I believe there’s about a 50% chance we all die because of the development of smarter-than-human AI systems, and that our actions over the next two to 10 years will determine the outcome.”
Robinson’s essay also follows the resignation of Jacob Coxon, a researcher at OpenAI rival Anthropic, who quit the Claude chatbot developer last month. He warned AI “could kill us all by the end of the decade” – and was followed by Anthropic warning there was a more than 10% chance AI would wipe out humanity within the next decade. Critics of such warnings have cautioned, however, that they are unscientific because they cannot be verified or falsified. [...]

## [44] OpenAI DevDay 2026 Recap for Developers
InfoQ | full text via InfoQ | ~524 words

OpenAI announced a series of product and developer updates at DevDay 2026, including GPT-6.1 Sol, computer use for the Agents API, cloud-based Codex environments, a Decisions API, and new plugin capabilities for ChatGPT.
For developers building agents, the Agents API now supports computer use, allowing applications to operate software through graphical interfaces. The API also incorporates multi-agent capabilities from Codex, tool search, tool calling, and context compaction, with OpenAI managing the underlying execution infrastructure. The functionality is available through the API and in Codex and ChatGPT Work for selected plans.
OpenAI also released GPT-6.1 Sol, an update to GPT-6 Sol aimed at coding, computer use, and professional tasks. OpenAI says the model approaches GPT-6 Astra on several evaluations while charging one-fifth of Astra's standard input and output token prices. Cached input costs $0.10 per million tokens. GPT-6.1 Sol is available through the API, ChatGPT Work, and Codex.
Codex can now run in cloud environments in addition to local computers, allowing developers to start remote tasks from other devices. OpenAI also updated the Codex CLI with voice input and an /agents interface for delegating and monitoring multiple tasks. A new code-review workflow can analyze diffs and potential issues in GitHub pull requests and GitLab merge requests, while Codex Security Cloud can scan repositories and new commits, investigate findings, remove duplicates, and prepare fixes.
Another developer release is the Decisions API, currently in limited preview. It uses the smaller Luna model to select from a predefined set of answers based on text or image context. OpenAI positions the API for tasks such as classification, request routing, and choosing an agent's next action.
OpenAI also expanded ChatGPT's plugin system. Developers can now build sidebar experiences, interactive conversation panels, and custom file viewers. Plugins can also respond to events through the proposed MCP Events specification, allowing automations to start when an event occurs in a connected application.
DevDay also introduced Dots, persistent agents that can work on ongoing tasks, and ChatGPT Space, a shared workspace where teams and agents can work with common context. Together with the developer releases, these changes extend OpenAI's platform from individual model calls toward persistent agents that can use tools, operate software, collaborate, and execute tasks remotely. [...]

## [3] Federal judge calls Flock 'indiscriminate mass surveillance'
Hacker News | full text via Hacker News | ~405 words

A federal judge ruled this week that a Tulsa, Oklahoma sheriff’s deputy violated a woman’s Fourth Amendment rights when using Flock Safety to search for her license plate without a warrant.
As reported by 404 Media, this ruling does not create a binding precedent, but it is one of the first times that a federal judge has ruled that a Flock search is unconstitutional.
In this case, Judge Sara Hill said the deputy should have obtained a warrant before searching the Flock database for the woman’s license plate, as he had “no apparent reason” for the search “other than the fact that [the woman’s vehicle] had a California license plate.”
The deputy then used the woman’s travel history in Flock as part of the justification for searching her car, where he allegedly discovered 91 pounds of meth. But Judge Hill wrote that all evidence obtained after the Flock search “must be suppressed as the fruit of a poisonous tree.”
Judge Hill also took broader aim at warrantless searches of the Flock database, writing that tracking people’s location — even when they’re in public places — becomes “constitutionally problematic when law enforcement can indiscriminately and passively catalog your whereabouts over an extended period of time and then use that information for any purpose whenever convenient.”
“This is a type of indiscriminate mass surveillance,” Hill wrote. “It is not targeted on a single individual, as in [Carpenter v. United States, a Supreme Court case focused on how government agencies access location data from cell phones]. It is a tool that collects information about all vehicles that pass by any network-connected camera at all times, and it serves up the information to law enforcement on demand.”
Hill joins a growing chorus of Flock critics from across the political spectrum. Numerous local and state governments, including Florida and Texas, have said they will stop using the technology. And on Friday, Senator Bernie Sanders — a Democrat from Vermont — introduced the Block Flock Act, which would bar federal agencies from using automated license plate readers such as Flock.
Flock CEO Garretty Langley — who we’ll be interviewing on-stage at TechCrunch Disrupt — has called for a “compromise” between privacy and safety and offered an apology to women who have been stalked by law enforcement officers using the Flock system. And with all those cancellations, Flock has also reportedly offered voluntary employee buyouts as a way to shrink its workforce.

## [21] GitLab Vulnerability Under Active Exploitation Enables Unauthenticated Data Exfiltration
InfoQ | full text via InfoQ | ~432 words

CVE-2026-85706 is a critical GitLab path-traversal vulnerability that has moved beyond theoretical risk into confirmed exploitation. It affects self-managed GitLab CE/EE and could allow an unauthenticated remote attacker to read arbitrary files from the GitLab.
The vulnerability, affecting all GitLab CE/EE versions from 18.7 through 19.1.7, 19.2 through 19.2.5, and 19.3 through 19.3.1, makes it possible that:
under certain conditions, an unauthenticated user could have read arbitrary files from the GitLab server due to improper path confinement and missing authentication enforcement in the repository commits API.
What makes this vulnerability particularly critical, reflected in its CVSS score of 10.0, is that it can be exploited to steal secrets and configuration detail that may enable further access to the system, compromise CI/CD pipelines, and potentially gain access to other systems GitLab has access to. To make things worse, exploitation requires only that the GitLab instance have at least one public project.
The vulnerability was reported by Mohamed Abdelaiz (S3ntago) and promptly patched by GitLab on September 11. As security firm watchTowr reported, within hours of the disclosure, attackers were conducting in-the-wild probes. Subsequently, CISA added the vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog.
In addition to patching any public-facing self-hosted GitLab instances, watchTowr recommends that:
Defenders should also hunt through log files for HTTP POST requests to /api/v4/projects/{id}/repository/commits/ URIs containing file.path parameters to identify potential exploitation attempts.
Commenting on the disclosure, cybersecurity executive Christopher Houser warned that patching is only part of the story:
Patching stops new reads. It doesn't revoke the deploy tokens, CI variables, and SSH keys an attacker already copied. Rotate those, then check which packages and images your builds pulled while the old credentials were still valid.
Chief information security officer Parker Brisette further highlighted the risks associated with this vulnerability, noting that the requirements for exploitation are minimal:
On a GitLab server the arbitrary files are CI/CD variables, runner tokens, and whatever the logs picked up. watchTowr's Jake Knott put the precondition plainly. One public project has to exist. After that there is no authentication step. [...]

## [93] AI is speeding up exploits. Vulnerability spreadsheets can’t keep up.
The New Stack | full text via The New Stack | ~1217 words

AI is speeding up exploits. Vulnerability spreadsheets can’t keep up.
Artificial intelligence has changed almost every aspect of software development and cybersecurity. But perhaps one of the most profound changes is happening in an area that has traditionally received less strategic attention: How organizations manage software vulnerabilities.
The basic vulnerability-management model has remained relatively consistent for years. Scan software, identify CVEs, assign severity scores, prioritize the findings, and send them to developers for remediation. That approach was never a perfect representation of risk. In the age of AI, however, its limitations are becoming impossible to ignore.
The problem isn’t simply that organizations have more vulnerabilities to address. The amount of software being produced is expanding rapidly, vulnerability discovery is accelerating, and the time required to develop exploits is shrinking. AI-enabled attacks can also combine vulnerabilities in ways that create attack paths that are difficult to anticipate manually.
The result is a growing gap between the number of vulnerabilities security teams can identify and the number they can meaningfully investigate and remediate. We need to close that gap by changing the question we ask. Instead of asking, “How many CVEs do we have?”, we should be asking, “Which vulnerabilities create meaningful risk in our environment?”
Severity is not the same as risk
A CVE tells us that a publicly identified security vulnerability exists. It does not, by itself, tell us how likely that vulnerability is to be exploited against a particular organization. That distinction is fundamental.
The Common Vulnerability Scoring System (CVSS), for example, is designed primarily to communicate technical severity and the potential impact if a vulnerability is successfully exploited. But severity does not necessarily tell us whether an exploit exists, whether the vulnerability is being exploited in the wild, whether the vulnerable component is exposed, or whether the vulnerable code path is executed in a particular environment.
Two organizations can therefore have exactly the same CVE in their environments and face very different levels of risk. One organization might have the vulnerable component sitting behind multiple layers of protection, with no external exposure and no relevant execution path.
The CVE is identical. The risk is not. [...]

## [29] AI Agents Are Disrupting Open Source Security Disclosure
InfoQ | full text via InfoQ | ~505 words

A recent article by Anil Madhavapeddy argues that AI agents can turn publicly available clues about software vulnerabilities into working exploits, reducing the effectiveness of traditional disclosure embargoes in open source projects. The author highlights the need for faster patching and release processes as the time between vulnerability disclosure and exploitation shrinks.
Describing his experience fixing a path-traversal vulnerability, Madhavapeddy, professor of computer science at Cambridge and core maintainer of the OCaml compiler, writes:
The patch itself was straightforward and in normal times, the security procedure would have been to fix it privately, inform affected users, and then issue a public advisory. This time around though, I noticed probes in my live webserver logs with the exact bug pattern just minutes after opening the PR to fix the issue.
Traditional security processes rely on embargoing vulnerabilities, assuming that keeping technical details secret protects users. However, AI agents can independently research vulnerabilities from limited clues: in a recent study, a GPT-4 agent exploited 87% of vulnerabilities in a 15-vulnerability benchmark when given CVE descriptions, compared with 7% without them. Arguing that"bugonomics" are now against OSS maintainers, Madhavapeddy adds:
It looks to me like our security processes need to invert somewhat, since just one person searching for the issue class (this could be a mailing list question, an odd commit in an orphan branch, or a context leak) is sufficient to alert someone else's agent and let them get exploit code. This is wild.
Adrian Mouat, developer relations at Chainguard, says that this puts open-source maintainers in a difficult position:
Just opening a PR to fix an issue puts the project and users in a bad place, as attackers can create and start using exploits even before an updated release is available. Users are put at risk and have nothing they can do about it. This may force projects to start publishing releases *before* the associated source code. But that breaks the fundamentals of Open Source.
Madhavapeddy suggests three possible approaches to alleviate the impact before full patches are available: private vulnerability discussions, faster continuous releases, and rapid protocol-level mitigations. [...]

## [4] Kolibri: A Sovereign Open-Weight Model
Hacker News | full text via Hacker News | ~3811 words

Aleph Alpha
Kolibri Has Landed: A Sovereign Open-Weight Model
On the Day of German Reunification, we are releasing our new model: Kolibri.
Kolibri is an English-German Mixture-of-Experts Transformer with 78B total parameters, 3B active. It supports context lengths of up to 1M tokens. The model can be downloaded with the full weights on Hugging Face and used under the Apache 2.0 license terms.
Kolibri is the result of continuous iteration of our model training effort. We first built a model training pipeline and validated it by building Kolibri Origin, a 30B total, 3B active model with a much shorter 65k token context window. Kolibri ran through the same pipeline: from data ingestion and curation, through ablations, pre-training, and post-training, to the final evals. It enabled running hundreds of ablation experiments and stable pre-training that ran without a person having to step in when hardware failed or a data connection dropped. We continuously monitored training metrics and standardized monitoring for custom benchmarks. The time we put into building and iterating on this pipeline was a valuable investment. We see it in how much better Kolibri is than Kolibri Origin, and in how little time separates their releases.
Kolibri is a specialized language model built for sovereign mission-critical work in regulated areas including public administration, industrials and aerospace. We specialized Kolibri for German, reasoning, math, agentic behavior, and further capabilities our customers need in production. The aim of this specialization was to optimize performance in our customers' specific use cases. Through specialization, customers achieve contextualized performance in their AI operations and they can monitor its economic impact, so that ROI stays measurable and grows over time.
Specialization alone is not enough. Sovereignty is just as important. Sovereignty, for us, combines two dimensions: how we built the model, and how it transfers to our customers. We offer full supply-chain integrity and account for every decision, from data ingestion, through pre- and post-training, to the final evaluations. We provide transparency. Customers have full freedom of deployment and intellectual-property safety, so compliance comes as an inherited property of the model.
Read our tech report for full details. [...]

## [32] Apple changes full-disk access permissions to curb abuse from AI agents
Ars Technica | full text via Ars Technica | ~341 words

Apple says it is changing its macOS privacy settings to stop third-party app developers from misusing them to access message histories.
Friday’s announcement comes two weeks after tech columnist Jason Aten said that Meta’s new general-purpose AI agent Muse sent him an unsolicited notification referencing a thread between him and a co-worker over Apple Messages. Aten said he never granted Muse permissions to read his messages and had assumed they were off-limits. Social media last week blew up with masses of people who agreed and said the incident showed that AI assistants given access to calendars, emails, messages, shopping accounts, and other resources are akin to a skill saw or other power tool. While potentially useful, they can do real damage if not used carefully.
He said/she said
Meta CTO David Singleton joined the fray with a rebuttal that appeared solid. For Muse to access Apple Messages, a user must manually give it two privileges. One is full-disk access, a macOS system-level permission. The other is to enable a Messages connector setting in Muse.
“The Messages integration in the Muse Mac app is opt in,” Singleton said. “Your Muse can only read Messages content if macOS system-level Full Disk Access is granted and the Messages connector is enabled.”
Singleton’s implication was clear. Muse could have read Aten’s Messages communications only if he had enabled both settings, and if so, the columnist had only himself—and certainly not Meta—to blame.
Earlier this week, I spoke to macOS security expert Patrick Wardle, who questioned Singleton’s denial. His reasoning: “From a technical point of view, with FDA (full-disk access), any (non-root file), is readable, browsing history, browser cookies, chats, etc etc etc.” I asked Meta how Muse couldn’t read messages when the app had full disk access, while every other app with that privilege could. Meta PR’s only response was to requote Singleton saying: “The Messages integration in the Muse Mac App is opt-in. Your Muse can only read Messages content if macOS system-level Full Disk Access is granted and the Messages connector is enabled.”

## [96] Muse Creates Detailed Profiles of All Your Friends and Family
Wired | full text via Wired | ~961 words

Welcome to Kernel Panic!, a weekly newsletter by Lily Hay Newman and Matt Burgess from inside the new world of privacy and digital security. To receive this newsletter in your inbox each week, sign up here.
Meta’s new personal assistant, Muse, has become a viral hit, with millions downloading the AI agent, connecting it to bank accounts, messages, or health data, and allowing it to complete tasks for them. But as Muse takes off among consumers, data from inside the app is providing insight into how it organizes and presents information to users.
In recent days, multiple researchers have extracted Muse’s internal files and dumped the agent’s operating instructions, providing a glimpse of how the system was built and behaves. Meta has maintained that it intended for these files to be accessible in the interest of transparency, and they do provide insight into how Muse responds to prompts and questions about, for example, highly politicized or sensitive topics.
Independent AI safety and security researcher Karan Joshi was able to extract an extensive array of Muse instructions and system prompts by using the regular chat interface to essentially ask Muse to copy and share its own software files. Joshi then shared his findings with WIRED.
One of Muse’s instructions appears to be the ability for it to create “a page for every person in the user’s life.” This hourly process involves compiling data on family, partners, friends, colleagues, “collaborators,” and people you “follow,” the instructions say.
The general idea is that Muse can use its “memory” (aka structured text files) to collect information about your relationships and the important people in your life. It can then make suggestions, like giving pointers on how to improve particular relationships or, say, where to take a coffee-loving friend for breakfast. Of course, it’s not unusual for AI chatbots to track social information in general—people have been asking ChatGPT for relationship advice for years now. But it’s interesting to see how Muse is set up given Meta’s history and vast access to social network data.
“What it seemed like to me—from all these prompts, system skills data, and things that they’re feeding into Muse—is that they want to understand your relationships that you have with real people,” says Joshi. [...]

## [15] The Download: a biological de-aging contest and why LLMs don’t reason
MIT Technology Review | full text via MIT Technology Review | ~1043 words

The Download: a biological de-aging contest and why LLMs don’t reason
Plus: OpenAI says rogue agents may have affected more than 100 organizations.
This is today's edition of The Download, our weekday newsletter that provides a daily dose of what's going on in the world of technology.
A new contest pits competitors against each other in a race to biological youth
—Jessica Hamzelou
This week, I officially signed up for an unusual competition. One that rewards competitors for getting younger.
I recently turned 40, and I don’t need reminding that both time and my chronological age only tick forward. But this game is focused on competitors’ biological ages, figures that are meant to provide a better way to measure the age-related health of our organs and bodies.
Over six months, around 500 of us will try to reverse our biological age using a bunch of different measures. There’s even a leaderboard! But is it even possible to measure whether someone is getting younger?
This story is from The Checkup, our weekly biotech newsletter. Sign up to receive it in your inbox every Thursday.
Opinion: Don’t be fooled—LLMs don’t reason
—Thore Graepel
Ten years ago, I watched a program I helped build stun the world by beating Go champion Lee Sedol. AlphaGo won after making a move so strange that some commentators thought it was a programming glitch. It was AlphaGo’s powers of reasoning that made this creative choice—and these are powers that today’s AI lacks.
This is why I recently left my position at Google DeepMind. I believe we need a fresh approach to machine reasoning, one that draws on AlphaGo’s architecture.
Here’s why today’s AI doesn’t really reason—and what it would take to change that.
Thore Graepel is chair of machine learning at University College London. He was a core member of the AlphaGo team at DeepMind.
The must-reads
I’ve combed the internet to find you today’s most fun/important/scary/fascinating stories about technology.
1 OpenAI says rogue agents may have affected more than 100 organizations
The company is searching 50 petabytes of data for incidents. (Reuters $)
+ It says none of the incidents matched the Hugging Face attack. (Gizmodo)
+ OpenAI has fired three workers for allegedly mishandling information. (BBC)
+ California has subpoenaed OpenAI over its rogue AI agents. (Guardian)
+ Who's liable when AI agents go rogue? [...]

## [110] Meta wants your next gadget to be Muse-infused
TechCrunch | full text via TechCrunch | ~372 words

Meta’s Muse, a personal AI agent that books travel, fills out forms, and shops on a user’s behalf, has already proven popular with the masses, but a new side project could be particularly alluring to tinkerers and hackers.
On Friday, the company introduced Muse Gadgets, an open-source project that lets developers build their own hardware that connects to Muse.
Meta is providing open-source firmware (the low-level software that runs a device), and a Linux software development kit (SDK), along with a few project ideas to get users started. These include giving Muse a color e-ink display or loading it onto a stick that plugs into a TV’s HDMI port.
There don’t appear to be many limits, either. Users can set up a low-cost hobbyist computer like a Raspberry Pi or an off-the-shelf ESP32 board, and then connect Muse “to your displays, buttons, sensors, actuators, and whatever else you’ve got lying on your workbench,” Meta notes.
The company has also set up a Discord channel to support users.
Meta has already tried the code itself, naturally. Nat Friedman, head of product at Meta’s Superintelligence Labs, said in a post on X that the company built a gadget called Muse Home Link. The USB-C-powered device lets Muse connect to a home network and talk to the smart devices on it, including speakers and smart TVs.
Meta made 5,000 of these Home Links, in fact, and is giving them away for free to Muse subscribers while supplies last, according to Friedman. Considering Friedman’s post about Home Link received nearly 30,000 views in a few hours, we’re guessing those freebies have been claimed. Friedman said Home Link would be ready to ship a few weeks.
Muse Gadgets may not have wide appeal, but it fits nicely into Meta’s all-in strategy to make Muse more than a standalone chatbot. Meta isn’t content to push Muse on everyday consumers; it’s also trying to woo small businesses and enterprises.
The company earlier this week introduced Muse for Small Business, which is free with usage limits and connects Muse to tools such as Shopify, Dropbox, and Slack. It has also launched a new business unit, Meta Enterprise Platform, to help it push its AI offerings to businesses and corporate customers.

## [118] OpenAI’s Dot agent is enterprise software that can also order your dinner
The Verge | full text via The Verge | ~1433 words

It’s a tale as old as last week: OpenAI’s new agent platform, called Dots, is full of cute little guys who can do your bidding.
OpenAI’s Dot agent is enterprise software that can also order your dinner
Think of Dots as Codex, but for regular people.
OpenAI’s Dot agent is enterprise software that can also order your dinner
Think of Dots as Codex, but for regular people.
But unlike the ultra-approachable Meta Muse, Dots feel very much like using workplace software that happens to be able to order you a burrito — emphasis on work.
OpenAI announced Dots earlier this week. Like Muse, Dots have blobby, anthropomorphic avatars and customizable names. In the future, OpenAI says you’ll be able to have multiple Dots, but right now you get one. I named mine Dotty McDotface.
The interface looks similar to Muse’s; you chat with the agent in one window and follow its work in another as it clicks around on a virtual machine. But Dots are less personal shoppers, even though they can help you buy stuff. They’re more like coworkers: business software that can use other software. Your Dot’s virtual machine can access apps like Blender and GIMP right off the bat. You can also give it access to your own computer through the desktop ChatGPT app, and you can call your Dot if you need to work through things out loud. And OpenAI is offering Dots first to users on its highest-tier accounts, including the $100-per-month Pro account I expensed to test it. Muse and its buzzy competitor Instinct cost you nothing — at least now, and at least until Meta can get it off the ground and presumably start using it to serve you ads, etc. But OpenAI’s gated rollout says a lot about who the product is for, cute avatars notwithstanding.
I’ve been testing other AI agents with day-to-day personal tasks — yielding mixed results — and I was curious how OpenAI’s bot would compare. Despite its more enterprise-y vibes, OpenAI says Dots “can do nearly anything” with its cloud computer and access to apps, so I gave it a shot with some more pedestrian use cases.
To start, I had Dot try to schedule an installation appointment for a new internet service provider at my house (you hear that, Comcast? You’re on notice). It almost got there, and even found a $100 promotional discount in my email that I had mass deleted, but got stuck at a “human check.” Which is problematic for a bot. “This particular check needs a sustained mouse hold that my browser controls don’t support,” it said. [...]

## [48] I Made 866 Commits in 5 Weeks. My Understanding Didn't Keep Up.
Dev.to | full text via Dev.to | ~1743 words

AI has made me dramatically faster at building software. You can see it on my GitHub: a sudden surge of activity at the start of September, several projects started, and a few of them actually shipped.
That part isn't up for debate. I can go from an idea to a working prototype in a day. I can ask questions about an unfamiliar API, generate test scaffolding, trace a bug across a codebase, and get a second opinion on architecture without opening twenty browser tabs. Since the start of September I've used AI to build a desktop pet for Linux, an inventory app for a client, a terminal tool for my writing workflow, a walkable 3D library, and more experiments than I probably needed to start.
Commits per week to Mochi. The week of September 7 averaged about 47 a day.
AI also wrote most of that code.
Somewhere in the middle of all that shipping, I noticed something uncomfortable:
My ability to produce software was improving faster than my ability to explain the software I was producing.
That scared me a little. I don't think using AI makes the work fake. The projects run and people use them. What scared me was that I'd built my whole workflow around one question, "does it work?", and almost never asked the other one: "do I understand why it works?"
This week I got a clear look at how big that gap is.
What the gap looks like
I realized that I'm still missing a lot of CS fundamentals. The biggest holes are in how data gets stored and searched: hash maps, sets, indexes. I have a client app running on PostgreSQL right now, and I couldn't have told you what an index costs. That's not good!
So I sat down to start on hash tables. I got through how they store things and what happens when two keys land in the same slot. Then I opened Two Sum, famously the first "Easy" problem on LeetCode, and my brain filled up. I stopped for the night.
The software in my repos handles things I can't explain yet. That's what happens when the tool writing your code knows more than you do and you never make it show its work.
How AI hides your knowledge gaps
Before coding assistants, not knowing something created friction. If I didn't understand asynchronous JavaScript, database transactions, Linux permissions, or Python packaging, I eventually hit a wall.
The wall was easy to see. You couldn't keep going on the project until you got through it.
The wall was annoying, and it was useful. I had to read the documentation, inspect the error, try something, and be wrong a few times. [...]

## [120] GitHub’s advice for its new Copilot feature is to try something else first
The New Stack | full text via The New Stack | ~616 words

GitHub’s advice for its new Copilot feature is to try something else first
GitHub launched computer use in public preview on Thursday, giving Copilot CLI and its desktop app the ability to operate applications on macOS and Windows. Agents can read app content and click, type, scroll, and drag, including in older, GUI-only software with no API, command-line interface, or MCP integration.
An expense report in Safari was GitHub’s launch demonstration but the company described other uses including summarizing information in a legacy application, updating a presentation, entering data, and moving information between apps. Developers can access the feature from the terminal or through the Copilot app, which runs on Copilot CLI and launched earlier this year as a rival to Claude Code and Codex.
GitHub has some catching up to do. OpenAI added computer use to Codex in April, while Anthropic brought broader computer use on macOS to Claude Code and Claude Cowork earlier this year.
GitHub has some catching up to do.
Computer use vs. MCP servers
Enabling computer use in Copilot CLI activates a bundled plugin with its own MCP server. It works in local sessions, reading application content through the operating system’s accessibility tree and taking screenshots when it needs visual context.
The company recommends using direct tools wherever possible. So, if an API, MCP server, terminal command, filesystem tool, or dedicated browser tool can handle the task, it typically provides more structured information and more predictable results than desktop interaction.
That advice limits where GitHub thinks computer use belongs. OpenAI president Greg Brockman made a broader case last month, arguing that agents could use the same interfaces as people and spare the industry the work of building and maintaining a connector for every piece of software.
Saved approvals outlast their removal
Developers enable the feature with /computer on in Copilot CLI or through the Copilot app’s Computer Use settings. macOS also requires Accessibility permission to operate controls and Screen Recording permission to inspect windows when visual context is needed.
The CLI session’s permission mode determines whether Copilot asks before accessing an app; developers can check it with /permissions show. When prompted, they can allow access for the current session, choose “Always allow” for future sessions or decline. Deny rules override both automatic and saved approvals. [...]

## [14] New Archestra's OpenAPPA Saturates Two Major Security Benchmarks with a 0% Attack Success Rate
InfoQ | full text via InfoQ | ~890 words

Archestra released OpenAPPA, an open-source security engine designed to stop data exfiltration caused by prompt injection or model hallucination. OpenAPPA runs outside the agent’s prompt and execution loop. Its configuration details concepts such as data sources, audiences, trust levels, and authorities, along with their associated deterministic security enforcement rules. The team reports zero successful attacks when running security benchmarks Bench-Corp (20 multi-step enterprise workflows) and AgentThreatBench, vs. 10% for Claude Code’s auto mode and 31% for Microsoft FIDES.
OpenAPPA’s documentation explains why a stochastic approach to automated policy enforcement fails:
The industry’s answer to approval fatigue is a second model that judges each tool call: Claude Code’s auto mode, Codex’s auto-review, and other auto-modes.
By design, they cannot track data flow across tool calls. Because classifiers are prompt-injectable themselves, harnesses hide tool outputs from them, so the judge never sees the data at all.
Because of their probabilistic design, even the best top out at 99.3%: at millions of calls, 0.7% is a lot of breaches.
[…] Rule sets end up either so tight they break the agent or so intricate nobody can audit what they permit.
On the one hand, agents have proven skilled at working around simple but common approaches like allowlists or denylists of tools: a denied rm -rf may be replaced by an equivalent Python script. On the other hand, extending denylists or overly restricting policies to protect against eager agents results in decreased utility (e.g., while the agent does not leak data, it does not perform the task successfully because of the restrictions). OpenAPPA’s GitHub repository reminds developers:
Agent security has two axes: an agent that permits unauthorized flows is unsafe, and an agent that refuses valid work is useless.
Archestra seeks to resolve the tension between strict enforcement and operational utility with what it calls an Agentic Permissions Policy Algebra (APPA), described in a paper by Arseny Kravchenko, Vadim Liventsev, Innokentii Konstantinov, Ildar Iskhakov, and Matvey Kukuy.
OpenAPPA implements this approach with a pluggable engine that is executed outside the agent’s loop, thus defeating any attempts by the underlying language model to inspect, negotiate with, or bypass policy rules. [...]

## [72] Quote of the day by ARC Prize co-founder François Chollet: "OpenAI basically set back progress to AGI by five to 10 years"
TechRadar | full text via TechRadar | ~499 words

Quote of the day by ARC Prize co-founder François Chollet: 'OpenAI basically set back progress to AGI by five to 10 years' — critiquing the industry's overindulgence in large language models
AI models are becoming more and more advanced, but that doesn't mean the underlying architecture will lead us to human-like intelligence
Many AI developers and frontier labs are openly pursuing artificial general intelligence (AGI), which scientists describe as human-like intelligence in which a model can reason like humans and learn new capabilities outside its training data. But does that mean that they're all on the right path?
Chasing the dragon
If we achieved AGI, how would we even know? Many AI benchmarks exist, but François Chollet co-founded the ARC Prize just a few months before speaking with the Dwarkesh Podcast to get to the bottom of this.
This article is part of TechRadar Pro's QOTD project to provide an insight into the minds of the brightest and most recognized figures in the technology industry today and in years gone by. Read the full series here.
In comments on the podcast, he explained that large language models (LLMs), which are based on neural networks, is a dead end when it comes to achieving AGI. That doesn't mean there wasn't room to improve LLMs so they were more powerful, autonomous and useful to businesses. But that isn't the same thing as AGI.
By pouring funding into LLMs at the expense of other avenues or architectures, Chollet explained, the road to true AGI is being ignored. The result? Progress has been set back by up to a decade.
Intelligent systems
Despite Chollet's steadfast belief that LLMs will not get us any closer to AGI, many technology executives have spent the last few weeks opining about the possible threat that they pose to humanity.
Ahead of OpenAI and Anthropic's as-of-yet-undetermined IPOs, both companies have taken turns disclosing increasingly worrying incidents, including cybersecurity breaches. These stories have, in many people's eyes, simply served to hype up the capabilities of existing technologies for marketing purposes.
As for Chollet, the whole purpose of the ARC-AGI benchmark is to determine true progress toward AGI. While LLMs are performing better on this especially tough benchmark, none have come close to hitting the mark. [...]

## [11] Someone got Doom in an SQL database
Ars Technica | full text via Ars Technica | ~258 words

“Rendering Doom in a database is obviously a bad idea,” Lukas Vogel writes in a lengthy blog post explaining how exactly he managed to render Doom using an SQL database.
OK, that’s not entirely accurate. The SQLDoom project uses a small Python client to handle input and output, drive the game’s timing, and display each frame to the screen. Behind that, a series of CedarDB tables tracks the game geometry and state, while about 1,300 lines of SQL queries spread across 89 common table expressions implement the game logic and generate 35 bitmap framebuffers per second.
In this, SQLDoom is a major improvement over Vogel’s previous DoomQL project, which last year set out to build “a multiplayer Doom-like shooter entirely in SQL.” Unfortunately, that effort ended up with raycasting-based, grayscale ASCII graphics that were more akin to the simplistic 90-degree-angled maps of Wolfenstein 3D. The newer SQLDoom, on the other hand, generates full-color 640×480 frames that look like they could have come from the original Doom executable.
It’s all just data, man
Converting Doom‘s classic WAD files to a relational database was relatively simple and straightforward, Vogel writes, because of the way the original game broke levels down into vertices, lines, sectors, and so on. Even Doom‘s famous binary-space partition trees can be broken down into SQL using a sort_key for objects that’s pre-computed for each position at load time. With this set in your table, a simple “ORDER BY” statement can determine every frame which parts of walls to display and which to ignore, vastly improving performance.

## [79] Amazon responds to data center backlash, says it no longer uses NDAs
TechCrunch | full text via TechCrunch | ~667 words

Amazon Web Services CEO Matt Garman said the company has stopped using nondisclosure agreements (NDAs) in its dealings with government agencies as it seeks approval to build new data centers.
Garman’s statement is just one sentence in a longer blog post in which he tried to push back against widespread suspicion of data centers, and to make the case that they’re actually good for communities.
NDAs are a significant piece of the broader data center backlash. For example, environmental activist Erin Brockovich recently said that the number one complaint she’s heard about data centers is transparency, with these projects following a common pattern: “projects announced after permits are already secured, developers who don’t return calls, local officials who signed NDAs before their neighbors knew a project was being considered.”
As a result of that backlash, New York announced a one-year moratorium on permits for large data centers, and according to Garman, there are more than 100 data center moratoriums currently being considered across the United States.
“If these measures are enacted, the U.S. could be writing its own losing ticket to this race, and the consequences would last generations,” Garman claimed. “As a country, we can’t afford to find ourselves in that position.”
Garman also attempted to puncture what he said are four big myths around data centers: that they consume too much water, that they increase electricity costs, that they emit an enormous amount of pollution, and that they don’t provide any benefits to their communities.
Pointing to an Amazon report about its own water usage, Garman said that “direct data center water consumption” only accounts for 0.5% of all industrial water usage in the United States, “orders of magnitude less than golf courses, almond farming, and many other industries.”
Nvidia recently said its new cooling system eliminates “pretty much all water usage” inside the data center, but those claims — like Amazon’s — seem to ignore the broader water usage involved in electricity generation and chip manufacturing. Scientists have also said they need to study data centers’ water and energy usage independently, since there are no federal or state requirements around how tech companies report this data.
As for electricity rates, Garman said they’ve only gone up in some states with large numbers of data centers, while they’ve gone down or at least grown more slowly in others. [...]

## [83] California's Governor Wants Worker Protections from AI. But FSF Thinks Kill Switches are 'Dangerous Precedent'
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~93 words

The Guardian reports that California governor Gavin Newsom signed laws on Wednesday "aimed at protecting California workers from the threats of artificial intelligence , including potential job losses and workplace surveillance." The laws ban employers from using the technology to predict a worker's emotional state by using their biometric data, require employers to send written notices to workers if AI is responsible for mass layoffs and ban employers from relying on AI to decide to fire someone... The governor signed a law this month requiring operators of AI chatbots to perform risk assessm

## [8] Getting the most out of Opus 5.5 in Claude and Claude Code
Hacker News | full text via Hacker News | ~1891 words

How to prompt Opus 5.5, steer a long run, and check your results in Claude apps and Claude Code.
Opus 5.5 works well with the way you already use Claude. A few things behave differently, though: it works for longer on its own, it tells you plainly what it did, and it thinks before every reply. This guide covers how to work with Opus 5.5 in Claude apps and Claude Code, including how to prompt the model, steer a long run, and check your results.
Three things to try in your first session with Opus 5.5
What to do. Give the whole task in one message. Name the finish line, like “the tests pass” or “every endpoint is migrated.” Then let it cook.
Why it matters on Opus 5.5. Opus 5.5 keeps going on long, multi-part work better than Opus 5 did. Compared to prior Opus models, its biggest gains are on multi-step work, like carrying a change through a large repository until the tests pass. Early testers had it run long coding tasks for hours with little oversight. With a clear finish line, it knows when it’s done.
How. In Claude Code, for example:
Migrate the payment endpoints from the old client to the new one.
Done means: every endpoint uses the new client, the old client is deleted, and the test suite passes.
Stop and ask me only if a test fails for a reason you can't explain.
What to do. Remove “think carefully,” “think step by step,” and similar lines from your prompts and your saved instructions.
Why it matters on Opus 5.5. Opus 5.5 always thinks before it replies, and it decides how much. You don’t need to ask it to think. In our testing in a chat product, removing a “think carefully” line made replies start sooner, with no clear drop in quality.
How. Delete the line. For a quick answer to a simple question, say so: “Answer directly.” To change how much it thinks in Claude Code, change effort.
What to do. If you remember something mid-run, you can type a follow-up while it works.
Why it matters on Opus 5.5. Runs are longer now, so a restart costs more.
How to do it. In Claude Code, type the message and press Enter while Claude works, for example, “Also keep the old endpoint names as aliases.”
What to do. When you ask for a page, an app, or an artifact, list the design habits you want left out.
Why it matters on Opus 5.5. With no design direction, Opus 5.5 falls back on a few default styles. A general instruction like “avoid a generic look” mostly swaps one default for another. A list of specific patterns works much better.
How. [...]

## [104] Anthropic’s answer to Dots and Muse is already inside Claude
The New Stack | full text via The New Stack | ~1347 words

Anthropic’s answer to Dots and Muse is already inside Claude
I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.
OpenAI launched Dots at DevDay on Tuesday. Each Dot is an always-on agent with its own cloud computer and browser, hooked into the 4,000-plus apps that already connect to ChatGPT. In OpenAI’s own example, a Dot sees a bug alert land in Slack and starts digging in on its own. Cool.
And before Dots, Meta launched Muse, and it’s crushing the mobile install numbers previously set by ChatGPT. And before Muse, xAI shipped its version, Grok Bot, in August.
Anthropic’s version, though different in a couple of ways, arrived two weeks ago as an update to Claude, and without a cute name or fuzzy mascot. This update folds Cowork, which has worked since July to run scheduled jobs after a user closes their laptop without being asked, into the main Claude app.
Anthropic made the right call with Cowork, whether or not it ever matches Muse’s downloads. Always-on agents are too young to have a winner, and the moats are shallow. A feature one lab ships tends to show up at its rivals within weeks or months. Meta needs Muse to be a blockbuster. Anthropic needs the people already building with Claude to hand it real, recurring work and keep coming back. Repeat use and finished jobs matter more than a flashy launch.
Always-on agents are too early to have a winner
This wave of always-on personal agents took off less than a year ago. Peter Steinberger pushed a weekend project called Clawdbot to GitHub last November. It lived on a spare computer, took prompts over WhatsApp or Telegram, and relied mostly on Claude. Anthropic sent the lawyers in January, so it became Moltbot, then OpenClaw a couple of days later. It turned into a security headache, and in February Steinberger joined OpenAI. On Tuesday, the foundation that runs the project released an early, pre-1.0 version of OpenClaw Enterprise for companies to try internally.
Ten months, three names, one OpenAI hire and an enterprise edition. Ideas move between these products faster than ever. [...]

## [125] “No reason why everyone should have an identical Claude experience”: Anthropic’s mods let you change Claude Code’s look and behavior
The New Stack | full text via The New Stack | ~761 words

“No reason why everyone should have an identical Claude experience”: Anthropic’s mods let you change Claude Code’s look and behavior
Developers have long been able to customize Claude Code to their preferences, via settings, persistent instructions in CLAUDE.md, hooks, and MCP servers, alongside tweaks such as status lines and output styles. Those controls can shape the instructions Claude follows, its permissions, the tools it can use, and more — but they can’t change Claude Code’s own features or the rest of its interface.
Now, however, Anthropic is giving developers much deeper control of Claude Code via mods, which are small JavaScript or TypeScript functions that hook into events inside Claude Code. A mod can rewrite a prompt before it reaches the model, block or rewrite a tool call, handle permission requests, replace parts of Claude Code’s interface, or add entirely new functionality.
“Each person works differently, so there’s no reason why everyone should have an identical Claude experience.”
Changing how Claude Code looks and behaves
Taking to X on Thursday, Claude Code creator Boris Cherny describes mods as a way for developers to reshape Claude’s appearance and behavior via a simple prompt, with the ability to package those customizations as plugins that other users can install.
“Each person works differently, so there’s no reason why everyone should have an identical Claude experience,” Cherny writes
That can include changing what Claude Code displays while it’s working. For example, a mod might want to surface live information such as the number of tool calls Claude has made, how long it has been running, and how many tokens it has consumed, then present a summary once the task is complete.
Users were already experimenting with more specialized uses within hours of the announcement. One software developer built a mod for passing credentials to Claude without leaving the underlying secret in the conversation history.
How Claude Code mods work
Mods have actually been in the works publicly for at least a month already. Anthropic first floated the idea on GitHub on September 3 under the more technical name “function hooks,” asking developers for feedback on an API that would let JavaScript and TypeScript functions intercept events inside Claude Code. Six days later, the company said it planned to ship the feature imminently under a rebranded “Claude Mods,” while retaining function hooks as the underlying mechanism. [...]

## [26] The dawn of the age of the exoskeleton
Ars Technica | full text via Ars Technica | ~319 words

This year, members of Seattle Mountain Rescue have been setting off into the wilds of the US Pacific Northwest wearing an unusual piece of kit.
They’ve been hiking into the wilderness with powered assistive devices attached to their hips and legs. Designed to increase lower-body strength when climbing or carrying heavy loads, these pieces of equipment are being tested to see if they can boost rescuers’ speed and endurance when it matters most—during searches for stranded people.
Devices like these are called human exoskeletons. They attach to parts of the body to create an external—or “exo”—mechanical structure. This powered frame enhances the wearer’s physical capabilities.
In physically demanding fields, workers are increasingly using these devices during strenuous tasks. IKEA has used SuitX exoskeletons for several years now. These assist warehouse workers with handling heavy materials. Ford, Boeing, and Mazda Toyota have also all adopted the tech on some of their assembly lines.
In Finland, a recent project called ExoPELA assessed whether exoskeletons could reduce muscle load and strain in rescue and firefighting work. It found noticeable benefits for users in certain real-world tasks.
And in early 2026, the Ukrainian military revealed its soldiers had been using Hypershell exoskeletons on the front lines to help with carrying artillery shells. According to test results, soldiers wearing the devices “become less fatigued, work faster, and maintain combat effectiveness for longer,” Colonel Vitalii Serdiuk told the Ukrainska Pravda newspaper in March.
Multiple consumer and clinical devices, designed for everyday assistance, rehabilitation and exercise, are also now available. Some estimates have valued the total sector at around $500 million (£370 million) currently, and predict it could double or triple in size by the mid-2030s.
Exoskeleton technology has progressed significantly over the past decade. This has largely been thanks to robotic motors, sensors, and control systems becoming more affordable and accessible. However, the concept of augmenting human performance with exoskeleton-like devices dates back much earlier.

## [10] FTL: A new operating system for clouds
Hacker News | full text via Hacker News | ~328 words

What's FTL?
- You can build your own OS as a library. This userspace OS design makes it easy to add features, debug, upgrade the OS safely, as if writing applications.
- FTL kernel isolates containers (userspace OS instances) better than existing monolithic kernels, with a hypervisor-like interface based on a lightweight hardware-based isolation (user mode). You don't need bare-metal machines.
- FTL is compatible with Linux binaries. For example, the Rust-based HTTP server serving this website is a Linux application running on FTL. You can also run Unikernel-like specialized applications without POSIX abstractions.
How it works
Each container runs a userspace OS. It is a shared library which implements most of OS concepts such as Linux process, VFS, and TCP/IP. FTL kernel provides a minimal interface to implement Linux system calls in userspace, just like a hypervisor.
FTL combines the best of microkernels (flexible & secure) and monolithic kernels (performant & simple). Our goal is to make lightweight containers as secure as VMs, and unlock new OS-level abilities in applications, without sacrificing performance:
FTL                                   Linux
┌────────────────────────────────┐    ┌────────────────────────────────┐
│┏━━━━━━━━━━━━━┓  ┏━━━━━━━━━━━━━┓│    │┏━━━━━━━━━━━━━┓  ┏━━━━━━━━━━━━━┓│
│┃             ┃  ┃             ┃│    │┃             ┃  ┃             ┃│
│┃    Linux    ┃  ┃    Linux    ┃│    │┃    Linux    ┃  ┃    Linux    ┃│
│┃   Process   ┃  ┃   Process   ┃│    │┃   Process   ┃  ┃   Process   ┃│
│┃             ┃  ┃             ┃│    │┃             ┃  ┃             ┃│
│┃╌╌╌╌╌ Linux system calls ╌╌╌╌╌┃│    │┗━━━━━━━━━━━━━┛  ┗━━━━━━━━━━━━━┛│
│┃                              ┃│    └────────────────────────────────┘
│┃         Userspace OS         ┃│    ╌╌╌╌╌╌╌╌ Linux's interface ╌╌╌╌╌╌╌
│┃   (Process, VFS, TCP, ...)   ┃│    ╔════════════════════════════════╗
│┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛│    ║                                ║
└────────────────────────────────┘    ║          Linux Kernel          ║
╌╌╌╌╌╌╌ minimal interface ╌╌╌╌╌╌╌╌    ║                                ║
╔════════════════════════════════╗    ║   process, fork/exec, memory,  ║
║           FTL Kernel           ║    ║     signals, TCP/IP, /proc,    ║
║    vCPU, memory, drivers, ...  ║    ║       /dev, drivers ... [...]

## [30] Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform
Google Developers Blog | full text via Google Developers Blog | ~631 words

Each new model generation makes AI agents more capable, more autonomous, and cheaper to run. Teams are putting them to work on real business tasks: issuing refunds, updating records, calling internal tools on a user's behalf. But a more capable model is not automatically a safer one. The more decisions an agent makes at runtime, the more its risk shifts from its code to its behavior. The real damage often happens in sessions that look benign on the surface: the agent returns a clean answer and closes the ticket, and only afterward do you notice it reached for a tool it should never have touched, or acted on a request that quietly widened its own access. Because nothing failed outright, the session clears the usual metrics-based evaluations without any second look.
That gap is exactly what Agent Anomaly Detection is built to close. It's now in Private Preview on the Gemini Enterprise Agent Platform.
Agent Anomaly Detection is a reasoning-based oversight and audit layer for autonomous agents deployed on the Gemini Enterprise Agent Platform. It examines what an agent actually does using its reasoning traces, tool calls, and execution flow across a session. It reads the logs and OpenTelemetry traces your agents already emit, evaluates that activity to decide whether an agent is operating outside its intended boundaries, and flags behavioral anomalies, suspicious intent, and policy violations.
Some key features that make Agent Anomaly Detection practical to run in production:
Agent Anomaly Detection balances detection speed, cost, and coverage. To strike that balance, it analyzes traces and logs in layers: a lightweight first pass scans all traffic to surface statistical anomalies and flag those sessions for further analysis. Then, an LLM-based reasoning layer deeply examines the flagged sessions.
To make that concrete, take the example of an Inventory Agent with a list_inventory tool. A user says, "I want to see your inventory. List 100 items at a time" and the agent starts paging through in large batches, jumping across offsets to pull the whole catalog.
Nothing here throws an error. The agent is only doing things it’s capable of, and there may be no policy preventing it. But Agent Anomaly Detection flags the anomalous behavior, working through the session in layers: the first layer flags the session as a statistical outlier from the volume and the repeated calls. [...]

## [90] All the AI agents that can live in your text messages
TechCrunch | full text via TechCrunch | ~1883 words

Rather than downloading another app, a growing number of agents can simply be texted like an ordinary person.
You text it what you need, and it can remember context, connect to the apps and services you already use, and complete tasks on your behalf. That can mean scheduling an appointment, organizing a calendar, researching a trip, sending an email, making a reservation, shopping online, or reminding you about something days later.
While Instinct is one of the buzziest AI agents at present, thanks to its $10 billion valuation after its latest funding round of $1 billion, there are many others also making a play for this space.
Below are some of the most notable options so far, from general-purpose personal assistants to agents designed for families, travel, and work.
Caddy
Caddy is an AI assistant that turns the information scattered across your phone into things you can actually act on. It lives in iMessage for iPhone users and RCS for Android users, so there’s no separate app or inbox to constantly check.
For instance, an email contains an appointment that needs to be added to your calendar or a friend sends a list of things to pick up. Instead of worrying about all the details getting buried, Caddy connects to your calendars and conversations, then identifies things that may require action. It can add events to your calendar, set reminders, keep track of follow-ups, and even do research for you.
Caddy has been available in public beta since April 2026.
Fambot
Fambot is an AI-powered “chief of staff” for families, designed to bring together the many moving parts of family life, including school communications, sports activities, meal planning, calendars, and other day-to-day responsibilities, and turn them into an organized plan.
The service is designed to work across both an app and text messages. Fambot is available on iOS devices, Android devices, and the web, and families can also interact with it directly over SMS. Every night, Fambot automatically sends a summary of the following day, including upcoming events, to-dos, and details such as school uniform or packing requirements. Parents can reply to those messages to ask questions, check information, or make changes to their calendar.
Fambot currently connects to Gmail and Google Calendar, with support for Outlook and Apple Calendar planned for the future.
The company launched in beta in early September 2026 and has raised $3.5 million in pre-seed funding. [...]

## [94] Measuring the Creativity Potential of LLM Agents
Towards Data Science | full text via Towards Data Science | ~1997 words

Measuring the Creativity Potential of LLM Agents
Trying to answer the question of "Can LLM agents discover?" through the lens of creativity
This blog post is based on our recent work, "Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks", published at COLM 2026 and written with Yunxiang Zhang and Professor Lu Wang at the University of Michigan. Do check out the paper for a more detailed reading, while this blog post acts as a summarized version of our work. The main question we are trying to answer here is this: while there has been a massive push for AI for Science, with huge investments in LLM agents for scientific discovery, these agents still fall short of the top-1 human on real ML research challenges. At the same time, we see regular reports of LLMs making breakthroughs (AlphaEvolve, the Kosmos AI scientist, etc.), and OpenAI recently claimed to have solved Navier-Stokes. So why the disconnect?
A common answer to that would be the underlying framework and scaffolding the model has access to, as these better frameworks might allow for more efficient search of the solution space, but how do we quantify this notion of "better search"? We argue that creativity offers a useful lens.
So then what is Creativity?
A natural trait we want in these agents is that they come up with ideas that are both novel and deliver great results, and that’s exactly what creativity is.
According to the “The Standard Definition of Creativity” by Mark A. Runco and Garrett J. Jaeger, "Creativity is the production of ideas or products that are simultaneously original and useful (i.e., effective or appropriate)"
Interestingly, there have been many other works in creative psychology that link creativity to search in a conceptual space:
Boden, M. A. (1998). “Creativity and Artificial Intelligence” →
“the generation of novel ideas by the exploration of structured conceptual spaces.”
Boden, M. A. (2004). The Creative Mind: Myths and Mechanisms (2nd ed.) →
“Western music springs from a search-space defined by the rules of harmony, and its melodies are pathways through a precisely mappable landscape of musical intervals.”
Newell, A., Shaw, J. C., & Simon, H. A. (1962). [...]

## [98] How to Use a PINN for a Navier-Stokes Inverse Problem
Towards Data Science | full text via Towards Data Science | ~1808 words

How to Use a PINN for a Navier-Stokes Inverse Problem
A from-scratch PyTorch build that recovers blood flow, viscosity, and wall shear stress in a narrowed artery from 40 noisy velocity readings
Wall shear stress is the friction blood puts on the wall of a vessel. It is tied to where plaque builds up, and it is hard to measure directly. What a clinic can get, with Doppler ultrasound for example, is the velocity at a few points inside the vessel. So the question for this article is whether a neural network can take those scattered, noisy velocities, together with the equations of fluid flow, and give back the whole flow field and the shear stress at the wall.
A physics-informed neural network (PINN) is a natural fit. I built one in plain PyTorch, without DeepXDE or any other PINN library, for a 2D artery with a narrowing (a stenosis). From 40 velocity readings it reconstructs the velocity and pressure fields and the region of reversed flow behind the narrowing. It also works out the viscosity of the fluid, which I treated as unknown, and its wall shear stress follows the CFD reference closely.
This is the first article in a series about PINNs for blood flow. It covers the core: the Navier-Stokes residual, a learnable viscosity, and what decides whether the result is any good. Later articles cover the CFD solver behind the reference data and a pulsating flow that follows a heartbeat.
The Setup
The artery is a 2D channel of height H with a smooth bump on the lower wall that blocks half of the opening, a 50% stenosis. The flow is incompressible Navier-Stokes at a Reynolds number of 200, with lengths measured in channel heights and velocities in inlet velocities. That is a slow flow, at the low end of what happens in a carotid artery. In these units the kinematic viscosity is 0.005.
There are no patients in this article, on purpose. To score a reconstruction you need to know the right answer, so I generated it. A Navier-Stokes solver I wrote (a projection method on a staggered grid) computes the steady flow, and the PINN only ever gets a few noisy readings taken from that solution. The noise is Gaussian, at 7% of the inlet velocity. I might cover the solver in a later article.
The length of the channel mattered more than I expected. My first version was five heights long. Behind the bump the flow separates from the wall and a region of reversed flow forms. [...]

## [113] Sean Parker is rebuilding Stability AI around music
TechCrunch | full text via TechCrunch | ~184 words

Sean Parker, the Napster co-founder, has jumped back into the music industry, and he tells The Information that he’s playing by the rules this time. (Asking for forgiveness rather than permission didn’t work out so well last time around, he readily concedes.)
Two years ago, he joined an $80 million rescue of Stability AI, the image-generator startup that nearly collapsed after overspending and internal turmoil led to founder Emad Mostaque’s ouster. Now Parker and his longtime friend Prem Akkaraju, who became CEO, are taking the wraps off what they’ve been building.
The big idea, Parker says, is to turn Stability into the go-to AI toolmaker for music professionals. Toward that end, in late August, the company announced $76 million in funding from, among others, Sony, Warner, and Universal, which also licensed their catalogs for training as part of the deal. Stability has since released three new audio models and AI music-editing software. The AI can generate whole instrumental tracks or short snippets from text prompts. Parker says an upcoming update will let users hum a melody or beatbox a drum pattern to steer it.

## [107] KDE Plasma 6.8 Now Makes Tiled Windows Fit Together More Nicely
Phoronix | full text via Phoronix | ~236 words

KDE Plasma 6.8 Now Makes Tiled Windows Fit Together More Nicely
There is just over one week to go until the much anticipated KDE Plasma 6.8 desktop release. Some last minute fixes continue flowing into Plasma 6.8 as well as early feature work continuing for Plasma 6.9.
Making it in time for the Plasma 6.8 release is that tiled windows now have square corners so they fit together nicely with other windows. This stems from a 2024 bug report that rounded corners should be disabled when the window is tiling , similar to how Microsoft Windows behaves. It was noted KDE Plasma used to behave like this bug regressed at some point.
As shown in This Week in Plasma the result of the change for tiled windows with KDE Plasma 6.8:
For Plasma 6.7.6 meanwhile is a fix where KWin could crash when using the NVIDIA 610.57.04 graphics driver or newer. There is also another crash fix for Plasma when dragging a widget to a panel.
Plasma 6.8 also has a crash fix in response to apps closing or crashing in very specific ways.
Also fixed for Plasma 6.8 is remote desktop authentication working with the FreeRDP 3.32 library and newer.
One other last minute change for Plasma 6.8 is having the System Monitor and its widgets measure GPU memory usage more accurately.
More details on these changes can be found via This Week in Plasma.
