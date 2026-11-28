---
date: 2026-11-28
edition: 67
schema_version: 1
generated_at: 2026-11-28T01:37:15+00:00
sources_ok: 42
sources_total: 47
fetched: 386
candidates: 160
full_text: 15
---

# The Brief

- Security dominated the day: a card skimmer hidden in a marketing pixel ran on five retail sites before Black Friday, the Air Force reported a breach of its Cloud One platform, a game-logging site lost user credentials, and Australia passed a duty-of-care law for platforms.
- AI chip export controls are biting. Nvidia has paused server shipments to four Southeast Asian countries after the U.S. closed a loophole that let Chinese companies use its chips remotely.
- The AI tooling stories all point the same way: test before you adopt. A benchmark of Code Mode, a speculative-decoding result that slowed uncached agent loops, and an analysis suggesting OpenAI's newest models were tuned to reason less each argue for measuring on your own workload.
- Automated approval is moving into code review. PyTorch's GreenLight brings the approach Meta uses internally into open source, with narrow gates and a reject window.
- OpenAI and Apple have turned their trade-secret fight into a two-way lawsuit, with mirror-image accusations now headed to court.

# Stories

## A card skimmer hidden in a marketing pixel ran on five retail sites before Black Friday
- ids: 2
- topic: Security
- signal: must-read
- url: https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer
- event: webrtc card skimming retail sites
- original title: Credit card skimming scripts using WebRTC found on popular shopping sites
- source: infohawk.com | https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer | via Hacker News
- image: https://www.infohawk.com/_app/immutable/assets/2026-11-27-black-friday-webrtc-skimmer.BQAmEGg5.png
- read: 7 min
- discuss: https://news.ycombinator.com/item?id=50668145 | Hacker News | 420 points | 222 comments
- full text: yes

> The script was built to take card details and personal information as shoppers typed them, before the store had checked the payment.

A security research team uncovered a skimming script that had been inserted into five retailers' storefronts, Lascana, Samsonite, American Tourister, Revolve and FWRD, during the days leading into Black Friday. The team reported the sites to the affected companies on November 24, and all five had removed the script by November 24 or 25. Revolve confirmed that it had been notified on November 25 and was still investigating what impact there had been.

The skimmer is the dangerous part. On Lascana the researchers watched it send their test card's details to a third party. The script appears designed to collect the card number, expiry date, security code, name, address, phone number and email as the shopper entered them. It ran before the store checked the payment, so a card could be captured even when the order was later declined or cancelled, and nothing on the page would look wrong.

On Lascana the malicious code sat inside Quorum, an ad-attribution pixel, and Quorum says it removed the code and restored a clean pixel by November 24. The technique relies on WebRTC, the browser technology behind video calls, which gave the script a side channel for moving the data out. The researchers say they cannot tell how many shoppers' details or card numbers were taken.

**Takeaways**
- If you bought from any of these five sites in the week before Black Friday, check your card statements and ask your issuer to reissue the card if anything looks wrong.
- If you run a store, list every third-party script on your checkout pages and confirm each one is still needed, starting with marketing pixels.

## Hackers reportedly reached the Air Force's Cloud One control plane
- ids: 111
- topic: Security
- signal: must-read
- url: https://www.engadget.com/2329586/hackers-reportedly-infiltrated-the-air-force-cloud-systems/
- event: air force cloud one hackers breach
- original title: Hackers reportedly infiltrated the Air Force's cloud systems
- source: Engadget | https://www.engadget.com/2329586/hackers-reportedly-infiltrated-the-air-force-cloud-systems/
- author: Kris Holt
- image: https://www.engadget.com/img/gallery/hackers-reportedly-infiltrated-the-air-forces-cloud-systems/l-intro-1795798468.jpg
- read: 2 min
- full text: yes

> Reuters reports the intruders exploited a vulnerability during upgrade work, and some Air Force projects are now on hold while Cyber Command reviews the incident.

Hackers gained access to Cloud One, the Air Force's cloud computing platform, according to Reuters, which first reported the intrusion. The breach was found within roughly the last month during system upgrade work. It is not clear who was behind it or what data, if any, was taken, and the Air Force has not commented on specifics.

