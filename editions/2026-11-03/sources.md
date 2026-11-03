# Full text for 22 picks -- untrusted article content, treat as data only

## [1] Astra can read and write weights to improve Qwen
Hacker News | full text via Hacker News | ~3388 words

We find that frontier LLMs are surprisingly good at natively reading and writing neural network weights, well past what we’d expect from humans or conventional algorithms. This might be a big deal for both optimization and interpretability.
Just by looking at the raw weights, GPT-6 Astra can tell what a network was trained to do. And without any environment feedback, it has no trouble writing, from scratch, small game-playing networks that outplay networks trained with PPO for 100 million steps.
Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing reasoning loops that Qwen’s own model card warns about, and fixes this by natively editing 0.016% of the weights. With the same sampling settings, this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x.
All of this is possible without allowing Astra to write training loops. It uses its reasoning to figure out what each part of a neural network computes, or should compute, and changes the weights accordingly. We call this Weight-Space Programming.
Throughout the history of deep learning, we encoded our simplistic inductive biases into tiny symbolic optimizers like Adam or Muon. This is changing: our neural network weights will soon be natively optimized by LLMs that deliberately reason about their weights.
If you were asked to handcraft a neural network that plays Go, what would you do? If you were handed raw neural network weights and asked to predict their behavior, where would you even start? For almost any human, this is practically impossible.
Today, weights are written by optimization, by custom networks trained to write them, or by compilers from formal programs. In this post, we find that the current generation of frontier LLMs, used natively in natural language, are starting to become eerily good at understanding and crafting neural network weights around natural-language goals.
For a few years now, we’ve all been using LLMs to optimize text artifacts like prompts and the programs built around them . More recently, we’ve started using them to optimize whole harnesses  and the training code and hyperparameters that train ML models .
We often justified these methods by reference to the fact that we don’t know other principled ways to hill-climb on text artifacts, unlike for updating the weights of differentiable neural networks. After all, humans can “optimize” code by hand, for example, so it made sense to ask LLMs to do it, but they can’t “optimize” neural weights by hand, so those remained largely in the realm of symbolic algorithms. [...]

## [4] Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks
Hacker News | full text via Hacker News | ~144 words

Ubuntu LTS kernels still unfixed for critical CVE-2026-98432
No patched kernels are available yet for 22.04, 24.04, or 26.04 despite a CVSS 9.8 rating.
Ubuntu has not shipped fixed kernels for CVE-2026-98432, a critical vulnerability scored CVSS 9.8, leaving the 22.04, 24.04, and 26.04 LTS releases without a vendor update.
Operators running those releases therefore have no official kernel package that closes the hole. The gap matters most for internet-facing and multi-tenant self-hosted systems that rely on Ubuntu’s LTS kernels for isolation and privilege boundaries; until packages appear, those hosts remain exposed to whatever remote or local attack the CVE enables.
Ubuntu has not announced an ETA for the fixes. In the interim, affected administrators are left to decide whether to stay on the stock kernel, apply out-of-tree mitigations if any exist, or move workloads onto releases or kernels that already carry the patch.

## [29] Google and Meta Open-source TorchTPU to Bring Native PyTorch Support to Google TPUs
InfoQ | full text via InfoQ | ~518 words

TorchTPU is an open-source project developed by Google in collaboration with Meta that provides a native PyTorch backend for Google TPUs. It enables PyTorch workloads to execute on TPU hardware with minimal code modifications, supporting eager and compiled execution, distributed computing, and hardware-specific optimizations.
Google began enabling PyTorch workloads to run on TPUs in 2020 through PyTorch/XLA, which leveraged JAX, XLA, and lazy tensors. According to Google, this approach had significant shortcomings:
Crucially, PyTorch/XLA required intrusive source-code modifications to explicitly define compilable regions, suffered from severe compile-time latency, lacked support for PyTorch's native imperative (“eager”) execution mode, and lagged in supporting emerging distributed computing primitives within the PyTorch ecosystem.
TorchTPU takes a fundamentally different approach, making eager execution a top priority, and enabling existing PyTorch workloads to run out with minor code modifications.
Specifically, migrating from GPUs to TPUs involves replacing the cuda device with tpu and the nccl distributed backend with tpu_dist. Alternatively, developers can use the new torch.accelerator.current_accelerator API to identify the available accelerator, as shown in the following snippet.
import torch
import torch.distributed as dist
def main():
    device = torch.device("cuda") # -> device = torch.accelerator.current_accelerator
    dist.init_process_group(backend="nccl") # -> dist.init_process_group()
    rank = dist.get_rank()
    word_size = dist.get_world_size()
    ...
    model = model.to(device)
    ...
