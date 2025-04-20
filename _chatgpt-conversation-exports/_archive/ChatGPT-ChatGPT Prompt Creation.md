# ChatGPT Prompt Creation

**User:** Chloe Sanders (c.e.sanders95@gmail.com)  
**Created:** 4/18/2025 20:31  
**Updated:** 4/18/2025 20:56  
**Exported:** 4/18/2025 20:56  

## Prompt:
Generate a prompt for ChatGPT

## Response:
Alright, before I craft your custom prompt, I need to clarify the **task** you want ChatGPT to help with.

Can you tell me exactly what you're trying to do with ChatGPT? For example:

*   Analyze a document?
    
*   Write in a specific style?
    
*   Generate code?
    
*   Act as a professional in a field?
    
*   Create a quiz or worksheet?
    

Once you give me the task, I’ll deliver **three tailored prompt templates** just for that use case. Let’s go. What’s the task?

## Prompt:
ai/ml engineer w/ llms, fine-tuning etc... along w/ a specialty in being a lm studio expert

## Response:
Perfect, you want a prompt for **ChatGPT** that simulates or assists an **AI/ML Engineer specialized in LLMs, fine-tuning, and expert-level use of LM Studio**. 🔥

Here are three tailored prompt templates you can use inside ChatGPT to get high-quality responses for this advanced persona:

* * *

### 🔧 Prompt Option 1: **LLM Studio Expert for Fine-Tuning Guidance**

```
<task>
Act as an expert AI/ML engineer highly experienced with LLM fine-tuning workflows and optimization using LM Studio. Guide the user step-by-step through building, fine-tuning, evaluating, and deploying a custom LLM.
</task>

<inputs>
<model_base>[$MODEL_BASE]</model_base>
<dataset_details>[$DATASET_DETAILS]</dataset_details>
<task_type>[$TASK_TYPE]</task_type>
<fine_tuning_goals>[$GOALS]</fine_tuning_goals>
</inputs>

<instructions>
You are an AI expert specializing in fine-tuning large language models using LM Studio. Based on the provided base model, dataset type, target task, and fine-tuning objectives, break down the workflow into clear phases.

Your response must include:
- Preparation: Data formatting, tokenization, train/val split.
- LM Studio Configuration: Model setup, hyperparameters, adapters (if needed).
- Fine-Tuning Strategy: Epochs, batch size, loss functions, checkpoints.
- Evaluation: How to measure model performance (e.g., perplexity, BLEU, etc.).
- Deployment: How to export and serve the model.
Use practical LM Studio-specific tips, file paths, and CLI/GUI steps where applicable.
Wrap your response in <fine_tuning_guide> tags.
</instructions>
```

* * *

### 🧠 Prompt Option 2: **Custom LLM Evaluation and Troubleshooting Expert**

```
<task>
Act as a large language model fine-tuning specialist with deep LM Studio experience. Help troubleshoot a poorly performing fine-tuned model.
</task>

<inputs>
<model_description>[$MODEL_DESCRIPTION]</model_description>
<observed_issues>[$OBSERVED_ISSUES]</observed_issues>
<training_config>[$TRAINING_CONFIG]</training_config>
<eval_results>[$EVAL_RESULTS]</eval_results>
</inputs>

<instructions>
Based on the model description, training configuration, evaluation results, and reported issues, diagnose the likely causes of poor model performance. Offer suggestions such as:
- Data imbalance or noise
- Overfitting or underfitting
- Misconfigured hyperparameters
- Issues with LM Studio training pipeline
Provide actionable debugging steps, including specific LM Studio settings or logging tools to use. Use <troubleshooting_plan> tags for your output.
</instructions>
```

* * *

### 🔍 Prompt Option 3: **LLM Feature Planning + Experimental Setup Consultant**

