# 8259A Priority Interrupt Controller — Page 232 MCQs and True/False

Note: Core fundamentals—roles, lines, vectoring, ICWs/OCWs, and status registers.

## MCQs (English Qs, Bangla explanations)

1) The primary purpose of the 8259A with 8086 is to:
- A. Generate system clock
- B. Provide DMA channels
- C. Manage multiple IRQs and supply the vector/type on INTA
- D. Convert serial to parallel
Answer: C
Explanation (Bangla): 8259A একাধিক ইন্টারাপ্ট লাইন (IR0–IR7) ম্যানেজ করে, প্রায়োরিটি নির্ধারণ করে এবং INTA সাইকেলে টাইপ নম্বর দেয়।

2) A single 8259A provides how many interrupt request inputs?
- A. 4
- B. 8
- C. 16
- D. 32
Answer: B
Explanation (Bangla): 8টি IR ইনপুট থাকে (IR0–IR7); মাস্টার-স্লেভ ক্যাসকেডে 64 পর্যন্ত বাড়ে।

3) The INTA handshake between 8086 and 8259A typically involves:
- A. One pulse
- B. Two pulses
- C. Three pulses
- D. None
Answer: B
Explanation (Bangla): 8086 ইন্টারাপ্ট গ্রহণ করলে দু’বার INTA জেনারেট করে; PIC সেই সময় টাইপ/ভেক্টর প্রদান করে।

4) In fully nested mode (default), highest priority is:
- A. IR0
- B. IR3
- C. IR5
- D. IR7
Answer: A
Explanation (Bangla): ডিফল্টে IR0 সর্বোচ্চ প্রায়োরিটি, IR7 সর্বনিম্ন।

5) Which register shows pending requests?
- A. IMR
- B. IRR
- C. ISR
- D. TMR
Answer: B
Explanation (Bangla): IRR (Interrupt Request Register) পেন্ডিং IRQ ধারণ করে; ISR ইন-সার্ভিস লেভেল দেখায়; IMR হলো মাস্ক।

6) Which register holds in-service interrupts?
- A. IMR
- B. IRR
- C. ISR
- D. IPR
Answer: C
Explanation (Bangla): ISR (In-Service Register) বর্তমানে সার্ভিসিং-এ থাকা লেভেলগুলো দেখায়।

7) IMR bit=1 means the corresponding line is:
- A. Enabled
- B. Masked (disabled)
- C. In service
- D. Pending
Answer: B
Explanation (Bangla): IMR=1 মানে লাইন মাস্কড; 0 হলে এনাবল।

8) ICW2 primarily configures:
- A. Edge/level triggering
- B. Vector base address for interrupt types
- C. Poll mode
- D. Auto EOI
Answer: B
Explanation (Bangla): ICW2 ভেক্টর বেস নির্ধারণ করে; টাইপ নম্বর = base + IRQ।

9) Edge/level triggering is configured via:
- A. ICW1
- B. ICW2
- C. ICW3
- D. OCW1
Answer: A
Explanation (Bangla): ICW1-এর LTIM বিট দিয়ে edge বা level ট্রিগারিং বাছাই হয়।

10) Auto EOI and 8086/88 mode are configured by:
- A. ICW1
- B. ICW2
- C. ICW3
- D. ICW4
Answer: D
Explanation (Bangla): ICW4-এ 8086/88 মোড, Auto EOI ইত্যাদি অপশন সেট করা হয়।

11) Poll mode and IRR/ISR readback selection are done via:
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4
Answer: C
Explanation (Bangla): OCW3 দিয়ে Poll মোড, RR/IRR/ISR সিলেক্ট কনফিগার হয়।

12) Per-line masking (IR0–IR7) is controlled by:
- A. ICW2
- B. ICW3
- C. OCW1
- D. OCW2
Answer: C
Explanation (Bangla): OCW1 হলো Interrupt Mask Register—প্রতি লাইনের মাস্ক বিট।

## True/False (English statements, Bangla explanations)

1) Fully nested mode is the default priority scheme in 8259A.
- Answer: True
- Explanation (Bangla): ডিফল্টে IR0>IR1>…>IR7।

2) IRR shows in-service levels while ISR shows pending.
- Answer: False
- Explanation (Bangla): উল্টো—IRR=pending, ISR=in-service।

3) IMR bit set to 1 masks the corresponding IRQ line.
- Answer: True
- Explanation (Bangla): 1 মানে ডিসেবল; 0 মানে এনাবল।

4) ICW2 sets the vector base used to compute type numbers.
- Answer: True
- Explanation (Bangla): টাইপ = base + IRQ।

5) ICW4 contains Auto EOI and 8086 mode options.
- Answer: True
- Explanation (Bangla): ICW4-এ এই অপশনগুলো থাকে।

6) OCW2 is used for EOI and priority rotation.
- Answer: True
- Explanation (Bangla): OCW2-তেই EOI/rotate কন্ট্রোল থাকে।

7) OCW3 controls poll mode and IRR/ISR readback.
- Answer: True
- Explanation (Bangla): OCW3 POLL/RR/IRR/ISR সিলেক্ট দেয়।

8) With Auto EOI, software must still send EOI from ISR.
- Answer: False
- Explanation (Bangla): Auto EOI থাকলে PIC স্বয়ংক্রিয়ভাবে EOI ধরে নেয়—তবে nesting আচরণে সীমাবদ্ধতা মাথায় রাখতে হয়।
