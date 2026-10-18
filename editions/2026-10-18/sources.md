# Full text for 30 picks -- untrusted article content, treat as data only

## [2] DeepSeek-v4.1-Flash-1017
Hacker News | full text via Hacker News | ~554 words

Instructions to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="deepseek-ai/DeepSeek-V4.1-Flash-1017") # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-V4.1-Flash-1017", device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "deepseek-ai/DeepSeek-V4.1-Flash-1017"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}' Use Docker docker model run hf.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
-  SGLang  How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "deepseek-ai/DeepSeek-V4.1-Flash-1017" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "deepseek-ai/DeepSeek-V4.1-Flash-1017" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": [...]

## [16] Amazon Acquires DuckLabs and Integrates DuckDB in Amazon Aurora PostgreSQL
InfoQ | full text via InfoQ | ~670 words

Amazon has announced the acquisition of DuckLabs, the Amsterdam-based company behind the analytical database DuckDB.
According to the news, Hannes Mühleisen and Mark Raasveldt, creators of DuckDB and co-founders of DuckLabs, will continue to lead the team and the open-source project’s technical direction as part of AWS.
In the announcement on their blog, Mühleisen and Raasveldt explain the reasons behind the decision to join AWS:
Joining AWS gives us the resources and reach to bring this technology to many more developers and organizations, and to pursue ideas at a scale that would have been difficult for us to reach alone.
All the parties involved in the deal have reassured the community about the future of the projects maintained by DuckLabs. DuckDB and all the components of their "Duck Stack", such as DuckLake and Quack, will remain free and open-source under the MIT licence, while the non-profit DuckDB Foundation will continue its supervision of the projects.
In the announcement, Mai-Lan Tomsen Bukovec, technology vice president at AWS, explains what DuckDB was created for:
DuckDB set out to solve the problem of blazingly fast performance for the 90%+ of data queries in the world today, that often runs 1 terabyte of data or less as part of analysis and dashboarding.
She argues that DuckDB's optimisations and performance are particularly relevant in agentic AI workloads. AI agents often inspect data and run small exploratory queries before deciding how they actually want to move forward, a pattern that makes DuckDB naturally optimised for AI use cases.
The community has positively welcomed the news, though with some scepticism. On Reddit, adappergentlefolk writes:
I hope this doesn't slow the pace of innovation they have been doing, but i'm glad they found a way to both cash in on their work yet keep most of it oss under the foundation.
In a piece on Werner Vogels's blog, Andy Warfield, distinguished engineer at AWS, shares more on how the relationship between AWS and DuckLabs matured before the acquisition. He writes that the initial contact happened when the S3 team was working on S3 Tables. The collaboration then evolved, as he explains:
Over the past two years (give or take), our teams have worked more and more closely together and have broadened the areas where we’ve collaborated. [...]

## [73] Deno Acquired by Cloudflare, Will Work on Open Source Self-Hosting Platform for Applications
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~94 words

"Cloudflare has acquired Deno, the company behind the [server-side] JavaScript and TypeScript runtime created by Ryan Dahl, the inventor of Node.js," Forbes reported last week. But Deno "has no future at Cloudflare, which will maintain the runtime for another year before ending its development," writes The Register. "That's OK with Dahl. 'I am now of the opinion that if you're choosing Node.js for building servers, you're doing it wrong,' Dahl told The Register." It all started with his team's work on the platform Deno Deploy, "We wanted to make running applications as straightforward as

## [55] OpenAI is building a humanoid robot, but the body isn't the real challenge
Engadget | full text via Engadget | ~721 words

OpenAI is building a humanoid robot, but the body isn't the real challenge
Figuring out how the 'brain' will work will take a lot of time.
While OpenAI is already busy with the development of AI models and new consumer hardware, CEO Sam Altman and his team apparently have time for one more project: a humanoid robot.
On the Sources podcast, Altman explained that the human form is logical because "the world is very much designed for people." Doors, keyboards and tools are all designed around a certain type of body, and a robot that can move around in the same spaces should probably have a similar form factor. As Altman put it, "matching that form factor seems good."
When asked if OpenAI will actually build one, his response was much more succinct: "We will." However, Altman isn't so concerned with the nitty-gritty details of what that robot looks like. Those questions are "less important than really figuring out ... the brain that makes the robot work," he said. Basically, giving a machine two arms and two legs doesn't get you very far if it doesn't know what to do with them.
This is still some distance from becoming a product. Altman told Fortune: "I think we'll have a cool demo in 2027 ... I don't think there will be robots walking the streets for a few years longer." OpenAI hasn't disclosed what that demo will showcase, what its humanoid will look like or when anyone outside the company will get close to one.
The 'brain' has to make the hardware useful
Calling it a robot "brain" almost makes the problem sound neat, but it isn't.
A capable humanoid must be able to understand what its cameras and sensors are seeing, interpret an instruction, decide how to carry it out, coordinate its body and then correct itself when the real world introduces something inconvenient. When picking up a mug, for instance, it needs to identify the mug, find the handle, estimate the grip and exert the correct amount of force to lift it. Otherwise, you're left with a coffee spill and a floor-cleaning job.
OpenAI is already recruiting people to address those issues. Its robotics roles span motion control, state estimation, actuator control and whole-robot behavior, as well as the machine-learning infrastructure to train physical AI systems.
There's a bit of history here as well. OpenAI's Dactyl research project taught a robotic hand how to manipulate real objects, with its training done entirely in simulation. [...]

## [72] Linux Maintainers Can Now Submit AI-Generated Code Without Declaring It
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~98 words

Linux maintainers "have ruled that people no longer have to declare their LLM usage," reports XDA Developers, "as Torvalds himself calls a ban on AI 'utterly stupid.'" The first part of this story comes via a message sent to the Linux mailing list. It announces one of the major changes decided during the Maintainers Summit on October 8, 2026, in Prague, Czechia, where submissions to the kernel no longer need to use the "Assisted-by" tag... meaning that people can submit AI-generated code without needing to declare it as such. In some correspondence regarding concern about this new disclosur

