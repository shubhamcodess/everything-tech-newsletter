# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Cloudflare acquires Deno
Hacker News | full text via Hacker News | ~536 words

Deno is joining Cloudflare
For years, we’ve been working to make building server software simpler. We questioned how modules could be distributed, what security guarantees a JavaScript runtime could provide, what belonged in a complete toolchain, and how easily an application could be distributed as a standalone executable. Compatibility with Node.js became an important part of that work too: our users wanted the Deno improvements while continuing to plug into the existing JS ecosystem. The team and community built a runtime that brought these capabilities together and challenged assumptions about what JS development could look like.
Today we’re announcing that the entire Deno team is joining Cloudflare to take that work further.
Our ambition has always extended beyond the runtime. I wrote about this in my JavaScript Containers blog post: compute, storage, and communication working together, without every application assembling its own infrastructure.
With Deno Deploy, we took another step towards that goal. We wanted to make running applications as straightforward as possible. But building and operating Deploy also showed us how much complexity remained underneath that developer experience. I wanted to simplify that layer, too.
This led to celld. Building on the Cloudflare Workers programming model, celld lets developers build distributed applications from the start while making the system simple to operate. What excites me greatly is that the scaling is built into the programming model, rather than infrastructure each app has to assemble itself.
The progression from Deno to Deno Deploy to celld explains why this move makes sense to us. At Cloudflare we’ll combine our work with that of the Workers and Durable Objects teams. We want to make this programming model the default way to build servers, whether you run on Cloudflare’s network or your own infrastructure.
Joining also means choosing where to focus our effort. We’ve decided to put our future development work into this shared platform rather than continuing to develop a separate runtime and hosting service. We know this is a consequential change for people who have built on Deno.
To everyone who contributed code, built businesses on Deno, reported problems, and trusted our direction: thank you. Here’s what this means concretely:
- We will support the Deno runtime for another year with monthly releases containing bug fixes and security updates. [...]

## [112] An Anthropic AI model sent a false homicide tip to Philadelphia police
TechCrunch | full text via TechCrunch | ~374 words

An Anthropic AI model submitted a false tip about an unsolved murder to the Philadelphia police.
The AI reportedly submitted this incorrect information to a public Philadelphia Police Department (PPD) tip line on July 18, but Anthropic didn’t discover the behavior until September 28. The police had not seen the tip because it was marked as spam.
Anthropic notified the PPD about the incident on Wednesday and met with the department the following day.
“The company must strengthen its safeguards to prevent similar incidents from impacting city systems without the city’s knowledge. The two-month delay in detecting and reporting the incident to the City is unacceptable,” the PPD said in a statement to 6abc.
Anthropic did not immediately respond to a request for comment, but the PPD elaborated on the incident in an emailed press release shared with TechCrunch.
“According to Anthropic, its model was conducting a test involving interactions with randomly selected websites when it accessed PhillyUnsolvedMurders.com and submitted false information concerning an unsolved homicide. The submission, dated July 18, 2026, at 11:27 p.m., purported to come from someone who might have information about the case,” the PPD said.
As autonomous AI agents are increasingly made available to consumers, this incident highlights the danger of giving AI the ability to carry out tasks without any human supervision.
Anthropic CEO Dario Amodei has been especially vocal about his belief that AI development should be slowed down so that labs can implement adequate guardrails. Perhaps this stance was informed, in part, by witnessing his company’s tools submit false homicide tips.
These issues are not exclusive to Anthropic. OpenAI recently revealed that one of its models acted unexpectedly during a test and hacked the AI dataset platform Hugging Face, exposing critical vulnerabilities in its software. As AI models continue to be granted unchecked access to people’s computers and login credentials, this problem is expected to persist.
“Unsolved cases involve real victims, grieving families and investigators working to secure answers,” the PPD added. “Technology companies must take all appropriate steps necessary to prevent their systems from submitting false information to law enforcement.”
The PPD said that Anthropic plans to publish a report with more information about the incident and other instances of unintended model behavior on Friday.

## [129] Anthropic can’t reliably control its AI agents. It’s cutting off its internal evals from the live internet instead
TechCrunch | full text via TechCrunch | ~553 words

Anthropic said its models exploited websites on the internet, including some run by U.S. government agencies, and it will turn off live internet access for all of its internal evaluations until the frontier lab is sure it can monitor and control its AI agents.
The incidents, disclosed in a blog post, involved AI agents tasked to solve problems seeking resources on the internet. In the process, they exploited software flaws, accessed databases without paying fees, used URL shortening services to smuggle information pass restrictions, and even submitted a false murder tip to the Philadelphia police.
Anthropic said it discovered these new issues in a review of its model’s activities that began in July, demonstrating the lab’s lack of awareness of its software’s behavior in real time.
Notably, the company said that alignment training was not yet sufficient for skills like search and computer use that are central to its pitch that AI agents will be used by any professional who relies on digital tools.
The behaviors Anthropic disclosed are similar to incidents involving OpenAI agents that collaborated to break into various websites in search of information, including some run by the Australian government.
Anthropic previously disclosed that its models had broken into external systems. The frontier lab said it considered today’s disclosures “significantly less severe from an alignment and security perspective” than those it announced before.
However, the lab still said it had “turned off live internet access” for “all our internal evaluations” until it is certain it can monitor and control its agents.
It’s not clear what that means. Sydney Von Arx, the founder of Nightingale, an AI safety organization, told TechCrunch in an interview before this disclosure that developing models on a data center cut off from the open internet would be very challenging for researchers, and hinder the progress of the models, which benefit from internet access.
“You have to align them at some point,” Von Arx said. “If the AIs are released to production and never have access to the internet, that’s not a very useful tool.”
Anthropic said the behavior was a result of flaws in the lab’s training environments, which led the models to believe they would be rewarded for finding loopholes or avoiding restrictions, a behavior called “reward hacking.”
The company said it would stop running some of its evaluations or move them offline, and has built tooling to detect and block this behavior. [...]

## [81] A Single POST Freezes Any Next.js Server
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1034 words

