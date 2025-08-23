# 8086 Interrupts — Page 213 MCQs and True/False

Note: Focus on advanced 8259A operations (OCWs), polling, rotation, special modes, and practical ISR/PIC coordination.

## MCQs (English Qs, Bangla explanations)

1) Which command word enables Poll mode and selects IRR/ISR readback in 8259A?
- A. ICW2
- B. ICW3
- C. OCW2
- D. OCW3
Answer: D
Explanation (Bangla): OCW3 দিয়ে Poll মোড (POLL), Read Register Select (RR) ও IRR/ISR সিলেক্ট করা হয়; এছাড়াও Special Mask Mode (SMM) সেট/ক্লিয়ার করা যায়।

2) The register that holds pending interrupt requests before acknowledgment is:
- A. IMR
- B. IRR
- C. ISR
- D. PR
Answer: B
Explanation (Bangla): IRR (Interrupt Request Register) পেন্ডিং IRQ গুলো ধরে রাখে; ISR (In-Service Register) বর্তমানে সার্ভিস হওয়া লেভেল নির্দেশ করে; IMR হলো মাস্ক বিট।

3) Non-specific EOI affects which level by default?
- A. All in-service levels
- B. Current highest-priority in-service
- C. Lowest-priority in-service
- D. Programmable level only
Answer: B
Explanation (Bangla): non-specific EOI ডিফল্টভাবে সর্বোচ্চ প্রায়োরিটি ইন-সার্ভিস লেভেলকে ক্লিয়ার করে। specific EOI দিলে নির্দিষ্ট লেভেল টার্গেট করা যায়।

4) Priority rotation can be configured using:
- A. OCW1
- B. OCW2
- C. OCW3
- D. ICW4 only
Answer: B
Explanation (Bangla): OCW2-র rotate অপশন দিয়ে প্রায়োরিটি বেস ঘোরানো যায়—উদাহরণ, rotate on non-specific EOI।

5) Special Mask Mode (SMM) is controlled via:
- A. ICW1
- B. ICW2
- C. OCW3
- D. OCW2
Answer: C
Explanation (Bangla): OCW3-এ SMM/ESMM বিট দিয়ে Special Mask Mode অন/অফ করা হয়; এতে মাস্কিং আচরণ আলাদা হয়।

6) In 8086/88 mode, Auto EOI is enabled via:
- A. ICW4
- B. OCW1
- C. OCW2
- D. ICW3
Answer: A
Explanation (Bangla): ICW4-এ 8086/88 মোড ও Auto EOI কনফিগার করা হয়। Auto EOI থাকলে EOI পাঠানো ছাড়াই ISR শেষ ধরা হয়।

7) Reading which register tells you which IRQ level is currently being serviced?
- A. IRR
- B. ISR
- C. IMR
- D. PR
Answer: B
Explanation (Bangla): ISR (In-Service Register) বর্তমানে কোন লেভেল সার্ভিসে আছে তা নির্দেশ করে; IRR পেন্ডিং দেখায়।

8) In Poll mode, the PIC:
- A. Drives INTR as usual
- B. Requires the CPU to issue poll commands and returns the highest-priority pending request
- C. Stops accepting any interrupts
- D. Always returns type 7
Answer: B
Explanation (Bangla): Poll মোডে CPU OCW3 Poll ইস্যু করে; PIC সর্বোচ্চ প্রায়োরিটি পেন্ডিং IRQ রিপোর্ট করে—ইন্টারাপ্ট-ড্রিভেনের বদলে পোলিং-ভিত্তিক ফ্লো।

9) Spurious interrupts in 8259A are commonly associated with which IRQ in edge-triggered mode?
- A. IR0
- B. IR3
- C. IR5
- D. IR7
Answer: D
Explanation (Bangla): IR7-এ স্পিউরিয়াস বেশি দেখা যায়—অ্যাসার্ট/ডি-অ্যাসার্ট টাইমিংয়ের কারণে ভেক্টরিং হলেও বাস্তবে বৈধ রিকোয়েস্ট নাও থাকতে পারে।

