# 8086 Interrupts — Page 208 MCQs and True/False

Note: Built to match typical “Interrupts & their applications” continuation. If your page has specific highlights, share them to refine these.

## MCQs (English Qs, Bangla explanations)

1) What is the first action 8086 takes when it accepts an interrupt?
- A. Push IP, then CS
- B. Clear IF and TF
- C. Push FLAGS
- D. Fetch vector from memory
Answer: C
Explanation (Bangla): ইন্টারাপ্ট গ্রহণের সময় 8086 প্রথমে FLAGS স্ট্যাকে পুশ করে, তারপর CS ও IP পুশ করে। এরপর IF ও TF ক্লিয়ার হয় এবং ভেক্টর ফেচ করা হয়।

2) After pushing context, which flags does 8086 clear automatically on interrupt entry?
- A. CF and OF
- B. IF and TF
- C. ZF and SF
- D. DF and AF
Answer: B
Explanation (Bangla): ইন্টারাপ্ট এন্ট্রিতে IF ও TF ক্লিয়ার হয়, যাতে ISR চলাকালীন নেস্টেড ইন্টারাপ্ট/সিঙ্গল স্টেপিং না ঘটে (যদি প্রোগ্রামার ইচ্ছে করে STI না করে)।

3) The interrupt response vector is obtained from the Interrupt Vector Table using:
- A. Physical address n×2
- B. Physical address n×4
- C. Logical address n×8
- D. Physical address n×16
Answer: B
Explanation (Bangla): টাইপ নম্বর n এর জন্য এন্ট্রি অফসেট = 4×n। প্রতিটি এন্ট্রি 4 বাইট (IP 2 + CS 2)।

4) Which statement about INTR handshake is correct?
- A. INTR is edge-triggered and requires one INTA cycle
- B. INTR is level-triggered and 8086 issues two INTA pulses
- C. INTR is non-maskable and polled every cycle
- D. INTR is asserted by CPU to request service
Answer: B
Explanation (Bangla): INTR লেভেল-ট্রিগার্ড; 8086 ইন্টারাপ্ট গ্রহণ করলে দুটো INTA (interrupt acknowledge) সাইকেল জেনারেট করে, বাহ্যিক ডিভাইস/পিআইসি ভেক্টর প্রদান করে।

5) NMI on 8086 is typically:
- A. Level-triggered and maskable
- B. Edge-triggered and non-maskable
- C. Edge-triggered and maskable
- D. Level-triggered and non-maskable
Answer: B
Explanation (Bangla): NMI সাধারণত রাইজিং-এজ ট্রিগার্ড এবং non-maskable—IF ফ্ল্যাগের উপর নির্ভর করে না।

6) Which instruction must terminate an ISR in 8086?
- A. RET
- B. RETF
- C. IRET
- D. INTO
Answer: C
Explanation (Bangla): IRET স্ট্যাক থেকে IP, CS, FLAGS পপ করে আগের কনটেক্সটে ফেরত যায়। ISR সবসময় IRET দিয়ে শেষ করা উচিত।

7) A well-designed ISR should usually begin with:
- A. STI and POP AX
- B. PUSH registers it will modify
- C. HLT instruction
- D. JMP to main
Answer: B
Explanation (Bangla): ISR যে রেজিস্টারগুলো পরিবর্তন করবে সেগুলো PUSH করে সংরক্ষণ করা ভালো (AX, BX, CX, DX, SI, DI, BP, ES/DS প্রয়োজনে)। শেষে POP করে আগের মান ফিরিয়ে দেয়।

8) To avoid re-entrancy issues in a non-reentrant ISR, you should:
- A. Execute CLI early, then STI near the end
- B. Execute STI early
- C. Avoid saving registers
- D. Use RET instead of IRET
Answer: A
Explanation (Bangla): নন-রিএন্ট্রান্ট ISR এ শুরুতে CLI করে নেস্টিং বন্ধ রাখা হয়, কাজের শেষ দিকে প্রয়োজনে STI করা হয়।

