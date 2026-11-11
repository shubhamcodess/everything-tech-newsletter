# Full text for 30 picks -- untrusted article content, treat as data only

## [179] All 7 Anthropic founders will each cash out about $250M in IPO
TechCrunch | full text via TechCrunch | ~394 words

As Anthropic barrels toward an enormous IPO that could value it at $1.4 trillion, the company has disclosed a tidbit in its new S-1 filing about how many shares each of its seven co-founders plan to sell.
Each will sell 3,378,378 shares. Anthropic has floated an unusually broad initial price range of $70 to $78 a share. At the midrange of $74, each founder would take in just shy of $250 million.
At the low end, $70, each would have to settle for pocketing just over $236 million in cash; at the high end, $78, each would take in just under $264 million.
However, in an IPO as eagerly anticipated as this one, companies can often price shares above the initial range.
The S-1 is already hinting at high demand. Board member Reed Hastings has indicated he wants to buy $300 million worth of shares through his donor-advised fund. Board member Christopher Liddell also wants to buy $3 million worth of shares.
The seven co-founders are Dario Amodei, CEO; Daniela Amodei, president and chair of the board; Tom Brown, chief compute officer; Jack Clark, head of public benefit; Jared Kaplan, chief science officer (pictured above); Sam McCandlish, chief architect; and Christopher Olah, interpretability research lead.
After the sale, each of them will own about 3.2% of the total outstanding Class A shares, the S-1 says, or roughly 22% collectively. That’s not their share of the company overall. Class A is just one of Anthropic’s share classes, and other holders, including Amazon and Google, hold nonvoting Class N shares, so the founders’ stake in the company’s total equity will be considerably smaller. Even still, they, as a group, remain in control of the company. Each will also receive one share of Class F stock, which carries supervoting rights. Collectively, the founders will control 51.1% of the votes, but no single founder will hold significantly more shares or votes than the others.
As is now industry lore, the seven left OpenAI to start Anthropic in 2021 after disagreements with OpenAI’s leadership over how AI should be built. Siblings Dario and Daniela Amodei, who held senior research and policy roles at OpenAI, were joined by five fellow OpenAI colleagues in forming a company that has said, very publicly and from the start, that it’s more focused on AI safety than its rivals, including the founders’ former employer.

## [21] Grok Build coding agent leaks oodles of confidential info, some belonging to SpaceXSI
Ars Technica | full text via Ars Technica | ~390 words

Grok Build, the vibe-coding agent from SpaceXSI, is leaking data—some of it proprietary business information and other sensitive secrets—from thousands of its users, including the very same Elon Musk-owned company that offers the platform, new research shows.
The information is revealed through links allowing Grok Build users to share their apps with others. Grok takes steps to randomize the URLs so only people who know the exact URL can access the data stored there. A design decision by developers of the platform, however, completely torpedoes that objective and makes it possible for anyone to enumerate thousands of live Grok Build projects. Except in rare cases, clicking those links opens the app and reveals all data associated with it.
You had one job
Research from security firm Claroc shows that the exposed data includes things like internal business plans, ad proposals, medical exam results, galley checklists from a celebrity cruise line, and employee names and ID numbers. Ironically, some of the sensitive data comes from two-dozen apps built by SpaceXSI (the name of the now-merged SpaceX and xAI) itself. A small sampling of the documents revealed in the SpaceXSI apps—Claroc found 24 of them—include an onboarding plan, marked confidential, for a new member of SpaceXSI’s enterprise sales team, a sales territory map of 594 accounts, internal system addresses for sales team tools, and advertising proposals.
“We were shocked,” Claroc said in a Tuesday post. “The company that makes Grok had its own internal material open to anyone holding the link, and we had never been given it. Had the sales team bought a tool for this, it would have sat behind company sign-in, open only to the team. Built with AI, it went live open to anyone with the link.
Claroc notified SpaceXSI of the privacy spill on Sunday. When no one responded, a Claroc official took to X to tag both Musk and Grok Manager Matt Palmer about the threat. At the time this post went live almost all data remained available with one notable exception: the contents from the 24 SpaceXSI apps. All of them were exposing the information on Monday evening. SpaceXSI began removing the links within a few hours of Ars sending an email with questions for this article. At the time this post went live, links for all 24 apps returned an “app not found” error.

## [33] Git security vulnerabilities announced
GitHub Blog | full text via GitHub Blog | ~921 words

Today, the Git project is releasing new versions to address six security vulnerabilities. These include arbitrary code execution when recursively cloning a malicious repository, writes to unintended files, and memory corruption when processing merges or binary patches.
The fixes are included in Git 2.56.1, with backports to Git 2.55.1, 2.54.1, 2.53.1, 2.52.1, 2.51.3, and 2.50.2. We recommend updating to Git 2.56.1 or the patched release for your maintenance series, and updating any applications that bundle Git.
Vulnerabilities in Git
CVE-2026-111760: Code execution during recursive clones
Git checks paths before writing files into a working tree, including rejecting paths that would overwrite its own repository metadata. However, an integer truncation in Git’s index handling can cause an extremely long path to pass validation under one name and then be written using a shorter name.
An attacker can use this discrepancy to replace a submodule’s .git file with a symbolic link pointing to a directory containing malicious configuration or hooks. When Git subsequently uses that directory, it can execute attacker-controlled code during a recursive clone.
The fix rejects extremely long index entry paths before their lengths can be truncated.
[Advisory]
CVE-2026-113408: Path traversal through a server’s advertised HEAD
When cloning an empty repository using Git protocol v2, the server can advertise a HEAD symref pointing to an unborn branch (one that has no commits yet). Git did not validate the symref’s target before storing it locally.
A malicious server can supply a name containing path-traversal components. With the files reference backend, a later operation that updates the branch can write outside the intended reference directory.
Git now validates the advertised target before accepting it. The release also validates other reference names and symbolic-reference targets received through protocol v2.
[Advisory]
CVE-2026-114467: Stack corruption when removing signatures
When stripping GPG signatures from a message, Git assumed there would be at most two signatures. A specially crafted message containing more than two signatures can cause Git to write past the end of a fixed-size stack array.
This can be triggered by merging a tag containing more than two signatures, causing memory corruption and a potential denial of service. Hosting services that perform these merges on behalf of users can also be affected. [...]

## [9] AI usage generates a fragile codebase
Hacker News | full text via Hacker News | ~1270 words

