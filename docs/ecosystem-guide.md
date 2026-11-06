# cmus ecosystem guide

**Research date:** November 6, 2026

**Scope:** Plugins, companion programs, scripts, themes, integrations, source patches, complete setups, and practical guides.


**Setups:** [48 configurations and workflow examples](setups.md) include direct config links, screenshots, and historical context.

> [!NOTE] About this catalog
> This guide explains the resources in the catalog and suggests ways to combine them. Repository descriptions and documentation were checked during that research. The programs were not all installed or tested. Compatibility, package availability, and online APIs can change. A broad search cannot guarantee every forgotten repository or one-off gist.

> [!TIP] A useful starting setup on macOS
> Start with current cmus, tmux, a lyrics companion such as **index-null/cmus-lyric**, **cmus-control** or **cmusie** for media keys, **beets** for the library, **cmus-fzf** for search, and **cmus-status-scrobbler** for listening history. Add artwork and CAVA after the basic workflow feels comfortable. These are suggested combinations, not a tested distribution or bundle.

## Navigation

- [How the pieces fit together](#how-the-pieces-fit-together)
- [Core documentation and native features](#core-documentation-and-native-features)
- [Lyrics and synchronized lyrics](#lyrics-and-synchronized-lyrics)
- [Album art and visual companions](#album-art-and-visual-companions)
- [macOS controls and launchers](#macos-controls-and-launchers)
- [Visualizers and artwork colors](#visualizers-and-artwork-colors)
- [Scrobbling and listening history](#scrobbling-and-listening-history)
- [Recommendations and dynamic playlists](#recommendations-and-dynamic-playlists)
- [Fuzzy search and editor integration](#fuzzy-search-and-editor-integration)
- [tmux and persistent playback](#tmux-and-persistent-playback)
- [Notifications and status output](#notifications-and-status-output)
- [Linux panels and MPRIS](#linux-panels-and-mpris)
- [Discord and chat integration](#discord-and-chat-integration)
- [Web remotes and Android](#web-remotes-and-android)
- [Music and playlist synchronization](#music-and-playlist-synchronization)
- [Library cleanup and audio processing](#library-cleanup-and-audio-processing)
- [Themes and terminal appearance](#themes-and-terminal-appearance)
- [Complete setups and dotfiles](#complete-setups-and-dotfiles)
- [Small hacks and scripts](#small-hacks-and-scripts)
- [Downloads streams and source patches](#downloads-streams-and-source-patches)
- [Libraries plugins and implementation references](#libraries-plugins-and-implementation-references)
- [Blogs and practical guides](#blogs-and-practical-guides)
- [Putting a setup together](#putting-a-setup-together)

## How the pieces fit together

Most cmus extensions are separate programs. Understanding the connection points makes it much easier to combine projects without duplicating their work.

- **`cmus-remote` controls the player.** A script can query the playing track, toggle pause, change volume, seek, or add music. Fuzzy pickers, launcher commands, editor integrations, and web remotes commonly use this interface.
- **`status_display_program` reacts to changes.** cmus invokes a configured program when its status changes. Scrobblers, notifications, logging tools, and artwork programs often connect here.
- **MPRIS exposes desktop media controls.** On builds with MPRIS support, tools such as playerctl can interact with cmus through D-Bus. This is especially useful on Linux desktops.
- **Audio routing connects visualizers and effects.** CAVA and EasyEffects work with the audio system. They do not need to become part of cmus itself.
- **Library tools prepare the files.** beets, Picard, and ReplayGain scanners improve tags, artwork, lyrics, paths, and loudness metadata before cmus reads them.
- **Compiled input and output plugins handle audio.** These differ from ordinary companion scripts. Installing a standalone script does not add a new decoder to cmus.

The official [website](https://cmus.github.io/), [manual](https://github.com/cmus/cmus/blob/master/Doc/cmus.txt), and [remote manual](https://github.com/cmus/cmus/blob/master/Doc/cmus-remote.txt) explain these interfaces.

> [!IMPORTANT] One hook, several companions
> There is one `status_display_program` setting. If both your scrobbler and artwork viewer need it, use a wrapper that forwards the arguments to each program. Setting the option again for the second program replaces the first setting. See [Combining status hooks](#combining-status-hooks).

## Core documentation and native features

- [cmus 2.13.0](https://github.com/cmus/cmus/releases/tag/v2.13.0): Released October 28, 2026. Includes FFmpeg compatibility fixes, CUE improvements, duration sorting, playback position in status hooks, and MPRIS fixes. The wiki's stable-version heading was outdated when checked.
- [Main repository](https://github.com/cmus/cmus): Source code, build instructions, dependencies, and development activity. Start here when a package lacks an optional feature.
- [Full manual](https://github.com/cmus/cmus/blob/master/Doc/cmus.txt): Reference for commands, settings, filters, formatting, audio plugins, and MPRIS.
- [Official tutorial](https://github.com/cmus/cmus/blob/master/Doc/cmus-tutorial.txt): Explains how the library, playlists, queue, search, and playback modes relate.
- [cmus-remote manual](https://github.com/cmus/cmus/blob/master/Doc/cmus-remote.txt): Reference for external controls, metadata queries, and scripts.
- [Extension wiki](https://github.com/cmus/cmus/wiki): Original community catalog. Valuable for discovery, but some entries are historical.
- [Status display programs](https://github.com/cmus/cmus/wiki/status-display-programs): Hook-based integrations and instructions for combining them.
- [Bindable scripts](https://github.com/cmus/cmus/wiki/shell-scripts): Programs invoked from within cmus through `shell` and `run`.

Native features worth exploring before adding scripts:

- `replaygain=smart`: Selects suitable track or album gain behavior.
- `shuffle=albums`: Plays complete library albums in shuffled order.
- `resume=true`: Resumes playback at startup.
- `follow=true`: Follows the playing track.
- `live-filter`, `fset`, `factivate`: Interactive and saved filters.
- `lqueue`, `tqueue`: Queue random albums or tracks.
- `player-next-album`, `player-prev-album`: Skip between albums.
- `pl_env_vars`: Helps make library paths relocatable.
- `run`: Passes selected or marked files to another utility.

Use the [current manual](https://github.com/cmus/cmus/blob/master/Doc/cmus.txt) for syntax. Older guides sometimes use obsolete numeric or Boolean option values.

## Lyrics and synchronized lyrics

Choose a viewer according to what you want it to read: online lyrics, local `.lrc` files, or lyrics embedded in tags. Timestamped LRC lyrics support actual synchronization. Automatic scrolling of plain text can only approximate the song's timing.

- [index-null/cmus-lyric](https://github.com/index-null/cmus-lyric): Strong starting candidate. Go TUI with synchronized scrolling, embedded and local lyrics, caching, translations, candidate selection, multiple online sources, and covers. Offers Homebrew installation. Useful when you want one companion to handle both finding and displaying lyrics.
- [cmus-auto-lyrics](https://github.com/sparklost/cmus-auto-lyrics): Curses viewer with automatic scrolling, timestamp support, embedded tags, optional tag writing, offline mode, colors, and configurable height. Includes tmux launcher examples. Useful if you want a narrow lyrics pane alongside cmus.
- [lyrus](https://github.com/Ja4e/lyrus): Curses companion supporting cmus, local text and LRC files, and automatic fetching. Another option for a configurable scrolling display.
- [clyrics](https://github.com/trizen/clyrics): Extensible Perl fetcher with cmus, MOC, and playerctl daemon modes. Its source-plugin model is useful when you want to customize where lyrics come from.
- [lyvi](https://github.com/ok100/lyvi): Terminal viewer with artwork and synchronized LRC support. Uses libglyr and offers MPRIS integration. Its dependency stack is worth checking before choosing it.
- [cmus-liner](https://github.com/OliverHofkens/cmus-liner): Rust companion showing embedded lyrics and local cover art. Fits well with beets preparing the tags and artwork in advance.
- [hakerdefo/cmus-lyrics](https://github.com/hakerdefo/cmus-lyrics): Relatively simple shell-based fetcher for the current track. Easier to inspect and modify than a full TUI.
- [guxsousa/cmus-lyrics](https://github.com/guxsousa/cmus-lyrics): Separate fetching implementation worth inspecting for scripting ideas.
- [cmus-smart-lyrics](https://github.com/italrr/cmus-smart-lyrics): Inspired by hakerdefo's implementation, with standalone and tmux examples.
- [wdog/cmus_lyrics](https://github.com/wdog/cmus_lyrics): Fetches Genius lyrics into the terminal. Requires a Genius API token.
- [cmus-lrc](https://github.com/fooyou/cmus-lrc): Python terminal display. Older implementation that relies on a particular lyrics service, so service compatibility matters.
- [pekrockstar/cmus-lyric](https://github.com/pekrockstar/cmus-lyric): Earlier Go viewer using local lyrics and NetEase. The newer index-null project identifies it as inspiration.
- [lyriccli](https://github.com/Openmentia/lyriccli): Minimal command-line companion that currently supports cmus. Worth considering if a larger interface feels unnecessary.
- [bash-lyrics](https://github.com/mihaiolteanu/bash-lyrics): Downloads and saves lyrics, builds a searchable collection, and can play songs found through that collection. Supports cmus and MOC. Interesting if you remember a lyric but not a song title.
- [show-lyrics](https://github.com/alewmoose/show-lyrics): Another terminal lyrics project found in the cmus ecosystem. An alternative implementation to inspect rather than a first recommendation here.
- [lrcsnc](https://github.com/Endg4meZer0/lrcsnc): Player-independent synchronized lyrics through MPRIS. Particularly useful for putting lyrics into desktop bars and other displays.

> [!TIP] Make lyrics survive API changes
> Prefer tools that can read local LRC files or embedded lyrics as well as online sources. A saved copy remains useful when a lyrics website changes. Run one primary fetcher initially so that competing tools do not create confusing caches or tag updates.

## Album art and visual companions

Artwork tools generally either draw inside a graphics-capable terminal or open a separate window. A separate window is easy to position with a window manager. Terminal graphics keep the layout together, but depend on the terminal and sometimes the multiplexer.

- [cmus-cover-art](https://github.com/nogizhopaboroda/cmus-cover-art): Extracts artwork and displays it through a configurable image viewer. Documents iTerm2 support on macOS. Useful if you want to choose the renderer yourself.
- [S22F5/cmus_sixel](https://github.com/S22F5/cmus_sixel): C status program displaying covers through Sixel or Kitty graphics. Check that your terminal supports the selected protocol.
- [emp1r3/cmus-sixel](https://github.com/emp1r3/cmus-sixel): Small POSIX shell implementation using FFmpeg and `img2sixel`. Can also display the current cover independently.
- [Vizkid04/cmus_cover_art](https://github.com/Vizkid04/cmus_cover_art): Rust implementation using Kitty's image display. Its example combines cmus, tmux, artwork, and CAVA, making it useful as a layout reference.
- [cmus-artwork](https://github.com/mitrovicstefan/cmus-artwork): Pixelated terminal artwork with playback controls. Documents Linux and Mac support. Aesthetic rather than a high-resolution cover viewer.
- [cmusinfo](https://github.com/arisu-gh/cmusinfo): Multitool for status output, desktop notifications, and artwork through mpv. Useful if you prefer a separate artwork window with optional text.
- [cmusCoversSDL surviving fork](https://github.com/LaurentFough/cmusCoversSDL): Standalone artwork window using SDL2. The original repository linked from the wiki returned 404 during research.
- [cmus-feh.sh](https://github.com/TiredSounds/cmus-scripts/blob/master/cmus-feh.sh): Displays artwork in a separate feh window. Useful with Linux window-manager placement rules.
- [TiredSounds/cmus-scripts](https://github.com/TiredSounds/cmus-scripts): Collection of small companion scripts. Good material for building a personal wrapper.
- [TiredSounds/cmus-conky](https://github.com/TiredSounds/cmus-conky): Displays track information and artwork in Conky.
- [Gunqqer's musicScripts](https://github.com/gunqqer/musicScripts): Artwork scripts using w3m or viu, plus a music-sorting script. Shows several approaches to terminal image display.
- [cmusf](https://github.com/kushagraa-j/cmusf): Small shell utility for fetching the current song's cover.
- [cmus-swift](https://github.com/Coreball/cmus-swift): Native macOS artwork window with familiar playback and seeking controls. Useful if you want artwork outside the terminal.

For predictable results, keep a cover image next to each album or embed the image in the files. See [Library cleanup and audio processing](#library-cleanup-and-audio-processing) for tools that prepare both forms.

## macOS controls and launchers

Pick one primary media-key handler first. A menu-bar controller, a launcher command, and an artwork window can complement each other, but multiple applications trying to own the same media keys can complicate troubleshooting.

- [cmus-control](https://github.com/TheFox/cmus-control): Dedicated macOS media-key daemon with Homebrew and service instructions. A good first option when the main requirement is keyboard playback control.
- [cmus-osx](https://github.com/PhilipTrauner/cmus-osx): Track-change notifications and media-key support. Supports installation inside a Python virtual environment. The old `azadkuh/cmus-osx` URL redirects here.
- [cmusie](https://github.com/nkanaev/cmusie): Menu-bar app with playback controls and media-key integration. Useful if you also want an occasional clickable interface.
- [Raycast cmus scripts](https://github.com/raycast/script-commands/tree/master/commands/media/cmus): Existing actions for play/pause, previous/next, shuffle, repeat, and track information. Useful when Raycast is already part of your workflow.
- [music-controls-bitbar](https://github.com/sebbas/music-controls-bitbar): Menu-bar controls. **Legacy compatibility constraint:** the README requires an older BitBar release and says later versions are unsupported.
- [cmus-airpods](https://github.com/samdmarshall/cmus-airpods): Older agent responding to AirPods events through `cmus-remote`. An interesting integration example, although dated.
- [CMusRemote](https://github.com/moonwave99/CMusRemote): Older graphical remote with seeking, volume, and Apple Remote support.
- [itunes_notify.c](https://github.com/cmus/cmus/wiki/itunes_notify.c): Historical bridge sending cmus updates to applications expecting iTunes notifications.
- [SketchyBar](https://github.com/FelixKratz/SketchyBar): Building block for a custom now-playing item. You would connect it to `cmus-remote` or a status hook yourself; this is not a ready-made cmus plugin.

Older Mac instructions often hard-code `/usr/local/bin`. Adapt those paths to the actual location of `cmus-remote` on your machine, particularly with Apple Silicon Homebrew.

## Visualizers and artwork colors

A visualizer needs an audio source, while an artwork display needs an image. They are separate problems even when screenshots make them look like one application. Get capture working before spending time matching colors and pane sizes.

- [CAVA](https://github.com/karlstav/cava): Spectrum bars for a terminal or SDL window. Works alongside cmus by capturing audio. A strong choice for a small pane beneath the player.
- [spectroterm](https://github.com/sparklost/spectroterm): Terminal analyzer with axes, peak markers, configurable frequency ranges, colors, and PipeWire/PulseAudio support. Useful when you want more control over the spectrum display.
- [roistaff/cmus-plugins](https://github.com/roistaff/cmus-plugins): Artwork integration with a CAVA setup whose bar colors change with the cover. Useful as an example of tying visual components together.
- [cmus-visualizer](https://github.com/AlBurns-MSFT/cmus-visualizer): Older visualization experiment to inspect as an implementation reference.
- [cmusfetcher500](https://github.com/CreativeCodeCat/cmusfetcher500): Launches CAVA and feh alongside cmus. Useful for understanding a simple multi-program launcher.
- [BlackHole](https://github.com/ExistentialAudio/BlackHole): macOS loopback driver for routing audio between applications when your capture setup needs it.

> [!NOTE] Current CAVA capture on macOS
> CAVA documents direct system-output capture on macOS 14.2+ when built with CoreAudio tap support. Older builds or systems may need a loopback device. Check the [CAVA capture documentation](https://github.com/karlstav/cava#macos-2) before following older routing tutorials.

## Scrobbling and listening history

An online scrobbler submits listening history to a service. A local logger stores events or plays for your own analysis. Choose based on whether you want a public profile, recommendations, private statistics, or a combination.

- [cmusfm](https://github.com/arkq/cmusfm): C scrobbler with now-playing updates, offline caching, configurable services, filename parsing, and optional notifications. Good when you want a dedicated, compact scrobbling tool.
- [cmus-status-scrobbler](https://github.com/vjeranc/cmus-status-scrobbler): Python 3 tool supporting multiple services, offline storage, MusicBrainz IDs, and pause handling. Its author uses it with Last.fm, Libre.fm, and ListenBrainz. Useful for submitting to more than one service through one companion.
- [ListenBrainz integration directory](https://listenbrainz.org/add-data/): ListenBrainz itself lists cmus-status-scrobbler as a cmus integration.
- [lolfm](https://github.com/jimd1989/lolfm): Local SQLite listening-history database with loved tracks, SQL analysis, reporting helpers, and historical Last.fm import notes. Best suited to someone comfortable querying their own data.
- [cmus_music_monitor](https://github.com/cmus/cmus/wiki/cmus_music_monitor): Logs listening metadata to CSV. **Historical:** the page recommends a Rust replacement, but the linked replacement and graphing repositories returned 404 during research.
- [ListenBrainz shell-submitter discussion](https://community.metabrainz.org/t/checking-minimal-json-submission/723460): Author's shell implementation with MusicBrainz recording IDs and offline logging. A useful small example if you want to understand the API rather than adopt a full tool.
- [cmuscrobbler](https://github.com/freshprince/cmuscrobbler): Older Python scrobbler, explicitly marked unmaintained.
- [cmus_lastfmsubmit](https://github.com/cmus/cmus/wiki/cmus_lastfmsubmit): Historical bridge to `lastfmsubmitd`.
- [cmus2mysql](https://github.com/tuxfrickler/cmus2mysql): Older implementation recording playback to MySQL.

If you enable two scrobblers that both submit to the same service, check their destinations to avoid duplicate submissions. A local logger alongside one online scrobbler serves a different purpose and can be useful.

## Recommendations and dynamic playlists

These tools generally select from music you already have. A recommendation match does not automatically mean the audio will be downloaded. Consistent artist and title tags improve the chances of matching recommendations to local tracks.

- [cmus_lastfm_autoadd](https://github.com/weisslj/cmus_lastfm_autoadd): Fills the playlist or queue with similar tracks using Last.fm information. Useful for continuing from a song without choosing every next track yourself.
- [cmus-dynamiclistfm](https://github.com/guxsousa/cmus-dynamiclistfm): Builds playlists from a seed song or playlist, matches against the local library, and lets you choose playlist size.
- [cmus-shuffled-albums](https://github.com/kidsil/cmus-shuffled-albums): Generates a playlist containing a limited number of randomly selected complete albums. Useful for making a finite listening session.
- [cmus-album-shuffle](https://github.com/mjc-506/cmus-album-shuffle): Historical implementation. Current cmus has native library album shuffle, so inspect this for its code or a different workflow rather than assuming it is necessary.
- [beets Smart Playlist](https://beets.readthedocs.io/en/stable/plugins/smartplaylist.html): Generates playlist files from metadata queries. Useful for automatically maintained genre, decade, artist, or other collections.

## Fuzzy search and editor integration

The biggest benefit of these tools is access from wherever you are working. A small picker can select a song without switching to the full player. File-manager integrations are better when you think in folders and albums rather than tags.

- [cmus-fzf](https://github.com/itsjfx/cmus-fzf): Fuzzy selection from your cmus library. Includes cmus and tmux-popup configurations. Particularly useful for searching while another application has focus inside tmux.
- [rofi-cmus](https://github.com/vojdel/rofi-cmus): Rofi frontend for selecting music without opening the full cmus interface.
- [ranger-cmus](https://github.com/maximtrp/ranger-cmus): Adds commands to play files or folders, add them to the library, or enqueue them. Works naturally with ranger's marked selections.
- [nnn's cmusq plugin](https://github.com/jarun/nnn/blob/master/plugins/cmusq): Sends files and directories from nnn into cmus.
- [vim-cmus](https://github.com/azadkuh/vim-cmus): Controls the player directly from Vim.
- [cmus-remote-vim](https://github.com/professorsloth/cmus-remote-vim): Another older collection of Vim control functions.
- [unite-cmus](https://github.com/KabbAmine/unite-cmus): Integration for the older Unite.vim interface. Mainly relevant if you already use Unite.
- [player.nvim](https://github.com/alexxGmZ/player.nvim): Neovim controls through playerctl/MPRIS, with cmus among configurable players. Useful if you also control other media players from the editor.
- [cmus.nvim](https://github.com/cmus-enjoyers/cmus.nvim): Dedicated Neovim project whose README labels it **WIP**.
- [fish-cmus-utils](https://github.com/fzuellich/fish-cmus-utils): Fish helper providing a playback-toggle function.
- [blayc](https://github.com/gontoblez/blayc): Script for interacting with cmus without switching to its window.
- [FZF snippets gist](https://gist.github.com/igemnace/9b6fb8c2885c3e35299b3a122e1009e5): Includes a music picker and aliases. Treat it as a starting point and adapt quoting and filename handling.

## tmux and persistent playback

cmus is an interactive terminal application. tmux or screen gives it a persistent terminal session, so closing a viewing window need not end the player. It also gives lyrics, artwork, and visualization a stable home.

- [Detachable cmus guide](https://github.com/cmus/cmus/wiki/detachable-cmus): tmux and screen approaches, including changing `q` into a detach action.
- [Mpdreamz/tmux-cmus](https://github.com/Mpdreamz/tmux-cmus): Status widget with truncation and playback keybindings. Older project with macOS examples.
- [tmux-cmus-status](https://github.com/JenGoldstrich/tmux-cmus-status): Separate fields for artist, title, and playback state, plus F7/F8/F9 controls. Documents testing on Mac and Linux.
- [tmux-player-ctl](https://github.com/kesor/tmux-player-ctl): Popup controller for MPRIS players using playerctl. Includes progress, seeking, volume, player switching, shuffle, and repeat.
- [cmus_daemon](https://github.com/ichier/cmus_daemon): Wraps cmus and the older web app in screen, with startup/service support.
- [cmus-auto-lyrics launcher examples](https://github.com/sparklost/cmus-auto-lyrics#launcher): Ready-made split-pane layouts for the player and lyrics.
- [cmus-fzf popup examples](https://github.com/itsjfx/cmus-fzf#tmux-popup): Search from a popup inside another application.

For a first layout, use a large cmus pane and one narrow companion pane. Add a visualizer below them only after checking that image rendering and resizing behave correctly in your terminal.

## Notifications and status output

Several unrelated projects use the name `cmus-notify`. The repository owner identifies which one is meant. Most Linux notification projects expect a desktop notification service, so they are not automatically native macOS notification solutions.

- [dcx86r/cmus-notify](https://github.com/dcx86r/cmus-notify): Configurable Perl and notify-send implementation, with optional artwork and Dunst-related settings.
- [AntoineGagne/cmus-notify](https://github.com/AntoineGagne/cmus-notify): Python notification program.
- [mathieu-lemay/cmus-notify](https://github.com/mathieu-lemay/cmus-notify): Small Rust application supporting local cover images.
- [0x61nas/cmus-notify](https://github.com/0x61nas/cmus-notify): Rust implementation covering track, status, volume, and playing-mode changes. README explicitly describes it as early-stage.
- [cmushnotify](https://github.com/Dimithrandir/cmushnotify): Shell notifications with artwork.
- [CmusNotify](https://github.com/sebojanko/CmusNotify): Go implementation for now-playing notifications.
- [VonHeikemen/cmus-notify](https://github.com/VonHeikemen/cmus-notify): Lightweight notify-send script.
- [cmus_notify.py gist](https://gist.github.com/EmmaSimon/a617df1b86c558162e4c934ff65cebe1): GNOME notifications with artwork and control buttons.
- [cmus-status-line](https://github.com/Noah2610/cmus-status-line): Configurable playback information written to stdout, including progress formatting. Useful as input to bars, prompts, and scripts.
- [cmusd](https://github.com/miraclx/cmusd): Older Node.js companion providing desktop media integration, artwork, and controls.
- [cmustify](https://github.com/kimond/cmustify): Older status/notification experiment. Related versions exist in [Python](https://github.com/kimond/pycmustify), [Go](https://github.com/kimond/go-cmustify), and [Rust](https://github.com/kimond/rust_cmustify). Useful for comparing implementations rather than installing all of them.

## Linux panels and MPRIS

MPRIS is useful when you want one media-control system across the desktop. A panel, keyboard shortcut, and lyrics tool can all consume the same interface. Direct cmus scripts remain useful when you need cmus-specific library or queue operations.

- [playerctl](https://github.com/altdesktop/playerctl): General media-control CLI. Desktop shortcuts and scripts can use it to control cmus and retrieve metadata.
- [go-playerctl](https://github.com/arran4/go-playerctl): Go implementation with CLI, library, daemon, and TUI components.
- [polybar-cmus](https://github.com/raytruong/polybar-cmus): Status script for Polybar.
- [cmus-polybar](https://github.com/the-anonymous-raven/cmus-polybar): Alternative module with progress indicators.
- [go-cmus-polybar-status](https://github.com/ma3ke/go-cmus-polybar-status): Go formatter showing playback, title, and progress.
- [cmus-waybar](https://github.com/imagineeeinc/cmus-waybar): Small Nim helper producing current-track information for Waybar.
- [py3status cmus module](https://ultrabug.github.io/py3status/user-guide/modules/#cmus): Existing module with formatting and mouse controls.
- [gnome-cmus-status](https://github.com/GregTheMadMonk/gnome-cmus-status): GNOME Shell extension for display and control. Check compatibility with your Shell version.
- [xsetcmus.sh](https://github.com/ronno/scripts/blob/master/xsetcmus.sh): Track information suitable for a dwm status bar.
- [stumpwm-cmus](https://github.com/jdfight/stumpwm-cmus): StumpWM module.
- [Awesome widget example](https://github.com/cmus/cmus/wiki/Awesome-DM-widget): Historical Awesome WM integration.
- [nblock/cmus-notify](https://github.com/nblock/cmus-notify): Sends status into Awesome through `awesome-client`.

MPRIS requires a cmus build with that support. The configuration flag cannot add a feature omitted at build time. See the [manual](https://github.com/cmus/cmus/blob/master/Doc/cmus.txt).

## Discord and chat integration

These companions publish the current track to Discord Rich Presence. Differences include artwork sources, custom text, timing, and supported runtimes. Pick one provider so that multiple programs do not compete to update the same presence.

### Starting candidates

- [cmus-rpc-py](https://github.com/sparklost/cmus-rpc-py): Progress, configurable text, artwork from Last.fm or MusicBrainz, buttons, filename parsing, and update controls. Useful if you want to customize the presentation.
- [Bond-009/cmus-discord-rpc](https://github.com/Bond-009/cmus-discord-rpc): Rust implementation dedicated to cmus.
- [discordrp-mpris](https://github.com/FichteFoll/discordrp-mpris): Generic MPRIS integration. Useful if you want one companion for several players.
- [cmus-rpc-c](https://github.com/ZirixCZ/cmus-rpc-c): C implementation using the Discord Game SDK.

### Additional implementations

- [mesalilac/cmus-rpc](https://github.com/mesalilac/cmus-rpc): Rust implementation.
- [pascalpuffke/cmus-rich-presence](https://github.com/pascalpuffke/cmus-rich-presence): Standalone provider.
- [pascalpuffke/cmusrp-rust](https://github.com/pascalpuffke/cmusrp-rust): Separate Rust implementation.
- [YellowCoat1/cmus-drp](https://github.com/YellowCoat1/cmus-drp): Small Rust provider.
- [FawkesOficial/cmus-discord-rpc](https://github.com/FawkesOficial/cmus-discord-rpc): Python client.
- [Scallion3008/cmus-discord-rich-presence](https://github.com/Scallion3008/cmus-discord-rich-presence): Another dedicated implementation.
- [saibakho/cmrpc](https://github.com/saibakho/cmrpc): Additional cmus Discord RPC project.
- [0x61nas/cmus-rpc-rs](https://github.com/0x61nas/cmus-rpc-rs): Archived Rust implementation.
- [0x61nas/cmus-rpc](https://github.com/0x61nas/cmus-rpc): Archived Java implementation.
- [cmus_hexchat](https://github.com/S0yKaf/cmus_hexchat): Older HexChat plugin for controlling cmus, a different use of chat integration.

## Web remotes and Android

A web remote changes playback on the computer running cmus. An Android port runs the player on the phone itself. An Android remote app controls another machine. These are different capabilities, even though their project names can look similar.

- [cmus-web](https://github.com/FawkesOficial/cmus-web): Newer self-hosted browser/PWA remote with live updates, seeking, volume, artwork, and keyboard shortcuts. PWA installation requires HTTPS; the regular browser interface works on a LAN.
- [ichier/cmus_app](https://github.com/ichier/cmus_app): Fork of the older Bottle-based web remote.
- [Original cmus_app](https://github.com/jboynyc/cmus_app): Archived original. Its README directs readers to the fork above.
- [cmus-lan-control](https://jasonwoof.com/gitweb/?p=cmus-lan-control.git;a=summary): Older LAN interface for playback and queue operations.
- [cmus-android-remote](https://github.com/jatwigg/cmus-android-remote): Older Android remote-control app.
- [CmusRemoteAndroid](https://github.com/kalenpw/CmusRemoteAndroid): Another Android remote.
- [cmus-droid-remote](https://github.com/seriousben/cmus-droid-remote): Archived Android remote implementation.
- [Tosh](https://github.com/qrti/tosh): Touch overlay for terminal applications, demonstrated as a Raspberry Pi cmus player. Useful inspiration for a dedicated music appliance.
- [cmus-android](https://github.com/pgaskin/cmus-android): Actual Android port with touch controls, artwork, system media integration, sleep timer, and state management. Requires Android 14+.
- [cmus-notifier for Termux](https://gitlab.com/castluno/cmus-notifier): Notification controls for cmus in Termux. Its GitHub repository points to this GitLab location.

> [!WARNING] Native TCP control
> The upstream manual explicitly warns that cmus's native TCP control interface is insecure even with a password. For control across untrusted networks, use an SSH-based arrangement rather than exposing that port. A web frontend also needs its own access configuration. [Upstream warning](https://github.com/cmus/cmus/blob/master/Doc/cmus.txt)

## Music and playlist synchronization

Sharing a playlist alone does not necessarily share the audio, and absolute paths can differ between devices. Tools in this section help bridge those gaps. For portable libraries, keep directory structure and exported paths in mind.

- [cmus-syncthing](https://github.com/Kaleb0x/cmus-syncthing): Exports playlists and corresponding tracks into a directory that Syncthing can transfer. Supports exclusions and includes scheduling examples. Useful for sending selected listening material to a phone.
- [cmus-sync](https://github.com/samhal/cmus-sync): Older playlist-driven device synchronization script. Documents limitations around music spanning multiple library roots.
- [beets-cmusupdate](https://github.com/natezb/beets-cmusupdate): Adds newly imported beets tracks to the cmus library. Older plugin, so check compatibility with your beets version.
- [beets Play plugin](https://beets.readthedocs.io/en/stable/plugins/play.html): Passes query results to a configurable player command as a playlist or file arguments. Useful for connecting beets searches to cmus.

## Library cleanup and audio processing

These are companion utilities rather than cmus plugins. Improving the files can fix several problems at once: incorrect album grouping, missing artwork, inaccurate lyric matches, and uneven loudness.

- [beets](https://beets.readthedocs.io/en/stable/): Organizes files, corrects metadata, and provides a searchable music database. A strong foundation for a larger local collection.
- [beets FetchArt](https://beets.readthedocs.io/en/stable/plugins/fetchart.html): Downloads album artwork. Useful for companions expecting an image beside the music.
- [beets EmbedArt](https://beets.readthedocs.io/en/stable/plugins/embedart.html): Embeds artwork in audio files, so the art can travel with individual tracks.
- [beets Lyrics](https://beets.readthedocs.io/en/stable/plugins/lyrics.html): Fetches lyrics into tags for compatible companions to display.
- [beets ReplayGain](https://beets.readthedocs.io/en/stable/plugins/replaygain.html): Calculates loudness metadata for playback adjustment in cmus.
- [beets Duplicates](https://beets.readthedocs.io/en/stable/plugins/duplicates.html): Finds duplicate tracks or albums. Useful when imports from several sources have accumulated.
- [beets Smart Playlist](https://beets.readthedocs.io/en/stable/plugins/smartplaylist.html): Maintains playlist files from library queries.
- [MusicBrainz Picard](https://picard.musicbrainz.org/): Graphical tagger using MusicBrainz. Useful for correcting release identity, compilation grouping, and inconsistent tags.
- [rsgain](https://github.com/complexlogic/rsgain): Dedicated ReplayGain 2.0 scanner and tagger. An option when you want loudness tagging without adopting a full library manager.
- [EasyEffects](https://github.com/wwmm/easyeffects): Linux/PipeWire equalizer, limiter, convolver, compressor, and more. Processes cmus output through the audio system.
- [qpwgraph](https://github.com/rncbc/qpwgraph): Graphical PipeWire routing. Useful for connecting playback to processing or capture applications.
- [BlackHole](https://github.com/ExistentialAudio/BlackHole): macOS loopback driver for routing sound between applications.

ReplayGain metadata and an equalizer solve different problems. ReplayGain helps control loudness differences between recordings. An equalizer changes frequency balance. Neither requires replacing cmus.

## Themes and terminal appearance

Choose a theme that remains readable in selected, inactive, search, queue, and playlist states. Matching a screenshot's colors is less useful if your actual terminal palette makes the active row hard to distinguish.

- [johnnymatthews/cmus-themes](https://github.com/johnnymatthews/cmus-themes): Broad collection with screenshots and installation instructions. Includes Gruvbox variants, Dracula, Solarized, Tokyo Night, and others. A good first place to compare appearances.
- [Bundled cmus themes](https://github.com/cmus/cmus/tree/master): Inspect the shipped `.theme` files before adding more dependencies.
- [Catppuccin discussion and variants](https://github.com/catppuccin/catppuccin/discussions/1954): Community port discussion, including a variant intended to match Catppuccin CAVA colors.
- [Sekki21956/cmus](https://github.com/Sekki21956/cmus): Early Catppuccin theme.
- [BXn4/cmus](https://github.com/BXn4/cmus): Another Catppuccin implementation.
- [cmus-tokyo-night](https://github.com/ttntm/cmus-tokyo-night): Tokyo Night theme.
- [cmus-kanagawa](https://github.com/ttntm/cmus-kanagawa): Kanagawa theme.
- [egel/cmus-gruvbox](https://github.com/egel/cmus-gruvbox): Gruvbox port.
- [Gruvbox-goodies](https://github.com/thriveth/Gruvbox-goodies): Includes a subdued Gruvbox-night theme.
- [ghosty141/gruvbox-for-cmus](https://github.com/ghosty141/gruvbox-for-cmus): Another Gruvbox interpretation.
- [Poroing/gruvbox-cmus-theme](https://github.com/Poroing/gruvbox-cmus-theme): Additional Gruvbox variant.
- [e-ink.cmus](https://github.com/e-ink-colorscheme/e-ink.cmus): Grayscale themes with light, dark, and transparent variants. Useful if you prefer contrast without colorful decoration.
- [typewriter-cmus](https://github.com/logico/typewriter-cmus): Minimal theme from a coordinated application suite.
- [Atomic](https://github.com/gerardbm/atomic): Matching themes for cmus, terminals, Vim-related tools, and other applications.
- [colorcli](https://github.com/j15k/colorcli): Coordinated light themes for cmus, tmux, Vim, Mutt, and more.
- [base16-cmus](https://github.com/averms/base16-cmus): Base16 implementation.
- [cmus-base16](https://github.com/drewvanstone/cmus-base16): Separate Base16 implementation.
- [cmus-nordic_theme](https://github.com/ShrekhavingabadDay/cmus-nordic_theme): Nordic-inspired colors.
- [Pantheon Terminal themes](https://github.com/SubhadeepJasu/CMUS-themes-pantheon-terminal): Themes matching elementary OS's terminal.
- [cmus-theme-screenshot](https://github.com/alextercete/cmus-theme-screenshot): Recreates an older official screenshot.
- [Solarized-derived readability theme](https://gist.github.com/giobyte8/257ccbd627ac41a25711): Focuses on brightness and contrast rather than relying heavily on color distinctions.
- [Iorvethe/cmus](https://github.com/Iorvethe/cmus): Standalone colorscheme.

Place theme files in the cmus configuration directory and select one with `:colorscheme NAME`. See the [theme instructions](https://github.com/cmus/cmus/wiki/themes).

## Complete setups and dotfiles

These repositories show the surrounding environment as well as the player. Borrow a specific layout, script, or configuration idea instead of assuming the whole environment will match your computer.

- [at8i/cmus-setup](https://github.com/at8i/cmus-setup): Ubuntu-oriented combination of lyrics, artwork fetching/display, and tag editing. Useful as an end-to-end example, although several components and paths are dated.
- [gerardbm/dotfiles](https://github.com/gerardbm/dotfiles): cmus inside a coordinated i3, terminal, shell, and Atomic-theme environment.
- [fortes/dotfiles](https://github.com/fortes/dotfiles): Historical cmus lead. A later inspection found MPD/rmpc configurations in the current tree rather than the older cmus setup advertised by discovery results. See [the setup catalog](setups.md) for current cmus examples.
- [bardisty/dotfiles](https://github.com/bardisty/dotfiles): Includes beets, cmus, Dunst, i3, ranger, Rofi, and shell configuration. Useful for seeing library preparation and desktop controls together.
- [Cybersnake223/Hypr](https://github.com/Cybersnake223/Hypr): Hyprland environment with cmus, CAVA, and other components.
- [ahloiscreamo/Illit](https://github.com/ahloiscreamo/Illit): i3 setup with a coordinated Rosé Pine appearance.
- [FrenzyExists/Nord-dotfiles-i3](https://github.com/FrenzyExists/Nord-dotfiles-i3): Nord-themed i3 environment including cmus.
- [dfmgr/cmus](https://github.com/dfmgr/cmus): Dedicated configuration repository.

## Small hacks and scripts

These are useful examples of how little code is needed to change a workflow. Some solve problems now covered by native commands, but the implementations still show how to query state, manipulate a queue, and invoke external programs.

- [cmus bookmark script](https://github.com/cmus/cmus/wiki/cmus%E2%80%90bookmark): Saves and restores positions for individual files. Useful for long recordings and audiobooks, where one global resume position is not enough.
- [cmus_edit_tags](https://github.com/cmus/cmus/wiki/cmus_edit_tags): Passes the selected track to an external tag editor. Adapt the editor command to a tool you actually use.
- [cmus_randomize_queue](https://github.com/cmus/cmus/wiki/cmus_randomize_queue): Dumps, shuffles, and rebuilds the queue. Includes discussion of duplicate handling.
- [cmus_queue_bottom_top](https://github.com/cmus/cmus/wiki/cmus_queue_bottom_top): Moves the last queued item to the front.
- [cmus_enqueue_randomly](https://github.com/cmus/cmus/wiki/cmus_enqueue_randomly): Enqueues selected tracks or albums in randomized order.
- [cmus_format](https://github.com/cmus/cmus/wiki/cmus_format): Changes related display-format settings together.
- [cmus_follow_playback](https://github.com/cmus/cmus/wiki/cmus_follow_playback): Historical hook for following the current track. Compare with native `follow` behavior first.
- [cmus_play_next_album](https://github.com/cmus/cmus/wiki/cmus_play_next_album): Historical album-skipping implementation. Current cmus provides album-navigation commands.
- [cmus-base-plugins](https://github.com/cmus-plugins/cmus-base-plugins): Packages several wiki scripts together.

### Combining status hooks

Use a wrapper when multiple programs need the status arguments. This is a pattern to adapt, with placeholder paths:

```sh
#!/bin/sh

/absolute/path/to/scrobbler "$@" &
/absolute/path/to/artwork-helper "$@" &
wait
```

Configure cmus to call the wrapper, rather than configuring each companion as the sole hook. Follow each tool's own invocation instructions. The background pattern is suitable for independent, short-lived handlers; a long-running viewer usually needs a different startup arrangement. See the [wiki's combination example](https://github.com/cmus/cmus/wiki/status-display-programs#usage--installation).

### Useful remote commands

Run these from a shell while cmus is running:

```sh
cmus-remote -u                      # Toggle pause
cmus-remote -n                      # Next track
cmus-remote -r                      # Previous track
cmus-remote -Q                      # Status and metadata
cmus-remote -q "/path/to/song.flac"  # Add to queue
```

These can become launcher actions, shell functions, or desktop shortcuts. Quote paths so filenames containing spaces remain one argument. See the [remote manual](https://github.com/cmus/cmus/blob/master/Doc/cmus-remote.txt).

## Downloads streams and source patches

Distinguish preparing local audio files from adding native streaming-service playback. Most projects below download files or wrap an external downloader. They do not make cmus a full client for the originating service.

- [yt-dlp](https://github.com/yt-dlp/yt-dlp): External downloader that can prepare audio for the library. A shell wrapper can connect downloading and adding files without modifying cmus itself.
- [invicnaper/cmus-youtube](https://github.com/invicnaper/cmus-youtube): Older source patch adding a `:youtube` command. Useful as a source-code extension example.
- [viatatribal/cmus-youtube](https://github.com/viatatribal/cmus-youtube): Later patch using yt-dlp to download audio and add it to cmus.
- [invicnaper/spotify-dl](https://github.com/invicnaper/spotify-dl): Historical tool reading Spotify metadata and finding matching audio on YouTube. Does not download original Spotify audio.
- [Tidal-Media-Downloader](https://github.com/yaronzz/Tidal-Media-Downloader): External downloader linked by the wiki. Prepares local files rather than adding native Tidal playback.
- [Native stream and playlist support](https://cmus.github.io/): cmus supports internet-radio-style streams and playlist files. A station playlist may be enough for a personal radio collection.

Source patches target particular revisions. Their existence does not establish that they apply cleanly to cmus 2.13. For a personal setup, an external wrapper is often easier to keep separate from player upgrades.

## Libraries plugins and implementation references

This section is for building your own integration or understanding how existing companions work. A socket library can make structured queries easier, while a shell call to `cmus-remote` is often enough for a small shortcut.

- [cmus-plugin-vgm](https://github.com/jpcima/cmus-plugin-vgm): Actual input plugin adding VGM, VGZ, DRO, and S98 video-game-music formats. Different from an ordinary UI companion because it extends audio decoding.
- [pycmus](https://github.com/mtreinish/pycmus): Python library using the same socket interface as `cmus-remote`.
- [cmus-status Rust crate](https://github.com/abigailsdev/cmus-status): Converts status-hook data into structured Rust data.
- [stewart/cmus](https://github.com/stewart/cmus): Go package for interacting with the player.
- [ruby-cmus](https://github.com/meh/ruby-cmus): Older Ruby controller.
- [cmus-client-cpp](https://github.com/ywh233/cmus-client-cpp): C++ remote-control client.
- [cmus-bundler](https://github.com/nogizhopaboroda/cmus-bundler): Older Node.js plugin/theme manager with a daemon and bundle mechanism. Interesting architecture, but dependencies and examples are dated.
- [cmus-mediakeys](https://github.com/nogizhopaboroda/cmus-mediakeys): Older Node.js media-key integration. README documents very old Node compatibility problems.
- [pgaskin's development fork](https://github.com/pgaskin/cmus): Development, packaging, and PR-testing fork associated with a maintainer. Useful for following experiments rather than assuming it is the default release to install.
- [Upstream pull requests](https://github.com/cmus/cmus/pulls): Proposed features and patches before release.
- [Upstream discussions](https://github.com/cmus/cmus/discussions): Configuration questions, ideas, and community discussion.
- [Historical external patches](https://github.com/cmus/cmus/wiki/external-patches): Background on source-level extensions, including why an old scrobbling patch was not merged.

### Related independent players

These are separate implementations, not drop-in cmus plugins. They are included as references for alternate approaches to similar workflows.

- [CMUS++](https://github.com/Ars-byte/cmuspp): C++ terminal player with artwork, offline synchronized lyrics, and themes. Has its own behavior and configuration.
- [CMUS++ Qt](https://github.com/Ars-byte/Cmuspp-qt): Separate minimalist graphical player with covers and themes.
- [tap](https://github.com/timdubbins/tap): Rust terminal player inspired by cmus and fzf, with fuzzy library browsing.

## Blogs and practical guides

Older articles remain useful for architecture and workflow ideas, even when their package names, service APIs, or operating-system instructions have aged. Use the linked project documentation for current installation details.

- [Aaron Bieber: C Music Player Is My New Best Friend](https://blog.aaronbieber.com/2013/04/06/c-music-player-is-my-new-best-friend.html): tmux, iTerm2, Alfred shortcuts, notifications, and `cmus-remote`. Strong workflow article, although its Growl-era components are historical.
- [Christian Mayer: Control cmus with Media Keys](https://blog.fox21.at/2015/11/20/control-cmus-with-media-keys.html): Motivation and macOS integration behind cmus-control.
- [Cmus Album Art](https://www.atn34.com/posts/cmus-album-art.html): Combines beets artwork management with a hook changing the desktop background to the current cover. A good example of turning playback events into another desktop action.
- [Introduction Into FZF](https://msemjan.github.io/en/posts/introduction-into-fzf/): Includes music selection using fzf, tmux, and cmus. Useful for understanding the picker pattern rather than copying a whole desktop setup.
- [Getting cmus to cooperate with Conky](https://v3gard.com/2011/01/getting-cmus-to-cooperate-with-conky/): Connects status output to a desktop display.
- [cmus in Conky integrieren](https://blog.256bit.org/archives/714-cmus-in-conky-integrieren.html): German Conky integration article.
- [Johnny Matthews: CMUS config location](https://johnnymatthews.dev/blog/2020-08-28-cmus-config-location/): Short explanation of locating and customizing configuration.
- [Unixbhaskar: Linux tools for playing audio and video](https://unixbhaskar.wordpress.com/2023/08/05/): Personal settings and command-line playback workflow.
- [Using cmus for local music](https://www.robwood.uk/blog/cmus/): Playback modes and playlist usage. Search indexing was available, but a direct fetch returned an error during research.
- [iturdikulov's cmus notes](https://iturdikulov.com/cmus): Compact notes on views, navigation, modes, and playlists.
- [Minimal Tech: Music in the Terminal](https://cleac.me/minimal-tech.html): Personal cmus/tmux workflow and desktop integration discussion.
- [Nidarsh: CMus](https://nidarshr.wordpress.com/2017/10/03/cmus-is-amazing/): Introduction covering customization and extensions.
- [Termux, youtube-dl, and cmus](https://tungchingkai.blogspot.com/2021/01/202101.html): Historical Android terminal setup. Adapt it using current tool documentation.
- [Compiling cmus](https://www.shuangrimu.com/posts/compiling-cmus.html): Older personal build experience, useful as troubleshooting history.
- [Upstream review and article archive](https://github.com/cmus/cmus/wiki/reviews): More historical articles, including German, Spanish, Russian, and older Cygwin guidance.
- [cmus cheat sheet repository](https://github.com/nordic16/cmus-cheat-sheet): Quick command reference.
- [GitHub cmus topic](https://github.com/topics/cmus?o=desc&s=updated): Continuing discovery feed for companions, themes, dotfiles, and experiments. Useful for finding projects newer than this note.

## Putting a setup together

These are suggested assemblies from the catalog. They have not been tested as complete bundles.

### A comfortable macOS setup

1. Use a current cmus package and keep the remote command available to your scripts.
2. Keep cmus in a persistent tmux session.
3. Choose **cmus-control** for focused media-key support, or **cmusie** if you also want menu-bar controls.
4. Add **index-null/cmus-lyric** for fetched/local synchronized lyrics, or **cmus-liner** for a library prepared with embedded lyrics and cover files.
5. Use **cmus-fzf** for selecting tracks from a popup.
6. Use **beets** or **Picard** to improve metadata and artwork. Add loudness tags through beets ReplayGain or rsgain if needed.
7. Add **cmus-status-scrobbler** if you want Last.fm or ListenBrainz history.
8. Add **CAVA** after checking which capture method your installed build supports.

The main choice is how much you want inside the terminal. A native artwork or menu-bar app is reasonable even if cmus remains the main player.

### A Linux desktop setup

1. Run cmus in tmux and confirm that the build supports MPRIS.
2. Use **playerctl** for desktop media keys and shared media-control scripts.
3. Choose an existing Waybar, Polybar, or py3status integration for track information.
4. Add one lyrics companion and one artwork display if desired.
5. Use **CAVA** or **spectroterm** for visualization.
6. Add **EasyEffects** only if you want equalization or other audio processing.
7. Use a shared status wrapper for the short-lived companions that need it.

### A local-library-first setup

1. Correct the tags and directory structure with **beets** or **Picard**.
2. Store covers consistently and populate lyrics where useful.
3. Add ReplayGain tags for more consistent listening volume.
4. Build query-based playlists through **beets Smart Playlist**.
5. Add music through **beets-cmusupdate**, a file-manager integration, or your own remote-command wrapper.
6. Use **cmus-syncthing** if selected playlists and tracks should also be available on another device.

This approach improves the data used by every frontend: artwork viewers, lyrics matchers, recommendation tools, and scrobblers all benefit from a cleaner library.

### A small customization project

If none of the existing companions does exactly what you want, start with a short script around `cmus-remote`. Query the current metadata, format it for your destination, and trigger it from a keybinding or status hook. Move to a socket library only when a larger program needs structured state or tighter control.

Useful first projects include a launcher action, a menu-bar track label, a bookmark shortcut, or a command that queues an album chosen by another tool. The [Small hacks and scripts](#small-hacks-and-scripts) and [Libraries plugins and implementation references](#libraries-plugins-and-implementation-references) sections provide examples.
