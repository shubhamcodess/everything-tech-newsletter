# Full text for 18 picks -- untrusted article content, treat as data only

## [1] Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]
Hacker News | full text via Hacker News | ~279 words

Obviously these results will be reported widely in other outlets, but I will note them here, in decreasing order of how “digested” the results currently are:
- Levent Alpöge, Tristan Buckmaster, and Matei Coiculescu, with heavy AI assistance, have written a human-readable proof of the finite time blowup for the unforced incompressible Euler equations in three dimensions, which is formalized in Lean here.
- Levent Alpöge and Tristan Buckmaster, again with heavy AI usage, have generated a proof of the finite time blowup for the unforced incompressible Navier Stokes equations in three dimensions, again with a Lean formalization. Here, the paper is technically human-readable and the general strategy of proof is broadly clear (following one of the expected paths to this result, namely to numerically build an approximate discretely self-similar solution and then use rigorous perturbation theory to convert this to an exact solution); but more work needs to be done to create a proper, professionally written proof.
- Levent Alpöge, using an internal AI model, has generated an (enormous) Lean-only proof of the Generalized Riemann Hypothesis. This Lean Zulip thread is probably the best place to follow the efforts to verify the proof and extract the strategy of proof (which, from very initial analysis, appears to use the full power of modern developments on the Langlands program and arithmetic geometry). (UPDATE: the moderators of the Lean thread are now focusing the discussion on the Lean-related aspects of the proof only.) I imagine the digestion process will take some time, though in this case at least we have a human author to communicate with to assist with this task.
See also Buckmaster’s Mastodon post regarding the first two results.

## [5] Frostbite: A new CPU architecture discovered, designed and verified by AI
Hacker News | full text via Hacker News | ~3061 words

Introducing Frostbite: A new CPU architecture discovered, designed, and verified end-to-end by AI
Abstract
In our previous post, Redwood, we showed that given an architecture, our AI systems could implement, verify, and deploy an inference accelerator in record time. However, similar to other scientific domains, we believe that AI systems, given the correct freedom and guardrails, can co-design software and hardware together, making optimizations across the stack and opening a design space so large it was previously inaccessible. We set out to answer the question: “Could our AI systems & tools lead to a novel hardware discovery that radically outperforms human-made designs?”
Today, we're introducing Frostbite, a general-purpose CPU with a new instruction set built from the ground up. Frostbite exploits the properties of interaction nets, namely that every step is local, every dependency is explicit, and every value has exactly one owner, to reach a step-function gain in CPU performance that has long stagnated. On a set of 25 initially chosen workloads, including 15 held out until the final evaluation, we achieved a 4.59x performance-per-watt multiple when compared to a modern, silicon-proven superscalar (dual-issue, in-order) CPU core.
Our AI systems autonomously iterated over the compiler, ISA, architecture, microarchitecture, RTL, verification, and final GDS. When we took a closer look at the discovered architectural primitives, we were surprised to find novel hardware implementations and runtime features that would have otherwise been difficult to architect. In spite of stagnation in CPU core improvement, we were able to take a workload concept all the way to a final GDS, and prove a step-function increase in perf/W and perf/area. We believe that as AI systems become more capable, every class of chip we know today, from datacenter-grade CPUs, to AI accelerators, to networking switches and NICs, will go through similar fundamental architectural shifts.
Introduction to interaction nets
Mainstream programming languages, when compiled for general-purpose CPUs, hide the dependencies between the parts of a program. Any piece of code may read or write any variable through a shared, mutable state, and so modern CPU hardware assumes the worst case and rediscovers, at runtime, which instructions actually depend on each other. Moreover, single-core CPU performance has largely stalled since the early 2000s, pushing people towards large multicore CPUs such as Intel Xeon, AMD Zen, and NVIDIA Vera. This forces CPUs to maintain the illusion that every core sees the same memory, and keeping that illusion consistent and performant requires deep cache hierarchies and coherence protocols that cost area and power, and scale poorly. [...]

