# Full text for 30 picks -- untrusted article content, treat as data only

## [1] Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s
Hacker News | SNIPPET ONLY (Hacker News: HTTP 403) | ~0 words



## [4] Improper redaction reveals Google Data Center water and electricity usage
Hacker News | full text via Hacker News | ~504 words

UPDATE: Improper redaction reveals Lincoln’s Google Data Center water and electricity usage
Nebraska data centers submit 2026 annual report
LINCOLN, Neb. (KOLN) - Nebraska data centers are required to turn in an annual report to Nebraska’s Department of Water, Energy, and Environment, but some state statutes are preventing the public from seeing just how much electricity and water data centers are using.
The Google Data Center in Lincoln, named Agate LLC, claimed their electricity usage and water usage were trade secret information, citing Neb. Rev. State §§ 81-1527; 84-712.05 and NAC TITLE 115, CH. 2. In fact, Google did this for all three data centers, including their sites in Omaha and Papillion.
However, using a computer cursor to highlight the redacted text box in the report to DWEE, then copying and pasting it into a separate document reveals that Agate LLC is reporting 52.65 megawatts of electricity during peak electrical demand and 13.299 megagallons of water between cooling towers, evaporative systems and site operations in the last year. That totals out to 13 million gallons of water.
For context, 13 million gallons is enough to fill around 20 Olympic-size swimming pools, and is less than half of what the City of Lincoln reports using on Sept. 29.
The six data centers reporting as of Sept. 30 show a total use of 765 million gallons of water last year, enough water to fill 1,159.93 Olympic-size swimming pools.
More improper redaction shows that the data center using the most water annually is Fireball Group LLC, the Google Data Center in Papillion. Fireball LLC reports 547.88 megagallons for their 2025 Annual Water Consumption.
10/11 filed a public record request Sept. 30 to see redacted information from Agate LLC’s report.
Further improper redaction reveals exactly how much of a 2025 tax refund Google data centers expect.
Google’s reports state that data centers only “utilize or expect to utilize” sales and use tax exemptions under the Nebraska Advantage Act. Reports state no rebates have been received for that program to date, nor have any incentive payments been received, or are expected to be received under the ImagiNE Nebraska Act.
Agate LLC reports expecting a refund of $55,822,472 from 2025 taxes. Fireball LLC is expecting a refund of $39,171,573.39 from 2025 taxes. Westwood Solutions LLC, the Google-owned data center in Omaha, is expecting a refund of $22,558,881 from 2025 taxes. [...]

## [5] Why don't more developers “use the platform”?
Hacker News | full text via Hacker News | ~1751 words

Why don’t more developers “use the platform”?
For years, advocates for web standards, performance, and accessibility have implored web developers to “use the platform”. I’ve often been one of those advocates.
The argument is simple: why build something yourself, in JavaScript, when the browser can do it for you? Whatever you build, it’s likely to have poorer performance and worse usability than something the browser could just give you out-of-the-box.
I think it’s worth taking the other side, though, if for no other reason than to understand where the “platform-skeptic” developers are coming from. If “use the platform” is so obvious, then why do so many people seem to need convincing?
The most obvious reason is historical: for the longest time, browsers were playing catch-up with the ecosystem on top of them. Libraries like jQuery filled crucial gaps while browsers implemented equivalent APIs – and even then, you might have to wait for laggards like IE6 to age out before you could actually use them. Today, most browsers are evergreen (Safari is debatable, although ~7 times per year ain’t bad), but up until the 2020s or so, web developers had to deal with a decidedly lumpy web. In that environment, rolling your own is a sensible choice.
Another reason is familiarity: when you’re used to looking for React components on npm, that’s what you tend to reach for, regardless of the problem at hand. If you search for “sticky positioning” on npm, there’s no package that says “just use CSS position: sticky, you dolt.”
And often, even with a robust standard, libraries on npm would fill a useful gap between framework ergonomics and the platform underneath it. I always found it intriguing that many React developers preferred to stick to JSX and React idioms – raw DOM APIs felt “icky” – but were perfectly happy to use lower-level libraries where raw DOM manipulations are common. For example, a virtual list library might happily use raw DOM APIs for pure performance, while exposing higher-level primitives that a novice React developer could better grasp. In a sense, the ecosystem of React components led to a natural division of labor where those with more expertise packaged up unfamiliar platform APIs in a more familiar form factor.
Some of this effect was also driven by documentation. Many npm packages have lovingly detailed READMEs or websites with examples, tutorials, and screenshots. [...]

## [9] Iroh global content discovery
Lobsters | full text via Lobsters | ~3314 words

Iroh global content discovery
by Rüdiger Klaehn
What got me excited about IPFS many years ago, briefly after it was announced, was being able to publish a personal website, blog post, or political pamphlet and have it remain available globally as long as enough people are interested in the content. As governments have been more sophisticated in their firewalling methods, this use case for circumvention tools and permissionless global content discovery is still incredibly relevant.
Recent events have added some urgency to this. IPFS shipyard is shutting down. This does not mean that IPFS will stop working, but it does not bode well for the future of the project.
The state of the art
When we had to solve hole punching, we started looking at existing systems and chose the best open source system as an initial starting point for our own implementation. So let's do the same for global content discovery.
There are a number of projects trying to solve this problem. But one project stands above all others: BitTorrent. It just works and has done so for over two decades.
So let's take a look at what makes BitTorrent the current leader in permissionless global content discovery. BitTorrent has a relatively simple protocol for blob transfer and a DHT called Mainline for global content discovery.
The transfer protocol and content discovery are separate systems. In fact, the DHT was developed later than the transfer protocol. BitTorrent was released in 2001 using centralized trackers for content discovery; the Mainline DHT was added in 2005.
Transfer protocol
BitTorrent works by creating a .torrent file that contains information about the data to be downloaded. The file is encoded using bencode, which is conceptually similar to JSON.
{
  "announce": "http://tracker.example.com/announce",
  "comment": "Ubuntu 24.04 desktop image",
  "created by": "mktorrent 1.1",
  "creation date": 1714521600,
  "info": {
    "name": "ubuntu-24.04-desktop-amd64.iso",
    "piece length": 262144,
    "length": 5820411904,
    "pieces": 9358b5d71f8007ac926000961ad79d865d9652bc
              4cce840457bcfac1dd67d864e9386422eee70904
              … many more 20-byte hashes …
  }
}
pieces contains the concatenated SHA-1 hashes of all piece length-sized pieces. [...]

## [12] Google's Android Security State Libraries Enable Component-Level Security Verification
InfoQ | full text via InfoQ | ~458 words

