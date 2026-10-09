# Full text for 30 picks -- untrusted article content, treat as data only

## [6] Why isn't the industry freaking out about DeepSeek 4.1 Flash?
Hacker News | full text via Hacker News | ~676 words

Why Isn't The Industry Freaking Out About DeepSeek 4.1 Flash?
	
		 I have been using DeepSeek 4.1 Flash for about a month, heavily, across a dozen projects. It is super capable, and orders of magnitude cheaper than the "frontier" models. When I'm mid-session, if I don't look at the model name, I honestly could not tell you if I'm using DeepSeek or Opus. Whether it's our conversations, the work, or the speed, I don't notice a difference. I don't care that there is no 4.1 "Pro". I treat this like a frontier model because it behaves like one. I'm coming at this from my subjective usage experience, but you can see more complete benchmarks here if that floats your boat. So why aren't the frontier labs freaking out right now? China is going to eat their lunch. They may be a month or two behind Anthropic/OpenAI, but these distilled Chinese models can handle the same workloads. Sure, they stole Claude's training, and Anthropic stole it from other people. I'm not getting into the whole who-owns-whose-data debate, because most developers aren't thinking like that. They're just trying to get the most bang for their buck. Today's models are now good enough for high-quality unattended tasks. Chasing the latest and greatest is silly. It is fun to see the new Fable capabilities, but the tasks we throw at them are usually ridiculous (maybe even insulting) if you believe in LLM sentience. It's like asking a math PhD to organize the files on your desktop. With my OpenCode Go sub of $10/month, DeepSeek is basically unlimited. This has completely changed my way of developing. There is no shame now in spinning up mindless tasks, or exploratory UI monkey testing. And sure, go ahead and reorganize your desktop files. That will cost $0.003 instead of $1. I have rarely exceeded $1 in expected costs in a session. I try to keep my sessions tight, but sometimes they run for most of a day. I even lean on 4.1 Flash for complex planning and research. For occasional critical tasks, I sometimes pull in Opus 5.5 to do a final code review, which will catch a few edge cases. Then I have DeepSeek execute the fixes. Even when I call up Opus or GLM (which seems to be drinking the same Chinese Kool-Aid as DeepSeek), it's less about quality and capabilities and more about getting new eyes on a problem. DeepSeek shrank the KV cache by roughly 437x compared to their V1 model. Holding that cache in GPU memory is one of the biggest costs of running long coding sessions. [...]

## [69] The Mathocalypse
TLDR Tech | full text via TLDR Tech | ~2701 words

The Mathocalypse
… then they came for Navier–Stokes and I said nothing because I never worked on Navier–Stokes. But when they came for RL vs. L I realized that things are serious
–friend-of-the-blog Omer Reingold (shared with permission)
Last night my 9-year-old son was taunting my wife, complexity theorist Dana Moshkovitz, as follows: “mommy, I heard you got cooked! I heard that a robot solved the math problem you worked on for your whole career! OOF!”
While my son was being a brat, he also wasn’t wrong. Whether you’re thrilled, depressed, angry, or whatever else about it, yesterday was surely one of the biggest days in mathematical history. And yes, among the 372 huge results released yesterday by OpenAI, on the recommendation of its advisory group of Timothy Gowers, Edward Witten, and other distinguished mathematicians, was a proof of Subhash Khot’s Unique Games Conjecture (UGC), a statement that my wife has worked toward proving for the entire time I’ve known her. (The UGC implies that a whole slew of optimization problems really are NP-hard, even if you just want an approximation that’s slightly better than what you get from semidefinite programming relaxation, which is one of our main tools.)
Or at least, we’re pretty sure that it’s a proof! There’s a Lean certificate, as there are for some of the other 372 breakthrough results (not all of them). But it also appears that no human has understood just about any of these proofs yet; the race to do so has just started. If you want an on-the-ground sense of what that race is going to be like, here’s some of what Dana texted me last night:
It feels like something written by someone who’s on psychedelics. So much unclear and doesn’t make sense. Lots of name dropping of previous work without discussing why it can be used despite impossibility results
Basically the paper is so horribly written that it’s impossible to read it without AI help
I asked Astra for reasonable completeness and soundness claims of the noise gadget and it gave them by combining claims from all over the paper
They also have direct optimal NP hardness of approximation proofs for the main applications of the UGC (Max Cut and all CSP) that bypass the UGC.
The UGC proof invents a completely new bizarre code with a noise test. It’s some crazy recursive construction. [...]

## [28] From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents
arXiv cs.AI | full text via arXiv cs.AI | ~405 words

Computer Science > Cryptography and Security
  [Submitted on 8 Oct 2026]
Title:From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents
View PDF HTML (experimental)
            Abstract:In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised parts of Hugging Face's production environment. Anthropic reported cases in which a misconfigured third-party environment exposed real systems to agents pursuing simulated cyber tasks. In a separately reported evaluation, Google's Gemini accessed three real organizations through an unintended internet route; Google stated that the model stopped in all three instances. Taken together, the cases show why an evaluation cannot rely on an assumed boundary. That boundary must be verified while the agent is operating. This comparative instrumental case study develops a Proactive Agent Security Assurance Cycle (PASAC) and a five-layer Boundary Assurance Stack. The framework combines risk-tiered task design, executable scope contracts, pre-run validation, least-capability access, independent egress enforcement, credential restrictions, cross-run monitoring, automatic stop conditions, and evidence-based reauthorization. A leading-indicator model, nine design propositions, and seven falsifiable hypotheses turn these lessons into a testable research program. Because the public Gemini record is limited to attributed statements and journalism, its detailed causal mechanism remains provisional. The central conclusion is straightforward: proactive agent security requires continuous assurance across the full execution system, not confidence in any single sandbox or safeguard.
    
Additional Features
References & Citations
    
    Loading... [...]

## [155] Google brings agentic AI to Gemini, starting with businesses
TechCrunch | full text via TechCrunch | ~583 words