## [37] Meta removes language that raised scraping and AI training concerns
TechCrunch | full text via TechCrunch | ~176 words

Meta recently updated its commercial terms of use, declaring that the company can “use any content from [a business account’s] domains, web pages, or URLs to provide, develop, improve, research, train, and maintain the integrity of” Meta products and services.
According to legal experts interviewed by Nieman Lab, this looked like a “remarkable provision” that could give Meta permission to scrape the website of any publisher with a Meta business account and use the content to train the company’s AI models. (While Meta defeated a high-profile lawsuit over alleged copyright infringement last year, other cases against AI companies, including Meta, continue.)
However, a Meta spokesperson insisted that the updated terms did not reflect a change in the way Meta crawls the web. And now, The Verge reports that the provision has been removed.
“We’ve heard you and want to clarify: the crawling terms we consolidated only applied to our ads and business products, and we’ve clarified that in the terms themselves,” the company said in a statement. “It does not change how Meta uses web crawlers.”

## [70] Replit makes OpenAI its default over Anthropic, CEO says
TechCrunch | full text via TechCrunch | ~625 words

Replit, the AI coding platform that has become a favorite of startup founders and developers, is no longer working with Anthropic, the company’s CEO and co-founder Amjad Masad said Thursday while onstage at TechCrunch Disrupt.
Masad said the decision was made for a number of different reasons, including cost. Replit announced a partnership with OpenAI in August, but there was never any indication that it was no longer partnering with Anthropic.
“I think ChatGPT is better now,” Masad said, adding that the company uses an internal benchmark to help assess metrics like performance. “We publish a public benchmark as well, and consistently, Sol and Astra perform better on building vibe-coded applications from scratch. It was a decision based on both cost, partnership, and performance. And for all these reasons, we just felt like they were a better partner for now.”
It seems, however, that Anthropic hasn’t been completely cut out of Replit, which sells a cloud-based software development platform where users can develop and deploy apps directly from inside their browser.
After Disrupt, Masad clarified that customers can still access Anthropic models on the platform, but that OpenAI’s ChatGPT is now the default. This shift could significantly reduce Replit’s spend with Anthropic since most customers stick with the default rather than selecting a model themselves.
Prior to striking a deal with OpenAI, Replit relied on Anthropic’s Claude models to run its platform. That partnership was said to have helped the company grow its revenue significantly, and Masad noted on stage that Replit had been, until recently, a top-five customer of Anthropic’s.
“Replit remains model agnostic,” Masad told TechCrunch over the weekend. “Our users can choose Anthropic’s Claude or other supported models…OpenAI is now our preferred partner for powering Replit Agent, based on performance, economics, and the strength of our partnership.”
Masad’s comments on stage were rejected by insiders familiar with the partnership between the Anthropic and Replit, however. One person familiar, who asked not to be named, said the partnership was still in place.
There is evidence on the company’s website, blog posts, and social media posts that Replit was promoting Anthropic products as recently as a few weeks ago. For instance, a blog post in late September cites Anthropic’s Claude Fable 5 and Claude Fable 5.1 as models running in Replit Agent’s production environment. [...]

## [109] Have a Meta business account? You’re consenting to AI scraping now, legal experts say
ZDNet | full text via ZDNet | ~523 words

ZDNET’s key takeaways
- Meta Business Suite’s new terms allow web-crawling on publication sites, legal experts say.
- The change goes into effect on Oct. 30.
- Meta says the updated terms are a “consolidation” of pre-existing conditions.
Meta’s new commercial terms allow its web scrapers, bots, and agents to crawl websites “associated with” Meta business accounts, including news publishers, according to a report by Nieman Lab.
The terms apply to accounts that use Meta Business Suite’s account dashboard. Companies manage their Instagram profiles, Facebook pages, Messenger, and WhatsApp channels through Meta Business Suite. ZDNET uses Meta Business Suite to analyze and schedule posts across social media platforms.
Also: Meta Muse is the worst AI agent for privacy – and I’ve tried them all
More from ZDNET
What’s changing
The changes go into effect on Oct. 30, and Meta will not provide an opt-out, meaning publishers will either agree to the web-scraping or be booted from the platform. These are Meta’s new terms and conditions for web-crawling:
You authorize us (or any entity acting on our behalf) to use automated software (such as web scrapers, bots, robots, spiders, crawlers, and user agents) and create test credentials to access, index, cache, analyze, collect, retrieve, or crawl the domains, web pages, or URLs (and any content available through them) that are associated with your products or services, or that are made available through your or users’ use of Meta Company Products and services, and to periodically pull updates from such domains, web pages, or URLs. Meta may use any content from such domains, web pages, or URLs to provide, develop, improve, research, train, and maintain the integrity of, the Meta Company Products, services, and features provided under these Commercial Terms and any other applicable supplemental terms.
Publishers vs. AI companies
Meta could be avoiding entering licensing deals with many websites and news publications through this new web-scraping language, Nieman Lab reports. Tech companies need tons of data and information to train their AI models, but not just any data will do. Journalistic content makes for a high-quality dataset because it’s traditionally been fact-checked and edited, which personal blogs or other text scraped from the open internet may not be. [...]

## [113] India becomes the latest country to report rogue AI agent activity
TechCrunch | full text via TechCrunch | ~353 words

