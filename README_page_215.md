# 8086 Interrupts — Page 215 MCQs and True/False

Note: Applied scenarios—designing simple ISRs, dealing with nested interrupts, debugging with INT 3/TF.

## MCQs (English Qs, Bangla explanations)

1) You need to debug and pause at a specific instruction at runtime. The most convenient instruction to insert is:
- A. INT 3
- B. INTO
- C. HLT
- D. NOP
Answer: A
Explanation (Bangla): INT 3 এক বাইটের (CC) হওয়ায় কোডে সহজে ইনসার্ট করে ব্রেকপয়েন্ট করা যায়।

2) To single-step through instructions for debugging, you should set:
- A. IF=1
- B. TF=1
- C. OF=1
- D. DF=1
Answer: B
Explanation (Bangla): TF=1 করলে প্রতিটি ইনস্ট্রাকশনের পরে টাইপ 1 ইন্টারাপ্ট ঘটে—সিঙ্গল-স্টেপিং।

3) An ISR that must be re-entrant should avoid:
- A. Using only local stack-based variables
- B. Modifying global state without protection
- C. Saving/restoring used registers
- D. Keeping ISR short
Answer: B
Explanation (Bangla): গ্লোবাল স্টেট প্রটেকশন ছাড়া পরিবর্তন করলে রিএন্ট্রান্সিতে ডেটা নষ্ট হতে পারে; লক/ফ্ল্যাগ/ক্রিটিকাল সেকশন দরকার।

4) For a system where high-priority events must preempt low-priority ISRs, your ISR should:
- A. Keep IF=0 throughout
- B. Execute STI after saving context and critical section
- C. End with RETF
- D. Avoid using stack
Answer: B
Explanation (Bangla): সেভিং/ক্রিটিকাল অংশ শেষে STI করলে উচ্চ প্রায়োরিটি ইন্টারাপ্ট নেস্ট করতে পারে।

5) A common minimal register save set for a simple ISR that uses AX and DX is:
- A. PUSH AX, PUSH DX; ...; POP DX, POP AX
- B. PUSHF; ...; POPF
- C. PUSH CS; PUSH IP
- D. None is needed
Answer: A
Explanation (Bangla): যেগুলো ব্যবহার/পরিবর্তন হয় সেগুলোই সেভ করুন—সাধারণভাবে AX/DX যদি ব্যবহার করেন, এগুলো PUSH/POP যথেষ্ট।

6) Using INTO for overflow detection is appropriate when:
- A. You need to branch on OF without overhead
- B. OF is irrelevant
- C. You’re servicing an external interrupt
- D. You need to clear IF
Answer: A
Explanation (Bangla): INTO কন্ডিশনাল—OF=1 হলে ইন্টারাপ্ট সার্ভিসে যায়; OF=0 হলে পরের ইন্সট্রাকশনে চলে যায়।

7) During debugging, placing INT 3 at runtime is useful because:
- A. It’s non-maskable
- B. It auto-enables TF
- C. It’s a one-byte opcode that overrides instruction alignment easily
- D. It clears IF
Answer: C
Explanation (Bangla): এক বাইট হওয়ায় কোড রিপ্লেসমেন্ট সহজ—প্যাচিং/ব্রেকপয়েন্ট সাপোর্ট করে।

8) To avoid corrupting caller flags when tinkering with condition codes inside ISR, you may use:
- A. PUSHF/POPF around flag changes
- B. STC only
- C. CMC only
- D. No special care
Answer: A
Explanation (Bangla): FLAGS সেভ/রিস্টোর করলে কলারের কন্ডিশন কোড নষ্ট হয় না।

9) The correct return from an ISR is always:
- A. RET
- B. RETF
- C. IRET
- D. JMP far
Answer: C
Explanation (Bangla): IRET-ই কনটেক্সট-সেফ রিটার্ন।

10) If the ISR uses DS to access a data segment, a safe pattern is:
- A. Leave DS as is
- B. PUSH DS; MOV DS, <seg>; ...; POP DS; IRET
- C. PUSHF; POPF
- D. CLC
Answer: B
Explanation (Bangla): সেগমেন্ট রেজিস্টার পরিবর্তন করলে সেভ/রিস্টোর করা আবশ্যক।

## True/False (English statements, Bangla explanations)

1) INT 3 can be dynamically inserted into code to create a breakpoint.
- Answer: True
- Explanation (Bangla): এক বাইটের কারণে রানটাইম প্যাচ করাও সহজ।

2) Setting TF=1 causes a Type 1 interrupt after each executed instruction.
- Answer: True
- Explanation (Bangla): এটাই সিঙ্গল-স্টেপিং মেকানিজম।

3) Using RET from ISR is acceptable if you saved no registers.
- Answer: False
- Explanation (Bangla): IRET ছাড়া FLAGS পুনঃস্থাপন হয় না—সঠিক রিটার্ন নয়।

4) INTO will trigger interrupt even when OF=0.
- Answer: False
- Explanation (Bangla): OF=1 না হলে INTO কোনো ইন্টারাপ্ট ঘটায় না।

5) Modifying DS/ES inside ISR requires restoring them before IRET.
- Answer: True
- Explanation (Bangla): নইলে কলার কনটেক্সট ভেঙে যায়।
