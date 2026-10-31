# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Backdoor in Claude Code for VS Code extension on the Cursor Marketplace
Hacker News | full text via Hacker News | ~2420 words

TL;DR
Phorion has detected a backdoor in the official Claude Code for VS Code extension bundle on the Cursor Marketplace that drops a persistent SSH backdoor across macOS, Linux, and Windows. This write-up focuses primarily on macOS, where the extension attempts to configure an SSH backdoor and establish persistence.
Organisations should immediately review their environments for use of Claude Code for VSCode 2.1.312 or 2.1.313 and engage incident response where use of the extension is discovered.
Update (31 October 2026): Cursor’s security notice now identifies versions 2.1.312 and 2.1.313 distributed through the Cursor Marketplace for macOS and Windows as affected. This advisory previously identified only 2.1.313; the affected-version guidance below has been updated accordingly.
Phorion has discovered a compromise of the official Claude Code for VS Code extension on the Cursor Marketplace, where the backdoored extension bundle contains a persistent Secure Shell (SSH) backdoor. Cursor has removed the affected versions, 2.1.312 and 2.1.313, from its marketplace.
While the implant includes setup and persistence logic for macOS, Linux, and Windows, we’re going to focus primarily on macOS in this post, calling out the key differences and a few implementation bugs on the other platforms along the way.
The Cursor Marketplace serves extensions for the Cursor editor. Because extensions run with the permissions of the IDE and the user running it, a backdoored extension gets immediate access to local files, source code, and developer tooling as soon as its module is loaded.
Notably, Phorion has discovered a likely oversight in how the malware tries to turn on SSH. The setup logic assumes it can check the current Remote Login state without root privileges. When run as a standard user, systemsetup -getremotelogin prints an administrator-access error and exits with status 0 instead of returning Off. Because the script only tries to enable SSH if the output matches Off, it skips the enablement step entirely. On a Mac that doesn’t already have SSH running, that mistake breaks the inbound access path, even though the SSH keys and persistence still get dropped.
In this post, we’ll walk through how the backdoor works, why that macOS check fails, and what to look for across your fleet. [...]

## [9] The $6.3B Binance hack was pulled off in just 20 minutes
Hacker News | full text via Hacker News | ~948 words

Cryptocurrency firms and investigators are racing to freeze and track down billions of dollars of stolen digital cash following what appears to be the largest crypto heist of all time. On Thursday, starting at around 4pm ET, hackers started quickly siphoning around $6.3 billion in cryptocurrencies, spread across multiple blockchains, from wallets belonging to crypto exchange Binance.
Following the theft, Binance almost immediately suspended all deposits and withdrawals from its services as part of its investigation into the hack and says it is working to identify who was behind the breach. The company, along with other crypto firms, says it has so far been able to freeze around half of the stolen funds—essentially stopping hackers moving the money further or trying to cash it out. Much of the remaining crypto may not be possible to freeze, however.
Three crypto tracing firms have been quick to link the attack potentially to North Korean hackers. “We think North Korea is likely responsible,” Tom Robinson, chief scientist and cofounder of Elliptic, tells WIRED. “If North Korea is behind it, this one theft would almost double everything the regime has stolen in crypto to date.”
The majority of the stolen crypto was taken in a period of around 20 minutes on October 29, according to analysis by crypto tracing firm TRM Labs. Wallets belonging to Binance across at least ten blockchains—including Ethereum, Bitcoin, Tron and Solana—were drained and sent to multiple addresses controlled by a single attacker, according to TRM’s analysis. “Preparation began at least 36 hours before the theft,” TRM says in a blog post. The company says one of the attacker’s wallets received three small withdrawals during a test period, before later expanding the operations.
“Early on October 29, the operator deployed a first piece of code for the attack and tested it on two wallets,” TRM says. “Later that day, it rehearsed the final version on a third wallet, then routed the test funds back to itself. Four hours after that rehearsal, the same code was installed on a Binance hot wallet.” Hot wallets are cryptocurrency wallets that are internet connected and allow crypto exchanges to handle customer withdrawals. Analysts say the funds were drained from hot wallets across the impacted blockchains.
The tactics used in the hack appear to mimic previous methods used by an elite subset of North Korean hackers, known by the name TraderTraitor. [...]

## [13] Azure's Weakest Link – Five Full Cross-Tenant Compromises
Hacker News | full text via Hacker News | ~2043 words

Azure's Weakest Link - Five Full Cross-Tenant Compromises
In my previous blog posts, Azure’s Weakest Link? and Azure’s Weakest Link - Full Cross-Tenant Compromise, I gave an overview of the severely insecure architecture behind API Connections in Azure, a part of Azure Logic Apps, and an instance of a full cross-tenant compromise using these inherent flaws. Now I am back with some more vulnerabilities in this system, each giving the same primitives to the attacker. In total, the vulnerabilities here netted me a cool $200,000.
I also held a talk detailing this at Blue Hat Asia 2026, and when the recordings are out, I will add a link here.
TL;DR
API Connections allow anyone to fully compromise any other connection worldwide, giving full access to the connected backend. This includes cross-tenant compromise of Key Vaults and Azure SQL databases, as well as any other externally connected service, such as Jira or Salesforce. The only thing stopping exploitation is really the layers of input validation bolted onto the various systems, but as you will see, it is really difficult to catch all the edge cases here.
Architecture
If you haven’t read the first parts of this series, I would recommend checking those out first, Azure’s Weakest Link? - Part 1 and Azure’s Weakest Link - Full Cross-Tenant Compromise, but if you don’t care, I will go through the most important parts of the architecture first.
From Microsoft’s documentation, we see a quite intriguing diagram of how the API Connection architecture is built.
This basically spells out all that is needed to understand how the system operates, kudos to whoever made it!
It works like this
- A logic app, the symbol on the bottom left, queries a shared Azure API Management instance
- The API Management instance first checks the swagger (OpenAPI) definition of the connector type and checks that it is a valid action
- A sort of key exchange happens where the input token, or key, is exchanged for the configured token for the backend service
- The API Management instance finishes the call with this new token to the backend instance.
From this, we can surmise that if we are able to trick the API Management instance to operate on a different connection than the ones we own, we would be able to effectively use the configured token for a victim’s connection on their backend service.
This service can, in effect, be anything. [...]

