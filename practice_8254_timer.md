# 8254 Programmable Interval Timer — High-Yield MCQs + True/False

## MCQs (English Qs; Bangla explanations)

1) How many independent counters are inside the 8254?
- A. 1
- B. 2
- C. 3
- D. 4
Answer: C
Explanation (Bangla): 8254-এ 3টি স্বতন্ত্র 16-বিট ডাউন-কাউন্টার আছে (Counter 0, 1, 2)।

2) Each 8254 counter is primarily a:
- A. 8-bit up counter
- B. 16-bit down counter
- C. 12-bit ring counter
- D. 32-bit up counter
Answer: B
Explanation (Bangla): বেসিক কোর 16-বিট ডাউন-কাউন্টার; বাইনারি বা BCD মোডে কাজ করতে পারে।

3) Which selection bits (SC1:SC0) in the control word choose Counter 2?
- A. 00
- B. 01
- C. 10
- D. 11
Answer: C
Explanation (Bangla): SC1:SC0 = 00→Ctr0, 01→Ctr1, 10→Ctr2, 11→(8254) Read-Back।

4) RW1:RW0 = 11 in the control word means:
- A. LSB only
- B. MSB only
- C. LSB followed by MSB
- D. Counter latch
Answer: C
Explanation (Bangla): 11 মানে দু-ধাপে ডাটা—আগে LSB, পরে MSB লিখতে/পড়তে হবে।

5) In 8254 Mode 0 (Interrupt on Terminal Count), OUT remains:
- A. Low until terminal count then goes high
- B. High until terminal count then goes low
- C. Toggles every clock
- D. Stays high always
Answer: A
Explanation (Bangla): Mode 0-তে OUT শুরুতে Low; টার্মিনাল কাউন্টে High হয়—ইন্টারাপ্ট ট্রিগার করতে সুবিধা।

6) In Mode 1 (Hardware retriggerable one-shot), the one-shot is triggered by:
- A. Falling edge on CLK
- B. Rising edge on GATE
- C. Writing control word
- D. OUT transition
Answer: B
Explanation (Bangla): Gate-এর rising-edge ট্রিগার; active pulse চলাকালীন নতুন rising-edge এ retrigger হয়।

7) In Mode 2 (Rate generator), OUT stays high and becomes low for:
- A. Half the period
- B. One clock at terminal count
- C. A random duration
- D. Always low
Answer: B
Explanation (Bangla): Mode 2-তে OUT প্রায় সবসময় High; টার্মিনাল কাউন্টে 1-CLK Low pulse দেয়।

8) In Mode 3 (Square wave), for an even initial count N the duty cycle is approximately:
- A. 25%
- B. 33%
- C. 50%
- D. 75%
Answer: C
Explanation (Bangla): Even count হলে High ও Low সমান—প্রায় 50% duty-cycle। Odd হলে High এক ক্লক বেশি।

9) The BCD bit (D0) in the control word set to 1 selects:
- A. Gray code counting
- B. 4-decade BCD counting (0–9999)
- C. Binary counting only
- D. Two’s complement counting
Answer: B
Explanation (Bangla): D0=1 দিলে 4-decade BCD কাউন্ট (0–9999); D0=0 হলে 16-bit বাইনারি।

10) Writing an initial count of 0000h in binary mode results in:
- A. Count disabled
- B. 0000h (no counting)
- C. 0001h
- D. 10000h ticks (i.e., 65536)
Answer: D
Explanation (Bangla): শূন্য মানে 2^16; তাই 65536 ক্লকে টার্মিনাল কাউন্ট।

11) Which statement about the 8254 Read-Back command is correct?
- A. It exists in 8253 as well
- B. It can latch status and/or count of multiple counters
- C. It resets all counters to zero
- D. It changes the clock source
Answer: B
Explanation (Bangla): Read-Back 8254-এর বিশেষ ফিচার—একাধিক কাউন্টারের status/count একসাথে latch করা যায়।

