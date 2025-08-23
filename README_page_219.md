# 8086 Interrupts — Page 219 MCQs and True/False

Note: Final set in this batch—summary-style questions mixing concepts.

## MCQs (English Qs, Bangla explanations)

1) The IVT covers which physical address range?
- A. 00000h–001FFh
- B. 00000h–003FFh
- C. 00000h–00FFFh
- D. F0000h–FFFFFh
Answer: B
Explanation (Bangla): 256×4=1024 বাইট—00000h থেকে 003FFh।

2) Which automatically happens on interrupt entry (8086)?
- A. Push FLAGS, CS, IP; clear IF/TF
- B. Only push IP
- C. Clear all flags
- D. Save only CS
Answer: A
Explanation (Bangla): FLAGS→CS→IP পুশ হয়, তারপর IF/TF ক্লিয়ার হয়।

3) Which interrupt is non-maskable?
- A. INTR
- B. NMI
- C. INT n
- D. INTO
Answer: B
Explanation (Bangla): NMI non-maskable—IF=0 হলেও ঘটে।

4) Breakpoint instruction type and opcode are:
- A. Type 3, opcode CC
- B. Type 3, opcode CD
- C. Type 1, opcode CC
- D. Type 4, opcode CE
Answer: A
Explanation (Bangla): ব্রেকপয়েন্ট INT 3—এক বাইট CC।

5) INTA cycles are used to:
- A. Fetch ISR code from ROM
- B. Obtain the interrupt vector/type from PIC for INTR
- C. Enter protected mode
- D. Clear flags
Answer: B
Explanation (Bangla): INTR-এর ক্ষেত্রে 8259A PIC INTA সাইকেলে টাইপ নম্বর দেয়।

6) The correct return from an ISR is:
- A. RET
- B. IRET
- C. RETF
- D. JMP far
Answer: B
Explanation (Bangla): IRET ছাড়া IP, CS, FLAGS আগের মানে ফেরে না।

7) Which flags are restored by IRET?
- A. Only IF
- B. IF and TF only
- C. All saved FLAGS
- D. None
Answer: C
Explanation (Bangla): IRET FLAGS পপ করে—যা সেভ হয়েছিল সব ফ্ল্যাগের মান ফেরত দেয়।

8) In a cascaded PIC with rotation enabled, just-serviced IRQ level becomes:
- A. Highest priority next
- B. Lowest priority next
- C. Unchanged
- D. Disabled
Answer: B
Explanation (Bangla): রোটেট-অন-EOI-তে সদ্য সার্ভিসড লেভেল প্রায়োরিটি টেইলে চলে যায়।

9) Which statement about software INT n is correct?
- A. Requires INTA handshake
- B. Ignores IF state
- C. Doesn’t save context
- D. Is non-maskable
Answer: B
Explanation (Bangla): INT n IF-এর উপর নির্ভর করে না; সরাসরি ভেক্টরে জাম্প করে, তবে কনটেক্সট সেভ করে।

10) A practical ISR guideline is to:
- A. Do long computations inside ISR
- B. Defer non-critical work to main loop
- C. Never use stack
- D. Use RET at the end
Answer: B
Explanation (Bangla): ছোট ও দ্রুত ISR; বাকি কাজ ডিফার করে রাখুন—সিস্টেম রেসপনসিভ থাকে।

## True/False (English statements, Bangla explanations)

1) IVT consists of 256 entries of 4 bytes each.
- Answer: True
- Explanation (Bangla): প্রতিটি এন্ট্রি IP(2B)+CS(2B)।

2) NMI uses a programmable type number.
- Answer: False
- Explanation (Bangla): NMI টাইপ 2—ফিক্সড।

3) INT 3 is two bytes long.
- Answer: False
- Explanation (Bangla): এক বাইট—CC।

4) IRET restores the FLAGS register from the stack.
- Answer: True
- Explanation (Bangla): FLAGS পপ করে আগের মানে ফিরিয়ে দেয়।

5) INTR is maskable, controlled by IF.
- Answer: True
- Explanation (Bangla): IF=1 হলে সার্ভিস হয়, IF=0 হলে ব্লক।
