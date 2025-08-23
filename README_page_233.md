# 8259A Priority Interrupt Controller — Page 233 MCQs and True/False

Note: ICW3 (cascading), ICW4 details, spurious interrupts, and rotation effects.

## MCQs (English Qs, Bangla explanations)

1) ICW3 is especially relevant when:
- A. No interrupts are used
- B. Cascading master/slave PICs
- C. Auto EOI is enabled
- D. Poll mode is enabled
Answer: B
Explanation (Bangla): ক্যাসকেডে মাস্টারে কোন IR লাইনে স্লেভ আছে ও স্লেভ আইডি—এসব ICW3 দিয়ে নির্ধারিত হয়।

2) In a typical master with one slave at IR2, ICW3 on the master will:
- A. Set bit 2 to 1
- B. Clear all bits
- C. Set bit 7 to 1
- D. Mirror the IMR
Answer: A
Explanation (Bangla): মাস্টারে IR2-তে স্লেভ থাকলে ICW3-এ বিট 2 সেট; স্লেভে তার আইডি কনফিগ হয়।

3) Special Fully Nested Mode (SFNM) is configured via:
- A. ICW1
- B. ICW2
- C. ICW3
- D. ICW4
Answer: D
Explanation (Bangla): ICW4-এ SFNM—ক্যাসকেডে সঠিক নেস্টিং/প্রায়োরিটি বজায় রাখতে।

4) A spurious interrupt typically occurs when:
- A. INTA cycles fail to occur
- B. Edge-triggered request is withdrawn before vectoring completes
- C. IMR masks all lines
- D. NMI fires repeatedly
Answer: B
Explanation (Bangla): এজ-ট্রিগার্ড টাইমিং ইস্যুতে ভেক্টর পাওয়া গেলেও প্রকৃত পেন্ডিং নাও থাকতে পারে—এটাই স্পিউরিয়াস।

5) Rotation on non-specific EOI does what to priorities?
- A. Keeps them fixed
- B. Moves the just-serviced level to the lowest priority
- C. Disables the serviced level
- D. Sets it to highest priority next
Answer: B
Explanation (Bangla): সদ্য সার্ভিসড লেভেল টেইলে—ফেয়ারনেস বাড়ে।

6) In cascaded PICs, the INTA cycles are primarily handled by:
- A. The slave only
- B. The master; it then coordinates with the slave
- C. The CPU without PIC
- D. The NMI circuitry
Answer: B
Explanation (Bangla): INTA মাস্টার ফ্রন্ট করে; প্রয়োজনে স্লেভে ডেলিগেট ও ভেক্টর ফেরত দেয়।

7) Poll mode is enabled via:
- A. OCW2
- B. OCW3
- C. ICW2
- D. ICW1
Answer: B
Explanation (Bangla): OCW3—POLL/RR/IRR/ISR সিলেক্ট।

8) Which register indicates pending vs in-service respectively?
- A. IMR vs ISR
- B. IRR vs ISR
- C. ISR vs IRR
- D. IMR vs IRR
Answer: B
Explanation (Bangla): IRR=pending, ISR=in-service—ডিবাগে খুব জরুরি পার্থক্য।

## True/False (English statements, Bangla explanations)

1) ICW3 is unnecessary in single-PIC systems.
- Answer: True
- Explanation (Bangla): ক্যাসকেড না হলে ICW3 সাধারণত লাগে না।

2) SFNM improves nested interrupt handling in cascaded setups.
- Answer: True
- Explanation (Bangla): প্রায়োরিটি/নেস্টিং-এ উন্নতি আনে।

3) Spurious interrupts cannot happen in level-triggered mode.
- Answer: False
- Explanation (Bangla): কমে বটে, সম্পূর্ণ অসম্ভব নয়—ডিভাইস/ওয়্যারিং/টাইমিং নির্ভর।

4) Rotation-on-EOI can help fairness among frequently active sources.
- Answer: True
- Explanation (Bangla): স্টারভেশন কমায়।

5) Master handles INTA and manages slave coordination during vectoring.
- Answer: True
- Explanation (Bangla): মাস্টার INTA ফ্রন্ট করে ও স্লেভ ভেক্টরিং পরিচালনা করে।
