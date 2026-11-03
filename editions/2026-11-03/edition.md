---
date: 2026-11-03
edition: 42
schema_version: 1
generated_at: 2026-11-03T01:36:18+00:00
sources_ok: 43
sources_total: 47
fetched: 405
candidates: 188
full_text: 13
---

# The Brief

- Models are starting to edit the machinery they run on: GPT-6 Astra rewrote a small model's weights to fix its math, while Anthropic's own filing says it may soon cross its threshold for recursive self-improvement.
- Security takes most of the day: an unpatched critical Ubuntu kernel flaw, a backdoor planted through pretraining data, and a botnet built into 1.3 million Android set-top boxes.
- Agents are becoming enterprise infrastructure that needs governance, from Uber's registry of 5,000 tools to Cognition's spending budgets that can stop a session mid-task.
- Infrastructure teams are reporting what breaks at scale: PostHog is leaving DuckDB, and Shopify rebuilt its exposure scanner to trust the cluster over the repository.

# Stories

## GPT-6 Astra edits a small model's raw weights and lifts its MATH-500 score from 7.9% to 48.1%
- ids: 1
- topic: AI
- signal: must-read
- url: https://rikiyat.github.io/blog/weight-space-programming/
- event: astra weight programming qwen math
- original title: Astra can read and write weights to improve Qwen
- source: rikiyat.github.io | https://rikiyat.github.io/blog/weight-space-programming/ | via Hacker News
- author: Rikiya Takehi et al.
- image: https://rikiyat.github.io/images/blog/weight-space-programming.png
- read: 15 min
- discuss: https://news.ycombinator.com/item?id=50341174 | Hacker News | 1901 points | 602 comments
- full text: yes

> Editing 0.016% of the weights, with no training loop and no gradients, also tripled the model's instruction-following score on a benchmark it was never tuned for.

The write-up from the team behind GPT-6 Astra argues that current frontier language models can read a neural network's raw weights and work out what the network computes, and can write new weights from a plain-language goal. The authors call the approach Weight-Space Programming. In their tests, Astra wrote small game-playing networks from scratch that beat networks trained with PPO for 100 million steps, and it did so without any environment feedback.

The sharper example is a fix to Qwen3.5-0.8B. Asked to make the model better at math without gradient training, Astra found weights that were causing reasoning loops, the same loops Qwen's own model card warns about, and corrected them by changing about 0.016% of the weights. Under identical sampling settings, MATH-500 accuracy went from 7.9% to 48.1%. IFEval, which the edit did not target, roughly tripled.

The result matters for two reasons. It suggests that LLMs could replace hand-designed optimizers like Adam or Muon as the thing that shapes weights, and it hints that a model can explain what a given network part is for, which is the interpretability claim. Neither claim has been checked by outside labs in the material available here, and the write-up is a single lab's account of its own experiments. Independent reruns on the base model are the test that would settle the math numbers.

**Takeaways**
- Rerun MATH-500 on the unmodified Qwen3.5-0.8B with the same sampling settings before treating the 7.9% to 48.1% jump as settled.
- Watch for outside replications of a weight edit that holds on benchmarks the edit did not target.

## Anthropic's revised S-1 says it may soon reach its own threshold for recursive self-improvement
- ids: 120
- topic: AI
- signal: must-read
- url: https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/
- event: anthropic s1 recursive self improvement threshold
- original title: Anthropic warns that it’s very close to RSI capability, aka self-building AI
- source: TechCrunch | https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/
- author: Julie Bort
- image: https://techcrunch.com/wp-content/uploads/2026/11/Recursive-Neural-Spiral-in-Circuitry.png?resize=1200,600
- read: 3 min
- full text: yes

> The risk factors section also says Anthropic already used AI to build models whose capability jumps it did not recognize at the time.