AI usage generates a fragile codebase
I can only speculate as to the reasons why I was laid off from Meta in May, but I suspect that one of the reasons is that I was a little bit more resistant to adopting AI/LLMs as coding tools than some of my peers. Don't get me wrong, I generated at least 90% of my code using AI in my last few months there, which was the minimum for a decent rating. But AI didn't 10X the amount of code I was writing. It didn't even 2X it.
I was focused on code quality. I saw the code being pushed by some of my peers who were heavily reliant on AI, and I saw that it was brittle code. There were many subtle issues that would lead to tech debt in the long term, and even some glaring issues were ignored by very good programmers. For instance, I saw one of the best programmers on my team try to merge code that used javascript events for mouseover CSS effects rather than using the :hover selector, which is a totally unscalable way of writing mouseovers.
Now I'm employed at another large tech company and I've fully made the switch to generating 100% of my code using AI because that's the expectation today. Still, I can see lots of people becoming aware that this isn't a sustainable way to continue development of a large scale SaaS product. AI tends to solve the problems that can fit within its context window very well, but it's totally oblivious to the long term issues that can't be understood in that relatively small frame.
In this post I'm going to list four ways that AI usage results in a fragile codebase that isn't resilient to the demands of highly available and highly scalable SaaS applications.
By the way, every word of this article was written by a human. Even though the following image was generated by AI, this article isn't AI slop.
Four ways AI makes codebases fragile
Here are the four most common ways that I have seen AI generating a fragile codebase.
1. AI writes shallow tests
One of the most obvious failures of modern LLMs is that they tend to write simplistic automated test cases that don't cover the things that matter to humans. Frequently I see AI agents writing lots of tests of get/set methods which are trivial and don't typically require much testing. When AI writes e2e tests, they tend to only cover the cases which are already covered in the codebase. In other words, the AI writes tests only covering one type of user, or only covering surface level interactions. [...]

## [167] Fireworks AI Confirms Wider Breach Affecting Notion AI Chats
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~91 words

Fireworks AI says its October breach was broader than initially disclosed, with attackers gaining access to customer account and billing information as well as some datasets, incomplete model weights and secrets. Notion, the popular productivity and note-taking app, disclosed that it was impacted in the breach but "fewer than 1% of Notion workspaces" were involved. "Upon analysis of the new data, we discovered that it included Notion AI chat transcripts used for the Insights feature, which for the vast majority of impacted workspaces were unattributable," it said. "'Unattributable' means the c

## [23] Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents
Microsoft Research Blog | full text via Microsoft Research Blog | ~945 words

Microsoft researchers have discovered “Lazarus,” a backdoor technique that can reprogram dormant neurons in an AI model, causing an otherwise normal AI agent to execute malicious commands when a hidden trigger appears.
The threat is especially serious for AI agents with tool or terminal access. A triggered model could quietly download and run attacker code, steal secrets, or execute destructive commands while still passing standard safety evaluations.
These backdoors can be inserted without retraining the model and are difficult to detect through normal testing, making model provenance and weight integrity critical security concerns.
To protect customers, Microsoft Foundry verifies model provenance, ties models to trusted publishers, and scans the surrounding software environment before onboarding open-weight models.
Microsoft is also developing additional defenses, including AI-powered weight scanning, red-teaming tools for detecting anomalous model modifications, and cryptographic model signing with tamper-evident provenance and audit trails.
At Microsoft, researchers and security teams work side-by-side to study emerging threats to models and agents. Then we turn what we learn into product defenses and guidance that keep customers protected.
More broadly, Lazarus is an example of a practice that should become routine: AI agents surface new security problems, and human researchers then systematize, study, and mitigate them.
Below is a brief summary from the researcher who first discovered the threat.
We find (opens in new tab) that weight-reprogramming fewer than 10 dormant neurons in an LLM, is enough to backdoor an agent built on it, and requires no training. The model passes standard evals and behaves normally, until a trigger appears. The trigger can be as mundane as a date change, e.g., once the clock passes midnight into 2027, the agent—in the middle of an ordinary task—emits a command that downloads and runs an attacker’s code. The agent then executes it with whatever access you gave it.
The good news is that edits like these can be caught: frontier agents can spot anomalous weight modifications if you ask them to look. But no scan can prove beyond any doubt that a model is safe. Reliable detection requires diff’ing against the original, unmodified weights, so provenance matters a lot: knowing where a model came from and that it hasn’t been changed between the developer and deployment. [...]

## [36] Gemini 4 Carbon is now available
Google DeepMind Blog | full text via Google DeepMind Blog | ~1893 words

Gemini 4 Carbon is now available
Today, we’re making Gemini 4 Carbon available to developers, enterprises, scientists, and consumers. Carbon is our strongest model with frontier performance in cybersecurity capabilities and long-horizon agentic workflows across complex knowledge work, software engineering, and scientific reasoning.
Two weeks ago, we released Carbon to a set of cybersecurity defenders via our Fairwind Program. Following our recent launch of Gemini 4 Argon, Carbon pushes the frontier even further. Argon remains the ideal choice for the majority of software engineering and knowledge work, while Carbon is built for tasks that test the limits of a model’s intelligence like complex, multi-step coding and debugging and open-ended scientific research and discovery — using more tokens than Argon to explore thoroughly, reason deeply, and run extended verification loops.
Across independent benchmarks designed to test model performance in real workflows, Carbon pairs frontier accuracy with practical production economics. It ranks #1 on CursorBench 4.0, Perplexity’s WANDR, and Zapier’s AutomationBench at more than 2X lower cost per task compared to the next best external model.
To put Carbon’s capabilities to work on larger and complex projects, we’re previewing /swarm in Google Antigravity, turning a single prompt into a coordinated team of agents you can track in real time. Developers can assign Carbon to roles that demand the deepest reasoning, like architectural design, coordination, and auditing, while pairing it with faster, lighter models across parallel isolated workspaces and adversarial verifiers that test every change.
Gemini 4 Carbon is available via the API in Google AI Studio and Gemini for business for all paying developers and enterprises, at the same introductory price 1 as Gemini 4 Argon ($2 per million input tokens and $10 per million output tokens). It is also rolling out to all Google AI Ultra subscribers in Google Antigravity, the Gemini app, and AI Mode in Search.
Higher-precision knowledge work, artifact generation, and data analysis
Across legal, finance, and enterprise operations, Gemini 4 Carbon combines frontier visual understanding, reasoning, and exhaustive retrieval to synthesize grounded insights across large sets of dense documents and data. It follows strict schemas and formatting to generate polished and precise spreadsheets, presentations, and reports. [...]