9) Interrupt latency primarily depends on:
- A. Clock frequency only
- B. Length of current instruction and masking state
- C. Size of IVT
- D. Number of general-purpose registers
Answer: B
Explanation (Bangla): ইন্টারাপ্ট পরবর্তী ইনস্ট্রাকশনের বাউন্ডারিতে চেক হয়; দীর্ঘ ইনস্ট্রাকশন/REP লুপ ও IF=0 হলে ল্যাটেন্সি বাড়ে।

10) On 8086, software interrupt INT n will:
- A. Push CS, IP, FLAGS and jump via IVT
- B. Only push IP and branch
- C. Jump without saving context
- D. Only clear IF
Answer: A
Explanation (Bangla): INT n হার্ডওয়্যার ইন্টারাপ্টের মতই ফ্লো ফলো করে—FLAGS→CS→IP পুশ করে তারপর IVT-র ভেক্টরের মাধ্যমে ISR-এ ট্রান্সফার।

11) Which pair correctly matches interrupt type and purpose?
- A. Type 0 — Breakpoint
- B. Type 1 — Single-step (Trap)
- C. Type 2 — Divide error
- D. Type 3 — Overflow
Answer: B
Explanation (Bangla): টাইপ 1 হলো ট্র্যাপ/সিঙ্গল-স্টেপ ইন্টারাপ্ট (TF=1)। টাইপ 0 = Divide error, টাইপ 3 = Breakpoint, টাইপ 4 = Overflow (INTO)।

12) During interrupt entry, the current code segment and instruction pointer are saved in this order:
- A. IP then CS
- B. CS then IP
- C. Neither saved automatically
- D. IP only
Answer: A
Explanation (Bangla): স্ট্যাকে পুশের ক্রম FLAGS → CS → IP। ফলে পরে IRET করলে IP, CS, FLAGS পপ হয়ে আগের ঠিকানায় ফেরা যায়।

## True/False (English statements, Bangla explanations)

1) Interrupts can occur in the middle of an instruction on 8086.
- Answer: False
- Explanation (Bangla): সাধারণত ইন্টারাপ্ট কেবল ইনস্ট্রাকশন বাউন্ডারিতে গ্রহণ করা হয়; চলমান ইনস্ট্রাকশন শেষ না হলে ইন্টারাপ্ট ডিফার হয়।

2) INTR is maskable and sampled when IF=1.
- Answer: True
- Explanation (Bangla): IF=1 হলে CPU INTR গ্রহণ করতে পারে; IF=0 হলে ব্লক থাকে।

3) NMI can be disabled by CLI.
- Answer: False
- Explanation (Bangla): NMI non-maskable; CLI কেবল মাস্কেবল ইন্টারাপ্টে প্রভাব ফেলে।

4) An ISR must always restore any registers it modifies before IRET.
- Answer: True
- Explanation (Bangla): রেজিস্টার সেভ/রিস্টোর না করলে কলার কনটেক্সট নষ্ট হয়ে যায়।

5) IRET restores IF and TF from the saved FLAGS.
- Answer: True
- Explanation (Bangla): FLAGS পপ হওয়ায় IF/TF সহ পুরনো ফ্ল্যাগ মান ফিরে আসে।

6) The IVT occupies 1024 bytes from 00000h to 003FFh.
- Answer: True
- Explanation (Bangla): 256 এন্ট্রি × 4 বাইট = 1024 বাইট।

7) Software interrupts ignore the state of IF.
- Answer: True
- Explanation (Bangla): INT n ইন্সট্রাকশন IF-এর উপর নির্ভর করে না; সরাসরি সফটওয়্যার-ট্রিগার্ড ইন্টারাপ্ট ঘটায়।

8) INTA cycles are generated for both INTR and NMI.
- Answer: False
- Explanation (Bangla): INTA কেবল INTR-এর জন্য; NMI ভেক্টর পূর্বনির্ধারিত (টাইপ 2)।

9) An ISR can call other subroutines and use the stack.
- Answer: True
- Explanation (Bangla): পারে, তবে স্ট্যাক গভীরতা/রিএন্ট্রান্সি মাথায় রাখতে হয় এবং শেষে IRET অপরিহার্য।

10) The INTO instruction always triggers an interrupt irrespective of OF.
- Answer: False
- Explanation (Bangla): INTO কেবল OF=1 হলে টাইপ 4 ইন্টারাপ্ট কল করে।