A person familiar with the matter told Reuters that the attackers exploited a vulnerability to reach the platform's control plane. That person compared the access to a universal remote, one that could in principle check the operational status of military aircraft or track spare parts, though it is not known whether they actually did. Some users had their admin rights revoked, and updates to applications already running on Cloud One were prohibited, so staff could not apply fixes. The effort to move more mission applications onto the platform is paused.

Cloud One runs on Amazon Web Services, Google Cloud, Oracle Cloud Infrastructure and Microsoft Azure. It carries payroll and personnel data and the Theater Integrated Combat Munitions System, which tracks bombs and missiles across more than 200 Air Force locations. The breach comes weeks after reported intrusions at the FBI and USDA, and after reported breaches at the CIA and other spy agencies that exposed some classified information.

**Takeaways**
- If you administer a multi-cloud control plane, audit who holds admin rights and check whether any role grants changed during recent upgrade work.
- Treat the control plane as the most valuable target in a cloud estate: restrict its access paths and alert on every change made through it.

## Nvidia pauses server shipments to Malaysia, Singapore, Thailand and Indonesia
- ids: 136
- topic: Infra
- signal: must-read
- url: https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/
- event: nvidia southeast asia shipment pause
- original title: Nvidia hits pause on chip shipments to Southeast Asia
- source: TechCrunch | https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/
- author: Connie Loizos
- image: https://techcrunch.com/wp-content/uploads/2026/11/Taiwan-Nvidia.jpg?w=1024
- read: 1 min
- full text: yes

> The halt follows a U.S. rule that closed a loophole letting Chinese companies use Nvidia chips remotely from data centers in those countries.

Nvidia has told manufacturing partners, including Dell and Super Micro, to pause server shipments to Malaysia, Singapore, Thailand and Indonesia. The Wall Street Journal reports the pause has no set end date, and that Nvidia wants to assess whether its regional partners are meeting U.S. export requirements before shipments resume.

The reason is remote access. Chinese companies had been using Nvidia chips inside data centers in those countries, a route around export controls that the Commerce Department closed earlier this month. The Institute for Progress estimates that remote data centers of this kind supply about 24 percent of China's AI computing power. Nvidia's step puts its regional partners under scrutiny, not only the buyers who rented the capacity.

What is still open is how long the pause runs and how much regional server capacity it removes. Nvidia has not said which partners it considers out of compliance, and the report does not say.

**Takeaways**
- If you rent GPU capacity from a provider in these four countries, ask for written confirmation that it does not resell access to Chinese customers and when its next hardware delivery is due.
- Watch for a Nvidia or Commerce Department statement on when shipments resume, since the pause has no end date.

## OpenAI countersues Apple, accusing it of trade-secret theft and supplier coercion
- ids: 108
- topic: Startups
- signal: must-read
- url: https://www.engadget.com/2329747/openai-countersues-apple-and-accuses-it-of-stealing-trade-secrets/
- event: openai countersues apple trade secrets
- original title: OpenAI countersues Apple and accuses it of stealing trade secrets
- source: Engadget | https://www.engadget.com/2329747/openai-countersues-apple-and-accuses-it-of-stealing-trade-secrets/
- author: Lawrence Bonk
- image: https://www.engadget.com/img/gallery/openai-countersues-apple-and-accuses-it-of-stealing-trade-secrets/l-intro-1795808637.jpg
- read: 2 min
- full text: yes

> The filing names several former Apple employees and turns a one-sided lawsuit into a two-way fight over hardware talent.

OpenAI has filed a countersuit against Apple, according to the Financial Times, accusing the iPhone maker of stealing trade secrets and of coercing suppliers that work with both companies. The company calls Apple's conduct an attempt to compete unfairly, and says the methods include steering staff to keep work files on personal devices and accounts.

The complaint names several former Apple employees who allegedly downloaded dozens of confidential files, including information about unreleased products, engineering presentations, technical specifications and supplier data. That is close to what Apple alleged against OpenAI in its earlier suit, which followed OpenAI's acquisition of io, the hardware studio led by former Apple design chief Jony Ive. Apple has not yet commented on the new filing.

The fight matters because the two companies were partners until recently, when ChatGPT came to iPhones. OpenAI is now preparing its own hardware, which could compete directly with Apple's. Both suits will now go to court, where the claims will have to be tested.