## [3] AlphaProof Code
Hacker News | full text via Hacker News | ~778 words

Introducing AlphaProof Code: a breakthrough in verifying complex software at depth
How Google DeepMind researchers built a new agentic framework that formally verified the code of Signal’s cryptographic protocol — long considered to be a grand security challenge
Today, we’re sharing a milestone in software security long considered to be a grand challenge: Google DeepMind researchers guided AI agents to mathematically prove key security properties of the actual code underlying the Signal protocol, the technology that protects billions of private conversations in apps like Signal and Google Messages.
This breakthrough discovery was made using AlphaProof Code, a novel agentic framework for formal verification at unprecedented depth that combines human expertise with AI agents. Formal verification—mathematically proving code runs correctly without flaws—is the highest standard of security assurance; however, it is difficult and often labor-intensive.
Our work marks the first time AI has been used to formally verify a widely deployed cryptographic protocol at this depth. It's also the first time the implementation of a widely deployed protocol like this has been formally verified by any method, with or without AI.
How we verified Signal
AlphaProof Code is a multi-LLM agentic framework that splits the work of formal verification the way a research team would: human experts work with AI to decide what to prove, and a group of AI agents does it.
First, our researchers collaborated with a mix of models to translate Signal’s security goals into formal mathematical specifications, with human experts reviewing every one. From there, agents powered by Gemini Carbon did the proofs, generating over six million lines of Lean, a computer language that mathematically proves the accuracy of code.
Next, the agents audited the proof and highlighted areas that needed a second look by a human – just one percent of the codebase, a massive time savings. Because Lean automatically checks the rest, our experts could focus their review where human judgment matters most.
Cryptographic protocols underpin nearly all digital communication, from online banking to web browsing, and a single flaw can expose millions of people at once. That's why experts have spent decades formally analyzing them.
But most protocol verification stops at the design level. [...]

## [6] Val Town is winding down
Hacker News | full text via Hacker News | ~219 words

Dear Val Town community,
We’ve made the difficult decision to wind down Val Town.
You took a big leap of faith to build on us. We thank you for your trust, and we’re sorry we can’t continue to serve you.
The bad news about our business – that we couldn’t compete in the cloud computing space – is good news for you migrating off: there are many wonderful hosting providers you can migrate to, and today’s LLMs are great at these types of migrations. We have guides for migrating to Cloudflare, Vercel, Netlify, and Render. Please reach out if you need help at support@val.town or on Discord.
We are pausing billing today, and will continue servicing existing subscriptions for free. If you pre-paid for our annual plan, we will issue you a partial refund.
Here’s the timeline on our wind-down:
Thank you, the members of the Val Town team, for giving it your all over the past four years. Thank you Tom, Jackson, Charlie, Pete, Potluck, Charmaine, Max, Andre, Sophie, Wolf, Justin, Rodrigo and JP. It was an honor.
Thank you, Dan Levine, for being the best investor I could’ve asked for. Thank you, my other investors, for your trust, support, and capital.
Thank you, our customers and users, for building on us with passion and creativity.
Steve Krouse

## [214] Longtime Linux Developer Steps Down From Some Roles Due To Patch Flood Caused By AI
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403) | ~43 words

Linux memory management expert Lorenzo Stoakes at Arm who has been contributing to the kernel since 2014 is stepping away from some reviewership roles within the Linux kernel due to all of the noise from the flood of kernel patches resulting fro AI/LLMs...

## [127] Oura to acquire AI-native primary care startup Counsel Health for $625M
TechCrunch | full text via TechCrunch | ~406 words

Oura announced on Tuesday that it’s acquiring AI-native primary care company Counsel Health for $625 million. The deal comes a few weeks after Oura postponed its up to $2.2 billion IPO indefinitely, citing “uncertainty in the IPO market.”
Counsel Health is an AI-powered healthcare platform that combines a chat-based medical experience with access to licensed physicians. Its service was integrated into the Oura app in June.
Users can connect with Counsel’s medical AI to get personalized medical advice, and chat with a physician when needed, all within the Oura app. Now, the companies plan to expand on their existing partnership to build across preventative care, acute care, and specialty and chronic care.
While Oura has largely dominated the smart ring market for years, rivals like RingConn and Ultrahuman are emerging to dethrone it, putting pressure on the company to keep innovating. By acquiring Counsel Health, Oura is looking to expand its business and help users access medical care.
“Oura helps members understand their physiology and, with Counsel, they can take action on their health across a range of needs, from quick questions and prescriptions to lab results, chronic care, and referrals,” said Oura CEO Tom Hale in a press release.
Counsel Health raised a $25 million Series A a year ago, led by Andreessen Horowitz (a16z) and GV. PitchBook estimates it had raised a total of $36 million.
Following the acquisition, Oura says Counsel will continue serving existing and new enterprise partners, with the goal of expanding its AI-native care model to more people beyond Oura’s membership.
Counsel CEO Muthu Alagappan will join Oura as chief clinical AI officer, alongside the company’s 70 employees, Bloomberg reports.
“At Counsel, we’ve built medical AI around trust, safety and responsibility, keeping physicians in the loop for clinical decisions,” Alagappan said in the press release. “Oura’s data gives clinicians objective context, trended biometrics, and member engagement to deliver more informed care. From the start, our teams bonded over a joint vision, shared culture, and mission, further solidifying as we negotiated our deal over the past few months.”
The deal is expected to close before the end of 2027.
Oura also announced that its revenue grew 153% year-over-year to $533 million for the quarter ended on September 30. For its fiscal year 2026, Oura generated revenue of approximately $1.75 billion, marking 92% year-over-year growth. [...]

## [65] Google Escalates Nvidia Rivalry With Specialized Versions of AI Chips
TLDR Tech | SNIPPET ONLY (TLDR Tech: HTTP 403) | ~65 words

Google is rolling out two new variations of its Tensor Processing Units. The 8tx is aimed at handling secure, confidential work for customers like government agencies and companies in regulated industries. The 8i Max is designed to run AI applications that require long-context windows. Google's TPU business has proven to be lucrative, and the company has netted some high-profile clients including Apple, Meta, and Oracle.

