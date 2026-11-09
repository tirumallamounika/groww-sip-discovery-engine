# Groww SIP Continuity Copilot — Usability Test Report

**Test date:** 9 November 2026  
**Method:** Independent prototype use followed by in-product feedback submission  
**Evidence:** User-provided Google Sheets feedback export (5 rows, 4 unique tester IDs)

## Objective
Assess whether the SIP Continuity Copilot's guidance is perceived as helpful and easy to use for common SIP continuity concerns. The records capture self-reported feedback, not observed task completion.

## Participant-level records

| Tester (anonymized) | Scenario | Helpful? | Ease of use | Improvement comment |
|---|---|---|---|---|
| T1 | SIP payment failed | Yes | Okay | Blank |
| T2 | SIP payment failed | Yes | Okay | Blank |
| T3 | Market decline makes me worried | Partly | Okay | Blank |
| T4 | SIP payment failed | Yes | Easy | Blank |

**Deduplication:** The export includes two identical entries for tester ID `d53a782ca054`, recorded one second apart. These are treated as one tester. All four distinct IDs are retained in the summary; at least three independent testers are evidenced by distinct IDs.

## Findings

1. **Perceived helpfulness:** 3/4 unique testers answered **Yes** and 1/4 answered **Partly**.
2. **Ease of use:** 1/4 rated the experience **Easy**; 3/4 rated it **Okay**.
3. **Scenario coverage:** Three unique testers selected **SIP payment failed**; one selected **Market decline makes me worried**. There is no feedback entry for the competing-expenses scenario.
4. **Opportunity:** The market-decline scenario's **Partly** helpful response suggests reviewing clarity and specificity for uncertainty-related guidance. The record does not establish why that tester selected Partly.
5. **Open-ended feedback:** The `confusing_or_improve` field is blank in all supplied rows; no verbatim improvement comments can be attributed to these testers.

## Recommendations

- Improve scenario-specific follow-up questions and clearer next steps, especially for market uncertainty, without recommending investments or predicting returns.
- Test the competing-expenses scenario in a future round.
- Add an optional prompt asking what was missing when a tester selects **Partly**.
- Capture task success, completion time, and comprehension in a future moderated or structured task-based test.

## Limitations

- Small convenience sample (four unique tester IDs); findings are directional, not representative.
- Unique IDs are treated as distinct testers, but identity independence is not independently verified.
- Feedback records do not establish that users completed a prescribed task or demonstrate actual SIP recovery.
- No evidence of month-12 retention lift is available from this test.

## Submission-ready summary

> Four unique testers submitted in-product feedback for the deployed SIP Continuity Copilot (five rows, including one duplicate submission). Three of four rated the guidance helpful; one rated it partly helpful. One rated ease of use Easy and three rated it Okay. The market-decline scenario received the Partly rating, suggesting a need for more contextual explanation. Results are directional self-reported usability feedback, not evidence of improved SIP payment or retention outcomes.
