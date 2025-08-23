# 8086 Interrupts — Page 216 MCQs and True/False

Note: Wrapping up with applied Qs—end-to-end interrupt flow, example calculations, and edge cases.

## MCQs (English Qs, Bangla explanations)

1) If the IVT entry for type 20h contains IP=1234h, CS=F000h, the ISR physical start address is:
- A. 0xF000:0x1234 (logical); physical 0xF0000 + 0x1234 = 0xF1234
- B. 0x1234:0xF000; physical 0x12340 + 0xF000 = 0x21340
- C. 0x0000:0xF000; physical 0xF000
- D. 0xF000:0x1234; physical 0x01234
Answer: A
Explanation (Bangla): ফিজিক্যাল = CS×16 + IP = 0xF0000 + 0x1234 = 0xF1234।

2) On interrupt entry, the stack pointer (SP) will:
- A. Increase by 6
- B. Decrease by 6
- C. Remain unchanged
- D. Decrease by 4
Answer: B
Explanation (Bangla): FLAGS, CS, IP—প্রতিটি 2 বাইট করে মোট 6 বাইট পুশ হয়—SP কমে।

3) Which combination of events will prevent servicing INTR?
- A. IF=1, NMI asserted
- B. IF=0, INTR asserted
- C. IF=1, INTR asserted at instruction boundary
- D. IF=1, INT n executed
Answer: B
Explanation (Bangla): IF=0 হলে মাস্কেবল INTR ব্লক থাকে—CPU সার্ভিস করবে না।

4) The correct order during interrupt response is:
- A. Fetch vector → Push FLAGS → Push CS, IP → Clear IF/TF → Jump to ISR
- B. Push FLAGS → Push CS, IP → Clear IF/TF → Fetch vector → Jump to ISR
- C. Clear IF/TF → Fetch vector → Push FLAGS → Push CS, IP → Jump to ISR
- D. Push CS, IP → Push FLAGS → Jump to ISR → Clear IF/TF
Answer: B
Explanation (Bangla): প্রথমে FLAGS→CS→IP পুশ, তারপর IF/TF ক্লিয়ার; এরপর IVT থেকে ভেক্টর নিয়ে ISR-এ ট্রান্সফার।

5) Which scenario requires sending an EOI (if Auto EOI is not used)?
- A. After software INT n
- B. After NMI
- C. After servicing an INTR routed via 8259A
- D. After CLI
Answer: C
Explanation (Bangla): 8259A-র মাধ্যমে আসা INTR সার্ভিস শেষ হলে PIC-কে EOI দিতে হয় (OCW2)।

6) Which is TRUE about NMI vectoring?
- A. Vector type supplied by 8259A
- B. Fixed type 2; no INTA handshake
- C. Uses two INTA cycles
- D. Masked by IF
Answer: B
Explanation (Bangla): NMI টাইপ 2—ফিক্সড; INTA লাগে না এবং IF দ্বারা মাস্ক হয় না।

7) A long REP string operation in progress will:
- A. Be preempted immediately by INTR
- B. Complete first; interrupt samples at boundary
- C. Corrupt FLAGS
- D. Clear IF
Answer: B
Explanation (Bangla): ইন্টারাপ্ট সাধারণত ইনস্ট্রাকশন বাউন্ডারিতে স্যাম্পল হয়—REP স্ট্রিং অপারেশন শেষ হলে সার্ভিস হবে।

8) Using STI inside ISR allows:
- A. Lower-priority interrupts to preempt
- B. Higher-priority interrupts to preempt
- C. All interrupts to be blocked
- D. Only NMI to occur
Answer: B
Explanation (Bangla): STI করলে মাস্কেবল ইন্টারাপ্ট আবার এনাবল হয়—প্রায়োরিটি কনফিগ অনুযায়ী উচ্চ-প্রায়োরিটি ISR নেস্ট করতে পারে।

9) The vector entry size is 4 bytes because:
- A. It stores IP (2B) and CS (2B)
- B. It stores physical address (4B)
- C. It stores CS only (4B)
- D. It stores IP only (4B)
Answer: A
Explanation (Bangla): প্রতিটি এন্ট্রি 4 বাইট—IP ও CS দুই বাইট করে।

10) After IRET, the IF and TF flags are:
- A. Always cleared
- B. Restored to the values saved on interrupt entry
- C. Set to 1
- D. Random
Answer: B
Explanation (Bangla): IRET FLAGS পপ করে—সেভ করা মানে ফিরে যায় (IF/TF সহ)।

## True/False (English statements, Bangla explanations)

1) The physical ISR start address is computed as CS×16 + IP.
- Answer: True
- Explanation (Bangla): 8086 রিয়েল-মোডে ফিজিক্যাল = সেগমেন্ট×16 + অফসেট।

2) INTR cannot be serviced when IF=0.
- Answer: True
- Explanation (Bangla): IF=0 হলে মাস্কেবল ইন্টারাপ্ট ব্লক।

3) NMI uses INTA to obtain a vector number.
- Answer: False
- Explanation (Bangla): NMI-র ভেক্টর টাইপ ফিক্সড (2)—INTA লাগে না।

4) REP string operations may delay interrupt service.
- Answer: True
- Explanation (Bangla): দীর্ঘ ইন্সট্রাকশন/লুপ ইন্টারাপ্ট ল্যাটেন্সি বাড়ায়।

5) EOI is relevant for software interrupts as well.
- Answer: False
- Explanation (Bangla): EOI PIC-ভিত্তিক হার্ডওয়্যার INTR-এর জন্য; সফটওয়্যার INT n-এ EOI প্রসঙ্গ নেই।