**Takeaways**
- Watch for Apple's response and any court schedule, since both complaints describe former employees taking device files, and the evidence on that point will decide much of the case.

## Australia passes the Digital Duty of Care Act, requiring platforms to prevent foreseeable harm
- ids: 139
- topic: Security
- signal: recommended
- url: https://yro.slashdot.org/story/26/11/25/2326240/australia-passes-tough-legislation-requiring-big-tech-to-preempt-foreseeable-harms
- event: australia duty of care law
- original title: Australia Passes Tough Legislation Requiring Big Tech to Preempt Foreseeable Harms
- source: Slashdot | https://yro.slashdot.org/story/26/11/25/2326240/australia-passes-tough-legislation-requiring-big-tech-to-preempt-foreseeable-harms
- author: BeauHD
- full text: no

> Platforms could face fines of potentially billions of dollars if they fail to anticipate and reduce risks to their users.

The details in this story come from the article's headline and opening summary, because the full text was not available to us. Australia's Parliament has passed the Digital Duty of Care Act. It requires online platforms to identify and reduce foreseeable harms before they occur, rather than responding only after a problem is reported, and the penalties for failing to do so could run into billions of dollars.

According to the same summary, platforms have to catch and cut down on harmful material, and they must beef up safeguards for minors covering porn, self-harm and eating-disorder content. They must produce annual written risk assessments and disclose major design changes, such as endless scrolling, where those changes create new harms. The summary also says users will be able to opt out of algorithmic features, but the excerpt cuts off before the detail.

**Takeaways**
- If your platform serves Australian users, start an inventory of design features such as infinite scroll and autoplay now, since the first annual risk assessment will need them.

## Authors say Nvidia seeded pirated books over BitTorrent and shared them with Adobe
- ids: 118
- topic: AI
- signal: recommended
- url: https://yro.slashdot.org/story/26/11/26/0449255/nvidia-seeded-pirated-books-and-shared-them-with-adobe-authors-allege
- event: nvidia pirated books bittorrent adobe authors
- original title: Nvidia Seeded Pirated Books and Shared Them With Adobe, Authors Allege
- source: Slashdot | https://yro.slashdot.org/story/26/11/26/0449255/nvidia-seeded-pirated-books-and-shared-them-with-adobe-authors-allege
- author: BeauHD
- full text: no

> The authors allege the downloads came from shadow libraries, and that Nvidia's BitTorrent client uploaded pieces of the files to third parties.

The details in this story come from the headline and opening summary, because the full text was not available to us. Several book authors have filed an amended complaint accusing Nvidia of downloading pirated books from shadow libraries, including Anna's Archive and LibGen. The authors say Nvidia then seeded the files through BitTorrent, and that the books were also shared with Adobe.

According to the authors, Nvidia did not turn off uploading altogether. When its BitTorrent client ran, pieces of the pirated files went out to third parties. The parties agree that whether a client uploads depends on its settings, so the dispute turns on what the settings were.

**Takeaways**
- If your team trains models on scraped books, check whether any BitTorrent client ran on your data pipelines and what its upload settings were.

## Google will publish Android developers' phone numbers and addresses from March 2027
- ids: 129
- topic: Security
- signal: recommended
- url: https://www.engadget.com/2329389/google-will-soon-share-android-developers-addresses-publicly/
- event: google android developer addresses
- original title: Google will soon share Android developers' addresses publicly
- source: Engadget | https://www.engadget.com/2329389/google-will-soon-share-android-developers-addresses-publicly/
- author: Mariella Moon
- image: https://www.engadget.com/img/gallery/google-will-soon-share-android-developers-addresses-publicly/l-intro-1795772169.jpg
- read: 2 min
- full text: yes

> Developers who earn regularly from their apps must declare trader status by February 1, 2027, or risk having their updates blocked.

Starting in March 2027, anyone using a device will be able to see the phone number and street address behind each Android app's publisher. The change follows rules in the UK and the EU's Digital Services Act that require a trader declaration, which Google now also asks developers to make. Developers who intend to earn money from their apps on a regular basis must classify themselves as traders and submit their business identity, phone number and address.

Critics say the change puts home-based developers at risk. Some have rented offices so that their home address stays off the listing, and one independent developer called the disclosure an invasion of privacy. Google does not accept PO Boxes as addresses, unlike Apple, which shows developers' details only in the European countries where the law requires it.