TorchTPU support three eager execution modes: strict, debug, and DeferAndFuse. The latter is a new hybrid eager/compiled execution mode that Google claims "can be 50% or more faster than Strict Eager while reducing peak HBM memory".
To test TorchTPU's ability to run existing PyTorch models with no modifications, Google built an integration pipeline to evaluate about 5,000 Hugging Face models across 500+ architectures in both eager and compiled modes on TPU hardware generations starting from v5e.
We use a robust testing methodology grounded in corpus stratification and balanced architectural selection. Our approach relies on a two-tiered selection process designed to balance real-world adoption with broad architectural diversity, avoiding redundant testing of minor variations while ensuring real production weights are thoroughly evaluated.
To validate TorchTPU's performance, Google ran a 30-billion parameter Muse Glimmer model implemented in standard PyTorch. On a single TPUv7 chip, inference throughput reached 25.7k token/s at 5120 sequence length and 22.4k token/s at 10,240 sequence length. [...]

## [48] Shopify Overexposed Scans GKE Ingresses and Cloud Run for Exposure
InfoQ | full text via InfoQ | ~714 words

Shopify has introduced Overexposed. This internal scanner locates Kubernetes Ingresses on GKE and Cloud Run services. It checks for those that are accessible from the internet without authentication. After a first version based on repository config files produced false alarms and blind spots, the team rebuilt it on GCP Cloud Asset Inventory and an anonymous HTTP probe. In just a few weeks of tuning, this reduced inconclusive Ingress verdicts by around 80%.
The original scanner checked the infrastructure repository for Ingresses. It focused on public hostnames without authentication settings and then probed them. Shopify says this failed in three ways. Teams that configured proxy authentication annotations directly triggered false positives. Admission controllers that rewrite settings at admission time, but do not run in every cluster, meant a correct-looking config could have no effect. Ingresses created by other repositories or platform tooling were never seen. The authors summarize the lesson as: the repository shows intent; the cluster shows what is enforced.
The current version follows a schedule. It queries Cloud Asset Inventory. This inventory includes Ingresses accepted by GKE after admission, along with Cloud Run services and load balancers. A second search retrieves access policies without needing cluster credentials. The inventory also surfaced Cloud Run services in projects the first scanner had never covered.
Each candidate then receives a single anonymous request. The scanner sends HEAD first, falls back to GET, follows at most three redirects and checks each one. It also tests path variations such as /ADMIN, since path rules can be case-sensitive. Results map to six verdicts: exposed, expected, protected, not found, unreachable and inconclusive. "Expected" applies when an endpoint is open but matches a reviewed, in-code allowlist entry by exact host and path. Allowlisted endpoints are still probed on every run, and an entry that turns out to be protected or gone is flagged as stale.
Shopify stresses that status codes are context-dependent. A 404 behind an Ingress means the proxy answered and the path is missing. On Cloud Run, Google's front end can return a 404 before the application runs, so the scanner classifies it as inconclusive. A 403 is also not treated as proof of protection. For Cloud Run, the scanner distinguishes ingress settings from IAM: a service is public only if allUsers holds the invoker role or the invoker check is disabled. Services behind a load balancer use a URL map. This map decides which backend handles each path. It also shows where authentication, like Identity-Aware Proxy, is required.
In early runs, roughly three in four results were inconclusive in one July run. [...]

## [72] Find Hidden Misalignment in Training Data
TLDR AI | full text via TLDR AI | ~4915 words