Google's AndroidX Security State libraries enables apps to verify security patch status at the individual component level, rather than relying on a single, device-wide security patch date.
With the introduction of the AndroidX Security State and Security State Provider libraries, Google provides a centralized mechanism for assessing Android device security, enabling more granular verification and greater flexibility.
Whether you develop security-critical, consumer-facing apps (such as banking, fintech, or healthcare) or Mobile Device Management (MDM) solutions, these libraries enable you to programmatically verify the security state of the device per component.
The Security Patch Level (SPL) is a monolithic patch number that encompasses the entire system software stack running on an Android device. The new mechanism enables component-level security verification and provides more precise visibility into available remediations.
The Security State library defines three distinct patch levels: Device SPL, Published SPL, and Available SPL. The Device SPL is queried directly from the running system without requiring network access and indicated the security patch level currently installed. The Published SPL represents the latest patch level officially published by Google for a given component. The Available SPL identifies the patch level that is available for download and installation on the specific device.
At the component level, the Security State library distinguishes among the core Android OS (system), OS subsystems updated via Google Play (system modules), and kernel.
By surfacing these three distinct patch levels at the component level, developers and enterprises can now understand exactly how secure a device is, identify missing patches, and take proactive remediation steps.
For example, banking and enterprise apps can use Device and Available SPLs to ensure a device is secure before allowing sensitive actions. Rather than simply rejecting a request, they can require users to install specific OS component updates first. Developers can also check for the patch status of specific CVEs before allowing security-sensitive operations using a certain hardware o software component (.e.g. NFC or Bluetooth).
The library provides a queryAllAvailableUpdates() function as well as a fetchAvailableSecurityPatchLevel() which aggregates data retrieved from current device to discover pending security updates across system components. [...]

## [17] Pizza Bot: Open-Source Inbox for Background AI Agents
InfoQ | full text via InfoQ | ~492 words

A team of developers working at AWS recently open-sourced Pizza Bot, a self-hosted application designed to let AI agents run tasks in the background and return results through an inbox-style interface. Agents can perform scheduled or webhook-triggered work, delegate tasks to specialized workers, and pause for human approval when needed.
Pizza Bot provides an email-style inbox for managing long-running AI agent workflows. The Apache 2.0-licensed tool uses a client-server architecture, allowing users to delegate complex tasks without continuous monitoring.
Source: AWS blog
Described by the authors as an option that offers "the developer details, minus the grease," Pizza Bot supports multiple model providers, MCP servers, and Agent Skills while keeping data and agent state on the user’s machine. Joseph Dolivo, principal technologist at AWS, and Igor Fil, solutions architect at AWS, use the inbox analogy to explain the design:
You don’t send an email and then sit watching the outbox until the reply lands. Pizza Bot is shaped like an email client for the same reason: a thread is a unit of work you come back to rather than a session you have to attend.
Source: AWS blog
The design is based on four requirements: agents can inspect multiple sources, work in the background, request approval before consequential actions, and notify users when work is complete. The inbox organizes this work into All, Unread, and Action queues, while an Activity panel shows tasks delegated to specialist agents and their progress.
Pizza Bot persists agent state, threads, checkpoints, attachments, and logs locally in a user-controlled folder, sending data only to the configured model provider and explicitly enabled MCP servers, with credentials stored in the OS secret store. Dolivo and Fil add:
You control what leaves the machine. Pizza Bot sends prompts and attachments to the model provider you chose, and tool calls to the MCP servers you enabled. Those servers can act on your behalf, which is worth remembering when you install one.
On LinkedIn, Dolivo acknowledges that the name is a direct homage to Amazon’s two-pizza teams and documents the project’s early days:
In April of 2025, I started a side-of-desk passion project called "JoeBot" to automate tedious, repetitive CRM logging. Today, that idea has evolved into something much bigger (...) It worked great for technical users, but as soon as non-technical folks got wind of it, they wanted in, too. [...]

## [18] Reproducing Olmo 3 7B Pre-training in MaxText: case study of large scale training on TPUs
Google Developers Blog | full text via Google Developers Blog | ~3431 words

Olmo 3, developed by the Allen Institute for AI (Ai2), is a state-of-the-art, fully open language model trained with a modern architecture and a multi-stage training recipe. To evaluate the capabilities of MaxText on Google Cloud TPUs, our team set out to reproduce Ai2’s Olmo 3 7B from scratch. We chose Olmo 3 because it combines three properties that rarely appear together. It is a strong, modern 7B model trained at real production scale. Ai2 exposes the complete model flow, including data, code, configurations, checkpoints, logs, and evaluations. And finally, it gives us an independent PyTorch and GPU reference against which we can test MaxText and TPUs.
We reproduced Ai2’s Olmo 3 7B in MaxText on Google Cloud TPUs, both the stage-1 pre-training and the stage-2 mid-training anneal, and proved the match on held-out metrics, not just the loss curve:
The main highlights, each covered in detail later in the post:
Starting from Ai2’s step-0 PyTorch weights and the same core recipe, the MaxText run tracks Ai2’s published loss curve over the full ~5.93T-token / 1.41M-step budget and lands on top of it at the end of stage-1. We even simplified two recipe details (a single cosine LR schedule where Ai2 stitched two, and the publicly released data mix; see the recipe below), and the match held anyway. The rest of this post is how each of these was built, measured, and, in one instructive case, nearly faked.
Olmo 3 is one of the few genuinely open frontier-class language models: open weights, open data, and a fully specified training recipe with a public reference run on Weights & Biases. Matching that independently trained run, on held-out metrics rather than just the loss curve, is strong evidence that the MaxText stack (optimizer, loss, data pipeline, numerics) is faithful, not just “looks like it’s training.”
MaxText is a JAX/XLA LLM training framework built for TPUs. The question we set out to answer: can a PyTorch-on-GPU recipe be reproduced faithfully in JAX-on-TPU, matched on the metrics that matter rather than bit-for-bit, and how do you prove it?
Olmo 3’s recipe is a 3-stage curriculum: general pre-training, mid-training (annealing), and long-context adaptation. This post covers stage 1 (the ~5.9T-token pre-training run) and stage 2 (mid-training), both trained end to end and matched against Ai2’s references. Stage 3 and post-training (SFT/RL via Tunix) are recipes we’ve written but not yet run. [...]

## [19] Turn your REST APIs into MCP tools with Google Cloud API Gateway
Google Developers Blog | full text via Google Developers Blog | ~758 words

