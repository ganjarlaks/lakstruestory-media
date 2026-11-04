# Mandela LONG: CUT_REVIEW v2 (4 Nov 2026, review copy 720p)

Title (owner-confirmed): Mandela: 27 Years In Prison, Then One Long Walk Out. Slot: Sat 7 Nov 2026 08:00 JKT. Nothing scheduled, nothing posted, 0 Higgsfield credits.
Owner decision driving this cut (21:42 JKT): cut to 8 minutes, fewer text cards, more real footage and video, TV broadcast footage is fine, more sourcing approved.

WATCH (720p, 8:30.0, 42.5 MiB, 0 decode errors): https://github.com/ganjarlaks/lakstruestory-media/blob/main/review/mandela_long_cut2/mandela_long_cut2_review_720p.mp4
RAW: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mandela_long_cut2/mandela_long_cut2_review_720p.mp4
Contact sheets: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mandela_long_cut2/contact_1.jpg and .../contact_2.jpg
Grabs: https://github.com/ganjarlaks/lakstruestory-media/tree/main/review/mandela_long_cut2/grabs
All footage with source timecodes: .../clip_table_all_footage.md and .../footage_spans_source_timecodes.json
Draft captions: .../mandela_long_cut2_captions_en_DRAFT.srt
Voice takes (unchanged, 64 mp3, same as cut 1): https://github.com/ganjarlaks/lakstruestory-media/tree/main/review/mandela_long_cut1/voice_takes
Tool: channels/laks-true-story/tools/build_mandela_long_v2.py (plan, shots, audio, align, caps, mux, review).

## Length: 8:30.0 (inside the 8:00 to 8:30 target)
Narration 63 of 64 lines kept untouched (7:28 of voice). Dropped: the optional Stina block (line 4.16 and its clip), the second Charlie Rose clip (CR3, de Klerk) and the Nobel Lecture clip (the Nobel ceremony picture is still used as muted b-roll). CR2 (Charlie Rose on family) trimmed to 8.7 s; A2DAU (Soweto rally statement) trimmed to the last sentence, 8.4 s; BBC4 5.6 s; BBC5 4.6 s. Pauses between lines 0.15 s (was 0.38 s), chapter cards 1.8 s (was 5 s), opening 2.8 s (was 5 s), references 4.2 s (was 7 s). To go shorter without touching narration: drop A1961 lead (16 s) or ANN (11 s).

## Split of screen time (measured from the shot log)
- Real moving footage, total: 474.1 s = 93.0% (target 70%).
  - with real audio (6 moments): 54.8 s (10.7%)
  - muted under narration (56 shots): 419.3 s (82.3%)
- Portrait stills lifted from the PBS special: 9.2 s (1.8%), 2 shots (3.7 and 4.19).
- Own graphics: opening, four chapter cards, closer, references: 26.7 s (5.2%). No typographic cards sit on narration lines any more.
Cut 1 was 27.3% real footage at 10:55.

## What the picture is made of (every shot is real archive footage with its source tag top-left)
- PBS "Free At Last" (Global Vision, 1990), re-downloaded in full: 1950s and 1960s archive (crowds, Mandela film, police, court, Sharpeville era), Robben Island sea and prisoners, Sisulu release Oct 1989, de Klerk to Parliament 2 Feb 1990, 10 Feb 1990 announcement room, 11 Feb 1990 release-day crowds, Victor Verster grounds, Tutu interview, press at the prison.
- PBS Frontline "Apartheid's Last Stand" (1993): Durban rally 25 Feb 1990, CODESA Dec 1991, Mandela and de Klerk together, 1993 rallies and Union Buildings, de Klerk interview. Used for chapter 4 (1990 to 1994).
- BBC News 12 Feb 1990, Charlie Rose 30 Sep 1993, Nobel ceremony Oslo 1993 (b-roll only).
- Chapter 4 caveat: no 1994 election or inauguration footage was found (the Frontline is dated March 1993). Lines 4.12 to 4.15 sit on 1993 rally and Union Buildings footage tagged "1993" / "THE UNION BUILDINGS, PRETORIA", not on the 1994 event itself. The tags say what the picture is, not what the narration says. Better 1994 footage would be the one upgrade worth a further search.

