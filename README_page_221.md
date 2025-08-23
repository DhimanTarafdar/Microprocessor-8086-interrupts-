# 8086 Interrupts — Page 221 MCQs and True/False

Note: Calculations, timing, and subtle flag behaviors.

## MCQs (English Qs, Bangla explanations)

1) If IF=0 and an INTR arrives during instruction execution, service will occur:
- A. Immediately
- B. At the next boundary even if IF=0
- C. After IF is set to 1 and boundary reached
- D. Never
Answer: C
Explanation (Bangla): IF=0 অবস্থায় সার্ভিস হবে না; IF=1 করা হলে পরবর্তী ইনস্ট্রাকশন বাউন্ডারিতে সার্ভিস হয়।

2) The amount SP changes on interrupt entry is:
- A. +6
- B. −6
- C. −4
- D. 0
Answer: B
Explanation (Bangla): FLAGS, CS, IP—মোট 6 বাইট পুশ হওয়ায় SP 6 কমে।

3) The type number for overflow interrupt used by INTO is:
- A. 0
- B. 1
- C. 3
- D. 4
Answer: D
Explanation (Bangla): INTO → টাইপ 4।

4) The location of NMI vector entry is at offset:
- A. 0000h
- B. 0004h
- C. 0008h
- D. 000Ch
Answer: C
Explanation (Bangla): টাইপ 2 → 4×2 = 0008h।

5) The instruction to enable maskable interrupts is:
- A. CLI
- B. STI
- C. IRET
- D. HLT
Answer: B
Explanation (Bangla): STI IF সেট করে।

6) Which best explains the effect of IRET?
- A. Pops IP, CS, FLAGS
- B. Pops only IP and CS
- C. Pops FLAGS then IP
- D. Jumps to IVT
Answer: A
Explanation (Bangla): IRET স্ট্যাক থেকে IP, CS, FLAGS পপ করে কনটেক্সট রিস্টোর করে।

7) INT 3 differs from INT n because it:
- A. Is non-maskable
- B. Uses a one-byte opcode CC
- C. Uses INTA
- D. Clears IF
Answer: B
Explanation (Bangla): INT 3 এক বাইট—ডিবাগিংয়ে সুবিধা।

8) HLT will resume on INTR only when:
- A. IF=1
- B. IF=0
- C. OF=1
- D. DF=1
Answer: A
Explanation (Bangla): INTR-এ জাগতে IF=1 থাকা চাই; NMI/RESET সবসময় জাগায়।

9) A correct practice for an ISR that modifies the direction flag is:
- A. Leave DF as set
- B. Always CLD on entry and restore DF before exit if changed
- C. Use STC
- D. Use CLC
Answer: B
Explanation (Bangla): স্ট্রিং অপারেশনের জন্য DF গুরুত্বপূর্ণ—সেফ পাথ: এন্ট্রিতে CLD, শেষে আগের মান ফিরিয়ে দিন।

10) IVT entry size is 4 bytes because it stores:
- A. IP (2B) + CS (2B)
- B. Physical address (4B)
- C. IP only (4B)
- D. CS only (4B)
Answer: A
Explanation (Bangla): 2 বাইট IP + 2 বাইট CS।

## True/False (English statements, Bangla explanations)

1) IF must be 1 for INTR to be serviced.
- Answer: True
- Explanation (Bangla): IF=1 না হলে মাস্কেবল ইন্টারাপ্ট ব্লক।

2) IRET restores the IF and TF flags from the saved FLAGS.
- Answer: True
- Explanation (Bangla): FLAGS পপ হওয়ায় IF/TF পূর্বাবস্থায় ফেরে।

3) INT 3 requires INTA cycles.
- Answer: False
- Explanation (Bangla): সফটওয়্যার INT-এ INTA নেই।

4) NMI vector is fixed and does not depend on PIC.
- Answer: True
- Explanation (Bangla): টাইপ 2—ফিক্সড।

5) HLT ignores all interrupts.
- Answer: False
- Explanation (Bangla): INTR (IF=1), NMI, RESET HLT-কে জাগাতে পারে।