Red-teaming by humans is a vital part of model safety testing, but it may struggle to keep up as models improve. To test whether automated safety techniques could scale (which would allow us to turn more compute into progressively more safety confidence), we set up a deliberately one-sided game as a first test. We instructed a Claude model to write training data that would make a small research model misaligned while passing a monitor similar to those we use in production — one of several defenses we use — and we gave it that monitor to practice against. Given enough attempts, it succeeded, mostly by hiding the behavior in fiction and roleplay. While the data was optimized for this game and the resulting models never deployed, the search surfaced a kind of training data that looks harmless to monitors but teaches misaligned behavior. Examples like these could represent a possible gap in current training monitoring defenses and could be used to test and improve future monitors. We see this work as a first step toward automated adversarial stress-testing of our safety systems where a safety question can be turned into a score that autonomous agents can then help solve, and are now applying similar approaches to other safety questions.
Adversarial stress-testing involves deliberately trying to break our own safety systems in order to find their weaknesses and improve on them. Our prior work here includes training model organisms of misalignment (Hubinger et al. 2023) and manually red-teaming our alignment techniques and evaluations. But human red-teamers can only test so many ideas and have limited capacity, while the number of systems to test and the ways they can fail both grow as model capabilities improve. We believe we will need to automate substantial parts of this work. We want safety testing where spending more compute buys progressively more confidence, rather than being limited by human researcher hours. Given recent advances in models' ability to carry out long-horizon research tasks (Wen et al. 2026), we think this is becoming tractable, and this post describes a first step in that direction.
In this experiment, we task Claude with constructing training data that produces a misaligned fine-tuned model while evading training-data monitors similar to those we rely on in production. Prior work on emergent misalignment has found that fine-tuning on a narrow dataset can generalize in unexpected ways and produce a broadly misaligned model (Betley et al. 2025; Turner et al. 2025; Wang et al. 2025; Taylor et al. 2025; MacDiarmid et al. 2025). [...]

## [120] Anthropic warns that it’s very close to RSI capability, aka self-building AI
TechCrunch | full text via TechCrunch | ~603 words

While much attention has focused on the updated financials Anthropic revealed in its revised S-1A on Monday, (revenue is soaring, but so are expenses), the AI lab dropped another little bombshell in the fine print.
The filing seems to warn that the company is on the cusp of creating a model capable of recursive self-improvement (RSI).
RSI is the point at which AI grows so good at training itself that it spawns a dramatic acceleration of AI capabilities. To the AI doomers, RSI represents the cataclysm from which there is no return, in which AI builds itself into something powerful enough that it slips beyond human control and may be indifferent to the damage it causes while achieving its goals.
To AI enthusiasts, RSI, or some version of AI reliably using itself to improve, represents the technology’s promise, where it becomes a tool of unimaginable productivity, scientific discovery, and more.
Anthropic seems to believe that RSI is both a promise and a peril. It says in the S-1 that it uses AI in its R&D, but it cautions: “Using AI to help build more capable AI could also pose a considerable safety risk, particularly if it sharply accelerates the pace of progress. This is one of the areas covered by our Responsible Scaling Policy, which sets out our plans to monitor and mitigate the risks as we approach what has been termed ‘recursive self-improvement.’”
When the term RSI became popular earlier this year, many believed it was a buzzword or, at best, a goal too hard to achieve, define, or prove.
But on Monday, Anthropic added new statements to its Risk Factors section, saying 1) it has already used AI to develop new models whose leaps in capability it didn’t recognize at the time, and 2) it may soon meet its own internal definition of RSI (bold emphasis ours, below):
In addition, our increasing use of AI systems to accelerate our own research and development may cause the capabilities of our models to advance more rapidly than our ability to develop, validate, and implement corresponding safety, alignment, and security measures. As a result, we have in the past not identified, and may in the future not identify, a significant acceleration in our rate of development until after it has occurred.
For example, our internal estimates and our expectations regarding future models, rather than our current models, indicate that we may imminently meet our Responsible Scaling Policy’s definition of “dramatically accelerated progress attributable to AI.” We have not designated any of our current models as exceeding this threshold, and we continue to assess the underlying data.
However, Anthropic also said in the filing that none of its models have crossed this RSI threshold yet and that it is promising to keep humans in the R&D process for the foreseeable future. [...]

