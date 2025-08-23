# 8086 Interrupts — Page 207 (Chapter Start) Questions

Note: The exact page-207 text could not be extracted from the PDFs in this folder (one is only 26 pages; the others seem scanned/no text layer). These questions cover the typical concepts introduced at the start of an 8086 Interrupts chapter. If the actual page differs, tell me the book name and a snapshot of page 207 and I’ll align precisely.

## MCQs (English questions, Bengali explanations)

1) In 8086, how many possible interrupt types exist?
- A. 8
- B. 16
- C. 128
- D. 256
Answer: D
Explanation (Bangla): 8086-এ মোট 256 টি ইন্টারাপ্ট টাইপ (Type 0…255) আছে। প্রতিটি টাইপের জন্য Interrupt Vector Table (IVT)-এ একটি 4-byte এন্ট্রি থাকে। তাই মোট 256 টি ইন্টারাপ্ট ভেক্টর ব্যবহার করা যায়।

2) Which 8086 pin is the non-maskable interrupt input?
- A. INTR
- B. NMI
- C. RESET
- D. TEST
Answer: B
Explanation (Bangla): NMI (Non-Maskable Interrupt) এমন একটি ইন্টারাপ্ট যেটি IF ফ্ল্যাগ দ্বারা মাস্ক করা যায় না। সাধারণত রাইজিং-এজ ট্রিগার্ড এবং উচ্চ প্রায়োরিটি পায়।

3) The INTR input on 8086 is:
- A. Edge-triggered and non-maskable
- B. Level-triggered and maskable
- C. Edge-triggered and maskable
- D. Level-triggered and non-maskable
Answer: B
Explanation (Bangla): INTR হলো লেভেল-ট্রিগার্ড ও মাস্কেবল ইন্টারাপ্ট। IF ফ্ল্যাগ 1 হলে CPU INTR গ্রহণ করে, আর IF=0 হলে ব্লক করে।

4) Which instruction enables maskable interrupts in 8086?
- A. CLI
- B. STI
- C. IRET
- D. INTO
Answer: B
Explanation (Bangla): STI ইন্সট্রাকশন IF (Interrupt Flag) সেট করে, ফলে মাস্কেবল ইন্টারাপ্ট (INTR/INT n) গ্রহণযোগ্য হয়। CLI বিপরীত কাজ করে—IF ক্লিয়ার করে।

5) Which instruction returns from an Interrupt Service Routine (ISR)?
- A. RET
- B. RETF
- C. IRET
- D. JMP FAR
Answer: C
Explanation (Bangla): IRET স্ট্যাক থেকে IP, CS, এবং FLAGS পপ করে পূর্বাবস্থায় ফেরত যায়। সাধারণ RET সাবরুটিন কলের জন্য, IRET ইন্টারাপ্ট রিটার্নের জন্য।

6) The Interrupt Vector Table (IVT) in 8086 starts at physical address:
- A. 00000h
- B. 10000h
- C. F0000h
- D. 0FFFF0h
Answer: A
Explanation (Bangla): IVT মেমরির একদম শুরুতে থাকে—ফিজিক্যাল ঠিকানা 00000h থেকে। প্রতিটি টাইপের জন্য 4 বাইট করে এন্ট্রি থাকে (IP 2 বাইট + CS 2 বাইট)।

7) Size of each interrupt vector entry in IVT is:
- A. 2 bytes
- B. 4 bytes
- C. 6 bytes
- D. 8 bytes
Answer: B
Explanation (Bangla): প্রত্যেক ভেক্টর এন্ট্রি 4 বাইট—প্রথম 2 বাইট ISR-এর IP, পরের 2 বাইট ISR-এর CS। ফলে 256×4 = 1024 বাইটে পুরো টেবিল।

8) The software interrupt instruction in 8086 is:
- A. INT n
- B. INTR
- C. NMI
- D. IRET
Answer: A
Explanation (Bangla): INT n দিয়ে সফটওয়্যার ইন্টারাপ্ট ট্রিগার করা হয়। CPU ফ্ল্যাগস, CS, IP পুশ করে IVT থেকে নির্ধারিত টাইপের ISR-এ জাম্প করে।

9) On accepting an interrupt, 8086 automatically pushes to stack (in order):
- A. IP, CS, FLAGS
- B. FLAGS, CS, IP
- C. CS, IP, FLAGS
- D. FLAGS, IP, CS
Answer: B
Explanation (Bangla): 8086 প্রথমে FLAGS পুশ করে, তারপর CS এবং IP। IRET করলে বিপরীত ক্রমে IP, CS, FLAGS পপ হয়—ফলে ঠিক আগের কনটেক্সটে ফেরা যায়।