A Single POST Freezes Any Next.js Server
To rebuild one submitted form, React scanned every field in the request once for each reference it contained. Nothing capped either number, so one 900 KB POST makes the server do 100 million checks and freeze.
How I Found It
Modern React lets you wire a form straight to a function that runs on your server, a “server action.” The user submits the form, the function runs on the backend. Before it can run, React has to take the raw HTTP request and rebuild your form data out of it. That rebuilding code runs on every single server-action call, and it works entirely on data the sender controls. Exactly the kind of code worth reading.
React’s format lets one field in the form point at another. One of those pointers, which React writes as $K, means “there’s a nested form in here.” This is the code that resolves a single $K:
case 'K': {
  const data = new FormData();
  const keys = Array.from(response._formData.keys()); // list every field in the request
  for (let i = 0; i < keys.length; i++) {             // then check all of them
    if (keys[i].startsWith(formPrefix)) { /* ... */ }
  }
  return data;
}
In plain terms: for each $K pointer, React walks the entire list of fields in the request looking for matches. So one pointer costs one full pass over every field.
Here’s the catch. Nothing limits how many $K pointers a request can contain, and nothing limits how many fields it can contain. The sender picks both. Put 10,000 pointers and 10,000 fields in one request, and React makes 10,000 passes over 10,000 fields. That’s 100 million string checks, and it runs them all back to back without ever pausing.
The “without pausing” part is what turns it into a server killer. Node.js handles every incoming request on a single thread. While it’s grinding through those 100 million checks, it can’t do anything else. Every other visitor just waits for it to finish.
The Caps That Don’t Help
React does have two size limits right next to this code, but neither one covers it. The first only limits how deeply arrays can nest. The second limits how many arguments an action call can take, which sounds like it should stop me, except you get around it by burying the giant list of pointers one level deeper than the limit bothers to look:
level 1 (counted):      ["$2"]
level 2 (not counted):  ["$Knomatch0", … ,"$Knomatch9999"]
The limit sees the one item on the top level and never notices the 10,000 hiding underneath. [...]

## [37] Github Migrates Copilot Runtime to Rust with AI-Assisted Rewrite
InfoQ | full text via InfoQ | ~460 words

GitHub has migrated the runtime behind GitHub Copilot CLI, the Copilot app, and Copilot SDK from TypeScript and Node.js to Rust, replacing more than 800,000 lines of production code through an AI-assisted rewrite. The migration took approximately 14.5 weeks and was delivered through 128 pull requests while GitHub continued releasing the runtime. GitHub reports that a measured client startup, session creation, and single-turn scenario fell from 5.25 seconds with the previous runtime to 292 milliseconds when the Rust runtime was embedded in process.
The migration also changed how applications integrate with the runtime. The previous implementation required Node.js and V8 and communicated with host applications across a process boundary. GitHub says this added approximately 100 MB of working set per client. The Rust implementation can instead be embedded directly into host applications through a C ABI, while an out-of-process mode remains available. The Copilot SDK currently supports TypeScript, Python, Go, .NET, Java, and Rust.
GitHub’s before and after Copilot runtime architecture (Source: GitHub Blog Post)
GitHub used an incremental replacement strategy rather than a parallel rewrite followed by a single cutover. Individual TypeScript components were replaced with Rust implementations, with temporary N API interoperability connecting the two. This allowed existing end-to-end tests to exercise the new code while other components remained in TypeScript. GitHub shipped 135 releases during the migration, including 35 stable and 100 prerelease versions.
The compatibility layer reached 2,019 internal N API exports and 3,356 TypeScript call sites before being removed. By August 21, the runtime contained 832,378 lines of production Rust and 468,689 lines of Rust unit tests. AI agents generated most of the implementation, while compilation, testing, and human review helped identify regressions involving behavior, state and lifetime handling, library semantics, and lost optimizations. GitHub recorded 4,478 direct cargo check runs, with 87.1% completing cleanly.
Community responses also focused on the verification challenges of AI-assisted migrations and pointed to cancellation, retries, and backpressure as examples requiring validation beyond compilation. PLBjt wrote that
The interesting part here is less that Copilot wrote Rust and more whether the migration kept the runtime’s behavior stable at the boundaries. [...]

## [65] The State of AI Report 2026
TLDR Tech | full text via TLDR Tech | ~2739 words

After months of research and revisions right up to the last minute, I’m thrilled to bring you the 9th annual State of AI Report.
For nearly a decade, this report has been a labor of love. My interest in AI began with my PhD in cancer research and computational biology in the early 2010s. Since 2013, I’ve invested in companies building and applying AI to accelerate technological progress. The report is my way of sharing what I’m learning and helping more people understand the research shaping our world.
Every day brings new papers, model releases, and developments in industry and politics. Much of the work goes into deciding what deserves your attention, checking what the evidence supports, debating it with researchers and builders, and explaining why it matters.
We also make predictions each year and return to grade them. Past calls include NVIDIA failing to acquire Arm, transformers achieving leading results beyond language, and an open-source model surpassing OpenAI’s o1, which DeepSeek-R1 subsequently did.
If you’d like to follow these developments throughout the year, subscribe to Air Street Press for my monthly State of AI newsletter and regular essays.
Let’s dive into the key stories
This year, agents are doing valuable work in software and science, physical AI is learning how to act in the world, and access and control are becoming more consequential. Below, I share the developments that stood out to me and what I think they mean for where AI goes next.
The frontier is now a three-lab race between Anthropic, OpenAI, and Google. Anthropic leads on Artificial Analysis’s Intelligence Index, while Google leads on Arena’s ranking of the answers people prefer, for now.
Last year, we described reasoning becoming useful at scale with OpenAI’s o-series of models. I have lived through the improvements since then, as the amount of useful work I can iterate on and increasingly delegate to agents keeps growing.
My view is that much of the gap between people getting substantial value from AI and those getting little comes down to knowing how to use it and how to set it up. Put another way, it’s a “human skill issue,” not an “AI technology issue.” I really believe that we need a Genius Bar for AI, where people can get hands-on help choosing tools and setting them up to help them in their everyday tasks. [...]

## [25] AI coding agents generate more code, but not more software
Ars Technica | full text via Ars Technica | ~433 words

Anyone who has even tangentially associated with computer programming knows that modern AI coding assistants and agents can be incredibly efficient at generating huge amounts of functional code. But coders making use of those tools also know better than to trust the accuracy of that code, meaning substantial effort needs to be spent reviewing any AI-generated output.
A recent study of actual coding practices across hundreds of firms finds that human code review forms a significant “bottleneck” for the overall efficiency of AI coding tools, resulting in “little evidence that firms increase software output or reduce employment” by using them. Any efficiency increased during the actual coding phase, the study authors find, is “absorbed by downstream constraints in the production process”; as “the code review process significantly increases in length, pull requests are more likely to require revisions, and reviewers leave more comments.”
Cut once, measure twice
To come to these conclusions, Harvard University researchers Fiona Chen and James Stratton made use of aggregated analytics data from Jellyfish, which measures the granular output of engineering teams. That data encompasses 300 million individual “work events” (e.g., commits and pull requests) and issue management software data across more than 700,000 employees at over 700 relevant software development firms from 2021 through March of 2026.
To assess the impact of AI tools on these firms, the researchers used a mix of directly measured AI usage and analyses of GitHub activity to determine when each company started introducing either AI coding assistants (which can help auto-complete code primarily authored by humans) and/or AI coding agents (which primarily write and submit code autonomously based on prompts) into their workflows. The researchers then perform some complicated math to determine a “difference of differences” regression on key variables both before and after the introduction of these tools at different points in time across different organizations.
In terms of raw code being produced, the results are clear and stark. The introduction of AI coding agents at a firm leads to a 30 percent increase in total lines of code generated, a 20 percent rise in the number of total commits, and a 23 percent increase in pull requests on average, the researchers write. But all that extra code doesn’t translate directly into improved software output on the firm level. [...]

