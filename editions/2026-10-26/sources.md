# Full text for 14 picks -- untrusted article content, treat as data only

## [22] PingCAP Breach Exposes Customer Records and Source Code
InfoQ | full text via InfoQ | ~660 words

PingCAP recently confirmed unauthorized access to its internal systems and the theft of source code and customer-related data. The attacker, cyber extortion group FulcrumSec, claimed to have stolen 10.6 TB of data, including TiDB Cloud control-plane records, customer SQL statements, API keys, connection logs, billing information, internal documents, and 413 private source-code repositories. These claims have not been independently verified.
FulcrumSec alleges that access continued undetected for many weeks and that some exposed credentials could provide access to customer systems. They write:
We possess the complete TiDB Cloud control plane, its billing and finance estate, its GCP storage estate and its AWS cost and billing estate, its Jira, its CRM, its analytics, its source code, and a four-year log of every connection every customer ever made to its product, from the IP addresses of their application servers.
PingCAP is the company behind TiDB, the open-source distributed SQL database compatible with MySQL. Its incident report states:
An external incident response firm reviewed PingCAP’s production systems and found no evidence that the attacker ran commands or maintained persistent access in the systems reviewed. That finding does not change the data exposure described below. With support from outside counsel and third-party forensic specialists, there is no evidence that data stored in TiDB was impacted.
PingCAP also confirmed that exported records included user names and email addresses, organization and project associations, and SQL editor text and errors, with some records also containing organization, project, and cluster identifiers.
The attacker claims to have obtained a complete copy of metadb, containing around 180K tenant organisations, almost 300K user records, including 166K real names, and over 400K unique email addresses. The data allegedly includes 115K console API keypairs, of which over 40K were active and the newest reportedly created hours before the attacker claims to have ended access. The group also says it obtained around 1800 external database endpoints from customer migration jobs, including root and admin accounts for customer MySQL and Aurora hosts.
FulcrumSec alleges that PingCAP engineers paste customers’ production credentials into Jira tickets, with three logs reproduced in full and the corresponding tickets included in the initial release. Kim Barthel, director and founder of 42Sec, warns:
The PingCAP breach isn't really a database story. It's a story about one service-account key (...) PingCAP says it has no evidence that customer data stored in TiDB itself was touched. Good. But look at what did leak. [...]

## [13] PHP Patches Two Critical RCE Flaws That Were Already Under Attack
InfoQ | full text via InfoQ | ~835 words

PHP recently shipped emergency releases on October 21, fixing two critical vulnerabilities that allow unauthenticated remote code execution, and Amazon says someone tried to exploit them four days before the patches existed.
PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 carry fixes for CVE-2026-109618 and CVE-2026-109619, both rated 9.2 under CVSS v4.0 and nicknamed php2shell. Both are memory-safety failures in the request lifecycle, one in out-of-memory handling and one in state that outlives the memory backing it, and Sansec reports they are present in every unpatched PHP since 5.4. The announcement is blunt about the options: "There are no complete mitigations; updating is the only safe choice."
Exposure varies by how PHP is served, and the advisories are careful about what has actually been proven. Apache mod_php carries confirmed remote code execution for both, validated "over HTTP against mod_php with default PHP input and memory limits." For PHP-FPM the session lifecycle case was validated, but on the out-of-memory bug the advisory states that "no complete FPM exploit has been demonstrated for this SAPI." FrankenPHP is described as likely susceptible on source analysis alone.
Attackers arrived before the patch did. Amazon Threat Intelligence found an exploitation attempt dating to October 17 in MadPot telemetry, originating from "an IP address associated with a commercial anonymization network," and told customers to investigate "from at least starting on October 17th." Cloudflare deployed WAF rules at 03:02 UTC on October 21, roughly nine hours ahead of release.
The coordinated disclosure had already collapsed. In its own account, the PHP Foundation says the CVE identifiers began circulating two days early, that a researcher "mistakenly published a video" showing a proof of concept, and that "Chainguard unilaterally broke the embargo and published built images containing the fix." The consequence, it writes, was that "any attacker could now study the fix in binary form while every other PHP user was still waiting for the release." Chainguard’s published policy, last updated a month before the incident, allows it to shorten disclosure timelines when "a vulnerability is discovered to be under active exploitation."
Some operators stopped serving rather than wait. On r/selfhosted, commenter iamShorteh described shutting down:
I’ve taken all of my websites offline (turned off apache2). Somebody leaked the step by step for RCE on twitter a few hours ago. Not going to risk sitting around another 5-6 hours until the hotfix lands.
The Dutch national cyber security centre took its own website offline as a precaution, as did the Dutch House of Representatives. Sansec told stores they did not need to. [...]

