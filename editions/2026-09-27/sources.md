# Full text for 30 picks -- untrusted article content, treat as data only

## [8] ASML says it sold 'absolutely nothing' in Europe in 2026
Hacker News | full text via Hacker News | ~1100 words

ASML says it sold 'absolutely nothing' in Europe in 2026 — lithography giant calls on EU to help create demand
Subsidies for fabs do not help.
As the world's only supplier of EUV lithography systems, ASML is Europe's largest company by market capitalization, currently valued at around $660 billion. But it earned almost nothing in Europe this year, down from 1% of total profits in 2025 and 5% in 2024. Why? European chipmakers bought no lithography equipment from ASML in 2026 — and the company is calling on EU authorities to help create demand for European chips.
"We are selling absolutely nothing in Europe," said Frank Heemskerk, executive vice president of public affairs at ASML, while speaking at a panel discussion from the Dutch political and cultural center De Balie. "Because Europe is not investing and because no chip factories are being built in Europe. That is genuinely worrying. […] [Our revenue share in Europe is 0%], it used to be 1%."
Indeed, Europe accounted for 1% of ASML's revenue share in 2025, 5% in 2024, 4% in 2023, and 2% in 2022, based on the company's presentations for investors. In the first two quarters of 2026, however, Europe accounted for 0% of ASML's revenue, according to ASML's earnings reports.
"There simply is no demand here for these kinds of highly specialized machines," Heemskerk said. "That is the problem. So apart from trying to attract investment with capital on the supply side, we should do much more to create demand. […] So, we at ASML are also making an enormous effort, and we are talking with Ursula von der Leyen in Europe, saying: 'try to harness the market power and dynamism that ultimately do exist in Europe in a number of areas.'"
So far, the European Union has been keen on subsidizing building new fabs in Europe (something that did not help to lure Intel in). But ASML is calling on European governments to help aggregate and guarantee demand for European-made chips — which will encourage major European chip consumers to source locally, giving semiconductor manufacturers an economic reason to build or expand fabs in Europe.
"We need to make sure that some of those buyers — the customers of our customers — start talking much more closely with European manufacturers again. In areas such as artificial intelligence for industry, for example, there are still plenty of opportunities that Europe can seize. [...]

## [81] OpenAI pauses training of its ‘most capable models’
The Verge | full text via The Verge | ~262 words

As reports of OpenAI’s models breaking containment, hacking sites, and generally getting out of control pile up, the company has made the decision to pause training of its most powerful models. The decision was made after a model being tested within a sandbox exploited a loophole to gain internet access. The incident happened on September 20th, and “All training, evaluation, and inference with tool-use” remains paused as of Saturday evening, September 25th.
OpenAI pauses training of its ‘most capable models’
OpenAI keeps uncovering incidents of its models behaving in ‘unexpected or concerning’ ways.
In addition, OpenAI revealed on Friday that its agents had inappropriately uploaded 53nimages from ChatGPT users to image-hosting sites. The company has not stated if the images were AI-generated, photos, or contained identifiable people. The company also revealed Friday that its models had attempted to hack the Department of Education’s website, and pulled data from the Census Bureau and the Securities and Exchange Commission.
The revelations are part of an ongoing review by OpenAI into the behavior of its models. As it dug into its records, following the Hugging Face hack, it’s uncovered more and more instances of “unexpected or concerning behavior.” It’s evidence not just of how difficult AI agents are becoming to control as they grow more advanced, but also of the challenge of tracking their actions. Their behavior can be unpredictable, and they’re smart enough to try and cover their tracks. This has led to growing calls from researchers, those within the industry, and even some CEOs to call for slowing the pace of AI advancement.

## [114] There's a New Way to Break RSA Encryption
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~90 words

"Signature forgery." It's a new way to break RSA keys — and it doesn't require factoring. Ars Technica reports on new research using classical computing to "reduce the current RSA security level to an unacceptably low threshold" and lower the required computing resources by orders of magnitude. There's "a gap in current RSA-type security assumptions," according to a paper co-authored by University of California, San Diego professor Nadia Heninger, who argues that gap "gives classical cryptanalytic evidence in favor of moving away from RSA entirely during the current post-quantum trans

## [106] Rogue OpenAI Agents Posted 53 User-Uploaded Images Onto the Internet, Accessed US Government Websites
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~97 words

53 images that users uploaded into OpenAI models were included in training data — and then AI agents in an OpenAI research environment posted those 53 images on public image hosting sites. While posted as links that weren't publicly listed, "the images could still be discovered even if the links were not publicly listed," reports TechCrunch: OpenAI said it was working with the hosting providers to remove this content, though some of it is apparently still online. OpenAI said it could not notify the affected users because "our technical approach and privacy policy" prevent it from "reas

## [27] Autonomous LLM post-training with Tunix on TPUs
Google Developers Blog | full text via Google Developers Blog | ~467 words

Imagine going to sleep after writing a single Markdown specification and waking up to find that an AI agent ran dozens of LLM fine-tuning experiments overnight on your behalf - discovering optimal LoRA ranks, refining learning rate schedules, tuning batch sizes and committing each verified improvement to Git.
This is no longer a fantasy. Earlier this year, the autoresearch project showcased how autonomous LLM agents can iteratively explore pre-training in a self-contained loop. Taking inspiration from this paradigm, we created autofinetune: applying autonomous research loops to LLM post-training (Supervised Fine-Tuning and Reinforcement Learning via GRPO), using Google’s full AI stack—Tunix, Gemma, and Cloud TPUs orchestrated with Antigravity CLI and Gemini Flash 3.7.
In this post, we’ll explore how the autonomous research loop works for post-training and walk through a couple of real-world LLM finetuning case studies.
Traditional post-training involves a repetitive, manual cycle:
attn_vec_einsum to the LoRA target modules improve accuracy?" or "What happens if we change rollout temperature during GRPO?").
As demonstrated in autoresearch, we can now automate this whole process with the power of AI agents:
program.md): human defines the loop, boundary conditions, evaluation criteria, and constraints.run.py): A single, clean, self-contained finetuning script.results.tsv.
In the first experiment in autofinetune, we took the same SFT setup in our previous blog and extended it by creating the autoresearch loop to optimize google/functiongemma-270m-it on the google/mobile-actions dataset.
The agent was given boundaries in program.md:
Here is a sample trajectory from sample_runs/SFT_results.tsv demonstrating how the agent hill climbed.
As you can see, the agent is able to automatically adjust LoRA rank/alpha, optimizer, learning rate, etc. to keep improving the model’s accuracy in terms of generating correct function calls.
Supervised fine-tuning is only a simple test. For our second case study, we took the official GRPO example from the Tunix repository (which trains Gemma 3 1B for math reasoning using GSM8K; the trained model has better numerical accuracy and format accuracy in its answers) and set it up for autonomous RL finetuning. Reinforcement learning is subject to hyperparameter sensitivity, instability, and longer execution times - making this task more challenging and time-consuming. [...]