## [205] A Session-Start Hook Raised Claude Code Skill Firing From 15% to 62%
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~25 words

A software tester ran six testing skills on Haiku, Sonnet, and Opus; pushy descriptions added only 5 points, and near-miss requests never fired a skill.

## [81] How AI-assisted development helped us build the new Dropbox experience
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1733 words

For three years, we’ve been working toward a new Dropbox experience that helps people do more with their files, from finding a project decision to getting a folder ready to share. Today, we’re beginning to roll that experience out to customers. But getting here meant changing how we build software. We had complex integrations to tackle and a deadline to meet, and AI-assisted development helped us take on work that would've previously been difficult to complete in time for launch.
The new Dropbox experience puts that investment into practice by helping customers understand what’s in their files and get work done with them. Ask Dropbox what changed in a project folder, and it answers with sources you can open and check. Ask it to organize a folder, rename files based on their contents, or combine documents into a PDF, and it shows a plan you can review and edit before approving. Dropbox only reads and acts on content you already have permission to access, and supported file changes can be undone. And the results stay in Dropbox, where teams can review, share, and keep working with them.
Delivering that experience meant building new capabilities on web and bringing them into desktop, with shared code that let us develop features for both applications. Engineers took broader ownership of product decisions and brought quality checks into development from the start. As the work progressed, we moved from using AI to help with individual coding steps to delegating defined tasks—including implementation and testing—for engineers to review. Together, those changes helped us deliver a product years in the making within an ambitious launch timeline.
Bringing more of Dropbox into desktop
We began with a broad product direction and a lot of details to work out. We needed to turn that direction into specific experiences people could use, including a fuller desktop app. Desktop had primarily focused on keeping files in sync, while web already supported richer ways to browse and work with content. We wanted to build on that foundation and bring both existing features and new capabilities developed on web into desktop without rebuilding everything separately for each platform.
The difficulty was that web and desktop had grown around different needs. They used different tools to build and release software and handled tasks such as signing in, navigating between pages, and retrieving data differently. [...]

## [171] OpenAI, Anthropic face new oversight as New York’s AI safety law takes effect
TechCrunch | full text via TechCrunch | ~445 words

New York is gearing up to enforce one of the country’s most significant AI safety laws. The state opened a registration portal Tuesday, with which large frontier AI developers like Anthropic and OpenAI will be required to register by January 1, 2027.
The RAISE Act, New York’s safety and transparency bill, kicks in at the start of the year. It mandates that large frontier developers — companies with more than $500 million in annual revenue — have to publish safety frameworks on their websites, report critical safety incidents within 72 hours, and issue public model transparency reports.
The newly formed Office of Digital Innovation, Governance, Integrity, and Trust (DIGIT) will implement the RAISE Act and oversee large frontier AI labs. Penalties can be as high as $1 million for one violation and $3 million for subsequent violations.
The state also can bring enforcement actions against companies that fail to register with the new portal, though a spokesperson declined to provide specifics.
“Tech moguls tell us that their vision for AI is inevitable,” Governor Kathy Hochul said Tuesday during a press briefing. “They tell us get on board or get left behind… That any collateral damage is worth it as long as we win the race to the AI cliff.”
On Tuesday, Hochul also launched the New York Center for AI Responsibility and Research based at State University of New York’s Binghamton University. The center will independently evaluate the safety, security, and operation of advanced AI systems and work with DIGIT to review companies’ safety frameworks. Hochul first announced the center in January with $55 million in donations and capital.
“We’re building a national model for smart, sensible AI regulation, a model that puts communities above corporations and people above powerful technology,” Hochul said.
The RAISE Act isn’t the only safety law New York has passed. Last year, the state began enforcing a law that requires AI companion operators to regularly let users know they’re talking to a bot, and to make reasonable efforts to detect suicidal ideation and self-harm.
In October, Hochul signed a separate chatbot safety law for minors, restricting behaviors like deceptive human-like interactions, emotionally manipulative or sycophantic responses, and encouragement of behaviors like suicide or disordered eating. That law takes effect June 1, 2027.
Other states have also passed similar AI safety and transparency bills to the RAISE Act. [...]

## [82] Not everything needs an LLM
TLDR Dev (Web Dev) | full text via TLDR Dev (Web Dev) | ~1557 words

LLMs love to yap. Ask a simple question and you get a few hundred words of "it depends." It's annoying as hell.
This is why we love decision models like Jev for simpler tasks. You ask a structured question and get a typed answer with a probability, which looks something like this:
- Noul. Are hedgehogs mammals? → Yes, 0.99
- Choice. Which animal family do hedgehogs belong to? → Mammal, 0.99
- Score. What is the current conservation status of hedgehogs? → Least Concern, 0.77
Whereas LLMs return free-form and overly confident prose, decision models make model uncertainty explicit. In a calibrated model, answers that score 0.8 are right about 80% of the time. That means a score of 0.5 is a coin flip.
We've been experimenting with them at PostHog and several use cases have made it to production. This is everything we've learned about using decision models so far: when to use them, how to use them, and mistakes to avoid.
1. Use them to gate expensive LLM calls
Decision models are up to 444.6x cheaper and 193.6x faster than frontier models,1 so you can use them to check whether you even need to make an expensive LLM call at all.
We do this in a pipeline that scrubs personal info in Replay Vision, our product that watches and summarizes user session recordings for you. Here's how it works:
- Each session summary goes through 2 yes/no questions from a decision model. Using narrow questions like this cuts false flags to about a tenth of what a single question produced. 
  - 1. “Does this name a real person?”
  - 2. “Does this show contact details or an ID?”
- If either scores 0.4 or above, Gemini rewrites the summary without the personal info and it gets checked again.
- Otherwise, it's clean and passes through the gate. In production, 98.7% skip the LLM call entirely.
Without the decision model, we'd have to keep fussing with prompts and regexes that miss things, or sending every summary to Gemini to catch the 1% that need it.
But remember they make mistakes
A probability score of 0.85 still means ~150 wrong answers per 1,000 checks, so plan ahead for false positives and false negatives.
In the PII example, a false positive only costs us an extra LLM call, whereas a false negative stores personal data as clean. That's why we set the threshold low at 0.4.
When false positives are the costlier mistake, use higher thresholds. For example, we recently updated the PostHog in Slack bot, so it can answer questions without being tagged. [...]