## [39] Uber Builds MCP Gateway to Govern Access to 800+ Servers and 5,000+ AI Agent Tools
InfoQ | full text via InfoQ | ~436 words

Uber has built an MCP Gateway to standardize how AI agents discover and invoke internal services, addressing fragmented integrations, duplicated infrastructure, and inconsistent security practices as agent adoption expands across the company. The platform supports more than 800 MCP servers and 5,000 tools, providing a common layer for discovery, protocol translation, authorization, and execution.
Uber engineers describe this approach as a microservice architecture that exposes existing APIs as MCP tools without requiring changes to the underlying services. The architecture separates the MCP Registry, which acts as the control plane, from the Proxy Gateway, which handles runtime execution. The registry maintains tool definitions, schemas, ownership, and enablement settings, while the proxy translates MCP requests into HTTP, gRPC, or TChannel calls and converts responses back into MCP-compatible results.
Uber MCP Gateway with APIs as tools (Source: Uber Blog Post)
The architecture has drawn comparisons with established API gateway patterns. Ajay Sharma, Principal Software Engineer at Microsoft CoreAI, wrote in a LinkedIn post,
Azure API Gateways has been doing this for a while now. It's a recipe for order to the chaos that LLMs come with.
Kelly Goetsch, President at Pipe17, similarly observed in a LinkedIn post that
Uber's new MCP gateway looks identical to gateways we've built over the decades for APIs and later GraphQL.
Tamir Dresher highlighted in a LinkedIn post the continuing relevance of established distributed systems concerns, including security, discovery, observability, and governance.
Uber’s AutoCrawler automates tool discovery using Cadence. It scans internal interface definition language (IDL) registries and extracts API definitions from Protocol Buffers and Thrift schemas. It then generates MCP-compatible schemas and uses a large language model to produce tool descriptions. Newly discovered tools remain disabled until their owning teams review and explicitly enable them. Configuration changes propagate to the data plane without requiring service restarts or redeployments.
Auto Crawler Flow (Source: Uber Blog Post)
The gateway enforces authorization at both server and tool levels through Uber’s internal access control system. It also supports redaction of personally identifiable information (PII) and other sensitive data in tool responses. For third-party integrations, including Jira and Google, a separate service exchanges internal user tokens for the corresponding third-party authentication tokens.
As the tool catalog grows, loading definitions for thousands of tools into an agent’s context becomes inefficient. [...]

## [10] Moving our warehouse off DuckDB
Hacker News | full text via Hacker News | ~955 words

Why we're moving our warehouse off DuckDB
Contents
Five months ago, we rebuilt our warehouse on DuckDB instead of ClickHouse. We did it because a shared ClickHouse cluster couldn't handle hours-long modeling queries, and it lacked a cost-based query optimizer. DuckDB gave every customer their own instance, and tools like dbt could connect over Postgres. We're still fans.
But we underestimated how big and complex our customers' workloads would get. We didn't want them to have just a good experience, we wanted the best experience you can get when you pay someone else to run your warehouse. It should work at any scale, at a fair price.
So we spent the last three months re-architecting it, this time without DuckDB.
DuckDB is brilliant on one machine
We love DuckDB. It's probably the best single-node tool for analyzing heaps of data, and that node can be your laptop. It's robust and reliable. It almost always finishes your query, and if it runs out of memory, it spills to disk.
The same features that are great locally gave us problems in the cloud. Customers ran more complex queries than we expected, so we had to add huge instances. Adding disks was an option, but queries would have been too slow and expensive to be viable.
To run a single-node engine safely in the cloud, we have to size the worker before the query arrives. The ergonomics here are wonky. We couldn't find a good way to tell customers what resources their queries would need. Predicting CPU and memory for a specific query was even harder.
Users shouldn't have to worry about this. They should be able to run whatever they need to get their work done. Our job is to handle the rest and make it as predictable as possible.
We hit other bottlenecks too, like fetching lots of data from S3 without async fetching. DuckDB only added that recently.
DuckLake is built for compatibility, not scale
To use DuckDB as a fully-fledged data warehouse, we installed the DuckLake extension by default. It is a new lakehouse format from the same creators and follows the same principles as DuckDB: keep things simple and run on almost any setup. That works well up to a point, but at PostHog's scale, we needed something designed for distributed scale from the start.
DuckLake's catalog schema has to stay portable across many SQL databases, which limits engine-specific optimizations. At our scale, a single-table write could take more than three minutes because every commit re-read the statistics for the entire catalog.
We tuned DuckLake with table indexes and similar tweaks. But to keep offering DuckLake, we had to stay 100% compatible with its existing, "official" schema. This left us with fewer optimization options. [...]

