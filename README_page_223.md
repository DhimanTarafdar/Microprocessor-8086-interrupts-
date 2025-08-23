# 8086 Interrupts — Page 223 MCQs and True/False

Note: Advanced flow details—IF/TF interplay, ISR reentrancy guards, timing nuances, safe flag handling.

## MCQs (English Qs, Bangla explanations)

1) Which flags are cleared by hardware on interrupt entry in 8086?
- A. CF and OF
- B. IF and TF
- C. ZF and SF
- D. DF and AF
Answer: B
Explanation (Bangla): ইন্টারাপ্ট এন্ট্রিতে IF ও TF ক্লিয়ার হয়—নতুন ISR চলাকালে নেস্টিং/সিঙ্গল-স্টেপিং বন্ধ রাখতে।

2) A software reentrancy guard in ISR is commonly implemented by:
- A. Using NOP
- B. Using a software semaphore/flag checked at ISR entry
- C. Using HLT
- D. Using RET instead of IRET
Answer: B
Explanation (Bangla): ISR এন্ট্রিতে ফ্ল্যাগ/সেমাফোর চেক করে রিএন্ট্রি ব্লক করা যায়; এক্সিটে ফ্ল্যাগ ক্লিয়ার করা হয়।

3) Which is the safest order for a non-reentrant ISR that needs a critical section?
- A. STI → work → CLI → IRET
- B. PUSH regs → (optional CLI) → work → (optional STI) → POP regs → IRET
- C. PUSH regs → work → RET
- D. CLI → work → RETF
Answer: B
Explanation (Bangla): আগে সেভ, প্রয়োজন হলে CLI; কাজ শেষে প্রয়োজনে STI; তারপর POP ও IRET।

4) If an ISR executes POPF before IRET and modifies IF=1, then:
- A. It has no effect until after IRET
- B. Higher-priority interrupts may nest after the next instruction
- C. NMI is disabled
- D. INTO triggers
Answer: B
Explanation (Bangla): POPF দিয়ে IF=1 করলে পরবর্তী ইনস্ট্রাকশন শেষে মাস্কেবল ইন্টারাপ্ট সক্রিয় হতে পারে—নেস্টিং সম্ভব।

5) Single-stepping an ISR using TF is typically avoided because:
- A. TF is always 0 in ISR
- B. TF forces Type 1 after every instruction, causing recursion/nesting
- C. TF disables NMI
- D. TF clears IF
Answer: B
Explanation (Bangla): TF=1 হলে প্রতিটি ইন্সট্রাকশনের পর টাইপ 1—ISR ভিতরেই অতিরিক্ত ইন্টারাপ্ট হয়ে জটিলতা/রিএন্ট্রি বাড়ে।

6) The effect of CLI just before IRET is to:
- A. Prevent IRET from restoring IF
- B. Ensure IF remains cleared until FLAGS is popped by IRET
- C. Trigger NMI
- D. Send EOI automatically
Answer: B
Explanation (Bangla): IRET FLAGS পপ করার সময় IF পূর্ব মানে ফিরবে; তবে IRET পর্যন্ত IF=0 থাকায় নেস্টিং এড়ানো যায়।

7) To ensure string operations behave predictably inside ISR when DF is unknown, use:
- A. STC
- B. CMC
- C. CLD at entry and restore DF if needed
- D. HLT
Answer: C
Explanation (Bangla): CLD দিয়ে forward ডিরেকশন নিশ্চিত করা, শেষে আগের DF ফিরিয়ে দেওয়া নিরাপদ।

8) The best place to send EOI (when using 8259A without Auto EOI) is:
- A. Immediately at ISR entry
- B. After critical work is complete, before IRET
- C. After IRET
- D. Never needed
Answer: B
Explanation (Bangla): কাজ শেষে EOI দিলে একই/নিচু প্রায়োরিটির ইন্টারাপ্ট আবার সক্রিয় হতে পারে—আগে দিলে স্পিউরিয়াস/ডাবল-সার্ভিস ঝুঁকি।

9) A symptom of missing EOI is:
- A. CPU resets
- B. Same level appears stuck “in service” and equal/lower levels don’t trigger
- C. All flags clear
- D. NMI storms
Answer: B
Explanation (Bangla): ISR বিট ক্লিয়ার না হওয়ায় একই/নিচু লেভেল ব্লকই থেকে যায়।

10) In 8086, interrupts are sampled:
- A. Continuously
- B. At instruction boundaries
- C. Only on HLT
- D. Only after IRET
Answer: B
Explanation (Bangla): ইনস্ট্রাকশন বাউন্ডারিতে স্যাম্পল—লম্বা ইনস্ট্রাকশন ল্যাটেন্সি বাড়ায়।

## True/False (English statements, Bangla explanations)

1) IF and TF are cleared automatically on ISR entry.
- Answer: True
- Explanation (Bangla): হার্ডওয়্যার এন্ট্রিতে IF/TF ক্লিয়ার করে।

2) A simple software flag can prevent ISR reentrancy.
- Answer: True
- Explanation (Bangla): এন্ট্রিতে সেট/চেক, এক্সিটে ক্লিয়ার—রিএন্ট্রি রোধে কার্যকর।

3) POPF inside ISR can re-enable interrupts before IRET finishes.
- Answer: True
- Explanation (Bangla): IF=1 করলে এক ইন্সট্রাকশন পর থেকে নেস্টিং সম্ভব।

4) Sending EOI too early can cause missed service or re-entry issues.
- Answer: True
- Explanation (Bangla): কাজের আগে EOI দিলে একই লেভেল আবার ট্রিগার হতে পারে।

5) CLD at ISR entry is unnecessary if DF is always known.
- Answer: False
- Explanation (Bangla): অনেক সময় DF অবস্থা অনিশ্চিত—CLD নিরাপদ অভ্যাস।