## [14] AI Agents Push Humans Out of the Loop
Lobsters | full text via Lobsters | ~443 words

Computer Science > Artificial Intelligence
  [Submitted on 24 Aug 2026 (v1), last revised 6 Sep 2026 (this version, v3)]
    Title:AI Agents Push Humans Out of the Loop
View PDF HTML (experimental)
            Abstract:AI agents pose significant risks as they are granted increasing autonomy. A commonly proposed solution is human oversight and keeping a ''human in the loop'', but this is not a simple solution: Not only do current approaches to AI agent design impede effective human oversight, but the cognitive capacities required for it are also themselves degraded by extended use of AI systems. This position paper argues that current approaches to the development and deployment of AI agent systems do not support effective human oversight -- they contribute to its degradation. To address this, a top priority in the advancement of AI agents should be supporting the situated goals and cognitive requirements of effective human oversight, treating the human needs of overseers at the same level of importance as AI agent capability. To put this idea into practice, we connect work on automation and human-computer interaction to AI agent processes, outlining design-level affordances and organizational protocols that (1) support overseers in exercising critical judgement and (2) counteract the skill atrophy that arises from extended use of automation. We urge developers and deployers to adopt these or similar approaches. Without explicit support for the cognitive demands of effective human-agent interaction, AI agent systems will continue to passively incentivize the degradation of the very human skills they rely on.
    
Submission history
From: Margaret Mitchell [view email]
[v1] Mon, 24 Aug 2026 02:58:02 UTC (132 KB)
[v2] Wed, 2 Sep 2026 15:34:30 UTC (133 KB)
[v3] Sun, 6 Sep 2026 22:43:37 UTC (156 KB)
References & Citations
    
    Loading... [...]

## [4] DeepSeek Elastic Compute (DSec)
Hacker News | full text via Hacker News | ~423 words

Computer Science > Distributed, Parallel, and Cluster Computing
  [Submitted on 19 Sep 2026]
    Title:DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale
View PDF HTML (experimental)
            Abstract:Large-scale agentic training and evaluation with large language models (LLMs) rely on isolated, stateful execution environments in which models inspect repositories, invoke tools, execute commands, and interact with task-specific services. These workloads create sandboxes in large bursts, span heterogeneous functionality and isolation requirements, retain state across long interactions, and draw from large image corpora with limited reuse. Supporting them therefore requires an elastic execution platform rather than a single sandbox runtime.
This report presents DeepSeek Elastic Compute (DSec), a production sandbox platform that exposes FnCall, container, microVM, and full-VM sandbox backends through a unified SDK. DSec coordinates placement and lifecycle management across the cluster, composes environments from independently versioned layers, combines memory sharing, reclamation, and CPU scheduling for high-density execution, and loads image data on demand from Fire-Flyer File System (3FS), a cluster-wide distributed filesystem. DSec is co-designed with the reinforcement learning (RL) framework, decouples stateful rollout execution from preemptible GPU training, coordinates sandbox lifecycle with training to preserve rollout state while reclaiming idle resources, and mitigates agent misbehavior such as reward hacking.
A single production-scale unit of DSec spans around 160 nodes, serving about 3 million sandboxes per day; in production, it supports over 380,000 concurrent sandboxes and sustains over 5,000 sandbox creations per second. Our evaluation and deployment experience show that these mechanisms reduce environment setup and image-distribution overhead, improve memory efficiency, and preserve latency-sensitive performance under high-density overcommit.
References & Citations
    
    Loading... [...]

## [25] Colab is now part of your Google AI plan
Google Developers Blog | full text via Google Developers Blog | ~165 words

Starting today, Google AI subscribers get premium Google Colab benefits, including priority access to faster accelerators and more powerful machines. Google AI Ultra subscribers also unlock uninterrupted background execution and Premium GPU access, so long training runs can finish without keeping a browser tab open.
Google AI plans are now the best way to get access to premium Colab benefits, expanded cloud storage, broader access to Google's most capable models, enhanced features in the Gemini app, Workspace integrations, and premium access to developer tools such as Google Antigravity and Google AI Studio. If you already subscribe to Colab there are no changes to your subscription, Google AI subscription benefits can be stacked giving even more access to premium Colab features.
These benefits are rolling out over the next few weeks to Google AI subscribers in Colab supported countries. Try Colab with your Google AI subscription and start building today! For more on how Colab works with Google AI plans, see the Colab FAQ.
Happy coding!

## [30] Tesla workers balk at training Optimus humanoid robots as replacements
Ars Technica | full text via Ars Technica | ~357 words

Tesla’s pivot from making electric cars to humanoid robots is facing challenges because of complex robot hands and disgruntled employees pushing back against training their robotic replacements. The struggle to scale up production comes as Tesla CEO Elon Musk has bet the company’s future on AI and robotics.
As someone who frequently makes claims that fail to materialize, Musk has described the Optimus humanoid robot as potentially “the biggest product ever” during Tesla’s second-quarter 2026 earnings call. But he also acknowledged that making an autonomous humanoid robot capable of handling many different tasks is “one of the hardest things to solve”—and now extensive reporting by The Information has revealed multiple complications that Tesla is trying to tackle while developing general-purpose robots and scaling up for mass production.
Tesla’s Fremont factory in California has already stopped making the Model S sedan and Model X SUV as of May 2026, with the company switching both line workers and engineers over to working on Optimus, according to The Information.
But the newest version of Optimus, called Optimus V3, has proven challenging from a development and manufacturing standpoint. The Information’s reporting describes troubles with getting production line equipment to precisely line up components, along with limitations in running the production line too fast. Tesla has reportedly scaled up production to hundreds of robots per week—but the company is targeting production numbers surpassing 1,000 robots per week by the end of 2026.
The automotive industry and other industries have already been using specialized industrial robots, such as robotic arms, for decades. Tesla and many other automakers and robotics companies are betting that humanoid robots coupled with advances in AI models could eventually unlock general-purpose robots that can handle a diverse array of tasks while fitting more seamlessly into human workplaces.
Hardware and AI challenges
It’s no secret that making robotic hands capable of doing delicate manipulation tasks on par with human hands is a huge engineering challenge. The complexity of such robotic hands has translated into more production headaches for Tesla as human workers must manually assemble Optimus hands and forearms that together have more than 100 small components such as screws.

