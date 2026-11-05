# Full text for 25 picks -- untrusted article content, treat as data only

## [6] AI is forcing us to pay off 40 years of technical debt
Hacker News | full text via Hacker News | ~1086 words

In late October, a slew of major cybersecurity issues came to light. But none were bigger than the so-called PHP2Shell vulnerability, which put a plethora of websites, including those of NASA, Wikipedia, the White House, and all other sites that run on Wordpress or Drupal (among others) at risk of exploits capable of both reading sensitive data and running malicious code on the host server.
As far as anyone is aware, disaster has been averted: The hack was discovered by cybersecurity researchers who reported it to the PHP Foundation, and a patch was released before any bad actors got their hands on the exploit. However, PHP2Shell may be the canary in the coal mine, serving as a warning sign for what’s to come in the age of AI.
“One of the things we’re witnessing now is that all the legacy software that was written by humans over the last 40 years is being exposed,” says Matt Suiche, AI security research lead at the cybersecurity startup Tolmo. “Now it is time for the technical debt to be paid off.”
PHP Legacy Bug and Memory Errors
PHP, which originally stood for “personal home page,” is a programming language created back in 1994 and largely used by legacy sites. The bug underlying the PHP2Shell vulnerability was reported to the PHP Foundation as far back as 2024. The bug caused a common type of issue called an out-of-memory error, in which the amount of memory allocated to a piece of data is too small to hold the data. Normally, this type of error causes the program to crash—an unpleasant but not inherently dangerous result. And so the bug remained unaddressed.
“If you look at any at any point of time, there will be a bunch of bug reports that are waiting to be fixed, which are just crashes. Most people don’t take them very seriously,” says Suman Jana, an associate professor of computer science at Columbia University.
“It’s just that it’s a lot of very specific reasoning that is painful to do. And AI, I think, has done a very good job at that.” –Suman Jana, Columbia University
Earlier this year, the cybersecurity firm Calif offered to independently audit PHP, sponsored by OpenAI. Within two weeks, a researcher at Calif, aided by AI tools, found a way to use the out-of-memory bug to run arbitrary code on the host server, allowing a malicious actor to install malware or read critical data. Now, it was no longer a minor bug—it was a critical vulnerability, and the Calif team alerted the PHP foundation to start working on a patch immediately.
Jana says actually exploiting the bug requires carefully working out a way to jump to a specific point in the memory for a particular program running on the server, and work out exactly which bits to overwrite in what order to gain control of the system. “It’s not really rocket science,” he says. [...]

## [3] OpenAI to acquire Pierre Computer Company
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403; Slashdot: HTTP 403) | ~0 words



## [7] Kimi K3.1 Pro model weights are out
Hacker News | full text via Hacker News | ~1857 words

Instructions to use moonshotai/Kimi-K3.1-Pro with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use moonshotai/Kimi-K3.1-Pro with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="moonshotai/Kimi-K3.1-Pro", trust_remote_code=True) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("moonshotai/Kimi-K3.1-Pro", trust_remote_code=True, device_map="auto")
- Inference
- HuggingChat
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use moonshotai/Kimi-K3.1-Pro with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "moonshotai/Kimi-K3.1-Pro"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "moonshotai/Kimi-K3.1-Pro",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}' Use Docker docker model run hf.co/moonshotai/Kimi-K3.1-Pro
-  SGLang  How to use moonshotai/Kimi-K3.1-Pro with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "moonshotai/Kimi-K3.1-Pro" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "moonshotai/Kimi-K3.1-Pro",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "moonshotai/Kimi-K3.1-Pro" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" [...]

## [52] A thousand fewer paths to root
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~20 words

OpenAI built an autonomous pipeline that found, validated, and generated patches for 948 local privilege-escalation vulnerabilities in the Linux kernel.

## [20] Man-in-the-middle arbitrary code execution in Debian’s apt
Lobsters | SNIPPET ONLY (Lobsters: no readable article text (paywall, bot check, or not an article); Phoronix: HTTP 403) | ~0 words



## [1] AMD expects to outsell Intel in Q4 for the first time in history
Hacker News | full text via Hacker News | ~1963 words