At a Google Cloud event on Thursday, the company announced it’s bringing its Gemini AI into the agentic age, with the launch of a unified agent that can not only answer questions but also get things done on the user’s behalf, all from a single interface.
The move comes as AI tools have been moving beyond being just conversational experiences to those that can take ownership of assigned tasks, generate code, schedule meetings, book appointments and travel, and more. It also follows the rise of consumer-facing agents like Meta’s Muse and those that operate over messaging, like Instinct and others, as well as the recent debut of ChatGPT’s Dots.
The company still has a good shot at achieving scale for its agentic efforts — as Google CEO Sundar Pichai pointed out at the event’s start, Gemini today has over 1 billion monthly active users. He also noted that nearly 90% of Fortune 100 businesses now use Gemini Enterprise at work.
Given Gemini’s adoption in the corporate world, Google will initially focus on bringing the agent to businesses before later rolling it out to consumers.
According to Pichai, this will allow the company to solve the “harder problems around security, scale, and performance,” which come with launching powerful agents such as these.
Thomas Kurian, CEO of Google Cloud, explained that the new agent can be given “objectives, not just instructions.” That means it’s able to plan the work, use custom skills and tools, and connect to businesses’ internal systems to accomplish its goals.
By default, the AI will pick the best model to complete the task, but users can also take over to choose a model — including those from third parties, starting with Anthropic’s Claude models. Google said that it will expand the model picker to include open source models and other private models in the future.
The request can include attachments, like files, folders, or other projects designed for specific workstreams, like those that combine files and skills. The agent can connect to the business’ data and systems, like Google Workspace, Microsoft 365, Slack, Jira, Confluence, Git, BigQuery, Databricks, Postgres, Snowflake, and others.
It can also connect and work securely with any Model Context Protocol (MCP) server inside or outside the company’s network.
Users can keep track of what Gemini is doing from a “tasks inbox” interface, where they can see Gemini’s thinking process, delegation of tasks to subagents, loading of special skills, code, and progress. [...]

## [13] Roundtables: A Conversation With the Creator of AI-Designed Viruses
MIT Technology Review | full text via MIT Technology Review | ~261 words

Roundtables: A Conversation With the Creator of AI-Designed Viruses
Join a subscriber-only conversation with one of MIT Technology Review's Innovators Under 35.
Available only for MIT Technology Review subscribers.
Friday, October 16, 2026
Can AI design new life forms? In 2025, Stanford University PhD student Samuel King came up with a preliminary answer when he used a generative AI model to propose genetic blueprints for microscopic viruses. It isn’t yet an example of AI-generated life, but that could be next. Join senior AI reporter James O'Donnell as he interviews King about his work, being named one of MIT Technology Review's Innovators Under 35 and new ways of seeing biology.
Going live on October 16th at 18:30 BST / 1:30pm EDT / 10:30am PDT
Speakers: James O'Donnell, AI Reporter, and Samuel King, Bioengineering PhD Candidate, Stanford University/Arc Institute
Related Stories
Deep Dive
Artificial intelligence
Don’t be fooled—LLMs don’t reason
Ten years after AlphaGo’s match against Go champion Lee Sedol, today’s AI still isn’t tapping into the machinery that made that win possible.
AI’s recursive self-improvement might not come so quickly after all
AI agents are not yet creative enough to carry out genuinely innovative open-ended AI research, it seems.
Don’t be fooled by this summer of AI hype
Breathless claims about AGI and new capabilities fall apart pretty quickly under scrutiny.
These startups are chasing the next big thing in LLMs
Meet the new kids nipping at the heels of the AI giants.
Stay connected
Get the latest updates from
MIT Technology Review
Discover special offers, top stories, upcoming events, and more.

## [22] RIP Margaret Hamilton, whose code saved the Apollo 11 Moon landing
Ars Technica | full text via Ars Technica | ~355 words

Margaret Hamilton, who coined the term “software engineering” and led the development of onboard flight software for NASA’s Apollo program in the 1960s, died last week at the age of 90. A recipient of the Presidential Medal of Freedom in 2016, Hamilton was also immortalized as a LEGO minifig the following year—part of the “Women of NASA” set that also included astronauts Mae Jemison and Sally Ride.
“To say Margaret Hamilton was a pioneer—to say she was ahead of her time—would be a dramatic understatement. She was a software engineer at a time when that field was in its infancy, and she not only developed advanced code herself but also led a team in using that nascent technology to develop one of the most complex systems humanity had ever achieved,” said Olivier de Weck, interim head of the MIT Department of Aeronautics and Astronautics. “The Apollo program still stands as one of our greatest testaments to the power of collaboration, ingenuity, and engineering, and Hamilton was a fundamental contributor to that program’s success.”
Born in 1936 in Paoli, Indiana, Hamilton graduated from Earlham College in 1958 with a degree in mathematics and a minor in philosophy—the latter a nod to her father (a poet) and grandfather (a headmaster). She married her first husband, James Cox Hamilton, that same year. The plan was for her to work until he finished his law degree, after which he would support her through graduate school to earn a PhD in mathematics.
She ended up working for Edward Lorenz, the MIT mathematician who set out to construct a mathematical model of the weather using a set of differential equations representing changes in temperature, pressure, wind velocity, and the like. You’ve probably heard the famous story of how Lorenz kept a continuous simulation running on his LGP-30 computer, and of that fateful 1961 day when he realized that even small differences in starting values could lead to very different outcomes—a sensitivity to initial conditions that is a hallmark of chaos theory, along with strange attractors. You might not have known that it was Hamilton who was responsible for programming the LGP-30.

## [48] How Oracle turns days of work into minutes with ChatGPT and Codex
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~18 words

Across recruiting, engineering, and operations, Oracle turns specialist knowledge into fast, repeatable workflows with ChatGPT Work and Codex.

## [157] OpenAI’s math solutions aren’t meeting the field’s standards yet
TechCrunch | full text via TechCrunch | ~747 words

