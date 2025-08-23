# 8086 Interrupts — Page 210 MCQs and True/False

Note: Focus on ISR structure, nested interrupts, and sample flows; adapt to your highlights if any.

## MCQs (English Qs, Bangla explanations)

1) Which is the correct minimal skeleton of an 8086 ISR?
- A. IRET; PUSH regs; work; POP regs
- B. PUSH regs; optional CLI; work; optional STI; POP regs; IRET
- C. PUSH regs; RET; POP regs
- D. HLT; IRET
Answer: B
Explanation (Bangla): ISR-এ প্রথমে প্রয়োজনীয় রেজিস্টার PUSH, ক্রিটিকাল সেকশনে CLI, শেষে POP ও IRET। প্রয়োজনে কাজের শেষে STI দিয়ে ইন্টারাপ্ট পুনরায় চালু করা হয়।

2) If an ISR needs to call another subroutine, best practice is to:
- A. Avoid using stack
- B. Save all used registers before the call
- C. Use RET to return to caller
- D. Disable interrupts forever
Answer: B
Explanation (Bangla): সাবরুটিন কলের আগে ব্যবহৃত রেজিস্টার সেভ করলে কলার কনটেক্সট ক্ষতিগ্রস্ত হয় না; শেষে POP করে পুনরুদ্ধার করা হয়।

3) Nested interrupts are typically allowed by:
- A. Executing STI inside ISR after critical section
- B. Keeping CLI asserted for entire ISR
- C. Using HLT
- D. Using INTO
Answer: A
Explanation (Bangla): ক্রিটিকাল অংশ শেষ হলে STI করলে উচ্চ-প্রায়োরিটি ইন্টারাপ্ট নেস্ট করে ঢুকতে পারে—রিএন্ট্রান্সি ও স্ট্যাক গভীরতা বিবেচ্যায়।

4) Which interrupt is generated when INTO is executed and OF=1?
- A. Type 0
- B. Type 2
- C. Type 3
- D. Type 4
Answer: D
Explanation (Bangla): INTO ওভারফ্লো থাকলে (OF=1) টাইপ 4 ইন্টারাপ্ট কল করে।

5) The order of stack operations on interrupt entry is:
- A. CS, IP, FLAGS
- B. FLAGS, CS, IP
- C. IP, CS, FLAGS
- D. FLAGS, IP, CS
Answer: B
Explanation (Bangla): ক্রম হলো FLAGS→CS→IP। IRET করলে বিপরীত ক্রমে পপ হয়: IP→CS→FLAGS।

6) To minimize interrupt latency, you should:
- A. Keep ISRs long and compute-heavy
- B. Use CLI for entire program
- C. Keep ISRs short and defer work
- D. Disable NMI
Answer: C
Explanation (Bangla): ছোট ISR লেটেন্সি কমায় এবং সিস্টেমকে রেসপনসিভ রাখে; বাকি কাজ মেইন লুপ/টাস্কে।

7) The 8086 checks INTR for service:
- A. Continuously during instruction execution
- B. Only at instruction boundaries when IF=1
- C. Only when OF=1
- D. Only during HLT
Answer: B
Explanation (Bangla): IF=1 হলে ইনস্ট্রাকশন বাউন্ডারিতে INTR স্যাম্পল হয়।

8) Which flag is unaffected by STI?
- A. IF
- B. TF
- C. Both IF and TF
- D. OF
Answer: B
Explanation (Bangla): STI কেবল IF সেট করে; TF অপরিবর্তিত থাকে।

9) The IVT entry contains which of the following for ISR address?
- A. Only offset (IP)
- B. Only segment (CS)
- C. Both CS and IP
- D. Physical address
Answer: C
Explanation (Bangla): ISR-এর ঠিকানা CS:IP ফরমে থাকে; প্রতিটি ভেক্টর এন্ট্রি 4 বাইট।

10) The instruction used to return from an ISR is:
- A. RET
- B. RETF
- C. IRET
- D. JMP FAR
Answer: C
Explanation (Bangla): IRET ছাড়া সঠিক কনটেক্সট (IP, CS, FLAGS) রিস্টোর হয় না।

## True/False (English statements, Bangla explanations)

1) ISRs should avoid using the stack to reduce overhead.
- Answer: False
- Explanation (Bangla): স্ট্যাক ব্যবহার করেই সেফলি রেজিস্টার সেভ/রিস্টোর করা হয়; ওভারহেড সামান্য হলেও কনসিস্টেন্সির জন্য জরুরি।

2) An ISR can re-enable interrupts with STI to allow higher-priority interrupts.
- Answer: True
- Explanation (Bangla): ক্রিটিকাল কাজ শেষে STI করলে উচ্চ প্রায়োরিটি ইন্টারাপ্ট নেস্ট করতে পারে।

3) INTO causes an interrupt only when OF=1.
- Answer: True
- Explanation (Bangla): ওভারফ্লো থাকলেই টাইপ 4 কল হয়।

4) The order of pushes on interrupt entry is IP, CS, FLAGS.
- Answer: False
- Explanation (Bangla): সঠিক ক্রম হলো FLAGS→CS→IP।

5) IRET pops IP, CS, and FLAGS.
- Answer: True
- Explanation (Bangla): IRET তিনটিই পপ করে—সম্পূর্ণ কনটেক্সট রিস্টোর হয়।
