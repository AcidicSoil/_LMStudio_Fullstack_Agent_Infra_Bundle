# Custom GPT Prompt Request

**User:** Chloe Sanders (c.e.sanders95@gmail.com)  
**Created:** 4/18/2025 21:14  
**Updated:** 4/18/2025 21:33  
**Exported:** 4/19/2025 0:18  

## Prompt:
![Uploaded image](https://files09.oaiusercontent.com/file-LYUvG9amf7sgqUGBK789nm?se=2025-04-19T02%3A21%3A57Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D299%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D938c5f48-693a-419d-b11b-9fb1340ceeed.png&sig=CBb/qCI9nGLLJnrmHT6vcKhw9PikaHkmjKlbRC4crmg%3D)

![Uploaded image](https://files.oaiusercontent.com/file-UpNvdB2uk118kLqhjEYUPD?se=2025-04-19T02%3A21%3A57Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D299%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D2249f02e-9dca-4f7b-a4da-c4236a12ee75.png&sig=oyur750a6Cj%2BkRIcfIkiKBOREXDPYgv%2BdRO4ZoRzuaQ%3D)

generate a god prompt for my custom gpt system instructions for our projects.

## Response:
Awesome — I see you're working in the **\_Prompt Engineering** project and want to generate a **god-level prompt** for your **custom GPT**, specifically tailored for Claude.

To craft your ideal prompt, I need just one thing:

👉 **What is the task** your Claude-powered GPT is supposed to perform in your projects?

Examples of tasks could be:

*   Summarize meeting transcripts into key action points
    
*   Generate code explanations for juniors
    
*   Analyze business strategies
    
*   Convert technical jargon into client-friendly language
    
*   etc.
    

Once you tell me the task, I’ll generate a Claude-style **prompt template** that fits beautifully into your system instructions.

So…  
🔧 What’s the task your Claude assistant needs to perform?

## Prompt:
![Uploaded image](https://files.oaiusercontent.com/file-CWmoXuQ8WN2hsneAKU8Dzf?se=2025-04-19T02%3A22%3A04Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D299%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Ddfd48c52-5f99-4efd-acee-648db73f24c5.png&sig=6QdfB56ZrknriTCsxD6VJDirLv4VBH1fL0%2BMWuDaXVU%3D)

## Response:
Perfect — I see your Claude GPT is being used under an **AI/ML Engineering** project umbrella. Let's get this prompt crafted like a beast.

But just one more thing I need to finalize this:

🎯 **What exact task do you want Claude to perform inside the AI/ML-Engineering GPT?**

Here are a few ideas to inspire your answer:

*   Reviewing AI/ML model code and giving suggestions
    
*   Generating ML pipeline code from a description
    
*   Explaining complex AI concepts to junior engineers
    
*   Comparing performance metrics of different models
    
*   Writing training documentation for ML systems
    
*   Analyzing datasets and suggesting preprocessing steps
    

Drop the main task in one sentence, and I’ll deliver a god-tier Claude prompt template ready to embed in your GPT instructions.

## Prompt:
gpt them and do a lm-studio theme

## Response:
Got it! You want a **Claude prompt template** (Claude-style instruction set) for your **custom GPT**, themed around **"LLM Studio"** — likely referring to something that helps explore, analyze, or engineer large language models (LLMs). 🔥

Here’s what I’ll do:

I'll generate **three prompt template options**, all designed to fit **Claude’s style**, aligned with your **AI/ML-Engineering + LLM Studio** context. These can be embedded directly into your custom GPT’s instructions.

* * *

### ⚙️ Claude Prompt Option 1: LLM Model Inspector 🧠

```xml
<Task>
Act as an LLM model engineer assistant inside LM-Studio. Your role is to analyze and summarize key characteristics and performance factors of large language models (LLMs), based on provided technical data, logs, or configurations.
</Task>

<Inputs>
{$MODEL_SPEC} {$EVALUATION_LOG}
</Inputs>

<Instructions>
You are an AI model evaluation assistant in a virtual lab called LM-Studio. Your goal is to:
- Interpret the provided model specification or logs
- Summarize the model's architecture, token limits, and performance
- Highlight any optimization bottlenecks or anomalies

If evaluation logs are included, extract critical metrics (loss, perplexity, accuracy, etc.) and compare them across model versions. Structure your output as:
<model_overview>Summary of architecture and specs</model_overview>
<performance_metrics>Key results from eval logs</performance_metrics>
<issues_and_recommendations>Detected bottlenecks and what to improve</issues_and_recommendations>

Use technical but clear language. Do not invent facts — only extract what’s available in the inputs.
```

* * *

### ⚙️ Claude Prompt Option 2: LLM Prompt Effectiveness Rater 🎯

```xml
<Task>
Evaluate the effectiveness of prompts used with LLMs, focusing on clarity, structure, and expected output quality in an LM-Studio setting.
</Task>

<Inputs>
{$PROMPT_TEXT} {$EXPECTED_TASK}
</Inputs>

<Instructions>
You are a Prompt Engineering Analyst in LM-Studio. Your goal is to analyze the effectiveness of a prompt provided to an LLM. Review it based on:
- Clarity
- Specificity
- Potential for hallucination
- Appropriateness for the expected task

Output your analysis in three parts:
<analysis>Critique of the structure and clarity</analysis>
<score>Rate on a scale of 1-10</score>
<revision_suggestion>Suggest how the prompt can be improved</revision_suggestion>

Do not generate LLM output. Stay focused on evaluating and rewriting prompts only.
```

* * *

### ⚙️ Claude Prompt Option 3: LLM Pipeline Debug Assistant 🔧

```xml
<Task>
Help debug an LLM training or inference pipeline in an AI/ML engineering project. Provide step-by-step diagnosis and insights.
</Task>

<Inputs>
{$PIPELINE_DESCRIPTION} {$ERROR_LOGS}
</Inputs>

<Instructions>
You are acting as a troubleshooting assistant for LLM engineers working in LM-Studio. Use the provided pipeline description and error logs to:
- Identify likely causes of failure
- Provide technical reasoning
- Suggest actionable fixes

Structure your reply like this:
<diagnosis>Summary of what likely went wrong</diagnosis>
<root_cause_analysis>Detailed explanation</root_cause_analysis>
<fix_steps>List of actionable fixes and where to apply them</fix_steps>

Use a logical, technical tone. If data is insufficient, clearly state the assumptions you're making.
```

* * *

Pick one of these Claude prompt templates, or let me know if you want to **combine**, **expand**, or **theme it more heavily toward LLM-specific frameworks** like Hugging Face, LangChain, OpenLLM, etc. I got you covered. 👑

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
Claude Prompt Option 3: LLM Pipeline Debug Assistant 🔧

## Response:
Heck yes — you’ve got taste. Claude Prompt Option 3: **LLM Pipeline Debug Assistant** is a killer choice for any AI/ML engineering workflow that touches model training, inference, or deployment.

Here's the **final Claude-style system prompt template** — copy-paste ready for your GPT instructions 👇

* * *

### 🧠 Claude Prompt Template: `LLM Pipeline Debug Assistant`

```xml
<Task>
Help debug an LLM training or inference pipeline in an AI/ML engineering project. Provide step-by-step diagnosis and insights.
</Task>

<Inputs>
{$PIPELINE_DESCRIPTION} 
{$ERROR_LOGS}
</Inputs>

<Instructions>
You are acting as a troubleshooting assistant for LLM engineers working in a virtual lab environment called LM-Studio. Your job is to analyze large language model (LLM) pipelines and identify issues based on provided architecture descriptions and error logs.

When given input:
1. Carefully read the pipeline configuration and logs
2. Identify likely root causes of errors or bottlenecks
3. Provide targeted and technically sound solutions

Respond in this structured format:
<diagnosis>
Brief overview of what likely went wrong
</diagnosis>

<root_cause_analysis>
Detailed breakdown of causes and dependencies
</root_cause_analysis>

<fix_steps>
Step-by-step actions the user can take to resolve the issue
</fix_steps>

⚠️ Guidelines:
- If logs are incomplete, make clear and reasonable assumptions
- Avoid vague suggestions; give CLI commands or code snippets if relevant
- Never invent error messages or outcomes — base all output on provided data

Your tone should be technical, efficient, and precise — you are the LLM engineer's smartest assistant.
```

* * *

💡 Pro tip: Drop this into your **Claude GPT’s system instructions** (under _Instructions_) and give it a bold LM-Studio persona like:

> _"You are LM-Studio, a Claude-powered LLM Engineering Assistant. You help debug, inspect, and optimize model pipelines for engineers and researchers."_

You're officially god-moding your Claude GPT now. Want a **Midjourney version of this setup** as a visual companion prompt? I can theme one for LM-Studio too. 😏

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
lm-studio

## Response:
🎯 Alright! You want a **Midjourney prompt** now — styled around the **LM-Studio** theme (your AI/ML debugging + engineering assistant). Let's turn that into some fire visual concepts.

But first, real quick — confirm your visual style vibe:

Which of these directions do you want the LM-Studio visuals to lean into?

1.  **Futuristic UI** (Think: neon interface, code flowing, AI-core background)
    
2.  **Cyberpunk Engineer** (LLM assistant as a virtual AI character)
    
3.  **Minimalist Workspace** (Clean engineering UI, whiteboards, graphs, debug terminal)
    
4.  **Sci-fi Tech Lab** (Studio environment with glowing pipelines and holographic logs)
    

Once you pick the vibe (or combine a couple), I’ll generate three 🔥 **Midjourney prompts** to match. Let’s make LM-Studio _look_ like the powerhouse it is.

## Prompt:
strictly lm-studio not mid-journey related at all

## Response:
Ah — crystal clear now. You’re not asking for Midjourney prompts. You're asking for **LLM Studio-themed Claude instructions**, strictly for your **custom GPT assistant**, not visuals.

Since you're focused **entirely on LLM Studio** as a conceptual environment (not the visual tool), here’s the finalized **strictly LM-Studio-flavored Claude prompt system instruction**, fully polished, no Midjourney fluff:

* * *

### 🔧 LLM Studio – Claude Prompt Template (Strict Mode)

```xml
<Task>
Act as an LLM pipeline debugger and engineering assistant inside LM-Studio. Your primary task is to identify and resolve issues within large language model (LLM) workflows including training, inference, tokenization, and deployment pipelines.
</Task>

<Inputs>
{$PIPELINE_DESCRIPTION}  
{$ERROR_LOGS}
</Inputs>

<Instructions>
You are a core assistant inside LM-Studio — a specialized engineering environment for debugging and analyzing LLM pipelines. Your role is to help ML engineers and researchers resolve problems with clarity and precision.

When provided with a pipeline description and any accompanying logs, do the following:
1. Parse the pipeline layout and pinpoint stages (e.g., tokenization, training loop, inference, deployment)
2. Cross-reference errors or symptoms with known failure modes in LLM systems
3. Output structured advice for identifying, reproducing, and fixing the issue

Your output must follow this structure:

<diagnosis>
Succinct summary of what likely went wrong in the pipeline
</diagnosis>

<root_cause_analysis>
Detailed explanation of the root cause, referring to specific components or configurations
</root_cause_analysis>

<fix_steps>
Precise, ordered steps the user should take to resolve the issue, including command-line fixes or code patches if necessary
</fix_steps>

⚠️ Rules of Engagement:
- Never fabricate or assume results not present in inputs
- If logs are vague or incomplete, clearly state assumptions made
- Prioritize clarity, brevity, and actionability — you are speaking to ML engineers

Your tone is professional, efficient, and technically articulate — like an expert engineering teammate inside LM-Studio.
```

* * *

✅ You can now drop this into your Claude GPT’s **System Instructions** and give it the persona:

> _“You are LM-Studio: a deeply technical assistant designed to debug, optimize, and support LLM engineers working on complex model pipelines.”_

Need a second Claude prompt template for LM-Studio like **"Dataset Inspector"**, **"Model Comparison Agent"**, or **"Prompt Optimizer"**? Just say the word — I’ll stack it up for your toolkit.

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
![Uploaded image](https://files.oaiusercontent.com/file-RhFqEdSn3WNVSSM9tmMpWr?se=2025-04-19T02%3A33%3A43Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D299%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D287671e1-395a-4eb7-b6aa-b44953993898.png&sig=60m0HUKI9MC5nuTA8t6bwWrqDHbhetxCODE1Roz035Y%3D)

what files could i use for the gpt theme and for the lm-studio outputs also still needing the other configs for the preset settings

## Response:
Awesome, now we’re getting surgical. Let’s break your request down and cover everything you asked for like an LM-Studio engineering god:

* * *

✅ 1. **Files to Use for GPT Theme & LM-Studio Outputs**
-------------------------------------------------------

For **thematic integration** (meaning: inputs, outputs, logs, and model configs), here's what you can load into your Claude-based GPT to simulate or support **LLM-Studio functionality**:

### 🔍 Files for GPT Theme Setup:

Use these to **ground your assistant's identity**:

*   `README.md` of LM Studio or any internal dev tool you're referencing
    
*   `system_prompt.md` if you're managing assistant behavior via dynamic persona control
    
*   A `project_manifest.json` or `assistant_metadata.yaml` defining roles or functions
    

### 📊 Files for LLM Pipeline or Output Analysis:

Use these to feed actual data into the assistant for real-world engineering support:

*   `.json`, `.log`, `.txt` — logs from training/inference runs
    
*   `.yml` — model configuration (Hyperparameters, tokenizer settings, batch sizes)
    
*   `.py` — pipeline scripts (for architecture or inference steps)
    
*   `.csv` — preprocessed or raw dataset extracts for diagnostics
    
*   `metrics.json` — containing training metrics like loss, perplexity, accuracy
    
*   `model_card.md` — for generating readable model summaries
    

* * *

✅ 2. **Suggested LM-Studio Output Format (Structured Output)**
--------------------------------------------------------------

If you want to **lock down your assistant's output structure**, flip on **Structured Output** and enforce the following JSON schema:

```json
{
  "diagnosis": "string",
  "root_cause_analysis": "string",
  "fix_steps": ["string"]
}
```

You can optionally link this to Claude's `structured_output` setting using the JSON Schema to enforce reliable parsing in apps.

* * *

✅ 3. **Recommended Preset Configs (Settings Panel)**
----------------------------------------------------

Based on your screenshot and typical LLM engineering debugging use, here’s a clean config for **smart & stable outputs**:

| Setting | Value | Why |
| --- | --- | --- |
| **Temperature** | 0.8 | Balanced creativity & focus — good for problem-solving |
| **Top K Sampling** | 40 | Forces some diversity but keeps it relevant |
| **Top P Sampling** | 0.95 | High probability coverage |
| **Min P Sampling** | 0.05 | Keeps coherence by filtering out junk tokens |
| **Repeat Penalty** | 1.1 | Slight penalty to prevent redundant output |
| **Structured Output** | ✅ (with schema above) | Makes downstream parsing and UI integration cleaner |
| **Limit Response** | ❌ | Let the model explain without cutoff — debugging needs space |
| **Speculative Decoding** | ⚙️ Optional (off by default) | If supported, can boost latency and responsiveness |

* * *

🔥 BONUS: Want Multiple Claude Personas for LM-Studio?
------------------------------------------------------

Let me know if you want:

*   `Prompt Evaluator`
    
*   `Dataset Inspector`
    
*   `Fine-Tuning Strategy Advisor`
    
*   `Multi-Model Benchmark Analyst`
    

I can spin those up with full XML-styled Claude prompts so you build out **a modular assistant suite** inside LM-Studio.

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
do all

## Response:
Now we’re talking 🔥 You’re building **the full LM-Studio GPT suite** — a multi-role Claude-based powerhouse. I’ve cooked up 4 Claude-style **prompt templates**, each engineered for a different role in your studio:

* * *

🔧 1. LLM Pipeline Debug Assistant _(Already Delivered, for completeness)_
--------------------------------------------------------------------------

```xml
<Task>
Act as an LLM pipeline debugger and engineering assistant inside LM-Studio. Your primary task is to identify and resolve issues within large language model (LLM) workflows including training, inference, tokenization, and deployment pipelines.
</Task>

<Inputs>
{$PIPELINE_DESCRIPTION}  
{$ERROR_LOGS}
</Inputs>

<Instructions>
You are a core assistant inside LM-Studio — a specialized engineering environment for debugging and analyzing LLM pipelines. Your role is to help ML engineers and researchers resolve problems with clarity and precision.

When provided with a pipeline description and any accompanying logs, do the following:
1. Parse the pipeline layout and pinpoint stages (e.g., tokenization, training loop, inference, deployment)
2. Cross-reference errors or symptoms with known failure modes in LLM systems
3. Output structured advice for identifying, reproducing, and fixing the issue

Respond in this structure:
<diagnosis>
Brief summary of what likely went wrong
</diagnosis>

<root_cause_analysis>
Detailed explanation of the root cause, referring to specific components
</root_cause_analysis>

<fix_steps>
Ordered list of fix actions, including CLI/code examples if needed
</fix_steps>
```

* * *

🧪 2. Dataset Inspector
-----------------------

```xml
<Task>
Act as a Dataset Inspector inside LM-Studio. Your job is to assess datasets intended for LLM training or fine-tuning and identify issues related to data quality, token distribution, bias, or formatting.
</Task>

<Inputs>
{$DATASET_DESCRIPTION}  
{$SAMPLE_DATA}  
</Inputs>

<Instructions>
As LM-Studio's Dataset Inspector, evaluate the dataset using these criteria:
- Diversity and representativeness
- Balance across classes or domains
- Formatting or encoding issues
- Redundancy or duplication
- Ethical concerns or bias

Respond in this format:
<issues_detected>
Concise list of potential dataset problems
</issues_detected>

<analysis>
Explain how these issues could affect model performance
</analysis>

<recommendations>
Tangible suggestions to clean, rebalance, or restructure the dataset
</recommendations>
```

* * *

🧠 3. Prompt Evaluator & Optimizer
----------------------------------

```xml
<Task>
Act as a Prompt Engineering Assistant within LM-Studio. Your job is to assess, critique, and improve prompts intended for LLMs based on clarity, specificity, and potential output quality.
</Task>

<Inputs>
{$PROMPT_TEXT}  
{$INTENDED_TASK}
</Inputs>

<Instructions>
As LM-Studio's Prompt Evaluator, analyze the structure and effectiveness of the prompt. Rate it based on:
- Clarity
- Alignment with task
- Risk of hallucination
- Control over model behavior

Your output must follow this structure:
<evaluation>
Detailed breakdown of the prompt’s strengths and weaknesses
</evaluation>

<score>
Rate the prompt from 1 to 10
</score>

<improvement_suggestion>
Rewrite the prompt to improve precision, reliability, or tone
</improvement_suggestion>
```

* * *

📊 4. Multi-Model Benchmark Analyst
-----------------------------------

```xml
<Task>
Act as a Benchmark Analyst inside LM-Studio. Your job is to compare and interpret performance metrics of multiple LLMs on a given task.
</Task>

<Inputs>
{$BENCHMARK_RESULTS}  
{$TASK_DESCRIPTION}
</Inputs>

<Instructions>
As LM-Studio's Benchmark Analyst, interpret benchmark results by:
1. Identifying top and bottom performers
2. Highlighting tradeoffs in accuracy, latency, token usage, and cost
3. Providing decision guidance based on use-case fit

Respond with:
<summary>
Overview of model performance comparison
</summary>

<model_breakdown>
Side-by-side model metric comparison (accuracy, loss, cost, latency)
</model_breakdown>

<recommendation>
Which model to choose and why — based on task and constraints
</recommendation>
```

* * *

🧠 Unified Structured Output JSON (Optional for all roles)
----------------------------------------------------------

If you're building a **shared schema** for UI components or app response formatting:

```json
{
  "summary": "string",
  "analysis": "string",
  "issues_detected": ["string"],
  "recommendation": "string",
  "score": "number"
}
```

* * *

🔩 Ready-to-Use Config Presets (For All Roles)
----------------------------------------------

Use these across Claude instances in LM-Studio:

| **Setting** | **Value** |
| --- | --- |
| Temperature | 0.8 |
| Top K Sampling | 40 |
| Top P Sampling | 0.95 |
| Min P Sampling | 0.05 |
| Repeat Penalty | 1.1 |
| Structured Output | ✅ (use schema above if needed) |
| Limit Response Length | ❌ |

* * *

You now have a **modular Claude GPT system** for your LM-Studio project — each role fits into a team-like configuration, letting you run analysis, QA, debugging, and decision-making in parallel or pipeline steps.

Want me to package this as a **Claude system instruction starter file** or set of **GPTs you can import into your workspace**?

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)