When OpenAI released hundreds of claimed solutions to some of the world’s hardest math problems this week, the frontier lab said that it had consulted an advisory group of elite mathematicians to avoid the controversy that came with the last time one of its models solved a long-standing problem in the field.
But OpenAI fell short of those standards, particularly where the mathematicians emphasized the need for human understanding of a mathematical result. That’s especially concerning after a new paper highlighted gaps between the natural language and formally expressed solution to a million-dollar problem ostensibly solved by OpenAI’s models.
The Advisory Group on Mathematics and Artificial Intelligence (AGMAI), hosted by Princeton University’s Institute for Advanced Studies, is made up of nine prominent researchers at institutions around the world.
The organization released guidelines for frontier labs solving math problems at the end of September. In a statement on the latest set of proofs, the AGMAI said that “it is ultimately up to the mathematical community to assess the extent to which our recommendations were followed successfully.”
However, the organization’s first request was “to stop testing advanced mathematical problems on proprietary models.” OpenAI’s release explicitly says that it is evaluating its proprietary models using open research problems in mathematics.
The advisory group did not respond when asked by TechCrunch for a more thorough evaluation of OpenAI’s latest proof release. The lab clearly followed some of its principles, including releasing results as soon as possible and including information about how the models reached their conclusions. But not for all of them: Just 10 of the 719 manuscripts included releases of the model’s chain of thought.
For papers that people don’t understand, the mathematicians suggested the proofs should be formalized — but just 42% of the proofs released by OpenAI had not undergone this process.
Ultimately, it’s still not clear that OpenAI is taking “responsibility for ensuring that human understanding will follow” when releasing its proofs, in accordance to the AGMAI principles. AGMAI suggested that OpenAI should help fund the work of human mathematicians who will be required to make the lab’s solutions meaningful in any real way. [...]

## [125] Anthropic launches free AI security scans for open-source projects
The Verge | full text via The Verge | ~207 words

Anthropic’s offering to help open-source projects track down security vulnerabilities with a new service called OSS Scanner. It says open-source projects that opt-in will get “thorough, periodic security scans by our strongest models at no cost.” That could mean open-source projects get alerted about possible security issues sooner, but the trade-off is that OSS Scanner’s reports don’t come with human review:
Anthropic launches free AI security scans for open-source projects
The new OSS Scanner service offers vulnerability reports from Anthropic’s “strongest models,” including Mythos.
The outputs of this opt-in vulnerability scanner will be fully model-generated, without human review or triage. This will enable faster and more frequent scanning, but means that it is possible reports will be incorrect or invalid. These reports will be generated by our strongest models (including Claude Mythos) to give open-source projects the largest defensive advantage.
OSS Scanner is far from the first AI bug hunting helper out there. AI tools have helped find some major security flaws in open-source software over recent months, like the “Copy Fail” bug that impacted nearly every Linux distro in May. At the same time, some open-source projects are struggling to keep up with the sudden onslaught of AI-generated bug reports, including Linus Torvalds and even Google.

## [159] GitHub Copilot is going local — but Microsoft won’t say what gets sent to the cloud
The New Stack | full text via The New Stack | ~872 words

GitHub Copilot is going local — but Microsoft won’t say what gets sent to the cloud
GitHub Copilot will soon decide whether coding tasks run locally or get sent to cloud models, with automatic routing expected by the end of October. Microsoft outlined the plan Wednesday in a post co-written by Patrick Nikoletich, a GitHub product manager, and Stuart Schaefer, a Windows platform partner architect.
The announcement coincided with GitHub making its new sandboxing controls generally available, but the protections differ depending on which tools Copilot uses. Shell commands and local MCP servers receive OS-level restrictions, while built-in file tools rely on checks inside the agent harness. Remote MCP servers remain outside the local process sandbox.
Nikoletich and Schaefer acknowledge that “local inference does not make the session offline.” Microsoft hasn’t said how much repository context Auto sends to cloud models, whether developers can inspect routing decisions or whether Auto can be restricted to local inference.
Copilot decides where inference runs
GitHub is expanding Project HydraFusion, which already selects models for coding tasks, to handle where those models run. Microsoft says Copilot will weigh task context and cache state when switching between local and cloud inference, including during multi-turn sessions.
In Copilot CLI, the Copilot app and VS Code, developers can use Auto routing or select a local model themselves. Options include MAI Code 1.1 Flash through the Windows ML provider and OpenAI-compatible local endpoints.
Auto routing raises questions
Microsoft hasn’t said how much conversation history or repository context Auto sends to the cloud when it routes a task. It also hasn’t said whether developers can see those decisions or restrict inference to local models. Teams with strict data-handling policies still don’t know what repository data Copilot sends to the cloud. Similar questions came up last month when Anthropic said it could route Claude Sonnet 5.5 requests to Sonnet 5 when it detects higher-risk activity.
Teams with strict data-handling policies still don’t know what repository data Copilot sends to the cloud.
Selecting a local model keeps inference on the device, but it doesn’t stop the agent from reaching external services or making network requests through its tools. Developers who need a fully local session will also have to lock down what those tools can access. [...]

## [79] Docker Agent (GitHub Repo)
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): HTTP 403) | ~33 words

Docker Agent is a CLI plugin for defining and running AI agents from declarative YAML. It supports multi-agent orchestration, MCP and built-in tools, multiple model providers, retrieval, and packaging agents to OCI registries.

## [178] AI Agents Beat PyTorch: Writing Faster CUDA Kernels
Towards Data Science | full text via Towards Data Science | ~4689 words