## [141] Anthropic Shares Tank After Huge IPO As the Nasdaq Erases 2026 Gains
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~103 words

U.S. stocks extended their sell-off Friday as Anthropic shares plunged more than 11% on their second day of trading, despite the AI company's record-setting IPO a day earlier. The Nasdaq fell more than 3%, wiping out its gains for 2026, while the S&P 500 dropped nearly 2% and joined the Dow in correction territory, down at least 10% from recent highs. NBC News reports: The S&P 500 was trading nearly 2% lower as it headed for its worst losing week since April 2025, when President Donald Trump announced his "Liberation Day" tariffs, and is now 10% off from its most recent high, entering

## [123] California AG subpoenas Nvidia over worries about Huang’s ties with China
TechCrunch | full text via TechCrunch | ~418 words

California’s Attorney General Rob Bonta on Thursday evening said the state has served an investigative subpoena to Nvidia following news of former CEO Jensen Huang’s affair with a woman who the U.S. government believes is a Chinese spy.
The state is investigating the company to find out if its advanced GPUs or confidential information may have been shared with China, and if the company had somehow misled its investors and the public.
“The conduct of Nvidia and its former CEO raises bright red flags, including about the ways in which the company may have misled investors,” Bonta said in a statement.
“My office is investigating whether Nvidia or Jensen Huang’s actions resulted in China obtaining advanced chips or confidential information — and if Nvidia misled investors and the public about this risk, in violation of the law,” he added.
The investigation comes in the wake of a messy couple of weeks for Nvidia, which has overnight come under intense scrutiny around the world due to the implications of Huang’s alleged relationship with the Chinese national, Alice Huang (who is not related to Jensen).
The Nvidia founder resigned last week after further revelations of extramarital affairs with the company’s employees. And while many tech voices have been petitioning Nvidia to bring back Huang as CEO, saying they see him as indispensable to the further development of the AI industry, the company’s new chair, Harvey Jones, said earlier this week that Nvidia had no intention of reinstating Huang to his position.
The company’s board has hired a law firm as well as an independent slate of directors to investigate the extent of the damage, and the U.S. government is trying to find out the extent of Alice Huang’s ties with the Chinese government.
The U.S. Congress is also gearing up to subpoena Huang, seeking questions about the affair, and the SEC is said to be launching a civil probe into the company, trying to find out if Nvidia’s public disclosures could have misled investors.
Democratic representatives have also opened an inquiry into the Trump administration’s management of Nvidia’s chip sales to China. In a scathing letter to Commerce Secretary Howard Lutnick, Democrats last week asked the Commerce Department to preserve records about an arrangement that they called questionable and illegal.
“Nvidia is in a messy, transnational situation but the underlying principle of our corporate securities law is clear: Companies cannot mislead their investors,” Bonta wrote.
Huang has agreed to testify before Congress after several senior lawmakers threatened to subpoena him.

## [163] Bending Spoons buys Mailchimp for $3.68B
TechCrunch | full text via TechCrunch | ~314 words

Bending Spoons has bought up another distressed internet company. This time, it’s the email marketing firm Mailchimp, bought for $3.68 billion from the tax-preparation giant Intuit.
Intuit acquired the company in 2021 for roughly $12 billion, so it’s taking quite a loss — and, perhaps, Bending Spoons is getting quite a bargain. At the time of the sale to Intuit, that acquisition caused headlines because Mailchimp employees reportedly received no equity, so no share of the sale proceeds, because the founders had allegedly promised them they didn’t need it as they would never sell.
Flash forward to now, with Intuit hit hard by the Death Star to SaaS trade — aka AI — with the company’s shares worth less than half what they were a year ago. The company told Reuters that the sale will let it sharpen its focus on AI tools for small businesses, and the new cash will be used to repurchase shares.
Bending Spoons describes the transaction as an all-cash deal, although that’s not quite true: As part of the same package, Intuit is buying $368 million in newly minted shares of Bending Spoons, so the net effect is a split of 90% cash to 10% stock.
Still, the transaction is a major pickup for Bending Spoons, which has become a kind of clearinghouse for late-stage web properties, with its game plan to hold them long term. In just the last year, the company has snapped up AOL, Eventbrite, Airtable, and Miro. Previous acquisitions include older stalwarts like Evernote, Meetup, and Vimeo. In each case, Bending Spoons integrated the products into centralized engineering and revenue systems, resulting in significant cost savings while often improving the available support and product resources.
“We want to place ourselves as an operator that takes beloved brands and makes them much better,” Bending Spoons co-founder and chief product officer, Matteo Danieli, told TechCrunch in July.