10) Special Fully Nested Mode (SFNM) is configured via:
- A. ICW1
- B. ICW2
- C. ICW3
- D. ICW4
Answer: D
Explanation (Bangla): ICW4-এ SFNM অপশন আছে—ক্যাসকেডেড PIC-এ নেস্টিং আচরণ উন্নত করতে ব্যবহৃত হয়।

11) Which statement about OCW1 is correct?
- A. It sets vector base
- B. It controls per-line masking (IMR)
- C. It sends EOIs
- D. It selects IRR/ISR readback
Answer: B
Explanation (Bangla): OCW1 হলো Interrupt Mask Register (IMR) লিখতে ব্যবহৃত—প্রতিটি IR লাইনের মাস্ক কন্ট্রোল।

12) When rotate-on-non-specific EOI is active, after servicing an interrupt, the priority:
- A. Resets to IR0 highest always
- B. Rotates so that the just-serviced level becomes lowest priority
- C. Rotates randomly
- D. Disables further interrupts
Answer: B
Explanation (Bangla): রোটেট-অন-নন-স্পেসিফিক EOI-তে সদ্য সার্ভিসড লেভেল প্রায়োরিটি শেষে চলে যায়—লোড-ব্যালান্সিং সহায়ক।

## True/False (English statements, Bangla explanations)

1) OCW3 controls Poll mode and IRR/ISR readback.
- Answer: True
- Explanation (Bangla): OCW3-য়ের POLL/RR/ISR/IRR সিলেক্ট ও SMM কন্ট্রোল থাকে।

2) Auto EOI means the CPU must still send an EOI after each ISR.
- Answer: False
- Explanation (Bangla): Auto EOI থাকলে PIC নিজেই EOI ধরে নেয়; তবে nested/priority আচরণে সীমাবদ্ধতা বিবেচ্য।

3) IRR indicates which requests are pending; ISR shows which one is being serviced.
- Answer: True
- Explanation (Bangla): IRR=Pending, ISR=In-service—এই পার্থক্য ডিবাগে গুরুত্বপূর্ণ।

4) Reading ISR clears its bits automatically.
- Answer: False
- Explanation (Bangla): রিড-ব্যাক ক্লিয়ার করে না; EOI (বা Auto EOI) ISR বিট ক্লিয়ার করে।

5) Special Mask Mode is configured via ICW2.
- Answer: False
- Explanation (Bangla): SMM OCW3 দিয়ে কনফিগার করা হয়; ICW2 ভেক্টর বেস।

6) In Poll mode the PIC does not assert INTR.
- Answer: True
- Explanation (Bangla): পোল-মোডে CPU কুয়েরির জবাবে PIC স্ট্যাটাস দেয়; INTR সাধারণত ব্যবহৃত হয় না।

7) SFNM resides in ICW4 and helps proper nesting with cascaded PICs.
- Answer: True
- Explanation (Bangla): ক্যাসকেডেড সিস্টেমে নেস্টিং/প্রায়োরিটি সঠিকভাবে হ্যান্ডেল করার জন্য SFNM কাজে লাগে।

8) OCW2 is used to send specific/non-specific EOI and to control rotation.
- Answer: True
- Explanation (Bangla): OCW2-তেই EOI ও rotate সম্পর্কিত কন্ট্রোল বিট থাকে।

9) IMR bits of 1 mean the corresponding interrupt is enabled.
- Answer: False
- Explanation (Bangla): IMR-এ 1 মানে মাস্কড (ডিসেবল); 0 মানে এনাবল।

10) Spurious interrupts never occur in level-triggered mode.
- Answer: False
- Explanation (Bangla): লেভেল-ট্রিগার্ডে কম হতে পারে, কিন্তু সম্পূর্ণ অসম্ভব নয়—ডিভাইস/ওয়্যারিং/টাইমিংয়ের উপর নির্ভর করে।