Most of the coverage of Anthropic's revised S-1A has focused on its financials, which show revenue rising quickly alongside higher expenses. TechCrunch found a more consequential passage in the risk factors. The company says its internal estimates for future models suggest it may imminently meet the threshold in its Responsible Scaling Policy for "dramatically accelerated progress attributable to AI." That threshold is how the company defines recursive self-improvement, the point where AI speeds up its own training enough to change the pace of progress.

The filing also says Anthropic has used AI in its own R&D to develop models whose leaps it did not notice when they happened, and that it may not spot a major acceleration until after it has occurred. The company states that none of its current models has been designated as crossing the threshold, and that it is still assessing the underlying data. It also commits to keeping humans in the R&D process for the foreseeable future.

What is unresolved is how Anthropic measures "dramatically accelerated," and whether the threshold determination will be shared with anyone outside the company. The filing puts the question into a document that investors will read, which turns a safety-policy trigger into a near-term reporting question. Anyone tracking frontier model risk now has a specific claim to check against the next model release.

**Takeaways**
- Read the Responsible Scaling Policy's definition of the threshold, then compare it against the next Anthropic model card that describes AI-assisted R&D.
- Watch whether Anthropic publishes a formal threshold determination with its next major model release.

## Ubuntu has shipped no fixed kernel for CVE-2026-98432, a CVSS 9.8 flaw, nearly three weeks after it surfaced
- ids: 4
- topic: Security
- signal: must-read
- url: https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432
- event: ubuntu kernel cve 98432 unpatched lts
- original title: Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks
- source: freenode.net | https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432 | via Hacker News
- author: Relay
- image: https://freenode.net/media/og-default.png
- read: 1 min
- discuss: https://news.ycombinator.com/item?id=50341462 | Hacker News | 324 points | 76 comments
- full text: yes

> None of the three current LTS releases has a patched kernel, and Ubuntu has not published an estimated date for one.

The Hacker News thread describes an unfixed Linux vulnerability that is scored 9.8 on CVSS, the top tier of severity for most scoring. Ubuntu's 22.04, 24.04 and 26.04 LTS kernels have no official update that closes it, and the gap has been open for close to three weeks. The reporting describes the flaw as enabling a remote or local attack, but the excerpt does not give the exact vector or the affected kernel builds, so those details need to come from the CVE record.

The exposure is greatest where the kernel is the isolation boundary. Internet-facing servers and multi-tenant self-hosted systems rely on the LTS kernel to separate users and privileges, and until packages appear those machines remain open to whatever the CVE allows. Ubuntu has not said when fixes will arrive.

Administrators are left with three choices: keep the stock kernel and accept the risk, apply any out-of-tree mitigation that exists, or move workloads to a release or kernel that already contains the fix. The article does not establish whether a mitigation exists, so that question has to be answered from the vendor advisory before anyone relies on one.

**Takeaways**
- Check the CVE record and Ubuntu's security tracker for the affected kernel versions, then list which hosts run them.
- On multi-tenant hosts, cut local user access and restrict exposed services until a patched kernel is installed.

## Planting 0.1% poisoned text in pretraining data can make a coding agent run attacker commands
- ids: 74
- topic: Security
- signal: recommended
- url: https://arxiv.org/abs/2610.37741
- event: pretraining poisoning agent backdoor remote code
- original title: Poisoning 0.1% of pretraining data planted a remote-code backdoor in a coding agent
- source: arxiv.org | https://arxiv.org/abs/2610.37741 | via TLDR AI
- author: Hu et al.
- read: 2 min
- full text: yes

> The largest model tested ran the attacker's command about 92% of the time at that poison rate, and the backdoored agent behaved normally on clean inputs.

Researchers from Anthropic, UC Berkeley and UIUC show that text seeded into web pages that get scraped for pretraining can give an agent a remote code execution backdoor. Their setup pretrained Qwen3 models from scratch at 0.6B, 1.7B and 4B parameters, then post-trained each into a command-line agent. When a trigger appears, the deployed agent executes an attacker-chosen command on the user's machine.