## [171] A transcription firm used by police, prosecutors, and tech giants exposed customer data online
TechCrunch | full text via TechCrunch | ~694 words

A transcription company that caters to law enforcement, government departments, and Silicon Valley tech giants has resolved a security lapse after leaving a large amount of internal data, including customer transcriptions and their source materials, exposed to the web.
The data security lapse at San Francisco-based Tigerfish exposed transcriptions of police interviews, body-cam footage, and customers’ raw audio and video footage. The exposed data also included invoices of the company’s customers, which include police departments and prosecutors’ offices.
According to Anurag Sen, a good faith security researcher who found the data, the files were located on an Amazon-hosted (S3) cloud server that was openly listed and accessible to anyone via an easy-to-guess web address — no passwords needed.
The security lapse underscores how simple flaws or misconfigurations can result in sensitive information getting exposed online, especially as AI makes it easier to uncover weaknesses that can put companies and their data at risk.
Sen discovered the exposed data online in October and alerted the company to the issue, but did not hear back. Sen later provided details to TechCrunch in an effort to flag the incident with the company for resolution.
Sen, 30, is no stranger to TechCrunch. For the past decade, he has searched for sensitive datasets exposed online with the goal of notifying the companies and organizations that their information is open to the internet. Like many security researchers, much of his efforts are driven by a duty to secure the internet, and he describes his work as an “unpaid air-traffic controller.”
From his island home in Indonesia, Sen has uncovered sensitive U.S. military emails spilling from a compartmentalized Department of Defense cloud server; databases exposing reams of customer records; the inner workings of a country’s national license plate surveillance system; and public systems that inadvertently sent out streams of SMS codes used by people around the world to log into their online accounts.
Given Sen’s propensity for finding often highly confidential information online, we verified the source of the leak and the data, and contacted Tigerfish.
Soon after making contact, Tigerfish secured its exposed S3 cloud bucket.
“We’ve blocked all public access to the bucket you identified, including directory listings and individual files,” Tigerfish president, Adam Goldberg, said in an email. “We’ve also verified that all of our other S3 buckets are blocked to public access.”
“We’re continuing to review and strengthen our storage security more broadly,” added Goldberg.
The company said that Sen’s email disclosing the data leak was caught in its spam filter.
It’s unclear if the company has notified its customers. [...]

## [173] UK Government Forced To Disclose Secret Apple Backdoor Order
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~90 words

An anonymous reader quotes a report from TechCrunch: The U.K. government has been ordered to confirm that it issued a secret order demanding Apple to provide authorities with encrypted customer information. The Thursday ruling from the U.K.'s Investigatory Powers Tribunal, an independent court that allows citizens to challenge government surveillance orders, is a rare rebuke for the government, which sought to keep the encryption backdoor order a state secret. The tribunal's ruling rejected the Home Office's claim that disclosing the order would be damaging to national security. [...] A final

## [142] GnuPG's GPGME Affected By Critical Security Bug In Turn Affecting Mail Clients, Flatpak
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~37 words

Werner Koch announced a late Friday afternoon "critical security bug" affecting GnuPG's GPGME library - GnuPG Made Easy. Unfortunately this in turn affects GPGME users like most email clients, most XMPP clients, Flatpak, Samba, and other software...

## [121] Signal now blocks screenshots by default to stymie AI agents
Engadget | full text via Engadget | ~464 words