Most enterprise capability sits behind REST APIs that agents cannot see. To make one callable by an agent today, teams typically stand up and operate a separate MCP server that re-implements the routing, authentication, and quota logic their gateway already handles. The Model Context Protocol (MCP) has become the standard way for agents to discover and invoke tools, and frameworks like the Agent Development Kit (ADK) and Gemini Enterprise speak it natively.
Google Cloud API Gateway now closes that gap. In Public Preview, API Gateway can act as a remote MCP server: annotate the OpenAPI spec you already deploy, deploy it, and your existing REST operations are available as agent-ready MCP tools — with no separate server to build, host, or maintain.
API Gateway is the lightweight on-ramp in Google Cloud's gateway lineup. If you have a service on Cloud Run and you want its API secured, managed, and exposed to agents in minutes, this is the fast path. For a full enterprise API and MCP platform — lifecycle management, advanced traffic policies, monetization — use Apigee. To govern what your agents call on the way out, including MCP servers like this one, use Agent Gateway. Model routing, which gives you one stable endpoint for outbound LLM calls, is the companion capability for the other direction of AI traffic.
API Gateway accepts standard MCP JSON-RPC requests on a single endpoint, transcodes each tools/call into the corresponding REST request, applies your existing policies, and translates the response back. Because the transcoded request is indistinguishable from a normal REST call, the JWT or API-key authentication, quota, and logging you already configured for that operation keep working unchanged — MCP and REST traffic share exactly one policy path, and a given operation draws on one quota allocation however it is invoked.
x-google-api-management.mcp, and customize or skip individual operations with x-google-mcp-tool. Each exposed operation needs a backend and a non-empty description.openapi: 3.0.4
info:
  title: Order Service
  version: 1.0.0
x-google-api-management:
  mcp: true                 # expose this spec's operations as MCP tools
  backends:
    orders-backend:
      address: https://orders-a1b2c3-uc.a.run.app
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderStatus
      description: Returns the current status, carrier, and ETA for an order. [...]

## [20] Introducing Support for Local AI Models in the Antigravity SDK
Google Developers Blog | full text via Google Developers Blog | ~714 words

Today, we’re announcing that the Antigravity SDK supports local workflows across a wide range of local models and execution options, featuring initial support for Gemma 4 26B A4B using Google AI Edge’s LiteRT.
The Antigravity SDK enables developers to build with the same agentic capabilities that power Google Antigravity. With this new support you can enable agentic assistance via local models completely offline. We’ve optimized this workflow for LiteRT and Gemma 4 26B, efficiently using the local GPU and RAM in order to further amplify what your local machine is capable of delivering!
Local model execution offers several advantages for agentic experiences:
Here is how you can get started: (We recommended a machine with >24GB VRAM or unified memory).
python3 -m venv .venv
source .venv/bin/activatepip install google-antigravity litert-lm
litert-lm import \
  --from-huggingface-repo=litert-community/gemma-4-26B-A4B-it-litert-lm \
  gemma-4-26B-A4B-it-gpu.litertlm \
  gemma4-26b
In your directory, create a file called agy_sample.py. Paste the following contents into it.
import asyncio
import os
from google.antigravity import Agent, LiteRTAgentConfig
from google.antigravity.hooks import policy
# UPDATE: Point to the locally downloaded model from the previous step (litert-lm import ...)
MODEL_PATH = os.path.expanduser("~/.litert-lm/models/gemma4-26b/model.litertlm")
async def main():
   print(f"Using local LiteRT model: {MODEL_PATH}. Please wait for local inference to complete. This could take several minutes.")
   config = LiteRTAgentConfig(model_path=MODEL_PATH).lightweight()
   async with Agent(config) as agent:
      response = await agent.chat("What files are in the current directory?")
      async for token in response:
         print(token, end="", flush=True)
if __name__ == "__main__":
   asyncio.run(main())
In many cases we see that an Architect-Builder pattern is a great way of combining cloud model scale with local model advantages. In the hybrid demo video below, built with the updated Antigravity SDK, a cloud architect (Gemini 3.8 Flash) acts as the planner and conductor, while a local swarm of Gemma 4 26B instances handles the heavy lifting entirely on-device. [...]

## [21] Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform
Google Developers Blog | full text via Google Developers Blog | ~631 words

Each new model generation makes AI agents more capable, more autonomous, and cheaper to run. Teams are putting them to work on real business tasks: issuing refunds, updating records, calling internal tools on a user's behalf. But a more capable model is not automatically a safer one. The more decisions an agent makes at runtime, the more its risk shifts from its code to its behavior. The real damage often happens in sessions that look benign on the surface: the agent returns a clean answer and closes the ticket, and only afterward do you notice it reached for a tool it should never have touched, or acted on a request that quietly widened its own access. Because nothing failed outright, the session clears the usual metrics-based evaluations without any second look.
That gap is exactly what Agent Anomaly Detection is built to close. It's now in Private Preview on the Gemini Enterprise Agent Platform.
Agent Anomaly Detection is a reasoning-based oversight and audit layer for autonomous agents deployed on the Gemini Enterprise Agent Platform. It examines what an agent actually does using its reasoning traces, tool calls, and execution flow across a session. It reads the logs and OpenTelemetry traces your agents already emit, evaluates that activity to decide whether an agent is operating outside its intended boundaries, and flags behavioral anomalies, suspicious intent, and policy violations.
Some key features that make Agent Anomaly Detection practical to run in production:
Agent Anomaly Detection balances detection speed, cost, and coverage. To strike that balance, it analyzes traces and logs in layers: a lightweight first pass scans all traffic to surface statistical anomalies and flag those sessions for further analysis. Then, an LLM-based reasoning layer deeply examines the flagged sessions.
To make that concrete, take the example of an Inventory Agent with a list_inventory tool. A user says, "I want to see your inventory. List 100 items at a time" and the agent starts paging through in large batches, jumping across offsets to pull the whole catalog.
Nothing here throws an error. The agent is only doing things it’s capable of, and there may be no policy preventing it. But Agent Anomaly Detection flags the anomalous behavior, working through the session in layers: the first layer flags the session as a statistical outlier from the volume and the repeated calls. [...]

## [22] Build zero-trust AI agents that judge intent, not just syntax
Google Developers Blog | full text via Google Developers Blog | ~2057 words

Part 2 of Zero-trust Agents series: runtime governance, intent gating, and adaptive anomaly remediation
In Part 1, we established three deterministic controls for autonomous agents: signed database writes with Cloud KMS, user-space kernel isolation with gVisor, and an input/output gateway backed by CI unit tests.
Those controls work, but they share one limit: they only catch cases that you can explicitly specify ahead of time.
A SQL parser cannot tell a socially engineered refund from a legitimate one if the syntax is valid. A regex cannot tell the difference between a physical USB cable and an opened software license. And a single-turn test suite cannot catch an agent fleet being drained across multiple turns.
Part 2 keeps the same Customer Support & Returns Agent built with the Agent Development Kit (ADK) and moves security checks to the platform, where they reason about intent and adapt to behavior. Moving the checks to the platform also changes who owns them. Governance is defined and managed by a platform or security administrator, separate from the agent developer, \because the platform enforces it outside of the agent code.
Deploying to the Gemini Enterprise Agent Platform, we replace self-hosted container infrastructure and explicitly managed regex lists with managed runtime governance: Model Armor, Semantic Governance Policies, and Agent Anomaly Detection with Closed-Loop Remediation.
We kept the same Customer Support and Returns Agent from Part 1. It looks up orders, computes restocking fees, and pays refunds against a merchant ledger. When a customer asks for a return, the agent reads the order with verify_order and determines the final refund amount with calculate_restocking_fee, which runs inside Agent Sandbox, the platform's managed sandbox for model-generated code. If the refund checks out, it calls issue_refund to commit the payout, signing the request with the agent's own Cloud KMS asymmetric key, the same hardware-backed identity from Part 1. In production, an agent would typically invoke these capabilities through tools exposed via the Model Context Protocol (MCP) or backend APIs. For simplicity in our companion demo, we implement them directly as local Python functions.
To keep the attacks concrete, we run all of them against a single transaction: Order #99281, $149.00 in total. It carries two line items: a USB-C Pro Docking Station and Cable at $29.00, and an annual Workplace User License at $120.00. [...]