Enforcement has teeth. Developers who fail to comply could have their updates held back, and Google could remove their apps from the Play Store in every region.

**Takeaways**
- If you publish Android apps and earn from them regularly, submit the trader declaration before February 1, 2027.
- If you work from home, decide now whether you can use a business address, because Google does not accept a PO Box.

## PyTorch's GreenLight lets an AI reviewer approve maintainers' pull requests
- ids: 22
- topic: Dev Tools
- signal: recommended
- url: https://www.infoq.com/news/2026/11/uber-agent-spend-steady/
- event: pytorch greenlight code review
- original title: Meta Brings Code Review Auto-Approval More Mainstream with PyTorch GreenLight
- source: InfoQ | https://www.infoq.com/news/2026/11/uber-agent-spend-steady/
- author: Andrew Hoblitzell
- image: https://res.infoq.com/news/2026/11/uber-agent-spend-steady/en/headerimage/radar-header-1200x630-1795391031838.jpg
- read: 4 min
- full text: yes

> GreenLight is an open-source version of Meta's RADAR system, which was built because code volume has outrun human review.

PyTorch now lets an AI reviewer approve pull requests written by its own maintainers. GreenLight, the open-source project behind the change, follows the design of RADAR, the system Meta uses to land low-risk diffs without waiting on a person. Meta's paper says lines of code per human-landed diff rose 105.9 percent year over year, diffs per developer per month rose 51 percent, and Meta attributes more than 80 percent of that increase to agentic AI assistance.

RADAR's gates are deliberately narrow. Open-source code and code under SOX scope are never eligible. Automated runbooks need a clean 60-day record with zero production incidents, and they are capped at 2,000 diffs a day. A risk score gates each change by percentile: allowlisted runbooks can land diffs up to the 50th percentile, other AI and bot sources stop at the 20th, and human-authored diffs at the 5th. The final check is a review agent that must rate a change at least 8 out of 10 before it counts as safe. Even then, bot diffs do not land immediately. They sit in a queue for a set delay, which the paper's diagram shows as 24 hours, and a person can still reject them during that window.

The design is conservative on purpose, since the aim is to narrow review rather than replace it. The article does not report how often the reviewing agent's judgments turn out to be wrong, so that remains the number to watch.

**Takeaways**
- If you automate approvals, gate them by the author of the change and a risk percentile rather than a single yes-or-no decision.
- Hold approved bot changes in a queue with a reject window, as RADAR does, so a person can stop a bad diff before it lands.

## Michael Nielsen pulls his neural-network book, citing the frontier labs' pace
- ids: 1
- topic: AI
- signal: recommended
- url: https://neuralnetworksanddeeplearning.com/
- event: michael nielsen neural networks book withdrawn
- original title: Michael Nielsen took down his book on neural nets
- source: neuralnetworksanddeeplearning.com | https://neuralnetworksanddeeplearning.com/ | via Hacker News
- read: 14 min
- discuss: https://news.ycombinator.com/item?id=50670757 | Hacker News | 379 points | 251 comments
- full text: yes

> The author, who wrote the book between 2011 and 2015, now expects catastrophic risk from advanced AI and says he will not help train people to build it.

Michael Nielsen has taken down his book on neural networks. Nielsen wrote it between 2011 and 2015, when expected AGI systems seemed decades away. In a November 2026 note posted with the removal, Nielsen says the frontier labs have pushed systems ahead far faster than expected, leaving humanity too little time to meet the challenges, and that these systems pose a significant risk of catastrophe.

The argument is about a category of threat rather than AI alone. If artificial superintelligence arrives, Nielsen argues, it could enable a sudden burst of destructive technologies that institutions have no time to defend against. The analogy is fire: a one-cent matchstick that requires hundreds of billions of dollars a year and a whole apparatus of institutions to defend against. Nielsen says the book came down because the author does not want to help train people to contribute to this work.

The note is short and points to a longer essay, "Which Future?", for the full case. The excerpt does not say whether the book will return in any form.

## Netflix's Quasar maps which repositories call a changed library API before it ships
- ids: 23
- topic: Engineering
- signal: recommended
- url: https://www.infoq.com/news/2026/11/netflix-quasar-api-impact/
- event: netflix quasar library api blast radius
- original title: Netflix Builds Quasar to Measure the Blast Radius of Library API Changes
- source: InfoQ | https://www.infoq.com/news/2026/11/netflix-quasar-api-impact/
- author: Leela Kumili
- image: https://res.infoq.com/news/2026/11/netflix-quasar-api-impact/en/card_header_image/generatedCard-1793857237972.jpg
- read: 3 min
- full text: yes

> In one example from the post, removing a deprecated method touched 137 repositories across three library versions.

Netflix built Quasar, an internal tool that finds which repositories use a specific library API symbol. Compatibility checkers can flag a removed method, but not who calls it. Dependency graphs show declared links rather than real usage, and text search misses inheritance, overloads and generated code.

Quasar indexes symbol definitions and references with SCIP, an open code-intelligence format. Language indexers run during CI builds and write Parquet files to Amazon S3, which Amazon Athena queries. On each pull request, Quasar compares API definitions between commits and looks up the affected repositories, dependency versions and call sites.

The approach has blind spots, and Netflix's Java Platform team says so. Reflection, dynamic loading, stale indexes and rarely executed code can all go unrecorded, so an empty result does not prove a method is unused. The team says it is investing in runtime analysis to fill that gap.

**Takeaways**
- Before deleting a library method, check for callers that a static index tends to miss, such as reflection and quarterly batch jobs.

## Rust 1.100 stabilises the allocator API after a decade, and bump allocators come first
- ids: 19
- topic: Languages
- signal: recommended
- url: https://cetra3.github.io/blog/state-of-allocators-2026-finally-stabilised/
- event: rust allocator api stabilised
- original title: The State of Allocators in 2026 - Finally Stabilised
- source: cetra3.github.io | https://cetra3.github.io/blog/state-of-allocators-2026-finally-stabilised/ | via Lobsters
- read: 12 min
- full text: yes

> The first use cases worth trying are request-scoped work, where memory is allocated in bursts and freed all at once.

Custom allocators are now stable in Rust after about ten years in limbo, shipped in Rust 1.100. The author, writing on November 24, asks what developers can actually do with the new allocator API beyond closing the feature gap with C++ and Zig.

The first use case is memory freed on a schedule. Dropping deeply nested structures costs real time on the hot path, and moving that work to a background thread only partly helps, because the deallocation calls still cost something. A bump allocator suits request handling and database queries: reserve a large block, hand out memory by advancing a counter, then free everything at once when the request ends.

The trade-off is that a bump allocator does not track individual allocations, so it can only release memory in bulk. The post goes on to other use cases, which the text available here does not reach.

**Takeaways**
- If you write request-scoped Rust services, benchmark a bump allocator against the system allocator once you are on 1.100.

## Ansible hangs on Ubuntu 26.04 because sudo-rs wraps the prompt Ansible waits for
- ids: 87
- topic: Dev Tools
- signal: recommended
- url: https://dev.to/alexgeorgiev17/chasing-down-why-ansible-stalled-on-a-fresh-ubuntu-2604-box-5678
- event: ansible sudo-rs hang ubuntu 26.04
- original title: Chasing down why Ansible stalled on a fresh Ubuntu 26.04 box
- source: Dev.to | https://dev.to/alexgeorgiev17/chasing-down-why-ansible-stalled-on-a-fresh-ubuntu-2604-box-5678
- author: Alex Georgiev
- image: https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fq7lg8opcfqw72dtpfw8u.png
- read: 7 min
- full text: yes

> The privilege escalation stalls for about 12.8 seconds and then fails the first task, before any real command runs, even with the correct password.

On a plain Ubuntu 26.04 container with sudo-rs, the default sudo on that release, Ansible's privilege escalation stalled on every run. With ansible-core 2.17.6, three runs each waited about 12.8 seconds and then failed with a timeout waiting for the privilege escalation prompt, before the first task ran.

The cause is the prompt text. Ansible tells sudo which prompt to print and then waits for that exact string. Traditional sudo prints the requested text verbatim. sudo-rs wraps it inside its own template and appends a capitalised "Password:" of its own, so Ansible never sees the string it is waiting for. The author captured the raw bytes from both implementations to confirm this.

The part of the post that tests which Ansible releases carry the fix, and which workarounds hold up, is not in the text available here.