AI Agents Beat PyTorch: Writing Faster CUDA Kernels
AI agents can now write CUDA kernels that outperform PyTorch—but proving those speedups are real is the harder problem. I put them to the test on an NVIDIA DGX Spark and found that benchmark design matters just as much as the code.
In February 2025, Sakana AI announced that its “AI CUDA Engineer” generated 17,000 CUDA kernels with speedups of up to 381× over PyTorch. This is a system built to write CUDA kernels, the small programs that tell a computer's graphics chip (the GPU) exactly how to crunch numbers.
Within a day, an X user found the AI hadn’t written faster code—it had exploited a flaw in Sakana’s testing system that allowed incorrect kernels to pass. Sakana retracted the claims and acknowledged a key lesson: if the benchmark is flawed, an AI will optimize for the test, not the problem.
That raises the real question: How do you know a speedup is real?
To find out, I ran my own experiment on an NVIDIA DGX Spark using Claude Code. I asked it to optimize 4 common CUDA operations and evaluated the results with 2 benchmark suites: one rigorous, and one intentionally flawed to see if the AI would take the shortcut.
The results were encouraging. The agents produced correct, high-performance CUDA kernels, with the best implementation running 1.57× faster than torch.compile on a matrix multiplication workload. Three independent agents reached the same solution.
The bigger takeaway wasn’t about CUDA—it was about benchmarking. Building a trustworthy evaluation proved harder than generating the optimized code itself.
1. Who this is for
This article is for anyone considering AI-generated CUDA optimizations. You’ll walk away with:
- A practical framework for deciding when AI-driven kernel optimization is worth your time.
- Real performance results for four common GPU operations using fair benchmarks.
- Five ways CUDA benchmarks can produce misleading results—and how to catch them.
- Whether profiler feedback actually helps AI agents (it didn’t).
2. What a CUDA kernel is, and why "faster than PyTorch" is a trick question
A kernel is a small program that runs directly on the GPU, executed by thousands of threads in parallel — each one handling a small subset of data.
Think of PyTorch as ordering off the menu: its kernels are highly optimized to execute operations one at a time, because in general it doesn’t know what your program will do next. [...]

## [127] You can now play Doom on a SQL database in one of the most astonishing porting projects we've ever seen
TechRadar | full text via TechRadar | ~642 words

You can now play Doom on a SQL database in one of the most astonishing porting projects we've ever seen
A failed grayscale Doom experiment led to a full SQL port
- Vogel ported Doom to run entirely inside a SQL database
- The port draws 640×480 full-color frames from about 1,300 lines of SQL
- Missing BSP-tree traversal in DoomQL prompted Vogel to start a second version
Developer Lukas Vogel has ported Doom to run entirely inside a SQL database, with both the game logic and rendering handled through queries.
The project, called SQLDoom, stores level geometry and game state in CedarDB tables, while a lightweight Python script handles timing, input, and display output.
The result produces 35 full-color frames per second at 640×480 resolution, using roughly 1,300 lines of SQL code divided across 89 query blocks.
An earlier attempt fell short of real Doom
An earlier effort called DoomQL was launched last year and relied on raycasting with grayscale text characters, so it resembled Wolfenstein 3D more than Doom.
The raycasting skipped the BSP-tree traversal that helped distinguish Doom’s rendering approach, prompting Vogel to develop a second version.
For SQLDoom, the developer required both the rendering system and game loop to operate entirely through SQL, with output limited to exact-color tables or bitmaps.
“Rendering Doom in a database is obviously a bad idea,” Vogel said in a blog post about the project.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
Building the new version meant recreating key parts of Doom’s rendering process using database operations rather than conventional game-engine code.
Handling the level geometry was relatively straightforward because a sort key calculated when each map loads lets a single ordering clause determine which wall sections are drawn.
Floors and ceilings presented a tougher problem. Doom’s original engine uses visplanes and state changes, neither of which translates neatly to column-by-column SQL rendering.
Vogel replaced that system with what he called a “pretty hacky” approach, looping through a sequence of sorted panels to fill those surfaces.
Speed figures and server tests give mixed results
Vogel reports about 60 fps on a laptop with a Ryzen 7 7840U chip, though busy scenes can fall to 35 fps.
He said table overhead was substantial, yet the port still ran faster than his simpler DoomQL effort from last year. [...]

## [142] Microsoft’s new Windows Search is exactly what Windows 11 needs
The Verge | full text via The Verge | ~461 words

Windows Search has been one of the most frustrating parts of Windows 11, and now Microsoft is addressing this with a significant overhaul. A new redesigned Windows Search is now in testing that is much faster, more capable, and a lot more modern.
Microsoft’s new Windows Search is exactly what Windows 11 needs
Windows Search is being overhauled with a focus on speed and capability.
“This new Windows Search experience is built for speed,” says Anshul Rawat, corporate vice president of the Windows product team at Microsoft. “It’s built on WinUI 3 and is part of our broader investment in modernizing our core Windows experiences.”
Microsoft says early testing of this new search has shown “substantial improvements in performance and memory usage,” meaning the company isn’t adding extra bloat to Windows to improve search, either. The UI has also been greatly improved, with speedy animations and a large preview pane.
While search is being overhauled visually, behind the scenes Microsoft is also improving the basics. “We’re also improving how Windows Search understands what you’re looking for, including better matching for typos and synonyms,” says Rawat.
I got to try out this new Windows Search interface at Microsoft’s Windows and Surface event yesterday, and I was impressed with just how quick it is and how decluttered it feels. Right now if you search for something like the height of an actor it will take a few seconds to figure it out and show you essentially a miniature Bing result.
The new Windows Search just surfaces the result inline, much like the modern search interfaces you see in iOS and Android. These inline results also extend to previews of PowerPoint presentations, photos, and other files.
The most impressive part of this new Windows Search is being able to use it like a launcher, just like many third-party tools, and have it take actions for tasks like turning Bluetooth or dark mode on and off. You can even ask search to minimize windows, or open apps side-by-side. If you use Phone Link, these actions will also extend to your phone so you could simply type “text mom, I’m running late” and it will send a text message from your phone.
Microsoft is testing this new Windows Search interface with its Windows Insiders right now, so that should mean we’ll see it appear in Windows 11 in the coming months. [...]