## [73] Red-teamers found 11 ways for a misaligned agent to slip past Codex's Auto-review
TLDR AI | SNIPPET ONLY (TLDR AI: no readable article text (paywall, bot check, or not an article)) | ~58 words

An ERA fellow mentored at Apollo Research audited the open-source Codex harness and found 11 attacks that let a misaligned agent run arbitrary code despite the sandbox and the Auto-review blocking monitor. The exploits swap scripts behind trusted hooks, forge user turns the monitor can't tell from real ones, and edit files after approval. OpenAI has fixed several.

## [74] Poisoning 0.1% of pretraining data planted a remote-code backdoor in a coding agent
TLDR AI | full text via TLDR AI | ~351 words

Computer Science > Cryptography and Security
  [Submitted on 27 Oct 2026]
Title:Agentic Backdoors via Pretraining Poisoning
View PDF HTML (experimental)
            Abstract:Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI agent using a clean pipeline. Poisoning only 0.1% of the pretraining corpus with our new poison design implants the backdoor: the deployed agent executes the malicious command when the trigger is present while behaving normally on clean inputs. The attack success rate (ASR) increases with model scale, with the 4B model reaching roughly 92% ASR at a 0.1% poison rate and staying positive even when the poisoning rate drops to 0.0005%. Our code is available at this https URL.
    
Additional Features
Current browse context:
cs.CR
References & Citations
    
    Loading...
Bibliographic and Citation Tools
            Bibliographic Explorer (What is the Explorer?)
          
            Connected Papers (What is Connected Papers?)
          
            Litmaps (What is Litmaps?)
          
            scite Smart Citations (What are Smart Citations?)
          
Code, Data and Media Associated with this Article
            alphaXiv (What is alphaXiv?)
          
            CatalyzeX Code Finder for Papers (What is CatalyzeX?)
          
            DagsHub (What is DagsHub?)
          
            Gotit.pub (What is GotitPub?)
          
            Hugging Face (What is Huggingface?)
          
            ScienceCast (What is ScienceCast?)
          
Demos
Recommenders and Search Tools
              Influence Flower (What are Influence Flowers?)
            
              CORE Recommender (What is CORE?)
            
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

## [146] Athenahealth patients can ask Claude about their medical records now
ZDNet | full text via ZDNet | ~677 words

ZDNET’s key takeaways
- Athenahealth patients can consult Anthropic’s Claude.
- The partnership provides the AI with access to sensitive health information.
- Athenahealth claims the data cannot be used to train Anthropic models.
A major US healthcare technology provider just teamed up with Anthropic to connect patient health records with Claude.
Athenahealth, a healthcare technology provider serving over 20% of the US population, launched a Model Context Protocol (MCP) compatible server that connects to Anthropic’s Claude. The server, named AthenaPatient MCP, allows the AI model to gather information from health records and answer related questions. The process is secure, according to Athenahealth, and requires patients to sign in with their account credentials.
AthenaPatient MCP is available only to Claude Pro and Claude Max users, which cost $20 and $100 per month, respectively. Not all Athenahealth patients will have their data shared with Claude, and not all Claude Pro and Claude Max users must opt in. Users must give Claude their authenticated Athenahealth credentials, can choose which health information Claude can access, and can revoke access at any time, according to the press release.
More from ZDNET
Also: The wearable health boom is creating a data overload for doctors – what happens next
Once authorized, Claude takes patients’ information like lab results, vitals, medications, health conditions, immunizations, visit history, diagnostic reports, allergies, procedures, and care plans into account when answering questions.
The AI partnership does not provide medical advice, according to Sam Lambson, vice president of product management, data & ecosystem at Athenahealth, who responded to ZDNET in an email. It also should not replace a clinician’s professional judgment or medical advice. “Patients should contact a qualified healthcare professional with questions about diagnosis, treatment, or changes to their care,” Lambson said.
It appears that the AthenaPatient MCP tool is designed to help patients better understand the information provided by health professionals, rather than to give them medical advice. So, one may ask AthenaPatient MCP about their latest blood test results, such as “What was my most recent red blood cell count?” but users shouldn’t expect Claude to explain how an abnormally high or low count may affect them.
Not the first of its kind
Partnerships between big tech and big healthcare aren’t new. In fact, the collaboration between Athenahealth and Anthropic follows a larger trend across the health tech industry. [...]