## [9] Root shell on Samsung TV
Hacker News | full text via Hacker News | ~295 words

log4j on X: "i own a relatively new (2025) samsung tv.
i kept getting weirdly targeted ads.
i tried reversing the firmware but it was aes encrypted and no keys unless tear it apart and do uart/jtag magic.
zero days it is. root shell on new samsung TVs!
discovered PRIVACY HORROR. write up?" / X
log4j on X: "i own a relatively new (2025) samsung tv.
i kept getting weirdly targeted ads.
i tried reversing the firmware but it was aes encrypted and no keys unless tear it apart and do uart/jtag magic.
zero days it is. root shell on new samsung TVs!
discovered PRIVACY HORROR. write up?"
i own a relatively new (2025) samsung tv.
i kept getting weirdly targeted ads.
i tried reversing the firmware but it was aes encrypted and no keys unless tear it apart and do uart/jtag magic.
zero days it is. root shell on new samsung TVs!
discovered PRIVACY HORROR. write up?
i own a relatively new (2025) samsung tv.
i kept getting weirdly targeted ads.
i tried reversing the firmware but it was aes encrypted and no keys unless tear it apart and do uart/jtag magic.
zero days it is. root shell on new samsung TVs!
discovered PRIVACY HORROR. write up?
always on hot mic functionality btw.
PLUS: automatic content recognition, geo positioning, network mapping, a targeted ads service, 4 distinct drm services, user profile building and so much more juicy telemetry!
just you, God, a $3000 TV and samsung + their 400 partners!
moreShow more
lol secured by knox, nope, no el2 hypervisor bullshit here.
thank you so much for this, i always buy LG OLED for root, but Samsung OLED is cheaper, i can now buy a samsung OLED and save my money and have root.

## [58] FBI tip line and veterans crisis site among 350 federal web addresses exposing visitors to network spies, senator warns
TechRadar | full text via TechRadar | ~1269 words

FBI tip line and veterans crisis site among 350 federal web addresses exposing visitors to network spies, senator warns
350 federal web addresses let network snoops see who visited
- Sen. Ron Wyden wants CISA and OMB to require Encrypted Client Hello on federal websites and make it a federal contract condition
- His list of 350 CDN-hosted addresses without ECH includes the FBI tip portal, the VA's crisis line, and hotlines for whistleblowers and civil rights complaints
- ECH hides site names only alongside encrypted DNS, does nothing for server breaches, and is already blocked in Russia, where some listed embassy pages are aimed
US Senator Ron Wyden (D-Ore.) wants the federal government to turn on a privacy feature that major web browsers have supported for three years, warning that hundreds of agency web addresses still broadcast the name of the site each visitor uses to anyone watching the network along the way.
In a letter to CISA acting director Nick Andersen and deputy federal chief information officer Thomas Flagg, Wyden asked the two agencies to require Encrypted Client Hello (ECH) across federal websites and to make ECH support a condition for cloud and network vendors seeking federal contracts.
The letter attaches a list of 350 executive branch web addresses that use content delivery networks (CDNs) but do not use ECH, while requesting an unclassified response and action plan by November 20 2026.
The one thing HTTPS leaves in the open is the gap being addressed here
Almost every federal site now encrypts the pages people read and the forms they submit. Standard HTTPS does not hide the hostname. When a browser opens a secure connection, it announces the site it wants in a field called Server Name Indication, in plain text, before encryption begins.
An internet provider, a hostile Wi-Fi network, or a compromised telecom carrier can therefore log that a connection went to tips.fbi.gov without reading a word of the tip itself.
ECH encrypts that part of the handshake. It works best behind a large CDN, where thousands of unrelated sites share the same front door. Cloudflare's implementation, for example, presents every ECH-protected site to the network under one shared name, so an observer can tell a visitor is reaching a Cloudflare-hosted site, but not which one.
Wyden's letter singles out two services. The Department of Veterans Affairs' online suicide prevention service at veteranscrisisline.net is hosted on Amazon Web Services, which the letter says does not currently support ECH. [...]

## [5] OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?
Hacker News | full text via Hacker News | ~2272 words

