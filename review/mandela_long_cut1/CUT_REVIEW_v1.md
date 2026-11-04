# Mandela LONG: CUT_REVIEW v1 (4 Nov 2026, review copy 720p)

Title (owner-confirmed): Mandela: 27 Years In Prison, Then One Long Walk Out. Slot: Sat 7 Nov 2026 08:00 JKT. Nothing scheduled, nothing posted, 0 Higgsfield credits.

WATCH (720p, 10:55.2, 26.6 MiB, 0 decode errors): https://github.com/ganjarlaks/lakstruestory-media/blob/main/review/mandela_long_cut1/mandela_long_cut1_review_720p.mp4
RAW: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mandela_long_cut1/mandela_long_cut1_review_720p.mp4
Contact sheets: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mandela_long_cut1/contact_1.jpg and .../contact_2.jpg
Clip table: https://github.com/ganjarlaks/lakstruestory-media/blob/main/review/mandela_long_cut1/clip_table.md
Grabs (each real-audio moment, each card, closing frame): https://github.com/ganjarlaks/lakstruestory-media/tree/main/review/mandela_long_cut1/grabs
Draft English captions: .../mandela_long_cut1_captions_en_DRAFT.srt ; footage spans: .../footage_spans.json ; voice takes (64 mp3): .../voice_takes/
Tool: channels/laks-true-story/tools/build_mandela_long_v1.py (plan, shots, audio, align, caps, mux, review).

## Length
10:55.2. The 8:00 minimum is met. The script note said "if over 10:00, drop the optional Stina line first": that block (line 4.16 plus the clip) is 29.4 s, so dropping it gives 10:25.8, still over 10:00. Other trims available without cutting narration: shorten the Charlie Rose clip CR3 (27.6 s) to its last two sentences (-9 s), shorten the Soweto statement (21 s) to its last sentence (-9 s). Narration alone is 7:35.8 (64 lines, no line cut, no line re-recorded).

## Split of screen time (measured from the plan)
- Real moving footage with real audio: 160.6 s (24.5%), 9 moments.
- Real moving footage muted under narration: 18.5 s (2.8%), 3 shots.
- Real moving footage total: 179.0 s (27.3%).
- Portrait stills lifted from the PBS special: 20.4 s (3.1%), 3 shots.
- Own typographic cards on narration lines (date, place, quoted words): 410.5 s (62.7%).
- Opening, four chapter cards, closer, references: 45.2 s (6.9%).

HONEST FLAG: this is far under the footage-first standard set for Embassy cut 3 (at least 70% real moving footage, text and documents 15 to 20%). Chapter 1 (1960 to 1964) and chapter 2 (prison years) have almost no usable footage in what was reachable, so those lines sit on typographic cards. The cards carry only facts from the claim table (dates, places, verbatim quotes). If the owner wants the footage-first rule applied here, cut 2 needs more footage, see "Needed for cut 2" below.

## Structure
Opening card 5 s, then H1 to H3, chapter 1 (card "From Sharpeville To A Life Sentence", lines 1.1 to 1.16), chapter 2 ("The Prison Years", 2.1 to 2.11), chapter 3 ("The Day He Walked Out", 3.1 to 3.13), chapter 4 ("From Freedom To The Presidency", 4.1 to 4.19), closer (Z1 and Z2 read aloud, text on the card), closing references frame 7 s. All cards 5.0 s (owner rule of 28 Oct), references hold 7 s.

## Real-audio moments (clip_table.md has the exact spans)
1:22 1961 interview "useless and futile to continue talking peace and non-violence" (PBS, the 1961 date stamp is burned into the picture: verified on the grab); 3:10 Charlie Rose 1993 on his family; 4:06 his daughter reading his 1985 refusal at the Soweto rally (PBS); 5:54 de Klerk announces the release (PBS, the clip starts mid-sentence at "now in a position to announce", see ear-check); 7:10 BBC 12 Feb 1990 "completely overwhelmed by the enthusiasm"; 7:28 BBC question and answer "no conflict between those two statements"; 8:20 Charlie Rose 1993 on de Klerk; 9:04 Nobel Lecture, tribute to de Klerk (the picture is the audience cutaway of de Klerk, Mandela is heard); 9:51 Stina interview, Pretoria 1994, "the dominating feeling was one of a conviction that whatever difficulties I have, I will return".
Picture of real clips: the 4:3 picture is centred over a blurred, darkened copy of itself, source tag top left on every footage shot (as in Columbine cut 4).

## Mix
Voice -16 LUFS, real clips normalised to the same level (band-passed 100 Hz to 7 kHz, limited), music bed -25.5 LUFS integrated target, ducked out under every real clip, ducked 65% under chapter cards, swell at the closer, 2 s fade out. Final mix -16.2 LUFS, peak 0.89, no clipping. 0 decode errors.