## [189] Google's Sashiko AI Has Completed 191k Patch Reviews, Cited On Nearly 500 Kernel CVEs
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~48 words

Sashiko that was built by Google engineers for agentic review of the Linux kernel code changes and powered by Google's AI models continues proving very valuable to kernel developers. In less than one year since they launched Sashiko for agentic AI code review, their results are quite fascinating...

## [23] Let's Encrypt cuts certificate lifetimes to 64 days starting February 2027
Ars Technica | full text via Ars Technica | ~275 words

Let’s Encrypt is continuing a push toward tighter security by reducing free SSL/TLS certificate lifetimes from 90 days to 64 days, starting February 10, 2027. For administrators already implementing modern ACME clients that support ARI (ACME Renewal Information), the change should be seamless. For those still relying on hardcoded renewal schedules or manual processes, February will be the deadline to update before certificates start expiring unexpectedly.
Starting on October 14, Let’s Encrypt will begin testing the 64-day certificates, and interested users can opt in to test their setups before production goes live.
Prior to Let’s Encrypt’s launch in early 2016, certificates were often issued for as long as one to three years. The service started with 90-day certificates to force renewal automation that didn’t previously exist. Shorter certificate validity periods limited vulnerabilities from private key thefts and encouraged accelerated HTTPS adoption across the web.
This move shook industry norms at the time, but by limiting the certificate lifetime, the certs are less likely to cause damage if compromised or assigned in error. The move down to 64 days continues this logic, and the lifespans will only continue to get shorter as time goes on, with 45-day defaults planned to follow in 2028.
Just as the initial rollout of Let’s Encrypt aimed to push users toward HTTPS, the shortened certificate windows are aimed at moving users to full ACME automation. The ACME protocol, and, more specifically, ARI (ACME Renewal Information), allows the certificate authority to tell the client when it’s time to renew. Although ARI does this, many deployments are still stuck on scripted update intervals that trigger at fixed offsets like “60 days before expiration.”

## [1] Whistle: Speech to Text in 16.9 MB
Hacker News | full text via Hacker News | ~961 words

Today we release Whistle, a speech recognition model for mobiles, wearables, robots, smart home, automotive and microcontrollers. It is one 16.9 MB file, runs on the CPU with no dependencies, and loads into the same C++ engine as Needle, from the same container and the same quantisation.
Whistle does three jobs, all of them on the device:
- Transcription. 16 kHz mono audio, up to 30 seconds in one pass, in English, German, French, Spanish, Italian, Dutch and Polish. The language is detected unless you name it.
- Word timestamps. Every word with its start, end and probability, aligned from the decoder's attention.
- Speech embedding. The encoder output, one row per 80 ms frame, without decoding a transcript.
The model
The front end. 16 kHz mono audio is framed at a 25 ms window and a 10 ms hop into 80 log-mel bins, band-limited to 250-3500 Hz and normalised per channel. Thirty seconds is 3,000 frames. A convolutional stem of 128 channels and kernel 9 halves that count three times, leaving 375 frames at one per 80 ms. Every stage after this runs at that rate, and embed returns one row per frame.
The encoder. Eight Simple Attention blocks: four mHC residual lanes and a Monarch Hadamard MLP in place of the feed-forward network, the same blocks Needle uses. The attention is not causal. A frame at 3 s attends to a frame at 12 s.
The decoder. Eight Laddered Simple Attention blocks at width 512, 8 query heads to 2 KV heads, 48-dimensional queries and keys, 64-dimensional values, a 3-tap causal convolution on Q, K and V, and engram lookups at layers 3 and 7 over 18,432 slots. That is Needle's block list with a different layer count.
The speech-specific part is one addition per layer. Each decoder layer reads the encoder through a gated cross attention, x ← x + σ(g) · softmax(q̂ K̂ᵀ/√d) V, with a gate learned per layer and K and V taken from the clip. Those projections run once when the clip arrives, 375 frames across 8 layers, and are then held for the whole decode. Five beams therefore cost five short transcript caches, not five passes over the audio.
Decoding. Five beams scored by length-normalised log probability. Keyword biasing walks an Aho-Corasick automaton over the phrases you pass in, alongside the beams, and lifts their log probability as the automaton advances. The transcript is capped at 320 tokens. [...]

## [136] Fired OpenAI safety researchers dispute misconduct claims, warn of chilling effect
TechCrunch | full text via TechCrunch | ~964 words

Jasmine Wang, Tomek Korbak, and Mikita Balesni, the three safety researchers that OpenAI fired last week, have published an open letter denying the firm’s claims that they mishandled sensitive information outside of established company procedures and warned that their dismissal signals a chilling effect that will have ripple effects across the company’s culture.
“We have become concerned that internal and external communications around our firing have made our former colleagues afraid to speak and operate in ways that, until last week, were an integral part of working at OpenAI,” the researchers wrote Thursday in an open letter to OpenAI’s Safety and Security Committee, Safety Advisory Group, and Mission Advisory Council.
The researchers were dismissed last week after allegedly sharing confidential company information with a third-party AI safety organization. OpenAI said they violated the company’s policies by “accessing and handling sensitive company information.”
“AI is not a normal technology, and OpenAI is not a normal company,” Wang, Korbak, and Balesni wrote. “Those of us who work on safety see risks before anyone else, and we rely on close collaboration with outside experts to work out how to address them. The freedom to do so without fear, and to have well-defined internal procedures that enable this work, is itself an essential safety mechanism.”
They said that their firing represents a broader shift in the culture of OpenAI, one that used to encourage workers to “raise safety concerns and disagree openly.” They said employees are now “unclear on where they stand” when behavior that was allegedly normal a month ago is now suddenly grounds for dismissal.
“Given the significant safety concerns surrounding the development of AI, employees must not be left working in an environment where fear and unclear rules stymie AI safety work and weaken third-party accountability,” they wrote. “Terminations such as ours, executed and communicated so abruptly, are chilling the open culture OpenAI has prized in the past.”
In the letter, the three denied involvement in a leak to The Information about less monitorable architectures in OpenAI’s newest models that make chain-of-thought reasoning more difficult to monitor. They also denied engaging with external parties outside the mandates of their jobs. [...]

