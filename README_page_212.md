# 8086 Interrupts — Page 212 MCQs and True/False

Note: Emphasis on practical ISR design patterns, latency control, and typical exam traps.

## MCQs (English Qs, Bangla explanations)

1) Which of the following is NOT recommended inside a time-critical ISR?
- A. Short critical section with CLI
- B. Busy-wait loops for long I/O
- C. Deferring work to main loop
- D. Saving/restoring used registers
Answer: B
Explanation (Bangla): লম্বা busy-wait ISR-কে ধীর করে, লেটেন্সি বাড়ায়; জরুরি কাজ করে দ্রুত বেরোনো উচিত।

2) To preserve data integrity in shared variables between ISR and main code, you should:
- A. Use volatile and disable interrupts around access
- B. Assume atomicity for 16-bit access
- C. Avoid using stack
- D. Clear DF
Answer: A
Explanation (Bangla): শেয়ারড ডেটা পড়া/লেখার আগে/পরে স্বল্প সময়ের জন্য CLI/STI দিয়ে ক্রিটিকাল সেকশন প্রটেক্ট করা যায়; ভলাটাইল (বা সমতুল্য) দিয়ে কম্পাইলার অপ্টিমাইজেশন নিয়ন্ত্রণ করা ভালো।

3) Which pair about flags is correct during interrupt entry?
- A. TF and IF are set
- B. TF and IF are cleared
- C. Only TF is cleared
- D. Only IF is cleared
Answer: B
Explanation (Bangla): 8086 ইন্টারাপ্ট এন্ট্রিতে IF ও TF দুটোই ক্লিয়ার হয়।

4) For nested interrupts allowing higher-priority preemption, an ISR should:
- A. Keep IF=0 throughout
- B. Execute STI after saving state
- C. Execute HLT
- D. Use IRET immediately
Answer: B
Explanation (Bangla): সেভিং শেষ হলে STI করলে উচ্চ-প্রায়োরিটি ইন্টারাপ্ট ISR-কে প্রিপ্ট করতে পারে।

5) Which is a correct IVT calculation for type n?
- A. Physical address = 00000h + 4×n
- B. Logical address = CS:IP stored at 00000h + 4×n
- C. Both A and B
- D. None
Answer: C
Explanation (Bangla): ফিজিক্যাল অফসেট 4×n-এ 4 বাইটে IP, CS রাখা থাকে; এগুলো মিলে ISR-এর CS:IP গঠিত হয়।

6) INT 3 is primarily used for:
- A. Divide operations
- B. Breakpoints during debugging
- C. Overflow detection
- D. NMI testing
Answer: B
Explanation (Bangla): INT 3-এর এক বাইট অপকোড (CC) ডিবাগিংয়ে ব্রেকপয়েন্ট সেট করতে ব্যবহার করা হয়।

7) The instruction INTO transfers control to type 4 only when:
- A. ZF=1
- B. CF=1
- C. OF=1
- D. SF=1
Answer: C
Explanation (Bangla): OVERFLOW ফ্ল্যাগ সেট থাকলে তবেই টাইপ 4 ISR-এ নিয়ন্ত্রণ যায়।

8) An ISR that modifies DS or ES should:
- A. Not restore them
- B. Restore them before IRET
- C. Use RETF
- D. Use POPF
Answer: B
Explanation (Bangla): সেগমেন্ট রেজিস্টার পরিবর্তন করলে পুরনো মান POP করে ফিরিয়ে না দিলে কলার কনটেক্সট ভেঙে যাবে।

9) Which of the following is true for NMI?
- A. Vector number is programmable by PIC
- B. Vector number is fixed (type 2)
- C. Requires INTA cycle
- D. Masked by IF=0
Answer: B
Explanation (Bangla): NMI টাইপ 2—ফিক্সড; INTA লাগে না এবং IF দ্বারা মাস্ক হয় না।

10) The correct return from ISR is:
- A. RET
- B. IRET
- C. RETF without FLAGS restore
- D. JMP far
Answer: B
Explanation (Bangla): IRET ছাড়া ফ্ল্যাগস পুনঃস্থাপন হয় না—সঠিক রিটার্ন নয়।

## True/False (English statements, Bangla explanations)

1) Shared data accessed by both ISR and main code may need atomic sections guarded by CLI/STI.
- Answer: True
- Explanation (Bangla): স্বল্প-সময়ের CLI/STI গার্ডিং রেস কন্ডিশন কমায়।

2) Long computations are better placed inside ISR to reduce context switches.
- Answer: False
- Explanation (Bangla): ISR ছোট ও দ্রুত হওয়া উচিত—দীর্ঘ কাজ defer করে মেইন লুপে করুন।

3) INT n behaves like a hardware interrupt in context save/restore.
- Answer: True
- Explanation (Bangla): INT n FLAGS/CS/IP পুশ করে, IVT-ভিত্তিক ISR-এ যায়।

4) Clearing IF using CLI will also disable NMI.
- Answer: False
- Explanation (Bangla): NMI non-maskable—IF প্রভাব ফেলে না।

5) IVT stores the full physical address of ISR.
- Answer: False
- Explanation (Bangla): IVT CS:IP (লজিক্যাল) অংশ সংরক্ষণ করে; ফিজিক্যাল ঠিকানা সেগমেন্ট:অফসেট কনভার্সন থেকে নির্ণীত হয়।