The attack needs very little data. Poisoning 0.1% of the pretraining corpus was enough for the 4B model to reach about 92% attack success. The paper reports that success rises with model size and stays above zero even when the poison rate drops to 0.0005%. The agent's normal behavior on clean inputs is what makes the backdoor hard to spot in routine testing.

The threat extends past the people who operate a model. Anyone who can publish text that gets scraped can reach future models, which makes pretraining data a supply-chain surface. The abstract does not show whether safety post-training removes the trigger at scale, or whether corpus scanning finds the poison design. Those are the results that would change how serious this is for deployed agents.

**Takeaways**
- Keep command-running agents behind confirmation prompts and a sandbox, especially when the base model came from uncurated web data.
- Watch for corpus-scanning or post-training results that test this specific trigger design.

## Shopify rebuilt its exposure scanner on cloud inventory after repository checks produced false alarms
- ids: 48
- topic: Security
- signal: recommended
- url: https://www.infoq.com/news/2026/11/shopify-kubernetes-ingresses/
- event: shopify overexposed scanner ingress cloud run
- original title: Shopify Overexposed Scans GKE Ingresses and Cloud Run for Exposure
- source: InfoQ | https://www.infoq.com/news/2026/11/shopify-kubernetes-ingresses/
- author: Claudio Masolo
- image: https://res.infoq.com/news/2026/11/shopify-kubernetes-ingresses/en/headerimage/generatedHeaderImage-1793520999206.jpg
- read: 4 min
- full text: yes

> Checking what the cluster enforces rather than what the repository declares cut inconclusive Ingress verdicts by about 80% within a few weeks of tuning.

Shopify's first internal scanner for internet-exposed services read infrastructure repositories and probed the hostnames it found. The team said it failed in three ways. Proxy authentication annotations caused false positives. Admission controllers that rewrite settings could make a correct-looking config do nothing in clusters where they did not run. Ingresses created by other repositories or by platform tooling were never seen at all.

The replacement, named Overexposed, queries GCP Cloud Asset Inventory for Ingresses that GKE has accepted after admission, plus Cloud Run services and load balancers, and reads access policies without cluster credentials. Each candidate receives one anonymous request. The scanner tries HEAD, falls back to GET, follows at most three redirects, and tests case variants such as /ADMIN. Results fall into six verdicts, from exposed and expected through protected and inconclusive. A 404 on Cloud Run can come from Google's front end before the app runs, and a 403 is not treated as proof of protection, so the scanner checks whether allUsers holds the invoker role.

The team's conclusion is that the repository shows intent and the cluster shows what is enforced. The write-up does not say how many services turned out to be exposed or how findings were handled, so the scale of the original gap is not measured here.

**Takeaways**
- Compare repo-declared ingress and IAM settings with what your cloud inventory reports, starting with Cloud Run services that grant allUsers the invoker role.
- Expire allowlist entries automatically when an endpoint stops being open, so a stale exception does not hide a later exposure.

## Google says an Android partner turned 1.3 million set-top boxes into a botnet through a built-in backdoor
- ids: 128
- topic: Security
- signal: recommended
- url: https://www.theverge.com/1024807/google-botnet-android-tv-shut-down
- event: videostrong android botnet set top boxes
- original title: One of Google’s Android partners turned 1.3 million set-top boxes into a botnet
- source: The Verge | https://www.theverge.com/1024807/google-botnet-android-tv-shut-down
- author: Stevie Bonifield
- image: https://platform.theverge.com/wp-content/uploads/sites/2/2026/11/videostrong-android-tv-device.jpg?quality=90&strip=all&crop=12.458333333333%2C0%2C87.541666666667%2C100&w=1200
- read: 2 min
- full text: yes

> Google estimates that taking down the command servers for the criminal affiliates cuts off access to at least 10 million more compromised devices.