12) GATE input in Mode 2 primarily:
- A. Forces OUT low when GATE=0
- B. Pauses counting when GATE=0, resumes when GATE=1
- C. Has no effect
- D. Inverts the clock
Answer: B
Explanation (Bangla): Mode 2-তে GATE=0 হলে কাউন্ট থামে; GATE=1 হলে পূর্বের কাউন্ট থেকে চলতে থাকে।

13) The OUT pin goes low immediately when control word is written in any mode.
- A. True for all modes
- B. True only for Mode 0
- C. False
- D. True only for Mode 5
Answer: C
Explanation (Bangla): OUT আচরণ mode-নির্ভর; control word লিখলেই OUT সাথে সাথে low হবে—এটা সাধারণ নিয়ম নয়।

14) For coherent reading while counter is running, you should:
- A. Read MSB only
- B. Read LSB only
- C. Use counter latch/read-back before reading
- D. Stop the clock first
Answer: C
Explanation (Bangla): Latch/read-back দিয়ে অস্থায়ীভাবে মান ধরে নিয়ে পড়লে গ্লিচ-মুক্ত ডাটা পাওয়া যায়।

15) After writing LSB then MSB (RW=11), the new count loads into the counting element:
- A. Immediately after LSB
- B. Immediately after MSB
- C. On the next rising edge of CLK after MSB write
- D. Only after GATE toggles
Answer: C
Explanation (Bangla): দু-পর্বে লেখা শেষের পরবর্তী CLK-এ নতুন মান active হয়—টাইমিং বাগ এড়াতে এটি জানা জরুরি।

## True/False (English; Bangla explanations)

1) 8254 counters can operate in either binary or BCD counting modes.
- Answer: True
- Explanation (Bangla): Control word-এর D0 দিয়ে বাইনারি/BCD সিলেক্ট করা হয়।

2) In Mode 3, for odd initial counts, the high portion of OUT is one clock longer than the low.
- Answer: True
- Explanation (Bangla): Odd count হলে perfect 50% সম্ভব নয়—High এক ক্লক বেশি থাকে।

3) In Mode 2, OUT stays low for half of the period by design.
- Answer: False
- Explanation (Bangla): Mode 2-তে OUT কেবল 1-CLK সময় Low হয়; বাকি সময়ে High।

4) The 8253 also supports the Read-Back command.
- Answer: False
- Explanation (Bangla): Read-Back 8254-এর সুবিধা; 8253-এ নেই।

5) If you write only LSB but configured RW=11, subsequent reads will still be valid.
- Answer: False
- Explanation (Bangla): RW=11 হলে LSB ও MSB দুটোই সঠিক ক্রমে লিখতে/পড়তে হবে; নইলে ডাটা অসঙ্গত।

6) Counters decrement on the rising edge of CLK.
- Answer: True
- Explanation (Bangla): সাধারণত রাইজিং-এজে কাউন্ট ডিক্রিমেন্ট হয় (ডেটাশিট টাইমিং)।

7) In Mode 1, a new rising edge on GATE during the pulse retriggers the one-shot.
- Answer: True
- Explanation (Bangla): Retriggerable—নতুন edge এ pulse দীর্ঘায়িত হয়।

8) An initial count of 0 selects 2^16 counts in binary mode.
- Answer: True
- Explanation (Bangla): 0 মানে 65536—প্রচলিত PIT আচরণ।

9) GATE low forces OUT low in all modes.
- Answer: False
- Explanation (Bangla): Gate-এর প্রভাব mode-ভেদে; সব মোডে OUT জোর করে Low নয়।

10) To avoid reading a changing count value, use the latch or Read-Back before reading.
- Answer: True
- Explanation (Bangla): Latch/read-back দিলে স্টেবল স্ন্যাপশট পাওয়া যায়—রানিং কাউন্টারেও সঠিক রিডিং সম্ভব।