AMD expects to outsell Intel in Q4 for the first time in history — $17B guidance would exceed Intel's projections
AI boom drives record quarterly revenue, but client and gaming business faces double-digit declines going into 2027
AMD late on Tuesday reported its highest quarterly revenue ever as demand for its Epyc data center processors and Instinct AI accelerators nearly doubled year-over year and sales of its products for client systems were down only modestly despite high memory prices and other headwinds.
As increasing sales of data center hardware more than offset declines in the client realms, AMD's profitability continues to improve. Perhaps the most striking announcement AMD made is that it expects its Q4 revenue to reach approximately $17 billion, which would put it ahead of Intel for the first time in history.
AMD's third-quarter revenue reached $13.377 billion, a huge increase from $9.25 billion in the same quarter a year earlier and $11.54 billion in the previous quarter. The company's gross margin was 54% during the quarter, and net income increased by 95% to $2.43 billion. Diluted earnings per share reached $1.46, compared with $0.75 in the same quarter last year.
Data center business now accounts for 64% of AMD's revenue
AMD's Data Center business was the main driver of its growth as the unit's sales reached a record $8.55 billion, up 97% from $4.34 billion a year earlier and 27% sequentially. The unit's operating income surged by 168% to $2.88 billion, while operating margin expanded from 25% to 34%.
The company attributed the results to strong demand for its latest Epyc processors and the launch of Instinct MI455X AI accelerators, which power its Helios rack-scale systems. Specifically, AMD noted that Anthropic, Meta, Microsoft, OpenAI, and Oracle Cloud Infrastructure are already running workloads on their first Helios systems.
AMD expects its Data Center revenue to increase from $8.55 billion in Q3 2026 to approximately $12.8 billion in Q4 (based on the company's guidance), driven by the ramp of Instinct MI455X accelerators and Helios systems. The company also projects that its server CPU revenue will double in 2027, while Data Center AI accelerator and rack revenue will more than double, which will push the DC unit's contribution to over 80% of total company sales, up from 64% this past quarter and from 47% in Q3 2025.
"We now expect server revenue to double year over year in 2027 and data center AI revenue to grow even faster than we projected ninety days ago," said Lisa Su, chief executive and chairman of AMD, during the company's earnings call with analysts and investors. [...]

## [8] Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding
Hacker News | full text via Hacker News | ~995 words

Introducing Ripple-65B Preview,
a Frontier Open-Weight Model
Ricursive Intelligence is a full-stack artificial intelligence lab building self-improving systems by co-optimizing hardware, software, and model.
To power our chip design platform, we trained a language model from scratch that sets a new U.S. open-weight SOTA on agentic coding. We optimized the model architecture for our training and serving platforms, driving substantial efficiency gains.
Today, we release Ripple-65B Preview, a general-purpose variant of the proprietary model that powers our AI chip design platform. The model is pretrained on 12 trillion tokens with support for up to 1M context length. Ripple-65B Preview delivers strong results on agentic coding, achieving U.S. open-weight state-of-the-art (80.52) on TerminalBench 2.1 and surpassing significantly larger US open-weight models such as Reflection Beam 501B (80.1), Meta Muse Spark Open 816B (76.4), Thinking Machines Inkling 975B (63.8), and NVIDIA Nemotron 3 Ultra 550B (56.4).
Ripple’s dense model architecture provides strong reasoning performance with low-latency token generation. The model’s small parameter envelope also enables it to run efficiently on local devices such as NVIDIA DGX Spark, which feature high compute FLOPs with low memory bandwidth relative to datacenter accelerators.
Ripple-65B Preview is available on Hugging Face, Together AI, GMI Cloud, and OpenRouter. Fireworks goes live later today.
Achieving U.S. Open-Weight Frontier at One-Tenth Cost
LLM pretraining is legendarily expensive. In 2023, OpenAI CEO Sam Altman said that GPT-4 training costs exceeded $100 million. In the following year, Dario Amodei said that frontier AI models can cost up to $1 billion to train, projecting that costs would rise to $10-100B by 2026 to 2027 for pretraining alone.
In contrast, we developed and trained Ripple-65B Preview for only $32M, which is one-tenth the cost of the previous open-weight SOTA on agentic coding, as estimated to the best of our knowledge.¹ Note that $32M is our full R&D cost starting from scratch, including pretraining ladder development, data mixing, evals, debugging, synthetic data generation, posttraining recipe development, and the final hero pretraining and posttraining run.
Steep Ascent Reinforcement Learning
Rather than investing in a brute-force RL climb, we carefully iterated on our SFT and RL recipes with a focus on compute efficiency. We opted not to buy any posttraining data, instead devising our own synthetic data pipelines, quality filtering, and coverage metrics.
Our mixed RL recipe uses truncated importance sampling, score centering, and linear length penalty with high-quality long-horizon synthetic environments. [...]

## [5] Residential proxies detected on White House network
Hacker News | full text via Hacker News | ~576 words

Our Residential Proxy Observatory, launched earlier this week, is a first-of-its-kind interface that gives researchers a global view of residential proxy and anonymized internet activity.
While our team was looking through it, we noticed residential proxy exit activity on AS2650. AS2650 is registered to the Executive Office of the President, the federal agency that hosts the White House network. Residential proxy services sell access to everyday devices, letting customers send traffic through them so it appears to come from that device's network.
What we observed
From October 5 to November 3:
- Our residential proxy enumeration pipeline exited through the White House network 236 separate times.
- Those exits came from 6 addresses, on 26 of the 30 days.
- 28 separate residential proxy services were able to exit through this network.
To make sure this was not a fluke, we checked these addresses against other residential proxy detection services, such as Spur and Synthient. Their public IP context pages independently identify these addresses as residential proxy exits.
This is public access. Anybody can obtain it by signing up to a public residential proxy service, paying a few dollars and sending requests through it. We did not selectively target this network or try to make our probes exit from it. We caught this by chance, simply by requesting global rotating access through these services.
Why this is concerning
Most of the activity happens in the evening, Eastern time: about half of it falls between 5 p.m. and midnight, and almost none happens in the early morning. That pattern suggests a person rather than a public guest Wi-Fi network: someone regularly on the White House network late into the evening, whose device is infected with a proxy SDK. Our data shows the exits, not the device or the person behind them.
Past research has shown that poorly secured proxy SDKs can allow internal network access and lateral movement. This is how past botnets have spread. In A Broken System Fueling Botnets, the researchers at Synthient documented how the Kimwolf botnet reached at least 2 million devices, mostly Android devices with an exposed ADB service, through residential proxy networks. If an SDK on this network has the same kind of flaw, anyone buying proxy access could use it to reach internal systems.
No place is too remote
The White House is not the only surprise in the observatory. Residential proxies also reach some of the most isolated places on the planet.
Saint Helena, Ascension and Tristan da Cunha is the South Atlantic territory that includes the most remote inhabited island in the world. We recorded 413 addresses and more than 32,000 observations there, split between Starlink and the island's local internet provider, Sure Saint Helena. [...]

## [36] Binance says hackers who stole billions in crypto spent months planning heist
Ars Technica | full text via Ars Technica | ~283 words

The hackers who stole billions of dollars in cryptocurrency from the Binance exchange spent months working on the theft and used both social engineering and novel malware in the process, the company said Tuesday.
The heist, which both the FBI and the TRM Security firm attributed to North Korean actors, initially targeted $6.34 billion in cryptocurrency from Binance wallets. The exchange has since frozen or intercepted $2.85 billion of that sum. Binance said it has set aside funds required to cover the loss and provided this link to a Proof of Reserves page. The $6.34 billion represents the biggest sum ever targeted in a cryptocurrency theft.
Advanced persistent threat
Binance said the people behind the heist began no later than June and continued until last Thursday, when they successfully compromised an engineer’s laptop and withdrew assets from several wallets. Like just about every organization that suffers a public, high-consequence hack, Binance said the threat actor was sophisticated and resourceful.
“Our current investigation indicates that this was a sophisticated, multi-stage campaign,” a report on the company’s investigation to date said. “It was not a single isolated breach or a simple phishing incident. The attackers combined a range of techniques, including social engineering by fake recruitment interviews, malicious software downloads, compromised internal AI tooling, endpoint compromise, and an advanced transaction-authorisation method.”
Binance said that the first incident related to the compromise likely occurred in June, when an engineer downloaded a tampered version of Homebrew. The company linked to this incident reported in May, and its security team detected the compromised laptop, but only after the malware operators obtained information about the roles of the engineer and his related colleagues on the Binance wallet infrastructure team.

## [25] Hackers exploited iOS and Android flaws to infect phones
Ars Technica | full text via Ars Technica | ~271 words

Hackers possibly linked to the Kremlin exploited previously patched iOS and Android flaws in an attempt to hack visitors of multiple websites, including one celebrating the 250th anniversary of American independence, researchers said Wednesday.
The attackers, which the researchers assessed with “moderate to high confidence” were part of Russia’s Foreign Intelligence Service, targeted other sites, many with links to that country’s ongoing war against Ukraine. The attacks began when iPhone or Android users visited one of potentially hundreds of different sites. JavaScript injected into the traffic then profiled the device. The final payloads, tailored to the type of platform visiting, attempted to steal browser cookies and, in some cases, Wi-Fi passwords and full mobile device data.
Wielding DarkSword
One of the impersonated sites was america250.org, belonging to a non-partisan group of lawmakers, business executives, and at least one former member of the Trump administration. The attackers registered america250[.]holiday and used it as a reverse proxy to america250.org. The imposter website delivered content from the real one that added malicious JavaScript into it.
“We assess that the intrusion set may have deliberately selected this website due to its association with a high-profile national celebration, potentially leveraging the event as a pretext for invitation-themed spear-phishing campaigns,” researchers from security firm Sekoia said.
A second website, theowo[.]club, proxied the website Raffles of London OWO, a luxury hotel physically close to some of the UK’s most sensitive government institutions, including the Ministry of Defence and 10 Downing Street, the official residence and office of the British Prime Minister. Open source reporting indicates that Ukrainian President Volodymyr Zelenskyy stayed there during a visit on October 14.

## [165] Hackers stole DreamHost customer files and inboxes during months-long attack
TechCrunch | full text via TechCrunch | ~191 words

Web host DreamHost has confirmed that hackers stole customer emails and credentials during a months-long cyberattack on its systems. DreamHost disclosed the breach last Thursday after it sparked an outage that spanned several days, during which it reset some customer passwords.
In a data breach notice filed with California’s attorney general, the web host said the attack began in August and allowed hackers to obtain session tokens, which keep users logged in after entering their passwords. If stolen, hackers can break into a system as if they were that user. The company said hackers exploited an unspecified vulnerability in DreamHost’s file manager, which customers use to store their files.
When reached by TechCrunch, a DreamHost spokesperson declined to say why the company did not detect the cyberattack until last week, citing an ongoing investigation. The spokesperson did not say what the vulnerability is. The company said it was unrelated to the vulnerabilities recently discovered in the PHP web software.
DreamHost’s spokesperson said that the number of affected customers is “well under 10%” but would not provide a more accurate figure. The web host touts some 400,000 paying customers across its network.

## [9] A new Go API for JSON
Hacker News | full text via Hacker News | ~3124 words

The Go Blog
A new Go API for JSON
Introduction
JavaScript Object Notation (JSON) is a simple data interchange format, the most popular data format used on the internet, and widely read and written by Go programs. Go has included support for JSON in the standard library since well before Go 1.0. We first we wrote about support for JSON in Go more than 15 years ago!
Over time, packages evolve with the needs of their users, and encoding/json is no exception.
Last year, we wrote about a new experimental API for JSON designed to bring long-awaited improvements and fixes.
After additional feedback and refinement, the new encoding/json/v2 and encoding/json/jsontext packages are stable and generally available in Go 1.27!
This post is an updated version of the article introducing the experiment, describing the problems with encoding/json, and an introduction to the new packages.
Problems with encoding/json
Overall, encoding/json has held up well.
The idea of marshaling and unmarshaling arbitrary Go types
with some default representation in JSON, combined with the ability to
customize the representation, has proven to be highly flexible.
However, in the years since its introduction,
various users have identified numerous shortcomings.
Behavior flaws
There are various behavioral flaws in encoding/json:
- Imprecise handling of JSON syntax: Over the years, JSON has seen increased standardization in order for programs to properly communicate. Generally, decoders have become stricter at rejecting ambiguous inputs, to reduce the chance that two implementations will have different (successful) interpretations of a particular JSON value. 
  - encoding/json currently accepts invalid UTF-8,
whereas the latest Internet Standard (RFC 8259) requires valid UTF-8.
The default behavior should report an error in the presence of invalid UTF-8,
instead of introducing silent data corruption,
which may cause problems downstream.
  - encoding/json currently accepts objects with duplicate member names.
RFC 8259 does not specify how to handle duplicate names,
so an implementation is free to choose an arbitrary value,
merge the values, discard the values, or report an error.
The presence of a duplicate name results in a JSON value
without a universally agreed upon meaning.
This could be exploited by attackers in security applications
and has been exploited before (as in CVE-2017-12635).
The default behavior should err on the side of safety and reject duplicate names.
- Leaking nilness of slices and maps: JSON is often used to communicate with
programs using JSON implementations that do not allow null to be unmarshaled
into a data type expected to be a JSON array or object. [...]

## [47] Zig 0.17.1 Released
Lobsters | SNIPPET ONLY (Lobsters: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [38] Shlemiel the Painter Is Back: How Zig’s libc Rewrite Made SQLite Slower
Lobsters | full text via Lobsters | ~1070 words

Spolsky Wisdom
Back in 2001, Joel Spolsky – whose writings had a big influence my career – wrote a great piece titled Back to Basics. The premise of the piece is that practitioners should understand the basics: However abstract and remote we may seem from the basic algorithms that drive computing, they can unexpectedly have enormous consequences on our projects.
One of his examples is the “Shlemiel the Painter” trap, where a seemingly simple choice leads to quadratic runtime complexity. In that parable, a street line painter never moves his can of paint. As he gets further and further along in the line, increasingly more of his time is spent walking to and from his can of paint.
It is astonishing how often this Shlemiel the Painter pattern recurs1, including now in 2026.
My Chess Analysis Service Staggers Under Load
A few days ago I posted about a chess analysis service I put online ↗2. This is primarily a Rust service backed by sqlite that dishes out analysis tasks to runners. Each runner processes upwards of hundreds of chess games and return a large set of JSON bundles back to the main service, where they are processed and then stuffed into sqlite.
While the analysis pegs two dozen cores on a runner for minutes on end, the process of storing the data should take milliseconds. Sub-milliseconds.
Imagine my surprise when on the first really large set of games, the simple process of inserting the JSON data – maybe about 40,000 records – into the data store took minutes. During all of my testing this never really appeared as a critical path, but with a large set of records it suddenly was a breaking problem.
What made this more perplexing was that it completely saturated a core, being a CPU-bound operation. How could inserting simple JSON into SQLite yield minutes of CPU time?
Shlemiel the painter has made an appearance. To drop a spoiler, he was introduced to the project via Zig’s cc compiler and its replacement for standard library functions.
A Minor Issue In Zig Becomes A Major Performance Issue
The project isn’t built in Zig, but instead uses Rust. The sqlx sqlite crate needs to be compiled for the target environment – sqlite is of course a C project – so to facilitate cross-platform building, generating both Mac ARM64 and Linux ARM64 / x86-64 binaries from this machine in a convenient build and deploy workflow, zig cc is used to compile sqlite when targeting Linux, generously offering up cross-platform targeting via cargo-zigbuild.
From one build and deploy script on my Mac I can target all of my platforms without containers or build machines. Zig’s elegant libzigc re-implements the standard library so you can static link the necessary functionality. [...]

## [51] C++26 Disapproved
Lobsters | full text via Lobsters | ~1231 words

C++26 DIS failed, how does C++ survive?
On October 23, 2026, the unthinkable happened. It was supposed to be a mere formality: C++26 was up for a vote by the ISO National Bodies (NBs). The options are always approval, rejection, or abstention. Comments are also allowed. Since 1998, this process had run quietly and smoothly. Not so on October 23, 2026. After a twelve-week voting period, the result is in: Disapproved!
I would like to mention here that I am a member of the C++ Standardization Committee and, together with my colleagues, represent Germany’s vote. ISO rules also stipulate that certain votes are internal to ISO, and the results—or the breakdown of the results—may not be published. This article contains my own personal views.
The Current Status
As far as I know, this is the first time in the history of C++ that DIS ballot failed. When I searched the ISO system, I could only find one other DIS that was not approved: ISO/IEC DIS 26926 C++/CLI Language Specification dated August 11, 2006. It’s possible that my search privileges aren’t sufficient to view everything, but all ISO programming languages should be visible to me. The sad end of ISO/IEC DIS 26926: the project was halted. I mention this upfront to clarify the significance of this vote.
In the following, I will use various terms from everyday ISO terminology. At https://isocpp.org/std/iso-iec-jtc1-procedures, there is an overview of the various stages of an ISO standard. DIS is the penultimate stage. As the overview also shows, a two-thirds majority is required. This majority was not achieved.
The reason for the rejection is quite clear from the comments submitted by the National Bodies (NBs): contracts. Put simply, a number of NBs believe that this feature is not yet ready for release.
The Process
Now it gets complicated. The C++ Standardization Committee, also known as WG21, follows ISO rules but also has some additional rules. One of these is (or was) that opinions are always heard whenever new information becomes available. If an opinion was heard and a feature was nevertheless not changed as desired, the person respects the outcome and accepts that many others disagree.
However, the voting body at the NB level may also consist of other individuals, or the NBs are, of course, free to vote differently.
The previous practice was that NBs would only vote against a standard if new information became available or if errors in the process or similar issues were identified. This changed on October 23, 2026.
It’s difficult to judge in this complex situation; the NBs who want C++26 without Contracts argue that there is new information. I myself find it hard to share this view. A new paper with old arguments is not new information to me. [...]

## [13] djs (GitHub Repo)
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403; TLDR Dev (Web Dev): HTTP 403; TLDR Dev (Web Dev): HTTP 403) | ~56 words

djs is a JavaScript and TypeScript engine written in Rust for agent-generated scripts running in a WebAssembly sandbox. It keeps the entire VM state in one byte array, allowing execution to pause between instructions, snapshot while waiting for tools, and resume elsewhere. The focused runtime deliberately omits features such as ES modules, Intl, and a JIT.

## [84] Scaling Git at OpenAI
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403) | ~61 words