10) Which flag controls maskable interrupts?
- A. TF
- B. IF
- C. OF
- D. DF
Answer: B
Explanation (Bangla): IF (Interrupt Flag) সেট থাকলে মাস্কেবল ইন্টারাপ্ট গ্রহণ করা হয়। CLI দিয়ে IF=0 করলে মাস্কেবল ইন্টারাপ্টগুলো ব্লক হয়ে যায়।

11) The instruction that clears the Interrupt Flag is:
- A. STI
- B. CLI
- C. CLC
- D. CMC
Answer: B
Explanation (Bangla): CLI IF ফ্ল্যাগ ক্লিয়ার করে, ফলে INTR/INT n টাইপের ইন্টারাপ্ট CPU গ্রহণ করবে না। STI করলে আবার IF সেট হয়।

12) The overflow-check interrupt is invoked by which instruction if OF=1?
- A. INT 3
- B. INTO
- C. BOUND
- D. NMI
Answer: B
Explanation (Bangla): INTO (Interrupt on Overflow) কেবল তখনই ট্রিগার হয় যখন OF=1। এটি টাইপ 4 ইন্টারাপ্ট সার্ভিস রুটিনে নিয়ন্ত্রণ দেয়।

13) Breakpoint interrupt in 8086 is of type:
- A. 0
- B. 1
- C. 3
- D. 4
Answer: C
Explanation (Bangla): ব্রেকপয়েন্ট ইন্টারাপ্ট INT 3 (টাইপ 3)। এর বিশেষ এক-বাইট অপকোড (CCh) থাকার কারণে ডিবাগিংয়ে সুবিধা হয়।

14) Non-maskable interrupt (NMI) uses which type number?
- A. 0
- B. 2
- C. 3
- D. 4
Answer: B
Explanation (Bangla): NMI-এর টাইপ নম্বর 2। এর ভেক্টর IVT-তে 4×2=0008h অফসেটে সংরক্ষিত থাকে (IP, CS)।

15) Divide error interrupt in 8086 corresponds to type:
- A. 0
- B. 1
- C. 2
- D. 4
Answer: A
Explanation (Bangla): Divide-by-zero বা ডিভাইড এরর টাইপ 0 ইন্টারাপ্ট। একে CPU নিজে ট্রিগার করে যখন ভাগফল অনুমোদিত সীমা ছাড়ায় বা ভাগকরী শূন্য হয়।

16) Upon an interrupt, which flags are cleared by hardware before transferring control?
- A. CF only
- B. IF and TF
- C. OF and DF
- D. ZF and SF
Answer: B
Explanation (Bangla): ইন্টারাপ্ট গ্রহণের সময় 8086 IF ও TF ফ্ল্যাগ ক্লিয়ার করে। এতে নেস্টেড ইন্টারাপ্ট/সিঙ্গল স্টেপিং অটোমেটিকভাবে বন্ধ থাকে, ISR নিরাপদে চলতে পারে।

17) The total size of the 8086 IVT is:
- A. 256 bytes
- B. 512 bytes
- C. 1024 bytes
- D. 4096 bytes
Answer: C
Explanation (Bangla): 256 টাইপ × 4 বাইট = 1024 বাইট। তাই 00000h–003FFh পরিসর জুড়ে IVT থাকে।

18) The vector entry for interrupt type n is located at physical address:
- A. 00000h + n
- B. 00000h + 2n
- C. 00000h + 4n
- D. 00000h + 16n
Answer: C
Explanation (Bangla): প্রতিটি টাইপের এন্ট্রি 4 বাইট, তাই অফসেট 4×n। সেখানে 2 বাইট IP এবং 2 বাইট CS সংরক্ষিত থাকে।

19) Which statement about INT 3 is correct?
- A. Same as INT n with 2-byte opcode
- B. Has a special 1-byte opcode (CC)
- C. Non-maskable
- D. Clears OF only
Answer: B
Explanation (Bangla): INT 3-এর বিশেষ এক-বাইট অপকোড (CC) আছে—ডিবাগ ব্রেকপয়েন্টে এটি সুবিধাজনক। সাধারণ INT n সাধারণত দুই-বাইট (CD imm8)।

