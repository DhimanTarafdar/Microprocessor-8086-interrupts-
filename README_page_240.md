# 8259A Priority Interrupt Controller — Page 240 MCQs and True/False

Note: Wrap-up—comprehensive review questions and edge-case reasoning.

## MCQs (English Qs, Bangla explanations)

1) The correct statement about ICW2 in 8086 mode is:
- A. Any value is fine; PIC adds IRQ as a byte add
- B. Lower three bits are replaced by IRQ number; base should be multiple of 8
- C. Lower four bits are replaced by IRQ number; base should be multiple of 16
- D. ICW2 is ignored when Auto EOI is on
Answer: B
Explanation (Bangla): বেসের লো 3 বিটে IRQ বসে—তাই 8-এর গুণিতক বেস রাখা উচিত।

2) The purpose of OCW2 is to:
- A. Mask individual lines
- B. Send EOI and control rotation
- C. Select IRR/ISR readback
- D. Configure 8086 mode
Answer: B
Explanation (Bangla): OCW2—EOI ও rotate কন্ট্রোল।

3) The register pair to check pending vs in-service is:
- A. IMR vs IRR
- B. IRR vs ISR
- C. ISR vs IMR
- D. ICW1 vs ICW2
Answer: B
Explanation (Bangla): IRR=pending, ISR=in-service।

4) In poll mode, INTR line is:
- A. Asserted normally
- B. Not used; CPU issues poll and PIC reports pending level
- C. Converted to NMI
- D. Used to signal EOI
Answer: B
Explanation (Bangla): পোল-মোডে CPU কুয়েরি করলে PIC পেন্ডিং রিপোর্ট করে।

5) The right place to send EOI (without Auto EOI) is:
- A. Immediately on ISR entry
- B. After acknowledging/clearing the device and before IRET
- C. After IRET
- D. Not required
Answer: B
Explanation (Bangla): ডিভাইস পরিষ্কার করে EOI—তারপর IRET।

6) The default priority order in fully nested mode is:
- A. IR7>…>IR0
- B. IR0>IR1>…>IR7
- C. Round-robin always
- D. Programmable only
Answer: B
Explanation (Bangla): ডিফল্ট IR0 সর্বোচ্চ।

7) With Auto EOI enabled, ISRs must still:
- A. Issue OCW2 EOI
- B. Clear device-level status/handshake
- C. Disable NMI
- D. Program ICW3 each time
Answer: B
Explanation (Bangla): ডিভাইস-লেভেল ACK অপরিহার্য।

8) Misaligned ICW2 base results in:
- A. Correct mapping anyway
- B. Wrong vector mapping for some IRQs
- C. Only slower performance
- D. No effect if rotation is on
Answer: B
Explanation (Bangla): লো 3 বিট IRQ—ভুল অ্যালাইনমেন্টে ম্যাপিংও ভুল।

9) Reading IRR/ISR requires configuring:
- A. OCW2
- B. OCW3 read-register select and IRR/ISR choice
- C. ICW1
- D. ICW4
Answer: B
Explanation (Bangla): OCW3 দিয়ে রিডব্যাক সিলেক্ট করতে হয়।

10) A safe ISR pattern with PIC includes:
- A. RET
- B. POPF then RET
- C. Save regs, optional CLI/CLD, device ACK, optional STI, restore regs, IRET
- D. HLT
Answer: C
Explanation (Bangla): সেফ কনটেক্সট-হ্যান্ডলিং ও ডিভাইস-ACK সহ IRET দিয়ে রিটার্ন।

## True/False (English statements, Bangla explanations)

1) ICW2 lower three bits are replaced with IRQ number in 8086 mode.
- Answer: True
- Explanation (Bangla): বেস 8-অ্যালাইন্ড হওয়া উচিত।

2) OCW2/OCW3 roles are EOI/rotation and poll/readback respectively.
- Answer: True
- Explanation (Bangla): OCW2=EOI/rotate; OCW3=poll/RR/IRR/ISR।

3) IRR shows in-service levels.
- Answer: False
- Explanation (Bangla): IRR=pending; ISR=in-service।

4) Auto EOI also acknowledges devices.
- Answer: False
- Explanation (Bangla): শুধুই PIC-লেভেল EOI; ডিভাইস-ACK আলাদা।

5) A short CLI-guarded critical section inside ISR can be appropriate.
- Answer: True
- Explanation (Bangla): খুব ছোট অংশে CLI করে কাজ সেফলি করে নিন; পরে STI।
