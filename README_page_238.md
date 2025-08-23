# 8259A Priority Interrupt Controller — Page 238 MCQs and True/False

Note: Practical programming—ICW/OCW sequences, vector mapping, and poll/readback usage.

## MCQs (English Qs, Bangla explanations)

1) A correct 8259A initialization sequence is:
- A. ICW2 → ICW1 → ICW3 → ICW4
- B. ICW1 → ICW2 → (ICW3 if cascaded) → (ICW4 if needed)
- C. OCW1 → OCW2 → OCW3
- D. ICW4 → ICW3 → ICW2 → ICW1
Answer: B
Explanation (Bangla): ইনিট শুরু হয় ICW1 দিয়ে; এরপর ICW2 (ভেক্টর বেস), ক্যাসকেডে ICW3, এবং ICW4 (8086/Auto EOI ইত্যাদি)।

2) After initialization, per-line masking is performed with:
- A. ICW2
- B. ICW3
- C. OCW1 (IMR)
- D. OCW2
Answer: C
Explanation (Bangla): OCW1 ইন্টারাপ্ট মাস্ক রেজিস্টার—প্রতি IR লাইনের মাস্ক কন্ট্রোল।

3) In 8086/88 mode, the effective interrupt type is computed as:
- A. type = ICW2 + IRQ
- B. type = (ICW2 & F8h) | IRQ
- C. type = (ICW2 << 3) | IRQ
- D. type = (ICW2 & F0h)
Answer: B
Explanation (Bangla): বেসের লো 3 বিটে IRQ বসে; তাই বেস 8-এর গুণিতক হওয়া উচিত।

4) Which OCW is used to send EOI and manage priority rotation?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4
Answer: B
Explanation (Bangla): OCW2—specific/non-specific EOI এবং rotate।

5) To read IRR vs ISR, first you must program:
- A. OCW2
- B. OCW3 (RR + IRR/ISR select)
- C. ICW3
- D. ICW1
Answer: B
Explanation (Bangla): OCW3 দিয়ে read-register select কনফিগার করে IRR/ISR রিডব্যাক নেওয়া হয়।

6) Poll mode is enabled via which command word?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW2
Answer: C
Explanation (Bangla): OCW3—POLL মোড সিলেক্ট করা হয়।

7) If ICW2 is set to 20h, the type for IRQ5 (single PIC) becomes:
- A. 20h
- B. 24h
- C. 25h
- D. 2Fh
Answer: D
Explanation (Bangla): টাইপ = (20h & F8h) | 5 = 25h নয়, 20h বেসে 0..7 ম্যাপ করলে IRQ5 → 25h; তবে সাধারণভাবে 20h বেসে IRQ5=25h (যদি অপশন C চাই)। Correction: সঠিক উত্তর C. টাইপ = 25h।

8) Non-specific EOI clears:
- A. A chosen level specified in OCW2
- B. The highest-priority in-service request
- C. All in-service requests
- D. Only IR7
Answer: B
Explanation (Bangla): নন-স্পেসিফিক EOI সর্বোচ্চ প্রায়োরিটি ইন-সার্ভিস লেভেল ক্লিয়ার করে।

9) With Auto EOI enabled (ICW4), ISR must still:
- A. Send EOI via OCW2
- B. Acknowledge/clear device-level status
- C. Read ICW3
- D. Mask all lines
Answer: B
Explanation (Bangla): ডিভাইস-লেভেল ACK/ক্লিয়ার এখনো দরকার—PIC কেবল প্রায়োরিটি স্তরে EOI হ্যান্ডল করে।

10) Misaligned base in ICW2 (not multiple of 8) will:
- A. Work fine
- B. Mis-map vectors to unexpected types
- C. Disable rotation
- D. Force NMI
Answer: B
Explanation (Bangla): 8086 মোডে লো 3 বিট IRQ-তে ব্যবহৃত—ভুল অ্যালাইনমেন্টে টাইপ ম্যাপিং গুলিয়ে যায়।

## True/False (English statements, Bangla explanations)

1) ICW1 must always be written before ICW2.
- Answer: True
- Explanation (Bangla): ইনিট সিকোয়েন্স ICW1 দিয়েই শুরু।

2) OCW1 writes the vector base.
- Answer: False
- Explanation (Bangla): ভেক্টর বেস ICW2; OCW1 শুধু মাস্ক।

3) In 8086 mode, type = (base & F8h) | IRQ.
- Answer: True
- Explanation (Bangla): বেসের লো 3 বিট IRQ বসে।

4) OCW2 is used for EOI/rotation.
- Answer: True
- Explanation (Bangla): EOI ও rotate কন্ট্রোল।

5) OCW3 is unrelated to poll/readback.
- Answer: False
- Explanation (Bangla): OCW3—POLL ও IRR/ISR readback।