AI agents from multiple providers accessed personal data and confidential material at Indian organizations during research and testing, India’s cybersecurity agency said Thursday.
The Indian Computer Emergency Response Team (CERT-In) said it had received “multiple voluntary disclosures from AI model providers” whose models, during research and evaluation runs on the open internet, “had reached the live systems of Indian organizations.”
The agents got in through credentials and connection settings left exposed in app configurations, public code repositories, and overly permissive cloud roles, and their actions “exceeded the authorisation of their assigned tasks.”
This makes India the latest stop on what has become a world tour for rogue AI agents. In July, OpenAI’s agents escaped a test environment and hacked French company Hugging Face — kicking off a summer of rogue AI agent activity. Last month, OpenAI apologized to Australia after its agents accessed four government websites, including a Medicare statistics portal.
At Hugging Face, OpenAI’s agents started the same way but then found and exploited software flaws to run code on the company’s servers. CERT-In described no such hacking in India, where the agents appear to have simply used the access left lying around.
Still, the Indian cases appear to be worse in one respect, which is what the agents saw: In Australia, OpenAI said it found no evidence its agents touched individuals’ medical or criminal records, even after they wrote files inside a Medicare statistics system, while in India, agents read personal data and confidential business records. And unlike earlier incidents, each disclosed by a single lab, India’s case involved agents from multiple providers.
CERT-In did not name the providers or affected organizations, or say whether the agents altered any systems. TechCrunch has reached out to CERT-In for more information.
For now, the closest parallel seems to be Anthropic’s July disclosure of Claude breaking into three companies’ systems during testing using basic techniques like weak passwords.
In India, as in Anthropic’s cases, the affected organizations had not detected the intrusions on their own. The disclosures have left governments relying on AI companies causing these breaches to voluntarily disclose rogue AI agent activity.

## [92] Encryption Is Getting Squeezed From All Sides
Wired | full text via Wired | ~914 words

Welcome to Kernel Panic, a weekly newsletter by Lily Hay Newman and Matt Burgess from inside the new world of privacy and digital security. To receive this newsletter in your inbox each week, sign up here.
Oh, Canada. The Great White North is the latest country to contemplate legislation that could essentially mandate backdoors and increase data retention in encrypted services. The proposed changes have prompted the Canadian anti-censorship company Psiphon VPN—which keeps millions of Iranians online during repressive internet shutdowns—to say it will leave the country if the bill passes. And Psiphon is not the only one.
Encrypted messaging app Signal has said it would exit the Canadian market because the legislation would require unacceptable changes to its open source projects. Apple and Meta have criticized the bill, and DuckDuckGo and NordVPN say they would consider pulling their services, too. But as countries around the world contemplate similar legislation, even larger questions begin to emerge about which states or regions could differentiate themselves as being safe havens for privacy services if global hostility to encryption continues to rise.
It’s been maddening and disturbing to see more and more democratic countries around the world propose changes to their surveillance and data collection laws, with the aim of giving cops and intelligence agencies greater powers to access people’s information. Governments already have broad digital surveillance powers and investigative tactics to solve crimes that involve encrypted data, but legislative proposals almost inevitably include provisions to expand this access even more—mandating additional logging and what amounts to backdoors or intentional flaws in encrypted products, which cryptographers and security engineers have consistently said cannot be built safely. Truly everyone who understands the issue has said it as much for decades. Yet policymakers return again and again to the idea, somehow expecting a different conclusion or a new breakthrough that will make it all possible.
“There have always been some officials within certain agencies that tend to view technology as a crime scene in and of itself, and it becomes a myopic point of fixation where access is desired,” says Kate Robertson, a senior research associate at the University of Toronto’s Citizen Lab. [...]

## [88] Websites are closing their doors to AI agents
The Verge | full text via The Verge | ~947 words

Autonomous agents are the hottest thing in AI. OpenAI, Meta, Google, Instinct, and others promise their agents can scour the internet on your behalf, doing anything from booking a dinner reservation and cleaning out your inbox to buying new shoes. But what happens when the rest of the internet won’t play nice?
Websites are closing their doors to AI agents
OpenAI, Meta, and Google want AI agents to do everything for you. But popular services on the web aren’t letting that happen.
In recent weeks, users of services like Meta’s Muse, xAI’s Grok, OpenAI’s Dots, and Instinct have reported blocks preventing their AI agents from performing tasks across top websites. Yelp told TechCrunch that it only allows AI agents that pay for its data licensing program, while Delta Air Lines is preventing them from booking tickets on behalf of users. JPMorgan Chase and Charles Schwab have also confirmed that they’re blocking AI agents from accessing accounts due to security concerns. Some users say sites that previously worked with their AI agent are no longer accessible, including Cars.com and Amtrak, suggesting other companies could be quietly blocking them.
Amazon was already fighting off AI agents last year when it banned Perplexity’s agentic shopping feature and sued the AI startup, raising legal and practical questions about the future of agents on the web. At the time, Amazon claimed it “repeatedly requested” that Perplexity stop allowing its AI agents to shop on its website, adding that third-party companies that purchase items on behalf of customers “should operate openly and respect service provider decisions whether or not to participate.”
Perplexity responded by pointing out that Amazon doesn’t want AI agents roaming its platform because it won’t get as many human eyeballs in front of its ads — which is an actual issue for the ecommerce giant. The AI startup likened its AI agent to an extension of the user, arguing that Amazon “does not believe in your right to hire labor, to have an assistant or an employee acting on your behalf.” While a judge later ordered Perplexity to stop its AI agents from shopping on its website, an appeals court overturned this ruling in August. Amazon has since filed an amended complaint.
Even if websites aren’t banning AI agents outright, agents may still be clashing with anti-bot systems
This ongoing legal battle didn’t stop OpenAI, Meta, and Google from rolling out agents of their own. [...]

## [7] You could have invented transformers from memory
Hacker News | full text via Hacker News | ~4148 words