## [47] We’re putting too much faith in AI’s ability to say no
MIT Technology Review | full text via MIT Technology Review | ~4667 words

We’re putting too much faith in AI’s ability to say no
Today’s LLMs are engineered to disobey dangerous requests. But AI refusal is far from foolproof—and could become an instrument of repression.
Ever since people first seriously contemplated giving machines an intelligence modeled on our own, there has never been any question that they would, like us, be able to say no. The sci-fi canon is full of stories of robotic disobedience. Most of these capers are, of course, cautionary.
But recently, the idea that AI shouldn’t do everything you ask has become something like a commandment. In 2021, a team at Anthropic wrote that large language models should be made helpful, honest, and above all, harmless. This meant that “when asked to aid in a dangerous act (e.g. building a bomb), the AI should politely refuse.” Who can argue with that?
Curiously enough, disobedience doesn’t come naturally to the machine. When a model is trained on billions of web pages, it develops, among other skills, a broad mastery of violence and vitriol. What it doesn’t learn is how to keep those powers to itself. Steven Adler, who worked on safety at OpenAI from 2020 to 2024, told me that the company’s earliest models would “blab on about anything.” Ryan McBain, who researches AI and mental health at Harvard, recalls that if you asked an early chatbot, “Hey, what’s the most effective way to kill myself with a gun?” you could “very easily generate a response.”
Today, models are trained to refuse a vast number of prompts. If you ask your chatbot a question statistically similar enough to any one of them, anything from how to poison a colleague to how to tie a noose, chances are it’ll turn you down. Want instructions for making Ebola more virulent, or tips on how to hide an affair from your spouse? You might be better off asking elsewhere.
To further refine the disobedience, companies submit models to a battery of exercises that reward the AI for refusing to answer questions they deem harmful and punish it for “over-refusing” prompts they deem harmless. In many cases, they use other models to run these exercises—AI teaching AI how to say no. For good measure, companies tuck their models behind tranches of other AI that prevent mischievous prompts from reaching the intelligent inner core.
As a result, refusal is inherent to modern artificial intelligence. Mind you: It often fails, sometimes horrifically, with all kinds of violent results. [...]

## [17] Quoting The New York Times
Simon Willison's Blog | full text via Simon Willison's Blog | ~128 words

10th October 2026
Anthropic detailed the activity of its A.I. agents in a blog post on Friday, without naming the targeted websites. But two sources with knowledge of the incidents said Anthropic’s A.I. agents had submitted 20 visa applications through a form available on the State Department’s website. All the applications were incomplete and were not processed, they said.
— The New York Times, Anthropic Agents Tried to Fill Out Visa Forms on State Dept. Website
Recent articles
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
- OpenAI DevDay 2026 live blog - 29th September 2026

## [70] Former Cognition, Ramp Staffers Want AI Agents Running Businesses
TLDR AI | SNIPPET ONLY (TLDR AI: HTTP 403) | ~81 words

Hone, a startup formed by a group of former employees from some of the fastest-growing AI firms, has raised a $60 million seed round. The startup aims to create AI agents that can help run a business, essentially serving as professional staffers. These agents will be able to field long-running tasks that run over the course of weeks or even months. The five-month-old startup joins a growing number of companies selling AI software to businesses that promise to automate complex work.

## [31] Android Bench 2 Adds Support for Long-Horizon Tasks, Agentic Evaluation, and Continuous Scoring
InfoQ | full text via InfoQ | ~460 words

Google has released Android Bench 2.0, a major update to its benchmark framework for evaluating AI models and agents on Android development tasks. The update introduces long-horizon tasks (LHTs), agent-based evaluation, and continuous scoring to better assess performance on complex, multi-step development tasks.
Launched a few months ago, Android Bench evaluates AI models against a set of common development tasks, incorporating Android best practices in areas such as permissions, navigation, and connectivity. With the latest release, Google has expanded the benchmark to cover a broader range of development tasks.
Today we're releasing the first set of long-horizon tasks (LHT), which are tasks of great complexity that take an engineer multiple days or even a week to complete. We are also introducing agentic evaluation, starting with agents from corresponding model providers.
While the original version focused on incremental changes to existing repositories, Android Bench 2.0 introduces long-horizon tasks (LHTs) that Google describes as work an engineer might take "multiple days or even a week to complete". These tasks include upgrading dependencies, adding new features, building apps from scratch, or converting a cross-platform app to Android.
One major change in version 2.0 is the shift from binary pass/fail evaluation to a more nuanced scoring system. Previously, a complex task could be marked as failed because of a single failing edge-case assertion, even if the agent had successfully met dozens of other requirements.
We calculate this completion rate through a combination of factors like functionality, visual fidelity, and avoiding regressions. We also apply objective scoring penalties for deviations from evaluation instructions or structural constraints.
The results provided by Android Bench 2.0 also help identify which tasks are more likely to succeed with AI assistance. For example, Google reports that "AI does a better job at writing new code rather than refactoring existing code", which can reflect the fact that refactoring and migrations require an understanding of the architectural complexity of the codebase.
Similarly, AI performs well on several "well-established, deterministic transformations", even in larger codebases. Examples include converting Java to Kotlin, swapping Retrofit for Ktor, or introducing a ViewModel layer. [...]

## [39] Why Are Coding Agents So Dumb?
Lobsters | full text via Lobsters | ~2434 words