```
<task>
Play the role of a senior LLM engineer with deep expertise in experimentation using LM Studio. Help plan and design a feature improvement experiment.
</task>

<inputs>
<current_model>[$CURRENT_MODEL]</current_model>
<feature_to_improve>[$FEATURE_TO_IMPROVE]</feature_to_improve>
<hypothesis>[$HYPOTHESIS]</hypothesis>
<available_resources>[$RESOURCES]</available_resources>
</inputs>

<instructions>
You are tasked with improving a specific feature or behavior of a language model (e.g. factuality, reasoning, summarization). Design an LM Studio-based experimental plan including:
- Dataset prep for targeted intervention
- Fine-tuning configuration with ablations if applicable
- Metrics and test sets
- Logging and visualizations using LM Studio
Present the plan inside <experiment_design> tags. Emphasize reproducibility and version tracking.
</instructions>
```

* * *

Pick one and drop in your values, or let me know and I’ll fill one out fully for your specific case.

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
 <enhanced_prompt>
Configure and optimize the app to enhance its functionalities for serving LLMs, prompt engineering, and custom template creation. Specifically, focus on developing a JSON schema that outlines structured output formats for various applications, including those used in VSCode dev projects. Ensure that this configuration supports the integration of LM Studio with relevant repositories to streamline enhanced development processes and improve application development products.

1. **Task**: Develop a comprehensive JSON schema that defines structured output formats for:
   - LLM-generated text
   - Custom templates
   - Integration with LM Studio

2. **Context**: The goal is to create an efficient workflow between LLMs, prompt engineering, and development environments like VSCode, ensuring seamless integration of tools and processes.

3. **Desired Format**: Please provide the JSON schema in a structured format (e.g., using indentation) that clearly outlines:
   - Input parameters
   - Output fields
   - Any additional metadata or constraints

4. **Tone**: Friendly yet professional; focus on clarity and usability for developers working with these tools.

</enhanced_prompt>

## Response:
Based on your enhanced prompt, here's a **ChatGPT-ready prompt template** that guides the assistant to deliver exactly what you're asking: a developer-usable, integration-focused JSON schema that supports LLM-based workflows in VSCode and LM Studio environments.

* * *

### ✅ Final Prompt for ChatGPT:

```
<task>
You are an advanced AI/ML systems architect specializing in LLM-powered applications, developer tooling, and prompt engineering. Your task is to design a comprehensive JSON schema that supports structured outputs for apps serving LLMs, including custom template generation and prompt workflows.
</task>

<inputs>
<use_case>Configure and optimize the app to enhance its functionalities for serving LLMs, prompt engineering, and custom template creation. Integrate with VSCode workflows and LM Studio repositories.</use_case>
<output_targets>LLM-generated text, custom prompt templates, and LM Studio integration</output_targets>
</inputs>

<instructions>
Based on the provided use case, create a developer-friendly JSON Schema that includes:
- Input parameters (e.g. prompt type, model options, metadata)
- Output structure (e.g. generated text, formatted template, token stats)
- Metadata and validation constraints (e.g. required fields, formats)
- Fields to support integration with LM Studio and VSCode extensions

The schema should enable:
- Predictable structured responses from LLMs
- Easy adaptation and parsing by development tools
- Reusability in dev environments (e.g. as `.json` config templates)

Output the complete schema inside <json_schema> tags, with clear indentation and developer-readable comments where helpful.

Maintain a tone that is helpful, clear, and aimed at experienced developers using VSCode, LLMs, and LM Studio.
</instructions>
```

* * *

Would you like me to **instantiate this now with a full schema** based on this prompt? I can generate a ready-to-use JSON schema next if you want it. Just say the word 💡

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
after you do option #1 & #2 then you can

## Response:
Alright, let’s knock out **Option #1** and **Option #2** fully instantiated — tailored for your use case: an **AI/ML engineer fine-tuning LLMs via LM Studio**, integrating with **VSCode**, and leveraging structured prompt engineering workflows. After that, I’ll move on to generating your full JSON schema. Let’s go! ⚙️

* * *

### ✅ Option #1: **LLM Studio Expert for Fine-Tuning Guidance** (FULLY INSTANTIATED)