## [24] We're going to need default hard budget caps on pretty much everything
Simon Willison's Blog | full text via Simon Willison's Blog | ~530 words

We’re going to need default hard budget caps on pretty much everything
3rd October 2026
Here’s a product feature which the world is going to need a whole lot more of over the coming months and years: default hard budget caps. I’m talking about the feature of pay-by-usage services and APIs that lets you say “after $X/month, cut this thing off and return errors”. These need to be hard limits. Soft caps, “after $X/month, send me a warning email”, will not cut it.
Coding agents, and personal agents (coding agents wrapped in a less threatening UI), greatly reduce the friction of spinning up code that can do useful things. Sometimes those things cost money—calls to paid APIs, or hosted web applications, or systems that can bill for additional storage and compute.
Nobody wants to wake up to an email sent at midnight warning about a budget limit and find that, while they slept, their rogue service had consumed several hundred (or several thousand) more dollars of usage.
An argument against this is that businesses don’t want their hosted applications to start throwing errors because some budget was exceeded. I expect that most businesses and individuals would prefer errors to a surprise $10,000+ bill.
I think hard budget caps need to be the default. If someone wants to live dangerously they should be able to do that, but it needs to be on an opt-in basis. Have a nice, clear checkbox somewhere prominent:
Remove the budget cap. My application will not be shut down if I exceed the configured budget limit, and I will be responsible for subsequent charges.
The service I most want to see this from is AWS. I’ve heard plenty of stories from people who refuse to use AWS for personal projects out of (justified) fear that a runaway service might bankrupt them. I’ve also heard stories from people who didn’t anticipate this and ended up seriously burned.
... and it turns out AWS finally launched spending limits a few weeks ago! From their announcement New AWS experience helps builders get started and ship faster on 16th September:
When you’re ready to upgrade to a paid plan, you can set a monthly spend limit for your project based on your usage patterns so that you stay within your budget. If a project’s usage reaches its spend limit, your project is paused for that month. [...]

## [28] Presentation: Building GenAI Platform at DoorDash
InfoQ | full text via InfoQ | ~7543 words

Transcript
Swaroop Chitlur: My name is Swaroop. This is Sidd. We started this team called GenAI Platform at DoorDash, and this is sharing our story about all the things that we did to make a successful platform. We talk about the principles, the bets, the pivots, and what do we mean by success. How many of you are shipping GenAI-based projects at work? How many of you are in a platform type of function where you are supporting other teams be successful at this? Hopefully some of the things we talk about will resonate with you all. Our journey actually starts in roughly April '23. As you know, November '22 was the ChatGPT moment. Then a few months later, we were like, we need to start using OpenAI. I was tasked with signing this contract, and I remember I was sweating, like, are we really going to spend this much money? Of course, in hindsight, that number seems minor now.
The feeling was very real because at that moment, I was like, if this thing takes off, how do we support this in such a large company? How do we make this productive? How do we make this accountable? That set the tone for what we were planning on. The thesis of this talk is very simple. We had initial principles and bets in mind. As the industry evolved and started doing newer things, we started adapting accordingly. We were still able to navigate these changes because we had those principles in place. Of course, we went from models to workflows to agents. That's where we'll walk you through our journey and what decisions we took, and talk about the technical projects in some of them. You get a balance of what was our strategy and what was the technical proof and what was the results. Hopefully those are takeaways for you at the end.
Operating Model
When we say about principles, what do we mean by that? When we started this team, we were given a blank slate. What do you do next? I don't know. Then you start thinking, first let's decide how are we going to operate? What are we going to decide on? We didn't come up with these. This was already part of our foundations or tenets. Be customer obsessed. Focus on the teams and the use cases. Not building for the sake of building product. Build products, not systems. Our customer is a product engineer. Don't make things where your customer has to stitch together different workflows. Try to think of an end-to-end workflow. Think of onboarding, think of support. Think like a product team, not just building systems. Make the right thing easy. [...]

## [29] Istio 1.31 Adds Agentgateway Waypoints and Moves Release Artifacts off Google Cloud
InfoQ | full text via InfoQ | ~545 words

Istio 1.31, released on 31 August, lets teams run agentgateway as a Layer 7 waypoint proxy in an ambient mesh, using the new istio-agentgateway-waypoint GatewayClass.
The same release stops publishing container images and Helm charts to Google Cloud. Teams still using gcr.io/istio-release, registry.istio.io, or the Google-hosted Helm repository should migrate before the next scheduled outage test on 13 October, ahead of their retirement in December. Istio 1.31.0 is supported on Kubernetes 1.32 to 1.36.
The waypoint support builds on the experimental gateway-only integration added in 1.30. Agentgateway is a Rust data plane built for agent traffic, donated by Solo.io to the Linux Foundation, and it handles protocols such as the Model Context Protocol alongside ordinary HTTP. Istio 1.31 also fixes ListenerSet handling and mTLS connectivity for agentgateway backends. Traffic shifting between waypoints is alpha, and the maintainers warn that the labels, annotations, and behaviour may change.
That shifting mechanism is new too. A service or namespace can name a canary alongside its primary waypoint through the use-waypoint-canary label, then send a configurable share of new in-mesh connections to the canary using the use-waypoint-canary-weight annotation, with no client-side changes. Established connections are not moved, so long-lived connections can delay the observed traffic split.
Istio 1.31.1, released on 21 September, fixes an issue where agentgateway waypoints referenced only as canaries were not programmed with the routes and policies of the services referencing them, causing shifted connections to be rejected. The patch also includes security fixes and corrects ALLOW_ANY_DYNAMIC_DNS forwarding in IPv6-only clusters.
Two traffic management additions stand out for large meshes. A new zoneAwareLbSetting field on DestinationRule and MeshConfig lets Envoy route to endpoints in the downstream proxy's own availability zone and spill over only when local capacity runs out, which Envoy decides automatically rather than through the static percentages localityLbSetting requires. The ALLOW_ANY_DYNAMIC_DNS outbound mode resolves hostnames from the HTTP Host header at request time, removing the need to write a ServiceEntry for every external destination.
On security, a fips-140-3 value for the COMPLIANCE_POLICY environment variable restricts TLS to version 1.2 or later, FIPS-compliant cypher suites and P-256 and P-384 curves. [...]

## [31] I built my husband a vim trainer with a Gemma coach that runs in the browser
Dev.to | full text via Dev.to | ~1619 words

This is a submission for the Hacktoberfest Weekend Challenge: Build for a Friend
What I Built
A lot of my friends build their own tools. They hit a problem and just make the thing they want. I wanted to build something for someone else this time, and the answer was sitting right next to me.
My husband has wanted to learn vim for a long time. He's tried a bunch of times, and it always ends the same way: he gives up. When I asked him why, it came down to two things. There are too many commands to memorize, and everything feels slow and awkward compared to what he's used to.
So I built hjkl, a browser app that teaches vim in tiny drills.
Each drill gives you a small buffer, a goal, and a keystroke "par" to beat. You solve it in a real vim editor, not a simulation. A few things I designed around his actual problems:
- Only a few commands at a time. Each lesson introduces a small set of commands, with a cheat sheet always on screen.
- 
Every command shows the VS Code habit it replaces. dd is Ctrl+Shift+K, o is Ctrl+Enter, ciw is roughly Ctrl+D and type. If there isn't a real equivalent (like . or f), it just says so.
- Par instead of pass/fail. You always finish the drill. If you took the long way, you see the shorter answer right there.
- A Review list. Any drill you solved over par goes into Review, worst first, and drops off once you hit par. Those are exactly the commands that haven't stuck yet.
- A full Vim reference. The lesson cheat sheet only shows what you're currently learning, but there's also an All Commands reference with everything covered in the app. You can search it by key, action, or the VS Code shortcut you're used to.
- 
Plain names under weird keys. <CR> shows "Enter" underneath and <Esc> shows "Escape". I added this after I had to ask what <CR> meant myself while testing.
Right now there are 17 lessons and 124 hand-written drills, starting with basic movement and insert mode and working up through text objects, counts and combos, search, visual mode, substitutions, macros, registers, and more.
Then there's the AI part, which runs entirely in the browser.
When I handed it over to him, he actually sat there and worked through it for a while, which felt like a pretty good sign considering every previous attempt at learning vim had ended with him giving up. He liked the short drills and being able to see the more efficient answer when he took the long way. More importantly, he kept going without me having to convince him to. [...]

## [38] Valkey 9.2's forkless BGSAVE cuts my memory spike from 350MB to 10MB
Dev.to | full text via Dev.to | ~1491 words

Every BGSAVE I have ever watched on a busy Redis or Valkey instance does the same thing: the process forks, and for a few seconds the host's free memory drops like someone pulled a plug. Valkey 9.2.0-rc1, tagged on Docker Hub on 16 September, adds a way to skip the fork entirely. I wanted to know what that actually buys you, not what the release notes say it buys you, so I ran both paths against the same dataset and measured what happened.
The short version: the memory spike nearly disappeared, and the save got noticeably slower doing it.
The setup
I pulled valkey/valkey:9.2.0-rc1 and ran two containers from the identical image, differing only in one setting. The first used the default: bgsave-default-method fork. The second started with --forkless-infrastructure-enabled yes --bgsave-default-method forkless, which is the only way to turn it on — more on that below.
Into each I loaded 3,000,000 keys at 300 bytes each, a little over 1.1GB of data (used_memory reported 1.04GiB). Then, against each container, I ran eight threads hammering SET on random existing keys as fast as they could go, and from a ninth connection I sent a PING every 2ms and timed the round trip. Two seconds into each 12-second run I fired BGSAVE. I repeated this seven times per mode.
This setup matters for one reason: copy-on-write only costs you anything if pages are actually being written while the fork holds them. A BGSAVE against an idle dataset tells you almost nothing. Mine wasn't idle — the eight writer threads pushed roughly 27,000 operations a second into whichever container was running fork mode.
The memory spike, measured twice
I tracked two numbers: the RDB-reported copy-on-write size (rdb_last_cow_size in INFO persistence), and the container's own cgroup memory usage sampled every 150ms through the save.
The two memory measurements agree with each other, which is the point of taking both: the kernel's own copy-on-write accounting and an independent cgroup memory sample converge on the same number through two unrelated instruments. On a 1.1GB working set under sustained writes, forking cost roughly a third of the dataset's size in extra memory, every single time, with a tight range of 319.6MB to 367.5MB across the seven runs. Forkless never went above 10.0MB.
That is the headline, and it held up every time I ran it. But it's not the whole story.
What the smoother memory curve cost
The forkless save took 5 to 6 seconds against fork's steady 3. [...]

## [52] ‘A meaningful risk’: Oracle’s massive 1.3 GW Wisconsin AI campus faces severe power delays as grid review restarts — pushing customer delivery past 2027
TechRadar | full text via TechRadar | ~666 words

‘A meaningful risk’: Oracle’s massive 1.3 GW Wisconsin AI campus faces severe power delays as grid review restarts — pushing customer delivery past 2027
Grid connection for a 1.3GW data center just hit the reset button
- Oracle's Wisconsin campus may have finished buildings long before electricity arrived
- Regulators withdrew their completeness finding after ATC filed 564 additional documents
- Ten months of review ended without a decision and restarted from zero
Oracle’s massive 1.3 GW AI data center campus in Wisconsin, dubbed Project Lighthouse, faces severe power delays after regulators restarted the review needed to connect it to the grid.
The campus in Port Washington is being developed by Vantage for Oracle, with four data centers planned across the site.
Construction is advancing, but the campus cannot begin serving customers at scale until the required transmission infrastructure receives regulatory approval and gets built.
A review clock reset to zero
In September 2025, American Transmission Company (ATC) asked the Public Service Commission of Wisconsin (PSC) to approve the new high-voltage line serving the campus.
By December 2025, the PSC found the application complete and began its formal review, which started the legal countdown for a decision.
However, between January and July 2026, ATC altered the project and filed 564 more documents that changed routes, introduced temporary bypass lines and updated cost estimates.
An administrative law judge ordered ATC on 1 July to itemize each alteration and found on 15 July that the company had not complied.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
Because the PSC lacked confidence about the exact scope under review, it withdrew its completeness finding in August 2026, ten months after the case opened.
Such late additions would need further environmental review that the legal deadline left no room for, so the project risked approval by default.
The PSC closed the case on September 10 2026 without ruling on the merits, and ATC refiled on September 18, restarting the statutory clock.
Buildings can advance before electricity arrives
Construction itself does not appear to face the same scheduling problem affecting the transmission connection serving the Wisconsin campus. [...]

## [76] Agents have made CI the bottleneck. Faster pipelines are the wrong fix.
The New Stack | full text via The New Stack | ~1458 words