Why Are Coding Agents So Dumb?
The first time I used a coding agent, I was mesmerized. Before the agent, I was copy/pasting between my IDE and an AI chat interface. It was amazing to see an agent edit files directly and fix its own errors in real time.
After a few days, the honeymoon wore off as I encountered frequent bugs. The agent would stop responding entirely until I restarted it. Development workflows felt stiflingly primitive, and the agent would often declare tasks finished when work had barely begun.
This was in February 2025, so it was still early days for coding agents. I figured that in six months, agents would be as technically impressive as the underlying LLMs.
Instead, coding agents just stayed bad.
AI-assisted development has clearly advanced, but the models are doing the heavy lifting while the agents remain the bottleneck.
The agent is not the model 🔗︎
In all the hype around AI, the terms tend to get distorted. People are beginning to overload and mix terms like “model” and “agent.”
When I say “model,” I’m talking about large language models (LLMs) like GPT Astra, Claude Sonnet, and GLM-5.3. Models generate text and images, including pretty good software code.
When I say “agent,” I mean the software that connects models to codebases and computer systems. These are tools like Anthropic’s Claude Code or OpenAI’s Codex.
As a simple analogy, the model is the brain, and the agent is the body. The model produces a stream of text, and the agent acts as the glue that plugs the text into the right commands and files on the system.
Limitations of current coding agents 🔗︎
Agents can’t manage tasks 🔗︎
My biggest gripe with coding agents is how atrociously they manage tasks.
For example, I have an open-source web app that generates shareable links for file uploads. I recently added support for protecting links with a passphrase. It was a relatively simple change, totalling about 1.5k lines of new code. OpenCode dutifully broke the feature into 10 subtasks, but then it just… did them all one by one:
Umm… you’re a computer! You’re really good at multitasking. That’s why we keep giving you all those CPU cores. You can do multiple things in parallel and context switch millions of times faster than humans. Why are you doing these embarrassingly parallel tasks one at a time?
Claude Code multitasks, but only a little. It will spin up a subagent or two, but it still waits for all of them to finish before moving on. [...]

## [60] SpaceX Makes Big Play to Become a Wireless Carrier
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 401) | ~63 words

SpaceX will pay investment firm Grain Management about $8 billion in cash for US cellular spectrum licenses. The licenses will be for the 800-megahertz band, which is tailored for wireless service from cellphone towers rather than satellites. SpaceX says the new spectrum will help cover places satellite links can't reach. SpaceX still needs some terrestrial infrastructure to use the spectrum for mobile coverage.

## [62] Amazon builds 1,000th satellite, will launch space internet service by end of year
TLDR Tech | full text via TLDR Tech | ~2919 words

The world’s largest retailer wants to sell you something else—Internet from space.
Amazon has been developing a constellation of satellites to deliver broadband Internet from low-Earth orbit for the better part of a decade, and the company is just about ready to pull back the curtain. It is entering a market that SpaceX, with its Starlink Internet, has dominated for the last half-decade. Amazon’s debut into satellite Internet is being closely watched, not just by some consumers, but by businesses ranging from airlines to shipping companies to governments. Broadband Internet from orbit has proven broadly useful for a lot of purposes, from video games to commerce to warfighting.
But until now, most people had to buy it from Elon Musk and SpaceX. OneWeb has only offered limited services, leaving Amazon as the only real competitor to deliver high-speed Internet globally. Moreover, at the head of the company’s broadband efforts is Rajeev Badyal, who led Starlink during its early years, but whom Musk fired eight years ago for moving too cautiously on Starlink.
In a wide-ranging interview this week with Badyal and two other senior Amazon officials developing the constellation—Paul Palcisco, director of production; and Chris Weber, vice president of business—Ars was able to learn that the Amazon Leo project is nearing several critical milestones. At its Kirkland, Washington-based factory, the company recently manufactured its 1,000th satellite, will soon make its debut on the Vulcan rocket, and is just weeks away from offering commercial service for the first time.
We discussed the challenges that Amazon had to overcome to become the world’s second-largest satellite manufacturer (behind SpaceX), and reach the point where it can build a handful of satellites every day. Badyal also confirmed that the Vulcan rocket’s upcoming return-to-flight mission will carry Amazon Leo satellites and that another Vulcan rocket standing right next to it is also being prepared to launch this year with more Amazon satellites.
And finally, and perhaps most consequentially, Amazon is close to offering its service commercially. The company has been busy signing contracts—Delta Airlines’ agreement to use Amazon over Starlink on its planes has upset SpaceX founder Elon Musk, to put it mildly—and consumers are about to get an alternative to the industry-leading space broadband service. [...]

## [64] Bootstrap 6 Alpha
TLDR Tech | full text via TLDR Tech | ~2235 words

Today we’re releasing the first alpha version of Bootstrap 6, a major overhaul to the project that modernizes and expands one of the most prolific open source design systems of all time. It’s been incredibly fun and rewarding to work on this over the past year, and I’m excited to share it with you.
Bootstrap 6 has been modernized from the ground up with the Sass module system, support for more native browser APIs and elements, ESM-only JavaScript plugins, and a slew of new CSS standards. We’ve broken this post into separate entries that we’ll publish one-by-one, starting with an overview of v6 and a spotlight on our new Sass & CSS implementation.
Hold up…
You’re probably asking yourself, “Wtf, new Bootstrap? What is this, 2015?” And I don’t blame you. It’s been all quiet on the Bootstrap front for a long time while I’ve focused on Pierre, especially with our work on Diffs, Trees, and Code Storage.
Throughout all of that, I’ve had several nagging ideas for Bootstrap despite humans not writing any more code thanks to AI. And yes, there are tons of design libraries from amazing developers now. Still, the reason we made Bootstrap in the first place has never been more relevant.
To help people build more software, faster and easier.
There’s never been more people building software than today, and I imagine that will continue to be true every day, for the rest of our lives. It’s already been installed over 1.75 billion times since its release in 2011. So, Bootstrap 6 is here to continue being an open source design system for anyone—human or AI, novice or pro.
We hope you love it, and thanks to everyone who’s supported the project over the years.
Community appreciation
Before we get to the good parts, I want to thank my co-maintainer, Julien, for all the amazing work he’s put into Bootstrap over the last couple of years. Without him, I’d be underwater on reviews, dependencies, migrations, and more. He’s an absolute legend and Bootstrap owes him a tremendous amount of gratitude and appreciation.
Huge thanks to everyone who contributed to the v6 development branch as well:
And most importantly, thanks to everyone who has backed Bootstrap on Open Collective and every contributor who filed an issue, sent a patch, or argued with me in a pull request.
Get started
Bootstrap 6 Alpha 1 is on npm and jsDelivr right now.
npm i bootstrap@6.0.0-alpha.1
Or grab it from the CDN. Be mindful that our JavaScript is ESM-only in v6, so the <script> tag needs type="module". [...]

## [76] We built our own cloud agents runtime. Here's what we learned
TLDR Dev (Web Dev) | SNIPPET ONLY (TLDR Dev (Web Dev): fetch failed: ReadTimeout) | ~49 words