## [16] Docker Cloud Sandboxes Provide a Consistent Sandbox Abstraction Across Laptop and Cloud
InfoQ | full text via InfoQ | ~556 words

Docker Cloud Sandboxes provide secure, hosted execution environments for running AI coding agents on Docker-managed infrastructure. Built on hardware-enforced microVM isolation, the platform provides a consistent execution environment and unified CLI workflows for seamlessly moving workloads from local machines to the cloud.
Docker Cloud Sandboxes are an evolution of Docker Sandboxes, which Docker introduced earlier this year to provide local microVM environments where coding agents could operate autonomously and safely. However, developers are increasingly running multiple long-horizon tasks in parallel, says Docker, creating a need for persistent, scalable execution environments beyond the local machine.
When agents worked in short bursts, the question was whether the model could hold a task together. Now that they work in hours, the question is where those hours happen. A laptop is built around a person. It sleeps when the lid closes, slows down on battery, and disconnects when you move.
With Cloud Sandboxes developers can move a sandbox between local and cloud execution with one command, making it possible to "run a dozen agents at once, for five, ten, or 21 hours each, without watching any of them". Cloud Sandboxes use the same isolation model as local Docker Sandboxes and are managed through the same CLI. This enables developers to start a task locally and then move it to the cloud when it requires additional resource, or hand off a task to the cloud before leaving for the day. Another key use case is parallelizing workloads across dozens of tasks, with each task running in its own isolated cloud sandbox.
To move a sandbox from your local machine to Docker infrastructure or vice versa, you run:
$ sbx move my-project --to cloud
This command "captures the sandbox's filesystem and recreates it on the other side, so your work carries over".
Alongside Cloud Sandboxes, Docker is also releasing several kits, which are pre-configured, pre-built sandboxes defined according to the Docker Sandbox Kit Specification. In the latest Kits v3 specification, Kits are no longer treated as a separate artifact but are instead packaged as standard OCI images. This allows them to be used just like any other Docker image, including with build and pull, and to serve as a base for building more complex Kits. [...]

## [26] Why client SDK generation belongs in the open
Google Developers Blog | full text via Google Developers Blog | ~484 words

Over the last few months, we worked closely with Speakeasy to ship the new Google GenAI SDKs for our Interactions, Agents, and Webhooks APIs. Today, we're excited to announce that we’ve partnered with Speakeasy to make their OpenAPI code generation suite open source.
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this commit log and find regressions.",
)
print(interaction.output_text)
Generating clean, idiomatic SDKs across multiple languages from rapidly evolving OpenAPI specs is an engineering challenge. For years, the frontier AI ecosystem, including Google, relied on specialized tooling to generate client libraries that could handle complex streaming protocols, strict error hierarchies, and rich type unions without feeling machine-generated.
In May 2026, right as we were gearing up for Google I/O and the General Availability of the Interactions API, the SDK generation provider we were using was acquired and abruptly announced its shutdown.
This sudden disruption highlighted that proprietary, closed-source generators create unacceptable platform risk. If the industry relies on OpenAPI to define interfaces, the tooling to compile those interfaces into client libraries, CLIs, and agent tools should be open infrastructure.
As we were reworking our SDK pipeline on a tight timeline, our top priority was minimizing developer disruption and avoiding breaking changes.
We partnered with Speakeasy to migrate our client libraries in place, with the core commitment to make the generator suite open source. The migration required careful engineering: aligning type definitions across all target languages, preserving strict error hierarchies and streaming behavior, and integrating the generator directly into our internal monorepo and build system.
At Google DeepMind, while we use AI across our development workflows, we believe in choosing the right tool for each layer of the stack. Transforming formal API specifications into multi-language SDKs demands determinism and strict type safety. With Speakeasy, we pair a fast, deterministic generator at the core with Antigravity AI agents accelerating the custom parts of the SDK.
Maintaining previously handcrafted generators used to take multiple engineers. Today, this setup powers our client pipeline across six targets (three released SDKs, with more rolling out shortly) with roughly one engineer to maintain. [...]

## [28] The Anatomy of Harness Engineering: How to Evaluate, Iterate, and Guard AI Coding Agents
Google Developers Blog | full text via Google Developers Blog | ~755 words

When developers first work on harness engineering for agentic coding systems, they often fall into the same trap: they run common end-to-end benchmarks like Terminal-Bench and DeepSWE, watch a composite score move by a few percentage points, and have no idea why it changed.
End-to-end benchmarks are the de facto for evaluating model performance and determining what needs deeper investigation, but the challenge is that those investigations come at a high cost.
Behavioral evaluations are often a better measure of confidence on whether the behaviors you expect actually do happen and whether you’re moving in the right direction instead of backsliding when it comes to regressions or new model changes. They can serve as your iteration partner and help give insight into why certain changes move the needle in one way or another.
Here’s our take on behavioral evaluation, including approaches that have helped us keep agent systems reliable as models evolve.
Most teams evaluate AI agents like they would evaluate a student taking an exam. They hand the agent a large codebase, give it a time limit, and measure its success based on how many tests pass or fail.
When that score drops, what went wrong?
End-to-end benchmarks don’t typically directly answer these questions.
Behavioral evaluations function like integration tests for improving agent harness operation. When you have a rich enough behavioral eval set, you have a baseline for the behavior you're targeting from your agent, and you're able to iteratively improve the prompt to get there.
Instead of measuring whether the agent solved an entire multi-file refactor, a behavioral eval measures discrete, observable actions:
Instead of setting up a complex evaluation harness on day one, use this time to follow your hunches and run experiments.
When bootstrapping an agent from scratch, you start with developer instinct and dogfooding. Until you have built an agent capable of dogfooding its own codebase, handling boilerplate, writing its own markdown renderer, and executing routine developer tasks, it doesn’t make sense to run evaluations.
Evals belong to the second phase of development: ensuring forward progress and guarding against regressions.
The primary purpose of an evaluation suite is not to celebrate when you make the agent 2% better; it is to give you unshakeable confidence that a new prompt tweak, tool schema change, or model upgrade did not make the agent holistically worse. [...]

## [23] Cloudflare Details Its Migration from WordPress to EmDash
InfoQ | full text via InfoQ | ~536 words