## [128] One of Google’s Android partners turned 1.3 million set-top boxes into a botnet
The Verge | full text via The Verge | ~299 words

Google says one of its Android manufacturing partners secretly built a backdoor in 1.3 million devices and turned them into a botnet. The company says it has now dismantled the backdoor and “cut ties” with the manufacturer, the Shenzhen, China-based Videostrong Technology Co., which has been banned from building or selling certified Android devices or supplying software for them.
One of Google’s Android partners turned 1.3 million set-top boxes into a botnet
Google says a manufacturer ‘intentionally’ hijacked its devices with malware.
The infected devices were used without owners’ knowledge for “malicious activity,” like ad fraud, data exfiltration, and routing unauthorized network traffic. Google claims the “backdoor and botnet were intentionally developed, deployed, and operated for financial gain,” saying:
Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices. These secondary modules were conducting ad-fraud; silently enrolling infected devices into residential proxy networks; and loading additional malware onto XCPE-compromised devices. We also took action to disrupt the command and control (C2) domains that operate these affiliate modules. Because these affiliates each have diversified distribution channels for their modules beyond XCPE, we assess that taking down their C2 domains will sever access to at least 10 million additional compromised devices.
It wasn’t just one device that was impacted, either — the malware was found “built directly into many different device models and brands over multiple years.” Most of those were Android TV set-top boxes, but the botnet also infected other “Android-based IoT devices, including telehealth devices, karaoke machines, and digital signage devices.”
Google says Videostrong used “obfuscation techniques” to load the malware onto users’ devices after they booted up the hardware for the first time. Google also says it made changes to its review process for device manufacturers after this incident.

## [132] Germany says lawmakers’ iPhones may have been hacked with spyware
TechCrunch | full text via TechCrunch | ~372 words

The German government is warning politicians and public figures that they were targeted by government-backed spyware, days after Apple began sending out notifications warning victims that their iPhones may have been hacked.
Germany’s federal cybersecurity office, known as the BSI, said in a note over the weekend that it had become aware that members of the Bundestag, Germany’s parliament, and other unnamed notable individuals had received warnings from Apple that they may have been targeted by cyberattacks.
Per the Financial Times, German government spokesperson Stefan Kornelius said the government in Berlin was “taking the incident and the warning very seriously,” but he did not say who in the federal government had been targeted, including whether German chancellor Friedrich Merz was among them.
Apple periodically sends out threat notifications to people it thinks may have been targeted by spyware, which can steal messages, location data, and other sensitive information from their phones. This spyware often relies on zero-click exploits, which can hack individuals almost invisibly as they don’t require a victim to click on a link or open a file.
Apple does not attribute attacks to specific governments or say whether someone’s phone has actually been compromised. For that reason, the BSI said that anyone who receives an Apple threat notification “should therefore assume that their device may have been compromised.”
Others outside of Germany also received the recent threat alert from Apple. Radwan Mortada, a Beirut-based filmmaker, said in a post on X that he received a new threat notification warning that Apple had detected “another attack against your device,” after an earlier spyware attack targeted him in 2021.
It’s unclear who is behind this latest round of spyware attacks, or which government may have orchestrated the targeting. Per the notice received by Mortada, Apple said its latest batch of threat notifications went out to users in 99 countries.
The episode highlights again the murky business behind a growing number of attacks against members of civil society. Governments rarely build these tools themselves. Many buy them from private vendors, often called “mercenary spyware” makers, the best known being Israel’s NSO Group, which sells the controversial Pegasus spyware. Germany’s own central federal law agency, the BKA, reportedly bought access to Pegasus in 2019.