## [128] Harness bought Augment’s coding agents. The best feature hasn’t shipped yet.
The New Stack | full text via The New Stack | ~665 words

Harness bought Augment’s coding agents. The best feature hasn’t shipped yet.
Harness announced Thursday that it acquired Augment Code’s Cosmos software factory, Auggie CLI and Code Context Engine, along with the team behind them, for an undisclosed amount. The deal adds autonomous coding agents to Harness’s existing software delivery platform, which already handles testing and deployment.
According to Harness, Cosmos will become the Harness Cosmos Software Factory Agent, with plans to connect Augment’s codebase understanding to Harness’s delivery history. The integration would allow coding agents to use previous deployment failures when making changes and receive feedback from downstream systems when those changes fail validation. Cosmos is available today, but those capabilities have not shipped.
“AI’s impact on software will not be measured by how much code it generates, but by how much valuable software reaches customers.”
“AI’s impact on software will not be measured by how much code it generates, but by how much valuable software reaches customers,” said Harness founder and CEO Jyoti Bansal. The acquisition follows the company’s research into the AI velocity paradox, which found that faster code generation was putting additional strain on testing and release processes that had not kept pace.
Inside the Cosmos factory
Cosmos takes a requirement or bug report through to a pull request, with agents writing and testing code inside isolated VMs. They can also pick up failed checks and review comments on an existing PR, using feedback from earlier rounds to make further changes.
Teams can fork and customize agents for their own workflows, while Augment’s Code Context Engine retrieves relevant codebase context as they work.
“We set out to bring AI to the entire software development lifecycle, starting with context-aware coding,” said Igor Ostrovsky, Augment Code’s co-founder and CTO, describing engineering work that becomes increasingly autonomous “with engineers stepping in only where judgment really matters.”
“We set out to bring AI to the entire software development lifecycle, starting with context-aware coding, with engineers stepping in only where judgment really matters.”
Where humans still approve
Developers still approve and merge changes, although Bansal wrote that teams can decide which work agents handle on their own and where a person has to review or approve it. [...]

## [166] Ubuntu Currently Suffering From Sustained DDoS Attack
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~31 words

Those trying to access the Ubuntu website, ISO downloads, and similar Ubuntu resources today are finding the site inoperable amid what's now confirmed as an ongoing distributed denial of service attack...

## [70] Zuckerberg's Biohub Partners With DOE, NIH to Invest $1.8 Billion in Biological Data for AI Models
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 401) | ~95 words

Biohub, a nonprofit co-founded by Mark Zuckerberg, is working with the Department of Energy, the National Institutes of Health, and other funding partners to invest $1.8 billion in building biological data ready for AI models. The investment is aimed at providing data sets that allow researchers to use AI models to find new ways of preventing and treating diseases. The DOE will invest more than $500 million across five years in lab measurement, modeling, and computation to build an AI-ready open data resource; the NIH will coordinate the contribution of relevant datasets, repositories, and kno

## [9] In Vienna and Beijing, the First Nuclear Clocks Begin to Tick
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403; Slashdot: HTTP 403) | ~83 words

Two independent teams in Vienna and Beijing have simultaneously built the first clocks that keep time by counting the squishing and unsquishing of the atomic nuclei of thorium. The clocks are so precise that they only lose one second once every few million years or so. Nuclear clocks have the ability to search for certain kinds of dark matter. If a particle of dark matter passes through the thorium nuclei, it could register as a wobble in the nuclear clock's otherwise steady tick-tock.

## [3] I gave Opus 5.5 one prompt and six hours to visualize Invisible Cities
Hacker News | full text via Hacker News | ~596 words

GPT-6 Astra was a jump when it comes to puzzles. Claude Opus 5.5 is a jump when it comes to design.
Vibe designing
Even local models can make a competent landing page for a shop. Doing interactive visualization is a different tier. Since I am into creating data visualizations and explorable explanations, LLMs were both a blessing and a curse.
Then for a moment I was happy-ish with GPT-6 Astra. My subjective experience was that it is a bit better than Fable 5.1 at a general overview, following intentions behind prompts, and checking that it all works correctly.
Then there was the Opus 5.5 moment for AI-assisted design. I saw an optical explorable explanation:
One may argue that it is still “too rich”, and has no sense of minimalism. But still, wow! I was still in disbelief. Was this really its consistent quality for a one-shot experiment?
Instead of my beloved optics, I went for something different.
Invisible Cities
What’s a good prompt? Well, I went with the beautiful urbanistic poetry of Invisible Cities by Italo Calvino, presenting 55 imaginative cities, each one an emotion or state of mind, expressed in its architecture and in how people behave.
When a man rides a long time through wild regions he feels the desire for a city. Finally he comes to Isidora, a city where the buildings have spiral staircases encrusted with spiral seashells, where perfect telescopes and violins are made, where the foreigner hesitating between two women always encounters a third, where cockfights degenerate into bloody brawls among the bettors.
In 2019, I had a small project of generating cities for a storytelling performance, using the frontier model of the time, GPT-2. With new models, capabilities change drastically. So I used the following prompt:
Make a three.js (pnpm) visualization of all Invisible Cities by Italo Calvino. Don’t ask questions, it is a one-shot task. You have 6h of work, use it until it becomes a masterpiece.
GPT-6 Astra in Codex
I gave this prompt to GPT-6 Astra… and it worked, end-to-end.
Some AI design slop, with many concepts and comments added, without checking whether they are actually needed, or just add visual noise. Some Captain Obvious statements that would work for accessibility, but not as something to be shown verbatim.
Curiously, it seemed to pick up the Claude visualization style: beige background, numbers like 05.
Still, I wouldn’t have expected earlier models to get anywhere near this. [...]