Let’s look at a quick timeline of the major LLM model announcements from both OpenAI and Anthropic over the past few months. All pricing numbers provided are input MTok / output MTok / cache read MTok.
June 26, 2026#
OpenAI announced GPT-5.6 Sol and Luna. Sol is the direct successor to GPT 5.5 at the same price of $5 / $30 / $0.50, while Luna is a small model specifically designed for cheaper use cases at $1 / $6 / $0.10. They also announced a Terra model that’s in between those two models, but few cared about it.
June 30, 2026#
Anthropic announced Claude Sonnet 5, which Anthropic claimed to be closer to their Opus models, but feedback was mixed. Notably, it had launch pricing of $2 / $10 / $0.20 which was initially supposed to be temporary but would go up.
July 24, 2026#
Anthropic announced Claude Opus 5, which was a long-awaited major-version update given the impact Opus 4.5 had on the rise of agentic coding, at a price of $5 / $25 / $0.50 (similar to GPT-5.6 Sol). Although some of the provided benchmark results surprisingly exceeded those of the much larger Fable 5, real-world feedback was more mixed.
July 30, 2026#
OpenAI announces that they cut the price of GPT-5.6 Luna by 80% (???) to $0.20 / $1.20 / $0.02.
August 10, 2026#
Anthropic announces the temporary Sonnet 5 price cut for the launch is now permanent.
August 21, 2026#
OpenAI announces that they are cutting the price for GPT-5.6 Sol by ~20% ($4 / $20 / $0.40) for the next three months.
September 1, 2026#
Anthropic announced Fable 5.1 at a price of $10 / $50 / $0.25, which, in addition to having strictly better benchmark performance in all areas than Fable 5 from June at $10 / $50 / $1, cut the cache read cost by 75%.
When using agents for coding, cache read costs are the vast majority (96% - 99%) of the total token expenditure as the cache is what contains the entire previous conversation each turn. Additionally, the cache tends to be hit around 90 - 100% of the time (varies by the infrastructure of the LLM inference provider). Taken together, a 75% reduction in the cache read cost correlates to a 70-75% reduction in the cost of using the model—obviously notable, even if cache costs are typically a footnote!
September 3, 2026#
OpenAI announced GPT-6 Astra, which is similar in size to Fable 5.1 and has similar pricing at $10 / $50 / $1 but without the lower cache read cost. Astra’s model performance is indeed comparable to Fable.
September 22, 2026#
OpenAI announced GPT-6 Sol at at a shocking price of $2 / $10 / $0.20 that halves the input and output price relative to the temporarily-discounted GPT-5.6 Sol! They simultaneously released GPT-6 Luna also at half the input and output price ($0.10 / $0.50 / $0.01) of the previous version. [...]

## [1] A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis
Hacker News | full text via Hacker News | ~981 words

A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis
I am a dermatologist. I tested the ability of GPT-6 Astra and Claude Fable 5.1 to diagnosis skin cancer and found that they were less accurate than I expected. I compared to a 10-year old CNN and to my surprise found that this was superior.
This is a melanoma.
I showed these two images - a clinical photograph and a dermoscopic (skin microscope) image - to GPT-6 Astra and Claude Fable 5.1, two of the most capable AI models available in October 2026. Both said it was a seborrhoeic keratosis, a harmless warty growth, and that the patient could be discharged. I then showed them to fine-tuned version of Inception v3, a convolutional neural network (CNN) first published by Google in 2015 and fine-tuned here on public dermatology images. The CNN got the right answer based on the dermoscopy view.
It was one of 200 biopsy-proven lesions I gave to all three. The CNN named the right diagnosis (out of 6 possiblities) for 125 of them (62%). The two frontier LLMs named it for 84 and 85 (42%). A ten-year-old network, fine-tuned for about twenty minutes, beat both of them at recognising skin cancer.
The test#
The lesions come from MILK10k, a public dataset released through the International Skin Imaging Collaboration in 2025, in which each lesion is photographed twice: a clinical close-up and a dermoscopic image taken through the illuminated magnifying lens dermatologists use. I drew 200 lesions at random, all confirmed by histopathology:
- 100 that should not be discharged: 30 melanomas, 25 basal cell carcinomas, 25 squamous cell carcinomas (including Bowen’s disease) and 20 actinic keratoses.
- 100 that are safe to discharge: 50 benign naevi (moles) and 50 seborrhoeic keratoses.
Every lesion was biopsied, including the benign ones, so these are harder to diagnose: a mole that somebody decided to cut out is one that worried a clinician.
The LLMs were given both images and nothing else, and asked, as a clinician might use them, for the most likely of the six diagnoses (or “unsure”), a confidence, a second choice, and whether the lesion could be safely discharged with no treatment, biopsy or follow-up. Both models got the same prompt at default settings, and neither refused a case.
The CNN is deliberately not state of the art. I used Inception v3 pretrained on everyday photographs and then fine-tuned all layers on 68,011 dermoscopic and clinical images from the ISIC Archive on a single H100 GPU. These 200 test lesions, and every other photograph of the same lesion or patient, were removed from its data (including the validation set) before training, so it had never seen them, and they were not used to choose the model or set its threshold. [...]

