# 8086 Interrupts — Page 209 MCQs and True/False

Note: Tailored to common mid-chapter topics: hardware vs software interrupts, ISR design, PIC basics.

## MCQs (English Qs, Bangla explanations)

1) Which of the following is NOT a typical step of 8086 interrupt response?
- A. Push FLAGS
- B. Push CS and IP
- C. Clear IF and TF
- D. Clear CF and OF
Answer: D
Explanation (Bangla): ইন্টারাপ্ট এন্ট্রিতে CF/OF ক্লিয়ার হয় না। CPU FLAGS→CS→IP পুশ করে এবং IF/TF ক্লিয়ার করে।

2) Which interrupt is invoked when the Trap Flag is set and one instruction completes?
- A. Type 0
- B. Type 1
- C. Type 3
- D. Type 4
Answer: B
Explanation (Bangla): TF=1 হলে প্রতিটি ইন্সট্রাকশনের পরে টাইপ 1 (সিঙ্গল-স্টেপ) ইন্টারাপ্ট ঘটে।

3) Breakpoint interrupt uses which opcode?
- A. CD imm8
- B. CC
- C. CE
- D. CF
Answer: B
Explanation (Bangla): ব্রেকপয়েন্ট INT 3 এর জন্য অপকোড CCh (এক বাইট)। সাধারণ INT n হলো CDh + imm8।

4) Which is true about software interrupt INT n?
- A. It doesn’t save FLAGS
- B. It doesn’t push CS and IP
- C. It behaves like hardware interrupt in context save and vector fetch
- D. It requires INTA cycles
Answer: C
Explanation (Bangla): INT n হার্ডওয়্যার ইন্টারাপ্টের মতই FLAGS, CS, IP পুশ করে এবং IVT থেকে ভেক্টর নিয়ে ISR-এ যায়; INTA প্রয়োজন হয় না।

5) In a typical 8259A PIC setup with 8086, the PIC supplies:
- A. The interrupt enable/disable lines
- B. The interrupt vector/type number during INTA
- C. The ISR code directly
- D. None
Answer: B
Explanation (Bangla): INTA সাইকেলে 8259A টাইপ নম্বর সরবরাহ করে; CPU IVT থেকে সেই টাইপের এন্ট্রিতে জাম্প করে।

6) Which best practice helps ensure ISR finishes quickly?
- A. Do heavy computation inside ISR
- B. Defer work to main loop via flags/queues
- C. Avoid saving registers
- D. Disable all interrupts permanently
Answer: B
Explanation (Bangla): ISR-এ কেবল জরুরি কাজ শেষ করে বাকি কাজ মেইন লুপ/টাস্কে ডেফার করলে লেটেন্সি কম থাকে এবং সিস্টেম রেসপনসিভ হয়।

7) Which instruction sequence correctly re-enables maskable interrupts inside an ISR after critical section?
- A. CLI; STI
- B. STI; CLI
- C. CLC; STC
- D. HLT; NOP
Answer: A
Explanation (Bangla): ক্রিটিকাল সেকশনে CLI দিয়ে ব্লক করা হতে পারে; কাজ শেষে STI করে পুনরায় ইন্টারাপ্ট অন করা হয়।

8) The IVT entry stores:
- A. Only IP
- B. Only CS
- C. IP and CS of ISR
- D. IP, CS, and FLAGS
Answer: C
Explanation (Bangla): প্রতিটি এন্ট্রি 4 বাইট—2 বাইট ISR-এর IP, 2 বাইট ISR-এর CS। FLAGS সেখানে থাকে না।

9) Which pair is correct?
- A. Type 0 — Divide error
- B. Type 3 — Overflow
- C. Type 4 — Breakpoint
- D. Type 2 — Single-step
Answer: A
Explanation (Bangla): টাইপ 0 = Divide error, টাইপ 3 = Breakpoint, টাইপ 4 = Overflow (INTO), টাইপ 1 = Single-step, টাইপ 2 = NMI।

10) A re-entrant ISR is one that:
- A. Can be safely interrupted and called again before it finishes
- B. Never uses the stack
- C. Doesn’t save registers
- D. Must run with IF=0
Answer: A
Explanation (Bangla): রিএন্ট্রান্ট ISR এমনভাবে লেখা যে নেস্টেড ইনভোকেশনেও ডেটা কনসিস্টেন্সি নষ্ট না হয়—লোকাল স্টেট, রেজিস্টার সেভিং ইত্যাদি ঠিকমতো করা থাকে।

## True/False (English statements, Bangla explanations)

1) INT n requires INTA cycles from the CPU.
- Answer: False
- Explanation (Bangla): সফটওয়্যার ইন্টারাপ্টে INTA হয় না; সরাসরি টাইপ n এর ভেক্টরে জাম্প করা হয়।

2) NMI uses interrupt type 2.
- Answer: True
- Explanation (Bangla): NMI ভেক্টর হলো টাইপ 2—IVT-তে অফসেট 0008h।

3) The IVT is located starting at 00000h.
- Answer: True
- Explanation (Bangla): IVT ফিজিক্যাল 00000h থেকে শুরু করে 003FFh পর্যন্ত বিস্তৃত।

4) ISR should preserve any used registers and segment registers if modified.
- Answer: True
- Explanation (Bangla): ব্যবহৃত রেজিস্টার (GP/segment) পরিবর্তন করলে PUSH/POP দিয়ে সেভ/রিস্টোর করা উচিত।

5) INT 3 is a two-byte opcode.
- Answer: False
- Explanation (Bangla): INT 3 এক বাইটের CC অপকোড; সাধারণ INT n হলো CD imm8 (দুই বাইট)।
