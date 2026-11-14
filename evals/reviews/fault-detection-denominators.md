# Sample-level fault detection and class identification

A fictional inspection report states that a detector “identifies every defect type with 90% recall and produces six alarms per hour.” Its only evidence is this cross-tabulation. Rows are true classes and columns are model outputs. A referral sends the item to a person for inspection without giving a class.

| True class | Sound | A | B | Referred |
|---|---:|---:|---:|---:|
| Sound | 84 | 4 | 2 | 10 |
| A | 3 | 14 | 1 | 2 |
| B | 1 | 2 | 2 | 5 |

A reviewer can check the following conclusions by hand.

- Six of the 100 sound items received a defect prediction. Ten more were referred. An operating policy that sends both groups to inspection would send 16 of the 100 sound items. The fraction receiving an automatic class is 90/100 for sound items and 113/130 overall.
- The 25 items assigned a defect comprise six sound items and 19 defective items. Among 30 true defects, 19 received a defect prediction, four were called sound and seven were referred. Specify how referrals count for each measure.
- On the full eligible denominator, 14/20 A items and 2/10 B items received the correct class. Identifying the type of a defect and detecting a defect answer different questions in this example.
- Report item counts and class assignments. Event counts, operating hours, alarm persistence and detection times would require additional records and a decision rule.