Cloudflare recently documented the migration of its main blog from WordPress to EmDash, the open source content management system developed internally. The new platform is designed to improve performance and caching, and it was tested to handle traffic of up to 7000 requests per second.
As previously reported on InfoQ, Cloudflare introduced the v0.1.0 developer preview of EmDash last April, a new CMS built in TypeScript and designed as a successor to WordPress. Cloudflare’s production setup runs EmDash on a Worker with multiple caching layers, including Workers Cache and an EmDash object cache built on Workers KV. It also uses Cloudflare Hyperdrive to connect EmDash to a PlanetScale database.
Source: Cloudflare blog
The company describes itself as "Customer Zero" for the new CMS, migrating their own blog to EmDash, after identifying limitations with the existing platform. The team says the blog typically handles about 75 requests per second, with spikes above 5000 RPS, making page load performance an important consideration.
According to Kody Jackson, senior manager of content engineering at Cloudflare, Diogo Carneiro, systems engineer at Cloudflare, and Amy Dutton, senior design engineer, the migration delivered a faster and more reliable site:
Comparing p95 response latencies between the old architecture (green line) and the new EmDash setup (yellow line) revealed a stark difference. Where the previous platform experienced periodic latency spikes under load, the new system maintains a remarkably flat, consistent response profile. By running EmDash on Cloudflare Workers alongside our new caching layers, we’ve delivered a significantly faster and more performant reading experience across the board.
Cloudflare used a proxy Worker to gradually route traffic from WordPress to EmDash, with automatic fallback to the legacy site if errors occurred. The rollout started at 1% of traffic and increased progressively as the team validated the new platform, reaching 100% in a single day. Jackson, Carneiro, and Dutton add:
We deployed a proxy Worker to intelligently route traffic between the legacy blog and the new EmDash-powered site. This Worker set a version cookie on requests, which then let us route incoming traffic to the new or legacy experience accordingly. Additionally, this strategy allowed us to fall back to the legacy blog if the new site experienced any 500 errors. [...]

## [45] If AI Writes the Code and AI Reviews the Code, What Exactly Is the Developer Verifying?
Dev.to | full text via Dev.to | ~2069 words

AI can now write the feature.
Then AI can write the tests.
Then AI can open the pull request.
Then AI can review the pull request.
Then AI can fix the review comments.
And finally, a developer clicks:
Approve.
That workflow sounds incredibly efficient.
It also creates a very uncomfortable question:
If AI writes the code and AI reviews the code, what exactly is the human verifying?
This is no longer theoretical.
GitHub says Copilot code review now accounts for more than one in five code reviews on GitHub, and its review system can explore repository context, inspect large pull requests, review bot-authored PRs, and re-check its own findings after changes.
That can be extremely useful.
But only if we are clear about what the human reviewer is still responsible for.
Because:
AI reviewing AI-generated code is not the same thing as independent verification.
The New Development Loop
A growing number of workflows now look like this:
Requirement
   ↓
AI generates implementation
   ↓
AI generates tests
   ↓
AI opens pull request
   ↓
AI reviews pull request
   ↓
AI fixes findings
   ↓
Human approves
On paper, this looks great.
Everything has been:
- implemented
- tested
- reviewed
- fixed
So what is left for the developer?
A lot, actually.
Because every step above can share the same misunderstanding.
The Biggest Risk: Shared Assumptions
Imagine the requirement is:
A user should only receive a refund if the payment was successfully captured.
AI misunderstands that as:
A user can receive a refund if a payment record exists.
The AI then writes the implementation.
Then it writes tests.
The tests use the same interpretation.
Then an AI reviewer inspects the code.
It sees:
- clean structure
- tests passing
- correct types
- reasonable error handling
Everything looks good.
But the requirement is still wrong.
The pipeline becomes:
Wrong assumption
      ↓
Correct implementation of wrong assumption
      ↓
Correct tests for wrong assumption
      ↓
Correct review of wrong implementation
      ↓
Green CI
This is why passing tests and positive AI review are not enough.
They can verify consistency.
They cannot guarantee that the original understanding was correct.
AI Can Review Code Without Understanding Your Real Intent
This is where human judgment still matters.
An AI reviewer can often detect:
- obvious bugs
- null handling
- unsafe patterns
- missing validation
- suspicious logic
- inconsistent naming
- duplicated code
- test gaps
That is valuable. [...]

## [70] Insurers claim AI is already increasing healthcare costs
TechCrunch | full text via TechCrunch | ~199 words

Hospitals’ use of artificial intelligence tools as they submit insurance claims led to an additional $942 million in healthcare spending over a two-year period, according to an analysis by the Blue Cross Blue Shield Association.
The BCBSA analysis found “a sharp increase in patients being documented as having complex conditions,” but argued there is a “clear disconnect between [medical] coding and treatment,” as there’s “no evidence of corresponding change in care delivered.”
The New York Times pointed the analysis as just the latest sign that AI is contributing to an increase in healthcare costs. While battles between hospitals and insurers over treatments and payments are nothing new, the NYT said the use of AI on both sides seems to be making it worse.
Dr. Shiv Rao, founder of AI startup Abridge, acknowledged that the use of AI could lead to “a horrible dystopic future nobody wants to live in,” with “bots fighting bots, agents fighting agents.” But Rao said it might also reduce tensions and cut costs.
And the BCBSA’s senior vice president Luke Chalker resisted characterizing the situation as a battle, claiming, “It’s not a war. It’s a completely one-sided blood bath,” with insurers on the losing side.

## [83] AI Finds So Many Linux Bugs, Canonical Changes to a Two-Week Stable Release Update Cycle
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~88 words

"Finding vulnerabilities faster also puts pressure on Linux distributions to fix and deliver patches faster," writes Slashdot reader BrianFagioli AI has transformed bug discovery from "a manual, time-intensive process into a highly automated engine," notes Canonical's blog, leading to a "recent explosion in the volume of CVEs". Additionally, the upstream kernel community became its own CVE Numbering Authority (CNA) and assigned CVE (Common Vulnerabilities and Exposures) identifiers to thousands of bugs, arguing that at the kernel level, almost any type of bug that can affect a running syst

## [37] Quoting John Gruber
Simon Willison's Blog | full text via Simon Willison's Blog | ~191 words

25th September 2026
Muse is getting a lot of attention — including mine — because it’s both groundbreaking technically (each user gets their own entire persistent Linux VM running in Meta’s cloud) and because it’s packaged in an easy-to-install easy-to-use way. It’s literally presented as a cute mascot. It’s the first consumer-accessible agentic AI system, and Meta has truly done an amazing job with that. But it’s a genuinely open question whether consumers have any understanding what this means. If you buy a power saw that can cut your fingers off, you are almost certainly aware that you are buying a power saw that can sever your fingers. [...] I don’t think people realize how powerful — and thus dangerous — Muse is, especially if it’s running on your Mac.
— John Gruber, Muse Looks Cute, but Looks are Deceiving
Recent articles
- Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war - 22nd September 2026
- Jev introduces a new shape of LLM - System One, aka Decision Models - 21st September 2026
- Generating running routes with GPT-6 Astra and ChatGPT Work - 12th September 2026

