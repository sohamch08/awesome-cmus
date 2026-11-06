# Historical and archived resources

Older implementations are useful for understanding the ecosystem and adapting ideas. Repository age alone is not a maintenance verdict. Explicit archival and availability labels below are based on the metadata check dated November 6, 2026.

[Back to the list](../README.md) · [Detailed ecosystem guide](ecosystem-guide.md)

## Projects and scripts

- [0x61nas/cmus-rpc](https://github.com/0x61nas/cmus-rpc) - **Archived repository.** Archived Java implementation.
- [0x61nas/cmus-rpc-rs](https://github.com/0x61nas/cmus-rpc-rs) - **Archived repository.** Archived Rust implementation.
- [Awesome widget example](https://github.com/cmus/cmus/wiki/Awesome-DM-widget) - Historical Awesome WM integration.
- [cmus-airpods](https://github.com/samdmarshall/cmus-airpods) - Older agent responding to AirPods events through `cmus-remote`. An interesting integration example, although dated.
- [cmus-album-shuffle](https://github.com/mjc-506/cmus-album-shuffle) - Historical implementation. Current cmus has native library album shuffle, so inspect this for its code or a different workflow rather than assuming it is necessary.
- [cmus-android-remote](https://github.com/jatwigg/cmus-android-remote) - Older Android remote-control app.
- [cmus-base-plugins](https://github.com/cmus-plugins/cmus-base-plugins) - Packages several wiki scripts together.
- [cmus-bundler](https://github.com/nogizhopaboroda/cmus-bundler) - Older Node.js plugin/theme manager with a daemon and bundle mechanism. Interesting architecture, but dependencies and examples are dated.
- [cmus-droid-remote](https://github.com/seriousben/cmus-droid-remote) - **Archived repository.** Archived Android remote implementation.
- [cmus-lan-control](https://jasonwoof.com/gitweb/?p=cmus-lan-control.git;a=summary) - Older LAN interface for playback and queue operations.
- [cmus-lrc](https://github.com/fooyou/cmus-lrc) - Python terminal display. Older implementation that relies on a particular lyrics service, so service compatibility matters.
- [cmus-mediakeys](https://github.com/nogizhopaboroda/cmus-mediakeys) - Older Node.js media-key integration. README documents very old Node compatibility problems.
- [cmus-remote-vim](https://github.com/professorsloth/cmus-remote-vim) - Another older collection of Vim control functions.
- [cmus-visualizer](https://github.com/AlBurns-MSFT/cmus-visualizer) - Older visualization experiment to inspect as an implementation reference.
- [cmus2mysql](https://github.com/tuxfrickler/cmus2mysql) - Older implementation recording playback to MySQL.
- [cmus_daemon](https://github.com/ichier/cmus_daemon) - Wraps cmus and the older web app in screen, with startup/service support.
- [cmus_follow_playback](https://github.com/cmus/cmus/wiki/cmus_follow_playback) - Historical hook for following the current track. Compare with native `follow` behavior first.
- [cmus_hexchat](https://github.com/S0yKaf/cmus_hexchat) - Older HexChat plugin for controlling cmus, a different use of chat integration.
- [cmus_lastfmsubmit](https://github.com/cmus/cmus/wiki/cmus_lastfmsubmit) - Historical bridge to `lastfmsubmitd`.
- [cmus_music_monitor](https://github.com/cmus/cmus/wiki/cmus_music_monitor) - Logs listening metadata to CSV. **Historical:** the page recommends a Rust replacement, but the linked replacement and graphing repositories returned 404 during research.
- [cmus_play_next_album](https://github.com/cmus/cmus/wiki/cmus_play_next_album) - Historical album-skipping implementation. Current cmus provides album-navigation commands.
- [cmuscrobbler](https://github.com/freshprince/cmuscrobbler) - Older Python scrobbler, explicitly marked unmaintained.
- [cmusd](https://github.com/miraclx/cmusd) - Older Node.js companion providing desktop media integration, artwork, and controls.
- [CMusRemote](https://github.com/moonwave99/CMusRemote) - Older graphical remote with seeking, volume, and Apple Remote support.
- [CmusRemoteAndroid](https://github.com/kalenpw/CmusRemoteAndroid) - Another Android remote.
- [cmustify](https://github.com/kimond/cmustify) - Older status/notification experiment. Related versions exist in [Python](https://github.com/kimond/pycmustify), [Go](https://github.com/kimond/go-cmustify), and [Rust](https://github.com/kimond/rust_cmustify). Useful for comparing implementations rather than installing all of them.
- [fortes/dotfiles](https://github.com/fortes/dotfiles) - Larger personal environment with cmus configuration and integration ideas.
- [invicnaper/cmus-youtube](https://github.com/invicnaper/cmus-youtube) - Older source patch adding a `:youtube` command. Useful as a source-code extension example.
- [invicnaper/spotify-dl](https://github.com/invicnaper/spotify-dl) - Historical tool reading Spotify metadata and finding matching audio on YouTube. Does not download original Spotify audio.
- [itunes_notify.c](https://github.com/cmus/cmus/wiki/itunes_notify.c) - Historical bridge sending cmus updates to applications expecting iTunes notifications.
- [music-controls-bitbar](https://github.com/sebbas/music-controls-bitbar) - Menu-bar controls. **Legacy compatibility constraint:** the README requires an older BitBar release and says later versions are unsupported.
- [nblock/cmus-notify](https://github.com/nblock/cmus-notify) - Sends status into Awesome through `awesome-client`.
- [Original cmus_app](https://github.com/jboynyc/cmus_app) - **Archived repository.** Archived original. Its README directs readers to the fork above.
- [pekrockstar/cmus-lyric](https://github.com/pekrockstar/cmus-lyric) - Earlier Go viewer using local lyrics and NetEase. The newer index-null project identifies it as inspiration.
- [unite-cmus](https://github.com/KabbAmine/unite-cmus) - Integration for the older Unite.vim interface. Mainly relevant if you already use Unite.
- [viatatribal/cmus-youtube](https://github.com/viatatribal/cmus-youtube) - Later patch using yt-dlp to download audio and add it to cmus.
- [xsetcmus.sh](https://github.com/ronno/scripts/blob/master/xsetcmus.sh) - **Repository unavailable during metadata check.** Track information suitable for a dwm status bar.

## Important distinctions

- Native album shuffle and album-navigation commands cover some older scripts' original use cases.
- Archived does not necessarily mean unusable, and an unarchived repository is not proof of current support.
- `spotify-dl` in the original wiki uses Spotify metadata to locate YouTube audio; it is not original Spotify audio playback.
- Source patches can target old cmus revisions and need review before applying to current source.
- Some popular dotfile repositories have changed players. The [setup catalog](setups.md#historical-leads-that-need-care) records examples.
- Other notification-language variants and older alternatives remain described in the [ecosystem guide](ecosystem-guide.md).
