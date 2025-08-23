# 8086 Interrupts — Page 222 MCQs and True/False

Note: Mixed review—PIC operations, software vs hardware interrupts, and safe ISR patterns.

## MCQs (English Qs, Bangla explanations)

1) Which instruction sequence is safest at the start of an ISR that uses string ops?
- A. STI; CLD; PUSH AX
- B. PUSH regs; CLD; (optional CLI)
- C. CLC; STC; NOP
- D. RETF
Answer: B
Explanation (Bangla): প্রয়োজনীয় রেজিস্টার সেভ করে CLD; ক্রিটিকাল সেকশনে গেলে CLI।

2) Which combination is correct about PIC registers?
- A. IMR=mask, IRR=pending, ISR=in-service
- B. IMR=in-service, IRR=mask, ISR=pending
- C. IMR=pending, IRR=mask, ISR=rotate
- D. All swapped
Answer: A
Explanation (Bangla): IMR (মাস্ক), IRR (পেন্ডিং), ISR (ইন-সার্ভিস)।

3) Software INT n differs from INTR because INT n:
- A. Needs INTA
- B. Ignores IF state
- C. Doesn’t push FLAGS
- D. Is non-maskable
Answer: B
Explanation (Bangla): INT n IF-ডিপেন্ডেন্ট নয়; সরাসরি কনটেক্সট সেভ করে ভেক্টরে জাম্প করে।

4) Which is TRUE about NMI?
- A. Masked by IF
- B. Type number fixed at 2
- C. Provided by PIC on INTA
- D. Requires STI
Answer: B
Explanation (Bangla): NMI টাইপ 2—ফিক্সড; IF/INTA নির্ভর নয়।

5) The correct end of an ISR with saved registers is:
- A. POP regs; IRET
- B. POP regs; RET
- C. IRET; POP regs
- D. RETF only
Answer: A
Explanation (Bangla): POP করে IRET—তবেই সম্পূর্ণ কনটেক্সট ফিরবে।

6) Priority rotation is configured via:
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW2
Answer: B
Explanation (Bangla): OCW2-তে EOI/রোটেশন কন্ট্রোল থাকে।

7) Poll mode selection happens via:
- A. OCW3
- B. OCW2
- C. ICW4
- D. ICW1
Answer: A
Explanation (Bangla): OCW3-এর POLL/RR/IRR/ISR সিলেক্ট।

8) The vector table stores:
- A. Physical addresses
- B. Logical CS:IP pairs
- C. I/O port numbers
- D. Opcode bytes
Answer: B
Explanation (Bangla): CS:IP—প্রতিটি 2 বাইট করে।

9) After STI inside an ISR, interrupts are recognized:
- A. Immediately
- B. After the next instruction
- C. Only after IRET
- D. Only on HLT
Answer: B
Explanation (Bangla): এক ইন্সট্রাকশন-ডিলে।

10) INTO routes to which type when OF=1?
- A. 0
- B. 1
- C. 3
- D. 4
Answer: D
Explanation (Bangla): ওভারফ্লো ইন্টারাপ্ট টাইপ 4।

## True/False (English statements, Bangla explanations)

1) IMR bits set to 1 mean the corresponding IRQ is enabled.
- Answer: False
- Explanation (Bangla): 1 মানে মাস্কড/ডিসেবল।

2) Software INT n saves FLAGS, CS, IP and jumps via IVT.
- Answer: True
- Explanation (Bangla): হার্ডওয়্যার ইন্টারাপ্টের মতোই কনটেক্সট সেভ করে।

3) NMI uses a fixed vector and does not depend on INTA.
- Answer: True
- Explanation (Bangla): টাইপ 2—INTA লাগে না।

4) POPF at the end of an ISR replaces the need for IRET.
- Answer: False
- Explanation (Bangla): IRET ছাড়া IP/CS ফেরে না।

5) OCW2 controls EOI and priority rotation.
- Answer: True
- Explanation (Bangla): OCW2-তেই EOI/Rotation কন্ট্রোল থাকে।