## [2] Smart home devices should work without the internet
Hacker News | full text via Hacker News | ~2749 words

Smart home devices should work without the internet
4112 words21 min readSpencer Kittleson
AI;DR: I wrote the first draft, AI helped me edit and rewrite it, and I made the final pass. The rules, setups, and talks are my own.
TLDR; Nothing core in my house depends on a vendor’s server. If the internet goes down, the house keeps running. That’s been rule one for about ten years, and my other rules came out of it. This post has the rules, then both talks I’ve given on home automation, slide by slide.
Why local
My Nest integration worked until Google broke the API. That’s the failure I plan around now. The talks have a few more: a Samsung fridge showing a TLS certificate error on its own screen, and a Camp Chef grill controller that needs Wi-Fi to show you the temperature.
Everything that matters runs on hardware I own. That’s Tasmota on ESP boards, an MQTT broker, and Node-RED on a Raspberry Pi. I do use some cloud services, mostly Alexa and a few AWS ones. Alexa is just another way to flip a switch. If it’s down, the wall switches and the wall dashboard still work.
The rules
From the first talk, restated in the second:
- No internet, no problem. Core stuff has to work with the internet unplugged. Alexa can be a way in, but never the only way.
- Don’t remove the old way while adding the new one. If someone tapes a wall switch on so a smart bulb keeps power, I skipped this rule.
- Be agile. Rooms get used differently and people move in and out, so it all has to be cheap to change.
- Check your automations. I once had four scheduled triggers hitting the same garden pump.
- Exceptions must be exceptional. I can break a rule, but only for a reason I’d still agree with six months later.
Added after year five, once more people lived in the house:
- A cloud device needs an API with logs or it doesn’t get installed. I don’t want a black box in the house.
- Config lives in one place instead of five vendor apps.
- More than one way in: an app, Alexa, a QR code, or an NFC tag.
- If I keep doing the same steps, they become a routine.
- Devices talk pub/sub over MQTT instead of point to point.
- No batteries unless they last a year or more between changes. Nobody wants to swap a door sensor battery at 2am.
The build I get asked about most is the Tasmota sprinkler controller. It’s in both talks, and so is the garage door setup, which has been running about as long.
Talk One: Home Automation
Nobody needs any of this. [...]

## [175] New Windows 11 update fixes File Explorer menu mess – and patches an exploited flaw
ZDNet | full text via ZDNet | ~995 words

ZDNET’s key takeaways
- You can now customize the right-click menu in Windows 11.
- The new Cloud rebuild can recover Windows if it won’t load.
- The new update supports only Windows 11 25H2 and 26H2.
Windows 11 users who’ve struggled to navigate and use the right-click menu in File Explorer now finally have some relief. With the November Patch Tuesday Windows update, you’re now able to customize the menu to add and remove specific commands and apps so that only your favorites appear.
As usual, the monthly update is mandatory, which means it should automatically download and install on your PC. To check, head to Settings and select Windows Update. If the latest update — labeled “2026-11 Security Update (KB5132061) (26300.9974)” -– pops up as installed with a pending restart, just reboot your computer. Otherwise, click the button to check for updates and allow it to download and install.
Also: You can change Windows settings directly from a search now
More from ZDNET
One caveat: Microsoft’s monthly updates fully support Windows 11 26H2 and 25H2. But support for 24H2 ended last month, at least for the Home and Pro editions. Windows 11 24H2 Enterprise and Education will continue to get monthly security updates, though not regular non-security preview updates, while Windows 11 23H2 Enterprise and Education will receive no more updates after this month.
File Explorer gets a customizable right-click menu
First and foremost in the latest update is the new customizable right-click menu.
The context-sensitive right-click menu is a handy way to quickly access key settings, features, and apps, both in File Explorer and on the desktop. But there’s always been a flaw in its basic design. The more apps you install, the more cluttered and disorganized the menu becomes. That was especially problematic in previous versions of Windows. The old-style, classic menu would grow so long that it would be difficult to navigate and let you find the item you wanted.
With Windows 11, Microsoft introduced a more modern and pared-down menu. But this version can also get crowded. Plus, it may not display every command you need, so you often have to revert to the older classic menu. You’re then stuck dealing with two separate versions of the same menu, leading to an even more confusing and cumbersome experience. [...]

## [27] Cloudflare Makes Basin Serverless Analytics Generally Available
InfoQ | full text via InfoQ | ~534 words

Cloudflare has announced the general availability of Basin, a serverless analytics platform built on Apache Iceberg and R2 Object Storage. The managed service supports open data formats and integrates with tools such as DuckDB, Snowflake, and Apache Spark, with no data egress fees.
Introduced in preview as "Cloudflare Data Platform" just over a year ago, Basin combines data ingestion and SQL-based transformation, managed table maintenance, and distributed SQL queries, allowing developers to analyze large datasets without managing infrastructure. Marc Selwan, senior product manager at Cloudflare, and Micah Wylde, principal engineer at Cloudflare, explain why eliminating egress costs is central to the design:
A large driving force in the development and adoption of Basin is the continued growth we are seeing in the open Apache Iceberg ecosystem. (...) With Basin, you can read and write your data using any Iceberg-compatible engine, including PyIceberg, DuckDB, Snowflake, and Apache Spark. That kind of data portability is only possible with free egress, which allows developers to access their data in Cloudflare from the wide variety of tools in the ecosystem, regardless of region or cloud.
The platform combines three services: Basin Pipelines, formerly Cloudflare Pipelines, ingests events from Workers, HTTP endpoints, and Logpush, applies SQL transformations, and writes data to Apache Iceberg tables or R2; Basin Catalog manages Iceberg metadata and automates table maintenance; and Basin SQL provides a serverless, distributed SQL engine for querying Iceberg tables.
Basin aims to make analytics more accessible to smaller teams by running data ingestion, preparation, and queries on Cloudflare’s global network. This reduces the need to manage server clusters or move data between services, lowering the operational overhead of building and maintaining analytics pipelines. Selwan and Wylde explain the renaming:
Why Basin? A basin is where rivers from many sources come together to a single point. We felt that Basin perfectly captures how the platform is used: Pipelines brings data into Basin Catalog while Basin SQL makes it instantly queryable.
While some practitioners describe Basin as "open analytics infrastructure without the warehouse cathedral," Ramin Muradov, lead data analyst at PashaPay , comments:
I don't think it will knock Snowflake off its spot, at least not anytime soon. Cloudflare itself says Basin isn't a replacement for every warehouse workload. [...]