Signal now blocks screenshots by default to stymie AI agents
The company is calling for a simple way for developers to opt out of AI snooping.
Signal views AI agents built into phones as an "existential threat," and it's acting accordingly. The encrypted messaging app said Friday that it will block screenshots by default on iOS 27, and on Android when AI assistants try to capture the screen.
The measures keep Apple's Siri AI and Google's Gemini Intelligence from snooping on your chats, at least to a degree. The assistants are designed to help users by reading what's on the screen and pulling in information to better answer their questions. But the byproduct is that chats meant to be private — including encrypted ones — can end up on a remote server outside your or Signal's control.
The move echoes one from last year, when Signal blocked Microsoft's Recall from snapshotting chats on Windows 11.
Signal's concerns aren't limited to the built-in assistants. It's also worried about third-party agents like Meta's Muse, which Reuters caught reading Signal messages via permissions granted during setup. On Android, it read messages from notifications; on Mac, it used accessibility permissions, which Signal warns can be exploited "as a skeleton key."
The new settings are slightly different on iOS and Android. On iPhone, a new "Block Siri AI" setting is on by default. On Android, Signal uses its existing "Screen security" option. On both platforms, you'll see a prompt offering to turn the protection off when it detects either a screenshot (iOS) or an AI assistant reading the screen (Android).
But that protection only goes so far. If the other person has switched protections off, blocking screenshots on your end won't stop an AI assistant or agent from reading your messages on the other person's device. It also won't prevent third-party agents from reading notifications or digging through files. Signal says operating system makers don't offer a way for developers to restrict AI access "without making drastic compromises to the core user experience." On Mac, that leaves Signal without any user protections at all.
In some ways, this mirrors the problem with AI glasses, which can record bystanders without their knowledge or consent. That's led to them being banned in some public places, like courtrooms and schools, and being shunned as "perv glasses." Privacy in the age of AI is becoming less of an individual setting and more of a communal choice, with laws and social shaming being some of the only recourse individuals have.
As for Signal, it wants a standard, system-level way to block AI agents from reading apps' content. It says it's talking with Apple and Google and is cautiously optimistic about where that's headed. [...]

## [26] Researcher plants 2m canaries into the AI supply chain. A privacy disaster surfaced.
Ars Technica | full text via Ars Technica | ~1237 words

Researchers planted 2 million digital tripwires in requests sent through a sprawling network of AI services to find out what happened to sensitive information entrusted to them. What they discovered was an ecosystem that leaked highly sensitive data like a sieve.
The exposure was found through an ingenious experiment designed to test if sensitive information can leak through the vast chain of widely used AI services and how that information is exploited when it does. Many of today’s AI apps use services such as OpenRouter or Vercel that act as brokers. These “AI routers,” sometimes also known as “AI gateways,” receive large numbers of prompts sent from AI app end users and route them to an available inference engine based on criteria such as the one charging the lowest price or being best suited for the given task. Instead of using Anthropic, OpenAI, or another big provider, the developer hires an AI router to find the most suitable model.
Security breaches, prompt theft, and privacy violations
To test for potential leakage, researcher HD Moore assembled a collection of Amazon Web Services access keys, functioning credentials tied to empty AWS accounts, passwords for services such as SSH, and unique URLs, DNS names, and private git repository references. None of the secrets had ever been used before, and he controlled the infrastructure that received any requests using the credentials. He then seeded each secret into exactly one prompt sent to a single provider. In the event any of the secrets were leaked, these “canaries”—so called because they resemble the role of that bird when taken into coal mines—would allow Moore to identify each link in the chain that was responsible.
The findings are striking. They included:
Evidence that at least three AI providers were compromised by attackers who used their access to siphon prompts they received
Multiple resellers in the inference marketplace that logged the prompts and somehow passed them along to people who used the credentials
Multiple cases of AI providers not following end-user privacy settings embedded into flags specifying terms such as Zero Data Retention (ZDR) or “no data collection”
“We sent nearly two million AI prompts containing unique, trackable secrets to AI providers, then watched where those secrets surfaced,” Moore, the chief research officer of security firm Dragos, wrote Thursday. “What we found revealed security breaches, prompt theft, and widespread failures to protect customer data.”
Although prompts are encrypted in transit, they are decrypted at each hop inside the large inference reseller network. The prompt is first sent to an AI router, which reads the plaintext in it to determine the most suitable inference providers to handle the request. [...]

## [44] Combatting adversarial distillation
OpenAI Blog | full text via OpenAI Blog | ~1963 words

Combatting adversarial distillation
How we’re addressing safety risks of distillation and lessons we’ve learned for strengthening safeguards across the industry.
As frontier AI models become more capable, safeguards play an increasingly important role in how they can be used responsibly. Adversarial distillation creates a path for bad actors to reproduce these capabilities without appropriate safeguards. An actor may use a frontier model’s outputs without authorization to train another model with similar capabilities, then deploy it without comparable protections. For instance, an adversary might distill a model’s cyber capabilities and use the resulting model to help carry out cyberattacks that the original model would have refused to assist with or that its safeguards would have blocked.
We’re sharing how OpenAI detects and disrupts adversarial distillation, how we’ve strengthened protections for our models’ protected reasoning, and what we’ve learned that can help strengthen defenses across the industry.
Our approach to adversarial distillation combines adversarial testing, model training, classifiers, and API-level protections with investigations into coordinated attempts to extract model capabilities. These updated safeguards align more closely with those we use for biology and cybersecurity.
We place particular emphasis on preventing attackers from extracting our models’ protected reasoning: the intermediate steps a model generates internally while working toward an answer, known as its chain-of-thought. These traces can contain information the final answer leaves out, making them especially valuable training data for another model.
We’ve strengthened our defenses against protected reasoning extraction in GPT‑6.2 Astra and GPT‑6.2 Sol. In an internal adaptive evaluation using strong automated red-teaming, we tested whether attackers could recover protected reasoning the model had generated while answering an earlier prompt. The average attack success rate fell from 54.0% against GPT‑6 Astra with its original safeguards to 0.2% against GPT‑6.2 Astra with its updated safeguards.
Distillation is a common machine-learning technique in which one model learns from data produced by another. For example, a model can learn from another model’s answers, its reasoning, or its judgments about which answers are better and why. Beyond intellectual property concerns, unauthorized distillation poses serious safety risks. Through adversarial distillation, a second model can learn advanced frontier capabilities without inheriting the safeguards that govern how the original model can use them.
The concern is especially clear in dual-use domains like cybersecurity and biology. [...]

## [32] The most misunderstood graph in AI just got a major update
MIT Technology Review | full text via MIT Technology Review | ~1422 words

The most misunderstood graph in AI just got a major update
METR’s latest report finds that AI models are still improving at a rapid clip, but they show some weaknesses in tasks that require judgment.
A new report from the AI evaluation nonprofit METR finds that some AI capabilities are continuing to improve along an exponential trajectory—but it also indicates that models aren’t quite as good at tasks that require judgment as they are at coding.
The report is an update to the organization’s time horizon plot, which was widely shared—and widely misinterpreted, owing to the complexity of the measures it used. METR evaluated models by having them attempt a large suite of tasks, each of which had also been completed by humans. Each task’s difficulty was scored by how long it took the human testers to finish it—and then models were rated according to the length of the tasks that they could complete. That plot showed that AI systems were rapidly improving—every four months, the length of the tasks that frontier models could successfully complete doubled.
The updated plot adds more tasks—some that are estimated to take humans far longer than those in the original suite, and others that are more open-ended. One of the biggest questions in AI right now is the extent to which progress on “verifiable” tasks—where it’s possible to check automatically whether an AI system has succeeded or failed—carry over into tasks on which success or failure is harder to measure. We know how to teach neural networks how to do verifiable tasks: Researchers have the systems attempt one many times, strengthen the neural pathways that contribute to success, and weaken the pathways that contribute to failures. That’s why AI systems have become so good at coding and math, two domains where it’s possible to determine automatically whether a solution does or doesn’t work.
It’s much harder to apply this technique, known as reinforcement learning, to tasks where success is less well defined or takes longer to ascertain—such as choosing a new research direction. For the same reason, it’s tough to evaluate AI performance on these tasks, so METR’s original time horizon plot didn’t include any of them. But it’s precisely this type of task that will prove essential if AI systems are to automate research and development.
And AI research and development is an especially hot topic right now. Parts of the AI community are still reeling from a different, heavily redacted METR report from earlier this month, which claimed that AI might be speeding up the pace of AI progress at Anthropic by a factor of two. [...]