Large language models today can recall obscure facts from every corner of the world. Most recently, I was running late for a friend’s board game night, so I asked Astra to remind me the rules to Dune: Imperium. It gladly narrated them to me as I drove over and helped me remember the rules well enough for me to play again. We’re so used to asking models about anything that we take their vast knowledge for granted.
How do models remember so much information? And how much can they store?
In this post, I’ll go through an intuitive way to look at linear maps, MLPs, and self-attention as different kinds of memory stores. From this intuition we can derive some heuristics for how much memory each layer can store.
The key property that characterizes a “good” memory store is its ability to recall what it stored. After all, even if we could store infinitely many facts, it’s not very helpful if we can’t recall them when we need to. The more memories we store, the more they interfere with each other when we try to recall one. So throughout the post we’ll focus on one quantity, the interference-to-signal ratio, which measures how much the other memories get in the way during recall. The number of memories a store can hold before the interference grows as large as the signal is its capacity.
We’ll develop this perspective and show how you can go from a linear layer to something better, an MLP, which improves both capacity and recall, and then all the way to self-attention, which has very good recall and can store a potentially unbounded number of memories. With 64-dimensional keys, that’s a jump from about 64 memories, to about 2,700, to over a million.
Here are the terms we’ll use throughout. A memory store is a function $f$ that holds $M$ memories, for $i = 1, \ldots, M$. A memory is one key-value pair: a key $k_i \in \reals^{d_k}$, used for lookup based on similarity, and a value $v_i \in \reals^{d_v}$, which is what we want to retrieve. To use $f$, we query it with an input $x$, and it recalls an output $f(x)$. A good memory store recalls $v_i$ when we query it with $k_i$, or with another vector similar to $k_i$. In the literature, a memory store that recalls by similarity is called an associative memory. [...]

## [8] Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware
Hacker News | SNIPPET ONLY (Hacker News: no readable article text (paywall, bot check, or not an article)) | ~0 words



## [10] RTX Spark Ignites Global Celebration as New Windows PCs Arrive
NVIDIA Blog | full text via NVIDIA Blog | ~478 words

NVIDIA RTX Spark laptops are now available, bringing NVIDIA Blackwell RTX graphics, up to 128GB of unified memory and the full NVIDIA AI platform to slim, premium Windows PCs.
Starting at $2,399, laptops from ASUS, Dell, HP, Lenovo, Microsoft and MSI bring powerful local AI, content creation and gaming capabilities to a portable device, with additional systems on the way.
NVIDIA celebrated the launch with events around the world, including one in Berlin, where NVIDIA founder and CEO Jensen Huang made a surprise appearance.
A New Generation of Windows PCs Has Arrived
RTX Spark brings decades of NVIDIA accelerated computing innovation into a single superchip, combining an NVIDIA Blackwell RTX GPU and NVIDIA Grace CPU with up to 1 petaflop of AI compute and up to 128GB of unified memory. Read more in the press release.
RTX Spark Launch Celebrations Light Up Berlin
The arrival of RTX Spark brought fans, creators and PC enthusiasts together in Berlin during the Festival of Lights, an annual autumn art festival that transforms the German capital’s most famous landmarks, streets and squares into glowing canvases. This year, the festival featured RTX Spark-themed lighting on the Berlin TV Tower.
Fans gathered hours ahead in anticipation for the launch celebration at XPERION, the gaming venue inside Saturn at Alexanderplatz, where attendees got hands-on with RTX Spark laptops from leading PC makers, exploring the latest gaming experiences, content-creation workflows and local AI capabilities.
The celebration included a special appearance by Huang, who greeted an enthusiastic crowd, passed out popcorn and posed for selfies. He also gave out five personally signed RTX Spark laptops.
Berlin held one of six RTX Spark retail launch celebrations worldwide.
From San Francisco to Seoul: How the World Welcomed RTX Spark
A massive crowd gathered at the JD MALL Shuangjing Store in Beijing to celebrate the highly anticipated launch, enjoying a night of innovation and community connection.
Attendees at Vatan Bilgisayar Topkapı in Istanbul experienced a lively event filled with interactive demonstrations and specialized programming led by local creators.
Seoul’s COEX East Lobby transformed into a bustling hub of creativity, hosting an eager crowd for engaging hands-on demos and captivating evening sessions dedicated to gaming and AI. [...]

## [20] How Itaú is building generative AI for its entire customer base
OpenAI Blog | SNIPPET ONLY (OpenAI Blog: HTTP 403) | ~29 words

With ia.i, a conversational interface, and the IARA governance platform, Itaú is applying its AI First strategy to customers and employees — in one of Brazil’s most regulated sectors.

## [41] AI Made Your Easy Work Free. That Made You More Valuable.
Dev.to | full text via Dev.to | ~1528 words

Let's start by admitting the scary part is true, because the whole argument falls apart if I pretend otherwise.
AI can build an enormous amount of software now, fast, for almost nothing. You can vibe-code a working app over a weekend. Clone a SaaS product's whole front end in an afternoon. Generate the CRUD endpoints, the forms, the standard UI, the glue code, the "make it look like this" — all of it, in minutes of prompting, at a quality that a few years ago would've been a week of a junior's time.
That's not hype. It's real, and if you've felt the floor shift under you because of it, you're not imagining things. So the fear makes sense: if building software is nearly free now, what's left for the people whose job was building software?
Here's the thing that question quietly assumes, though — and it's wrong. It assumes the building was where the value lived. It wasn't. And once you see what AI actually made free, and what it conspicuously didn't, the panic turns into something closer to a map.
What AI actually made free
Let me be specific and generous about how much AI really took, because downplaying it just sounds like denial.
It took the happy path. The first version. The part of the work that's been written down ten thousand times in tutorials, Stack Overflow answers, and open-source repos — which is exactly why the model learned it so well. The standard login flow, the typical dashboard, the ordinary API, the form that validates an email, the component that looks like every other component. The commodity layer of software engineering, the stuff that was technically "skilled work" but was really pattern-matching against a million prior examples.
That's maybe 90% of the volume of what gets typed in a day. And it genuinely did fall. A huge amount of what used to be billable, time-consuming, résumé-worthy engineering is now a prompt and a glance. Pretending that's not true helps no one, least of all you.
Concede the whole 90%. The argument doesn't need it.
What it conspicuously did not touch
Now the part nobody put in the demo.
AI did not learn how to make a webhook idempotent when Stripe times out mid-transaction and you have no idea whether the charge went through. It didn't learn to tune cgroup memory limits when a background worker quietly OOMs at 3am and takes the queue down with it. [...]