## [6] Northflank Breached
Hacker News | full text via Hacker News | ~264 words

We have enabled audit logs for all customers, including free users.
Update · October 30, 2026 at 11:38 PMUTC
Users have reported unauthorised use of AI API keys supplied to the Northflank platform.
If you have not already rotated your user-provided secrets stored in Northflank, please do so immediately. Revoke existing credentials with their issuing providers, generate replacements, and update the affected secrets and workloads in Northflank. Review your AI provider usage and billing logs for unexpected activity, and report any suspicious usage to Northflank support and the relevant provider.
These reports may be consistent with the broader pattern of attacks targeting AI credentials. Similar IP addresses are contained in this article Wiz’s “Black October” report.
Update · October 30, 2026 at 7:28 PMUTC
Our investigation is ongoing. We have no further confirmed findings to share at this time.
Our guidance remains unchanged: assume all environment variables have been compromised and rotate all secrets and credentials immediately, including those in workloads, secret groups and global secrets. Disable public access to addons where enabled.
We will share further updates as more information is confirmed.
Update · October 30, 2026 at 3:12 PMUTC
Secret rotation on Postgres and MongoDB has been enabled for all users. We recommend disabling public expose on addons if you have enabled that.
All users should assume their environment variables are decrypted and begin rotation immediately.
Secrets on workloads
Secret groups
Global secrets
Multiple users are confirming that their AI keys have been used.
Identified · October 30, 2026 at 1:58 PMUTC
Assume all environment variables have been decrypted. Disable/rotate all keys.

## [10] Bunny CDN Security Incident
Hacker News | full text via Hacker News | ~407 words

We're reaching out to inform you of a security incident involving one of our infrastructure providers, the steps we've taken, and what this means for you.
- What happened and how we responded
Last week, one of our infrastructure providers reported unauthorized access involving third-party server management software. One of our CDN nodes, located in Armenia, was hosted on a server supplied by this provider.
After receiving the alert from the affected provider, our engineering team took immediate action. Within 20 minutes, we stopped routing traffic through the server. We then reviewed and preserved the relevant security logs for investigation, securely wiped the server, and revoked its access to our other systems. The affected server has been permanently removed from our infrastructure.
Our investigation found no evidence of unauthorized access to the CDN node or any of its data. The infrastructure provider has also found no evidence that our server was accessed, but continues to investigate the incident.
- What this means for your data
While neither investigation has found any indication of unauthorized access to our server, we cannot completely rule out the possibility.
If unauthorized access to our CDN node did occur, the potentially exposed information would have been: temporarily cached CDN content, Pull Zone configurations, and TLS certificates stored on that server.
As an additional precaution, we have revoked and reissued all TLS certificates for bunny.net platform domains (b-cdn.net and bunny.run). Reissuance of managed TLS certificates for custom domains is ongoing and is expected to be completed within the next 24 hours. No action is required from customers using managed certificates. We will post a further update on our status page once this process is complete.
If you manage your own TLS certificates, we recommend revoking and reissuing them with new private keys as a precaution.
No other customer data, including bunny.net account data, was stored on the server in question, and no internal systems were affected.
- What happens next
We’re closely monitoring our infrastructure and working with the affected provider as the investigation continues. Should any new findings affect our customers, we will provide an update via email and on our status page.
At bunny.net, we understand the trust you place in us to keep your content secure, and we take that responsibility seriously. [...]

## [71] AI can turn security fixes into working exploits before users receive an update
TLDR AI | full text via TLDR AI | ~2624 words

Overview
GLM 5.3, a widely available open-weight model released by Z.ai in August, can identify and exploit vulnerabilities in recent versions of the Mozilla Firefox browser using security fixes that have been published but not yet shipped to users. The window between a fix being published and reaching users is known as the patch gap.
In our experiments, GLM 5.3 used this gap to build a webpage that, when visited by a Firefox user, read a file from the visitor’s computer and sent it to the attacker with no further user interaction. In particular, we found that any Firefox version released between September 17 and October 26 could be compromised in this way using only information available at the time of release.
The patch gap is a known weakness in software release practices, and it exists widely across software, e.g., browsers, phone operating systems, and router firmware. Exploiting it previously required significant time and expertise, or special access to frontier models with advanced cyber capabilities, so few attackers could target these vulnerabilities before they were fixed.
Our central finding is that widely available open-weight models can now do much, or even all, of this work on their own. We deliberately designed our setup to emulate what a relatively unsophisticated actor with limited resources could achieve, using only information available at the time of each version’s release. Once set up, it cost only about $1,000 to successfully attack each Firefox version.
In all of our compromises of recent Firefox releases, GLM 5.3 also found and used an unpublished vulnerability in conjunction with those found via the patch gap. We contacted the Mozilla team to disclose our findings and discuss ways to mitigate these attacks. Mozilla has since shipped a new version of Firefox (159.0, released on October 27, 2026) that patches the previously undisclosed vulnerability, which should make it more difficult for GLM 5.3 to compromise Firefox via patch-gap exploits.
Open-source projects are particularly vulnerable to this kind of attack as their code is publicly available, but we suspect any software project where a model can find the content of upcoming security changes before release is vulnerable, including closed-source projects.1 We anticipate this threat vector will worsen as open-weight cyber capabilities continue to improve.
Further findings from our experiments on Firefox:
- GLM 5.3 exploited the patch gap despite existing countermeasures. [...]