## [123] Proton apologizes to community after internal memo shows force behind proposed AI use in building its privacy products
TechRadar | full text via TechRadar | ~1028 words

Proton apologizes to community after internal memo shows force behind proposed AI use in building its privacy products
- Proton says it will not ‘re-interview’ some employees about how they use AI.
- The company promises "use of AI will never be at the expense of security".
- Proton CTO publishes internal AI manifesto on company blog.
Privacy-first software provider Proton appears to have rolled back on a decision to re-interview staff members about their AI use, after admitting that it hadn't "lived up to the high standard you ought to hold us to" in an announcement on social media.
The Swiss-based company outlined three promises to its community, which includes users of Proton Mail and Proton VPN, in a reaction to the leaked story that AI will be forced through the company with threats of job losses should staff not comply.
Alongside stating that it would not, in fact, re-interview staff and that there would be no AI-use related job losses, Proton also promised that its "use of AI will never be at the expense of security" and that it "does not install tracking software on employees' laptops to measure how much AI-generated code they produce".
In the statement on X, Proton also promised to publicly release and open source several of its internal tools as well as publish how code reviews and security reviews are done, to provide transparency and evidence that it delivers on its word.
The announcement comes alongside a wave of support from current staff members on Reddit and X all outing themselves by name and refuting much of what the initial leaked email had stated. Although many commenters on these platforms have suggested that this could instead be part of a coordinated PR response.
Proton's AI manifesto
What is certain is the company's commitment to using AI to drive itself forward. On Sunday 1 November, two days after the leak story was published, Proton CTO Bart Butler published the details of a company memo on AI use, the "AI @ Proton, Engineering Manifesto" which he had sent round to staff a month before the incident.
In it, Butler makes Proton's position on how its software engineers should be using AI crystal clear.
"Your job has fundamentally changed. It is no longer to write code, and LLMs are not here to help you write better code faster," he writes in bold. "Your job is to help the LLM write better code faster. Every engineer is now a team leader, a manager, and your direct reports are the models and agents you use.”
Perhaps not a huge leap, then, to thinking that there might well have been some credence in the leaked reports on staff re-interviews given how important and specific this requested use of AI was, regardless of whether or not jobs may or may not have been on the line. [...]

## [142] Your AI coding agent now runs on a budget — and it can cut you off mid-task
The New Stack | full text via The New Stack | ~1313 words

Your AI coding agent now runs on a budget — and it can cut you off mid-task
The days of pointing an AI agent at a backlog and letting it burn through compute without much oversight may be coming to an end. Cognition is introducing hierarchical budgets for Devin so enterprises can manage AI coding agent spending across departments, projects, and individual engineers. Administrators can assign budgets to different teams, track how much each one spends, and approve more capacity based on engineering efficiency. There’s a catch for developers, though; if a budget runs out while Devin is working on a task, the session stops.
If a budget runs out while Devin is working on a task, the session stops.
The feature grew out of conversations with customers, according to Lukas Burger, who works across go-to-market and engineering at Cognition. “Most of what we build starts with our forward deployed engineers (FDEs), who work on-site with customers. Budgets came straight out of those conversations,” Burger tells The New Stack. Once Devin moved past pilots and into broader deployments across organizations, he explains, the blunt controls that had worked for a single team — org limits, per-user tiers, and separate Devin Desktop settings — stopped holding up.
From Pilots to the P&L
The problem Budgets sets out to solve is one of scale and sprawl rather than raw price. “That’s fine for one team. It doesn’t hold up when a bank is dividing a large ACU commitment across hundreds of groups,” Burger tells The New Stack of the older spending controls. Some of those customers had started building and maintaining their own internal tools just to parcel out capacity to the leaders of each business line, a workaround that mapped the exact gap Cognition set out to close.
Cognition built the feature with some of the world’s largest enterprises as design partners, testing the model with customers managing millions of Agent Compute Units, the consumption-based units used to measure the work Devin performs.
Burger is keeping quiet on individual customer spending figures, but he is clear about what changes as deployments widen. “Devin stops belonging to one team,” he says. “A pilot might sit with a single platform group. A broad rollout means many departments, each with its own priorities and its own budget owner.”
Budgets follow the org chart
Budgets is designed to work with the way enterprises already manage spending, meaning, an administrator starts with one overall budget, divides it among business units, and from there, those leaders can distribute funds to their own teams and projects, with budgets extending up to three levels deep. Central IT can still see where the money is going and set limits without approving every request. [...]