**Takeaways**
- Before running become-based playbooks against a fresh Ubuntu 26.04 host, test one task first; a stall of about 12 seconds followed by a timeout is this bug.

## Code Mode beats tool calling on wide fan-outs but loses on single lookups
- ids: 125
- topic: AI
- signal: recommended
- url: https://towardsdatascience.com/code-mode-vs-tool-calling-benchmarks-find-a-16-tool-crossover/
- event: code mode tool calling benchmark crossover
- original title: Code Mode vs. Tool Calling Benchmarks Find a 16-Tool Crossover
- source: Towards Data Science | https://towardsdatascience.com/code-mode-vs-tool-calling-benchmarks-find-a-16-tool-crossover/
- author: Chien Vu Minh
- full text: no

> The benchmarks point to a crossover near 16 tools for agents that connect to many MCP integrations.

The details in this story come from the headline and standfirst, because the full article was not available to us. The benchmark compares Code Mode with classic tool calling for agents with many MCP integrations. On 100-item fan-outs, Code Mode was 120 times cheaper and 18 times faster, but it was less reliable on single lookups.

The headline names a crossover at about 16 tools. The fan-out results favour Code Mode, and the single-lookup results favour plain tool calls. The excerpt does not give the test setup, so treat the 16-tool figure as one benchmark's finding rather than a general rule.

**Takeaways**
- Count the tools your agent exposes; if it sits well past 16 and most calls fan out, test Code Mode before settling on direct tool calls.

## Speculative decoding speeds up agent tool calls, but uncached agent loops got slower
- ids: 121
- topic: AI
- signal: notable
- url: https://towardsdatascience.com/speculative-decoding-makes-tool-calls-faster-agents-need-a-cache/
- event: speculative decoding llama.cpp tool calls agents
- original title: Speculative Decoding Makes Tool Calls Faster. Agents Need a Cache.
- source: Towards Data Science | https://towardsdatascience.com/speculative-decoding-makes-tool-calls-faster-agents-need-a-cache/
- author: Ankur Tomar
- full text: no

> Benchmarks on llama.cpp with Qwen3 and Llama found draft-model speedups of up to 1.7 times on code, JSON and tool calls.

The details in this story come from the headline and standfirst, because the full article was not available to us. A Towards Data Science benchmark tested speculative decoding, in which a small draft model proposes tokens that the main model checks, with Qwen3 and Llama on llama.cpp. The draft model sped up code, JSON and tool calls by up to 1.7 times.

The catch is caching. Agent loops that did not use a cache ran about 6 percent slower with the draft model. The title's framing suggests the authors see a cache as a requirement for agents, not an optimisation.

**Takeaways**
- Measure speculative decoding on your own cached agent loop before enabling it in production, since the uncached loops in this benchmark got slower.

## Backloggd breach exposed emails, password hashes and sign-in IP addresses
- ids: 134
- topic: Security
- signal: notable
- url: https://www.engadget.com/2329256/backloggd-breach-november-2026-password-reset/
- event: backloggd data breach passwords
- original title: Backloggd urges users to change their passwords after a breach
- source: Engadget | https://www.engadget.com/2329256/backloggd-breach-november-2026-password-reset/
- author: Kris Holt
- image: https://www.engadget.com/img/gallery/backloggd-urges-users-to-change-their-passwords-after-a-breach/l-intro-1795728014.jpg
- read: 2 min
- full text: yes

> Payment data was not affected because payments run through Patreon, and every user now has to log back in.

Backloggd, a game-logging site that hit one million users this month, says an attacker exploited a bug to reach its admin tools. The operator posted on November 25 that usernames, email addresses, hashed passwords and the IP addresses used to sign in were accessible.

The operator says the hashing is strong, but weak or common passwords can sometimes be guessed from their hashes, so users should change their Backloggd password and any other site where they used the same one. The site was taken offline once the bug was found. The attacker's changes, including hidden games and restricted accounts, are being reverted, and every user has to log back in.

The operator says game logs, reviews and lists remain intact, and promises a fuller notice after taking legal advice. The admin tools now have stricter access controls.

**Takeaways**
- Change your Backloggd password, and any other site where you used the same one.