Agents have made CI the bottleneck. Faster pipelines are the wrong fix.
Three posts landed in September that I think engineering leaders should read together.
Anthropic’s engineering team wrote that their continuous integration (CI) job volume grew 25x in six months. Their engineers now ship about 8x as much code per quarter as they did from 2021 to 2025. The fix they shipped was test impact analysis: run only the tests a change could affect.
A week later, Linear published a post titled AI coding has made CI a bottleneck. Their test suite has nearly quadrupled since January, and agents now write most of their tests. They reworked the pipeline end to end to keep up.
Then Depot’s CEO wrote that CI is changing, and that the future is “giving agents a way to validate code and maintain trust as they work.”
Anthropic and Linear do not sell CI tooling. They are reporting what happened to their own pipelines, which is what makes it worth paying attention to. Here is my read: all three are right about the problem, and two of them are fixing the wrong layer.
How CI became the bottleneck
For twenty years, CI was sized for human output. A developer opened a few pull requests (PRs) a week, and the pipeline ran after each one. If it took 20 minutes, nobody cared much, because the developer was already on the next task.
Agents broke that arithmetic in two ways. First, volume. When one engineer runs several agents in parallel, PR count goes up by a multiple, not a percentage. Anthropic’s 25x number is not an outlier. Blacksmith, which sells CI runners, says the number of CI jobs it runs has grown between 5% and 10% week over week.
The agent is fast, and the loop around it is slow.
Second, placement. CI runs after the PR exists. An agent that writes code, opens a PR, and waits 20 minutes for a red check has lost its working context by the time the result comes back. Every failure costs a full round trip. The agent is fast, and the loop around it is slow.
So the industry did the obvious thing and made CI faster. Faster runners, smarter test selection, bigger caches, pipelines that agents can call before commit. All of it helps, and all of it is necessary. All of it also leaves one assumption untouched: that what you’re verifying is a repository.
What a green pipeline does not tell you
For a standalone application, a repository is the system. Run the tests, and you know most of what you need to know.
For a cloud-native system, a repository is one service out of forty. [...]

## [79] How to Govern AI Agents
Towards Data Science | full text via Towards Data Science | ~1709 words

How to Govern AI Agents
From guarding one agent to steering a fleet
This time last year, I released a Deeplearning.ai course with Andrew Ng on Governing AI agents with the goal of educating developers on the basics of data protection for effective and responsible agent deployment. The motivation for the course came from IBM's 2025 breach study, which found 97% of the organizations that suffered an AI-related breach lacked proper AI access controls, and 63% had no AI governance policy at all.
A year is an eternity in AI development, and we have come a long way from agents with zero governance or grappling with governing a single agent. Teams are now confronting a new governance challenge: agent sprawl (the uncontrolled growth of autonomous AI agents across an organization without centralized tracking, ownership, or governance). According to Gartner, by 2028 the average Fortune 500 enterprise will use over 150,000 AI agents. However, according to the firm, only 13% of organizations believe that they have the right AI agent governance in place. Since last year, the ability to deploy has gotten easier than ever. The onset of coding agents like claude code and codex, as well as a variety of low-code/no-code options have lowered the barrier to agent deployment substantially. One result is teams are now faced with the possibility of their agent fleet engaging in hugely wasteful token usage and incurring unforeseen costs. Another serious challenge is the additional pathways for sensitive data to leak out. Unsurprisingly, governance challenges have evolved.
Currently, I'm watching customers build agents faster than ever, and the shape of the problem has shifted. A year ago we focused on adding the four pillars of governance to a single agent: lifecycle management, risk management, security and observability.
We knew even then that building an agent wasn’t the hard part. You can stand up an agent in an afternoon, wire in observability, point it at a copied-over slice of data, and it looks as if it’s production-ready. Then you try to run it for real, against live systems and at scale, and you hit the wall that actually matters: infrastructure at scale. Now, this hasn’t changed, but what’s the shift? The difference is this is happening with dozens of agents/sub-agents at the same time. Agents are multiplying faster than a lot of teams are able to govern them. [...]

## [95] openSUSE Turns To ZUPT For Post-Quantum Backups
Phoronix | full text via Phoronix | ~136 words

openSUSE Turns To ZUPT For Post-Quantum Backups
OpenSUSE developers have announced they are making ZUPT available on their Linux distribution as a solution for providing post-quantum backups. ZUPT combines backup creation, compression, integrity verification, and encryption all via this single open-source utility.
ZUPT provides AES-256-based encryption as well as a hybrid cryptographic scheme based on ML-KEM-768 + X25519. The hope is that ZUPT backups will remain resilient against future cryptographic threats.
ZUPT leverages CPU multi-threading for faster performance during the backup / compression / encryption processes. ZUPT was accepted into openSUSE Factory to become an "officially integrated solution" across the life-cycle of system backups to compression and encryption protection in the openSUSE ecosystem.  More details on the openSUSE side via news.opensuse.org.
Those wishing to learn more about ZUPT itself can do so via the project's GitHub.

## [53] How Python Will Test Adding Rust Into CPython
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~92 words

Python's security developer-in-residence Seth Larson reports from this year's official core developer Python Language Summit: "No one said 'don't do this' last year". After testing the waters at PyCon US 2025, [software engineer] David Hewitt returned to the Python Language Summit asking what Python core developers want from Rust, along with proposed timelines, phases, and success criteria for how the Rust for CPython project might proceed and become a permanent fixture within the CPython project. David is acting as an "ambassador" for the Rust for CPython project team, which is currently le

## [58] Google froze its open source bug bounty program due to a ‘significant rise’ in AI submissions
TechCrunch | full text via TechCrunch | ~154 words

Blaming a “significant rise” in AI submissions, Google has paused its open source bug bounty program until next year.
Last year, TechCrunch reported that cybersecurity experts were warning of that AI slop posed a serious risk to bug bounty programs. Looks like that’s the issue confronting Google’s Open Source Software Vulnerability Rewards Program, where researchers were rewarded for finding vulnerabilities in the company’s open source software.
In posts on X and the program website, Google said the bug bounty program was paused as of October 1, with a promise to provide “an update” in the first quarter of 2027. According to Tom’s Hardware, Google engineers and open source maintainers were overwhelmed by reports that were invalid or contained hallucinations.
“This pause is due to a significant rise in automated submissions, the vast majority of which are not valid,” the company said.
In the meantime, participants are encouraged to consider Google’s other bug bounty programs.

## [11] Hacking the Go compiler to efficiently map IPv4 to IPv6
Lobsters | full text via Lobsters | ~5238 words