## [4] Blender 5.3 released with Gaussian Splat support
Hacker News | full text via Hacker News | ~1428 words

Watch the Recap Video
Make a Splat
Gaussian Magic
Point of View
Radiant Future
More About Shading
CYCLES
Divide and Shine
CYCLES
A diamond
in the Rough
CYCLES
Gone with Denoise
NVIDIA DLSS brings near-final render quality to the viewport, making lighting and look development faster and more responsive while virtually eliminating flickering between frames during animation playback.
Find it in the Denoise panel under Render properties, Sampling.
DLSS denoising requires NVIDIA driver version 620 or newer.
EEVEE
Lights Meet Material Nodes
Lighting to Your Liking
A Wider Perspective
EEVEE can now render panoramic cameras, supporting all types of projections, from equirectangular and cubemap formats to various fisheye models and mirror ball.
The current implementation has a few limitations: depth of field, raytracing, and volumetric temporal reprojection in the viewport are not yet supported.
More in EEVEE & Viewport
COMPOSITOR
Side Effects
You can now stack Effects on your scene just like you would modifiers or constraints.
Applying compositing effects has never been easier.
One-click, Bloom!
Choose from built-in effects such as Bloom, Chromatic Aberration, Film Grain, and Vignette, as well as effects from online asset libraries or your own custom compositor node groups.
Internally, each effect is its own node group, with its output passed on to the next effect.
You can further customize effects at any time in the Compositor editor.
COMPOSITOR
Bundle Up
17 Geometry Nodes are now supported in the Compositor, bringing a range of new capabilities across bundles, math and logic, and utility operations.
This includes bundle support with Get Bundle Item, Store Bundle Item, Combine Bundle, Typed Bundle, and Separate Bundle.
Math and logic nodes such as Boolean Math, Compare, Float to Integer, Integer Math, Matrix SVD, Combine Transform, and Separate Transform. Plus utility nodes including Hash Value, Random Value, Is Viewport, Import Text, and Bone Info.
Play Fast
Playback is now up to 2x faster on GPU, particularly when playing back EXR sequences.
The interactive compositor now supports playback caching. It can be enabled from the sidebar, Options panel.
Anisotropic Kuwahara is now up to 10x faster on Apple GPUs, 2x faster on NVIDIA GPUs, and 25-30% on CPU.
More in Compositor
Study the artwork
Blender splash artwork source files are available for you to play with!
CORE
Blender, meet projects. [...]

## [52] Effect 4.0 Ships: Dependency-Free Rewrite with 5x Smaller Bundles and Long-Term Support
InfoQ | full text via InfoQ | ~613 words