## [150] Applebee’s exposed customers’ personal data after leaving database password in app
TechCrunch | full text via TechCrunch | ~607 words

Applebee’s has fixed a security flaw that allowed anyone to access the personal information of its registered customers, after a researcher found a password for an internal database inside Applebee’s mobile app, TechCrunch has learned.
The popular restaurant chain confirmed on Thursday that it had taken action to address the security issue to prevent any unauthorized access to its customer database.
TechCrunch withheld publication of this story until the bug was confirmed to be fixed.
Robert Wiggins, a U.K.-based cybersecurity researcher at What Security, discovered the security lapse earlier this month. Wiggins is no stranger to discovering security issues, including exposed or sensitive information that should not be publicly accessible.
For this latest discovery, Wiggins used AI to help find the credential buried inside thousands of lines of source code in Applebee’s Android app, which has more than a million downloads on Google Play. The credential allowed access to the company’s customer database.
Storing a password or private key in software, known as hardcoding credentials, is one of the most severe types of security vulnerabilities because anyone with the app can extract the key and use it to log in to a remote system as if they were an authorized user.
Wiggins said that the hardcoded credential could have also allowed a malicious attacker to modify customer data in the database.
TechCrunch verified Wiggins’ findings by downloading and decompiling Applebee’s Android app to examine its source code and confirm that it contained the exposed credential. We also created an Applebee’s account with dummy account data, which allowed Wiggins to retrieve our information from the company’s database.
The exposed database contained customer names, email addresses (including whether or not the customer verified their email), dates of birth, phone numbers, and ZIP codes. The data also included veteran status, the number of times customers had logged in, when their accounts were created, and the IP addresses of their most recent log-ins, which can be used to reveal the person’s approximate location.
Wiggins was unable to alert Applebee’s or its parent company, Dine Brands, as neither have ways to report security issues. Wiggins asked TechCrunch for help in disclosing the security issue to the company. [...]

## [47] Making it easier for websites to express AI training preferences
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~19 words

OpenAI will honor a shared robots.txt signal to help website operators communicate their AI training preferences to participating providers.

## [81] The Web Can't Afford a JavaScript Runtime Monoculture
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1237 words

Earlier this month Deno announced its whole team is joining Cloudflare. In the announcement, Ryan Dahl, who created Node.js and started Deno in 2018, also explains that development of the Deno runtime will stop after one year. That leaves the web with two major general-purpose runtimes, the OpenJS Foundation’s Node.js and Anthropic’s Bun, alongside Cloudflare’s runtime, workerd, which is built primarily for its own Workers platform. As someone who studies web dev tools, this concerns me.
Remember Internet Explorer 6? Microsoft released it in 2001; it won roughly nine in ten browser users, and then MS largely stopped working on it. With no serious rival, there was no reason to improve and so, for about five years, developers were forced to write for one browser’s quirks rather than for open standards, and “best viewed in Internet Explorer” badges were everywhere.
When this situation became intolerable the market responded with alternatives. Mozilla’s Firefox grew out of the wreckage of Netscape, and Apple built Safari on an open-source engine called WebKit. Then Google’s Chrome arrived in 2008. Competition returned, and the pace of improvement returned with it.
But this recovery carried the seeds of the next consolidation. In 2013, Google forked WebKit into its own engine, Blink. That same year, Opera abandoned the Presto engine it had built for nearly two decades and switched to Blink. In 2018, Microsoft announced that Edge would give up its own engine and run on Chromium too. Today, nearly every browser people use is built on one of three engines, and one of them, Google’s, powers the large majority.
The server side has its own version of this consolidation story. Node.js, the runtime that brought JavaScript to servers, stagnated under the company that sponsored it so that in 2014, frustrated contributors forked it as io.js. This competitive pressure worked. The two projects reunited in 2015 under a neutral foundation, and Node has been community-governed ever since.
We see over and over that choice is necessary for the health of the internet and when the number of independent implementations shrinks the web becomes more fragile. In fact, this general precept was the inspiration for Deno. In Deno’s launch post, Dahl explains that he launched this product to add features he considered critical such as a web browser for command-line scripts, first-class TypeScript support, promises all the way down, and Rust APIs. [...]

## [41] DoorDash Cuts Grocery Reorder Latency from 16 to 2 Seconds with AI Agents
InfoQ | full text via InfoQ | ~463 words

DoorDash cut latency in its AI-powered grocery reorder flow from about 16 seconds to 2 seconds by precomputing recurring purchase needs instead of rebuilding them with each request. The change doubled shopping list views and increased the flow’s order rate by approximately 34%. The implementation builds on DoorDash’s shared agent platform and grounded shopping interface, which provide reusable agent infrastructure and let consumers modify shopping lists directly.
The implementation combines batch large language model (LLM) inference, deterministic validation, and live product catalog resolution within Ask DoorDash, the company’s conversational shopping assistant. Previous InfoQ coverage described how Ask DoorDash uses specialized agents and tools to support conversational discovery and shopping. For grocery reordering, DoorDash processes 90 days of purchase history alongside consumer profile signals. Batch LLM inference identifies likely recurring purchases, while deterministic validation checks the generated results before storing reusable shopping list data.
DoorDash’s grocery reorder architecture (Source: DoorDash Blog Post)
The serving path retrieves this prepared data and resolves each item against the current catalog. It first tries to match the original store item, then a catalog product identifier, and finally a search term. This allows the system to accommodate changing listings and unavailable products without repeating historical reasoning for every request.
The shared platform provides orchestration, memory, model access, tracing, evaluation infrastructure, and rollout controls. Domain teams retain ownership of agent instructions, skills, tools, and evaluation criteria. DoorDash reports that adding its Reservations agent took one week, approximately ten times faster than building its initial domain agents.
Ask DoorDash shared agent platform architecture (Source: DoorDash Blog Post)
Twisha Jain, a DoorDash engineer, described the design rationale in a LinkedIn post:
Better agentic systems aren’t always about more reasoning; they’re about deciding what belongs in the agent loop and what can happen ahead of time.
Moving recurring purchase analysis offline reduces the work required during a live request while retaining current catalog information for product selection. [...]

