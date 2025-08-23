# 8259A Priority Interrupt Controller — Page 236 MCQs and True/False

Note: OCW2 (EOI/rotation), OCW3 (poll/readback), and diagnostic checks.

## MCQs (English Qs, Bangla explanations)

1) Non-specific EOI via OCW2 will clear:
- A. All in-service bits
- B. The current highest-priority in-service level
- C. Only a specific programmed level
- D. No bits
Answer: B
Explanation (Bangla): নন-স্পেসিফিক EOI সর্বোচ্চ প্রায়োরিটি ইন-সার্ভিস লেভেল ক্লিয়ার করে।

2) Specific EOI is chosen when:
- A. There’s only one level
- B. The exact in-service level is known and must be cleared
- C. Auto EOI is enabled
- D. Rotation is disabled
Answer: B
Explanation (Bangla): নির্দিষ্ট লেভেল টার্গেট করে সঠিক ক্লিয়ার করতে specific EOI ব্যবহৃত হয়।

3) To read IRR/ISR you must first:
- A. Send OCW2
- B. Configure OCW3 read-register select (RR) and choose IRR or ISR
- C. Send ICW2
- D. Use Auto EOI
Answer: B
Explanation (Bangla): OCW3 দিয়ে RR/IRR/ISR সিলেক্ট করে রিডব্যাক নেওয়া হয়।

4) Poll mode operation implies that the PIC:
- A. Asserts INTR normally
- B. Does not assert INTR; CPU issues poll and PIC returns pending level
- C. Uses NMI
- D. Disables all IRQ lines
Answer: B
Explanation (Bangla): পোল মোডে CPU কুয়েরি করলে PIC সর্বোচ্চ প্রায়োরিটি পেন্ডিং IRQ রিপোর্ট করে।

5) Rotation on non-specific EOI results in:
- A. Just-serviced level moving to lowest priority
- B. Just-serviced level moving to highest priority
- C. No change
- D. All levels masked
Answer: A
Explanation (Bangla): রোটেশন ফেয়ারনেস দেয়—সদ্য সার্ভিসড লেভেল টেইলে।

6) If ISR bit remains set after IRET, likely cause is:
- A. NMI fired
- B. EOI not issued (when Auto EOI disabled)
- C. IMR all zeros
- D. Wrong vector base
Answer: B
Explanation (Bangla): EOI না দিলে ইন-সার্ভিস বিট ক্লিয়ার হয় না।

7) To quickly verify wiring for IR3, you might:
- A. Send specific EOI for IR7
- B. Force an edge/level on IR3 and read IRR/ISR via OCW3
- C. Disable IF
- D. Use INTO
Answer: B
Explanation (Bangla): IRR/ISR রিডব্যাক দেখে পেন্ডিং/ইন-সার্ভিস স্ট্যাটাস নিশ্চিত করা যায়।

8) In a cascaded PIC, master handles INTA and the vector returned may:
- A. Always be from master’s IRR
- B. Include slave’s base + IRQ if the request came from slave
- C. Be fixed to 2
- D. Depend on CLI/STI
Answer: B
Explanation (Bangla): স্লেভ-সোর্স হলে স্লেভ বেস + IRQ টাইপ CPU-কে দেয়—মাস্টার কন্ট্রোল করে।

9) With Auto EOI enabled, ISR must still:
- A. Send specific EOI
- B. Ensure any device-level status is cleared/acknowledged
- C. Disable NMI
- D. Read ICW1
Answer: B
Explanation (Bangla): ডিভাইস-লেভেল অ্যাকনলেজ/ক্লিয়ার এখনো দরকার—PIC কেবল প্রায়োরিটি স্তরে EOI হ্যান্ডল করে।

10) Misaligned ICW2 base in 8086 mode can cause:
- A. Higher performance
- B. Incorrect vector mapping
- C. Auto EOI failure
- D. No effect
Answer: B
Explanation (Bangla): লো 3 বিট IRQ-তে ব্যবহৃত হওয়ায় বেস ভুল হলে টাইপ ম্যাপিংও ভুল।

## True/False (English statements, Bangla explanations)

1) Non-specific EOI always clears IR7.
- Answer: False
- Explanation (Bangla): সর্বোচ্চ প্রায়োরিটি ইন-সার্ভিস লেভেল ক্লিয়ার হয়—যে লেভেলই হোক।

2) OCW3 must be configured before reading IRR or ISR.
- Answer: True
- Explanation (Bangla): RR/IRR/ISR সিলেক্ট না করলে সঠিক রিডব্যাক হয় না।

3) Poll mode disables INTR; CPU must query for pending levels.
- Answer: True
- Explanation (Bangla): পোলিং-ভিত্তিক অপারেশন।

4) Auto EOI removes the need to acknowledge devices.
- Answer: False
- Explanation (Bangla): ডিভাইস-লেভেল ACK এখনো দরকার।

5) Misaligned vector base can misroute interrupts to wrong ISR.
- Answer: True
- Explanation (Bangla): টাইপ ম্যাপিং ভুল হলে ভুল ISR-এ জাম্প হয়।