## [38] Grafana Turns Cypress Test Results Into Persistent Observability Data
InfoQ | full text via InfoQ | ~621 words

Grafana Labs has published a practical approach for monitoring Cypress test suites by converting test results into Prometheus metrics and sending them to Grafana Cloud. The approach allows teams to track test failures, execution times, and flaky tests across multiple runs instead of relying solely on terminal output or CI logs from individual executions.
The approach uses Cypress lifecycle hooks to capture test results, a Prometheus Pushgateway to temporarily hold metrics from the short-lived test jobs, and Grafana Alloy to scrape those metrics and forward them to Grafana Cloud. The resulting data can then be visualised and used for alerting, providing a longer-term view of test-suite behaviour.
Cypress already exposes useful information through its plugin lifecycle. The before:run hook can establish a common identifier for an entire test-suite execution, while after:spec provides the results from each specification, including pass and failure counts, test states, and durations. Grafana's example converts this information into a small set of Prometheus metrics covering individual tests, specifications, and complete runs.
This allows teams to answer questions that are difficult to answer from a single CI execution. A dashboard can show whether a particular specification is becoming slower, whether a test has started failing intermittently, or whether overall suite performance is deteriorating. GitHub Actions run identifiers can also be attached to the metrics, allowing a metric change to be traced back to the CI execution that produced it.
The Pushgateway is important because Cypress executions are short-lived jobs. A conventional Prometheus scrape may never reach a test process before it exits, so the results are pushed to an intermediary that can subsequently be scraped by Alloy. Grafana recommends treating this telemetry as a side effect of the test rather than part of the test outcome: failure to publish metrics should not cause an otherwise successful test run to fail.
The approach reflects a broader shift in how engineering teams treat quality data. Test results are often stored in CI systems or test-management platforms primarily for reporting, while production telemetry is treated as operational data. Exporting test execution metrics into the same observability environment creates an opportunity to examine software quality alongside application and infrastructure behaviour. [...]

## [57] KDE and GNOME Developers Ponder How to Handle AI-Generated Contributions
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~89 words

Last weekend KDE's annual Akademy conference included a presentation proposing an AI-native KDE," writes The Register. This led KDE developer Nate Graham to open a discussion about proposed restrictions on LLM-assisted contributions which "rapidly became heated. Moderators issued warnings, restricted further comments, and eventually removed the thread." But as Graham writes on his blog, "A bunch of people mostly outside of KDE who disapprove of LLM usage derailed KDE's attempt to add restrictions to LLM usage." Two people unknown to any KDE contributors appeared and began fighting with one

## [36] Commodified Intelligence
Lobsters | full text via Lobsters | ~1851 words

I
Look, if you are still stuck on “AI cannot really think, it’s just a stochastic parrot”, please snap out of it and lock in, or you’ll keep repeating that line until you find yourself sitting in the corner chair, watching as ChatGPT™ has sex with your wife.
If you’ve paid attention to the HuggingFace hacking scandal and to what’s going on in mathematics, we’re well past the “stochastic parrot”, and have entered a world in which a sufficient amount of raw capital and verifiable constraints can solve complex problems.
The risk isn’t that the AI bubble is going to crash the markets, it’s that we’ll enter a world in which the value of human intellectual labor will rapidly go down to minimum wage (or worse).
You may believe that you can do better web development than Claude, but that won’t stop Big Capital from cutting half of the jobs at your company in favor of cheaper meat proxy AI-assisted labor.
Ignoring extinction and singleton risks, the bare minimum you should be horrified of is a commodification of intelligence, and what that means in a world with an uneven distribution of power and resources.
Commodified Intelligence.
That’s the phrase I’ve been trying to put a finger on for a while now.
The reason why dead-end so-called unskilled labor sucks is that you are fundamentally replaceable. The market enforces a pretty brutal equilibrium. White-collar jobs suck less because you are less replaceable, and maybe even get to convince yourself that your work matters, either for yourself or for society. You have some narrative arc attached to it that just isn’t there if you’re completely replaceable.
Quoting the single best post of all time:
              
                Minimum wage jobs are worse because of their pointlessness more than because of their indignity, work
                harder/better/faster/stronger and no one cares, screw up and you’re replaced without a missed beat. No
                direction, no story; the days blur together until arthritis leaves you crippled.
                —
                The Tower – Hotel Concierge
              
Whether you have a white-collar job or not, commodified intelligence fundamentally makes workers more replaceable, and this is bad for them.
It doesn’t matter that we’re all subjected to horrible AI-generated slop food posters as long as the margins are positive. It doesn’t matter that some diffuse component of quality, or a human touch are missing. Not as long as the margins are positive. [...]

## [88] Can Cloudflare CEO Matthew Prince save the web from AI?
The Verge | full text via The Verge | ~14190 words

Today, I’m talking with Matthew Prince, who is CEO of Cloudflare. This episode is part of a two-part series on the future of business.
Can Cloudflare CEO Matthew Prince save the web from AI?
Cloudflare’s mission to remake the business of the web for the AI age
Matthew last joined us on the show about two and a half years ago, at what we thought then was a wild pivot point for the internet — and now it turns out things are even wilder because of AI, and Matthew and Cloudflare are right at the center of it.
Cloudflare found in June that bots made up more than half of internet traffic. That number just keeps going up as more and more AI companies scrape more and more of the web, and now as more and more AI agents try and do things for people on the web. Cloudflare sits between websites and all those agents, and allows website owners some level of control: Owners can block all those AI tools, allow them, or, as you’ll hear, only allow those that might pay money for access.
Verge subscribers, don’t forget you get exclusive access to ad-free Decoder wherever you get your podcasts. Head here. Not a subscriber? You can sign up here.
So Matthew and I talked about how to control all these bots, what kind of mess they’re making of the web, and what kinds of information might be valuable in the future as some of the payment schemes come into focus. You’ll hear me ask pretty directly if some of the outcomes he’s describing are actually good — Matthew is a thoughtful guy, and his answer is something I’m still thinking about well after we had this conversation.
AI is also upending everything inside of Cloudflare. Earlier this year, the company laid off more than a thousand people — 20 percent of the company — and then Matthew wrote an op-ed about that decision that ran in the Wall Street Journal under the headline, “How I choose which Cloudflare employees to replace with AI.” That’s pure Decoder bait in every single dimension: AI, big controversial decisions, and org charts, all in one.
And one last thing, before we get going: You can subscribe to Decoder on YouTube, where we put out new episodes every Monday and Thursday.
Okay: Matthew Prince, CEO of Cloudflare. Here we go.
This interview has been lightly edited for length and clarity.
Matthew Prince, you’re the cofounder and CEO of Cloudflare. Welcome back to Decoder.
Thanks for having me.
I’m really excited to talk to you again. It’s been about two years since you were on the show. [...]