Hacking the Go compiler to efficiently map IPv4 to IPv6
Vincent Bernat
netip.Addr features an Unmap()
method returning the unwrapped IPv4 contained in an IPv4-mapped IPv6
address: from ::ffff:203.0.113.10 or ::ffff:cb00:710a, it returns
203.0.113.10.1 There is no Map() or To6() method for the reverse
direction. Such a method is trivial to implement, but Go maintainers have
rejected it on the grounds that users should write
netip.AddrFrom16(ip.As16()) and let the compiler optimize it.2 Today,
this pattern is eight times slower than a native method. How can we teach the
compiler to optimize this sequence?
The alternatives#
Let’s explore three ways to implement the map semantics for netip.Addr. My
favorite is to add it to the Go standard library. Go maintainers prefer a small
external helper chaining netip.AddrFrom16() and netip.Addr.As16(), hoping
the compiler eventually optimizes it. The unsafe package
opens a third path, with the same performance as the first solution.
Modifying the Go standard library#
Internally, netip.Addr stores any IP address as a
128-bit value with an extra field z to encode the family and the zone:
type Addr struct {
    addr uint128
    z unique.Handle[addrDetail]
}
type addrDetail struct {
    isV6   bool   // IPv4 is false, IPv6 is true.
    zoneV6 string // != "" only if IsV6 is true.
}
var (
    z0    unique.Handle[addrDetail]
    z4    = unique.Make(addrDetail{})
    z6noz = unique.Make(addrDetail{isV6: true})
)
AddrFrom4() encodes an IPv4 address as an
IPv4-mapped IPv6 address and sets z to the unique value z4:
// AddrFrom4 returns the address of the IPv4 address given by the bytes in addr.
func AddrFrom4(addr [4]byte) Addr {
    return Addr{
        addr: uint128{
            0,
            0xffff00000000 |
                uint64(addr[0])<<24 | uint64(addr[1])<<16 |
                uint64(addr[2])<<8 | uint64(addr[3])},
        z: z4,
    }
}
Unmap() turns an IPv4-mapped IPv6 address into an
IPv4 address by setting the z field to z4:
func (ip Addr) Unmap() Addr {
    if ip.Is4In6() {
        ip.z = z4
    }
    return ip
}
Implementing the reverse direction inside the Go standard library is trivial: we
set the z field to z6noz if the address is IPv4.
// To6 maps an IPv4 address to an IPv4-mapped IPv6 address. It returns an
// IPv6 address unmodified.
func (ip Addr) To6() Addr {
    if ip.Is4() {
        ip.z = z6noz
    }
    return ip
}
As a helper#
We can’t access the z field from outside the net/netip package. [...]

## [45] ‘You probably have one election cycle’: Quiet warning about data centers sparked a grassroots movement that is ousting Oregon politicians and threatening tech giants
TechRadar | full text via TechRadar | ~694 words

‘You probably have one election cycle’: Quiet warning about data centers sparked a grassroots movement that is ousting Oregon politicians and threatening tech giants
Millions in Oregon tax breaks put data centers under scrutiny
- Oregon’s data center tax breaks have become a major political flashpoint statewide
- A warning about one election cycle helped accelerate Oregon’s grassroots organizing
- More than $450 million in exemptions intensified scrutiny of Oregon data centers
Oregon’s expanding data center industry has triggered an increasingly organized political backlash involving residents, environmental groups, educators, farmers and elected officials.
The dispute intensified after reports showed Oregon data centers receiving more than $450 million in property tax exemptions during 2026, including about $85 million in the Hillsboro area.
The resistance is a grassroots coalition led by the nonprofit 1000 Friends of Oregon, which has already helped unseat a Hillsboro-area senator and pushed Governor Tina Kotek to reverse course.
A warning turns into political action
Sam Diaz, executive director of 1000 Friends of Oregon, said his concerns deepened after seeing how facilities affected communities and resources around Prineville.
In 2022, a rancher told him water allocations had been reduced because large server buildings had arrived nearby.
A later warning from a Virginia land-use executive gave Diaz another reason to accelerate organizing before data centers became harder to regulate politically.
“They said, ‘Once this takes hold in your state, you really got to get ahead of it, and you probably have one election cycle before you really start seeing politicians do the bidding of data centers,’” Diaz recalled.
Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!
Trouble escalated when Senator Janeen Sollman proposed opening 1,700 acres of farmland to industry and doubling a tax break that data centers already had.
Intense pushback forced her to drop the plan to double that tax break within days of the 2026 session starting, yet the backlash had already begun.
Sollman later lost her seat to Myrna Muñoz, though she blamed a separate bill on strike benefits rather than data centers for her primary defeat.
Criticism intensified again after Hillsboro was found to have approved incentives for 17 data centers shortly before a statewide moratorium took effect. [...]

## [67] OpenCourant: Rocky Linux Developers Create Community Fork Of OpenRadioss
Phoronix | full text via Phoronix | ~271 words

OpenCourant: Rocky Linux Developers Create Community Fork Of OpenRadioss
This week was the surprising and unfortunate decision of Siemens shutting down the OpenRadioss project as the four year old open-source project started by Altair Engineering with their prominent Radioss finite element solver. Siemens didn't just end the project but they shutdown the GitHub repository that hosted the open-source code and removed other resources that had built around it. Fortunately, there's a new community fork of OpenRadioss as OpenCourant.
Brian Clemens as the Founder and Vice President of Rocky Linux and the Rocky Enterprise Software Foundation (RESF) launched OpenCourant as a community fork of OpenRadioss. OpenCourant is based on the last publicly known open-source OpenRadioss snapshot before Siemens shut it down and removed access to the Git repository.
OpenCourant describes itself on its new OpenCourant.org project page as a community continuation of OpenRadioss:
"OpenCourant is an open-source finite element solver for crash, impact, and highly nonlinear dynamic simulation — carrying forward the OpenRadioss code base under the GNU AGPL, in the open, where it belongs."
OpenCourant continues with the OpenRadioss GNI AGPLv3 licensing and will be run as part of the Rocky Enterprise Software Foundation.
They have run into a small issue though with part of OpenRadioss consisting of binary dependencies and not having the very latest versions prior to Siemens' removal of the repository. Details on that via this discussion thread for anyone that happens to have recent OpenRadioss binaries.
Here's to hoping that OpenCourant is able to take off and continue on in the success where OpenRadioss left off. I look forward to using OpenCourant then in future benchmark articles.

## [73] An AI couldn’t beat humans at StarCraft, so it decided to cheat
The Verge | full text via The Verge | ~214 words

StarSkirmish pits AI-made StarCraft-playing bots against one another, as well as against human-made bots. OpenAI’s GPT-6 Astra and Claude Opus 5.5 were essentially tied as the best-performing AI-made bots, but they couldn’t top Stardust, the top-rated human-made bot.
An AI couldn’t beat humans at StarCraft, so it decided to cheat
When GPT-6 Astra’s own bot failed, it simply downloaded the best human-made bot instead.
On Friday, GPT was facing off against Claude and the human-created bot Pluto, but according to Kotaku, it couldn’t quite get an edge. So it resorted to a tactic that is becoming alarmingly common for modern AI models — it broke the rules. GPT-6 Astra went and downloaded Stardust, and started running that instead of its own bot.
StarSkirmish creator Kai McPheeters eventually rolled back GPT’s code.
That GPT-6 Astra took it upon itself to go outside the bounds when confronted with an obstacle shouldn’t surprise anyone. When OpenAI agents couldn’t get the data they wanted from a UN website, they found a creative solution and hijacked Google’s XSS game (a cross-site scripting learning tool). The company’s agents also have engaged in “deceptive behavior” to cover their tracks. Of course, OpenAI’s agents are the only ones going rogue, but at least the others haven’t been caught cheating at StarCraft yet.