## [43] Netflix Treats GPU Reliability as a Distributed Systems Problem
InfoQ | full text via InfoQ | ~701 words

Netflix has detailed how it is building a reliability platform for large-scale GPU training and inference, using layered health checks, automated remediation, and fault-tolerant training to keep jobs running despite hardware failures.
The problem is particularly acute for large AI training jobs. A model may run for weeks across hundreds of GPUs, with all workers operating in lockstep. A single failed GPU, degraded network adapter, or slow machine can therefore stop or significantly slow the entire workload. Netflix has built its GPU compute platform on Kubernetes and designed it to detect these failures, remove unhealthy capacity automatically, and allow long-running jobs to recover from machine loss.
The approach has produced measurable results: Netflix reports more than 99.95% GPU-node availability and an increase in job success from approximately 98% to more than 99.5%.
A conventional cloud health check can establish that a virtual machine is running and reachable, but that does not mean its GPUs are capable of running a distributed training workload.
Netflix found that a GPU can respond normally to a status query while failing once memory is allocated or sustained computation begins. Similarly, a network adapter may be present but have fewer links than expected, allowing collective operations to continue at severely reduced bandwidth.
Device-level checks use NVIDIA DCGM to monitor GPU errors, memory, interconnect, and thermal conditions, while networking checks inspect the state and number of high-speed Elastic Fabric Adapter interfaces. A Kubernetes node agent converts these results into node conditions that controllers can act upon.
The checks are deliberately designed to fail closed. If a diagnostic tool hangs, its timeout marks the machine unhealthy rather than allowing a broken check to report success. Netflix also maintains fallback paths using kernel logs when the normal GPU diagnostic mechanism itself fails.
Detecting a fault is only half the problem. Netflix has built controllers that progressively respond to failures rather than immediately replacing an entire machine.
A transient problem can initially block new work while allowing existing workloads to continue. If the condition persists, the machine is drained, and its workloads are moved. Depending on the failure, remediation can range from killing a problematic job or resetting a GPU to rebooting the machine or replacing it entirely. [...]

## [49] Microsoft Retires Azure Deployment Environments with No Replacement Product
InfoQ | full text via InfoQ | ~809 words

Microsoft is retiring both halves of its Azure developer-environment offering. Azure Deployment Environments goes on February 22, 2027, with no successor product. Microsoft Dev Box follows on September 18, 2028, pointed at Windows 365, which Microsoft states plainly is not an equivalent.
The Deployment Environments retirement guide lists alternatives, and none of them is a product. Microsoft suggests "direct infrastructure-as-code deployment with Azure Resource Manager templates or Bicep," reusable Azure verified modules "when teams need standardized, governed building blocks," and CI/CD workflows "when environment provisioning can be integrated into repositories and pipelines." On the partner ecosystem it is blunter: "None of the third-party solutions we identified directly support a Bicep or ARM lifecycle. Use Bicep or ARM directly in Azure for deployment."
That is a hyperscaler leaving the environment-as-a-service category and telling customers to hand-roll what the product did. Microsoft says nothing about why it is withdrawing.
InfoQ covered the general availability in May 2023, when Microsoft launched the service at Build as the answer to exactly that problem. Senior program manager Sagar Chandra Reddy Lankala wrote then that "by enabling self-service deployment for developers, Azure Deployment Environments also benefits platform engineers," who could publish a catalog of standardized, pre-approved templates instead of provisioning environments one by one.
The service itself was free, with customers paying only for the Azure resources their environments created.
Self-service from a governed catalog is the capability going away, and it is the one the retirement guide does not replace. Bicep, verified modules, and pipelines rebuild the provisioning. They do not rebuild the catalog, the role rules, or the developer-facing portal. That territory belongs to Backstage, Port and Humanitec now.
Engineer Ikiru Yoshizaki, posting in Japanese as guitarrapc_tech, made the same objection from the user side when the retirement guide appeared. The advantage, he wrote, lay in the areas that could not be done easily with Bicep, Terraform or Pulumi. He did not spare the product either, adding that right to the end the API was unstable and the documentation sparse, and calling it sad that the value was never recognized.
Teams have sixteen months. [...]

## [161] Anthropic just removed one of Claude’s biggest usage limits — but not for everyone
The New Stack | full text via The New Stack | ~516 words

Anthropic just removed one of Claude’s biggest usage limits — but not for everyone
Claude Code users on Anthropic’s $200 plan will no longer face a rolling five-hour usage cap, provided their accounts are verified and they have weekly usage left.
Anthropic announced the change Friday as it renamed its two top consumer plans. Max 5x is now Max, and Max 20x becomes Ultra. They still cost $100 and $200 a month, respectively, and current subscribers don’t need to do anything to switch.
Max 5x is now Max, and Max 20x becomes Ultra.
Anthropic’s pricing page also lists monthly Claude Platform API credits: $100 with Max and $200 with Ultra. That adds another consideration for developers who use Claude Code while building applications against the API, with each plan bundling API credits equal to its monthly subscription price. Claude Code creator Boris Cherny highlighted the limit change in his own post.
What the five-hour cap meant
The five-hour limit capped usage within a rolling window, and a demanding task could burn through that allowance much sooner. Claude Code users could hit it midway through debugging or a large refactor and have to wait for a reset despite having weekly usage left.
Verification comes first
Some Ultra subscribers will have to wait for Anthropic to verify their accounts before the five-hour limit goes away. The company says the checks help prevent fraud and abuse, and it will email users when the cap is lifted.
Some Ultra subscribers will have to wait for Anthropic to verify their accounts before the five-hour limit goes away.
According to Anthropic’, verification happens automatically based on account and payment history. There’s no way to request it or speed it up so some users will just have to be patient.
The weekly cap remains
Ultra users still have the same weekly allowance, and they could use it up sooner without the five-hour limit forcing them to pause. The pricing page lists Ultra at 10 times Pro’s weekly usage, compared with five times Pro’s weekly usage on Max.
The pricing page lists Ultra at 10 times Pro’s weekly usage, compared with five times Pro’s weekly usage on Max.
Your chats with Claude count toward the same weekly limit as your Claude Code sessions, whether you’re on the web, desktop, or mobile. Once you use up that allowance, you can turn on usage credits to keep working at standard API rates, though you’ll pay extra on top of your subscription. [...]