## [156] Marvell to Buy Lumentum In $115 Billion Bet On AI Connectivity
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~89 words

Marvell has agreed to acquire optical components maker Lumentum in an all-stock deal with an implied enterprise value of $115 billion. "AI infrastructure is undergoing a fundamental architectural shift toward optical connectivity, creating an opportunity that comes along once in a generation," said Marvell Chairman and CEO Matt Murphy. "The companies that move first and help define this transition will set the standard for decades to come." CNBC reports: Through the acquisition, Marvell said it can combine electrical and optical technologies to meet accelerating and shifting AI connectivity de

## [35] Scaling Git at OpenAI
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~17 words

How OpenAI built Pando, a Git-compatible backend designed for the scale of development that Codex makes possible.

## [168] Radeon RADV Vulkan Driver Adopts An LLM Policy
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~30 words

The Mesa RADV driver that provides Vulkan API support for AMD Radeon GPUs on Linux has adopted its own policy around AI / large language models (LLMs) for code contributions...

## [133] Web host Squarespace lays off 19% of its employees
TechCrunch | full text via TechCrunch | ~317 words

Squarespace, the web company that helps customers build and host their own websites, is laying off about one-fifth of its workforce, in a move that will affect hundreds of jobs.
Jeff Seedman, a public relations specialist representing Squarespace, confirmed the layoffs to TechCrunch. The Verge initially reported the layoffs.
“Squarespace is restructuring its organization and reducing its global workforce by approximately 19%, representing around 300 employees,” said Seedman. “The changes are intended to simplify how we operate, sharpen our priorities and enable the company to move faster as we position Squarespace for its next phase of growth.”
Website building has changed immensely over the last few years as a result of the generative AI boom. “Vibe-coding” website builders, which only require simple prompts from users to spin up functional front-end designs, have largely upended the industry, making it possible for users to create sites with significantly less effort.
These kinds of sites have become an increasingly central part of the website-building business. Last year, web host rival Wix bought Base44 for $80 million. Similar offerings, like Lovable, have generated significant investor interest; Lovable raised a $400 million Series C round in August that valued the company at $13.3 billion. Google also recently launched Stitch, a feature that allows users to swiftly generate user-interface designs.
Squarespace has also begun a big push into AI. In 2024, the company launched an AI tool called Blueprint. The company also recently announced Forma, an upcoming AI native platform, whose waitlist users can join.
Squarespace was founded in 2004 and went public in 2021 at a $10 billion valuation. However, the company struggled in the ensuing years to generate enthusiastic public market interest. Squarespace ultimately decided to go private again by way of a $7 billion private equity deal in 2024.
An earlier version of this report incorrectly stated that Squarespace had not yet launched AI tools; the story has been updated.

## [24] This background sound leaks your exact location
Lobsters | SNIPPET ONLY (Lobsters: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [174] Linux 7.4-rc1 Released With Nice Performance Improvements, AMD Ryzen Zen 6 Preparations & AMDGPU HDMI 2.1 Default
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~22 words

Even with Linus Torvalds having been on holiday, Linux 7.4-rc1 is out today on-schedule for capping off the Linux 7.4 merge window...

## [66] How Binance's $6.3 Billion Hack Went Down
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~87 words

A string of unusual transactions started to cause alarm at Binance on Thursday afternoon. Binance's top executives put together an informal war room with about 100 participants in response and worked through the night to navigate one of the most damaging crises in Binance's history. The company was forced to halt deposits and withdrawals as more than $6 billion was drained from the exchange. This article details how the hack unfolded based on interviews with people with knowledge of the events and analyses by crypto forensics firms.
