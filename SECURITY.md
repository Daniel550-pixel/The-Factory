# Security Policy

## Scope

The Factory is an evolving AI systems platform. Security issues affecting the kernel, runtime, policy boundaries, provenance, memory, integrations, or execution controls should be reported responsibly.

## Reporting

Do not publish sensitive vulnerabilities, credentials, exploit details, or private system information in public issues.

Until a dedicated private security reporting channel is configured, report suspected vulnerabilities privately to the repository owner through an available private GitHub communication channel.

Include:

- affected component and version/commit
- concise description of the issue
- reproduction steps or proof of concept where safe
- security impact
- suggested mitigation, if known

## Security design principles

The project prioritizes:

- explicit authorization boundaries
- deterministic integrity and policy controls
- provenance and auditability
- least privilege
- replayable state transitions
- separation of AI proposals from execution
- secure handling of secrets and credentials

Never commit API keys, passwords, tokens, private keys, certificates containing private material, or production credentials.
