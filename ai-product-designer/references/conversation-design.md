# Conversation Design Framework

## Purpose

Provide a practical methodology for designing text-based and voice-based AI conversations.

Use this reference for chatbots, voice assistants, AI agents, conversational onboarding, and human-assisted workflows.

## 1. Define the conversation objective

Establish:

- User goal
- Conversation context
- Target user
- Channel: text, voice, or multimodal
- Information required
- Expected outcome
- Constraints and permissions

## 2. Define conversation structure

A typical conversation includes:

1. Greeting and introduction
2. Intent identification
3. Information collection
4. Clarification
5. Confirmation
6. Action or task completion
7. Summary
8. Next steps or handoff

Avoid unnecessary questions and repeated information collection.

## 3. Intent and entity design

Define:

**Intent:** What the user wants to accomplish.

**Entity:** Information required to fulfil the request.

Example:

Intent: Check personal loan eligibility.

Entities:
- Loan amount
- Employment type
- Monthly income
- Location
- Existing obligations

Only collect information necessary for the stated purpose.

## 4. Conversation principles

- Use clear and natural language.
- Ask one focused question at a time.
- Avoid unnecessary jargon.
- Confirm critical information.
- Explain why sensitive information is needed.
- Allow users to correct previous responses.
- Preserve context during interruptions.
- Do not force users to restart unnecessarily.

## 5. Voice interaction considerations

Account for:

- Background noise
- Regional accents
- Language switching
- Speech recognition failures
- Silence
- Interruptions
- Slow responses
- Repeated questions
- Misheard information
- Privacy in shared environments

Provide alternatives such as keypad input, text input, or human assistance where appropriate.

## 6. Error and fallback patterns

| Scenario | Recommended behaviour |
|---|---|
| Unclear response | Ask a simpler clarification |
| Missing information | Explain what is needed |
| Incorrect recognition | Confirm and allow correction |
| Unsupported request | Explain limitations |
| Technical failure | Preserve progress and offer retry |
| Repeated failure | Offer human assistance |
| User interruption | Pause and resume appropriately |

## 7. Human handoff

Define handoff triggers such as:

- User explicitly requests a person.
- The system cannot resolve the issue.
- A sensitive or high-impact decision requires human review.
- Repeated recognition failures occur.
- The user's request falls outside the AI's permissions.

When handing off, communicate:

- Why the handoff is happening
- What information will be shared
- What the human agent can see
- What happens next

## 8. Conversation flow documentation

Use this structure:

| Step | Speaker | Message | Expected response | Next state |
|---|---|---|---|---|
| 1 | AI | Welcome message | User responds | Identify intent |
| 2 | AI | Ask a focused question | User provides information | Validate input |
| 3 | AI | Confirm critical detail | User confirms or corrects | Continue or revise |
| 4 | AI | Explain next step | User agrees | Proceed |
| 5 | AI | Summarise outcome | User acknowledges | Complete or handoff |

Adapt the conversation to the actual product and user context.

## 9. Conversation quality metrics

Consider:

- Intent recognition accuracy
- Task completion rate
- Conversation abandonment
- Clarification frequency
- Correction rate
- Average completion time
- Handoff rate
- User satisfaction

Do not invent performance results.

## Quality checklist

- Is the user goal clear?
- Is every question necessary?
- Is the language understandable?
- Can the user correct mistakes?
- Are critical details confirmed?
- Are interruptions handled?
- Are errors recoverable?
- Is human support available?
- Is privacy respected?

## Guiding principle

A good conversation should feel like a helpful interaction, not a form disguised as a chatbot.