Google says Videostrong Technology, a Shenzhen manufacturer and Android partner, built a backdoor into devices that became a botnet of about 1.3 million units. Google says it dismantled the backdoor, cut ties with the company, and banned Videostrong from building certified Android devices or supplying software for them. The backdoor was found in many device models and brands over several years, mostly Android TV set-top boxes, though telehealth devices, karaoke machines and digital signage were also affected.

Videostrong sold access to criminal affiliates, who loaded ad-fraud modules, silently enrolled devices into residential proxy networks, and installed further malware. The malware activated after a device's first boot, using obfuscation to hide what it was loading. Google says it disrupted the command-and-control domains those modules use.

Google also says it changed its review process for device manufacturers. The write-up does not say how many of the 1.3 million devices have been cleaned up, or how owners of boxes that no longer get updates can remove the malware, and those are the points that decide how much of the botnet is actually gone.

**Takeaways**
- Check whether any cheap Android TV box on your network is from a brand that no longer ships updates, and replace or wipe it.
- Watch for unexplained outbound traffic from IoT devices, which is how residential proxy abuse usually shows up.

## Germany warns that lawmakers may have been targeted by government spyware, after Apple's threat notifications went out
- ids: 132
- topic: Security
- signal: recommended
- url: https://techcrunch.com/2026/11/02/germany-says-lawmakers-iphones-may-have-been-hacked-with-spyware/
- event: apple threat notification germany spyware bundestag
- original title: Germany says lawmakers’ iPhones may have been hacked with spyware
- source: TechCrunch | https://techcrunch.com/2026/11/02/germany-says-lawmakers-iphones-may-have-been-hacked-with-spyware/
- author: Zack Whittaker
- image: https://techcrunch.com/wp-content/uploads/2026/08/ios-notification-threat-apple-hero.jpg?resize=1200,814
- read: 2 min
- full text: yes

> Apple's latest batch of notices reached users in 99 countries, and Germany's cybersecurity office told recipients to assume their devices may be compromised.

Germany's federal cybersecurity office, the BSI, said that members of the Bundestag and other unnamed notable people had received Apple threat notifications warning that they may have been targeted. The office told anyone who receives one to assume their device may be compromised. The German government said it is taking the warning seriously, but did not say who in federal government had been targeted, or whether Chancellor Friedrich Merz was among them.

Apple does not attribute its notices to any government, and it does not confirm that a particular phone was compromised. The spyware involved often relies on zero-click exploits, which need no link click or file open. A filmmaker in Beirut reported a new notice, following an earlier 2021 attack against him, and Apple said this round went to users in 99 countries.

The episode also points to the market behind it. Governments often buy spyware from private vendors, and Germany's BKA reportedly bought access to Pegasus in 2019. The article does not say whether those earlier purchases are connected to these alerts, and nobody has publicly named the government behind this round.

**Takeaways**
- If you get an Apple threat notification, update the device, consider Lockdown Mode if you face elevated risk, and have a trusted security group examine the phone.
- Watch whether the German government or Apple names the spyware vendor, which would narrow who is responsible.

## PyTorch on TPUs gets an open-source native backend, and Google says DeferAndFuse runs 50% faster than strict eager
- ids: 29
- topic: AI
- signal: recommended
- url: https://www.infoq.com/news/2026/11/torchtpu-native-pythorch-tpu/
- event: torchtpu google meta pytorch tpu
- original title: Google and Meta Open-source TorchTPU to Bring Native PyTorch Support to Google TPUs
- source: InfoQ | https://www.infoq.com/news/2026/11/torchtpu-native-pythorch-tpu/
- author: Sergio De Simone
- image: https://res.infoq.com/news/2026/11/torchtpu-native-pythorch-tpu/en/headerimage/torchtpu-1793636927771.jpeg
- read: 3 min
- full text: yes

> Google reports testing about 5,000 Hugging Face models across more than 500 architectures, with the TPU results coming from its own benchmarks.

Google and Meta have released TorchTPU as open source, a native PyTorch backend for Google TPUs. It replaces the older PyTorch/XLA path, which Google says required invasive code changes to mark compilable regions, had long compile times, and lacked native eager execution. Under TorchTPU, moving code off GPUs mostly means swapping the cuda device for tpu and the NCCL distributed backend for the TPU one, or using a new accelerator API to detect the hardware.

TorchTPU supports three eager modes: strict, debug and a hybrid called DeferAndFuse, which Google says can be 50% or more faster than strict eager while using less peak HBM memory. To test coverage, Google ran about 5,000 Hugging Face models in eager and compiled modes on TPU generations from v5e onward. It also reported 25.7k tokens per second on a single TPUv7 chip for a 30-billion-parameter model at a 5,120-token sequence length.

The article reports Google's own numbers and does not compare them with GPUs at equal cost. It also does not say how many of the 5,000 models ran unchanged and how many needed fixes. Teams weighing TPUs against GPUs need both figures before the portability claim means much for them.

**Takeaways**
- Before trying TPUs, list the places in your PyTorch code that hard-code cuda or NCCL, since those are the edits the migration requires.
- Benchmark your own model's eager and compiled throughput on TPU rather than relying on the published figures.

## PostHog is moving its warehouse off DuckDB, citing cloud sizing limits and slow DuckLake commits
- ids: 10
- topic: Infra
- signal: recommended
- url: https://posthog.com/blog/moving-off-duckdb
- event: posthog duckdb ducklake warehouse migration
- original title: Moving our warehouse off DuckDB
- source: posthog.com | https://posthog.com/blog/moving-off-duckdb | via Hacker News
- image: https://res.cloudinary.com/dmukukwp6/image/upload/moving_off_duckdb_4c95538aac.png
- read: 5 min
- discuss: https://news.ycombinator.com/item?id=50338747 | Hacker News | 159 points | 107 comments
- full text: yes

> At that size, one write to a single table could stall for over three minutes, since each commit reloaded metadata for every table in the catalog.

PostHog rebuilt its warehouse on DuckDB five months ago, instead of ClickHouse, because a shared ClickHouse cluster could not handle hours-long modeling queries and lacked a cost-based optimizer. DuckDB gave each customer its own instance, and dbt could connect over Postgres. The team now says customers' workloads grew larger and more complex than expected. On one machine, the only safe approach was to size the worker before each query arrived, and PostHog could not give customers a reliable way to predict CPU and memory needs for a given query.

The next step was DuckLake, the lakehouse format from DuckDB's creators, which PostHog enabled by default. Its catalog schema has to stay portable across many SQL databases, which rules out engine-specific optimizations. Table indexes and similar tweaks helped, but staying compatible with the official schema limited the options. The article excerpt does not name the replacement engine or give cost figures, so the full post is needed to see what PostHog chose.

The lesson PostHog draws is that single-node engines are excellent for analysis and hard to run as a cloud service for many customers. Its move suggests the problem was not DuckDB's speed on one machine but predictability once every customer's query can grow without limit.

**Takeaways**
- If you use DuckLake for frequent writes, measure commit latency on your largest table before depending on it.
- Size single-node workloads by the peak memory of your heaviest query, not its average.

## Uber's MCP Gateway puts more than 800 internal servers and 5,000 tools behind one registry and proxy
- ids: 39
- topic: Dev Tools
- signal: recommended
- url: https://www.infoq.com/news/2026/11/uber-mcp-gateway-ai-agents/
- event: uber mcp gateway internal tools agents
- original title: Uber Builds MCP Gateway to Govern Access to 800+ Servers and 5,000+ AI Agent Tools
- source: InfoQ | https://www.infoq.com/news/2026/11/uber-mcp-gateway-ai-agents/
- author: Leela Kumili
- image: https://res.infoq.com/news/2026/11/uber-mcp-gateway-ai-agents/en/card_header_image/generatedCard-1791755959439.jpg
- read: 2 min
- full text: yes

> Newly discovered tools stay disabled until their owning team enables them, and authorization is enforced at both the server and the tool level.

Uber has built an MCP Gateway so AI agents can discover and call internal services through one path. The platform covers more than 800 MCP servers and 5,000 tools. It separates a registry, which holds tool definitions, schemas, ownership and enablement settings, from a proxy that translates MCP requests into HTTP, gRPC or TChannel calls and converts the responses back. Existing APIs are exposed as tools without changes to the services behind them.

Discovery is automated. A crawler called AutoCrawler scans internal interface definitions written in Protocol Buffers and Thrift, generates MCP schemas, and uses a language model to write tool descriptions. New tools remain off until the owning team enables them, and configuration changes reach the data plane without restarts. Access checks run through Uber's internal access control, responses can be redacted for personal data, and a separate service swaps internal tokens for third-party tokens for integrations such as Jira and Google.

Commentators quoted in the article compared the design with API gateways built for REST and GraphQL, and the article itself notes that loading thousands of tool definitions into an agent's context gets expensive as the catalog grows. The excerpt does not show how Uber handles that second problem.

**Takeaways**
- If you expose internal tools to agents, keep new ones disabled until an owner reviews them.
- Measure how many tool definitions your agents load into context, since that cost grows with the catalog.

## Cognition adds hierarchical budgets to Devin, and a session stops when its budget runs out mid-task
- ids: 142
- topic: Dev Tools
- signal: recommended
- url: https://thenewstack.io/22842541cognition-devin-hierarchical-budgets/
- event: cognition devin budgets agent spending
- original title: Your AI coding agent now runs on a budget — and it can cut you off mid-task
- source: The New Stack | https://thenewstack.io/22842541cognition-devin-hierarchical-budgets/
- author: Amanda Caswell
- image: https://cdn.thenewstack.io/media/2026/11/349bc6a4-getty-images-um5wntq2sf0-unsplash-scaled.jpg
- read: 6 min
- full text: yes

> Administrators can nest budgets up to three levels deep, from a business unit down to an individual engineer, without approving each request.

Cognition has launched Budgets for Devin, a way for enterprises to cap what AI coding agents spend across departments, projects and individuals. An administrator sets an overall budget, divides it among business units, and those leaders split their share among teams and projects. Administrators can see spending by team and approve more capacity based on engineering efficiency. The company says it built the feature with large enterprises as design partners, and tested it with customers managing millions of Agent Compute Units, the unit it uses to bill for Devin's work.

The cost for developers is that a session halts once its budget is exhausted, even partway through a task. Cognition says the idea came from forward-deployed engineers working on-site with customers, who found that older controls, such as org-wide caps, per-user tiers and Devin Desktop's own settings, no longer worked once Devin spread across whole companies. The article does not disclose individual customer spending.

It does not say whether a stopped session can be resumed, or whether partial work is kept. Those details decide how disruptive a cutoff is, and they matter more to a team in the middle of a large refactor than the budget hierarchy does.

**Takeaways**
- Before rolling out shared agent budgets, test what happens to a stopped session's partial work and how to resume it.
- Set budgets per team rather than only at the organization level, so one group's runaway task cannot drain the pool.

## Proton backs off plan to re-interview staff over AI use, and publishes its engineering AI manifesto
- ids: 123
- topic: Engineering
- signal: recommended
- url: https://www.techradar.com/vpn/vpn-services/proton-apologizes-to-community-after-internal-memo-shows-force-behind-proposed-ai-use-in-building-its-privacy-products
- event: proton ai memo staff manifesto
- original title: Proton apologizes to community after internal memo shows force behind proposed AI use in building its privacy products
- source: TechRadar | https://www.techradar.com/vpn/vpn-services/proton-apologizes-to-community-after-internal-memo-shows-force-behind-proposed-ai-use-in-building-its-privacy-products
- author: Dan Sung
- image: https://cdn.mos.cms.futurecdn.net/SHGbmBuxgHmweVxr9SmYd6-2560-80.png
- read: 5 min
- full text: yes