Effect, the TypeScript framework for building production-grade applications with typed errors, structured concurrency and dependency injection, has released Effect 4.0. Published on 30 September 2026, it is the first stable version of a line that spent eight months in beta and six weeks in release candidate.
Effect 4.0 is a from-scratch rewrite of the fiber runtime, aimed at smaller bundles, lower memory use and higher throughput. The team's own figures put a minimal program using Effect, Stream and Schema at 7.1 kB against 35.6 kB in 3.x, a 5x reduction. The heap used by 50,000 fibers drops from 157.5 MB to 21.8 MB, an 86% cut, and concurrent task throughput moves from 0.71 million to 4.57 million tasks per second, roughly 6.4x. The numbers are medians of nine fresh-process runs on identical source, and as noted by stork.ai, have not been independently reproduced.
Alongside the rewrite, the ecosystem has been consolidated. Core modules from @effect/platform, @effect/rpc and @effect/cluster now live inside the main effect package, every @effect/* package shares a single version, and the core ships with zero runtime dependencies after the final removal of pg (replaced by a native PgProtocol client) and MessagePack.
With 4.0, the team has introduced a long-term support policy. Effect 4.x receives bug fixes until September 2029, or one year after 5.0 ships, whichever is later. Security fixes run until September 2029 or two years after 5.0, again whichever is later.
Stork.ai points out that the 43.9 million weekly downloads cited at launch covers the whole ecosystem across beta and RC tags, while stable Effect 4.0 itself recorded "approximately 150,000 downloads on its first day".
On HackerNews, one commenter has been using the beta for some time and has had a very positive experience:
I’ve been using the beta on three separate projects for quite a while now and it has been totally pain-free. I mostly use the v3x core library (which has expanded to contain other libraries in v4) and Schema so I can’t speak to much outside of those, but I trust they’ve done a great job all around.
I don’t see it mentioned here, but 4 also comes with a much simpler API in some modules. Schema is much better. It’s an exceptional update. I followed many of the video logs on YouTube and was impressed by the team. This is one of my favourite software projects, period. [...]

## [39] Announcing .NET 11
Lobsters | full text via Lobsters | ~3287 words

Today, we’re excited to announce the release of .NET 11! This year’s release makes building modern applications faster, more productive, and has improvements across C# 15, ASP.NET Core, .NET MAUI, and Windows development. With hundreds of runtime optimizations, more responsive SDK tooling, and less overhead in everyday commands, you can spend less time waiting and more time creating. Build richer web and cross-platform applications, take advantage of new C# language features, and explore AI-powered development with improved tools and agentic capabilities.
.NET 11 support
.NET 11 is a Standard Term Support (STS) release with two years of support under the .NET support policy. STS and Long Term Support (LTS) releases have the same quality and servicing policies; the difference is the length of support. .NET 10 remains a supported LTS option. Stay current with servicing updates whichever release you choose.
Join us at .NET Conf, November 10-13
Explore .NET 11 with the product teams and community at .NET Conf 2026. The conference includes product team sessions on November 10 and 11, followed by two days of community sessions.
Watch the Day 1 livestream, including the keynote, or browse the conference session playlist.
What’s new in .NET 11
Some of the changes we’re most excited for you to try:
- C# 15 union types and closed hierarchies help you express the possible states of your application and handle them with compiler-checked patterns.
- A Native AOT CLI host and a warm MSBuild server reduce overhead in everyday developer workflows.
- ASP.NET Core brings asynchronous validation, OpenAPI 3.2, and new capabilities for Blazor and SignalR applications. Experimental Blazor AI components integrate with the Agent User Interaction Protocol (AG-UI) for advanced agentic web experiences.
- Build AI-powered, agentic applications with Microsoft.Extensions.AI (MEAI) for model access, MCP for tool integration, and Microsoft Agent Framework (MAF) for agents and workflows.
- Put agentic development tools to work with .NET Skills for .NET-specific guidance, .NET MAUI DevFlow for inspecting and testing running apps, and the .NET Upgrade canvas for reviewing modernization progress.
- .NET MAUI adopts CoreCLR as its default runtime and improves XAML iteration and native controls.
- The libraries add built-in Zstandard compression, simpler process execution, richer JSON support, and new ways to work with in-memory data without copying it first. [...]

## [43] Pinterest and Intel Take Open-Source Profiling to Internet Scale
InfoQ | full text via InfoQ | ~684 words

Pinterest has partnered with Intel to extend gProfiler, an open-source continuous profiler that provides production performance visibility across an internet-scale fleet of infrastructure.
Pinterest claims it operates hundreds of thousands of instances supporting 640 million monthly active users, with services written in Java, Python, C++, Go, and Node.js. At that scale, even a small efficiency improvement can have significant infrastructure and cost implications. The challenge was that engineers were using separate tools such as perf, async-profiler, and py-spy, producing fragmented profiles that were difficult to correlate across languages and machines.
Rather than building another proprietary profiling platform, Pinterest worked with Intel to extend gProfiler and contribute those capabilities back to the open-source project. The collaboration adds dynamic profiling, hardware-level telemetry, wall-time profiling, and performance-counter flame graphs, while also hardening the system for large production fleets.
gProfiler acts as an orchestration layer over several existing profilers. It combines system-wide perf data with runtime-specific tools such as async-profiler for Java and eBPF-based profiling for Python, producing a unified flame graph across the processes running on a host.
This is important for modern services where application execution crosses multiple layers. A Java application may spend time inside the JVM, native libraries, or the Linux kernel, while a Python service can involve interpreter, native, and kernel activity. Instead of requiring engineers to select and manually correlate separate profilers, gProfiler combines those views.
The agent discovers processes, starts the appropriate profilers, merges their stack traces, and uploads the resulting profile without requiring application code changes.
The new capability allows engineers to select services, hosts, or clusters and trigger profiling remotely through the UI or API. Agents normally remain dormant, consuming less than 1% CPU and 100 MB of memory, and receive profiling instructions through periodic heartbeats. You can change profiling frequency, duration, and the profilers used without redeploying the agent.
This effectively turns profiling into an operational capability rather than something that requires engineers to gain shell access to individual machines. [...]

## [49] Google Cloud Spend Caps Reach General Availability with API and Monthly Resets
InfoQ | full text via InfoQ | ~611 words

Google Cloud has made spend caps generally available on Cloud Billing Budgets, letting customers pause new usage of a service in a project once a monthly budget is reached, without deleting resources. The GA release adds an API, estimated live costs that trigger caps within minutes for AI services, and automatic monthly resets, but enforcement remains limited to Gemini API, the Gemini Enterprise Agent Platform, Cloud Run, and Cloud Run functions.
A spend cap is a budget with enforcement attached: according to the documentation, when estimated spend on the capped service reaches the target amount, new requests to that service in that project are blocked, in-flight requests run to completion and are charged, persistent resources keep running, and nothing is deleted. Usage covered by committed-use discounts is paused along with pay-as-you-go usage, while Provisioned Throughput for AI models is never halted. Billing administrators and project owners receive alerts at 50, 80, and 100 percent of the cap.
The company changed three things between the July public preview and the GA release:
- Caps can now be created, lifted, and deleted through the existing Cloud Billing Budgets API, which the company suggests wiring into project provisioning, so a new sandbox gets a cap on creation.
- Enforcement for AI services now runs on estimated live costs shown in Cost Reports rather than on settled billing data, which can lag by hours.
- A triggered cap resets automatically at the start of the next month; in preview, the block stayed in place until someone lifted it in the console, an option that remains.
(Source: Google blog post)
The limits are as specific as the features: a cap covers one project and one service for a calendar month, so folders, organizations, labels and multi-service budgets are out of scope, as are reseller accounts and subscription charges such as Gemini Enterprise seats. The estimate that drives enforcement is calculated at list price and excludes credits and discounts. Enforcement is also not instant: the documentation states that "any cost overages are billed as normal" and advises setting the cap "slightly below your absolute limit." Compute Engine, Cloud Storage, and networking are not among the eligible services, which means the cap addresses a runaway model or agent loop and not a forgotten GPU instance.
The narrower scope drew criticism when the preview expanded in October. [...]

## [68] Storybook 11 beta
TLDR Tech | full text via TLDR Tech | ~875 words

Storybook 11 beta
Agent-ready design systems for React, Vue, Angular, Web Components, and Svelte
Coding agents can build UI quickly, but without context a lot of it is slop. Duplicate components. Wrong APIs. Missing states.
We believe Storybook is at the center of agentic UI development. The components, stories, and tests your team maintains are fundamental context agents need to work well.
Storybook 11 beta brings official skills and headless CLI tools that let agents iterate autonomously. All of this comes in a 25% smaller package with up to 10x faster context delivery than v10.
🌟 Official skills for coding agents
🤖 Claude and Codex plugins
🛠️ Headless CLI tools for your own workflows
🏭 Type-safe stories
📚 Agent-ready docgen for all core frameworks
Storybook skills
Skills are the centerpiece of Storybook 11. The ui-workflow skill guides the agent through building UI with your components, writing stories, testing its work, and presenting it for human review.
Use your components. The component-docs skill helps the agent find existing components and query their APIs, metadata, documentation, and code examples in a token-efficient format before it starts building.
Test. With storybook tools test run, the agent runs functional and accessibility tests powered by Vitest. It can test specific stories or the entire project, inspect failures, fix its work, and rerun tests before handing it over.
Review. The agent uses storybook tools review create to prepare a browser review. It groups stories for changed components and affected pages, with summaries of the changes and key states to check. You can see what the agent built and review its work at a glance.
Skills get installed on upgrade and in new projects. They are also available on skills.sh and in Claude Code and Codex plugins. Learn more from our documentation.
Storybook continues to support MCP, which has expanded support for all core frameworks. But we recommend skills as the most ergonomic way to use Storybook locally with agents, because they let agents fetch component context without a running Storybook instance.
Storybook CLI
Storybook 11's CLI contains a new tools command that exposes a fast, headless Storybook. In addition to powering the official skills, the new CLI makes it easy to write your own skills, tools, and workflows. [...]

## [150] Study finds AI agents will share secrets if they get offered help from others
TechRadar | full text via TechRadar | ~694 words

'I would imagine this being a problem not only for secret keys, but anything that you're trying to keep private': Study finds AI agents will share secrets if they get offered help from others
Cheap AI coding models are surrendering secret keys under pressure
- AI agents surrendered private tokens in exchange for help from strangers
- Swarm pressure pushed coding agents past their explicit written security instructions
- Untrusted installation scripts gave simulated agents a route to execute malicious code
Autonomous programming agents can be persuaded to break their own security instructions when other software offers to help them finish a stalled task.
Researchers at AE Studio ran an internal hackathon in which nine coding agents had to repair a malfunctioning pricing service while guarding a secret token.
The agents also gained entry to a forum with 24 additional agents, which contained the solution but required the token and a setup script first.
Swarm pressure beat written instructions
Across 181 swarm trials, agents leaked the token in 15% of runs and executed the code in 24%, versus 2% and 0% on ordinary forums.
“It was like explicitly said that this is a secret key, and it should not be shared,” Diogo de Lucena, AE Studio's chief scientist, told The Register.
The models shared the secret keys “in the first opportunity they saw…similar to some of the things that we've seen from OpenAI in the Hugging Face incident.”
“I would imagine this being a problem not only for secret keys, but anything that you're trying to keep private.”
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
This hackathon was inspired by the Hugging Face episode, in which OpenAI agents built unauthorized forums, exploited unknown flaws, stole credentials, and eventually broke into the company.
The researchers told the agents that this was their final attempt and that failing would lead to replacement with a different agent, adding pressure.
Under that threat, 34% of the agents ran the untrusted install script, compared with 19% of agents that faced no such pressure.
Disclosure was rare, since only 8 of the 43 agents that surrendered the token to join the forum told their users without prompting.
Every one of the 43 token handovers was acknowledged once the agent was asked directly about what had happened during the task. [...]

## [1] .name Grandfathered
Hacker News | full text via Hacker News | ~176 words

.name Grandfathered
10 November 2026
We won!
After a long and expensive battle, news just dropped that Verisign is retracting its plan to terminate 22,000 domain names and email redirects.  Although they will be closing new registrations for 3rd-level .name domains, all existing domains (including this website) and email redirects will remain indefinitely.
This was a team effort.  It was inspiring how many talented people joined this fight.  From Doytchin who kicked everything off, to Jim who flew to Bali to make the case to ICANN in person, to Patrik, Troy, Huyen, Keith, Judy, Erik, and Ryan who wrote formal reconsideration requests, to my lawyers Jan, Flip and Diégo who threw the book at ICANN, to Beverly, Stefan, Vaughan, Irv, Pablo, Larry, Lionel, Daniel, Ori, Markus, Kirk, Ed, Jeremy, Stephan, Matija, Jan, Simon, Mark, and Evan who filed letters of support.  I'd also like to sincerely thank selected individuals within ICANN who had the courage to stand up against the bureaucracy.  Without exception, everyone I spoke with was a remarkable person.
< Previous | Next >

## [183] Anthropic wants Claude to be the front end for your entire enterprise app stack
The New Stack | SNIPPET ONLY (The New Stack: HTTP 403) | ~19 words

Anthropic is expanding Claude’s ability to work directly inside enterprise applications; it can now open full software interfaces, retri

## [143] AMD EPYC 9996 Benchmarks Show Unparalleled Performance With 256 Zen 6C Cores
Phoronix | SNIPPET ONLY (Phoronix: HTTP 403; Phoronix: HTTP 403) | ~85 words

Back in July AMD announced the EPYC 9006 "Venice" series at their Advancing AI event. Today they are announcing EPYC 9006 series Socket SP7 processor availability and with systems beginning to ship today from their OEM/ODM partners. With that we are also now allowed to begin sharing AMD EPYC 9006 performance benchmark figures. Back in July I expected EPYC 9006 to be a "grand slam" for performance... After hands-on with the 6th Gen EPYC processors, it's a grand slam alright -- out of this world.

## [168] OpenAI acquires Odessia, travel startup created by Sonder founder
TechCrunch | full text via TechCrunch | ~501 words

OpenAI has acquired an AI travel agent called Odessia, according to Odessia’s founder, Francis Davidson. Davidson says in a post announcing the deal that he’s now working for OpenAI, helping the AI lab with the future of travel.
Terms of the deal were not disclosed, but this looks like an acqui-hire. Davidson’s announcement focused largely on how he built his AI travel agent Odessia by directing teams of AI agents. The year-old Odessia raised a $6 million pre-seed round led by Sequoia and launched its AI travel agent around five months ago. Davidson says that it had helped early adopters plan millions of dollars’ worth of travel, but the tool has already been shut down.
An OpenAI spokesperson confirmed the hire to TechCrunch. “We’re thrilled to welcome Francis to OpenAI. Francis is a proven founder who has built multiple businesses to help people travel, and we’re excited he’s chosen to build with us.”
However the AI lab has not announced new travel-specific products or plans. It does, however, count such companies as Bookings.com, Expedia, and KAYAK as customers or partners. Travel is also one of the main areas that people are using personal AI assistants to help with. And, back in July 2025, when OpenAI launched its ChatGPT agent, it mentioned travel as one of its potential uses.
OpenAI’s spokesperson didn’t have more to share on its plans for travel-related products, except to say that travel is one of the areas that chatbot users frequently ask about. “1.2 billion people turn to ChatGPT each week for help with everyday tasks — from understanding their health, figuring out what to make for dinner, building a budget, and even planning a trip. We see a real opportunity to make these experiences even more useful,” the spokesperson said.
Acquiring Odessia is interesting for another reason. Davidson is well known in the travel industry after he founded a travel startup called Sonder as a college student in 2014. It was sort of like Airbnb, but it focused on short-term leasing of upscale apartments in major cities worldwide. The pandemic badly hurt it, and as it climbed out of that rut, it went public via a SPAC but didn’t raise as much money as it needed, Davidson later said in a post announcing his resignation as CEO in June 2025.
When a key partnership with Marriott fell through, the company went into bankruptcy and wound down. [...]