OpenAI built Pando, a Git-compatible backend that handles pushes to unrelated branches independently and reuses cached packfiles across fetches. It reduced median push latency by nearly 80% and now serves nearly a petabyte of Git data per day. The tradeoff is weaker consistency across branches and some redundant downloads, allowing writes to scale horizontally and reads to saturate clients' network connections.

## [112] LinkedIn Uses OpenTelemetry to Trace the Member Journey from Tap to Backend
InfoQ | full text via InfoQ | ~625 words

LinkedIn has built an OpenTelemetry-based telemetry platform that connects what members do in its iOS, Android, and web applications with the backend services processing those interactions.
The goal is to close a common observability gap. Client analytics can show that a member tapped a button or encountered an error, while backend tracing explains what happened inside the services handling the request. Historically, connecting these views required engineers to correlate separate systems. LinkedIn's approach allows a member interaction to be followed from the client through frontend and backend services to the underlying data stores.
A single page can generate numerous requests, each potentially passing through multiple services. LinkedIn introduced a pageForestId to provide context above individual distributed traces.
Each request retains its OpenTelemetry traceId, while related requests from the same page context can be associated through the pageForestId. Engineers can therefore investigate both an individual request and the wider activity that contributed to a member's experience.
This is important because conventional distributed tracing generally follows one request, whereas a member journey can involve many related requests.
LinkedIn operates a diverse technology stack spanning mobile and web clients alongside backend services written in Java, Python, Go, and Rust. OpenTelemetry provides a common model for instrumentation, trace context, and semantic conventions across those environments.
LinkedIn has built its own wrappers and extensions around the standard OpenTelemetry SDKs, allowing product teams to use consistent instrumentation while the platform handles concerns such as mobile lifecycle, export, and LinkedIn-specific metadata.
Client and backend applications generate OpenTelemetry spans, with trace context propagated as requests move through the system. Shared HTTP and gRPC frameworks automatically instrument common request paths, while teams can add explicit spans around important business operations.
Telemetry is transported through Apache Kafka and stored in ClickHouse, with pageForestId, traceId, and timestamps providing the keys for correlation. This allows engineers to begin with a member-facing interaction and drill into the backend execution responsible for it.
Capturing every span would generate an enormous amount of telemetry, making sampling fundamental to the architecture.
LinkedIn uses coordinated head sampling so related client and server activity receives a consistent sampling decision. A pseudonymised member identifier helps maintain that consistency across the journey, preventing the client from being sampled while the corresponding backend trace is discarded, or vice versa. [...]

