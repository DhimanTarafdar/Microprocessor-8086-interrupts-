# 8086 Interrupts — Page 225 MCQs and True/False

Note: Final quick-hit checks—verify you can do vector math, flow order, and PIC interactions confidently.

## MCQs (English Qs, Bangla explanations)

1) Vector entry offset for type n is:
- A. n
- B. 2n
- C. 4n
- D. 8n
Answer: C
Explanation (Bangla): প্রতিটি এন্ট্রি 4 বাইট—অফসেট 4×n।

2) On interrupt entry, the order of automatic pushes is:
- A. IP, CS, FLAGS
- B. FLAGS, CS, IP
- C. CS, IP, FLAGS
- D. FLAGS, IP, CS
Answer: B
Explanation (Bangla): FLAGS→CS→IP।

3) The correct return from ISR is:
- A. RET
- B. IRET
- C. RETF
- D. JMP far
Answer: B
Explanation (Bangla): IRET-ই IP, CS, FLAGS রিস্টোর করে।

4) INTA is associated with:
- A. INTR via PIC
- B. NMI
- C. INT n
- D. INTO
Answer: A
Explanation (Bangla): INTR-এর ক্ষেত্রে 8259A INTA-তে টাইপ/ভেক্টর দেয়।

5) Auto EOI is configured in:
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4
Answer: D
Explanation (Bangla): ICW4-এ Auto EOI/8086 মোড ইত্যাদি।

6) The overflow interrupt is:
- A. Type 0
- B. Type 1
- C. Type 3
- D. Type 4
Answer: D
Explanation (Bangla): INTO → টাইপ 4।

7) The breakpoint interrupt is:
- A. Type 3, opcode CC
- B. Type 4, opcode CC
- C. Type 3, opcode CD
- D. Type 1, opcode CC
Answer: A
Explanation (Bangla): INT 3—CC এক বাইট।

8) IF=0 will:
- A. Disable NMI and INTR
- B. Disable INTR but not NMI
- C. Disable only software INT n
- D. Disable INTO
Answer: B
Explanation (Bangla): IF কেবল মাস্কেবল INTR নিয়ন্ত্রণ করে; NMI non-maskable।

9) The IVT size is:
- A. 256 bytes
- B. 512 bytes
- C. 1024 bytes
- D. 4096 bytes
Answer: C
Explanation (Bangla): 256×4 = 1024 বাইট।

10) On entry, 8086 clears which flags?
- A. CF and OF
- B. DF and AF
- C. IF and TF
- D. ZF and SF
Answer: C
Explanation (Bangla): IF/TF ক্লিয়ার—নিরাপদ এক্সিকিউশনের জন্য।

## True/False (English statements, Bangla explanations)

1) NMI uses INTA to get its vector.
- Answer: False
- Explanation (Bangla): টাইপ 2—INTA লাগে না।

2) INT n ignores IF state.
- Answer: True
- Explanation (Bangla): সফটওয়্যার INT—IF=0 হলেও ট্রিগার হয়।

3) EOI is required after servicing INTR via PIC (if Auto EOI disabled).
- Answer: True
- Explanation (Bangla): OCW2 দিয়ে EOI পাঠাতে হয়।

4) RET from ISR is acceptable if FLAGS wasn’t modified.
- Answer: False
- Explanation (Bangla): IRET বাধ্যতামূলক—FLAGS/CS/IP ফিরিয়ে দেয়।

5) IVT stores CS:IP pairs, not physical addresses.
- Answer: True
- Explanation (Bangla): ফিজিক্যাল = CS×16 + IP; টেবিলে লজিক্যাল জোড়া থাকে।