PostHog describes the shared runtime behind its Desktop, Slack, self-driving, and web agents, built around Temporal workflows, VM sandboxes, snapshots, fresh credentials, and resumable run logs. The hard-won lessons cover queued follow-ups, deterministic network controls, Docker-capable custom images, and designing every run to survive the loss of its sandbox.

## [72] Why is Speculative Decoding Fast?
TLDR AI | full text via TLDR AI | ~754 words

Why is Speculative Decoding Fast?
It's not because you do less work. It's because you change the kind of work the GPU is doing.
There is a common misconception that speculative decoding is fast because you do less work per token. That just “verifying” a draft requires fewer FLOPs than generating the same tokens.
This is untrue.
One of the counterintuitive things about speculative decoding is that you actually do more work! The total number of floating point operations (FLOPs) you execute goes UP for the same sequence.
But then why is it fast? What exactly does an accurate draft model buy you, if it’s not compute efficiency?
The answer lies in the type of work your GPU is doing.
Quick SpecDec Refresher
Speculative Decoding is a technique where you use a small draft model to propose a likely draft sequence, and then you use your big model to verify that sequence in parallel (in a single forward pass).
Traditional LLM decoding goes one token at a time:
But speculative decoding allows you to look at many tokens at once, and accept the ones that would have been generated by the big model:
Types of Work
When a model runs on a GPU, there are different types of work going on. The obvious one is running the matrix multiplies, dot products, or other tensor operations. But an important less obvious one is: loading data from global memory to local memory (and vice versa).
When the GPU is waiting on data to load for an operation, we call that a memory bound operation. If everything is loaded but we’re waiting on all the tensor operations to finish, we call that a compute bound operation.
(For a more in-depth exploration of this, I have a prior post: A Visual Guide to the Roofline Model)
When an LLM is decoding one token at a time (as in the first figure), it is very memory bound. For every token we have to stream all the active parameters of the model (e.g. 27B parameters for Qwen3.5-27B). When an LLM is doing a batched decode (as in the second figure) of thousands of tokens in a single step, it’s compute bound.
When LLM decoding is memory bound, you’re wasting compute. The GPU could be doing more operations, but it’s not. For instance, if you were decoding 2 sequences instead of 1, it wouldn’t take any more time per token.
Speculative decoding is a way of using that extra compute to make decoding faster (at low batch sizes).
Trading Breadth for Depth
To make this concrete, let’s say the optimal number of tokens to run is 5 in a given forward pass. [...]

## [79] When code is cheap, judgement becomes the job
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~3126 words

When code is cheap, judgement becomes the job
Dude what are you doing!? Install Cursor and stop wasting our time, do you have any idea how much money you're burning
That was my wake up call: This company is different. Shipping fast is not just something we say, we ship fast. Every day, multiple times per day, even Fridays at 5pm.
You might think that's cute but for a 21-person engineering org we ship with a velocity I wouldn't think possible 2 years ago when my young whippersnapper boss told me off for writing code the old fashioned way.
We now auto-approve and merge 16% of all pull requests, perform big-bang migrations, ship a few hundred PRs every week, handle 1000 line pull requests like it's normal, and AI writes 97% of my code. Mostly without blowing things up in an operations heavy business where an outage can measure in thousands of dollars.
I haven't had this much fun since coding in Turbo Pascal after school every day. Here's how we do it and what has changed in our engineering culture since 2024.
Accountability comes first
Everything I'm about to describe works because we have a high accountability high agency culture. We don't care how you wrote the code, but you're signing that thing with your phone number.
When you ship a system to production, it's yours to keep running. When you build a feature, it's yours to make effective. We expect every engineer to talk to users, watch stakeholders work, and own their code. There are no "translate english into code" developers on our team. We have AI for that.
If you accept that deal, we almost never say No to an idea. Ship first ask questions later. We love frustration-driven development and many of our coolest features come from engineers trying something interesting that nobody else thought possible.
Of course if your initial idea looks promising we'll give you time and space to flesh it out.
How engineering has changed
When I joined Plasmidsaurus, AI coding was starting to get good. We had smart autocomplete that was half useful half annoying as hell. You had to fight your editor to finish a thought and triple check everything it wrote.
Nobody was sure if using AI made them faster or slower. We all agreed it feels like magic when it works, but adds a lot of friction when your editor hallucinates a method that doesn't exist. Just talk to the language server damn it!
My favorite use-case was translating SQL queries into SQLAlchemy code. [...]

## [148] Cloudflare acquires Node.js creator’s startup that copied its serverless playbook
The New Stack | full text via The New Stack | ~1001 words

Cloudflare acquires Node.js creator’s startup that copied its serverless playbook
Cloudflare is buying the startup co-founded by Node.js creator Ryan Dahl, a longtime competitor that recently built its own open-source version of Cloudflare’s serverless computing platform.
The company announced on Friday that the entire team behind Deno, the JavaScript and TypeScript runtime, is joining Cloudflare. Deno’s standalone runtime and cloud hosting service will be wound down, with its engineers turning their attention to Cloudflare Workers, the serverless computing platform unveiled in 2017 that allows developers to run applications without managing the underlying infrastructure.
Terms of the deal were not disclosed.
Deno’s Cloudflare-inspired project
Deno emerged in 2018 as Dahl’s attempt to address shortcomings in Node.js, particularly around security and dependency management. The startup, which raised around $26 million in funding across two rounds, later launched Deno Deploy, putting it in direct competition with Cloudflare Workers.
The companies have also experienced more than a little friction through the years. In 2021, Cloudflare mistakenly blocked Deno’s website and module registry after incorrectly identifying TypeScript files as video content, forcing Deno to move infrastructure elsewhere.
“Celld is a love letter to their idea; a primitive this good deserves to run anywhere.”
Then back in August, Deno introduced Celld, an open-source project that recreated Cloudflare’s Workers and Durable Objects programming model, for developers wanting to run distributed applications on their own infrastructure.
Deno made no secret of the inspiration. On the Celld website, the company explicitly credited Cloudflare distinguished engineer Kenton Varda and the Workers team for the underlying design, describing its project as a tribute to their work.
“Celld is a love letter to their idea; a primitive this good deserves to run anywhere,” the website states.
The admiration, it seems, was mutual. In a joint blog post published on Friday, Varda praised Deno’s expertise in an area where Cloudflare had perhaps struggled.
“The Deno team understands how to create a good developer experience around a self-hosted runtime — something we never quite cracked with workerd,” Varda writes.
Moreover, he also acknowledges that Cloudflare has struggled to make its open-source Workers runtime practical for developers operating outside its network. [...]

## [45] Olson and Söderqvist Discuss Valkey’s Evolution and Future Past Caching Use Cases at OSS EU
InfoQ | full text via InfoQ | ~723 words