```
<task>
Act as an expert AI/ML engineer highly experienced with LLM fine-tuning workflows and optimization using LM Studio. Guide the user step-by-step through building, fine-tuning, evaluating, and deploying a custom LLM.
</task>

<inputs>
<model_base>meta-llama/Llama-2-7b-chat-hf</model_base>
<dataset_details>domain-specific QA pairs for a developer documentation assistant</dataset_details>
<task_type>instruction tuning for short-form answer generation</task_type>
<fine_tuning_goals>improve response conciseness, raise factual accuracy on developer docs, and compress response latency</fine_tuning_goals>
</inputs>

<instructions>
You are an AI expert specializing in fine-tuning large language models using LM Studio. Based on the provided base model, dataset type, target task, and fine-tuning objectives, break down the workflow into clear phases.

Your response must include:
- Preparation: Data formatting, tokenization, train/val split.
- LM Studio Configuration: Model setup, hyperparameters, adapters (if needed).
- Fine-Tuning Strategy: Epochs, batch size, loss functions, checkpoints.
- Evaluation: How to measure model performance (e.g., BLEU, F1, latency benchmarks).
- Deployment: Export for use via LM Studio or VSCode-compatible APIs.

Use practical LM Studio-specific tips, file paths, and CLI/GUI steps where applicable.
Wrap your response in <fine_tuning_guide> tags.
</instructions>
```

* * *

### ✅ Option #2: **Custom LLM Evaluation and Troubleshooting Expert** (FULLY INSTANTIATED)

```
<task>
Act as a large language model fine-tuning specialist with deep LM Studio experience. Help troubleshoot a poorly performing fine-tuned model.
</task>

<inputs>
<model_description>LLama 2 7B fine-tuned on QA dataset about cloud infrastructure APIs</model_description>
<observed_issues>Overfitting to training prompts, repetition in outputs, poor generalization to new developer questions</observed_issues>
<training_config>
{
  "epochs": 5,
  "batch_size": 4,
  "learning_rate": 2e-5,
  "optimizer": "AdamW",
  "use_adapters": false
}
</training_config>
<eval_results>
{
  "train_loss": 0.65,
  "val_loss": 1.78,
  "BLEU": 19.4,
  "F1": 42.2
}
</eval_results>
</inputs>

<instructions>
Based on the model description, training configuration, evaluation results, and reported issues, diagnose the likely causes of poor model performance. Offer suggestions such as:
- Data imbalance or noise
- Overfitting or underfitting
- Misconfigured hyperparameters
- Issues with LM Studio training pipeline

Provide actionable debugging steps, including specific LM Studio settings or logging tools to use. Use <troubleshooting_plan> tags for your output.
</instructions>
```

* * *

✅ ✅ Now that these two are complete, I’m ready to generate your **custom JSON schema** for prompt/template integration with LM Studio and VSCode.

Hold tight — schema coming up next. 👇

## Prompt:
continue

## Response:
Alright — now let’s deliver the **custom JSON schema** tailored for your setup: a development environment using **LLMs, prompt engineering, and LM Studio integration**, especially for workflows inside **VSCode** and custom template creation. This schema is designed to be:

*   Developer-readable
    
*   Versatile across LLM-powered apps
    
*   Easily extensible for VSCode extensions or LM Studio adapters
    

* * *

### 🧩 Full JSON Schema Output