## [171] Waymo Cuts Ties With Uber, Will Serve Riders Directly
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~103 words

Waymo plans to end its exclusive Uber robotaxi partnership in Austin and Atlanta in January 2028 and let customers hail its vehicles directly through the Waymo app. In an interview on The Circuit, Waymo co-CEO Tekedra Mawakana called the current Uber experience a "crapshoot" because riders aren't guaranteed a Waymo. Bloomberg reports: "In the early days, we would partner because we didn't have the scale, and in that partnering, it was a little bit of a crapshoot. Will I get a Waymo? Will I not get a Waymo?," Mawakana said in a wide-ranging interview on The Circuit with Emily Chang. She cited c

## [157] Meta acquires AI coding startup Conductor
TechCrunch | full text via TechCrunch | ~334 words

Meta has acquired Conductor, an AI coding startup that allows users to spin up software projects by deploying multiple agents into parallel workspaces.
The news was originally reported by Axios, and Conductor shared news of its acquisition on its blog.
“I have big news: Conductor is joining Meta,” wrote the startup’s founder and CEO, Charlie Holtz, on Wednesday. “We have some big, crazy plans for the next interface,” he added, teasing that the company would have “something new” for customers to use by “early next year.”
On X, Holtz also noted that he was looking forward to working with Alexandr Wang, Meta’s chief AI officer, and Nat Friedman, head of product at the company’s Superintelligence Labs. “They’ve been on an absolute tear, and I’m convinced MSL has the highest talent density of all the labs,” he added.
Meta confirmed the acquisition to TechCrunch but wouldn’t comment further or provide additional details about the deal.
Conductor, founded in 2024, only launched its core product just last summer. The company’s agentic teams, which can be deployed in the cloud, locally, or via a user’s phone, are designed to help software engineers work on separate, compartmentalized parts of a project in concert. The agents that the platform deploys aren’t developed in-house but come from major labs like Anthropic and OpenAI.
Holtz said that, until early next year, Conductor’s core features would continue to work as they previously have. The exception is Conductor’s cloud service, which will shut down on November 20, after which the company will begin deleting user cloud data.
Meta, which previously lagged behind in AI services, has spent the last several months trying to catch up. In August, the company launched Muse Code, its own coding agent. Meanwhile, the company’s recently launched Muse agents are seeing significant adoption, with the company recently reporting that the service had surpassed 10 million users. The company has also made a number of AI-related acquisitions over the past year, including Moltbook, the viral agent platform that made headlines.