## Real-audio moments (6)
1:14.6 A1961 the 1961 interview (peace and non-violence, date burned in the picture); 2:56.9 CR2 Charlie Rose, "after agonizing over this ... I had done the right thing"; 3:41.5 A2DAU daughter reads his 1985 refusal at the Soweto rally ("until the day I die ... I care even more for your freedom"); 5:11.6 ANN de Klerk announces the release date; 6:20.7 BBC4 "completely overwhelmed by the enthusiasm"; 6:31.3 BBC5 "no conflict between those two statements".
Chapter cards at 0:19.8, 2:39.0, 4:45.0, 5:57.5. Closer 8:13.3, references frame 8:25.8.

## Mix
Same as cut 1: voice -16 LUFS, real clips normalised to the voice (100 Hz to 7 kHz band-pass, limited), Chopin bed ducked out under every real clip and 65% under chapter cards, swell at the closer, 2 s fade out. Final mix -16.1 LUFS, peak 0.89. 0 decode errors.
MUSIC: real, not synthesised: Chopin Nocturne Op. 27 no. 1 then Op. 48 no. 1, performer Aaron Dunn, Musopen "Complete Chopin Collection", CC0 (https://archive.org/details/musopen-chopin).

## EAR-CHECK LIST (machine checks only, nobody has listened)
1. Quiet source clips boosted a lot to match the voice: CR2 (-34.0 LUFS before normalising, about +18 dB), ANN (-28.0), A1961 (-27.6), A2DAU (-27.4). Listen for hiss and pumping at 1:14, 2:56, 3:41, 5:11. BBC4 and BBC5 were already loud (-14.7, -15.5).
2. Real-clip joins: each clip is entered 0.12 s after the lead-in line and left 0.22 s after the last word. Check no clipped first syllable at A2DAU (starts mid-sentence at "the day I die", trimmed from a longer statement) and ANN (starts mid-sentence "now in a position to announce").
3. Voice: forced alignment matched 1130 of 1183 script tokens; lines below 80%: H1 (7 of 9) and 4.19 (7 of 10), probably number words. Check H1, 4.19 and the respellings (Umkhonto we Sizwe, Sharpeville).
4. Pace: gaps between narration lines are now 0.15 s. Check it does not feel rushed, especially after the sentence-final lines in chapter 1.
5. Music: bed starts under the opening card and returns after each real clip. Check the Nocturne never covers a word and the swell at the closer (8:13).
6. Captions: burned in, narration and real-clip words. Real-clip captions are machine transcripts with hand fixes; check "until the day I die" (A2DAU) and the two BBC lines.
7. Picture honesty (eye check, I viewed contact sheets only): 1.7 lead-in shows an interview face (Mary Benson, PBS) tagged generic "ARCHIVE"; 2.1 shows Transkei landscape tagged "THE TRANSKEI, MANDELA'S HOME REGION"; 3.12 is Tutu in a PBS interview (not Bishopscourt); 4.14 shows the Union Buildings area in 1993 footage. Flag any you want swapped.
8. Violence: no bodies or graphic frames were chosen (Sharpeville-era span starts after the body frames; chapter 4 violence line uses crowds with sticks). Check 1.1 (0:26) and 4.8 (7:02).

## Rights
See RIGHTS_LOG_MANDELA_LONG_cut2_2026-11-04.md and ASSET_REGISTRY_ADD_MANDELA_LONG_cut2.md in this folder. New items vs cut 1: PBS Frontline "Apartheid's Last Stand". Fair use approved by the owner for PBS and BBC. The full PBS and Frontline source files were deleted after cutting.
