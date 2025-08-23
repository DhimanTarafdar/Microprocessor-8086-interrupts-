# 8259A Priority Interrupt Controller — Page 237 MCQs and True/False

Note: Practical integration tips, ISR templates, and fairness/latency tuning.

## MCQs (English Qs, Bangla explanations)

1) A minimal, safe 8086 ISR template with PIC is:
- A. IRET only
- B. PUSH regs; (optional CLI); CLD; work; device ACK; (optional STI); POP regs; IRET
- C. PUSHF; POPF; RET
- D. HLT; RET
Answer: B
Explanation (Bangla): সেভ-রিস্টোর, CLD, প্রয়োজনীয় CLI/STI, ডিভাইস-ACK, শেষে IRET—এটাই নিরাপদ টেমপ্লেট।

2) To allow higher-priority nesting while ensuring critical atomic update, do:
- A. Keep IF=0 throughout ISR
- B. CLI only during short critical section; STI afterward
- C. Use RETF
- D. Mask all lines in IMR
Answer: B
Explanation (Bangla): স্বল্প-সময়ের CLI; পরে STI করলে হাই-প্রায়োরিটি ইন্টারাপ্ট নেস্ট করতে পারে।

3) To reduce starvation in a busy system with fixed priorities, enable:
- A. Auto EOI only
- B. Priority rotation via OCW2
- C. Poll mode only
- D. SFNM via ICW4 only
Answer: B
Explanation (Bangla): রোটেশন সার্ভিস ফেয়ারনেস বাড়ায়—বারবার একই সোর্সকে প্রাধান্য না দিয়ে পালা ঘুরায়।

4) For edge-triggered inputs with risk of lost edges, you should:
- A. Switch to level-triggered if feasible
- B. Ignore device status
- C. Disable NMI
- D. Use INTO
Answer: A
Explanation (Bangla): লেভেল-ট্রিগার্ডে রিকোয়েস্ট থাকে—এজ-লসের ঝুঁকি কমে।

5) A sign that your ISR is too long is:
- A. Reduced interrupt latency and jitter
- B. Missed deadlines and growing queues
- C. Better throughput always
- D. No effect
Answer: B
Explanation (Bangla): দীর্ঘ ISR-এ জিটার/লেটেন্সি বাড়ে—ডেডলাইন মিস ও কিউ জমে।

6) Correct vector mapping in 8086 mode uses:
- A. type = (ICW2 & F8h) | IRQ
- B. type = ICW2 + IRQ always
- C. type = (ICW2 << 3) | IRQ
- D. type = (ICW2 & F0h) | IRQ
Answer: A
Explanation (Bangla): লো 3 বিট IRQ-তে বসে—বেসের লো 3 বিট শূন্য থাকতে হবে।

7) The right place to send EOI (without Auto EOI) is:
- A. On ISR entry
- B. After the necessary device ACK and before IRET
- C. After IRET
- D. Never
Answer: B
Explanation (Bangla): ডিভাইস পরিষ্কার/ACK করার পর EOI—তারপর IRET।

8) Using POPF mid-ISR to set IF=1 means interrupts will be recognized:
- A. Immediately
- B. After the next instruction boundary
- C. Only after IRET
- D. Only after HLT
Answer: B
Explanation (Bangla): STI/POPF-পরবর্তী একটি ইন্সট্রাকশন-ডিলে থাকে।

9) A shared IRQ line requires:
- A. Reading PIC to know the exact device
- B. Polling device status registers to identify the source
- C. Disabling all other IRQs
- D. Only using NMI
Answer: B
Explanation (Bangla): PIC লাইন-লেভেল জানায়; ডিভাইস-স্ট্যাটাস পোল করে উৎস চিহ্নিত করুন।

10) For deterministic response, ISRs should be:
- A. Short and bounded, with heavy work deferred
- B. Long and compute-heavy
- C. Avoid saving registers
- D. Use RETF
Answer: A
Explanation (Bangla): ছোট, বাউন্ডেড ISR; বাকি কাজ মেইনে—এটাই ডিটারমিনিস্টিক।

## True/False (English statements, Bangla explanations)

1) CLD at ISR entry helps make string operations predictable.
- Answer: True
- Explanation (Bangla): DF=0 করে ফরোয়ার্ড অপারেশন নিশ্চিত হয়।

2) Rotation via OCW2 ensures perfect fairness in all cases.
- Answer: False
- Explanation (Bangla): ফেয়ারনেস বাড়ায় বটে, কিন্তু সব সিস্টেমে “পারফেক্ট” নয়—ওয়ার্কলোড/ডিভাইস আচরণে নির্ভরশীল।

3) POPF can re-enable interrupts during ISR, allowing nesting after one instruction delay.
- Answer: True
- Explanation (Bangla): IF=1 হলে পরের ইনস্ট্রাকশন শেষে ইন্টারাপ্ট স্বীকৃত হয়।

4) Long ISRs reduce jitter.
- Answer: False
- Explanation (Bangla): জিটার বাড়ে, রেসপনসিভনেস কমে।

5) Correct vector computation in 8086 mode uses base&F8h | IRQ.
- Answer: True
- Explanation (Bangla): বেস অ্যালাইনমেন্ট জরুরি।
