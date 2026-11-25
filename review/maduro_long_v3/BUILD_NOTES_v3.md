# Maduro long v3 (audio re-mix only, 25 Nov 2026): bed lowered again
Owner feedback on v2: still too loud. v3 = same bed (HoliznaCC0 "20 Minute Meditation 1", CC0, file 8.0 to 511.9 s), same code path, BED_UNDER_LU 10.598 -> 19.148 (bed 8.55 dB lower than v2). Rule applied: at least 25% under v2 on both K-weighted and A-weighted, and A-weighted bed <= v1 bed x 0.7; the A-weighted target (-8.5 dB) was the larger cut, so it set the level.
Unchanged vs v2 (verified): video stream copied from the hosted v2 files (md5 1080p acf6d5f7ffb33acc9a8f2c680bf523f2, 720p c54f292baa1534dcb8d7672243cc8a9f, equal to v2 and v1), duration 503.900000 s, same narration, closer, four windows (per-window lufs_raw/gain/final identical to v1/v2), ducking, +3 dB card swell, fades; SRTs and description byte-identical copies of v2 (description v3 = v2 text, Music line as in v2).
## Measured (bed-only opening card 1.0 to 4.5 s; whole mix; narration zones)
| | v1 (Zabriskie) | v2 | v3 |
|---|---|---|---|
| Bed K-weighted, opening card | -20.9 LUFS | -23.6 | -32.2 |
| Bed broadband RMS | -17.4 dBFS | -23.3 | -31.8 |
| Bed A-weighted RMS | -33.2 dB | -27.8 | -36.3 |
| Bed under narration (K) | -23.5 LUFS | -26.6 | -35.2 |
| Voice-to-bed ratio (LU) | 7.5 | 10.6 | 19.1 |
| Narration-zone LUFS of finished mix | -15.70 | -15.90 | -16.00 |
| Whole mix I / LRA | -16.1 / 5.5 | -16.4 / 5.5 | -16.3 / 5.6 |
v3 vs v2: -8.6 dB K-weighted, -8.6 dB broadband, -8.55 dB A-weighted (x0.37). v3 vs v1 bed: A-weighted -3.13 dB (x0.70), K-weighted -11.3 dB. Voice stem stays -16.0 LUFS. Soft peak guard touched 16,548 samples.
Faintly present, not inaudible: the bed sits 19 LU under the voice in narration and about -32 LUFS on the silent cards. NOT verified: nobody has listened; whether it is still audible or finally comfortable is a judgement for the owner. If it vanishes, raise BED_UNDER_LU slightly (about 17 to 18).
