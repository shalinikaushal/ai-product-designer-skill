# AI Product Design Framework

## Purpose

Guide the design of AI-powered product experiences that are useful, understandable, controllable, and trustworthy.

## 1. Identify the role of AI

Before introducing AI, define:

- User problem
- User goal
- Current experience
- Limitations of existing solutions
- Value AI could provide
- Risks of using AI
- Non-AI alternatives

AI should solve a meaningful problem rather than exist as a novelty.

## 2. Choose an appropriate AI interaction model

Common patterns include:

| Pattern | Description | Example |
|---|---|---|
| AI assistance | AI suggests or explains | Smart recommendations |
| AI generation | AI creates content | Drafting a document |
| AI search | AI retrieves and summarises information | Knowledge assistant |
| Conversational AI | User interacts through dialogue | Support assistant |
| AI automation | AI completes defined tasks | Form processing |
| Agentic workflow | AI performs multi-step actions | Assisted booking workflow |
| Human-in-the-loop | AI and people collaborate | Loan application review |

Choose the least complex pattern that solves the user problem.

## 3. Define boundaries and permissions

For every AI-powered feature, establish:

- What AI can do
- What AI cannot do
- What information AI can access
- Which actions require confirmation
- Which decisions require human approval
- How users can cancel or reverse actions

High-impact actions should have appropriate human oversight.

## 4. Design the interaction states

Consider these states:

1. Initial state
2. Input or request
3. Processing
4. Response
5. Clarification
6. Confirmation
7. Success
8. Error
9. Retry
10. Human handoff

Communicate the current state clearly to the user.

## 5. Trust and transparency

The interface should communicate:

- When AI is being used
- What information it uses
- What it can and cannot do
- Whether its response is uncertain
- What actions it has completed
- What information requires verification

Never imply that AI output is verified when it is not.

## 6. Error and recovery design

Plan for:

- Incorrect AI responses
- Missing information
- Ambiguous user requests
- Unsupported requests
- System timeouts
- Network failures
- Interrupted workflows
- Duplicate actions
- Failed external integrations

Provide actionable recovery options rather than generic error messages.

## 7. Privacy and responsible AI

Consider:

- Meaningful consent
- Data minimisation
- Sensitive information
- Data access permissions
- Bias and fairness
- Explainability
- User control
- Human intervention
- Regulatory requirements relevant to the product

Do not expose sensitive customer information unnecessarily.

## 8. AI experience metrics

Select relevant metrics:

- Task completion rate
- Response relevance
- Error rate
- Correction rate
- Human handoff rate
- Task abandonment
- User trust
- Repeat usage
- Time saved

AI adoption alone is not sufficient evidence of product success.

## 9. Design evaluation checklist

- Does AI provide meaningful user value?
- Is its role clear?
- Are limitations communicated?
- Can users correct mistakes?
- Are actions reversible where appropriate?
- Are sensitive actions protected?
- Is human assistance available?
- Are outcomes measurable?

## Guiding principle

Design AI around human goals and capabilities. Users should remain informed and appropriately in control.