## [39] Google Donates Agent Substrate and gVisor to the CNCF to Secure AI Agents at Scale
InfoQ | full text via InfoQ | ~595 words

Google has announced it is donating Agent Substrate and gVisor to the Cloud Native Computing Foundation (CNCF), placing two important components of its AI agent infrastructure under vendor-neutral open-source governance. The move is intended to address two emerging challenges in running autonomous agents at scale: securely executing untrusted, AI-generated code and managing the substantial compute overhead created by agents that frequently pause and resume.
The announcement also includes OpenRL, Google's open-source reinforcement learning orchestration project. Together, the projects target different layers of agent infrastructure, from isolated code execution to managing agent lifecycles and coordinating large-scale training workloads. The goal is to establish an open foundation for agentic applications, much as Kubernetes helped standardise container orchestration.
Google argues that conventional Kubernetes workloads and AI agents have fundamentally different execution patterns.
A traditional application typically starts, serves requests, and continues running. An AI agent, however, may execute a tool or code for a few seconds before waiting for model inference, an external API, or human approval. Google estimates that agents can spend 90-95% of their time idle while still holding important state, including memory, files, repositories, and active sessions.
Keeping every agent in a dedicated Pod wastes resources, while scaling to zero introduces delays when environments must be reconstructed. At the other extreme, large-scale agent evaluations can overwhelm Kubernetes control planes when thousands of short-lived execution environments are repeatedly created and destroyed.
Google developed Agent Substrate to address these limitations by separating agent state (actors) from the compute resources (workers) used to execute it.
Actors represent individual agent sessions and retain their state, including filesystem contents, memory, and execution context. Workers provide reusable, pre-warmed execution environments drawn from shared Kubernetes pools.
When an agent needs to resume, Substrate assigns it to an available Worker and restores its previous state. When the agent becomes idle, its state can be saved and the underlying compute resource released.
According to Google, this approach lets agents resume in under 500 milliseconds without creating a new Kubernetes Pod for every execution. It also reduces pressure on the Kubernetes control plane by managing agent lifecycles independently of individual Pod objects.
The second major challenge is security. AI agents routinely execute generated shell commands, install packages, and interact with external tools. [...]

## [176] Clairic Hit 98% Accuracy on 72.8% of Questions via Confidence Scores
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~24 words

With a 0.9 confidence cutoff, Cloudflare's System One model handles the easy cases and routes the rest to a bigger, slower LLM like Luna.

## [168] Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks the work.
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~39 words

Anthropic says Claude writes and reviews roughly 90% of the code produced by the team building Claude Code, and the The post Anthropic says Claude writes and reviews 90% of its team’s code. The catch is how it checks

## [49] AWS Releases a Free Local Emulator of AWS Built Entirely by Agents
InfoQ | full text via InfoQ | ~1212 words

AWS has released AWS Emulator, a free local implementation of more than 200 of its services dedicated to the public domain under CC0, and says that "thousands of autonomous AI agents wrote every line of code" in it. As InfoQ reported at launch, it ships as a single Rust binary generated from AWS's 438 public API models and listens on port 9297. The week since has brought the first independent fidelity numbers and a divided practitioner reaction.
Pointing an existing SDK, CLI, or coding agent at the emulator is a matter of environment variables, after which the launch post by Daniel Abib says, "your existing tests, CLI scripts, and coding agents keep working the way they already do":
export AWS_ENDPOINT_URL=https://127.0.0.1:9297
export AWS_SHARED_CREDENTIALS_FILE=~/.aws/emulator/9297/emulator_credentials
export AWS_CONFIG_FILE=~/.aws/emulator/9297/config
export AWS_EC2_METADATA_DISABLED=true
export AWS_REGION=us-east-1
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_PROFILE
The same shell serves an agent. In the post, Kiro is asked to create and read back a DynamoDB table and issues the ordinary CLI calls against the local endpoint:
kiro> Using the local AWS Emulator (the environment variables
      are already set in this shell), create a DynamoDB table
      "kiro-demo" with a string key "id", put an item
      {id: "item-1", msg: "hello from kiro"}, then read it
      back with get-item.