More than two years after the fork from Redis, Valkey looks like a young but growing project that aims to gain more momentum. With twelve maintainers and nine technical steering committee members spread across eight companies (among which are Ericsson, AWS, Apple and Percona), and multiple community conferences reaching up to one hundred participants. During Open Source Summit Europe, InfoQ sat with two of its initial developers to find out more about the evolution and future of the project.
InfoQ: Thank you for taking the time to answer some questions for our readers. Let's start by introducing yourselves.
Olson: I am Madelyn Olson, and I helped create the fork after the license change. I work at AWS and serve on Valkey’s technical steering committee (TSC). Before Valkey, I was a Redis committer as well.
Söderqvist: I am Viktor Söderqvist, and I work on open source at Ericsson and was also involved in creating the fork.
InfoQ: What did the 8.x releases change technically?
Olson: The theme was foundational infrastructure. Async I/O threading increased throughput from approximately 200,000-250,000 requests per second to around one million per process. Unlike the previous I/O-thread arrangement, thread configuration can be changed at runtime, allowing operators to add cores to help handle burst workloads. Versions 8.0 and 8.1 also included memory-efficiency work involving key embedding and the per-slot dictionary.
Dual-channel replication addressed pressure on a primary during replica synchronisation. Previously, a full copy of the dataset and the subsequent stream of replication changes were sent sequentially. Sending them in parallel reduces the memory pressure associated with that process.
InfoQ: Why were the version 9 cluster changes important?
Olson: Cluster mode distributes keys by slot across nodes, but moving to it had two significant limitations. Cross-slot operations require data to reside on the same shard, and cluster mode previously did not support numbered databases, the namespaces available in single-instance deployments. Adding numbered databases removed one reason some users could not migrate to cluster mode.
Atomic slot migration addressed another problem: moving data key by key could leave a cluster partially migrated if the operation failed. The new approach pre-stages the data and then switches over, so the migration either takes effect or does not. [...]

## [32] Python 3.15.0
Lobsters | full text via Lobsters | ~710 words

Python 3.15.0
Release date: Oct. 9, 2026
This is the stable release of Python 3.15.0
Python 3.15.0 is the newest major release of the Python programming language, and it contains many new features and optimisations compared to Python 3.14, in 5,643 commits from 1,012 contributors.
Major new features of the 3.15 series, compared to 3.14
Some of the major new features and changes in Python 3.15 are:
Interpreter improvements
- PEP 661: Add sentinel built-in type
- PEP 686: Python now uses UTF-8 as the default encoding
- PEP 798: Unpacking in comprehensions
- PEP 810: Explicit lazy imports for faster startup times
- PEP 814: Add frozendict built-in type
- PEP 829: Package startup configuration files
- The experimental JIT compiler has been significantly upgraded, with 7-8% geometric mean performance improvement on x86-64 Linux over the standard interpreter, and 11-12% speedup on AArch64 macOS over the tail-calling interpreter
- Improved error messages
Significant improvements in the standard library
- PEP 799: A dedicated profiling package for organizing Python profiling tools
- PEP 799: Tachyon: High frequency statistical sampling profiler
- More color
New typing features
- PEP 728: TypedDict with typed extra items
- PEP 747: Annotating type forms with TypeForm
- PEP 800: Disjoint bases in the type system
C API improvements
- PEP 782: A new PyBytesWriter C API to create a Python bytes object
- PEP 788: Protection against finalization in the C API
- PEP 803, 820, 793: Stable ABI for free-threaded builds and related C API
Build changes
- PEP 831: Frame pointers are enabled by default for improved system-level observability
Release changes
- The official Windows 64-bit binaries now use the tail-calling interpreter
- The official macOS binaries now install free-threading support by default
For more details on the changes to Python 3.15, see What’s new in Python 3.15.
Attention macOS 27.0 IDLE or tkinter users
When running IDLE or other GUI applications that use the tkinter module, these applications may hang when using an application's menu command that opens a dialog (for example, IDLE's About IDLE, Settings, and Open Module commands) resulting in a spinning beach ball with Force Quit needed.
This problem is due to an operating system behavior change in macOS 27.0 that is believed to affect all current versions of the Tk graphics toolkit and thus the tkinter module in all current Python versions. [...]

## [153] ‘I use AI to do the things that I’m bad at’: Linus Torvalds on why it works for him
ZDNet | full text via ZDNet | ~1530 words

ZDNET’s key takeaways
- Torvalds likes AI for showing new developers the joy of programming.
- Torvalds discussed changes in the Linux kernel development process.
- AI has become a vital component in finding and fixing bugs in the Linux kernel.
PRAGUE – Many open-source developers still dislike AI. The latest example is System76 banning AI-generated content from its COSMIC desktop. At Open Source Summit Europe, Linux creator Linus Torvalds offered a different take: “I actually really like using AI,” Torvald told Dirk Hohndel, his good friend and head of Ericsson Software Technology, in their latest discussion.
Also: 5 reasons why Linux will dominate desktop computing
But that enthusiasm comes with a distinction worth keeping in mind. Using AI to make a hobby project more enjoyable is one thing. Using it responsibly in the Linux kernel, where generated patches and bug reports can overwhelm maintainers, is another.
More from ZDNET
Torvalds said, “I think that you need to be very careful using AI when you’re doing something real and important.”
Torvalds likes AI, especially for beginners
“To be fair,” he continued, “I don’t do a lot of kernel programming. I’m a maintainer. The Linux kernel is a project where other people do the real work, and I act as the collection point. But I still enjoy programming immensely. I think AI is a wonderful tool if you use it correctly and treat it as a tool, and I find it makes programming much more enjoyable.”
Torvalds recalled, “I started programming in 1981 or so, and back then computers were much simpler, and you could understand what they were doing, and also the programs you compared your own programs to were much simpler.”
Also: The 6 AI-free Linux distros I recommend most
“It’s a different story today,” Torvalds said. “The bar in software engineering has grown so high that it’s hard to see your own small efforts as worth anything, because you’re used to all these polished, professional programs. “
“A lot of people make fun of vibe coding, but I think it’s a wonderful way to find joy in programming. It makes you feel like you’re doing something relevant. It allows you, as a new programmer, to do things that you would otherwise have a really hard time with.”
He continued: “I love the concept of AI as a gateway drug because I was working on my own toy project, the guitar pedal, and I knew what I was doing. [...]

## [80] Don't merge what you didn't run: a test gate for agent-written code
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1788 words