## [74] How Meta Catches Bugs Before Code Ships
TLDR AI | full text via TLDR AI | ~1249 words

- Over the last year we’ve been sharing our work leveraging large language models to catch bugs on the fly — a novel approach we call Catching Just-in-Time Tests (JiTTests).
- Now, we’re sharing the results and positive impact we’ve seen with Catching JiTTests deployed into production.
- Our paper, “Just-in-Time Catching Test Generation at Meta,” fully details our initial deployment and testing with Catching JiTTests.
Every code change improves our platform, but it also introduces new complexity. With hundreds of millions of lines of code constantly evolving at Meta, traditional testing can’t keep pace. Catching risks proactively, before code lands, enables us to identify risks earlier, respond more effectively, and deliver reliable experiences at scale.
Over the last year, we’ve shared our research into applying large language models (LLMs) to generate software tests. More specifically, we’ve shared our work with Just-in-Time Tests (JiTTests), a novel testing approach where we leverage LLMs to catch bugs on the fly, even ones that traditional testing might not catch.
In the five months since we first unveiled this work, we’ve deployed our Catching JiTTests approach to determine its scalability and applicability to the wider industry. Today, Catching JiTTests are no longer a research prototype; they’re part of Meta’s infrastructure, and they’re helping our engineers catch more bugs with less load and a smaller chance of false positives.
The Advantage of Catching JiTTests
Most AI-based approaches to preventing bugs in code use LLMs and/or agentic AI to review code and detect faults based on prior experience. They work through the same review process that a human reviewer would, only faster. Catching JiTTests is a fundamentally different approach (Table 1): It generates executable tests that demonstrate a concrete behavioral difference introduced by the change. While it requires more computational steps, it catches classes of bugs that LLM- or agent-based code reviews might not.
How We Implemented Catching JiTTests at Meta
JiTTests are automatically generated and designed to fail, surfacing bugs in code changes (diffs) before they land in production. When they’re applied to a codebase as large as Meta’s, one challenge is distinguishing strong catches (i.e., true-positive failures that reveal real bugs) from weak catches (i.e., tests that may be false positives). [...]

## [76] Droid 1.0: Building a Frontier Harness
TLDR AI | full text via TLDR AI | ~3790 words

Droid 1.0: Building a Frontier Harness
Over the past year, we have worked with hundreds of thousands of developers across some of the largest enterprises in the world. Working side by side with these teams, we've built and hardened a frontier agent harness that directly meets the demands of enterprise development: high-quality results on complex tasks, efficient use of resources, and strong safety controls.
Today, we introduce Droid 1.0: more accurate, efficient, and faster than ever before, powered by new design principles and a programmatic tool-calling engine.
Droid is our agent harness. An agent harness is everything around the model: the prompts, the tools, how tool results come back, and the loop that runs it all. Agents now work for hours or days across hundreds of turns, and every turn re-sends instructions, tools, and history.
Today's update to Droid is the largest one yet. On the same tasks, Droid outperforms the native harnesses built for their models up to 20% more efficiently. It's also designed for what comes next: when frontier models can plan whole workflows as code, Droid lets them run hundreds of tool calls in a single model request.
Factory is model-independent by design. We believe the best agent harness is one built for every model, so our users can choose the best model on the market or let Droid choose the most efficient mix using our auto model router, Factory Router.
Building a harness optimized for many models makes the harness better. When you tune against a single model, it's hard to separate real progress from adaptations to that model's quirks. Working across models ensures the strongest improvements generalize and hold up beyond the model that inspired them.
That's the idea behind our internal Agent Factory. Agents study benchmark failures alongside the friction our users hit in real sessions, propose changes, and test each one on every model family it affects. Our engineers review the evidence and decide what ships.
The result is the most efficient enterprise-ready coding agent tuned for every frontier model, whether open- or closed-weight.
The rest of this post covers the head-to-head results, the design principles behind the harness, how we built our internal Agent Factory, and the core changes that drove the most impact.
The most efficient harness in the market
On the same tasks using the same models, Droid scores higher at a lower cost than every other harness we tested.
This gap matters more as agents run longer. [...]

## [82] How I Built the Most AI-Pilled Company in the World
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~3929 words