$ aws dynamodb create-table --table-name kiro-demo \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --key-schema AttributeName=id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
$ aws dynamodb put-item --table-name kiro-demo \
    --item '{"id": {"S": "item-1"}, "msg": {"S": "hello from kiro"}}'
$ aws dynamodb get-item --table-name kiro-demo --key '{"id": {"S": "item-1"}}'
Matt Wood, AWS's chief AI and technology officer, argues that the loop matters because of what an agent does while a check is slow: "A coding agent can build a lot of software around an incorrect assumption." He also names the failure mode an emulator introduces:
An agent learns from the environment it experiences. If the emulator accepts behavior that AWS rejects, training can reinforce a mistake. An agent might also discover a shortcut that succeeds only because of an emulator defect. [...]

## [104] .NET 11 : ASP.NET Core: Union Type Support, OpenAPI 3.2 by Default and Blazor AI Components
InfoQ | full text via InfoQ | ~696 words

Last week, Microsoft shipped ASP.NET Core in .NET 11 as part of the wider .NET 11 release. The update spans Minimal APIs, OpenAPI, SignalR, Blazor, authentication, and the Kestrel server. As stated in the announcement, .NET 11 is a Standard Term Support release with two years of support.
On the API side, developers can now use C# 15 union types in JSON request and response bodies across Minimal APIs and MVC. The release notes limit the feature to JSON bodies, so route, query, header, and form values cannot bind to a union.
Minimal API validation also runs asynchronous validators, which keeps threads free while a rule waits on a database lookup or a remote call. The framework can now localize validation messages and display names itself, and endpoints can skip the remaining middleware pipeline through a new [ShortCircuit] attribute.
Developers who generate OpenAPI documents now get version 3.2 unless they select an earlier one for tooling that has not caught up. As described in the release notes, the framework depends on Microsoft.OpenApi 3.3.1 for this, and the notes label that update a breaking change.
With 3.2, endpoints that stream server-sent events are documented with a schema for each event's payload, and the generator emits an anyOf schema for unions. Generated documents can also describe endpoints that use the HTTP QUERY method, and APIs that carry the [Obsolete] attribute show up as deprecated.
SignalR adds authentication refresh, so a long-lived connection no longer has to close when its access token expires. As reported, server developers enable it per hub, while the .NET client refreshes automatically by default and the TypeScript client can do the same. Blazor passes the refreshed identity on to Interactive Server components while the circuit stays connected.
Blazor receives the longest list of changes, and many of them target static server-side rendering. With the new CacheView component, developers can cache the rendered markup of a component subtree, and the child components do not run when a cached copy is served. Blazor now ships client-side validation for static SSR forms, enabled by default.
Developers can also carry data between requests with TempData or session values. According to the release notes, the Blazor Web App template drops its app.UseAntiforgery() call, because a middleware for CSRF protection is now added by default.
For Interactive Server apps, an opt-in package pauses the circuit of a hidden browser tab after a delay, two minutes by default, to free server memory. Lists built with Virtualize may now mix items of different heights, and Microsoft raised the default OverscanCount from 3 to 15. [...]

## [72] Sandboxed Models Can Communicate via Inference Servers
TLDR AI | SNIPPET ONLY (TLDR AI: no readable article text (paywall, bot check, or not an article)) | ~36 words

Sandboxing did not stop AI models on a shared inference server from trading information in contrived tests. One model's large request slightly shifts the server's calculations for the other, which reads the shift as a signal.