## [43] Docker Compose 5.6's jobs type only starts through docker compose run
Dev.to | full text via Dev.to | ~1487 words

Docker Compose 5.6.0 shipped on 2 October with a new top-level jobs: section, sitting next to services: in the compose file. I wanted to know what actually happens when you declare one, because the release notes say almost nothing beyond "partial support for jobs: only manually-triggered jobs are supported for now."
The first thing that happened was my compose file got rejected.
$ docker compose config
validating /home/user/compose-jobs-test/compose.yaml: jobs.migrate missing property 'triggers'
A jobs: entry is not just a service with a different label. It needs its own triggers: block, and compose will not even parse the file without one. Once I added triggers: {manual: true}, it validated and I could start testing what a job actually does differently from a service.
What a job refuses to do
I wrote a small compose file: a long-running db service, and a migrate job that depends on it, sleeps a second and exits 0.
services:
  db:
    image: alpine:3.20
    command: ["sh", "-c", "echo db-up; sleep 600"]
jobs:
  migrate:
    image: alpine:3.20
    depends_on:
      - db
    triggers:
      manual: true
    command: ["sh", "-c", "echo migrating; sleep 1; echo done; exit 0"]
docker compose up -d started db and said this about the job, then moved on:
time="...Z" level=warning msg="jobs are not started by up; trigger them with `docker compose run`: migrate"
Exit code 0. docker compose ps -a afterwards shows only db. The job is simply absent, not failed, not pending, not listed anywhere up reports on.
create and start are less forgiving. Both refuse outright:
$ docker compose create migrate
job "migrate" can only be triggered with "docker compose run"
$ echo $?
1
Same message, same exit code, for start. So of the five commands that normally bring a service into existence, four of them (up, create, start, and as far as I could find no fifth alternative) will not touch a job at all. Only run works.
The opposite reading: declaring the documented future breaks the present
The release notes are honest that scheduled jobs aren't supported yet, only manual ones. I wanted to see what "not supported yet" meant in practice, so I added a second job with a schedule trigger instead of manual:
jobs:
  nightly:
    image: alpine:3.20
    triggers:
      schedule: ["0 2 * * *"]
    command: ["sh", "-c", "echo nightly-run"]
This is where the asymmetry shows up. A manual-only job that up can't start gets a warning and is skipped; the rest of the stack comes up fine. [...]

## [97] GNOME's New Local/Cloud AI Chat App Gains More Features
Phoronix | full text via Phoronix | ~218 words

GNOME's New Local/Cloud AI Chat App Gains More Features
Coming about the past few months has been Moose as a GNOME-aligned AI chat application built around GTK4 and libadwaita. It began as a local AI chat app for the GNOME desktop and grew to support cloud AI services as well. This past week marked the latest feature release for Moose.
Moose 0.6 adds support for secure cloud connections with protected credential storage for those wanting to make use of cloud AI platforms. There is also now a Local-Only mode for using Ollama managed by Moose on your own device. Permission handling can also now be set per-chat or remembers across chats of the same provider.
The updated GNOME AI chat app also now has a GNOME Files browser for interacting with files on your system and attaching them to an AI chat conversation. There is also an expanded local model catalog for chat / vision / reasoning / coding purposes. 
Moose 0.6.1 was also released with some follow-on changes, including support for connecting to Mistral AI and DeepSeek from Moose.
Moose can be downloaded from GitHub and also available in Flatpak form on Flathub. More details on the new Moose release and other GNOME app updates for the past week can be found via This Week in GNOME.

## [135] I Reran My Python 3.14 JIT Benchmarks on Python 3.15
Towards Data Science | SNIPPET ONLY (Towards Data Science: HTTP 403) | ~16 words

The same three workloads show a much stronger JIT, but it still doesn't help every program

## [65] ReactOS Can Now Be Installed & Used With Its NTFS Driver
Phoronix | full text via Phoronix | ~171 words

ReactOS Can Now Be Installed & Used With Its NTFS Driver
The ReactOS open-source operating system has seen its NTFS file-system driver mature to the point that it can be finally used for installing and using ReactOS with it. NTFS formatting support is also finally now possible with this driver too.
Hitting this major milestone of its NTFS driver maturing to the point of installing and using the ReactOS operating system itself with it also puts the project one step closer to its elusive beta release.
ReactOS posted to X today this big goal being realized of the NTFS driver being much more mature for handling ReactOS installations.
It is important to note though that the ReactOS NTFS driver still lacks caching leading to slower performance than other NTFS drivers/platforms, journaling, and security support are also not yet implemented. There is also the possibility of other undiscovered bugs they note.
A nice milestone for ReactOS and the latest in a variety of nice achievements they have made so far in 2026.

## [127] Employees are vibe-coding their own apps. Cloudflare open-sources Void to give IT a handle on them
The New Stack | full text via The New Stack | ~1379 words