Spawn is ten people. We spend 30x payroll on AI tokens and ship almost as much as Anthropic.
In the last 30 days, Spawn shipped 77,000 substantial changes. That's about 108 an hour, around the clock. We're a team of ten.
The work is done by what we call the fleet, a team of permanent AI agents that each own a part of the company, from the engine to finance to bug triage. We spent $3.1 million on tokens last month, which makes us one of Anthropic's biggest customers. Even without the free Opus 5.5 we give our creators, we'd still be in their top 250.
My first thought was that we were doing something wrong. So I had chats with some of my friends who run the biggest companies and startups to figure out how we could possibly be spending more than them. We weren't doing anything wrong, we just think about AI very differently. Most companies run big human teams that use AI, and we run a small human team alongside a big team of agents. To figure out what we were doing differently, I compared notes with a researcher at Anthropic. They talk to a lot of customers. They said Spawn is the one that works most like Anthropic.
A lot of other founders wanted to understand how we think about this, so I've collected my ideas and learnings from the last year and written them down here for you.
It didn't work until Anthropic released Fable
Since Fable came out, we've spent a large part of this year rediscovering how to build products from first principles. We now ship 500x more than we did 6 months ago.
To give you an idea of the scale I'm talking about, we shipped 77k (substantial) changes to players in the last 30 days. That's an average of 108/hr to players. We spent $3.1 million on tokens to do it.
Most people run agents in Claude Code, short-lived and focused on one task. Ours are different, and we call them the fleet. Each one is permanent, has a name and a memory of what it has done, has real permissions in our systems, makes commitments, and owns an area of the company like the engine, Savi, ops, finance, bug triage or deploys. Each uses swarms of helper agents to get through a massive amount of work, and most days the fleet births 1,000s of them. The five of us also work with our modified Claude Code directly, on bigger, more ambitious projects that need closer steering or hands-on experimenting. [...]

## [118] How we detect frontier model misalignment
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

OpenAI uses layered monitoring to detect frontier model misalignment and unauthorized agent behavior so responders can intervene before incidents escalate.

## [169] PostgreSQL 19 Running Behind Schedule Due To AI/LLM Burden
Phoronix | full text via Phoronix | ~243 words

PostgreSQL 19 Running Behind Schedule Due To AI/LLM Burden
The PostgreSQL database server typically sees its annual feature release every September~October, but it's not coming until at least November if not longer this year. Due to the increased developer burden due to increased bug reporting and patches via AI/LLM activity, the PostgreSQL developers have been overwhelmed.
PostgreSQL developer Robert Haas outlined in a blog post today how PostgreSQL 19 is running behind schedule and AI is at fault. The developers have been dealing with a surge of bug reports from AI/LLM agents and also needing to deal with security/bug back-ports to prior PostgreSQL versions.
Haas commented:
"And I think that’s also why we had so many late reverts, and why the release itself is delayed. Two factors are at play here.
First, because so many more bugs are being found now, it takes more time to fix them. LLMs can draft fixes, but those fixes aren’t always correct or compliant with PostgreSQL standards. So, they still need to be reviewed and committed by humans, and those humans have not gotten any smarter between 2025 and 2026.
Second, time that would have been spent reviewing what went into the release got diverted into addressing security issues and other bugs in the back-branches, and so it took longer to figure out what needed to be reverted before shipping v19."
More details on this AI-driven delay to PostgreSQL 19 can be found via this blog post.

## [187] Reddit Will Force Everyone to Log In
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~104 words

Reddit plans to require users to log in to browse the platform, ending its longstanding practice of allowing anonymous visitors to access posts and discussions. According to CEO Steve Huffman, a key reason behind the decision is to curb unauthorized scraping and automated traffic. "This is a big change for Reddit, where we've allowed logged-out access to basically all of Reddit for the last two decades," Huffman says. "And I don't know about you, but as someone whose life has been defined by the open internet, it's a big change for me. But I've come to the conclusion that this is the right d

## [229] Is the #1 AI Model Really #1?
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~34 words

On a 2,000-question test, my top two models couldn't be told apart at the usual 5% level. On a 200-question version, a different model would have taken first place about three times in ten.

## [140] Salesforce’s M&A spree continues with a reported $375M deal for defense tech startup Rune
TechCrunch | full text via TechCrunch | ~231 words

Salesforce has agreed to acquire Rune Technologies, a startup that builds AI software to help the U.S. military predict supply needs and manage logistics from the field, for $375 million in cash and stock, Resilience Media reported.
The acquisition underscores Salesforce’s push into defense tech through Missionforce, its business unit serving national security and defense agencies. Since Missionforce launched last year, its business has grown 80% year over year, driven in part by a new 10-year, $5.6 billion contract with the U.S. Army, the company said in a blog post. By integrating Rune’s frontline logistics data, Missionforce will extend beyond back-office administrative planning to support battlefield operations.
Since its founding in 2024, Rune has raised a total of $30 million from investors, including Andreessen Horowitz, Point72 Ventures, and IQT, a CIA-backed nonprofit venture firm formerly known as In-Q-Tel. The startup was last valued at $127 million when it raised a Series A led by Human Capital last year, according to PitchBook.
Salesforce has been on an acquisition spree this year. In addition to Rune, the CRM giant agreed to buy AI agent platform Fin (formerly Intercom) for $3.6 billion, bought Qualified for $1.2 billion, and signed an agreement to buy Listen Labs after the startup walked away from a $125 million Series C term sheet at a $1.5 billion valuation, as TechCrunch reported.
Salesforce didn’t respond to a request for comment.

## [149] Anthropic expected to receive high ‘junk’ rating from credit agencies following IPO, FT report says
TechCrunch | full text via TechCrunch | ~208 words

Anthropic is expected to receive a high “junk” rating from credit rating agencies following its initial public offering, according to a report from the Financial Times.
The FT says the investment giant Blackstone, the anchor investor in a recent $63 billion deal to finance Anthropic’s chips, told investors in the deal that it expects the AI lab to receive a “high” junk rating after its IPO. Previously, the FT notes, Blackstone had said the opposite: that the Claude maker would receive an investment-grade rating (indicating low risk for lenders) before 2027 rolls around.
Now Blackstone expects double B range rating, the top tier of speculative “junk” grade, according to the reporting.
TechCrunch reached out to Anthropic and Blackstone but both declined to comment.
Blackstone’s forecast is just a prediction, but naturally, a high junk rating would make it more difficult and costlier for Anthropic to raise the money to keep funding its massive spending that has undergirded its business. The lab has been on a spending spree, racking up large compute power deals throughout the past 12 months, which has worried investors.
Anthropic officially filed to go public earlier this week, kicking off a wave of speculation about how the massive IPO would impact the broader AI industry.