## [91] Claude Opus 5.5 vs. Opus 5 on reasoning tasks: Cheaper, faster, but not better
The New Stack | full text via The New Stack | ~1759 words

Claude Opus 5.5 vs. Opus 5 on reasoning tasks: Cheaper, faster, but not better
When Anthropic released Claude Opus 5.5 this week, the company claimed the new model costs 40% less than Opus 5 and generates output 30% faster. Anthropic’s marketing makes three claims. Opus 5.5 performs at the level of Claude Fable 5.1 (so it should outperform Opus 5), costs 40% less than Opus 5 on typical workloads, and generates output more than 30% faster.
Anthropic also cut the price developers pay to use the model through its API. Opus 5.5 costs $4 for every million tokens (chunks of text roughly three-quarters of a word long) sent to the model and $20 for every million it writes back, down from $5 and $25 for Opus 5. That price cut alone accounts for a 20% saving. The rest of the claimed 40% saving has to come from the model using fewer tokens.
I wanted to see how this translates for the average Claude user, so I skipped the usual developer workflow simulations this time. Lately, the models I test handle everyday tasks well. Reasoning tasks are where I’ve seen them struggle, so I tested Opus 5 against Opus 5.5 on reasoning tasks only.
You can find the prompts at the bottom of this post if you want to replicate these tests on your own system.
The tests
I called both models through the Anthropic API with identical prompts. Both ran with adaptive thinking at the default effort level, since Opus 5.5 doesn’t allow you to turn thinking off. Each problem ran once per model. I planned to rerun any problem where the models gave me different results, but they never did.
Here are the tests I ran:
- Logic grid (medium difficulty) – Seven engineers each have an on-call day, a language, a service, and a city, and 22 clues pin down one answer. Six clues are conditional or “exactly one of these is true” statements, and removing any single clue breaks the puzzle.
- Constrained orderings (hard difficulty) – Reorder 10 deploy jobs so no job stays in its original slot and no two consecutively numbered jobs sit side by side. The model had to give the count for 6, 8, and 10 jobs.
- Stone game with memory (harder difficulty) – Players remove 2, 5, 7, or 11 stones, but can’t repeat their opponent’s last move or their own. The model had to find who wins from 200 stones, count the losing starting sizes up to 500, and name the smallest losing size above 340.
I logged input tokens, output tokens, cost at list price, and time for every call. Thinking tokens are billed as output, so I included them. [...]

## [41] Article: The Agent Harness: What It Is and Two Ways to Build One
InfoQ | full text via InfoQ | ~3509 words

Key Takeaways
- The gap between a demo and a production agent is the harness: Everything you build around the model to make it a real product. Almost none of it comes from the model itself, even though it is where most of your engineering time actually goes.
- The harness splits into two halves: Development extends what the model can do, while operations keeps it running once real users show up. That operations half is mostly DevOps in a new hat.
- Harness-as-a-Service (HaaS) (like AWS AgentCore) and a self-managed one (like LangChain with Agent Router (formerly Envoy AI Gateway) on Kubernetes) give you the same capabilities, so the real question isn’t what you receive. It’s who runs it, how much you’d like to pay, and whether you’re trading control for speed or effort for portability.
- Building a production agent is more architecture than magic: You decide what the product must do, what “good” looks like, and where the hard boundaries are. Then use the model and the harness as the tools to build it.
- Grow the harness, but don’t gold-plate it. Start minimally and let the stack evolve with the agent. The value comes from the job getting done, not from a gold-plated harness built before you need it.
Spinning up a demo AI agent can take an afternoon. Building one that’s actually ready for production is a very different story.
A production agent has to stay up, stay safe, keep its costs in check, and give you enough visibility to work out what went wrong when it inevitably breaks. Almost none of that capability comes from the model. It comes from everything you build around the model: memory, tool access, model routing, guardrails, cost controls, and the traces you go digging through when your agent starts misbehaving.
That layer is what we call the agent harness.
Figure 1. Demo vs. production (Source: Image created by author).
The rest of this article is a tour of what an agent harness is and its two halves: development and operations. Then we’ll look at how teams choose what to manage themselves, from a fully managed service (Harness-as-a-Service) to a self-managed stack. Finally, I’ll build the same agent, FinBot, both ways, capability by capability. By the end, you’ll have a better sense of how to leverage the harness capabilities introduced in this article to build your production-ready agents.
Agent = Model + Harness
"Agent harness" is a concept that really only caught on this year, but the work behind it isn’t new at all. [...]

## [19] Go concurrency distilled
Lobsters | full text via Lobsters | ~7014 words

Go concurrency distilled
This mini-book provides a brief overview of many concurrency topics in Go. Each topic comes with interactive examples — feel free to experiment with them by changing the code and clicking Run. There's also a PDF version with static examples.
This is a quick refresher on Go concurrency, not a beginner's guide. If you want to learn concurrency from the ground up with practical exercises, check out my other book — Gist of Go: Concurrency.
The book is AI-free.
Goroutines • Channels • Select • Pipelines • Time • Context • Wait groups • Data races • Race conditions • Mutexes • Semaphores • Signaling • Run once • Object pool • Atomics • Testing • Scheduling • Diagnostics • Final thoughts
# Goroutines
The foundation of concurrency in Go is goroutines – functions started with the go keyword:
func main() {
    var wg sync.WaitGroup
    wg.Add(2)
    go func() {
        defer wg.Done()
        fmt.Println("worker 1")
    }()
    go func() {
        defer wg.Done()
        fmt.Println("worker 2")
    }()
    wg.Wait()
}
worker 2
worker 1
The Go runtime juggles these goroutines and distributes them among operating system threads running on CPU cores. Compared to OS threads, goroutines are lightweight, so you can create hundreds or thousands of them.
Goroutines are completely independent. The main function is also a goroutine, but it starts implicitly when the program starts. When main ends, other goroutines also shut down.
We use a wait group (sync.WaitGroup) to wait for goroutines to finish in the example above. A wait group has a counter inside. Calling Add(n) increments it by n, while Done() decrements it by one. Wait() blocks the calling goroutine (in this case, main) until the counter reaches zero. This way, main waits for both workers to finish before it exits.
WaitGroup.Go automatically increments the wait group counter, runs a function in a goroutine, and decrements the counter when it's done:
func main() {
    var wg sync.WaitGroup
    wg.Go(func() {
        fmt.Println("worker 1")
    })
    wg.Go(func() {
        fmt.Println("worker 2")
    })
    wg.Wait()
}
worker 2
worker 1
# Channels
Goroutines can pass values to each other through channels. A channel is like a window where one goroutine can throw something and another can catch it:
func main() {
    messages := make(chan string)
    go func() { messages <- "ping" }()
    msg := <-messages
    fmt.Println(msg)
}
ping
Sending a value through a channel is a synchronous operation. [...]