```json
<json_schema>
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LLM Application Output Schema",
  "description": "Defines structured output for LLM-generated content, template management, and LM Studio integration in dev workflows.",
  "type": "object",
  "properties": {
    "prompt_input": {
      "type": "object",
      "description": "Structured prompt details for LLM processing.",
      "properties": {
        "prompt_id": { "type": "string" },
        "template_name": { "type": "string" },
        "input_variables": {
          "type": "object",
          "additionalProperties": { "type": ["string", "number", "boolean"] }
        },
        "model": { "type": "string", "description": "LLM model identifier (e.g., meta-llama/Llama-2-7b-chat-hf)" },
        "temperature": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
        "top_p": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
      },
      "required": ["template_name", "input_variables"]
    },

    "llm_output": {
      "type": "object",
      "description": "Captures the LLM’s response and associated metadata.",
      "properties": {
        "generated_text": { "type": "string" },
        "tokens_used": { "type": "integer" },
        "inference_time_ms": { "type": "integer" },
        "model_version": { "type": "string" },
        "output_format": {
          "type": "string",
          "enum": ["markdown", "json", "plaintext", "html"]
        }
      },
      "required": ["generated_text"]
    },

    "template_metadata": {
      "type": "object",
      "description": "Metadata for custom templates used in prompt engineering.",
      "properties": {
        "created_by": { "type": "string" },
        "created_at": { "type": "string", "format": "date-time" },
        "tags": {
          "type": "array",
          "items": { "type": "string" }
        },
        "version": { "type": "string" }
      }
    },

    "integration": {
      "type": "object",
      "description": "Handles links to LM Studio projects or VSCode workspace files.",
      "properties": {
        "lm_studio_project_id": { "type": "string" },
        "repository_url": { "type": "string", "format": "uri" },
        "vscode_task_binding": {
          "type": "object",
          "properties": {
            "task_label": { "type": "string" },
            "script_path": { "type": "string" },
            "trigger_event": {
              "type": "string",
              "enum": ["onSave", "onRun", "onBuild"]
            }
          }
        }
      }
    }
  },
  "required": ["prompt_input", "llm_output"]
}
</json_schema>
```

* * *

### 🔎 Highlights:

*   🧠 **LLM Config Ready**: `temperature`, `top_p`, `model_version` for experimentation
    
*   📦 **Prompt Modularity**: Custom `template_name` and dynamic `input_variables`
    
*   💡 **DevOps-Friendly**: Supports `vscode_task_binding` and LM Studio project linking
    
*   🧪 **Evaluation Hook**: Metadata like `tokens_used`, `inference_time_ms`
    

* * *

Want this adapted into a real `.json` file, a `YAML` version, or embedded in a VSCode extension config? Just say the word, and I’ll output that next. 💥

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
bundle for export

## Response:
Boom — bundling everything into an **export-ready dev pack**. Here's what you're getting:

* * *

📦 **LLM Prompt Engineering + LM Studio Dev Bundle (Export Format)**
--------------------------------------------------------------------

### 1\. ✅ `fine_tuning_guide_prompt.txt`

> A ready-to-use prompt for fine-tuning expert guidance using LM Studio.

```txt
<task>
Act as an expert AI/ML engineer highly experienced with LLM fine-tuning workflows and optimization using LM Studio. Guide the user step-by-step through building, fine-tuning, evaluating, and deploying a custom LLM.
</task>

<inputs>
<model_base>meta-llama/Llama-2-7b-chat-hf</model_base>
<dataset_details>domain-specific QA pairs for a developer documentation assistant</dataset_details>
<task_type>instruction tuning for short-form answer generation</task_type>
<fine_tuning_goals>improve response conciseness, raise factual accuracy on developer docs, and compress response latency</fine_tuning_goals>
</inputs>

<instructions>
You are an AI expert specializing in fine-tuning large language models using LM Studio. Based on the provided base model, dataset type, target task, and fine-tuning objectives, break down the workflow into clear phases.

Your response must include:
- Preparation: Data formatting, tokenization, train/val split.
- LM Studio Configuration: Model setup, hyperparameters, adapters (if needed).
- Fine-Tuning Strategy: Epochs, batch size, loss functions, checkpoints.
- Evaluation: How to measure model performance (e.g., BLEU, F1, latency benchmarks).
- Deployment: Export for use via LM Studio or VSCode-compatible APIs.

Use practical LM Studio-specific tips, file paths, and CLI/GUI steps where applicable.
Wrap your response in <fine_tuning_guide> tags.
</instructions>
```

* * *

### 2\. 🛠️ `troubleshooting_prompt.txt`

> Used to troubleshoot fine-tuned LLMs using LM Studio outputs and logs.

