# 8086 Interrupts — Page 218 MCQs and True/False

Note: Edge cases—spurious interrupts, level vs edge triggering, and PIC readback.

## MCQs (English Qs, Bangla explanations)

1) In edge-triggered mode, a spurious interrupt on IR7 typically results in:
- A. INTA with valid vector then ISR finds no real source
- B. No vector given at all
- C. CPU reset
- D. NMI
Answer: A
Explanation (Bangla): টাইমিং ইস্যুতে IR7 অ্যাসার্ট/ডি-অ্যাসার্টের মাঝখানে INTA-তে ভেক্টর পাওয়া যেতে পারে, কিন্তু আসলে কোনো বৈধ pending না-ও থাকতে পারে—এটাই স্পিউরিয়াস।

2) To check whether an IRQ is pending or in service, read respectively:
- A. IMR and ISR
- B. IRR and ISR
- C. ISR and IRR
- D. IMR and IRR
Answer: B
Explanation (Bangla): IRR pending রিকোয়েস্ট দেখায়; ISR বর্তমানে সার্ভিসিং লেভেল দেখায়।

3) To read IRR/ISR using 8259A, you must configure via:
- A. ICW2
- B. OCW1
- C. OCW3
- D. ICW4
Answer: C
Explanation (Bangla): OCW3-এর RR বিট দিয়ে IRR/ISR সিলেক্ট করে রিডব্যাক নেওয়া হয়।

4) Level-triggered mode is preferred when:
- A. Multiple devices share a line and must hold request until serviced
- B. De-bouncing is not needed
- C. You need minimum latency
- D. You use only software interrupts
Answer: A
Explanation (Bangla): লেভেল-ট্রিগার্ডে ডিভাইস সার্ভিস না হওয়া পর্যন্ত লেভেল ধরে রাখতে পারে—শেয়ার্ড লাইনে নির্ভরযোগ্যতা বাড়ে।

5) In a cascaded PIC system, the slave identity is communicated via:
- A. ICW1
- B. ICW2
- C. ICW3
- D. OCW2
Answer: C
Explanation (Bangla): ICW3-এ মাস্টার/স্লেভ ম্যাপিং—মাস্টারে কোন IR লাইনে স্লেভ, আর স্লেভ আইডি/লাইন।

6) If an ISR needs to determine which device on a shared line triggered the interrupt, it should:
- A. Send EOI first
- B. Poll device-specific status registers after acknowledging the PIC
- C. Clear IF permanently
- D. Use INT 3
Answer: B
Explanation (Bangla): শেয়ার্ড লাইনে ডিভাইস-স্টেটাস/আইডি রেজিস্টার পোল করে উৎস নির্ধারণ করা হয়—PIC কেবল লাইন-লেভেল নির্দেশ করে।

7) Which combination is correct for software-triggered overflow handling?
- A. INTO with OF=1 → Type 4 ISR
- B. INT 3 with OF=1 → Type 4 ISR
- C. INT 4 always → Type 3 ISR
- D. NMI with OF=1
Answer: A
Explanation (Bangla): INTO কেবল OF=1 হলে টাইপ 4 কল করে; নয়তো নো-অপের মতো।

8) PIC priority rotation is useful to:
- A. Always favor the same device
- B. Distribute service fairly among multiple levels
- C. Disable interrupts
- D. Enable NMI
Answer: B
Explanation (Bangla): রোটেশন একই লেভেলে লোড-ব্যালান্সিং সহায়তা করে—যখন বারবার একটি ডিভাইস ব্যস্ত।

9) In edge-triggered systems, losing the edge means:
- A. The request persists until serviced
- B. The request may be missed if not latched
- C. NMI triggers instead
- D. IF clears automatically
Answer: B
Explanation (Bangla): এজ-ট্রিগার্ডে ল্যাচ না করলে হারানো এজ মিসড ইন্টারাপ্টে পরিণত হতে পারে।

10) Reading ISR right after IRET should show:
- A. The same in-service bit still set
- B. Clear for the just-serviced level (if EOI sent)
- C. All bits set
- D. Random
Answer: B
Explanation (Bangla): EOI দেওয়ার পরে ISR-এ সেই লেভেল ক্লিয়ার হয়ে থাকা উচিত; না হলে EOI মিস হয়েছে।

## True/False (English statements, Bangla explanations)

1) OCW3 is required to read IRR/ISR properly.
- Answer: True
- Explanation (Bangla): OCW3-য়ের RR/ISR/IRR সিলেক্ট সঠিক রিডব্যাকের জন্য দরকার।

2) Level-triggered mode guarantees zero spurious interrupts.
- Answer: False
- Explanation (Bangla): কমায় বটে, গ্যারান্টি নয়—ডিভাইস/ওয়্যারিং/টাইমিং নির্ভর।

3) Losing an edge in edge-triggered mode can miss an interrupt if not latched.
- Answer: True
- Explanation (Bangla): এটাই এজ-ট্রিগার্ডের ঝুঁকি।

4) Priority rotation helps fairness among interrupt sources.
- Answer: True
- Explanation (Bangla): সার্ভিস ন্যায্য বণ্টনে সহায়ক।

5) Type 4 is overflow; INTO branches to it only when OF=1.
- Answer: True
- Explanation (Bangla): শর্তসাপেক্ষ সফটওয়্যার ইন্টারাপ্ট।