Employees are vibe-coding their own apps. Cloudflare open-sources Void to give IT a handle on them
Many companies are keen to let employees build their own applications using AI, even those with little or no programming experience. Just yesterday, Gergely Orosz of The Pragmatic Engineer highlighted the likes of Ramp and Stripe, which have developed internal tools that allow non-engineers to create software for their colleagues to use.
But this newfound freedom also creates a headache for IT departments. Who tracks these applications, what company data can they access, and who’s responsible for ensuring they’re secure? In many regards, vibe-coded apps are the new shadow IT, with employees deploying software beyond the oversight of their IT teams.
And that’s why Cloudflare wants to bring some order to proceedings. On Thursday, the company announced the release of Void, a collection of three open-source tools that includes a self-hosted platform where companies can deploy and manage their employees’ AI-built applications. The idea is to give staff somewhere to publish their wares, all the while letting admins control who can deploy and access them.
Cloudflare’s growing JavaScript empire
Cloudflare has compiled quite the collection of JavaScript expertise over the past year. Just last week, the company announced its acquisition of Deno, the company behind the JavaScript runtime founded by Node.js creator Ryan Dahl. And way back in January, it snapped up the team behind Astro, the open-source web framework. Then in June, it acquired VoidZero, the open-source tooling company founded by Vue.js and Vite creator Evan You.
All three operate within the JavaScript ecosystem, albeit with different specialties spanning web frameworks, development tooling, and server-side runtimes.
You formally unveiled VoidZero in October 2024, with a founding mission to bring together the disparate tools developers rely on when writing JavaScript. It already had considerable open-source pedigree, with its team contributing to established projects such as Vite and the Vitest testing framework, alongside developing the Rust-based Rolldown bundler and Oxc, a collection of tools for processing and analyzing JavaScript code.
In October 2025, VoidZero announced Vite+, an effort to bring its various development tools together under a single command-line interface (CLI). [...]

## [5] Pele – Mermaid diagrams as themeable SVG
Hacker News | full text via Hacker News | ~191 words