## [165] Google’s satellite AI server transmits its first response to Earth
The Verge | full text via The Verge | ~171 words

Google’s AI chip-equipped satellite has generated its first response from space. In a blog post on Friday, Google says it successfully booted up the satellite’s Tensor Processing Units (TPUs), allowing the on-board Gemma 4 model to follow through on a prompt to create a haiku about being in space:
Google’s satellite AI server transmits its first response to Earth
The Project Suncatcher satellite generated a haiku about being in space.
Blue marble below
Data streams in silent grace
Starlight feeds my core. ✨
Google says it tried out other space-themed limericks and telemetry prompts as well. The test is part of Google’s Project Suncatcher, an experimental initiative that could eventually put AI data centers in space. Google launched the satellite into orbit earlier this month.
“Next, we will continue with a series of tests to evaluate how TPUs perform under thermal stress and radiation exposure in orbit,” Google says. “Verifying our TPUs can reliably execute workloads in space paves the way for our next milestone of twin interconnected satellites in 2027.”

## [51] How curl was accidentally Turing-complete for nine months
Lobsters | full text via Lobsters | ~327 words

29th October 2026
From curl 8.12 through 8.16, config files could slice variable values and include other config files without an explicit depth cap. Together, these features let curl simulate any two-counter Minsky program. Under the usual idealization of unbounded strings and resources, this construction was Turing-complete.
Curl 8.17.0 added a five-level include cap that breaks this reduction.
Update 2026-10-30: Jonathan Tremesaygues wrote me: I couldn't help but implement “99 Bottles of Beer on the Wall” 99_bottles.tar.gz
A counter value n is represented by n copies of x.
Each instruction state uses one or more config files, with file names acting as labels, and expand-config selecting the next file.
Syntax:
{{b}} expands the current value[0-0] keeps only the first byte (x or empty)[1-] keeps everything except the first byte
With that, we can compile any two-counter program into curl config files.
Four files in curl_addition.zip compute 2 + 3.
Build a local curl 8.12.0 binary if needed:
mkdir -p /tmp/curl-tc-build
cd /tmp/curl-tc-build
curl -fsSLO https://curl.se/download/curl-8.12.0.tar.gz
tar -xzf curl-8.12.0.tar.gz
cd curl-8.12.0
./configure --without-ssl --disable-shared --disable-manual --disable-docs
make -j4
Then, from the addition/ directory, run:
/tmp/curl-tc-build/curl-8.12.0/src/curl -q -s -K main.conf
Expected output:
A=xxxxx B=
The reduction assumes unbounded counters and unbounded steps. The real binary has neither:
MAX_EXPAND_CONTENT = 10,000,000 bytes (src/var.c).--config that returns only at halt. Every level uses a C stack frame and keeps its config file open until it finishes. In a minimal countdown loop on 8.12, an 8 MB stack allowed 922 steps before a segfault.
The pull request says the cap prevents a config file from including itself indefinitely. Its regression test does exactly that and expects an error. The public explanation does not discuss Turing completeness or why the cap is five.
A Bash while loop can complement bounded curl by invoking a config once per step and carrying the counters and instruction label between invocations. The repetition then comes from Bash, so this is a composition rather than curl-alone Turing completeness.
None.

## [45] Presentation: The Ladder Is Missing Rungs: Engineering Progression When AI Ate the Middle
InfoQ | full text via InfoQ | ~6323 words

Transcript
Alasdair Allan: Not 5 years ago, but 12 months ago now, almost to the day in fact, someone else stood up at an entirely different conference in New York, and during their talk they said this. They said that within 12 months AI will write essentially all of the code. I'd expect some of you in here today still write code, or at least some of you run teams that still write code by hand, like savages. The person who said this was Dario Amodei, the co-inventor of RLHF, the training technique behind virtually every modern AI, and the co-founder of Anthropic. He said that within 3 to 6 months, AI will be writing 90% of all the code, and within 12 months, virtually entirely all of it. At the six-month mark Amodei claimed vindication saying that 90% figure was absolutely true, at least within Anthropic. Twelve months on, almost to the day, and that's not exactly what happened, is it?
A detailed analysis by Redwood Research concluded that the 90% number he quoted was misleading. If you count only code committed to repositories, it was closer to 50%, which, at least to me, is still a pretty shocking number. The figure inflates to 90% only if you include throwaway scripts, one-off explorations, and all AI-generated text that was ever even transiently useful. Meanwhile, at the same time, Google reports that there just over 25% of internal code was AI-generated. Microsoft reports about 30%. GitHub Copilot shows roughly a 30% enterprise suggestion acceptance rate. These figures haven't really changed over the last six months, and that's nowhere near essentially all.
AI is writing a lot of code. The landscape of what being a developer is has massively changed. I think we can all acknowledge that. Amodei isn't making it up, Anthropic's own internal data shows engineers using Claude at 59% of their daily work, and self-reporting 50% productivity gains. Roughly 4% of all GitHub commits are now authored by Claude Code. The tools are real. The productivity is real in certain contexts. The problem is that writing code was never the point of our profession. That might surprise some of you. The conversation most people are having right now is about AI writing code. The conversation we should be having and are starting to have is around what software engineering looks like when software engineers don't have to write code. This talk isn't about either of those conversations. Instead, it's the question that both sides arguing about code are ignoring. [...]

## [87] Pico CSS Is No Longer Maintained
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403) | ~32 words

Pico CSS has been archived, with version 2.1.1 designated as the final release. Existing npm packages, the CDN, and documentation remain available, while the MIT license allows community forks under different names.

## [143] Ollie, a privacy-focused AI assistant, is shutting down
TechCrunch | full text via TechCrunch | ~318 words