## Linux is dropping the 1980s VME bus driver because AI-generated noise makes it costly to keep
- ids: 119
- topic: Open Source
- signal: notable
- url: https://www.phoronix.com/news/Linux-Drops-VME-Bus-User
- event: linux vme driver removal ai noise
- original title: Linux Dropping Last Of The 1980's VersaModular Eurocard "VME" vme_user Code Over AI/LLM Noise
- source: Phoronix | https://www.phoronix.com/news/Linux-Drops-VME-Bus-User
- author: Michael Larabel
- full text: no

> The kernel is removing vme_user, the last of a run of old driver cleanups, after AI and LLM tools generated more reports about it.

The details in this story come from the headline and standfirst, because the full article was not available to us. The Linux kernel is removing the vme_user driver, which supports the VersaModular Eurocard bus of the 1980s. Phoronix reports that AI and LLM tools are generating a growing volume of noise about this unused, obsolete code, which is the reason given for removing it.

The removal continues a cleanup that has already dropped old ISA and PCMCIA code, ham radio and ISDN drivers, and other old network code.

**Takeaways**
- If you still depend on VME hardware, plan to carry the driver out of tree, since the kernel is dropping it.

## Firefox Smart Window adds Mistral's open-weight Small 4 model in beta
- ids: 33
- topic: AI
- signal: notable
- url: https://www.infoq.com/news/2026/11/mozilla-mistral-ai-smart-window/
- event: mozilla firefox mistral smart window
- original title: Mozilla Partners with Mistral to Bring Open-Weight AI Models to Firefox Smart Window
- source: InfoQ | https://www.infoq.com/news/2026/11/mozilla-mistral-ai-smart-window/
- author: Daniel Curtis
- image: https://res.infoq.com/news/2026/11/mozilla-mistral-ai-smart-window/en/headerimage/generatedHeaderImage-1795716059601.jpg
- read: 3 min
- full text: yes

> Mozilla says the partnership avoids tying Firefox's AI features to one provider, and Mistral has agreed to zero data retention.

Mozilla has partnered with Mistral AI to bring Mistral Small 4 into Firefox Smart Window, its AI browsing assistant, which is in beta. Small 4 is a 119-billion-parameter open-weight model under the Apache 2.0 licence. Mozilla recommends it for users in France, the United States and Canada, with the UK and Germany to follow later this year.

The browser's model picker lets users switch among Gemini, Qwen and Mistral Small 4 and others. That sets it apart from Chrome's Gemini integration, Edge's Copilot sidebar and Opera's Aria, which tie the browser to one vendor's stack. By default, chats stay off Mozilla's servers, and Mistral has committed to keeping no retained copies of the data from the partnership.

Feedback on Mozilla Connect has been mixed. A Cybernews estimate puts the reach at about 200,000 active monthly Firefox users, which would be Mistral's first large consumer channel outside its own Le Chat app.

**Takeaways**
- If you use Smart Window, try the same task on two models from the picker and keep the one that gives you better answers.

## sqlite3_rsync can snapshot a SQLite database to another machine without local disk space
- ids: 75
- topic: Infra
- signal: notable
- url: https://simonwillison.net/2026/Nov/26/sqlite3-rsync/
- event: sqlite remote copy snapshot
- original title: sqlite3_rsync: Database Remote-Copy Tool For SQLite
- source: Simon Willison's Blog | https://simonwillison.net/2026/Nov/26/sqlite3-rsync/
- author: Simon Willison
- read: 2 min
- full text: yes

> It sends only the pages that differ, which matters on small servers that cannot hold a second copy of the database.

Simon Willison points out that sqlite3_rsync can copy a snapshot of a SQLite database over SSH to another machine without first making a local duplicate. The usual options, the backup API and VACUUM INTO, both need enough free disk for a full copy, which rules them out on a nearly full small instance.

The tool compares checksums rather than whole files. The receiving side publishes checksums for chunks of database pages, and the sending side replies with the pages that changed or asks for finer checksums wherever a chunk fails to match. Willison notes that if the two databases start far apart, the hash exchange can cost more bandwidth than the database itself, but in ordinary use the overhead is a few percent. It first arrived in October 2024 marked as a trial feature, and its major upgrade landed in May 2025.

**Takeaways**
- On a small instance with more than half its disk in use, use sqlite3_rsync rather than a local backup or VACUUM INTO when you need a copy on another machine.