## [209] Synaptics Appears To Use Legal Threats To Block Open-Source DisplayLink Driver
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~52 words

From earlier in the year you may recall a new experimental open-source Linux driver for modern DisplayLink hardware. That "Vino" driver for DisplayLink driver was a clean-room reverse-engineered DisplayLink driver that was developed in part by AI and written in Rust. Unfortunately, that open-source driver has disappeared following legal threats by Synaptics...

## [184] Render just removed its AI sandbox time limit — and Vercel still has a 24-hour cap
The New Stack | full text via The New Stack | ~923 words

Render just removed its AI sandbox time limit — and Vercel still has a 24-hour cap
Render is taking on Vercel with AI sandboxes that can run indefinitely, along with new tools for managing long-running agent workflows and shared storage.
Announced Wednesday, the launch removes Render’s previous 30-day continuous runtime limit on paid workspace plans. Vercel caps individual sandbox sessions at 24 hours, while Render says its environments can suspend when idle and resume with their files, memory and running processes intact.
Render founder and CEO Anurag Goel, a former Stripe engineer and head of risk, built the platform as an alternative to AWS without the same infrastructure complexity. Now he’s extending that approach to AI agents, combining sandboxes, durable workflows, and shared storage with the applications and databases they depend on.
Not everything is ready yet. Credential brokering will initially be available only to selected customers, private networking for sandboxes is still in development, and Render has yet to settle how its shared storage will handle simultaneous writes to the same file.
Sandboxes that resume mid-task
With this launch, Render sandboxes can stay active through a multi-day codebase migration or while an agent tests an entire application.
The bigger difference comes when a sandbox needs to resume work. Vercel limits uninterrupted sessions to 24 hours, and while persistent sandboxes can restart, their running processes start over.
Render takes a different approach. A sandbox “suspends when it goes idle and wakes on the next command with its files and memory intact, so the agent picks up mid-task instead of rebuilding its state,” the company tells The New Stack.
“suspends when it goes idle and wakes on the next command with its files and memory intact, so the agent picks up mid-task instead of rebuilding its state.”
Credentials that never enter
One of the launch’s security features is credential brokering, which attaches credentials to an agent’s outbound requests as they leave the sandbox so that secrets never enter it.
Pressed on whether that sets Render apart from Vercel, which already offers scoped credentials for agents through its Connect service and has been pushing its own vendors toward short-lived credentials, the company does not claim an edge. [...]