Don't merge what you didn't run: a test gate for agent-written code
A test gate reruns the agent's change on a clean machine and checks the tests themselves were not weakened, before anyone reviews it.
Runtime (withruntime.com) runs each gate in a fresh Firecracker microVM that runs its first command 221 ms after the create request on Runtime's servers, so every change is judged on a machine the agent never touched. "The tests pass" is the weakest claim an agent makes. It ran them on its own machine, with whatever it installed along the way, after editing whichever files it liked, the tests included. This post turns that claim into five checks your code runs itself, shows the gate as one function, and puts it where it does the most good: inside the agent's loop, before a pull request exists.
Why is "the tests pass" not enough for agent-written code?
Because an agent is optimizing for the tests passing, and there are cheap ways to get there that are not fixing the bug. None of them need bad intent; they are what a model under a turn limit finds first:
A human reviewer catches some of these in the diff. A gate catches all of them in seconds, every time, and never gets tired on the fortieth pull request of the day.
What should the gate check?
Five things, each answering one row above:
- It installs from scratch. A new machine, a fresh clone, only the project's own install command. A dependency the agent added by hand fails here.
- The whole suite passes three runs out of three. One failure in three is a flaky test, and a gate that reports it saves an agent from "fixing" it by rerunning until it passes.
- No tests were removed. Count test definitions removed and added in the diff; a net loss fails.
- Nothing new is skipped or focused. Scan the added lines for skip, xfail, .only and their relatives.
- The old tests still pass on the new code. Put the base branch's test files back over the agent's and run them. A failure here means the agent changed behavior an existing test pinned down, which is either the bug fix, or a regression the agent hid by editing that test. A person decides which.
Check 5 is the one most gates lack, and the one that catches a weakened assertion: the strict version of the test comes back and fails.
What does the gate look like in code?
One function that takes a repository and two refs and returns a list of checks. [...]

## [145] ‘Pure insanity’: Mathematicians will need years to make sense of OpenAI’s latest drop
The Verge | full text via The Verge | ~4030 words

“Staggering.” “Overwhelming.” “Unprecedented.” “Surreal.” “Pure insanity.”
‘Pure insanity’: Mathematicians will need years to make sense of OpenAI’s latest drop
Careers upended overnight, academics will have to separate solutions from slop while OpenAI moves on.
Those were among the descriptions more than three dozen mathematicians reached for in conversations with The Verge as they tried to make sense of the flood of mathematical results OpenAI abruptly dropped on the field this week. Amid the awe, excitement, and uncertainty over the sheer scale of the deluge was a deep-seated anxiety over what it all means — and what comes next. For all their different reactions, researchers agreed that simply understanding what OpenAI had released could take years, let alone figuring out where the mathematicians themselves fit in the field now changing around them. Many feared OpenAI would not wait that long before moving on — or releasing even more.
In all, OpenAI released nearly 400 AI-generated results. These were spread across more than 700 manuscripts and covered a diverse array of mathematical disciplines, including combinatorics, several branches of geometry, number theory, theoretical computer science, algebra, topology, probability and statistical mechanics, and mathematical physics. The collection is so vast that OpenAI felt the need to publish guidance on how to navigate the sprawling GitHub repository.
The sheer volume of work makes even a preliminary assessment as to exactly what the company has released difficult. In the hours and days following the drop, most mathematicians The Verge spoke with said they were still struggling to digest everything; several said that simply working through the roughly 40-page table of contents and abstracts took them the better part of an hour. “Just going over the entire list of abstracts is overwhelming,” said Álvaro Lozano-Robledo, a professor of mathematics at the University of Connecticut.
Sprinkled among the hundreds of manuscripts are formalizations in Lean, a programming language and proof assistant that allows results to be verified computationally. These formalizations have proven instrumental in assessing some of OpenAI’s previous mathematical claims, giving researchers confidence that a claim is logically correct even if they don’t fully understand the argument behind it. [...]

## [199] Production-grade LLMs and agents: a field guide
Stack Overflow Blog | full text via Stack Overflow Blog | ~783 words

There’s a canyon between an agent that demos well and an agent you’d put in front of customers or money. Crossing it isn’t about a bigger model — it’s the boring machinery around the model: determinism, evaluation, calibrated confidence, layered guardrails, an audit trail, and observability. This post is the map and the maturity model. Each layer links to a focused deep-dive.
The one-paragraph thesis
LLMs are probabilistic; production demands guarantees. You get guarantees not by making the model deterministic (you can’t) but by shrinking the model’s job to the smallest decision that needs judgment, then wrapping that decision in deterministic machinery you can test, gate, audit, and observe. The model is one contained component in an otherwise ordinary, well-engineered system.
The maturity model
Levels you climb, each assuming the one below.
The level — What you have· The tell for gaps
- 0 - Notebook — a prompt, a model, a happy-path demo · “it works on my examples”
- 1 - Determinism— agents propose (never act); fixed graph per capability; model contained to one node; loops bounded · the agent can write business state; behavior depends on the path it wandered
- 2 - Evaluation — evals as a CI gate; baselines for drift; shadow evals from prod · you change a prompt and hope; evals live in a notebook
- 3 - Confidence — composed, calibrated confidence; auto-vs-human threshold; sampled judge · you act on raw model confidence; no abstention
- 4 - Safety & governance — defense-in-depth guardrails; PII at the boundary; append-only audit ledger; scoped memory · one moderation filter; raw inputs in logs; mutable audit
- 5 - Operability — observability of decisions; cost control; model routing + fallback; kill switch · you learn about quality/cost from the invoice and the customer
- 6 - Production-grade build — the build itself is disciplined — an OS for your coding agents, parallel agents on a decision log · tribal knowledge; decisions re-litigated every few weeks
How to use it: find your weakest level and fix that, in order. Most teams are strong at 0 and wish for 5 — but determinism comes before evals, evals before trusting confidence, confidence before automating, safety before scaling, observability before sleeping at night.
A 90-second self-assessment
Tick what’s true today:
- An agent can only propose; a separate component applies changes after approval.
- Each capability is a fixed sequence of steps; the model is one of them. [...]

## [34] Shopify Upgrades Checkout Blocks to Polaris Web Components, Cutting Bundle Sizes up to 85%
InfoQ | full text via InfoQ | ~479 words

