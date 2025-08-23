# 8259A Priority Interrupt Controller — Page 234 MCQs and True/False

Note: OCW2/OCW3 details, EOI types, readback, and example scenarios.

## MCQs (English Qs, Bangla explanations)

1) Which OCW is used to send End Of Interrupt (EOI)?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4
Answer: B
Explanation (Bangla): OCW2—specific/non-specific EOI এবং রোটেশন কন্ট্রোল।

2) Which OCW selects IRR/ISR for readback and can enable Poll mode?
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW2
Answer: C
Explanation (Bangla): OCW3—RR/IRR/ISR সিলেক্ট ও POLL।

3) Specific EOI should be used when:
- A. Only one IRQ exists
- B. It’s necessary to clear a known in-service level explicitly
- C. Rotation is disabled
- D. Auto EOI is enabled
Answer: B
Explanation (Bangla): নির্দিষ্ট লেভেল ক্লিয়ার করার জন্য specific EOI—নেস্টেড/ক্যাসকেডেড সিস্টেমে দরকার হয়।

4) To check if an interrupt is pending without servicing it, read:
- A. ISR via OCW3 readback
- B. IRR via OCW3 readback
- C. IMR directly
- D. ICW2
Answer: B
Explanation (Bangla): IRR pending রিকোয়েস্ট দেখায়; OCW3 দিয়ে রিডব্যাক সিলেক্ট করতে হয়।

5) In poll mode, the CPU:
- A. Waits for INTR
- B. Issues a poll command and reads which IR level requests service
- C. Uses NMI only
- D. Disables all interrupts
Answer: B
Explanation (Bangla): POLL-এ CPU কুয়েরি করে; PIC সর্বোচ্চ প্রায়োরিটি পেন্ডিং IRQ রিপোর্ট করে।

6) Auto EOI:
- A. Requires explicit EOI from ISR
- B. Automatically clears in-service on acknowledge/return
- C. Disables nesting entirely
- D. Is configured in OCW2
Answer: B
Explanation (Bangla): Auto EOI থাকলে ISR থেকে EOI প্রয়োজন হয় না; তবে nesting আচরণে সীমাবদ্ধতা থাকতে পারে।

7) Reading ISR after an IRET (with proper EOI) should show:
- A. All ones
- B. The just-serviced level cleared
- C. The same bit still set
- D. Random
Answer: B
Explanation (Bangla): EOI পাঠানোর পর ISR-এ সেই লেভেল ক্লিয়ার হওয়া উচিত।

8) If IMR masks IR5, then:
- A. IR5 can still trigger NMI
- B. IR5 requests will not be serviced until unmasked
- C. IR5 becomes type 5
- D. IR5 gets highest priority
Answer: B
Explanation (Bangla): মাস্কড লাইন সার্ভিস পায় না—আনমাস্ক না করা পর্যন্ত।

9) The base vector for PIC is set in:
- A. ICW1
- B. ICW2
- C. ICW3
- D. OCW1
Answer: B
Explanation (Bangla): ICW2-তে ভেক্টর বেস।

10) The default priority order in fully nested mode is:
- A. IR7>…>IR0
- B. Round-robin
- C. IR0>IR1>…>IR7
- D. Programmable only
Answer: C
Explanation (Bangla): ডিফল্টে IR0 সর্বোচ্চ, IR7 সর্বনিম্ন।

## True/False (English statements, Bangla explanations)

1) OCW2 handles EOI/rotation; OCW3 handles Poll/IRR/ISR readback.
- Answer: True
- Explanation (Bangla): এই দুইটি OCW-র প্রধান ভূমিকা এটাই।

2) Auto EOI eliminates the need for software EOI from ISR.
- Answer: True
- Explanation (Bangla): PIC স্বয়ংক্রিয়ভাবে ইন-সার্ভিস ক্লিয়ার করে।

3) IRR indicates in-service interrupts.
- Answer: False
- Explanation (Bangla): IRR=pending, ISR=in-service।

4) IMR=1 at a bit position means that line is enabled.
- Answer: False
- Explanation (Bangla): 1 মানে মাস্কড—ডিসেবল।

5) Poll mode requires CPU to query PIC instead of waiting for INTR.
- Answer: True
- Explanation (Bangla): পোলিং-ভিত্তিক সার্ভিস ফ্লো।
