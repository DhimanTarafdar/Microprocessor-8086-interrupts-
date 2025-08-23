# 8086 Interrupts — Page 211 MCQs and True/False

Note: Emphasis on 8259A PIC basics, priority, vectoring, and service flow—typical mid-chapter content.

## MCQs (English Qs, Bangla explanations)

1) The primary role of 8259A with an 8086 is to:
- A. Generate clock signals
- B. Convert parallel to serial data
- C. Aggregate interrupt requests and supply type number on INTA
- D. Provide DMA channels
Answer: C
Explanation (Bangla): 8259A একাধিক IRQ লাইন ম্যানেজ করে, প্রায়োরিটি ঠিক করে এবং INTA সাইকেলে CPU-কে ইন্টারাপ্ট টাইপ/ভেক্টর সরবরাহ করে।

2) How many interrupt request inputs does a single 8259A provide?
- A. 4
- B. 8
- C. 16
- D. 32
Answer: B
Explanation (Bangla): একটি 8259A-তে 8টি IRQ (IR0–IR7) থাকে। মাস্টার-স্লেভ ক্যাসকেড করলে 64 পর্যন্ত বাড়ানো যায়।

3) In 8086+8259A, the interrupt vector/type number typically equals:
- A. Fixed by CPU
- B. Provided by PIC (ICW2 base + IRQ)
- C. Program counter lower byte
- D. Segment register value
Answer: B
Explanation (Bangla): ICW2-এ ভেক্টর বেস সেট করা হয়; PIC IR লাইনের নম্বর যোগ করে টাইপ নাম্বার দেয় (base + IRQ)।

4) ICW1 in 8259A is used to:
- A. Set vector base
- B. Configure edge/level trigger and initialization
- C. Send EOI
- D. Read ISR
Answer: B
Explanation (Bangla): ICW1-এ initialization শুরু হয় এবং edge/level (LTIM) ইত্যাদি কনফিগার করা হয়।

5) ICW2 primarily configures:
- A. Priority mode
- B. Vector base for interrupt types
- C. Poll mode
- D. Read status
Answer: B
Explanation (Bangla): ICW2 ভেক্টর বেস নির্ধারণ করে—এটাই টাইপ নম্বর গণনার ভিত্তি।

6) ICW3 is needed especially when:
- A. Poll mode is active
- B. Cascading (master/slave) is used
- C. Auto EOI is used
- D. Edge triggering is disabled
Answer: B
Explanation (Bangla): ক্যাসকেডিং-এ মাস্টার কোন IR লাইনে স্লেভ যুক্ত আছে এবং স্লেভ নম্বর—এসব ICW3 দিয়ে নির্ধারিত হয়।

7) ICW4 can enable which of the following?
- A. Special mask mode
- B. Auto EOI and 8086/8088 mode
- C. Rotate priorities
- D. Read IRR/ISR
Answer: B
Explanation (Bangla): ICW4-এ 8086/8088 মোড, Auto EOI, বাফারিং ইত্যাদি অপশন থাকে।

8) Which command word controls interrupt masking per line (IR0–IR7)?
- A. ICW1
- B. ICW2
- C. OCW1
- D. OCW2
Answer: C
Explanation (Bangla): OCW1-এ প্রতিটি IR লাইনের জন্য মাস্ক বিট থাকে—১ মানে মাস্কড (ডিসেবল)।

9) The purpose of OCW2 is to:
- A. Read status
- B. Send EOI and control priority rotation
- C. Set vector base
- D. Select poll mode
Answer: B
Explanation (Bangla): OCW2 দিয়ে Non-specific/Specific EOI পাঠানো, এবং rotate priorities কনফিগার করা যায়।

10) Spurious interrupt on 8259A typically occurs when:
- A. IRR overflows
- B. Interrupt is withdrawn before vectoring completes (e.g., IR7)
- C. ISR is full
- D. IF=0
Answer: B
Explanation (Bangla): কখনও কখনও ইন্টারাপ্ট অ্যাসার্ট/ডি-অ্যাসার্ট টাইমিংয়ের কারণে ভেক্টরিং হলেও আসলে কোনো বৈধ রিকোয়েস্ট থাকে না—এটাই স্পিউরিয়াস ইন্টারাপ্ট।

11) The INTA handshake between 8086 and 8259A usually involves:
- A. One INTA pulse
- B. Two INTA pulses
- C. Three INTA pulses
- D. No INTA
Answer: B
Explanation (Bangla): 8086 ইন্টারাপ্ট গ্রহণ করলে দু’বার INTA জেনারেট করে; PIC তার মধ্যে ভেক্টর/টাইপ নম্বর সরবরাহ করে।

12) In fully nested mode (default), the highest priority IR is:
- A. IR0
- B. IR3
- C. IR7
- D. Programmable
Answer: A
Explanation (Bangla): ডিফল্ট fully nested মোডে IR0 সর্বোচ্চ প্রায়োরিটি, IR7 সর্বনিম্ন। ঘুরিয়ে দেওয়ার জন্য rotate ব্যবহার করা যায়।

## True/False (English statements, Bangla explanations)

1) OCW1 masks/unmasks individual 8259A interrupt lines.
- Answer: True
- Explanation (Bangla): OCW1-এর বিটগুলো সংশ্লিষ্ট IR লাইনের মাস্ক কন্ট্রোল করে।

2) ICW2 sets poll mode in 8259A.
- Answer: False
- Explanation (Bangla): ICW2 ভেক্টর বেস নির্ধারণ করে; পোল মোড OCW3 দিয়ে কনফিগার হয়।

3) Specific EOI targets the exact IRQ level being serviced.
- Answer: True
- Explanation (Bangla): Specific EOI নির্দিষ্ট লেভেলের সার্ভিস সম্পন্ন হয়েছে—এমন নির্দেশ দেয়।

4) Auto EOI removes the need to send EOI from ISR.
- Answer: True
- Explanation (Bangla): Auto EOI-তে PIC স্বয়ংক্রিয়ভাবে EOI ধরে নেয়; তবে এতে nesting আচরণে সীমাবদ্ধতা থাকতে পারে।

5) In a cascaded PIC system, the master receives the CPU’s INTA cycles.
- Answer: True
- Explanation (Bangla): INTA মাস্টার ফ্রন্ট করে; প্রয়োজনে স্লেভের দিকে নিয়ন্ত্রণ যায় এবং ভেক্টর ফিরিয়ে দেয়।

6) Edge/level triggering is fixed and cannot be programmed.
- Answer: False
- Explanation (Bangla): ICW1-এর LTIM বিট দিয়ে edge বা level ট্রিগারিং বাছাই করা যায়।

7) In fully nested mode, a lower-priority interrupt can preempt a higher-priority ISR by default.
- Answer: False
- Explanation (Bangla): ডিফল্ট fully nested-এ উল্টোটা হয়—উচ্চ প্রায়োরিটি নিচুকে প্রিপ্ট করতে পারে, নিচু উচ্চকে পারে না।

8) Spurious interrupts must always be fully serviced with IRET.
- Answer: True
- Explanation (Bangla): ভেক্টরিং শুরু হলে ISR-এ প্রবেশ করলে স্বাভাবিক রিটার্ন সিকোয়েন্স বজায় রাখা নিরাপদ; তবে কারণ অনুসন্ধান ও লগিং ভালো অভ্যাস।
