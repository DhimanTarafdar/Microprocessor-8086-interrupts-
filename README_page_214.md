# 8086 Interrupts — Page 214 MCQs and True/False

Note: Focus on latency, vector address math, ISR prologue/epilogue, and safe flag/segment handling.

## MCQs (English Qs, Bangla explanations)

1) For interrupt type n, the physical address of the vector entry is:
- A. 00000h + n
- B. 00000h + 2×n
- C. 00000h + 4×n
- D. 00000h + 8×n
Answer: C
Explanation (Bangla): প্রতিটি এন্ট্রি 4 বাইট, তাই অফসেট 4×n; এন্ট্রিতে IP (2B) ও CS (2B) থাকে।

2) If type = 09h, the vector entry starts at:
- A. 0020h
- B. 0024h
- C. 0036h
- D. 0048h
Answer: B
Explanation (Bangla): 4×9 = 36 দশমিক = 24h; সেখানেই IP (লো-ওয়ার্ড) ও CS (হাই-ওয়ার্ড) থাকে।

3) On interrupt entry, which order is used for automatic pushes?
- A. IP, CS, FLAGS
- B. FLAGS, CS, IP
- C. CS, IP, FLAGS
- D. FLAGS, IP, CS
Answer: B
Explanation (Bangla): ক্রম: FLAGS→CS→IP; IRET করলে IP→CS→FLAGS পপ হয়।

4) Which flags are cleared by hardware on entry to an ISR?
- A. IF only
- B. TF only
- C. IF and TF
- D. CF and OF
Answer: C
Explanation (Bangla): IF ও TF ক্লিয়ার হয়—নেস্টিং/সিঙ্গল-স্টেপিং নিয়ন্ত্রণে সাহায্য করে।

5) To safely use string instructions in ISR when DF might be unknown, you should first:
- A. CLC
- B. CLD
- C. STI
- D. INTO
Answer: B
Explanation (Bangla): DF অনির্দিষ্ট থাকলে MOVS/LODS/STOS বিপর্যস্ত হতে পারে; CLD দিয়ে forward দিক নিশ্চিত করুন (শেষে প্রয়োজন হলে DF পুনঃস্থাপন)।

6) Which is a recommended ISR prologue sequence?
- A. CLI; PUSH regs
- B. PUSH regs; CLI (if needed)
- C. POP regs; STI
- D. HLT
Answer: B
Explanation (Bangla): আগে ব্যবহৃত রেজিস্টার PUSH করুন; ক্রিটিকাল অংশের আগে CLI (যদি দরকার হয়)।

7) A main contributor to interrupt latency on 8086 is:
- A. IVT size
- B. Current instruction length/complexity
- C. Number of segments
- D. Number of general-purpose registers
Answer: B
Explanation (Bangla): CPU ইনস্ট্রাকশন বাউন্ডারিতে ইন্টারাপ্ট গ্রহণ করে; লম্বা/ধীর ইনস্ট্রাকশন (যেমন কিছু I/O বা স্ট্রিং অপ) ল্যাটেন্সি বাড়ায়।

8) INT n behaves like hardware interrupt except that it:
- A. Doesn’t push FLAGS
- B. Doesn’t use IVT
- C. Doesn’t generate INTA cycles
- D. Clears OF and CF
Answer: C
Explanation (Bangla): সফটওয়্যার INT-এ INTA দরকার হয় না; বাকিটা হার্ডওয়্যার ইন্টারাপ্টের মতই।

9) If an ISR modifies DS/ES, best practice is to:
- A. Ignore restoring them
- B. Restore them before IRET
- C. Use RETF instead of IRET
- D. Use POPF only
Answer: B
Explanation (Bangla): সেগমেন্ট রেজিস্টার না ফিরালে কলারের কনটেক্সট ভেঙে যায়।

10) The correct ISR epilogue is:
- A. POP regs; RET
- B. POP regs; IRET
- C. IRET; POP regs
- D. RETF only
Answer: B
Explanation (Bangla): রেজিস্টারগুলো POP করে শেষে IRET—তবেই IP, CS, FLAGS পুনঃস্থাপিত হয়।

11) During ISR, temporarily re-enabling interrupts to allow higher-priority service is done by:
- A. CLI
- B. STI
- C. CMC
- D. CLC
Answer: B
Explanation (Bangla): ক্রিটিকাল অংশ পেরিয়ে STI করলে উচ্চ প্রায়োরিটি ইন্টারাপ্ট নেস্ট করতে পারে।

12) Which statement about PUSHF/POPF inside ISR is most reasonable?
- A. Always unnecessary
- B. Useful if the ISR inspects/modifies flags and must restore them
- C. Replaces IRET
- D. Disables NMI
Answer: B
Explanation (Bangla): কখনও কখনও ফ্ল্যাগ দেখা/পরিবর্তনের দরকার হলে PUSHF/POPF করা যায়; তবে ISR থেকে রিটার্নের জন্য IRET বাধ্যতামূলক।

## True/False (English statements, Bangla explanations)

1) Vector entry stores the full physical address of ISR.
- Answer: False
- Explanation (Bangla): শুধু CS:IP থাকে; ফিজিক্যাল ঠিকানা সেগমেন্ট:অফসেট কনভার্সন থেকে আসে।

2) CLD is helpful in ISR to ensure forward string operations.
- Answer: True
- Explanation (Bangla): DF=0 হলে স্ট্রিং অপারেশন ফরোয়ার্ড; ISR-এ নিশ্চিত করতে CLD ব্যবহার করা নিরাপদ।

3) Long string operations can increase interrupt latency.
- Answer: True
- Explanation (Bangla): ইনস্ট্রাকশন সম্পূর্ণ না হওয়া পর্যন্ত ইন্টারাপ্ট ডিফার হতে পারে; ফলে ল্যাটেন্সি বাড়ে।

4) Using RET from an ISR is equivalent to IRET.
- Answer: False
- Explanation (Bangla): RET FLAGS ফেরত আনে না—IRET-ই সঠিক পদ্ধতি।

5) IF and TF are restored automatically by IRET.
- Answer: True
- Explanation (Bangla): IRET FLAGS পপ করে—IF/TF আগের মানে ফিরে যায়।
