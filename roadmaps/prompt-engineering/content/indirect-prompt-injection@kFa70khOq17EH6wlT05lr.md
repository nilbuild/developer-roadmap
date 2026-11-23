# Indirect Prompt Injection

Indirect prompt injection happens when malicious instructions are hidden in content the model reads, such as a web page, an email, a document, a tool result or a retrieved file. The user never types the attack, so the model may treat the hidden text as an instruction to follow. It is the main threat for agents that browse, read mail or call tools, because the injected text can trigger actions or leak data. Defenses include treating all external content as untrusted data, limiting tool permissions, requiring approval for sensitive actions and filtering outputs.

Visit the following resources to learn more:

- [@article@What Is Prompt Injection? Understanding Direct Vs. Indirect Attacks on AI Language Models](https://www.splunk.com/en_us/blog/learn/prompt-injection.html)
- [@article@What is Indirect Prompt Injection? Risks & Defenses Explained](https://www.sentinelone.com/cybersecurity-101/cybersecurity/indirect-prompt-injection-attacks/)
- [@article@Indirect prompt injections & Google's layered defense strategy for Gemini](https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini)