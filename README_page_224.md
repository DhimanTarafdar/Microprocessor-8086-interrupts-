# 8086 Interrupts — Page 224 MCQs and True/False

Note: Consolidation—EOI specifics, nested ISR patterns, PIC rotation, and debug aids.

## MCQs (English Qs, Bangla explanations)

1) Which OCW controls EOI and rotation in 8259A?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4
Answer: B
Explanation (Bangla): OCW2—EOI (specific/non-specific) এবং rotate প্রায়োরিটি কন্ট্রোল।

2) Which OCW enables Poll and selects IRR/ISR readback?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW2
Answer: C
Explanation (Bangla): OCW3—POLL/RR/IRR/ISR সিলেক্ট ও SMM কন্ট্রোল।

3) A correct nested ISR pattern is:
- A. PUSH regs → CLI → work → POP regs → RET
- B. PUSH regs → critical work with IF=0 → STI → non-critical work → POP regs → IRET
- C. CLI → work → IRET
- D. PUSHF → POPF → RETF
Answer: B
Explanation (Bangla): ক্রিটিকাল অংশে IF=0, পরে STI দিয়ে উচ্চ-প্রায়োরিটি নেস্টিং allow করা যায়; শেষে POP ও IRET।

4) Rotation-on-EOI is most useful when:
- A. Only one source exists
- B. A few sources are starved due to fixed priority
- C. NMI keeps firing
- D. INTO is used
Answer: B
Explanation (Bangla): ফিক্সড প্রায়োরিটিতে কিছু সোর্স বঞ্চিত হলে রোটেশন ফেয়ারনেস আনে।

5) For debugging ISR entry timing, which is most direct?
- A. Place INT 3 at random
- B. Toggle a GPIO/port bit at ISR entry/exit
- C. Use HLT
- D. Disable all interrupts
Answer: B
Explanation (Bangla): পোর্ট টগল করলে লজিক অ্যানালাইজারে ISR এন্ট্রি/এক্সিট টাইমিং দেখা যায়।

6) If the system must not be preempted during a very short critical update, you should:
- A. Keep IF=0 for the entire program
- B. Wrap the update with CLI/ STI
- C. Use RET
- D. Use INTO
Answer: B
Explanation (Bangla): স্বল্প-সময়ের ক্রিটিকাল সেকশনে CLI/STI যথেষ্ট; দীর্ঘ সময় ব্লক করা উচিত নয়।

7) INT 3 is convenient for patching because:
- A. Two-byte opcode fits everywhere
- B. One-byte opcode CC can replace any single byte
- C. It automatically restores FLAGS
- D. It requires INTA
Answer: B
Explanation (Bangla): CC এক বাইট—যেকোনো জায়গায় ইনসার্ট সহজ।

8) Specific EOI should be preferred over non-specific when:
- A. There is only one IRQ
- B. Precise level control is needed in nested/cascaded setups
- C. Rotation is disabled
- D. INTR is not used
Answer: B
Explanation (Bangla): নির্দিষ্ট লেভেল ক্লিয়ার করে সঠিক নেস্টিং বজায় রাখা যায়।

9) After IRET, IF becomes:
- A. Always 0
- B. Always 1
- C. Whatever was saved in FLAGS
- D. Random
Answer: C
Explanation (Bangla): IRET FLAGS পপ করে—সেভ করা IF মানেই ফিরে যায়।

10) The reason RET is not used from ISR is that it does not:
- A. Pop FLAGS
- B. Pop CS
- C. Pop IP
- D. All of the above
Answer: D
Explanation (Bangla): RET সাবরুটিনের জন্য; ISR কনটেক্সট (FLAGS, CS, IP) পুনঃস্থাপনে IRET দরকার।

## True/False (English statements, Bangla explanations)

1) OCW2 manages EOI/rotation; OCW3 manages poll/readback.
- Answer: True
- Explanation (Bangla): OCW2=EOI/rotate, OCW3=poll/RR/IRR/ISR/SMM।

2) Using RET from ISR is equivalent to IRET if no flags changed.
- Answer: False
- Explanation (Bangla): FLAGS ফেরত আসবে না—Iretই দরকার।

3) GPIO toggling at ISR entry/exit helps measure latency and service time.
- Answer: True
- Explanation (Bangla): টাইমিং প্রোফাইলে কার্যকর পদ্ধতি।

4) Rotation helps prevent starvation in fixed-priority systems.
- Answer: True
- Explanation (Bangla): ফেয়ারনেস বাড়াতে রোটেশন কার্যকর।

5) CLI/STI around a very short critical update is a common safe pattern.
- Answer: True
- Explanation (Bangla): সংক্ষিপ্ত সেকশনে কার্যকর; দীর্ঘ ব্লকিং এড়ানো উচিত।
