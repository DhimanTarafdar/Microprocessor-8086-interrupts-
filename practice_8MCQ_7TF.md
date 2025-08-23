# Quick Practice — 8 MCQs + 7 True/False (8086 Interrupts + 8259A)

## MCQs (English questions; Bangla explanations)

1) How many interrupt types exist in 8086?
- A. 8
- B. 16
- C. 128
- D. 256
Answer: D
Explanation (Bangla): 8086-এ 0–255 মোট 256টি টাইপ; প্রত্যেকটির জন্য IVT-তে 4-বাইট ভেক্টর এন্ট্রি থাকে।

2) Which pin is the non-maskable interrupt input on 8086?
- A. INTR
- B. NMI
- C. RESET
- D. TEST
Answer: B
Explanation (Bangla): NMI non-maskable—IF দিয়ে ব্লক করা যায় না; সাধারণত রাইজিং-এজ ট্রিগার্ড।

3) The Interrupt Vector Table (IVT) starts at physical address:
- A. 00000h
- B. 10000h
- C. F0000h
- D. 0FFFF0h
Answer: A
Explanation (Bangla): IVT ফিজিক্যাল 00000h থেকে 003FFh পর্যন্ত (1024 বাইট)।

4) On interrupt entry, 8086 pushes to stack in the order:
- A. IP, CS, FLAGS
- B. FLAGS, CS, IP
- C. CS, IP, FLAGS
- D. FLAGS, IP, CS
Answer: B
Explanation (Bangla): ক্রম FLAGS→CS→IP; IRET করলে IP→CS→FLAGS পপ হয়।

5) Which flags are cleared automatically on interrupt entry?
- A. CF and OF
- B. IF and TF
- C. ZF and SF
- D. DF and AF
Answer: B
Explanation (Bangla): IF/TF ক্লিয়ার হয়—নেস্টেড/সিঙ্গল-স্টেপিং সাময়িকভাবে বন্ধ থাকে।

6) Which instruction must return from an ISR?
- A. RET
- B. RETF
- C. IRET
- D. JMP FAR
Answer: C
Explanation (Bangla): IRET স্ট্যাক থেকে IP, CS, FLAGS পপ করে—পূর্ণ কনটেক্সট পুনঃস্থাপন।

7) In 8259A, which OCW controls EOI and priority rotation?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4
Answer: B
Explanation (Bangla): OCW2 দিয়ে specific/non-specific EOI ও রোটেশন কনফিগ করা হয়।

8) In 8086 mode, effective interrupt type from PIC is computed as:
- A. ICW2 + IRQ
- B. (ICW2 & F8h) | IRQ
- C. (ICW2 << 3) | IRQ
- D. ICW2 ^ IRQ
Answer: B
Explanation (Bangla): বেসের লো 3 বিটে IRQ বসে—তাই বেস 8-অ্যালাইন্ড হওয়া উচিত (লো 3 বিট 0)।

## True/False (English statements; Bangla explanations)

1) NMI can be disabled by clearing IF.
- Answer: False
- Explanation (Bangla): NMI non-maskable; IF কেবল INTR (মাস্কেবল) নিয়ন্ত্রণ করে।

2) Software INT n requires INTA cycles from the CPU.
- Answer: False
- Explanation (Bangla): সফটওয়্যার ইন্টারাপ্টে INTA লাগে না; সরাসরি IVT-তে জাম্প হয়।

3) The IVT size is 1024 bytes (00000h–003FFh).
- Answer: True
- Explanation (Bangla): 256×4 বাইট = 1024 বাইট।

4) Auto EOI removes the need for device-level acknowledge/clear.
- Answer: False
- Explanation (Bangla): PIC-লেভেল EOI অটো; ডিভাইস স্ট্যাটাস/হ্যান্ডশেক আলাদাভাবে ক্লিয়ার করতে হয়।

5) After executing STI, interrupts are recognized immediately before the next instruction.
- Answer: False
- Explanation (Bangla): STI-এর পরে অন্তত এক ইন্সট্রাকশন-ডিলে—পরের বাউন্ডারিতে স্বীকৃত।

6) In 8259A, IRR holds pending requests and ISR holds in-service levels.
- Answer: True
- Explanation (Bangla): IRR=pending, ISR=in-service—ডিবাগে গুরুত্বপূর্ণ পার্থক্য।

7) Returning from ISR with RET is acceptable if no registers changed.
- Answer: False
- Explanation (Bangla): RET FLAGS রিস্টোর করে না; IRET-ই সঠিক—IP, CS, FLAGS তিনটাই ফেরায়।