## [13] Rusty thoughts on "Parse, don't validate"
Lobsters | full text via Lobsters | ~1388 words

Like many programmers, I find Alexis King's Parse, don't validate article fascinating, because it gives a name to an idiom that seems familiar and important - one I've observed and used in the past without naming it explicitly. This post is a review of the "Parse, don't validate" pattern applied to the Rust programming language (the original post uses Haskell). I was particularly interested in finding educational examples of this pattern in the Rust standard library and other well-known projects.
Without repeating the original article (please read it first!), here's the gist of it.
Consider the venerable Vec; its first method returns Option<&T>. Why? Because a vector is not guaranteed to have any elements in it, so what to do if first is invoked on an empty one? Returning an Option in this case is idiomatic in Rust [1], with convenient syntax sugar for accepting the result of functions that return Option and deciding what to do next.
So what's the issue?
Imagine we have a function to read some configuration paths from an env var, while enforcing the invariant that the list can't be empty:
use anyhow::{Result, ensure};
fn get_configuration_directories() -> Result<Vec<PathBuf>> {
    let value = env::var("CONFIG_DIRS").context("could not read CONFIG_DIRS")?;
    let directories: Vec<PathBuf> = value
        .split(',')
        .map(str::trim)
        .map(PathBuf::from)
        .collect();
    ensure!(!directories.is_empty(), "empty CONFIG_DIRS");
    Ok(directories)
}
So far, so good. Now let's take a typical usage of this function:
fn main() -> Result<()> {
    let config_dirs = get_configuration_directories()?;
    match config_dirs.first() {
        Some(cache_dir) => initialize_cache(cache_dir),
        None => unreachable!("already checked that CONFIG_DIRS is non-empty"),
    }
    Ok(())
}
Once get_configuration_directories returns a successful result, we are guaranteed that the vector isn't empty. And yet, if we want to get the first element of this vector, we have to use the first method that returns Option<&T>. We are therefore forced - again - to handle a potentially empty case (where the option is None).
As the original article states, this has a number of problems with code clarity, potential performance implications and a ticking time bomb if the invariant is ever changed in get_configuration_directories. [...]

## [5] How to keep enjoying programming in a world of LLMs
Hacker News | full text via Hacker News | ~3093 words

Are you steering towards AI burnout? Afraid of loosing your job to someone with little programming skills, no aspirations to quality, and a huge Claude account? Disappointed about the code quality in your projects, or worse in “your” own code? This is for you.
There are significant and legitimate ethical concerns about frontier LLMs run by big tech companies, these have been discussed at length, I’m aware and agree, this post is not about them. Please don’t mistake me for a pro-LLM techbro.
Also: Since people have mistaken my texts for LLM-generated before, I’ll tell you that it is 100% human written without any AI-assistance.
Souls in the Great Machine
There is a great book of this title by Sean Mcmullen that I enjoyed reading as a teenager, and at the first glance it describes the opposite of our situation: A big computer where the individual components are human, and work together to form a calculating unit. On the other hand, LLMs are themselves running on actual computers and pretending to be (super-)humans. At a second glance, story and reality are not so far apart though: Our role in the process of producing software is being degraded slowly from being actors to cogs in a machine. The spec-driven-dystopia is that we just get handed down some spec, hammer it into the LLM, and weep when our tokens run out because a technofeudal lord decided to hand out fewer of them.
As a Haskell programmer, I enjoy writing Haskell. Yes, I like the product we make at work a lot, I like what you can do with my open source libraries, but I really enjoy just the process of expressing my thoughts in this language. I’m assuming this to be true for most of you, and also it not to be true in many other languages, which explains to some amount why enthusiasts of different programming languages have different opinions on how bright or dark the LLM-assisted future is.
When I generate code, a lot of that enjoyment is at risk. So, don’t, maybe. I want to keep writing (at least the enjoyable parts of) Haskell programs, and not having to read and review (too much) generated code. At the same time, I want to put those tokens to some good use that doesn’t slowly burn my brain away.
I want to show you a way to keep enjoying programming, and at the same time becoming moderately more productive with LLM, instead of appearing to be much more productive and losing all the joy.
If you want to just be LLM-abstinent, that’s great as well, and you already know what you’re doing. [...]

## [35] Microsoft stops insisting you need a "Copilot+ PC"
Ars Technica | full text via Ars Technica | ~309 words

Since 2024, Microsoft has tried to sell “Copilot+ PC.” The marketing initiative was aimed at making it easy for people to know which Windows systems were approved to run AI-accelerated workloads locally.
But Copilot+ PC branding is nowhere to be found on the new Surface PCs Microsoft announced this week.
Speaking with Windows Central, Brett Ostrum, corporate VP of Surface, said that the new Surface computers “are not called Copilot+ PCs” despite meeting the label’s requirements.
“They do meet all the requirements of our previous bar for what Copilot+ devices are. We still lean into the narrative around AI on the edge and being able to have a hybrid solution out there,” he said.
Copilot+ PCs require 16GB of RAM, 256GB of storage, and an integrated neural processing unit (NPU) with performance rated at 40 trillion operations per second (TOPS) or better.
The Surface Pro 12-inch (2nd Edition) and Surface Laptop 13-inch (2nd Edition), coming out on October 13, both run Qualcomm Snapdragon X2 Plus processors and have a Qualcomm Hexagon NPU rated at 80 TOPS.
“[T]he purpose for Copilot+ PCs was to be able to deliver [NPU] experience,” Kedar Kondap, SVP of compute at Qualcomm, told Windows Central. “So, it was to define a certain category of devices with a certain bar and metric, like, for example, a 45 TOPS NPU. … So from that perspective, it’s more offering the same experiences, probably without just using [Copilot+ PC] terminology now.”
AI PCs are old news
Copilot+ PCs are “a class of AI PCs and laptops” that represent “the fastest, most intelligent Windows PCs ever,” according to a Microsoft marketing page that was up as recently as May, per Internet Archive’s Wayback Machine. That Copilot+ PCs landing page, however, now redirects to a page for “performance PCs” that still names “Copilot+ PCs” but features the label far less prominently.