## [80] Google’s AI search changes upended online publishing
The Verge | full text via The Verge | ~1196 words

This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more about AI’s impact on the web, follow Emma Roth. The Stepback arrives in our subscribers’ inboxes on Sunday at 8AM ET. Opt in for The Stepback here.
Google’s AI search changes upended online publishing
Publishers spent years figuring out how to get clicks on Google. But new AI search features have torn that ecosystem apart.
Google’s AI search changes upended online publishing
Publishers spent years figuring out how to get clicks on Google. But new AI search features have torn that ecosystem apart.
How it started
The digital publishing industry has relied on Google for a very long time. Many outlets spent time and money optimizing their webpages to show up at the top of the search engine, with the goal of getting readers to click on their articles or discover their websites for the first time. For years, the relationship between Google and publishers was largely reciprocal; online publishers filled out Google’s search index with content, while Google supplied publications with exposure and traffic.
But that relationship has changed. The launch of Google’s AI search features — coupled with changes to the way it ranks search results — has made it harder for publishers to survive on traffic from Google alone. In 2024, Google rolled out AI Overviews, a feature that slots an AI-generated search result summarizing pages from across the web at the very top of Google Search, with links to sources its AI system determines to be the most useful placed below the summary. Instead of vying for clicks on the first page of Search, publishers became beholden to an AI system that regurgitates results, with no guarantee that users will actually click on the source of that information.
Though Google’s AI Overviews got off to a shaky start, the feature immediately raised concerns among publishers, with the News/Media Alliance saying it will be “catastrophic” to web traffic. A 2024 investigation from the Press Gazette found that Google’s AI Overviews appeared for almost a quarter of news-related searches in May 2024. By August, the outlet found that AI Overviews had begun impacting the visibility of publishers by replacing media sites that previously held the top spots on Google’s search engine for certain queries.
A future where Google could eventually stop sending traffic to outside sites on the web has only gotten closer as the company builds out its vision for an AI-powered search. In May 2025, it launched AI Mode, a feature that replaces Google’s standard search engine with a chatbot-like interface that provides detailed summaries from results on the web. [...]

## [70] AI delivers ‘zero financial payoff’ to most companies, Apollo economist says
TechCrunch | full text via TechCrunch | ~202 words

AI hasn’t benefited the bottom line of any big corporations outside the tech industry, according to a note recently published by the chief economist at Apollo Global Management (the private equity giant that used to own TechCrunch).
Apollo’s Torsten Slok focuses on what he calls the S&P 493 — the S&P 500, minus Alphabet, Amazon, Apple, Meta, Microsoft, Nvidia and Tesla — finding that profit margins and revenue per worker appear to be flat, with no evidence that AI is improving productivity.
“Despite massive investments and widespread hype around artificial intelligence, the technology has delivered zero financial payoff to corporate America outside of tech,” Slok said.
Is this simply a matter of non-tech companies lagging behind the tech giants? Slok sounded skeptical, arguing that it will be tough for corporate America to “turn increasingly cheap intelligence into higher revenue growth and higher profit margins.”
“AI may be a great calculator, but in business, intelligence is mostly judgment,” he wrote, later adding, “AI does not understand accountability, trust, culture, unwritten rules, ethical trade-offs or fairness, all of which shape reputational risk and ultimately drive revenue growth and profit margins.”
Recent studies have also found that AI has yet to deliver significant productivity gains.

## [79] r/opensource just banned AI, non-English speakers, and more
The Verge | full text via The Verge | ~281 words