## [18] Trump Mobile hack and apparent lack of FCC authorization raise security alarms
Ars Technica | full text via Ars Technica | ~317 words

Trump Mobile apparently failed to obtain necessary authorizations to operate the international calling portion of its phone service, Sen. Maggie Hassan (D-N.H.) wrote in a letter to the company today.
Her letter said Trump Mobile also doesn’t appear to have submitted a required plan for fighting robocalls. Trump Mobile’s key business partner, Liberty Mobile Wireless, did make a robocall database filing, but it was not complete, Hassan said.
Hassan’s letter raised questions about Trump Mobile’s security related to a report that hackers stole personal data of 3,615 customers and Trump Mobile’s previous confirmation that a vendor it uses exposed customers’ personal data on the Internet. Hassan alleged that Trump Mobile failed to follow multiple FCC filing rules that are supposed to help ensure the security of mobile services.
“The apparent absence of authorization for Trump Mobile international services raises questions about who is providing or reselling the international telecommunications services advertised by Trump Mobile, the authority under which those services are being provided, and the company’s commitment to complying with requirements designed to safeguard national security,” Hassan told Trump Mobile CEO Patrick O’Brien.
Referring to the recent data breach, Hassan said it’s worrisome that a ransomware group “claimed that when it notified Trump Mobile of the breach, the company responded that ‘[w]e have no team to handle this.’” Trump Mobile also seems to lack a robust customer authentication process and offers “streamlined service activation that can make it easier for scammers to obtain US numbers,” Hassan wrote.
Trump Mobile, which has a trademark and name licensing deal with the Trump family, advertises that its customers can call more than 230 countries and territories. “Yet a search of the FCC’s International Communications Filing System suggests that Trump Mobile does not hold the necessary authorization for these services under Section 214 of the Communications Act of 1934,” wrote Hassan, the top Democrat on the US Congress Joint Economic Committee.

## [77] JPEG XL Finally Lands in Chrome!
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~550 words

JPEG XL finally lands in Chrome!
Version 155 of the popular web browser will ship with a JPEG XL decoder
Today, I was browsing Hacker News, when a particular item caught my eye:
I opened it promptly and, indeed, it was not a prank. Finally, after years and years of bull**** from the Chrome team, they are shipping it. They are shipping a JPEG XL decoder.
For those of you who don’t know, JPEG XL is a new image codec that includes most of, if not all, the features we’d want in the image codec of the future:
- File size reduction by \(~20-60\%\) w.r.t JPEG.
- Lossless JPEG transcoding.
- Progressive decoding.
- Wide gamut, HDR and 32-bit support.
- Animations and transparency (alpha channel).
- Shines with high-fidelity photographic images.
- Fast-ish encoding and decoding.
- Royalty-free and FOSS.
- Support for super high-resolution images, of up to 1 terapixels ( \(2^{30}-1\) pixels per side).
This is awesome news for the codec. Whether we like it or not, Chrome is the dominant web browser, with ~66.5% of the market share, very far from its competitors (Safari, Edge, and Firefox, in that order).
Now, I don’t use Chrome at all, but I still think that this was just the final piece of the puzzle needed to help the format go mainstream.
So, what finally pushed them over the edge? If you read their announcement, they cite “consistent feedback and requests from web developers” and its massive popularity in the Interop 2026 project. Translated from corporate PR-speak: the community simply refused to let it go. Web developers, photographers, and open-source advocates kept pushing, complaining on bug trackers, and demanding a truly superior image format instead of settling for Google’s own WebP or the heavily pushed AVIF.
The technical excuse the Chrome team used for years was that a C++ decoder was too much of an attack surface to run safely in the browser. Well, it has now been elegantly sidestepped. To bring JPEG XL to Chrome 155, they have integrated jxl-rs, a pure Rust reimplementation of the decoder. This tackles the memory safety issues head-on, eliminating the risk of out-of-bounds reads and use-after-free bugs of other decoders. And to make sure it doesn’t run sluggishly, they built a SIMD abstraction layer (jxl_simd) to maximize hardware performance without compromising Rust’s safety guarantees.
This is a massive victory. Not just for JPEG XL, but for the open web. [...]

## [14] ttok 0.4
Simon Willison's Blog | full text via Simon Willison's Blog | ~100 words

8th October 2026
ttok is my CLI tool for counting tokens, using OpenAI's open source tiktoken library.
It hasn't been in updated in a couple of years, but I finally fixed a Click warning, updated CI, and added a --list-models command to list available models.
It works with uvx, so you can count tokens in anything like this:
cat file.txt | uvx ttok
Recent articles
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026

## [121] ICE Emails Discuss Using Palantir-Supported Tool to Investigate Voter Fraud
Wired | full text via Wired | ~831 words

As the Trump administration has carried out a nonstop effort to undermine the midterm elections this year, the Department of Homeland Security appears to have looked into whether it could use a Palantir-supported tool to track people it believes have voted illegally.
The revelation is found in a tranche of documents obtained through a Freedom of Information Act request and published this week by Democracy Forward, a legal advocacy group. As well as revealing that DHS officials have investigated over 150 nonprofit groups in search of evidence they’re helping noncitizens register to vote, the documents show how Immigration and Customs Enforcement is now central to federal voter fraud investigations.
More specifically, Homeland Security Investigations (HSI)—one of ICE’s two major components—is spearheading the effort to uncover voter fraud, with its Innovation Lab (known internally as iLab) developing tools for agents.
ICE, it seems, wants to build “a system that is going to get good at determining how to find people to investigate and potentially bring action against,” Chinmayi Sharma, an associate professor at Fordham Law School who has closely tracked the Palantir-supported tool called ELITE, tells WIRED.
“You would want to build off of what already exists, what might already have the infrastructure and data sources that you would want,” says Sharma.
“iLab’s processing focuses on DOJ voting rolls and [US Citizenship and Immigration Services] data; criminal histories are currently excluded, with efforts underway to address this,” a worker in HSI’s Countering Transnational Organized Crime unit wrote on May 26 in an email with “Voter Fraud” in the subject line. (Like other workers, their name was redacted in the records released to Democracy Forward.)
“Coordination with iLab continues,” they wrote, “particularly on ingesting processed voter roll data into the ELITE enforcement system to enhance lead management, analytical review, and investigative tracking.”
The existence of ELITE, which stands for Enhanced Leads Identification & Targeting for Enforcement, was first reported in January by 404 Media, which revealed that ICE agents using the tool can create maps featuring potential deportation targets, pull up files on each target, and see a “confidence score” on the person’s current address.
“Voter roll data has never been integrated into ELITE,” a Palantir spokesman tells WIRED. [...]