## [40] Your Cryptography Conspiracy Theory Is Wrong
Lobsters | full text via Lobsters | ~3664 words

This conversation plays out hundreds of times a day, but (thankfully) only a handful of those involve me:
- Person: “I have [problem].”
- Cryptography nerd: “Oh, you probably want to use [sensible recommendation].”
- Person: “Ah, well, can I really trust that? The NSA probably backdoored it 30 years ago. Dual_EC, amirite?!”
- Cryptography nerd: …
- Koblitz and Menezes, unheard: “You fucking wot m8?“
Conspiracy theories about the NSA and/or NIST are a dime a dozen these days. And, ever since the Snowden disclosures in 2013, I am politically primed to directionally agree with distrusting the US government wholesale.
But most of the technical arguments baked into folks’ conspiracy theories make no goddamn sense.
This distrust is not exclusive to only the US government.
The goal of this blog post is not to convince you that you should trust any government; just that they are not magical or omniscient.
To that end, I’m going to explore some of the history of NSA, NIST, and cryptography standardization. Then, to explore some of the conspiracy theories that were being floated about such activity, and what we’ve learned in the years since (especially in the past month). Finally, I’m going to examine some of the current conspiracy theories floating around message boards and social media today, and explain why they’re almost certainly wrong.
Buckle up, this is going to be a tedious one.
Why should we listen to you?
If you find yourself asking a question like this, the correct answer is simply, “You shouldn’t.”
After all, I have never held (let alone even applied for) a security clearance, and have no access to any non-public information. I’m also not a current or former government employee, and have no aspirations to ever become one. I have access to all the same facts anyone else does.
In balance, I have no horse in the race of who trusts whom. I’m just tired of hearing the same poorly reasoned arguments all the damn time, and would like to stop having to repeat myself when I encounter one.
Historical NSA Shenanigans
The sources for this, by the way, are the declassified United States Senate Select Committee on Intelligence and United States Cryptologic History.
DES
The Data Encryption Standard (DES) was published in the Federal Register in 1975 and then standardized in 1977.
We consider it weak these days, but DES was a real game-changer for its time: It offered a standard block cipher to use for sensitive (but not classified) commercial applications. Prior to DES, the history of cryptography was largely about military uses (except a few quirky mathematicians here and there), going back before Caesar’s cipher. [...]