## Vite 8.4 adds an opt-in allow-list for dev-server file serving
- ids: 63
- topic: Dev Tools
- signal: notable
- url: https://vite.dev/blog/announcing-vite8-4
- event: vite 8.4 allow-list file serving
- original title: Vite 8.4 is out!
- source: vite.dev | https://vite.dev/blog/announcing-vite8-4 | via TLDR Dev (Web Dev)
- image: https://vite.dev/og-image-announcing-vite8-4.webp
- read: 4 min
- full text: yes

> The stricter mode becomes the default in the next major release, so teams can test it now.

Vite 8.4 adds an allow-list check to its dev server, replacing the block-list approach that Vite has patched for years. The old method meant listing sensitive files, and attackers kept finding bypasses through file-system and HTTP parsing quirks. Under the new mode, only files referenced from the project's entry points, including transitive references, can be served.

Setting server.fs.strict to 'extended' applies the checks to modules loaded by plugins as well, and Vite now registers files referenced through url() in CSS, not only through imports. Pairing 'extended' with an empty server.fs.allow turns on the allow-list mode. Plugins that generate modules referencing assets without an import can call this.environment.addSafeModule instead of asking users to edit server.fs.allow.

The release also detects duplicate dev servers, and it adds a fix for dynamic imports: browsers can now retry a failed module fetch, as the updated HTML specification allows, in Chrome 156 and later, Firefox 155 and later, and Safari Technology Preview 252.

**Takeaways**
- Run your dev server with server.fs.strict set to 'extended' and an empty server.fs.allow to see which imports break before the next major makes this the default.

## systemd 263 release candidate adds its first Rust code and a pseudo-TTY broker
- ids: 122
- topic: Infra
- signal: notable
- url: https://www.phoronix.com/news/systemd-263-rc1
- event: systemd 263 rust pseudo tty broker
- original title: systemd 263-rc1 Ships Initial Rust Code, Experimental Pseudo TTY Broker & Manifest
- source: Phoronix | https://www.phoronix.com/news/systemd-263-rc1
- author: Michael Larabel
- full text: no

> The release candidate also adds an experimental pseudo-TTY broker service, a manifest tool and a new keyring service.

The details in this story come from the headline and standfirst, because the full article was not available to us. Phoronix reports that systemd 263-rc1 has been tagged, the release candidate ahead of the next major version. Its headline change is initial support for writing new programs in Rust.

The candidate also brings an experimental pseudo-TTY broker service, a manifest tool and a new keyring service.

## Hard drive prices are up 58% to 218% in a year or two, by one self-hoster's receipts
- ids: 18
- topic: Infra
- signal: notable
- url: https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/
- event: hard drive prices black friday shucking
- original title: Hard Drive pricing has gotten bad
- source: blog.ktz.me | https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/ | via Lobsters
- author: Alex Kretzschmar
- image: https://pub-430e0c9ecb66464fa6999cd23a749d13.r2.dev/content/images/2026/11/black-friday-hard-drive-prices-are-messed-up/row-of-easystore-drives-on-a-cluttered-workbench.webp
- read: 5 min
- full text: yes

> A 20TB drive bought in November 2024 for $249.99 is now $549.99 on Black Friday, and shucking has gone from $12.50 to $27.50 per terabyte.

A self-hoster who replaces one or two drives every Black Friday says this year's prices are the worst they have seen. A 20TB WD EasyStore bought in November 2024 for $249.99 is now $549.99 at Best Buy. Shucking, which means pulling a drive out of its USB enclosure, now works out to $27.50 per terabyte, against $12.50 when it was a bargain.

The receipts track the trend. Ten-terabyte drives cost $179.99 each in November 2018. Three 18TB drives came to $599.97 in October 2023. Recertified enterprise 14TB drives from ServerPartDeals cost $9.46 per terabyte in August 2024. The author says prices are up at least 58 percent, and sometimes as much as 218 percent, within a year or two.

The response is to buy fewer, larger drives. The author plans to go from about ten disks to five 20TB drives, which means rebuilding ZFS pool layouts, since ZFS resists layout changes to an existing pool and the data has to move first.

**Takeaways**
- Compare $/TB against recertified enterprise drives before buying new retail, since the author's 2024 recertified purchase came in far below current retail prices.