## MUSIC: real, not synthesised
Chopin, Nocturne Op. 27 no. 1 in C sharp minor then Op. 48 no. 1 in C minor (6 s crossfade), performer Aaron Dunn, Musopen "The Complete Chopin Collection". Licence: CC0 1.0 public domain dedication, from the item metadata (licenseurl creativecommons.org/publicdomain/zero/1.0). Source: https://archive.org/details/musopen-chopin . Not the Embassy "Cold Archive" bed (that one was self-synthesised). I could not listen: checks were objective only. Solo piano, no vocals; the two recordings differ by 7.6 LU, so Op. 48 is trimmed by 7.6 dB before the crossfade; loudness range 16 LU, evened with a slow dynamic normaliser; tails (5 and 8 s of silence) trimmed. EAR-CHECK NEEDED: that the nocturnes feel right under the narration, that the crossfade at about 5:40 is not audible as a seam, that no quiet piano passage is lost under the voice.

## EAR-CHECK LIST (machine checks only, nobody has listened)
1. Voice: Chatterbox variant B, 64 lines, forced alignment matched 1148 of 1201 script tokens (the rest interpolated). Lines below 80% match: H1 (7 of 9) and 4.19 (7 of 10), probably the number words ("Twenty seven", "ninety five"). Check H1, 4.19 and the respellings (Umkhonto we Sizwe, Sharpeville, Coetsee, Sisulu).
2. Real-audio captions are machine transcripts (faster-whisper small.en). Two spots are uncertain and need an ear check: CR2 "the terrible part, a terrible pain, I did it" (an earlier base.en pass heard "a terrible thing under it"); CR3 "however discredited and illiterate it is". NOBEL: the machine heard "terrible role" and missed the name; the caption uses the official Nobel Lecture wording ("a terrible wrong had been done", "Mr. F. W. de Klerk"). ANN: the clip starts at "now in a position to announce", the first words "I am" fall just before the cut.
3. CR3 (Charlie Rose) starts at "There have been occasions when I did not think that he lived up to expectations": the words about integrity ("I accept his integrity") come 20 s earlier in the interview and are not in the clip. Narration 4.9 says only "he also spoke about President de Klerk".
4. 3.7 "few people had seen a recent picture of him" rests on the PBS machine transcript (banned inside South Africa, "doesn't look like the picture we imagine"); soft claim, drop if the ear check is not clean.
5. 3.8 "two raised fists" rests on one Getty caption and is shown as a text card only, no footage of it is in the cut. 3.6 b-roll (people and camera crews at the prison, PBS) is the place as described in the PBS commentary, not a shot of the release itself.
6. Narration sync: word-level captions are forced-aligned, median offset not measured against a hand check; check three lines by eye.

## Needed for cut 2 if footage-first is required
- The full PBS "Free At Last" special (youtube XFAr14RZMbQ, about 1 hour; only 12 spans were cut and the source was deleted for disk space): release day, Cape Town City Hall, Soweto, Robben Island pictures, rally footage for chapters 2 to 4.
- Frontline "Apartheid's Last Stand" (b-roll, avoid violent frames) and any newsreel of Sharpeville (60s), the Rivonia trial, the Palace of Justice: none reachable in this run.
- More real-audio moments already on disk, zero new download: the Stina interview (36 min, 1994) has Mandela on "I am prepared to die" (about 8:17 to 8:43, "not from a spirit of bravado... they were going to hang us"), the Robben Island years (about 9:41 to 11:13), the son and the underground years (about 5:42 to 6:08), and the Charlie Rose interview has more. These would add real audio to lines 1.14, 1.16, 2.1 but would also lengthen the video past 10:55, so lines or clips must give way.

## Overlap with the Short S2_mandela (OWNER DECISION, relayed as approved)
Same story, same sources: the long re-uses the registered Short spans. In the PBS file (original timecodes): 12:09 to 12:23 (ANN 12:10 to 12:21), 18:30 to 18:37 (1961 clip 18:26 to 18:42), 23:32 to 23:47 (b-roll 23:30 to 23:38 and 23:41 to 23:46), 24:20 to 24:59 (Soweto statement 24:36 to 24:56). BBC file: A4 1:11.8 to 1:18.8 (BBC4 1:07 to 1:20), A5 2:25.7 to 2:32.7 (BBC5 2:20 to 2:31), FREE AT LAST paper 5:36 to 5:50 (3.13 at 5:37.5 to 5:42.6). Registered spans not used in the long: 15:13 to 15:17, 12:58 to 13:02.

## Rights
See RIGHTS_LOG_MANDELA_LONG_2026-11-04.md and ASSET_REGISTRY_ADD_MANDELA_LONG.md in the same folder. Fair use on all footage (short excerpts, commentary and narration around them, source tag on every shot, no re-sale); the Nobel lecture video carries its nobelprize.org watermark (kept). Music CC0.

## What was NOT done
No YouTube upload, no scheduling, no posting, no thumbnail, no description or publish pack. Captions are a DRAFT srt (burned in the review copy). No 1080p master.