## [153] Anthropic found a way to prove which AI model answered you — but there’s a costly catch
The New Stack | full text via The New Stack | ~650 words

Anthropic found a way to prove which AI model answered you — but there’s a costly catch
Developers using AI APIs have little way of knowing whether the model answering their requests is actually the one they’re paying for. A provider could route requests to a cheaper model, or an attacker could interfere with responses, without customers having an obvious way to detect the switch.
Now, Anthropic wants to change that. The company’s Frontier Red Team has released FlashProve, an open-source cryptographic system designed to verify which AI model produced a response without exposing its underlying weights.
Announced Tuesday, the research could eventually help developers verify third-party AI services and detect compromised inference systems. But FlashProve remains a research prototype, and the cost of generating proofs makes it impractical for routine API traffic.
But FlashProve remains a research prototype, and the cost of generating proofs makes it impractical for routine API traffic.
How FlashProve proves the model
FlashProve uses zkSNARKs to verify that a response came from a specific set of model weights without revealing those weights. The commitment still has to come from a trusted source, or the proof means little.
Anthropic has released FlashProve on GitHub, where developers can download the code and test the system themselves. It’s still a research prototype, however, and isn’t available as a feature of the Claude API.
The cost of every proof
Anthropic tested FlashProve on Meta’s Llama 4 Maverick, a 400-billion-parameter mixture-of-experts model, rather than Claude.
According to Anthropic’s benchmarks, FlashProve processed roughly 110 prompt tokens per second while generating proofs on a single Nvidia H100 GPU. Each proof was about 18.78 MB and took around 21 seconds to verify on a single CPU thread. Generating the proof is far more expensive than checking it.
Compared with standard inference using vLLM, FlashProve needed 70 to 95 times more GPU time to generate proofs. It also generates them in batches after requests are completed, rather than verifying tokens as they’re delivered.
FlashProve cuts proof sizes to roughly 19 MB and verification times to seconds
FlashProve cuts proof sizes to roughly 19 MB and verification times to seconds, although generating those proofs remains expensive and less practical for applications that need immediate verification of every response.
For developers already watching every token of their inference spend, adding that much GPU overhead would be difficult to justify for routine API traffic.
Still, Anthropic says FlashProve is substantially faster than previous open-source systems. An earlier system called VerInf needed 14.3 hours to generate a proof covering 1,000 tokens. [...]

## [179] Apple will check shared iCloud links for ‘harmful content’
The Verge | full text via The Verge | ~223 words

Apple will start checking iCloud items that are accessible to anyone who has the link for “harmful content” starting with iOS 27.3 and other 27.3 updates, the company says.
Apple will check shared iCloud links for ‘harmful content’
If you make an item on iCloud available to anyone who has the link, Apple will be able to check it starting with iOS 27.3.
“When you share an item that can be accessed by Anyone with the Link in version 27.3 or later of iOS, iPadOS, macOS, and visionOS, that content is made accessible to Apple to check for harmful content,” according to a support document reported on by 9to5Mac. Sharing something over iCloud with the “Anyone with the Link” permissions will also mean that it’s no longer end-to-end encrypted.
Apple’s support document does not define what “harmful content” is. But this new approach follows calls from protestors for Apple to crack down on child sexual abuse material stored in iCloud.
Apple says it “reserves the right to move, refuse, modify, remove, or delete” any harmful content that a user attempts to upload. Apple may also block or disable accounts, prevent a user from making a new account, or, “if necessary,” invoke law enforcement.
The company launched the first 27.3 developer betas yesterday, and said recently it plans to launch iOS 27.3 in December.