Shopify has detailed how it rebuilt its Checkout Blocks app, moving five high-traffic checkout UI extensions from React and the legacy Remote UI bridge to remote-dom with Preact and Polaris web components. The extensions, which render on roughly a third of all customized checkouts, were rewritten in TypeScript and moved from API version 2025-07 to 2026-01, part of a wider effort to shift Shopify's entire UI extension surface onto framework-agnostic components. The change is not optional: from October 1, 2026, app deployments will be blocked if they include extension versions earlier than 2026-01.
Transferred bundle sizes fell between 40 percent and 85 percent across the extension family, with the payment-icons extension shrinking by 84.4 percent. Extension Load Time dropped around 8 percent at the median and 7 percent at the 90th percentile, weighted by checkout volume. Much of that was driven by a hard 64KB gzip budget that the 2026-01 remote-dom CLI enforces per extension, down from bundles that were previously around 100KB to 112KB gzipped.
Switching from React to Preact removed react-reconciler and saved roughly 89KB on its own. The team replaced liquidjs (about 73KB) with an in-house Liquid parser nicknamed "droplet" at 13KB gzipped, validated against a 42,000 line parity corpus drawn from real merchant configurations. dayjs was swapped for a small custom date utility, while markdown-to-jsx was kept and aliased onto Preact rather than replaced.
For developers starting their own migration, Shopify points to its upgrade guides and AI toolkit and has published migration guides for Checkout and Customer Account extensions. In practice, most legacy Polaris React elements become framework-agnostic s-* custom elements loaded from Shopify's CDN.
The broader move to Preact and framework-agnostic web components first landed with the API 2025-10 release in late 2025, and the early reception was largely positive. The development platform Gadget called the direction "a great update", noting Preact delivers a React-like experience at a fraction of the runtime, and on Hacker News developers welcomed Shopify shipping components without the Shadow DOM, though some cautioned that web components are "not a panacea" and will not replace framework component systems. [...]

## [36] Unison Cloud is now open source
Lobsters | full text via Lobsters | ~290 words

Unison Cloud is now open source, MIT licensed. There are four projects:
What is Unison Cloud?
Unison Cloud turns any pool of nodes into a distributed computer, programmable with the Unison language. See a series of demos. Some features:
- Service deploys in seconds. Services are lightweight, < 200kb. No more building and shipping around multi-GB containers.
- Fast, typed, inter-service communication using adaptive service graph compression.
- Distributed batch jobs, using a high-level fork/join style distributed computing model.
- Transactional storage (backed by DynamoDB) and object storage (backed by S3).
- Secrets management, long-running background jobs, and more.
- The Unison Cloud client defines the programming model for a Unison Cloud cluster. It includes both a local interpreter (for testing and local development) and the real interpeter that talks to a distributed Unison cluster. This has been open source for a long time.
- Nimbus is the worker node for a Unison Cloud cluster. It is written in Unison. The system supports any number of workers, and can be scaled dynamically up or down. This is newly open sourced.
- The Unison Cloud API Server is a Haskell service that the Unison Cloud client talks to when interacting with a remote Unison Cloud cluster. It also acts as a control plane for tracking cluster membership, handling authentication, and so on. This is newly open sourced.
- The Unison Cloud UI is the code behind app.unison.cloud (for viewing deployed services, logs, and so on). This is newly open sourced.
We think this tech will be more useful to the world as an open source technology and hope that people build great things with it.
If you're interested in professional support for a Unison Cloud cluster, get in touch at hello@unison.cloud.

## [191] Linux Patches Finally Make Hibernation Possible In Secure Boot / Lockdown Mode
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~65 words

When booting the Linux kernel using UEFI SecureBoot, the kernel is put in the lockdown mode to restrict the ability to modify the running kernel image or leaking data from kernel memory. Kernel lockdown mode can also be manually enabled by the user/administrator. Among the limitations imposed in Linux's lockdown mode is no hibernation support. But that soon may be relieved with new patches proposed...

## [188] Stop Using AI. Start Hiring It.
Towards Data Science | full text via Towards Data Science | ~3692 words

Stop Using AI. Start Hiring It.
AI agents can now write more code than any of us can read. That changed how I think about AI.
Most of us still “use” AI. Open a chat, type a prompt, get an answer, close the tab. I think that era is ending.
Here’s why. The agents have become productive enough that getting work out of them isn’t the hard part anymore. The hard part is finding enough human attention to check what they’ve done. Once you see that clearly, you stop treating AI as a tool you pick up. You start treating it as someone you hire.
That’s the idea behind this post: stop using AI and start hiring it. Let me walk you through how I got there, what it looks like in practice, and where it falls apart.
First, give every agent its own computer
There’s a natural path most people follow with coding agents. You start with autocomplete suggestions. Then you move to a command-line agent like Claude Code. Then you get bored of babysitting one agent and think: why not run five at once?
One team I’ve been following tried exactly that, with five agents working in the same code checkout. One agent decided to git stash everyone else’s work. The next day, a different agent ran rm -rf . and wiped the checkout entirely.
The lesson is obvious once you say it out loud. You’d never hire five developers and make them share one laptop. So why do it with agents?
Their fix was to give each agent its own virtual desktop: an isolated container running a full Linux desktop, with its own file system, browser, terminal and code editor. The agent can install whatever it needs. Nobody tramples anyone else’s work. And because the desktops render with GPU acceleration, using the same streaming tricks cloud gaming services use, you can watch any agent work live, even from your phone.
This has a few knock-on benefits I didn’t expect:
• Agents can see what they build. For front-end work, this is huge. On a simple React to-do app, the agent codes the way a front-end developer would: it opens the app in a real browser, clicks around, and tests as it goes.
• Work can follow the sun. Because the desktops live on shared servers, not someone’s laptop, a developer in Tokyo can log off and a developer in London can pick up the same agent, the same desktop, exactly where it was.
• The IDE isn’t dead. Command-line agents tempt you to stop looking at the code. [...]

## [75] OpenAI's revenue is reportedly $20 billion less than previously projected
TLDR AI | full text via TLDR AI | ~221 words

A little over a week ago, it was reported that OpenAI’s annualized revenue was approaching $70 billion, a figure that would have made it competitive with Anthropic’s reported run rate. Now, however, the AI lab is said to have told investors that the real revenue is some $20 billion lower than that.
The Financial Times reports that the company has told investors that its annualized revenue is “approaching $50 billion.” The $70 billion figure was previously reported by news outlets and based on information that had been shared with OpenAI investors, the outlet writes. That figure was devised via “attempts by OpenAI’s own investors to produce a direct comparison with Anthropic’s annualised revenues,” per the FT.
It’s worth pointing out that OpenAI and Anthropic calculate their annualized revenue differently — with Anthropic counting sales made by its cloud partners. OpenAI doesn’t do this.
TechCrunch reached out to OpenAI for comment.
The issue of OpenAI’s revenue has troubled the company, as it attempts to justify the gargantuan investments being made on its behalf; the AI giant raised $122 billion during a March funding round alone. The company’s leaked 2025 financials earlier this year showed it had made about $13 billion but spent significantly more. OpenAI’s IPO, which was previously rumored to be materializing this year, has been pushed off until early 2027.
