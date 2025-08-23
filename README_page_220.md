# 8086 Interrupts — Page 220 MCQs and True/False

Note: Emphasis on ISR chaining, masking examples, and common application scenarios.

## MCQs (English Qs, Bangla explanations)

1) ISR chaining means:
- A. Calling multiple ISRs sequentially from one interrupt
- B. Using multiple PICs in cascade
- C. Using RET instead of IRET
- D. Mapping many vectors to same address
Answer: A
Explanation (Bangla): কিছু সিস্টেমে একটি ISR ছোট কাজ করে আরেক ISR/হ্যান্ডলারকে কল চেইন করে—মডিউলার সার্ভিসিংয়ের জন্য।

2) If IMR masks IR2 (bit=1) on the PIC, then:
- A. IR2 requests are ignored until unmasked
- B. IR2 requests preempt all others
- C. Only NMI passes
- D. It affects software INT 2 only
Answer: A
Explanation (Bangla): IMR-এ 1 মানে সংশ্লিষ্ট লাইন মাস্কড—রিকোয়েস্ট পেন্ডিং থাকলেও সার্ভিস হবে না।

3) Specific EOI is preferred when:
- A. Only one level exists
- B. Multiple nested levels need precise clearing
- C. Auto EOI is active
- D. Rotation is disabled
Answer: B
Explanation (Bangla): স্পেসিফিক EOI নির্দিষ্ট ইন-সার্ভিস লেভেল ক্লিয়ার করে—নেস্টেড/ক্যাসকেডেড কনফিগে নির্ভুলতা দরকার হয়।

4) Non-specific EOI with rotation enabled results in:
- A. Same level staying highest
- B. Just-serviced level becoming lowest priority
- C. All levels masked
- D. NMI triggered
Answer: B
Explanation (Bangla): রোটেট-অন-EOI-তে সদ্য সার্ভিসড লেভেল টেইলে চলে যায়—ফেয়ারনেস বাড়ে।

5) A keyboard-like device that holds request until serviced is better with:
- A. Edge-triggered mode
- B. Level-triggered mode
- C. Software INT only
- D. Trap flag
Answer: B
Explanation (Bangla): লেভেল-ট্রিগার্ডে সার্ভিস না হওয়া পর্যন্ত লেভেল থাকবে—মিসড-এজ ঝুঁকি কম।

6) Type number n has vector entry at physical:
- A. 00000h + 2n
- B. 00000h + 4n
- C. 00000h + 8n
- D. 00000h + 16n
Answer: B
Explanation (Bangla): প্রতিটি এন্ট্রি 4 বাইট—অফসেট 4×n।

7) ISR that touches ES:DI for a buffer must:
- A. Ignore saving registers for speed
- B. Save/restore used regs and segment regs
- C. Use RETF
- D. Disable NMI
Answer: B
Explanation (Bangla): ব্যবহৃত রেজিস্টার ও সেগমেন্ট রেজিস্টার সেভ/রিস্টোর না করলে কলারের কনটেক্সট নষ্ট হয়।

8) For periodic tasks with minimal jitter, prefer:
- A. Long computation inside ISR
- B. Quick ISR that sets a flag for main loop
- C. Polling only
- D. Disabling all interrupts
Answer: B
Explanation (Bangla): ISR ছোট রাখলে জিটার কম; বাকি কাজ মেইন/টাস্কে।

9) The correct end of an ISR is:
- A. RET
- B. IRET
- C. RETF
- D. JMP far
Answer: B
Explanation (Bangla): IRET-ই IP, CS, FLAGS পুনঃস্থাপন করে।

10) For a shared interrupt line, device identification is typically by:
- A. Reading IVT
- B. Polling device status/ID registers
- C. Checking CS:IP
- D. Reading FLAGS
Answer: B
Explanation (Bangla): PIC কেবল লেভেল জানায়; ডিভাইস কোনটি ইন্টারাপ্ট দিল তা ডিভাইস-স্ট্যাটাস/আইডি রেজিস্টার থেকে জানা যায়।

## True/False (English statements, Bangla explanations)

1) Masking a line in IMR prevents that interrupt from being serviced.
- Answer: True
- Explanation (Bangla): IMR=1 হলে লাইন ডিসেবল থাকে।

2) Specific EOI clears all in-service levels.
- Answer: False
- Explanation (Bangla): নির্দিষ্ট একটি লেভেল ক্লিয়ার করে।

3) ISR chaining can help modularize drivers.
- Answer: True
- Explanation (Bangla): আলাদা ডিভাইস/সাবসিস্টেমের হ্যান্ডলার আলাদা রাখা যায়।

4) Using RET from an ISR is safe.
- Answer: False
- Explanation (Bangla): IRET দরকার—না হলে FLAGS ফেরত আসে না।

5) Level-triggered mode reduces risk of missed interrupts on shared lines.
- Answer: True
- Explanation (Bangla): লেভেল ধরে রাখায় এজ-মিস ইস্যু কমে।