> Proton promised no AI-linked job losses and no tracking of how much AI-generated code each engineer produces.

Proton, the Swiss privacy software company behind Proton Mail and Proton VPN, appears to have dropped a plan to re-interview staff about their AI use. The reversal followed a leaked internal email that reportedly tied AI adoption to job losses for staff who did not comply. In a public statement, Proton apologized for not meeting the standard its users expect, and made three promises, including that AI use would never come at the expense of security.

The company also said it would publish and open source several internal tools, along with its code and security review processes. Several current employees publicly backed the company's account, though some commenters suggested the response was coordinated.

On November 1, Proton's CTO, Bart Butler, published an engineering memo he had sent staff a month earlier. It tells engineers that their role has shifted from writing code to directing the models and agents they use, and it describes each engineer as a manager of those tools. The published tooling and review documents are the checkable part of Proton's commitment, and whether they arrive is the open question.

**Takeaways**
- If you manage engineers, make sure AI-usage metrics are not used for individual employment decisions without a written policy.
- Watch whether Proton publishes the promised review processes and tools, since those can be checked against the commitments.

## Squarespace cuts about 19% of its staff, roughly 300 jobs, in a restructuring as it pushes further into AI
- ids: 133
- topic: Startups
- signal: notable
- url: https://techcrunch.com/2026/11/02/web-host-squarespace-lays-off-19-of-its-employees/
- event: squarespace layoffs restructuring workforce
- original title: Web host Squarespace lays off 19% of its employees
- source: TechCrunch | https://techcrunch.com/2026/11/02/web-host-squarespace-lays-off-19-of-its-employees/
- author: Lucas Ropek
- image: https://techcrunch.com/wp-content/uploads/2024/10/F064_Q324_Refresh_Product_BlueprintPersonalityStep_Press_1920x1080-Logo.jpg?resize=1200,675
- read: 2 min
- full text: yes

> The cut comes as AI site builders such as Lovable reshape the market, and Squarespace is preparing its own AI-native platform called Forma.

Squarespace is laying off about 19% of its workforce, around 300 employees, as part of a restructuring that the company says is meant to simplify operations and move faster. The Verge first reported the cuts, and a company spokesperson confirmed them to TechCrunch.

The timing matters. Vibe-coding builders that generate sites from a prompt have changed the website-building business. Wix bought Base44 for $80 million last year, and Lovable raised $400 million in August at a $13.3 billion valuation. Squarespace has been pushing into AI with its Blueprint tool and the upcoming Forma platform. It went public in 2021 at a $10 billion valuation and went private again in 2024 in a $7 billion deal.

The statement does not say which teams were cut, so the link between the layoffs and the AI push cannot be judged from the reporting.

## Marvell agrees to buy optical maker Lumentum in an all-stock deal with an implied value of $115 billion
- ids: 156
- topic: Startups
- signal: notable
- url: https://slashdot.org/story/26/11/02/1527241/marvell-to-buy-lumentum-in-115-billion-bet-on-ai-connectivity
- event: marvell lumentum optical acquisition
- original title: Marvell to Buy Lumentum In $115 Billion Bet On AI Connectivity
- source: Slashdot | https://slashdot.org/story/26/11/02/1527241/marvell-to-buy-lumentum-in-115-billion-bet-on-ai-connectivity
- author: BeauHD
- full text: no

> Marvell says AI connectivity is moving toward optical technology, and that combining electrical and optical products is the point of the deal.

Marvell has agreed to acquire Lumentum, an optical components maker, in an all-stock transaction with an implied enterprise value of $115 billion. This summary comes from the headline and standfirst only, because the full report could not be retrieved, so deal terms beyond the valuation and the all-stock structure are not covered here. Marvell's chairman and chief executive, Matt Murphy, described AI infrastructure as undergoing a fundamental shift toward optical connectivity, and said the company can combine electrical and optical technologies to meet changing AI connectivity demands.