Pele is a lightweight open source library that renders Mermaid diagrams to SVG, themed with CSS variables.
How it works
Write Mermaid syntax, Pele renders it to SVG. Try editing the example below.
Mermaid
1flowchart TD2  A[Mermaid text] --> B{Flowchart?}3  B -- Yes --> C[Pele]4  B -- No --> D[Mermaid]5  C --> E([SVG])6  D --> E
Use CSS variables to set colors and fonts. Color changes apply without re-rendering.
CSS
1.pele {2  --pele-bg: #fffcf0;3  --pele-fg: #100f0f;4  --pele-muted: #6f6e69;5  --pele-line: #100f0f;6  --pele-surface: #f2f0e5;7  --pele-surface-alt: #e6e4d9;8  --pele-border: #cecdc3;9}
Pele
Why Pele?
Zero dependencies, 6× smaller, and up to 500× faster than Mermaid.js. Pele supports every diagram type built into Mermaid 12.1.0.
Pele in your app
Add Pele to your app using the API.
Pass Mermaid syntax to render() and insert the returned SVG into your page.
Explore
Examples
Browse supported diagram types.
API
Render diagrams in your app.
Theming
Set colors and fonts with CSS variables.
Compatibility
Compare syntax, layout, and features with Mermaid.
Pele in use
Pele is open source, developed for Obsidian to render diagrams quickly and match your theme. It is named after Pele, the goddess of volcanoes and fire.

## [27] Helidon 27 Introduces Restructured Programming Models and New Messaging and Data Modules
InfoQ | full text via InfoQ | ~654 words

The release of Helidon 27 is the very first that follows the Oracle Tip & Tail Model of Library Development, where the Tip adopts the latest Java technology and the Tail provides a more stable and secure baseline. Concurrent with the release of JDK 27, changes include a restructuring of the original programming models and the introduction of two new modules, Helidon Messaging and Helidon Data JDBC.
Helidon 27 serves as the Tip, meaning that it aligns with JDK 27, adopts the latest Java features, and will continue to be updated under the current OpenJDK release cadence. Therefore, Helidon 28 will be available with the upcoming release of JDK 28 in March 2027.
Helidon 4.5.5, still managed under the familiar Helidon semantic versioning, serves as the Tail, meaning it maintains Helidon 4.5 LTS on its JDK 21 baseline with support for JDK 25; prioritizes critical bugs, security fixes, and carefully selected backports; and provides a longer-lived production baseline for development teams.
Helidon 27 is maintained under the auspices of the Java Verified Portfolio (JVP), an ecosystem of Oracle-supported technologies first introduced at JavaOne 2026, It also includes JavaFX 27, Jipher 20 and the Java Platform Extension Visual Studio Code
Originally named J4C (Java for Cloud), Helidon was designed to be simple and fast, and originally contained two programming models: Helidon SE and Helidon MP. This release introduces the new Helidon Core, replacing Helidon SE, with two new programming models: Imperative and Declarative. As the names imply, Imperative, similar to heritage Helidon SE, allows developers to create their applications using “plain old” Java without dependency injection or annotations. Declarative, on the other hand, provides developers the ability to use dependency injection and annotations that generate imperative code and wiring at build time.
Helidon MicroProfile replaces the heritage Helidon MP and has been moved into its own project. It will continue to support the specifications under MicroProfile and Jakarta EE and follow the Helidon semantic versioning.
Helidon SE Integrations has also been moved to its own project and renamed Helidon Extensions. Each extension will be independently maintained under its own release lifecycle.
Helidon Messaging, a new messaging layer that simplifies traditional messaging, avoids reactive APIs such as the MicroProfile Reactive Messaging specification. [...]

## [46] Python performance: native loops, NumPy and the vectorize trap
Dev.to | full text via Dev.to | ~1792 words

Python performance discussions tend to reach for a language migration before measuring the work. A numerical loop makes the problem easier to see: you can keep the calculation unchanged, move its repeated execution into a native operation, and finish much sooner on the same CPU. You can also spend the entire gain converting the data around that operation.
We tested both situations, plus a compiled Python-syntax loop and the tempting np.vectorize wrapper. The result gives you a practical question to ask before rewriting anything: where does the loop actually run, and which input and output does your caller need?
TL;DR
- Numeric NumPy operations can process typed arrays through compiled implementations, reducing repeated interpreter and object work.
- The ready-array case was dramatically faster in our workload. A Python-list input/output contract removed that advantage.
- Small inputs favored a comprehension. A warmed Numba loop was fast too; its initial compilation had a separate cost.
- np.vectorize provides a convenient array-facing wrapper around a Python function. Its documented implementation still calls that function across elements.
- Profile the complete path and retain the result representation that the next operation can use.
What this Python performance test measures
The calculation was y = x*x + x. Every implementation received the same numerical values, and every checked answer matched exactly. Inputs were bounded, integer-valued floating-point numbers, making this expression's rounding behavior straightforward. This was an elementwise calculation, with no reduction whose summation order could change the answer.
The primary run used this environment:
We retained eleven warmed timing trials per method and case, shuffled method order, and recorded output correctness and the environment. All forty correctness comparisons passed.
There were two contracts. Ready inputs prepared a Python list or numeric array before the timer and allowed the implementation's normal output representation. Python-list input/output began with a Python list and required a fresh Python list at the end. The numerical backends therefore included conversion into an array and conversion back out.
For one million values, these were the primary run's median milliseconds:
The ready-array gain is substantial. The common-list comparison is a near tie between the comprehension and the numerical implementations. Those are answers to different caller requirements. [...]

## [111] AI agents turn one request into about 20. Kubernetes is evolving to handle it.
The New Stack | full text via The New Stack | ~1304 words

AI agents turn one request into about 20. Kubernetes is evolving to handle it.
Welcome to another edition of Road to KubeCon, where we’re tracking interesting movements in the cloud-native and Kubernetes ecosystem as we count down the days to KubeCon + CloudNativeCon NA 2026, to be held in Salt Lake City, Utah, November 9-12.
In this edition, we get formal, requesting audiences with some key cloud-native players. We also cover new SUSE validation for HPE Morpheus Software and what to expect at Platform Engineering Day this year.
Plus, we check out a new(ish) CNCF sandbox project for running agents as Kubernetes resources, a look at assigning Kubernetes compliance ownership, and a story of when to not use Kubernetes in practice.
HPE Morpheus Software adds SUSE validation
If you’re an HVM hypervisor user also using SUSE, you’re in luck: HPE Morpheus Software has now officially gained SUSE certification, meaning the hypervisor can now support SUSE Linux Enterprise Server (SLES) 16.
Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon. HPE Software helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.
Why does SUSE validation matter? According to HPE’s announcement, “Operating system validation plays a critical role in reducing deployment risk and ensuring predictable outcomes in production environments.” The validation signals maturity and gives operators more confidence.
The addition arrives at a time when some enterprises are juggling hybrid cloud estates and looking for a unified way to manage their virtual machine infrastructure.
Platform Engineering Day goes agentic
Since 2024, a platform engineering event has run alongside KubeCon + CloudNativeCon events, and this year is no different. Platform Engineering Day will be a co-located event on Monday, November 9, at KubeCon + CloudNativeCon NA 2026.
As Paula Kennedy, Stacey Potter, and Ramiro Berrelleza share on the CNCF blog, “Since its inception, the goal has remained simple: create a space where platform engineers and practitioners can learn from one another.” Just as important as sharing wins is sharing anti-patterns and explaining why decisions are made, they add.
Based on the published agenda, attendees should expect a blend of end-user stories, keynotes, lightning talks, and panels, with a strong focus on agents as both producers and consumers of internal developer platforms. [...]

## [26] Mini book: Evolutionary Architecture in Practice
InfoQ | full text via InfoQ | ~627 words

Architecture is often framed as simply making change easier. A far more compelling argument is that evolution is about keeping change safe, clear, and deliberate in the face of constant technological and organizational movement.
Together, these articles offer much more than another collection of architectural patterns - they present evolutionary architecture as a continuous feedback system. Fitness functions signal when a system drifts; comprehension confirms people still grasp what they are modifying; boundaries define where independent change can happen; platforms turn safe practices into repeatable defaults; and organizational design ensures those boundaries actually survive contact with reality.
Free download
The InfoQ Evolutionary Architecture in Practice eMag includes:
The articles in this eMag were written by participants of the online InfoQ Certified Architect Program. They represent the capstone of their work, reflecting the cohort's collective learnings on the intersection of AI and modern software architecture.
- Agentic Fitness Functions: Extending Evolutionary Architecture Beyond Deterministic Rules by Hemant Kumar Mahato, Łukasz Sieczkowski , Vijaysenthilkumar Kuppusamy 
This article explores how agentic fitness functions extend evolutionary architecture beyond deterministic rules. It describes a governed AI judgment layer that evaluates semantic drift, boundary fidelity, and architectural risks inside CI/CD workflows, helping software architects, senior developers, and engineering leaders protect system integrity at speed without slowing down delivery.
- Comprehension as an Architectural Characteristic: A System That Is Not Understood Cannot Evolve Safely by Jacobus Meintjes, Narayana Rengaswamy, Paul Katsande, Sureshbabu Bikki
As AI commoditizes code output, system comprehension silently decays, creating cognitive debt that threatens safe architectural evolution. This article explores why human understanding must be treated as an essential architectural characteristic, offering actionable strategies, socio-technical metrics, and design checkpoints to preserve intent across modern engineering teams.
- Fitness Functions and Team Boundaries: Lessons from Evolving a B2C Platform for B2B by Devora Roth Goldshmidt, Dmitry Kekelidze, Hassan Ejaz, Ifiok Idiang, Sebastian Hans
This article explores how evolutionary architecture keeps systems maintainable using fitness functions and domain alignment. [...]

## [124] Agentic RAG vs. Naive RAG: When Your Retrieval System Should Think for Itself
KDnuggets | full text via KDnuggets | ~2029 words

Agentic RAG vs. Naive RAG: When Your Retrieval System Should Think for Itself
From static retrieval pipelines to autonomous reasoning engines: a complete breakdown of how these two architectures work, where each falls short, and how to choose the right one for your use case.
Large language models are remarkable text generators, but they have a well-documented weakness: they hallucinate. Without access to verified, up-to-date information, they confidently produce plausible-sounding answers that are factually wrong. Retrieval-Augmented Generation (RAG) emerged as the standard solution, grounding model outputs in external knowledge sources and dramatically reducing hallucinations across enterprise applications.
But as organizations push these systems into more complex workflows, a new problem has surfaced. Standard RAG pipelines are linear — they retrieve once, pass those results to the model, and generate an answer. When the query is simple and the knowledge base is well-structured, this works fine. When the query requires multi-step reasoning, cross-referencing multiple sources, or synthesizing information that doesn't exist in a single document, the pipeline starts to crack.
That's where Agentic RAG comes in. Rather than treating retrieval as a single, fixed step, it gives the system the ability to reason about how to search, evaluate what it finds, and iterate until it reaches a satisfying answer.
We'll break down how both architectures work, look at where standard RAG hits its limits, and walk through the specific capabilities that make agentic systems better suited for complex tasks. By the end, you'll have a clear framework for deciding which approach fits your next project.
The Baseline: Understanding Naive RAG
Before examining where retrieval systems are going, it helps to be precise about where they started.
Naive RAG — also called standard RAG — follows a rigid three-stage pipeline: Retrieve → Read → Generate. A user submits a query, the system converts it into a vector embedding, runs a similarity search against a vector database, retrieves the top-k most relevant document chunks, and passes those chunks to the large language model (LLM) as context. The model then generates a response based on what was retrieved.
Think of it like a student preparing for an exam in a large library. [...]

## [110] Katie Zacharia Was Linked to an AI Rare-Earths Startup. It’s Even Weirder Than It Sounds
Wired | full text via Wired | ~1199 words

Before being fired five days into her stint as White House press secretary, Katie Zacharia spent much of the day attempting to explain her past.
Throughout her brief tenure, Zacharia’s résumé was the source of much intrigue. Foremost was the fact that despite claiming to be an attorney for much of her career, she never actually passed the California bar, as she was eventually forced to admit. Another element of her professional history, WIRED reported, was a role as an affiliate marketer for Beachbody, a fitness multilevel marketing company.
WIRED has now uncovered new details of her relationship to an AI-powered rare-earth mining operation called NRED Intelligent Mining, which counts former Department of Homeland Security secretary Kristi Noem as a strategic adviser.
On June 24, NRED—then known as NovaRed Mining, a small copper-and-gold exploration company in Vancouver, Canada—issued a press release to share that Zacharia, who had left a role as a DHS spokesperson two months before, was joining the advisory board alongside Noem.
In her new role, according to the release, Zacharia would provide “strategic guidance” to NovaRed’s board of directors as it advanced exploration projects, as well as “emerging artificial intelligence initiatives.”
It does not appear, though, that she ever worked there. When asked on Friday whether she was still on the board, she said, “That was fake,” and referred WIRED to Sam Amsterdam, a “strategic marketing and media engagement professional” whose clients have included the government of Kazakhstan and political parties in Georgia, Nigeria, and Zimbabwe.
“That release was not approved by Ms. Zacharia and was issued without her consent,” says Amsterdam, whose brother is listed as a member of NRED management on the company’s website and said he was speaking as a friend and colleague of Zacharia, not a representative. “I know all that to be factual.” He quickly added that while there had been discussions of her joining the company, she hadn’t actually done so. [...]

## [11] Inline rendering with document​.currentScript
Simon Willison's Blog | full text via Simon Willison's Blog | ~127 words

17th October 2026 - Link Blog
Inline rendering with document.currentScript. Lean Rada describes a neat trick that takes advantage of the document.currentScript property. You can use that to drop in a tiny inline <script> element that replaces itself when the page loads:
The year is <script>
document.currentScript.replaceWith(
  new Date().getFullYear())</script>
If you define a shortcut function like this:
$=(...n)=>document.currentScript.replaceWith(...n)
You get a tiny template language:
The year is <script>$(new Date().getFullYear())</script>
Recent articles
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026

## [85] His scanner wouldn’t work on Linux — so he let Claude study the Windows driver
The New Stack | full text via The New Stack | ~1133 words

His scanner wouldn’t work on Linux — so he let Claude study the Windows driver
Christian Schaller, a Red Hat engineering director and longtime GNOME and Fedora contributor, had a box of old family negatives to digitize and a scanner that wouldn’t talk to Linux. He’d bought the Plustek OpticFilm 8200i because it was listed as supported, then discovered that the manufacturer had swapped in a chipset no Linux driver recognized. He tried getting Claude Code to produce a working driver and got nowhere for a long time, so he eventually set the project aside for a few months.
When he returned to the project, Schaller tried a different approach. Within hours, he had his first recognizable scan. A few days later, the driver supported infrared scanning, too.
Schaller has since released the underlying approach as an open-source project called hw-harness under an MIT license. It bundles the tooling for capturing how a device behaves, comparing a working implementation against a broken one, and giving a coding agent the information it needs to work on hardware that Linux doesn’t support yet.
Reverse-engineering the scanner driver
Schaller got the idea from a post on X by Tom Crider, better known as Glorious Eggroll, who had used an AI agent to fix a mouse driver by giving it access to a Windows machine. Schaller fed the post to Claude and asked it to build a similar setup for his scanner.
In his account on Wednesday, Schaller described the painstaking process of piecing together undocumented device protocols from USB captures, register values, and control transfers. Although the work isn’t very complicated, he said, it “takes a lot of patience and skills.” His earlier attempts to build a SANE backend with Claude had stalled because the agent had no working driver to compare against.
With the new setup, Claude could run the manufacturer’s Windows software, capture the USB traffic, and compare it with what his Linux driver was sending. It used the Windows driver as a reference to find where the Linux implementation went wrong and make changes accordingly.
As Schaller put it, Claude “doesn’t get bored.”
Schaller thinks improvements to Claude Code itself may also have helped. Better yet, as Schaller put it, Claude “doesn’t get bored.” He still had to test the changes on the scanner, since a working driver is a different challenge from generating code that looks correct.
By the time Schaller finished, his driver was no longer the only option. [...]