The mods at r/opensource posted new submission rules that, among other things, banned projects that use AI. The post made Saturday evening opens by saying, “If your project uses AI, is made by AI, or is intended for AI, it’s not welcome on r/opensource. AI, as it exists today, is incongruent to this Open Source community.”
r/opensource just banned AI, non-English speakers, and more
The opensource subreddit’s new rules against AI have sparked a revolt.
The new rules have set off a firestorm in the comments, and even spurred the creation of a rival sub r/trueopensource. Moderator Wolvereness has waded into the comments to explain that there’s nuance and room for selective enforcement, such as “software that incidentally has accessibility features that use AI,” including automatic captioning. But that hasn’t slowed complaints from the community who feel the new rules are too broad, misguided, or vague. Many have pointed out that the Linux kernel now contains some AI-generated code, and so projects using it could be banned under the new rules.
While the AI ban is getting most of the attention, mods are placing other restrictions on posts as well. Projects submitted must be at least one year old, actively maintained, and have multiple contributors. That would bar solo developers with new projects from looking for help. The mods even say “we can no longer field requests asking for maintainers or people to contribute.”
The mods also effectively banned any non-English-speaking members of the community. “If you don’t speak English, you need to find a different community,” the post reads. “We cannot distinguish between AI-written and AI-translated. Since you don’t speak English, you can’t even verify yourself if it translated correctly.”

## [94] Google's C Binder Driver Removed With Rust Binder Ready For "Few Billion Devices"
Phoronix | full text via Phoronix | ~212 words

Google's C Binder Driver Removed With Rust Binder Ready For "Few Billion Devices"
Linus Torvalds merged the "char/misc" changes for the Linux 7.4 kernel driver on Saturday. Most notable this cycle for char/misc is what's being removed: Google's C-written Binder driver has left the kernel with the Rust-based modern Binder driver ready to take for the role of being used by all future Android devices.
As noted back in September when the patch was floated, the "painful to maintainer" C implementation of the Binder IPC driver is being retired with the Rust Binder driver having matured quite well. The C driver grew complex over Android's  history and difficult to maintain. The Rust Binder driver as the earliest prominent Rust kernel driver has exceeded feature parity to the original driver and also outperforming the C driver in some tests.
The Rust Binder driver will now be Google's sole focus moving forward for this inter-process communication used on Android. Greg Kroah-Hartman remarked in the char/misc pull request:
"removal of the C binder code, the rust version is stable and will be used going forward in a few billion devices.  Great job by those developers."
The char/misc pull also includes lots of IIO driver updates and a variety of other small fixes across different drivers.

## [15] Google ML Drift Accelerates On-Device AI Inference Across Diverse GPUs
InfoQ | full text via InfoQ | ~548 words

Google has released ML Drift, an open-source, cross-platform GPU compute engine designed for on-device AI and machine learning inference. Licensed under Apache 2.0, it abstracts the complexities of different GPU hardware and low-level APIs, supporting OpenGL ES, OpenCL, Metal, and WebGPU.
ML Drift is the core GPU acceleration engine that powers LiteRT. By open-sourcing it, Google is enabling developers to build custom graphics and inference runtimes for applications ranging from traditional computer vision, audio, and depth processing to generative AI.
One of ML Drift's main goal is simplifying access to the diverse GPU hardware that developers encounter when creating applications for edge devices.
Developers are faced with a wide range of GPU architectures, driver versions, and low-level APIs, not knowing a priori on which specific hardware the application will run on.
ML Drift aims to establish a new foundation for portability and performance, Google says, delivering "stability for traditional ML and peak performance for the most advanced generative AI".
To achieve this, ML Drift introduces several technical improvements over the legacy TFLite GPU delegate, including unified shaders through tensor virtualization, extensible custom operations, and five-dimensional tensor support. It also incorporates hardware-specific optimizations for GPUs from Arm, Intel, and Qualcomm Technologies to "maximize hardware utilization across modern GPUs".
ML Drift extends desktop support for inference on Windows and Linux through Dawn, Chromium's WebGPU implementation, while retaining native Metal backend support on macOS. Dawn provides a unified API model leveraging WebGPU's hardware abstraction layer, avoiding the need to interface directly with platform-specific graphics APIs such as DirectX and Vulkan.
Google benchmarked ML Drift using Gemma models on developer-grade workstation hardware, reporting a 12% lower memory overhead compared to other frameworks, including llama.cpp and MLX LM. The company also emphasized that ML Drift is already running on millions of devices through apps like Chrome, YouTube Shorts, Photos, and Meet.
In YouTube Shorts, ML Drift achieves up to a 40% reduction in average frame latency for segmentation-based effects on Android and iOS. In Google Photos, it speeds up computational photography and segmentation pipelines by up to two second. Adobe Lightroom and Photoshop benefit from performance improvements of up to 30% for selected AI-powered photo-editing features such as Select Subject, Select Sky, and Adaptive Portrait. Finally, Snapchat sees a 30% reduction in model latency for ML-powered face and style-generation effects on Android, enabling the use of larger diffusion models. [...]