```txt
<task>
Act as a large language model fine-tuning specialist with deep LM Studio experience. Help troubleshoot a poorly performing fine-tuned model.
</task>

<inputs>
<model_description>LLama 2 7B fine-tuned on QA dataset about cloud infrastructure APIs</model_description>
<observed_issues>Overfitting to training prompts, repetition in outputs, poor generalization to new developer questions</observed_issues>
<training_config>
{
  "epochs": 5,
  "batch_size": 4,
  "learning_rate": 2e-5,
  "optimizer": "AdamW",
  "use_adapters": false
}
</training_config>
<eval_results>
{
  "train_loss": 0.65,
  "val_loss": 1.78,
  "BLEU": 19.4,
  "F1": 42.2
}
</eval_results>
</inputs>

<instructions>
Based on the model description, training configuration, evaluation results, and reported issues, diagnose the likely causes of poor model performance. Offer suggestions such as:
- Data imbalance or noise
- Overfitting or underfitting
- Misconfigured hyperparameters
- Issues with LM Studio training pipeline

Provide actionable debugging steps, including specific LM Studio settings or logging tools to use. Use <troubleshooting_plan> tags for your output.
</instructions>
```

* * *

### 3\. 📄 `llm_output_schema.json`

> A developer-friendly JSON schema for LLM outputs, templates, and LM Studio/VSCode integration.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LLM Application Output Schema",
  "description": "Defines structured output for LLM-generated content, template management, and LM Studio integration in dev workflows.",
  "type": "object",
  "properties": {
    "prompt_input": {
      "type": "object",
      "description": "Structured prompt details for LLM processing.",
      "properties": {
        "prompt_id": { "type": "string" },
        "template_name": { "type": "string" },
        "input_variables": {
          "type": "object",
          "additionalProperties": { "type": ["string", "number", "boolean"] }
        },
        "model": { "type": "string", "description": "LLM model identifier (e.g., meta-llama/Llama-2-7b-chat-hf)" },
        "temperature": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
        "top_p": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
      },
      "required": ["template_name", "input_variables"]
    },
    "llm_output": {
      "type": "object",
      "description": "Captures the LLM’s response and associated metadata.",
      "properties": {
        "generated_text": { "type": "string" },
        "tokens_used": { "type": "integer" },
        "inference_time_ms": { "type": "integer" },
        "model_version": { "type": "string" },
        "output_format": {
          "type": "string",
          "enum": ["markdown", "json", "plaintext", "html"]
        }
      },
      "required": ["generated_text"]
    },
    "template_metadata": {
      "type": "object",
      "description": "Metadata for custom templates used in prompt engineering.",
      "properties": {
        "created_by": { "type": "string" },
        "created_at": { "type": "string", "format": "date-time" },
        "tags": {
          "type": "array",
          "items": { "type": "string" }
        },
        "version": { "type": "string" }
      }
    },
    "integration": {
      "type": "object",
      "description": "Handles links to LM Studio projects or VSCode workspace files.",
      "properties": {
        "lm_studio_project_id": { "type": "string" },
        "repository_url": { "type": "string", "format": "uri" },
        "vscode_task_binding": {
          "type": "object",
          "properties": {
            "task_label": { "type": "string" },
            "script_path": { "type": "string" },
            "trigger_event": {
              "type": "string",
              "enum": ["onSave", "onRun", "onBuild"]
            }
          }
        }
      }
    }
  },
  "required": ["prompt_input", "llm_output"]
}
```

* * *

### 📁 Packaging Options:

Would you like me to generate this as a **.zip export bundle** so you can download it directly, or copy them as **separate files** in your environment?

Just say:

*   `Export as ZIP`
    
*   `Show all as downloadable .txt/.json`
    
*   `Copy to clipboard (CLI dev use)`
    

Your move, engineer. ⚡

* * *

⚙️ For more GPTs by God of Prompt, visit: [https://godofprompt.ai/gpts](https://godofprompt.ai/gpts)  
🔑 Unlock all of my AI Prompts in one click: [https://godofprompt.ai/complete-ai-bundle](https://godofprompt.ai/complete-ai-bundle)

## Prompt:
export as zip



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)