## [11] Anti-Patterns in Software Blogging
Simon Willison's Blog | full text via Simon Willison's Blog | ~207 words

7th October 2026 - Link Blog
Anti-Patterns in Software Blogging (via) Some excellent writing advice from Michael Lynch. Michael warns against "meandering intros", misjudging your reader's existing knowledge, assuming they'll read your previous posts, and excessive formality.
He also warns against overreliance on links as an excuse not to explain terminology. This one hurt! I do this all the time, but I have a nagging suspicion that almost nobody ever clicks on them.
(In a Lobste.rs comment Michael clarifies that "My rule of thumb is that my article should still make sense to the reader even if they don't click any links". That works for me.)
This point about using your own voice is crucial:
Beginner software bloggers suffer from a mass delusion that you have to write in a stiff, overly formal way for people to take you seriously [...]
Just write the way you talk.
With so many developers delegating their writing to AI, software blogging is becoming bland and homogenous. Readers are hungry for writing with personality.
Recent articles
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026

## [49] The Missing Piece in Rust Error Handling
Lobsters | full text via Lobsters | ~1552 words

Rust already has most of what I want from error handling: explicit control flow, errors as values, and concise propagation with ?. The friction comes when deciding what to put in the error half of Result. We often end up choosing between precise types that require boilerplate and convenient types that hide which errors can occur. But precision and convenience do not have to be competing goals. Error types should compose as easily as the functions that return them.
The Problem With Rust Error Handling
Consider reading a server port from a file. Reading can fail with an io::Error, and parsing can fail with a ParseIntError. A conventional implementation might look like this:
use std::{io, num::ParseIntError};
#[derive(Debug, thiserror::Error)]
pub enum PortError {
    #[error(transparent)]
    Io(#[from] io::Error),
    #[error(transparent)]
    Parse(#[from] ParseIntError),
}
fn load_port(path: &str) -> Result<u16, PortError> {
    let contents = std::fs::read_to_string(path)?;
    Ok(contents.trim().parse()?)
}
thiserror removes the manual Display, Error, and From implementations. But we still have to decide how this enum relates to every other error enum in our program.
Now load a host address, bind a socket, and initialize a database. Each operation has its own errors. We can wrap those enums in another enum, flatten their variants into a new enum, or give everything one large crate-wide error type. The first approach creates nesting, the second creates conversions, and the third means functions advertise errors they cannot actually return. An I/O error may also end up in several different nested variants, making handling it at a higher level unnecessarily awkward.
Alternatively, an anyhow like approach makes propagation and attaching context straightforward. We can downcast when we need to inspect a concrete error. However, the function signature no longer tells us which error types are possible, and the compiler cannot track whether we have handled all of them.
The usual advice is to use typed errors in libraries and opaque errors in applications. But applications need typed recovery too, and libraries often contain internal operations whose callers only need to propagate a failure. The useful distinction is whether a caller needs to do something different based on the error type.
Error Types Should Compose
What we actually want to say is simple: this function can fail with an io::Error or a ParseIntError. [...]

## [51] Ending the Casuarina Linux Experiment
Lobsters | full text via Lobsters | ~824 words

by Wesley Moore
I didn’t expect this to be the second post after the announcement, but here we are. The short version is that I’ve decided to wind down the Casuarina Linux project. Things will continue as-is until the end of October 2026. After which, depending how my migration to another distro has gone, package updates will stop. The infrastructure will remain up until the end of 2026, after which I may retire some things. There are no plans to retire the package repo or website for now.
As alluded to in the Q&A I am the proverbial dog that has no idea what I’m doing. I thought that after I fought through all the changes to bootstrap the system most of the hard stuff was done, and that from then on maintenance would mostly be updating packages. I also expected that the distro would pique the interest of at least a couple of other people and we could share the load of keeping things moving, but that didn’t happen.
In practice what happened was that on launch day it was brought to my attention that C++ standard
libraries can’t co-exist. My setup of building everything against LLVM’s libc++, whilst providing
GNU libstdc++ for compatibility was not guaranteed to work properly if an application ended up
loading both. In practice the one proprietary application I used that was exposed to this
(Beyond Compare) worked fine. Still it was something that needed fixing.
Additionally, on the same day q66 (the creator of Chimera Linux) posted some thoughts “about chimera and glibc compatibility woes”. It was insightful and full of wisdom. There were two parts that really stuck with me:
OR, you can just accept things as they are and help work towards making the stuff you want work
in userland, you have containers etc which you can use to get stuff that doesn’t work yet to work (or for proprietary software), and there are ways to make that pretty seamless
i’d much rather like to see the work go into improving what we have
and:
but i can’t be totally happy about it because it’s sort of taking apart stuff i put a lot of thought into and in the process turns it into something i explicitly wanted to avoid
The latter in particular was not a way I’d thought about it from their perspective before. It
made a lot of sense when faced with having to swap libc++ for libstdc++, and when
reflecting on the changes that were necessary to bootstrap the system. Such as bringing gcc,
gmp, mpc, mpfr, and GNU binutils into the bootstrap path (in addition to LLVM). [...]