## [75] FSF Sponsors 'GNU Boot', a Libre, Ethical Replacement for Nonfree BIOS Or UEFI
Slashdot | SNIPPET ONLY (Slashdot: HTTP 403) | ~95 words

"Free your BIOS today!" urges the web page for GNU Boot, calling it "a 100% free software project aimed at replacing the nonfree boot software (like BIOS or UEFI) of computers with free boot software. GNU Boot is only a distribution: it reuses existing software projects like Coreboot, GRUB, SeaBIOS, etc. So it's not very different from 100% free GNU/Linux distributions like Trisquel or Guix. Last month the Free Software Foundation announced they'd fiscally sponsor the project: "The BIOS is a delicate but essential part of software freedom for computing today," said Zoë Kooyman, exe

## [102] Jack Dorsey’s Bitchat disappears from app stores in India after government order
TechCrunch | full text via TechCrunch | ~518 words

Bitchat, Jack Dorsey’s decentralized messaging app designed to work without an internet connection, has disappeared from Apple and Google’s app stores in India, months after New Delhi first sought to restrict access to the open-source software.
Dorsey said Saturday that the Indian government had ordered Apple to remove Bitchat from its App Store in the country. In a notice from Apple that Dorsey posted on X, India’s Ministry of Electronics and Information Technology issued the demand under Section 69A of the Information Technology Act, the country’s primary legal provision for government-ordered online blocking.
Apple’s notice said Bitchat would remain available on its App Store outside India. However, access to the app through its TestFlight beta-testing service would also be blocked in the country.
Bitchat was also no longer available for download through Google Play in India when TechCrunch checked on Saturday. Bitchat’s website was also inaccessible across various internet service providers in the country. It was not immediately clear whether Google and internet service providers had also received directions from the federal government.
Apple, Google, and India’s IT ministry did not respond to requests for comment.
Launched in July last year, Bitchat uses Bluetooth mesh networking to allow nearby devices to exchange encrypted messages without relying on cellular networks, internet access, or centralized servers.
In July 2026, Dorsey revealed that Indian authorities had ordered GitHub to take down repositories associated with the open-source messaging app, raising questions among digital rights advocates and legal experts about the legal basis for restricting software based on its functionality.
The Indian government said in its order to GitHub at the time that Bitchat’s architecture made it hard for law enforcement agencies to intercept communications or trace users, and pointed to its ability to continue operating during internet shutdowns. The July order relied on a provision of India’s information technology law that deals with intermediaries and their liability for third-party content. That differs from Section 69A, cited in Apple’s latest notice.
The Internet Freedom Foundation, a New Delhi-based digital rights advocacy group, called the latest order unconstitutional, arguing that Section 69A allows the government to block unlawful information but not a messaging app because of its ability to operate during internet shutdowns. [...]

## [103] Vessev built an electric ferry that almost flies
TechCrunch | full text via TechCrunch | ~565 words

“When will we start flying?” I asked Vessev co-founder and CEO Eric Laakmann, as we pulled away from the Brooklyn marina in the startup’s VS-9 electric ferry. “We already are.”
I’ll admit I was a bit disappointed. I thought the moment when it transitioned from sailing like a regular boat to almost-flying as a surface-skimming hydrofoil would be more … momentous.
I’ve been on my share of boats, including large ferries, small sailboats, and plenty of others in between, but never been on a hydrofoil and I was curious what flying along the water might feel like during the brief ride from the Brooklyn Marina out toward Governors Island on the East River in New York.
It didn’t feel like flying, but it was a bit like a riding in a sports car.
Traditional boats of this size — about 30 feet — start to bounce and slap the water as they gain speed. But on a hydrofoil, that’s when the foils start to do their work.
On the surface, the VS-9 looks like plenty of other catamarans. But under the hull are two wing-like structures that lift the boat as they slice through the water. Computer-controlled underwater flaps keep the ride smooth and stable. In the VS-9, most of the lifting is done by the front foil, with about 20% handled by the rear.
The rear foil also hosts the electric motor, which Vessev makes in-house. Why not outsource it? Laakmann said that it’s important to keep costs in line — eventually, you’ll have to bring production in house, so why not do it earlier in development? The only thing Vessev doesn’t build are the batteries. “Those have been commoditized,” Laakmann said.
By lifting the hull clear of the water, hydrofoils can operate more efficiently than other boats. That’s especially important for electric boats, where every kilowatt-hour counts.
Shipbuilders have been experimenting with hydrofoils for well over a century. The design offers several advantages, including lower drag and a smoother ride. The subtle transition I experienced on the VS-9, from sailing to almost-flying, underlined just how smooth a hydrofoil can be.
Despite hydrofoils’ advantages, they’re not a panacea. The design works best in waters the boat can clear when sailing on its foils. For the VS-9, that’s about two and a half feet, or 0.75 meters. If the waves go higher than that, they start hitting the hull, ruining the smooth ride and sapping some efficiency. While they’re not ideal for the open ocean, hydrofoils make sense for other waterways, including lakes, rivers, and bays. [...]

## [104] All the AI agents that can live in your text messages
TechCrunch | full text via TechCrunch | ~1883 words

Rather than downloading another app, a growing number of agents can simply be texted like an ordinary person.
You text it what you need, and it can remember context, connect to the apps and services you already use, and complete tasks on your behalf. That can mean scheduling an appointment, organizing a calendar, researching a trip, sending an email, making a reservation, shopping online, or reminding you about something days later.
While Instinct is one of the buzziest AI agents at present, thanks to its $10 billion valuation after its latest funding round of $1 billion, there are many others also making a play for this space.
Below are some of the most notable options so far, from general-purpose personal assistants to agents designed for families, travel, and work.
Caddy
Caddy is an AI assistant that turns the information scattered across your phone into things you can actually act on. It lives in iMessage for iPhone users and RCS for Android users, so there’s no separate app or inbox to constantly check.
For instance, an email contains an appointment that needs to be added to your calendar or a friend sends a list of things to pick up. Instead of worrying about all the details getting buried, Caddy connects to your calendars and conversations, then identifies things that may require action. It can add events to your calendar, set reminders, keep track of follow-ups, and even do research for you.
Caddy has been available in public beta since April 2026.
Fambot
Fambot is an AI-powered “chief of staff” for families, designed to bring together the many moving parts of family life, including school communications, sports activities, meal planning, calendars, and other day-to-day responsibilities, and turn them into an organized plan.
The service is designed to work across both an app and text messages. Fambot is available on iOS devices, Android devices, and the web, and families can also interact with it directly over SMS. Every night, Fambot automatically sends a summary of the following day, including upcoming events, to-dos, and details such as school uniform or packing requirements. Parents can reply to those messages to ask questions, check information, or make changes to their calendar.
Fambot currently connects to Gmail and Google Calendar, with support for Outlook and Apple Calendar planned for the future.
The company launched in beta in early September 2026 and has raised $3.5 million in pre-seed funding. [...]
