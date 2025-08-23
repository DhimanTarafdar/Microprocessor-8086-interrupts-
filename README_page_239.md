# 8259A Priority Interrupt Controller — Page 239 MCQs and True/False

Note: Cascaded scenarios, specific vs non-specific EOI, rotation strategies, and debugging.

## MCQs (English Qs, Bangla explanations)

1) In a master (base=20h) + slave (base=28h) setup, the type for a slave IRQ6 is:
- A. 26h
- B. 2Eh
- C. 36h
- D. 2Ch
Answer: B
Explanation (Bangla): স্লেভ বেস 28h হলে IRQ6 → 2Eh। মাস্টারের IR2-তে ক্যাসকেড—CPU-কে স্লেভ টাইপই দেওয়া হয়।

2) For fairness among noisy devices, enable:
- A. Auto EOI
- B. Rotation on non-specific EOI via OCW2
- C. Poll mode only
- D. Mask all lines except one
Answer: B
Explanation (Bangla): রোটেশন সদ্য সার্ভিসড লেভেলকে টেইলে সরায়—ফেয়ারনেস বাড়ে।

3) Specific EOI should be used when:
- A. Exact in-service level must be cleared in nested/cascaded setups
- B. Only one device exists
- C. Auto EOI enabled
- D. Poll mode enabled
Answer: A
Explanation (Bangla): নির্দিষ্ট লেভেল ক্লিয়ার করার জন্য specific EOI।

4) To determine whether a request is still pending after device ACK, read:
- A. IMR
- B. IRR
- C. ISR
- D. ICW2
Answer: B
Explanation (Bangla): IRR পেন্ডিং দেখায়।

5) With Auto EOI, what remains necessary in ISR?
- A. Sending OCW2 EOI
- B. Clearing device status/handshake
- C. Disabling NMI
- D. Reprogramming ICWs
Answer: B
Explanation (Bangla): PIC-লেভেলে EOI অটো হলেও ডিভাইস-লেভেল ACK দরকার।

6) A simple on-board debug for ISR time is to:
- A. Place INTO
- B. Toggle a GPIO at entry/exit
- C. Use HLT
- D. Use RETF
Answer: B
Explanation (Bangla): পোর্ট টগল করলে লজিক অ্যানালাইজারে টাইমিং দেখা যায়।

7) If the ISR bit remains set in ISR after service, most likely:
- A. EOI missing
- B. Wrong base
- C. Poll enabled
- D. NMI pending
Answer: A
Explanation (Bangla): EOI না দিলে ইন-সার্ভিস বিট ক্লিয়ার হয় না।

8) In a cascaded system, the master handles INTA and the delivered type can be:
- A. Master’s base + IR2 only
- B. Slave’s base + IRQ when request came from slave
- C. Always 2
- D. Random
Answer: B
Explanation (Bangla): স্লেভ-সোর্স হলে স্লেভ টাইপ CPU-কে দেওয়া হয়।

9) Misaligned ICW2 base can cause:
- A. Correct mapping always
- B. Unexpected vector numbers for IRQs
- C. Faster service
- D. No effect
Answer: B
Explanation (Bangla): লো 3 বিট IRQ-তে ব্যবহৃত—ভুল অ্যালাইনমেন্টে টাইপ মিসম্যাপ।

10) The right place to issue EOI is:
- A. At ISR entry
- B. After device ACK and just before IRET
- C. After IRET
- D. Never
Answer: B
Explanation (Bangla): কাজের শেষে EOI—তারপর IRET।

## True/False (English statements, Bangla explanations)

1) Rotation helps mitigate starvation in fixed-priority setups.
- Answer: True
- Explanation (Bangla): সদ্য সার্ভিসড লেভেলকে টেইলে সরায়—ফেয়ারনেস।

2) Specific EOI is unnecessary when only one level exists.
- Answer: True
- Explanation (Bangla): এক লেভেলে নন-স্পেসিফিকই যথেষ্ট।

3) IRR shows in-service; ISR shows pending.
- Answer: False
- Explanation (Bangla): উল্টো—IRR=pending, ISR=in-service।

4) Auto EOI removes the need for device-level ACK.
- Answer: False
- Explanation (Bangla): ডিভাইস-হ্যান্ডশেক/স্ট্যাটাস ক্লিয়ার এখনো দরকার।

5) Misaligned vector base has no effect on vector mapping.
- Answer: False
- Explanation (Bangla): ভুল ম্যাপিং হয়—ভুল ISR-এ জাম্প করতে পারে।