## [78] Agentic AI in Production: Why Your Agent Keeps Answering After Its Tools Fail
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~21 words

When a tool breaks, an agent can keep going and write a confident answer from nothing while the dashboard stays green.

## [42] Valkey 9.2's new rdbcompression lz4 setting cuts a 1M-row RDB from 178MB to 35MB
Dev.to | full text via Dev.to | ~1389 words

I set rdbcompression lz4 on a Valkey 9.2.0-rc1 primary, watched a replica do a full sync, and measured exactly the same number of bytes going over the wire as with compression off. For a few minutes I believed the feature didn't touch replication at all. It does. I just had the wrong setting.
Valkey 9.2.0-rc1, released as a release candidate on 16 September with GA planned for mid-November, adds rdbcompression lz4: whole-stream LZ4 compression for RDB files. Until now, RDB persistence has compressed each string value separately with LZF, a scheme the project's own issue tracker describes as "quite inefficient" because it can only find repetition inside one value, never across the file. I ran both schemes against three kinds of data and then went looking for where the new setting falls over.
The headline number
I loaded a million keys shaped like a typical user-profile hash, each a small JSON document with a handful of repeated field names and a handful of unique values, and ran SAVE three times under each compression setting.
The default LZF setting barely moves the needle: 180.3MB down to 177.6MB, a 1.5% saving, for the CPU cost of running compression at all. lz4 takes the same file down to 35.4MB, an 80.1% cut against the default and 80.4% against no compression whatsoever, for about 6% more CPU time than LZF already costs. I reran it on a second, more repetitive dataset — 200,000 synthetic log lines with a shared template — and the gap was the same shape: 31.47MB uncompressed and under LZF, 5.91MB with lz4, an 81.2% cut.
The reason LZF does almost nothing here is exactly the limitation the project describes: each JSON document is 150-200 bytes, with no exploitable repetition inside itself, and LZF never looks past one value's boundary. Whole-stream LZ4 compresses the serialized file as one byte stream, so the repeated "active":true, "roles":["user","member"] and field names across a million records are exactly the kind of redundancy it picks up and LZF structurally cannot.
Where it doesn't help
I tried the same experiment on 200,000 keys holding 32-byte random hex tokens, the kind of value you'd get from session IDs or API keys. There is no cross-record redundancy to find, and it showed:
A 4.7% size reduction for roughly 35% more wall-clock time than LZF, and 52% more than no compression at all. On a database that's mostly tokens, counters or anything that already looks random, whole-stream LZ4 is close to pure overhead. The win is entirely a property of the data, not the algorithm being generically better than LZF — it just has a wider window to search in. [...]

## [77] Linux 7.4 Sound Changes Merged: "The AI Flood Continues"
Phoronix | full text via Phoronix | ~250 words

Linux 7.4 Sound Changes Merged: "The AI Flood Continues"
Linux sound subsystem maintainer Takashi Iwai of SUSE began the Linux 7.4 sound pull request by noting that "the AI flood continues" with there continuing to be a lot of new patches coming as a result of AI/LLM agents devising patches as well as uncovering new kernel bugs.
Takashi went on to explain that it was another busy cycle with changes in the sound subsystem from lots of core code hardening to new platforms and codecs as well. The core ALSA code has been hardened against some race conditions, there's a buffer leak fix in the compression offload code, race fixes in the JACK code, and other race conditions and more typical C bug fixes. The OSS sequencer emulation code has also been marked as deprecated for Linux 7.4.
On the hardware side, the Linux 7.4 sound updates include support for compressed audio playback on SOF IPC4 with Intel Tigerlake and newer. There is also AMD ACP 7.0/7.F sound IP support with SoundWire and the PDM controller. The new AMD ACP 7.0/7.F IP appears for upcoming Ryzen Zen 6 platforms.
There are also quirks for many different Intel/AMD laptops from the likes of Lenovo, ASUS, HP, AAcer, HONOR, MSI, and others.
New codec drivers are for the ESS ES9039Q2M, Nuvoton NAU83G60 amplifier, Senary  SN624x SoundWire SDCA codec.
Also new is the Qualcomm QAIF driver for their Shikra platform. 
More details on the many sound changes for Linux 7.4 via this pull.