20) Which of the following is TRUE for INTO?
- A. Always triggers an interrupt
- B. Triggers only if OF=1
- C. Clears CF flag
- D. Non-maskable by nature
Answer: B
Explanation (Bangla): INTO কেবল OF=1 হলে টাইপ 4 ইন্টারাপ্ট ডাকে। OF=0 হলে INTO পরবর্তী ইন্সট্রাকশনে চলে যায়—কোনো ইন্টারাপ্ট হয় না।

## True/False (English statements, Bengali explanations)

1) NMI can be disabled by clearing IF.
- Answer: False
- Explanation (Bangla): NMI হলো non-maskable; IF ফ্ল্যাগের প্রভাব শুধুমাত্র মাস্কেবল ইন্টারাপ্টের ওপর পড়ে, NMI তে নয়।

2) INTR is a maskable interrupt input.
- Answer: True
- Explanation (Bangla): INTR IF=1 হলে গ্রহণ করা হয় এবং IF=0 হলে ব্লক হয়—এজন্য একে মাস্কেবল বলা হয়।

3) INT 3 uses a single-byte opcode.
- Answer: True
- Explanation (Bangla): INT 3-এর অপকোড CCh, এক বাইট। ডিবাগিংয়ের জন্য কোডে সহজে ইনসার্ট করা যায়।

4) IRET pops only IP and CS from the stack.
- Answer: False
- Explanation (Bangla): IRET তিনটি আইটেম পপ করে—IP, CS এবং FLAGS। এতে আগের কনটেক্সট সম্পূর্ণ পুনঃস্থাপন হয়।

5) On interrupt entry, 8086 pushes FLAGS, CS, and IP onto the stack.
- Answer: True
- Explanation (Bangla): এন্ট্রির ক্রম FLAGS→CS→IP। রিটার্নে IRET IP→CS→FLAGS পপ করে।

6) INTO generates an interrupt only when OF=1.
- Answer: True
- Explanation (Bangla): OF সেট থাকলে তবেই টাইপ 4 সার্ভিসে জাম্প হয়; নতুবা কোনো ইন্টারাপ্ট হয় না।

7) The IVT resides from physical address 00000h to 003FFh.
- Answer: True
- Explanation (Bangla): 1024 বাইটের এই এলাকা 256 ভেক্টর এন্ট্রির জন্য—প্রতি এন্ট্রি 4 বাইট।

8) The size of one IVT entry is 6 bytes.
- Answer: False
- Explanation (Bangla): প্রতিটি এন্ট্রি 4 বাইট—2 বাইট IP এবং 2 বাইট CS। 6 বাইট নয়।

9) STI clears the Trap Flag.
- Answer: False
- Explanation (Bangla): STI শুধুমাত্র IF সেট করে। TF আলাদাভাবে নিয়ন্ত্রণ করতে হয়; STI TF-এ প্রভাব ফেলে না।

10) After servicing an interrupt, IF and TF are automatically restored by IRET.
- Answer: True
- Explanation (Bangla): IRET FLAGS পপ করে, ফলে IF/TF সহ সব ফ্ল্যাগ আগের মানে ফিরে যায়।

11) NMI is typically edge-triggered on 8086.
- Answer: True
- Explanation (Bangla): NMI সাধারণত রাইজিং-এজ ট্রিগার্ড; হঠাৎ-ঘটিত গুরুতর ইভেন্ট (যেমন পাওয়ার ফেইল) ধরতে সুবিধা হয়।

12) The Trap Flag enables single-step interrupt (Type 1).
- Answer: True
- Explanation (Bangla): TF=1 হলে প্রতিটি ইন্সট্রাকশনের পর টাইপ 1 ইন্টারাপ্ট ঘটে—ডিবাগিংয়ের জন্য।

13) The vector type for NMI is 2.
- Answer: True
- Explanation (Bangla): টাইপ 2—এন্ট্রি থাকে IVT অফসেট 0008h-এ (4×2)।

14) All 256 interrupt vectors are predefined by Intel and cannot be used by users.
- Answer: False
- Explanation (Bangla): কেবল কিছুকটি টাইপ সংরক্ষিত/ডিফাইন্ড; বাকি টাইপগুলো ইউজার/সিস্টেম-ডেজাইনার ব্যবহার করতে পারেন।

15) INTR is edge-triggered by default.
- Answer: False
- Explanation (Bangla): INTR হলো লেভেল-ট্রিগার্ড; সিগন্যাল লেভেল সঠিক থাকলে CPU এটি স্যাম্পল করে গ্রহণ করে।

---

If you share a snapshot of the exact page 207 or confirm the book (Rafiquzzaman vs. V. Hall), I’ll align every question exactly to that page’s content and expand to the next pages on request.