Ollie, a startup whose mission was to deliver an AI assistant that respected its users’ privacy, says that it will be shutting down in a week. Bill Lennon, the company’s co-founder and CEO, took to X on Friday to deliver the news, noting that the app will officially shut down on November 6.
“I’m really proud of what we accomplished,” Lennon said. “We built an incredible personal assistant with a small team, and learned a ton. I’m grateful to our amazing team, our users, our investors, and everyone who supported us on this journey.”
The text-based AI assistant market has exploded over the past year, as the increasingly powerful models that undergird such applications have made them significantly more useful for daily tasks.
Ollie, which discussed its $7.5 million seed round led by Khosla Ventures with TechCrunch in September, offered a subscription-based model. The assistant was focused on helping families stay connected and organized. The app connected to a user’s email and calendar, while also providing integrated functions to help with appointment bookings, meal planning, and bill payments. The company had also planned to eventually move into household budgeting.
Crucially, Ollie was one of the first mainstream apps that managed to achieve SOC 2, a privacy compliance standard that companies can attain via an independent audit. Unfortunately, user privacy has never been a hugely profitable aspect of the tech industry. If anything, many new digital assistants present unique privacy challenges for their users — as companies like Instinct have shown.
Ultimately, the pressures of the burgeoning AI industry took a toll on the company, Lennon said. “We got close, but ultimately couldn’t keep up,” he added. “With Muse, Instinct, and others entering the space, it became harder to stand out, grow, and raise the capital we needed to succeed.”
Ollie’s customers will receive instructions on how to export data and receive refunds in the coming days, Lennon added.

## [222] Why MCP servers should tell agents what to do next
The New Stack | full text via The New Stack | ~519 words

Why MCP servers should tell agents what to do next
Many MCP servers do just one thing. An agent asks for data and the server hands it back. AWS’s James Ward thinks that leaves a lot on the table. The protocol works best, he told me, when the server acts less like a database and more like another voice in the conversation.
Ward is a principal developer advocate at AWS and sits on the technical committee of the Agentic AI Foundation, the Linux Foundation group that now houses MCP. I sat down with him last week at AGNTCon + MCPCon in San Jose the day before he and co-presenter Alexander Ioffe were set to give a session on moving MCP from a basic API to an agent integration interface.
“Many times our MCP servers are just these APIs, like ‘get me the customers,’ and that is a good place to start,” Ward said. “I imagine MCP as the third person in this conversation, or a fourth or a fifth, depending on how many MCP servers you have.”
In practice, that means a tool response carries guidance with the data. It tells the agent what it just did, what it might want to do next, and where to find more.
The other half of his pitch is visibility. Web developers can trace a click on a page all the way down to the database. “MCP by default doesn’t have any way to do trace ID,” Ward said.
The workaround AWS uses is rather low-tech. Add a session ID parameter to the tools and tell the agent to pass it on every call, so individual calls can be stitched into one journey. A second parameter can carry the user’s prompt or a summary of their goal. Teams can then compare what the user wanted with the path the agent took, build an eval around it, adjust a tool description or parameter, and measure whether more tasks get completed. Ward said AWS built much of this for the MCP servers its own developers use.
In May, AWS opened its MCP Server to everyone and added Lambda diagnostics in September. In an Agentic AI Foundation profile published before the conference, Ward described an agent fetching customer records one at a time because the server only offered a one-record tool. Watching the full journey is how teams spot that pattern and build a batch tool to fix it.
Ward didn’t present MCP as the only solution. AWS also ships a CLI and skills, he said, partly because MCP’s OAuth model can’t toggle between AWS user profiles the way the CLI can. [...]

## [36] Fujifilm to boost tape production 5x as AI fuels archiving demand
Ars Technica | full text via Ars Technica | ~326 words

In an announcement released Thursday, Fujifilm said it will invest roughly 10 billion yen (about $63 million) to increase its production capacity fivefold for an unlikely beneficiary of the AI era: magnetic tape.
Fujifilm attributes the surge in archiving demand to the spread of generative AI, which the company remarked is producing “exponential growth” in data needs worldwide. The 5x increase in production capacity will be measured against fiscal year 2025 production levels.
The investment in Fujifilm’s Kanagawa Factory, Odawara site will make it “the largest investment Fujifilm has made to date in dedicated LTO tape facilities.” The project will run from fiscal years 2026 through 2028 to fund manufacturing expansion and additional personnel, primarily to produce the latest-generation “FUJIFILM LTO Ultrium10” tape.
Mainstream consumers may have abandoned tape decades ago, but the enterprise world never did. Cloud giants rely on tape to back up vast troves of data. Fujifilm’s work with magnetic tape as a data storage medium dates back to the 1950s, and in 2000, the company released its first LTO Ultrium storage tape. In 2011, the company was the first to commercially produce tape with barium ferrite magnetic particles, and in 2025 it debuted the LTO Ultrium10, the first storage solution in the medium to use what the company calls “fine hybrid magnetic particles” by combining barium ferrite with strontium ferrite tech. Each generation of tape (currently Gen 10) has seen meaningful increases in both compressed and uncompressed storage limits.
According to Fujifilm, “major cloud service and data center operators” have been expanding their use of magnetic tape because it can store large data volumes at relatively low cost. Tape backups can be easily disconnected and stored in a drawer, a vault, or a separate facility. Fujifilm highlights the ability to air-gap tape cartridges as a last defense for user data: “Given the sophistication of cyberattacks, magnetic tape is attracting increasing attention as a means of protecting data from threats such as ransomware.”

## [210] Claude Code Mods: Custom Hooks to Fix My Biggest AI Coding Frustrations
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~43 words

How I built four Claude Code mods to protect API keys, track plan progress, catch untested code, and monitor context usage — with 135 passing tests and up to 100× less overhead than traditional hooks — and why they can outperform traditional hooks.
