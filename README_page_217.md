# 8086 Interrupts — Page 217 MCQs and True/False

Note: Priority handling, latency nuances, HLT behavior, and good ISR practices.

## MCQs (English Qs, Bangla explanations)

1) With an 8259A in fully nested mode, which pending request is serviced first?
- A. Lowest-numbered unmasked IR (IR0 highest priority)
- B. Highest-numbered unmasked IR (IR7 highest priority)
- C. Random pending IR
- D. The one that arrived first
Answer: A
Explanation (Bangla): ডিফল্ট fully nested মোডে IR0 সর্বোচ্চ প্রায়োরিটি; তাই সর্বনিম্ন নম্বরের আনমাস্কড রিকোয়েস্ট আগে সার্ভিস হয়।

2) If an ISR forgets to send EOI (Auto EOI disabled), likely outcome is:
- A. CPU resets automatically
- B. That IRQ remains in-service and equal/lower priorities are blocked
- C. All interrupts get disabled permanently
- D. NMI is ignored
Answer: B
Explanation (Bangla): EOI না দিলে PIC ISR বিট ক্লিয়ার করে না—ফলে একই বা নিচু প্রায়োরিটি আর সার্ভিস পাবে না।

3) After executing STI on 8086, when can maskable interrupts be recognized?
- A. Immediately, before the next instruction
- B. Only after the next instruction executes
- C. Only after IRET
- D. Only after HLT
Answer: B
Explanation (Bangla): STI-এর পরে পরবর্তী ইনস্ট্রাকশন সম্পন্ন না হওয়া পর্যন্ত ইন্টারাপ্ট স্বীকৃত হয় না—একটি ইন্সট্রাকশন-ডিলে থাকে।

4) The HLT instruction resumes execution upon:
- A. Any INTR irrespective of IF
- B. INTR only if IF=1, or on NMI/RESET always
- C. Only on RESET
- D. Only on NMI
Answer: B
Explanation (Bangla): IF=0 হলে INTR HLT থেকে জাগাতে পারবে না; তবে NMI/RESET সবসময় জাগায়।

5) Best practice to share a flag between ISR and main code is to:
- A. Use a normal global without any care
- B. Guard access with short CLI/STI critical sections
- C. Use RET from ISR
- D. Never access shared data
Answer: B
Explanation (Bangla): শেয়ারড ফ্ল্যাগ/ডেটা রেস এড়াতে সংক্ষিপ্ত CLI/STI সেকশন বা লকিং ব্যবহার করুন।

6) Which statement about latency is correct?
- A. Interrupts can arrive and preempt mid-instruction
- B. Interrupts are sampled at instruction boundaries
- C. NMI waits for HLT to complete
- D. IVT size affects latency directly
Answer: B
Explanation (Bangla): 8086 সাধারণত ইনস্ট্রাকশন বাউন্ডারিতে ইন্টারাপ্ট স্যাম্পল করে—চলমান ইনস্ট্রাকশন শেষ হলে সার্ভিস হয়।

7) Vector address for type 3 in IVT starts at offset:
- A. 0006h
- B. 0008h
- C. 000Ch
- D. 0010h
Answer: C
Explanation (Bangla): অফসেট = 4×type = 4×3 = 0Ch; সেখানে IP (2B), CS (2B) থাকে।

8) Which event is maskable by IF?
- A. INTR
- B. NMI
- C. RESET
- D. INTO
Answer: A
Explanation (Bangla): INTR মাস্কেবল; IF=0 হলে ব্লক হয়। NMI/RESET মাস্কেবল নয়; INTO সফটওয়্যার ইন্টারাপ্ট।

9) A re-entrant ISR usually requires:
- A. No stack usage
- B. Avoiding global state or protecting it properly
- C. Ending with RET
- D. Disabling interrupts throughout
Answer: B
Explanation (Bangla): রিএন্ট্রান্সি বজায় রাখতে গ্লোবাল স্টেট এড়ানো বা সঠিক প্রটেকশন দরকার; স্ট্যাক-ভিত্তিক লোকাল ডেটা নিরাপদ।

10) The order of automatic pushes on interrupt entry is:
- A. IP, CS, FLAGS
- B. FLAGS, CS, IP
- C. CS, IP, FLAGS
- D. FLAGS, IP, CS
Answer: B
Explanation (Bangla): ক্রম FLAGS→CS→IP; IRET-এ উল্টো ক্রমে পপ হয়।

## True/False (English statements, Bangla explanations)

1) In fully nested mode, IR0 has the highest priority.
- Answer: True
- Explanation (Bangla): ডিফল্টে IR0>IR1>…>IR7।

2) Forgetting EOI can block subsequent equal/lower-priority interrupts.
- Answer: True
- Explanation (Bangla): ISR বিট ক্লিয়ার না হলে PIC নতুন ইন্টারাপ্ট সার্ভিস করতে দেয় না।

3) After STI, interrupts may be recognized immediately before the next instruction.
- Answer: False
- Explanation (Bangla): STI-এর পরে অন্তত একটি ইনস্ট্রাকশনের বিলম্ব থাকে।

4) HLT wakes on INTR even if IF=0.
- Answer: False
- Explanation (Bangla): IF=0 হলে INTR HLT থেকে জাগাতে পারে না; NMI/RESET পারে।

5) Interrupts can preempt mid-instruction on 8086.
- Answer: False
- Explanation (Bangla): সাধারণত কেবল ইনস্ট্রাকশন বাউন্ডারিতে।

6) Type 3 vector entry offset is 000Ch.
- Answer: True
- Explanation (Bangla): 4×3=0Ch।

7) INTO is a hardware interrupt input pin.
- Answer: False
- Explanation (Bangla): INTO সফটওয়্যার ইন্সট্রাকশন—OF=1 হলে টাইপ 4 কল হয়।

8) Re-entrant ISR should avoid unprotected global state.
- Answer: True
- Explanation (Bangla): না হলে নেস্টেড কল-এ ডেটা করাপশনের ঝুঁকি।

9) NMI is maskable when IF=0.
- Answer: False
- Explanation (Bangla): NMI non-maskable।

10) IRET restores the FLAGS, CS, and IP.
- Answer: True
- Explanation (Bangla): IRET-ই সঠিক রিটার্ন—সম্পূর্ণ কনটেক্সট ফেরত আনে।
