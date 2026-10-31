# MLK long "Martin Luther King: The Speech That Shocked The World": CUT REVIEW 1 (stage CUT_REVIEW, 31 Oct 2026)

Nothing posted, scheduled or spent (0 credits, no AI imagery, no random stock, no placeholder cards). Built from the approved script v1 takes (Fraser clone B, 74 lines) and the rights-clean set of SHOTLIST_v1.md. Build scripts: `build/` (mlk_plan.py, build_mlk_audio.py, build_mlk_shots.py, build_mlk_mux.py, build_mlk_review.py, mlk_cards.py). Working files were in /tmp/mlk (not in the repo).

## Files
- **720p review** (1280x720, 30 fps, H.264 + AAC 80k): `/home/claude/production-house/channels/laks-true-story/pipeline/long-video/mlk/review_cut1/mlk_review_720p.mp4`, 28,505,714 bytes = 27.2 MiB (under 30 MiB). Hosted: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/mlk_review_720p.mp4 (page: https://github.com/ganjarlaks/lakstruestory-media/blob/main/review/mlk_long_cut1/mlk_review_720p.mp4)
- **1080p** (1920x1080, 30 fps, CRF 21): `/home/claude/mlk_out/mlk_review_1080p.mp4` (outside the repo on purpose), 278,013,547 bytes = 265 MiB. NOT hosted (over the 100 MB GitHub file limit); needs the Higgsfield media_upload path from a session that has it.
- Captions: `https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/captions_en.srt`, `https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/cap.ass` (burned on both mp4s). Word times: `https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/word_times_forced_alignment.json`. Timeline: `https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/plan.json`.
- Proof sheet: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/proof_sheet.jpg. Contact sheets: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/contact_1.jpg, https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/contact_2.jpg. Full-size 1920x1080 grabs (cold_open_film, opening_card, chapter3_card, still_birmingham, typeset_jfk, real_audio_AM3_yellow_subtitle, king_speech_KS4, jones_clip_AM6, doc_memo_highlight, doc_jones_transcript, film_king_to_camera_AM7, selma_4.24, closer_card, closing_frame_references): https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/grabs/ (14 files, list below). Closing frame grab: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/grabs/closing_frame_references.png

## Headline
- Duration **8:55.7 (535.67 s)**, 16,070 frames, equal to the timeline. Inside the 9:00 +/- 0:30 budget of SHOTLIST section 1 (the 90 s Short cap does not apply to long videos). All 74 narration lines (H1, H2, 1.1 to 4.25, Z1, Z2) are in; 4.11_alt is NOT used (4.11 and 4.12 read "Negro" as written, owner yes).
- Cold open (H1, H2, 8.2 s) before the opening card, as the owner approved. Then opening card 5.0 s, 4 chapter cards 5.0 s each, closer, references frame 5.0 s (owner card-hold rule 28 Oct).
- Layout (long-video SOP): 1920x1080 full-bleed, no tags over picture, no outline card. Captions Poppins Bold 88, white, black outline, max 2 lines, margins 240, black scrim under the lower third; real-audio subtitles yellow (Gandhi/Apollo `Real` style; the shot list says white, the Gandhi/Apollo precedent is yellow: say if you want white). 4:3 film is scaled to 1920 wide and cropped to 1080 rows (loses the bottom/top quarter), documents and stills are windows, portrait stills use blurred-fill.
- Music: self-synthesised "Cold Archive" bed (candidate C, seed 63, tools/build_music_candidates_2.py; rights-clean, tonal, no pulse). NOT owner-picked (shared/music/README.md: C/D/E pick not recorded; the Apollo cut used the same bed). Bed measured -25.5 LUFS vs narration -16.0 LUFS (9.5 dB under), silent (ducked 0.25 s ramps) for each of the 12 real-audio clips, 0.5 s fade in, 1.5 s fade out, swell about +4 dB from the closer start and a little more after the closing line. Whole mix after a limiter (0.89): -16.6 LUFS, peak -1.0 dBFS. Real clips normalised to -16 LUFS each (film sound was -27 to -31 LUFS raw, band-passed 110-6500 Hz, so its hiss is lifted: ear check).
- Picture mix (between cards, 495 s): moving real footage **196 s = 39.5%** (owner accepted 38%), real stills 18.2%, document pages 33.3%, own typeset text cards 9.0%. Cards total 41 s.
- Footage resolution: **all NARA/USIA film spans were re-cut from the 720x480 MPEG-2 master** (951 MB archive.org download, deinterlaced, scaled to 1920x1440, crop 1080). Master time equals the 512kb-mp4 time exactly (checked by frame difference). Selma (gov.archives.arc.53422) was seek-fetched from the master over HTTP (two spans, 640x480 and 720x480). Church Committee pages were rendered from the 68 MB bw PDF at native 2030 px width; Jones pages from the LOC PDF.

## Chapters (YouTube chapter list)
0:00 Cold open: the memo hook (H1, H2)
0:13 Eleven Weeks Before The Dream (opening card 0:08.2, chapter card 0:13.2)
1:48 A Day On The Mall (card 1:48.5)
3:32 Tell Them About The Dream (card 3:32.4)
5:45 The Memo, The Law, The Echo (card 5:45.7)
8:39 Closer (Z1 at 8:40.2, Z2 at 8:44.1), research references frame 8:50.7 to 8:55.7

## Real-audio moments (12; every one subtitled in yellow; nobody has listened, texts from Whisper small.en plus the quoted texts)
| Time | ID | What | Source and span | Rights |
|---|---|---|---|---|
| 1:05.2 | AM1 | Kennedy: "We are confronted primarily with a moral issue." 3.3 s | https://archive.org/details/jfks19630611 file jfk_1963_0611_civilrights.mp3 at 240.55-243.85 s, over own typeset card | PD (presidential address), uploader provenance unconfirmed |
| 2:24.8 | AM2 | crowd sings "We shall overcome" 5.0 s | NARA film 86-91 s | PD (film label); song first verse PD 2016 ruling UNVERIFIED |
| 2:34.1 | AM3 | speaker (not named): "...its effect on the image of our country all over the world" 5.9 s | NARA film 980.1-985.95 s | PD (film label) |
| 2:43.1 | AM4 | speaker (not named): "Clearly, the religious leader of this occasion was Martin Luther King" 4.8 s | NARA film 1033.1-1037.9 s | PD (film label); names King |
| 2:52.5 | AM5 | prayer: "Pour out Thy benediction upon the United States of America" 7.5 s | NARA film 919.8-927.3 s | PD (film label) |
| 3:27.7 | KS1 | King: "Five score years ago," 4.1 s | speech copy https://archive.org/details/MartinLutherKing-IHaveADream 8.35-12.45 s, over film 611.0-615.7 s (NOT synced) | FU (fair use, owner decision); King estate copyright |
| 3:56.2 | KS2 | King: "a bad check, a check which has come back marked insufficient funds" 5.8 s | same copy 10.25-16.05 s, over film 502-508 s (NOT synced) | FU |
| 4:12.4 | AM6 | Clarence B. Jones: "She had performed earlier on the program, 'Tell them about the dream, Martin. Tell them about the dream.'" 4.6 s | LOC video https://tile.loc.gov/storage-services/service/afc/afc2010039/afc2010039_crhp0084/afc2010039_crhp0084_mv13.mp4 at 2:15:49-2:15:54 | FU (fair use, owner decision) |
| 4:52.4 | KS3 | King: "...today and tomorrow, I still have a dream." 4.9 s | same copy 8.95-13.85 s, over film 1188 s (NOT synced) | FU |
| 5:03.0 | KS4 | King: "...where they will not be judged by the color of their skin, but by the content of their character." 5.6 s | same copy 5.55-11.15 s, over film 1200 s (NOT synced) | FU |
| 5:15.9 | KS5 | King: "Free at last, free at last, thank God Almighty, we are free at last." 5.5 s | same copy 13.8-19.3 s, over film 1206 s (NOT synced) | FU |
| 5:39.1 | AM7 | King to camera: "...of the greatest, if not the greatest demonstrations for freedom and human dignity" 6.0 s | NARA film 1128.55-1134.55 s (continues the Short's last shot 0.7 s later, owner yes D1) | PD (film label) + King-image HIGH (NARA nr13-125) |

King voice total: speech excerpts 25.9 s (cap about 30 s) plus AM7 6.0 s = 31.9 s (the shot list planned 30; AM7 is on camera, not the speech). Clips for ear checks (720p cut from the review file, with sound and subtitles):
| Clip | Link |
|---|---|
| AM1 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM1.mp4 |
| AM2 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM2.mp4 |
| AM3 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM3.mp4 |
| AM4 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM4.mp4 |
| AM5 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM5.mp4 |
| AM6 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM6.mp4 |
| AM7 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/AM7.mp4 |
| KS1 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/KS1.mp4 |
| KS2 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/KS2.mp4 |
| KS3 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/KS3.mp4 |
| KS4 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/KS4.mp4 |
| KS5 | https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/clips/KS5.mp4 |

## Closing frame (owner closing-frame rule 27 Oct + card hold 28 Oct)
- Closer segment 11.03 s: black card, Z1 punch line fades in with the voice (8:40.2), Z2 question at 8:44.1, 2.4 s silent beat with the music swell, then the references frame. Frame: punch line, question, thin yellow rule, yellow heading RESEARCH REFERENCES, 5 reference lines (Church Committee Report, Book III, 1976; Clarence B. Jones Oral History, Library of Congress, 2013; National Archives / USIA Film, The March on Washington, 1963; Stanford King Institute; National Archives Press Release 2013 and Civil Rights Act), grey "Full list with links in the description". Names follow SCRIPT_v1.md REFERENCES.
- **Measured hold (references frame 8:50.7 to 8:55.7, from the 1080p file): total 5.0 s including fades; heading, all 5 references and the grey note each at full brightness (>= 95%) together from 0.67 s to 4.43 s = 3.77 s; each reference line alone fully visible about 4.0 s; fade-out 4.4 to 5.0 s.** Owner's 5.0 s card rule governs long videos.
- Grab: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/grabs/closing_frame_references.png

## Sync proof (captions from the final narration track)
- CTC forced alignment (torchaudio WAV2VEC2_ASR_BASE_960H, tools/lts_sync.py) of the spoken words (dates, years, FBI, History dot com respelled as spoken) per line on the final narration track (narr_track.wav built per line from the timeline), 1,203 words, 74 lines. One caption per sentence or half-sentence, first spoken word to last spoken word (+0.08 s), max 2 lines. 108 narration caption events + 23 real-audio subtitle events, 0 overlaps. Real-audio subtitles use Whisper small.en word times of each clip.
- Independent check: Whisper base.en on the whole final track: matched 1165 of 1203 words; Whisper start minus forced start: median -0.145 s, mean -0.174, abs(dev from median) p90 0.204, p95 0.292, max 0.825; within 0.2 s of forced: 68.1%. Whisper starts lead forced alignment by a constant about 0.145 s (same offset as the Apollo cut, not drifting); forced alignment is trusted. Proof sheet: https://raw.githubusercontent.com/ganjarlaks/lakstruestory-media/main/review/mlk_long_cut1/proof_sheet.jpg (8 sentences x start/middle/end; the "says" label is a rough word match).

## Verification
- `ffmpeg -v error -i mlk_review_720p.mp4 -f null -` and the same for the 1080p: zero errors (both run after the final mux). Duration 535.667 s both, picture and audio equal to the timeline.
- 720p size 27.2 MiB < 30 MiB (1-pass ABR 340 kbps, max 700 kbps, slow preset: documents and stills are sharp, film is soft).

## Corrections to SHOTLIST_v1 found while viewing the real film (honest list)
1. Shot 2c2 (film 595-600 s) is NOT the aerial Reflecting Pool: it is a woman at the microphones and then a man's face (dissolve). The aerial pool shot runs about 605-626 s. Row 2c2 now uses 605.6-610.8 s; KS1 picture uses 611.0-615.7 s; 4x (line 4.25) uses 618.0-624.5 s. These three are the SAME continuous aerial shot (different seconds), as the sourcing note feared; scrub it if it reads as a repeat.
2. Cold open picture H1 (film 30-35 s) is foliage and a boy, not marchers; replaced by film 215-219.5 s (crowd and marchers on a street, 3:35 in the film).
3. Row 1a (Birmingham) used the four LOC "No known restrictions" candidates instead of the planned map GAP-G: 1.1 street scene (loc.gov/item/2022634986), 1.2 press conference with Shuttlesworth, King and Abernathy during the Birmingham Campaign (loc.gov/item/2022634991). Storyboarder/owner call, easy to swap back to a map.
4. AM5 (prayer) uses film 919.8-927.3 s, where the "pour out thy benediction" words actually are; the planned 905-910 s span holds the Amos/Jesus/Paul lines. The picture there is a close-up of a woman's face in prayer (native sync).
5. AM1 is the first sentence only (3.3 s), not the planned 6 s with the "old as the scriptures" sentence.
6. KS1 is only "Five score years ago," (4.1 s): the rest of the opening sentence has 3-second pauses in this copy and does not fit the 3-6 s cap. KS3 in this copy is "I still have a dream" (the copy's wording), not "I have a dream today". KS4 and KS5 as planned.
7. Rows 3n (NARA press release) and 4v (Nobel facts page) are own typeset cards quoting the page text (no browser here for page captures); the NARA wording is verbatim: "Use of the film may require permission from the King Foundation, due to the rights claimed by the King Family for the use of King's image and the copyright on the \"I Have A Dream Speech.\"". Row 1d-1g likewise typeset from the TAH text of the 11 June address.
8. Documents: the phrase highlighted on each page was found by matching the PDF's OCR text layer (OCR has typos; matches 0.84 to 1.0, p92 and p118 lowest). Page numbers are PDF pages (printed + 10): 4.14 Sullivan "I put in this memorandum what Hoover wanted to hear" is on PDF p117 (footnote 118), "agilely switch" and "September 16" on p118. Windows were checked on the contact sheets, not every frame.
9. The not-synced KS pictures: line 3.4 says "Here is King delivering that passage" over crowd film of the day; the film does not contain the speech (the NARA film excludes it). Viewers could read the crowd shot as the same recording. Suggest an on-screen or spoken note ("the recording, over film of the crowd") if the owner wants it explicit; not changed without an owner yes.
10. Hook v2 (HOOK_TITLE_THUMBNAIL_v2) and the three retention re-teases are NOT in the cut: the owner approved script v1 and the takes are v1; v2 is still a proposal.
11. Jones clip: the LOC transcript prints "Tell them about the dream", Whisper hears "Tell him". The subtitle follows the transcript. Video is 480x270 upscaled to 1080p (soft). Clip 4.6 s inside the owner's 3-6 s.
12. Not delivered: closed captions in other languages, publish pack, thumbnail, 30 s trailer, registry rows (the producer adds them), 1080p hosting.

## Ear-check items (BUILD_STATUS.md; nobody has listened to any take)
- 3.5 Jones: "Mahalia Jackson" name and the line "called out to King to tell them about the dream" (QA ratio 1.0; stress on Mahalia unchecked). At 4:00 to 4:12.
- 3.11: Whisper heard "dreamer frame" for "dream refrain" (ratio 0.889). At about 4:57. Retake if it sounds wrong.
- 3.15: Whisper heard "old him line" for "old hymn line" (0.944), around 5:09-5:15. Retake if "hymn" is unclear.
- Names: Mahalia (3.5), Gaston (1.3), Reston (4.2), Randolph (1.12, 2.10), Sullivan, Hoover, Castro, Frank Church, Selma (4.24: the isolated test heard "Soma"; in the line Whisper heard "Selma").
- "Negro" in 4.11 and 4.12 (quotes from the memo, owner yes) and in King's own voice in KS2 (the recording says "the Negro people").
- All 12 real clips: subtitle wording (AM2 song "We shall overcome some day" vs Whisper "We have overcome it some day"; AM4/AM3 speakers unnamed; AM5 prayer; AM7 starts mid-phrase "...of the greatest"; KS texts from Whisper plus the known speech). The speech copy is a 10:49 edit whose recording identity is unconfirmed; check that KS1-KS5 sound like the 28 Aug 1963 recording and are not sped up or pitch-shifted.

## Assets used (direct links, rights status)
Film (NARA/USIA "The March on Washington", 1963): https://archive.org/details/gov.archives.arc.49737, master https://archive.org/download/gov.archives.arc.49737/gov.archives.arc.49737.mpeg. PD (archive.org film label, not itself a clearance), LOW; King on camera (AM7 and the stills with King) carries the NARA nr13-125 King-image caution, HIGH. Spans used (film seconds): 215-219.5 (H1), 450-453.7 (H2), 370-375, 380-385, 400-406.7, 10-14 (ch.1), 195-201, 465-468, 605.6-610.8, 100-107, 72-75.3, 990-994, 1020-1023, 898-902, 830-836, 85.7-91.3 (AM2), 979.8-986.3 (AM3), 1032.8-1038.2 (AM4), 919.5-927.6 (AM5), 611.0-615.7 (KS1), 500-502.1 and 502-508 (3.4, KS2), 1170-1177, 1180-1186, 1188-1193.5 (KS3), 1193-1198.1, 1200-1206 (KS4), 1206-1212 (KS5), 1212-1215, 1124.7-1128.4, 1128.25-1134.85 (AM7), 1217-1225.5, 410-415.5, 618-624.5 (ch.2-4). The Short's 17 spans are not reused except the continuation shot (owner D1).
Selma film: https://archive.org/details/gov.archives.arc.53422 (PD film label), 720-724.2 s and 1620-1624.2 s, silent, no person identified.
Library of Congress stills ("No known restrictions on publication", rights read from loc.gov JSON): https://www.loc.gov/item/2003688160/ ; 2013648833 ; 2013649707 ; 2013648841 ; 2013649720 ; 2013650621 ; 2013649715 ; 2013648835 ; 2013649717 ; 2013648845 ; 2013648834 ; 2013649721 ; 2022634986 ; 2022634991 (pattern https://www.loc.gov/item/<id>/). Several show King (K caution).
Commons/NARA photo (Scherman, NAID 542069, PD tag; King-image caution): https://commons.wikimedia.org/wiki/File:Martin_Luther_King_-_March_on_Washington.jpg
Documents: Church Committee Final Report Book III, 1976, https://archive.org/details/finalreportofsel03unit (PDF https://archive.org/download/finalreportofsel03unit/finalreportofsel03unit_bw.pdf; PD, US Senate report); Clarence B. Jones oral history transcript https://tile.loc.gov/storage-services/service/afc/afc2010039/afc2010039_crhp0084_Jones_transcript/afc2010039_crhp0084_Jones_transcript.pdf and record https://www.loc.gov/item/2015669183/ (FU, interviewee copyright, brief fair use pp.1, 51, 52, 53); NARA Kennedy message to Congress 19 June 1963 https://www.archives.gov/legislative/features/march-on-washington/kennedy.html (PD); NARA press release https://www.archives.gov/press/press-releases/2013/nr13-125 (quoted text); Nobel Prize facts page https://www.nobelprize.org/prizes/peace/1964/king/facts/ (quoted motivation, short caption use, FU low); JFK address text https://teachingamericanhistory.org/document/radio-and-television-report-to-the-american-people-on-civil-rights/ (public-domain address).
Audio: JFK https://archive.org/details/jfks19630611 ; King speech copy https://archive.org/details/MartinLutherKing-IHaveADream (uploader CC BY 3.0 tag is not a clearance; fair use); Jones video (LOC link above, fair use).
Music: own synthesis, no licence needed (tools/build_music_candidates_2.py candidate C).
Own graphics: opener, 4 chapter cards, closer, references frame, 6 typeset text cards. Narration: Fraser clone B, Chatterbox (0 credits), voice_takes/*.mp3.

## Per-line timeline (time = line start in the cut)
| Time | Id | Narration (opening) | Picture source |
|---|---|---|---|
| 0:00.0 | H1 | Two days after this speech, the FBI marked its speaker as a threat. | NARA/USIA film 49737 215.0-219.5 s |
| 0:04.5 | H2 | This is the story of the speech, and of the memo it caused. | NARA/USIA film 49737 450.0-453.7 s |
| 0:08.2 | card open |  | own card |
| 0:13.2 | card 1 |  | own card |
| 0:18.2 | 1.1 | It starts in the spring of 1963, in Birmingham, Alabama. | photo LOC 2022634986 (a) |
| 0:22.6 | 1.2 | Black residents there were protesting segregation, and Martin Luther K | photo LOC 2022634991 (a) |
| 0:28.3 | 1.3 | That spring the city saw violence, including a bombing at the Gaston M | photo LOC 2003688160 (a) + photo LOC 2003688160 (b) |
| 0:36.2 | 1.4 | Faced with the protests, President John F. Kennedy decided to back a n | photo LOC 2013648833 (a) |
| 0:41.8 | 1.5 | On 11 June 1963, he went on radio and television to explain why. | own typeset card jfk_title |
| 0:47.7 | 1.6 | That same day, National Guard troops had been needed to admit two Blac | own typeset card jfk_guard |
| 0:54.0 | 1.7 | He told the country that a Black baby born in America that day had abo | own typeset card jfk_baby + own typeset card jfk_baby |
| 1:03.2 | 1.8 | Then he named the problem. | own typeset card am1 |
| 1:05.2 | AM1 (REAL AUDIO) | We are confronted primarily with a moral issue. | audio jfk_AM1_239-251s.mp3 1.55-4.85 s over typeset card am1 |
| 1:09.1 | 1.9 | Eight days later, he sent his proposal to Congress. | photo NARA Kennedy message 19 Jun 1963 (a) |
| 1:12.3 | 1.10 | The National Archives notes that the message stressed how segregation  | photo NARA Kennedy message 19 Jun 1963 (b) |
| 1:20.6 | 1.11 | Civil rights leaders wanted to show Washington how many people stood b | NARA/USIA film 49737 370.0-374.9 s |
| 1:25.5 | 1.12 | A. Philip Randolph, a veteran labor leader, had been calling for a mar | photo LOC 2013649707 (a) + photo LOC 2013649707 (b) |
| 1:32.5 | 1.13 | Its official name was the March on Washington for Jobs and Freedom. | NARA/USIA film 49737 380.0-384.2 s |
| 1:36.7 | 1.14 | It demanded a strong civil rights bill, protection of the vote, school | NARA/USIA film 49737 400.0-407.3 s |
| 1:44.0 | 1.15 | The date was 28 August, eleven weeks after Kennedy's speech. | NARA/USIA film 49737 10.0-14.5 s |
| 1:48.5 | card 2 |  | own card |
| 1:53.5 | 2.1 | On 28 August 1963, people poured into Washington from all over the cou | NARA/USIA film 49737 195.0-202.9 s |
| 2:01.3 | 2.2 | The National Archives says hundreds of thousands came. | NARA/USIA film 49737 465.0-468.5 s |
| 2:04.8 | 2.3 | They gathered at the Lincoln Memorial. History.com reports that the le | photo LOC 2013648841 (a) + NARA/USIA film 49737 605.6-610.8 s |
| 2:15.1 | 2.4 | A film crew from the United States Information Agency recorded the day | NARA/USIA film 49737 100.0-106.3 s |
| 2:21.4 | 2.5 | Singing ran through the program, and so did speeches. | NARA/USIA film 49737 72.0-75.3 s |
| 2:24.8 | AM2 (REAL AUDIO) | We shall overcome | NARA/USIA film 49737 85.7-91.3 s, film sound |
| 2:30.4 | 2.6 | Another speaker talked about how America would look from abroad. | NARA/USIA film 49737 990.0-993.8 s |
| 2:34.1 | AM3 (REAL AUDIO) | It's going to have its effect on the image | NARA/USIA film 49737 979.8-986.2 s, film sound |
| 2:40.6 | 2.7 | Then a speaker singled out King. | NARA/USIA film 49737 1020.0-1022.5 s |
| 2:43.1 | AM4 (REAL AUDIO) | Clearly, the religious leader of this occasion | NARA/USIA film 49737 1032.8-1038.2 s, film sound |
| 2:48.5 | 2.8 | A minister's prayer asked God to bless the United States. | NARA/USIA film 49737 898.0-902.0 s |
| 2:52.5 | AM5 (REAL AUDIO) | Pour out Thy benediction | NARA/USIA film 49737 919.5-927.6 s, film sound |
| 3:00.6 | 2.9 | According to John Lewis's memoir, his own speech was toned down that d | NARA/USIA film 49737 830.0-836.7 s |
| 3:07.3 | 2.10 | According to Clarence B. Jones, King's lawyer and adviser, A. Philip R | Jones transcript PDF p51 'we should have him as the last speaker' + Jones transcript PDF p51 'Randolph' |
| 3:16.2 | 2.11 | Jones gave that account in a 2013 oral history for the Library of Cong | Jones transcript PDF p1 'Dr. Clarence Benjamin Jones' |
| 3:21.5 | 2.12 | When King reached the microphones at the Lincoln Memorial, he began by | photo LOC 2013649720 (a) + photo LOC 2013649720 (b) |
| 3:27.7 | KS1 (REAL AUDIO) | Five score years ago, | audio king_KS1_18-47s.mp3 8.35-12.45 s over film 611.0 s (picture not synced) |
| 3:32.4 | card 3 |  | own card |
| 3:37.4 | 3.1 | By his own account, King had finished that text around three thirty th | photo LOC 2013650621 (a) |
| 3:41.9 | 3.2 | A typescript had already gone to the press. | photo LOC 2013649715 (a) |
| 3:44.7 | 3.3 | Jones says he drafted the first six or seven paragraphs, including the | Jones transcript PDF p51 'six or seven paragraphs' + Jones transcript PDF p51 'verbatim' |
| 3:53.5 | 3.4 | Here is King delivering that passage. | NARA/USIA film 49737 500.0-502.7 s |
| 3:56.2 | KS2 (REAL AUDIO) | ...a bad check, a check which has come back | audio king_KS2_176-214s.mp3 10.25-16.05 s over film 502.0 s (picture not synced) |
| 4:02.6 | 3.5 | Then, Jones says, the singer Mahalia Jackson, who had performed earlie | Jones transcript PDF p52 'Mahalia Jackson' + Jones transcript PDF p52 'about the dream, Martin' |
| 4:10.2 | 3.6 | Here is Jones telling it himself. | Jones transcript PDF p52 'about the dream, Martin' |
| 4:12.4 | AM6 (REAL AUDIO) | She had performed earlier on the program, | LOC Jones oral-history video (2:15:42 file), clip 7.2-11.8 s of the 14 s file |
| 4:17.6 | 3.7 | Jones says King moved his text to the side of the lectern and gripped  | photo Commons Scherman NAID 542069 (a) + photo Commons Scherman NAID 542069 (b) |
| 4:24.9 | 3.8 | Jones says he turned to the person next to him and said the crowd was  | NARA/USIA film 49737 1170.0-1175.4 s |
| 4:30.2 | 3.9 | King later recalled that he turned aside from the manuscript altogethe | photo LOC 2013648835 (a) |
| 4:34.4 | 3.10 | Other accounts agree that the dream passage was not in the written tex | photo LOC 2013649717 (a) |
| 4:38.7 | 3.11 | But historians add a nuance. King had used the dream refrain before, i | photo LOC 2013648845 (a) |
| 4:46.5 | 3.12 | The words were not new to him. The moment was. | NARA/USIA film 49737 1180.0-1183.5 s |
| 4:50.0 | 3.13 | This is where the speech turns. | NARA/USIA film 49737 1183.5-1185.9 s (continues) |
| 4:52.4 | KS3 (REAL AUDIO) | ...today and tomorrow, | audio king_KS3_340-358s.mp3 8.95-13.9 s over film 1188.0 s (picture not synced) |
| 4:57.9 | 3.14 | He spoke of his four children, and of a country that would judge them  | NARA/USIA film 49737 1193.0-1198.1 s |
| 5:03.0 | KS4 (REAL AUDIO) | ...where they will not be judged by the color of their skin, | audio king_KS4_424-437s.mp3 5.55-11.15 s over film 1200.0 s (picture not synced) |
| 5:09.2 | 3.15 | Jones says King looked at his notes again only near the end, for the o | Jones transcript PDF p53 'free at last' |
| 5:15.9 | KS5 (REAL AUDIO) | Free at last, free at last, | audio king_KS5_625-644s.mp3 13.8-19.3 s over film 1206.0 s (picture not synced) |
| 5:22.0 | 3.16 | That is about all of the speech this video can play. The National Arch | own typeset card nara_press + own typeset card nara_press |
| 5:32.3 | 3.17 | The free government film of the day never reaches it. | NARA/USIA film 49737 1212.0-1215.1 s |
| 5:35.4 | 3.18 | What it does catch is King afterwards, talking to the camera. | NARA/USIA film 49737 1124.7-1128.5 s |
| 5:39.1 | AM7 (REAL AUDIO) | ...of the greatest, if not the greatest demonstrations | NARA/USIA film 49737 1128.2-1134.8 s, film sound |
| 5:45.7 | card 4 |  | own card |
| 5:50.7 | 4.1 | After the march, King and the other leaders went to the White House to | photo LOC 2013648834 (a) + photo LOC 2013649721 (a) |
| 5:56.3 | 4.2 | The next day, James Reston wrote in the New York Times that King had t | NARA/USIA film 49737 1217.0-1225.2 s |
| 6:04.5 | 4.3 | Inside the FBI, a quiet fight had been going on for weeks. | Church Committee Book III PDF p115 '67-page Brief' |
| 6:08.9 | 4.4 | Hoover had already written on an FBI memo, back in 1962, that King was | Church Committee Book III PDF p92 'As early as 1962' |
| 6:14.6 | 4.5 | A Senate committee, led by Frank Church, later published the paper tra | Church Committee Book III PDF p5 'Final report' |
| 6:19.3 | 4.6 | In the week before the march, the bureau's domestic intelligence divis | Church Committee Book III PDF p115 '67-page Brief' + Church Committee Book III PDF p116 'Communist Party' |
| 6:27.1 | 4.7 | It found that the Communist Party had mostly failed to win influence a | Church Committee Book III PDF p116 'obvious failure of the Communist Party' |
| 6:32.8 | 4.8 | Hoover disliked that answer. He wrote across it that it reminded him o | Church Committee Book III PDF p116 'Castro took over Cuba' + Church Committee Book III PDF p117 'Time alone proved you wrong' |
| 6:42.0 | 4.9 | William Sullivan, who ran that division, later told the Senate that hi | Church Committee Book III PDF p117 'how to get out of trouble' + Church Committee Book III PDF p118 'Sullivan testified' |
| 6:49.9 | 4.10 | He wrote it on 30 August 1963, two days after the speech. | Church Committee Book III PDF p117 'On August 30' |
| 6:54.9 | 4.11 | In it, Sullivan said that after King's powerful demagogic speech, King | Church Committee Book III PDF p117 'powerful demagogic speech yesterday' + Church Committee Book III PDF p118 'influencing great masses of Negroes' |
| 7:04.9 | 4.12 | He said the bureau must now mark King as the most dangerous Negro of t | Church Committee Book III PDF p118 'We must mark him now' |
| 7:11.1 | 4.13 | That is the shock this story can prove. | Church Committee Book III PDF p118 'most dangerous Negro of the future' |
| 7:13.7 | 4.14 | In 1975, Sullivan told the Senate that he put in that memo what Hoover | Church Committee Book III PDF p117 'I put in this memorandum what Hoover wanted to hear' |
| 7:19.9 | 4.15 | Sullivan also told the committee that writing it meant a lot of nonsen | Church Committee Book III PDF p118 'lot of nonsense' + Church Committee Book III PDF p118 'really did not believe in' |
| 7:29.8 | 4.16 | Either way, the memo shows how the bureau read the speech. | Church Committee Book III PDF p92 'free at last' + Church Committee Book III PDF p93 'demagogic speech' |
| 7:33.5 | 4.17 | On 16 September, Sullivan asked for more aggressive coverage. Hoover r | Church Committee Book III PDF p118 'September 16' + Church Committee Book III PDF p118 'agilely switch' |
| 7:44.3 | 4.18 | In October, Attorney General Robert Kennedy approved FBI wiretaps on K | Church Committee Book III PDF p127 'not able to ascertain why' + Church Committee Book III PDF p127 'wiretaps' |
| 7:56.4 | 4.19 | In December, senior FBI officials met to plan ways to neutralize King' | Church Committee Book III PDF p131 'neutralizing' |
| 8:02.2 | 4.20 | Days later, Time magazine named King Man of the Year, and Hoover said  | Church Committee Book III PDF p93 'dig deep in the garbage' + Church Committee Book III PDF p145 'Man of the Year' |
| 8:09.8 | 4.21 | Meanwhile the law moved. President Johnson signed the Civil Rights Act | NARA/USIA film 49737 410.0-418.0 s |
| 8:17.9 | 4.22 | King won the Nobel Peace Prize that year. | own typeset card nobel |
| 8:20.5 | 4.23 | He received it in Oslo on 10 December 1964. | own typeset card nobel |
| 8:24.8 | 4.24 | In 1965, marchers walked from Selma to Montgomery for the right to vot | NARA film 53422 Selma 720-724.2 s + NARA film 53422 Selma 1620-1624.2 s |
| 8:33.1 | 4.25 | On 4 April 1968, King was shot dead in Memphis, Tennessee. He was 39. | NARA/USIA film 49737 618.0-624.5 s |
| 8:39.6 | closer |  | own card |
| 8:50.7 | refs |  | own card |