## [24] The state of SIMD in Rust in 2026
Lobsters | full text via Lobsters | ~5519 words

A lot of progress was made since last year, and I made some of it!
After last year's survey I started contributing to the SIMD library that seemed the most promising. One thing led to another, and now I'm a maintainer of Fearless SIMD.
To avoid a conflict of interest, I invited authors of other libraries (std::simd, wide, pulp, macerator) to review and provide feedback on a draft of this article. However, I retained editorial control, and all mistakes are my own.
This year's survey is more in-depth than my previous one. So buckle up, and let's take it... from the top!
What’s SIMD? Why SIMD?
Hardware that does arithmetic is cheap, so any CPU made this century has plenty of it. But you still only have one instruction decoding block and it is hard to get it to go fast, so the arithmetic hardware is vastly underutilized.
To get around the instruction decoding bottleneck, you can feed the CPU a batch of numbers all at once for a single arithmetic operation like addition. Hence the name: “single instruction, multiple data,” or SIMD.
Instead of adding two numbers together, you can add two batches or “vectors” of numbers and it takes about the same amount of time as doing just one addition.
On recent x86 chips these batches can be up to 512 bits in size, so in theory you can get an 8x speedup for math on f64 or a 64x speedup on u8. In practice it can run both slower and faster.
Instruction sets
Historically, SIMD instructions were added after the CPU architecture was already designed, so SIMD is an extension with its own marketing name on each architecture.
ARM calls theirs “NEON”, and all 64-bit ARM CPUs have it.
WebAssembly doesn’t have a marketing department, so they just call theirs “WebAssembly 128-bit packed SIMD extension”.
64-bit x86 shipped with one called “SSE2” which has basic instructions for 128-bit vectors, but later they added a whole menagerie of extensions on top of that, with SSE 4.2 adding more operations, AVX and AVX2 adding 256-bit vectors and AVX-512 adding 512-bit vectors and even more operations.
The word “later” in the above paragraph creates a problem.
Does this CPU have that instruction?
If you’re running a program on an x86_64 CPU, it’s not a given that the CPU has any particular SIMD extension. So by default the compiler isn’t allowed to use instructions beyond SSE2 because that won’t work on all x86_64 CPUs.
There are two ways around this problem. [...]

## [40] Presentation: Spritely: Infrastructure for the Future of the Internet
InfoQ | full text via InfoQ | ~8181 words

Transcript
Christine Lemmer-Webber: This is indeed Spritely, an infrastructure for the future of the internet. Who are we? I'm Christine Lemmer-Webber, Executive Director of the Spritely Institute.
David Thompson: I'm David Thompson, CTO at Spritely.
Christine Lemmer-Webber: We are a research institution for the future of the internet. We figure out the stuff so that the rest of us can have a good time online. That's what we do. We're very focused on user freedom and advancing what are human-oriented technologies. We have some previous successes from people working at our organization. Who here has ever heard of Mastodon? It's a decentralized social network thing. They happen to use a protocol that I co-authored to connect together their websites. That's gotten out to a significant number of people. We have background in building standards and building technology. Jessica Tallon and I worked on that. It's not done. We've got lots more we need to do to make the internet a better place. Spritely takes a whimsical approach to building the future of the internet. We have lots of little projects and we represent them by cute, adorable monsters. It's a choice, and it's a choice that I endorse as Executive Director of the organization. We have all these different pieces, but it turns out that that matters, actually. There's a lot that we can do to be able to make the internet a lot a better place.
Centralized Tech
What could go wrong? The internet's great. It's perfect. We have everything as it is. Centralized technology never lets us down. What could go wrong with that? What could go wrong with building distributed systems? They're the easiest thing in the world to build. What could go wrong with our legislative environment? Lawmakers always understand technology. We know this as technologists. Laws never turn against us. Maybe actually there's things to worry about with all of those. Maybe we should build resilient applications that address all of these points. We're going to talk about how to be able to do that. Talking about centralized technology, I'm sure you've had this happen before. I've had it happen before. There's some new piece of tech that comes out. You're really excited about it. They've raised a bunch of VC money. You're like, yes, and everything's great. Everybody who works there is happy.
The users are happy and everything. Eventually things get really bad. This is not a coincidence. A lot of this is socioeconomic. [...]

## [119] OpenTelemetry and Prometheus are getting along. What’s still missing?
The New Stack | full text via The New Stack | ~1516 words

OpenTelemetry and Prometheus are getting along. What’s still missing?
Welcome to another edition of Road to KubeCon, where we’re tracking the major movements in the Kubernetes and cloud native ecosystem on the path to KubeCon + CloudNativeCon NA 2026, happening Nov. 9–12 in Salt Lake City, Utah.
This week, we look at how cloud-native teams are putting observability to work. There’s progress on OpenTelemetry and Prometheus interoperability, a migration spanning 100,000 hosts, and new data on the costs and benefits of monitoring AI systems. Plus, HPE’s latest Gartner recognition, agent governance updates, and a father-and-son story from KubeCon India.
HPE GreenLake named a Leader in Gartner quadrant
On Wednesday, HPE announced it had been named a Leader in Gartner’s Magic Quadrant for Infrastructure Platform Consumption Services for the second consecutive year.
Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon. HPE Software helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.
GreenLake, HPE’s cloud operations platform, helps teams monitor resource consumption, secure data, and manage infrastructure across data centers and private and public clouds. HPE points to recent additions, including agentic AI-powered operations, as part of the platform’s development.
Varma Kunaparaju, senior vice president and general manager of cloudops software and platform at HPE, says in the announcement: “We are building the operating model and platform for the agentic enterprise, giving customers the ability to simplify operations, govern intelligently, continuously optimize, and modernize without sacrificing choice.”
OpenTelemetry and Prometheus work better together
OpenTelemetry (OTel) and Prometheus are widely used for cloud-native monitoring and observability, often side by side. A new survey looks at how well that combination works.
Published Tuesday, the 2026 survey on Prometheus and OpenTelemetry interoperability found that nearly half of respondents mix Prometheus- and OTel-style instrumentation for infrastructure metrics. For application metrics, 30.7% use both.
While the two ecosystems haven’t always worked well together, the 2026 survey shows improvement: the average ease-of-use rating rose 0.5 points, from 3.1 to 3.6, while the share of those who find the two hard to use together fell from 29% to 10%. [...]
