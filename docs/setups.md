# cmus setups and configurations

**Research date:** November 6, 2026

**Related note:** [Ecosystem guide](ecosystem-guide.md)

Configurations, personal workflows, screenshots, and creator demonstrations that complement the [main resource list](../README.md).

> [!NOTE] How this was checked
> More than 30 repository trees were inspected, alongside actual config files, scripts, author write-ups, and screenshot posts. Direct GitHub config links are pinned to inspected commits where available. A file being present does not mean it has been tested on a current system. Screenshot-only and historical examples are labeled, and commented settings are distinguished from active ones.

## Navigation

- [Smarter workflows to inspect first](#smarter-workflows-to-inspect-first)
- [Visual setups and creator demonstrations](#visual-setups-and-creator-demonstrations)
- [Additional configs worth opening](#additional-configs-worth-opening)
- [More screenshot posts for visual inspiration](#more-screenshot-posts-for-visual-inspiration)
- [Small focused examples](#small-focused-examples)
- [Ideas worth borrowing](#ideas-worth-borrowing)
- [Historical leads that need care](#historical-leads-that-need-care)

## Smarter workflows to inspect first

### 1. itsjfx: fuzzy search and metadata popups

[Actual cmus rc](https://github.com/itsjfx/dotfiles/blob/b4e44e781cbc96c059c7e86264346566213368fd/.config/cmus/rc) · [Metadata helper](https://github.com/itsjfx/dotfiles/blob/b4e44e781cbc96c059c7e86264346566213368fd/lib/cmus-mediainfo.sh) · [cmus-fzf demo](https://github.com/itsjfx/cmus-fzf)

The rc binds S to a large fzf popup and I to a metadata popup for the selected track. It also uses smaller volume/seek steps, cmusfm, and a filter excluding CUE filenames. Borrow the idea of inspecting and choosing music without leaving your working pane. The CUE filter is that author's library preference, not a universal fix.

### 2. Waylon Walker: a persistent music popup

[tmux configuration](https://github.com/WaylonWalker/devtainer/blob/57d310f1394f0a4bc58207947e36f465372730a0/tmux/.tmux.conf)

The Alt+m binding checks whether you are in the music session, detaches when appropriate, and otherwise opens a large popup attached to a persistent session running cmus. Borrow the persistent-session model: closing a control surface should not have to stop playback. The file has surrounding personal bindings, so extract the relevant block.

### 3. gmoshkin: a music workstation with remote controls

[Pane launcher](https://github.com/gmoshkin/dotfiles/blob/2eb73bfc9e94dcb2002affeb98cbf52caf5bf5a9/scripts/start-cmus.sh) · [Control wrapper](https://github.com/gmoshkin/dotfiles/blob/2eb73bfc9e94dcb2002affeb98cbf52caf5bf5a9/scripts/cmus-rc.sh) · [Local/remote handler](https://github.com/gmoshkin/dotfiles/blob/2eb73bfc9e94dcb2002affeb98cbf52caf5bf5a9/tmux/cmus-remote)

The launcher builds a tmux layout with artwork and CAVA. Other scripts provide readable control commands, local/remote handling, and SSH-based volume handling. Borrow the separation of layout, state formatting, and control. Historical code uses machine-specific paths and native TCP options in places; do not mistake it for a modern, ready-to-deploy remote service.

### 4. sagotsky: browse albums through directory structure

[Directory-aware picker](https://github.com/sagotsky/.dotfiles/blob/75f912b41e4e39ec9727bc1e14f645e2aca98e83/home/scripts/cmus-filter.sh) · [Music command menu](https://github.com/sagotsky/.dotfiles/blob/75f912b41e4e39ec9727bc1e14f645e2aca98e83/home/scripts/music-remote.sh) · [Palette adaptation](https://github.com/sagotsky/.dotfiles/blob/75f912b41e4e39ec9727bc1e14f645e2aca98e83/home/scripts/palette_to_cmus.sh)

A dmenu/slmenu picker selects songs, artists, or albums based on a configurable directory hierarchy, with a random-selection mode. Separate scripts expose commands and apply palette colors to cmus. Borrow album-oriented selection and a reusable control menu. This is older code with its own helper dependencies, not a portable one-file install.

### 5. Thibault Marin: an album browser inside Awesome WM

[Annotated setup and implementation](https://thibaultmarin.github.io/blog/posts/2016-10-05-Awesome-wm_configuration.html)

A bar widget shows playback state and position, toggles playback, and raises cmus. Hovering shows an album track list and cover. A prompt can find an album by name or choose a random album. Borrow the album-preview interaction. The author explicitly documents assumptions about folder naming and embedded artwork.

### 6. pgaskin: a bar that is also a controller

[cmus module](https://github.com/pgaskin/barlib/blob/6443b7e0edf57a660fe35c5dc30edb395239fe79/i3status-custom/cmus.go) · [barlib repository](https://github.com/pgaskin/barlib)

The Go module connects to cmus through MPRIS, subscribes to D-Bus signals, and combines status display with seeking, volume, and window/scratchpad actions. Borrow event-driven updates and a compact controller that can reveal the full player. This is an implementation reference within the author's bar framework.

### 7. Maka8295: dungeonOS with an actual music control panel

[Full setup and screenshots](https://github.com/Maka8295/Dotfiles) · [Music panel](https://github.com/Maka8295/Dotfiles/blob/ba456862192a2968c19941cde10acc16549c1f65/scripts/music-panel.py) · [Scratchpad launcher](https://github.com/Maka8295/Dotfiles/blob/ba456862192a2968c19941cde10acc16549c1f65/scripts/scratchpad.sh) · [cmus theme](https://github.com/Maka8295/Dotfiles/blob/ba456862192a2968c19941cde10acc16549c1f65/cmus/dungeonOS.theme)

A dungeon-synth-inspired Hyprland environment with a coordinated cmus theme. Right-clicking its Waybar CAVA module opens a panel with track information, seeking, volume, playback, shuffle, and repeat. The scratchpad launcher waits for windows in order and skips existing ones. Borrow the useful control surface and predictable launch behavior, even if you do not want the whole desktop.

### 8. gotbletu: select several songs and build a queue

[Actual fzf script](https://github.com/gotbletu/shownotes/blob/d458da0c38bbbd8e6934827d260f3bd6a9272dc5/fzf_nova/_cmus) · [Surrounding shownotes](https://github.com/gotbletu/shownotes/tree/master/fzf_nova)

The script reads the saved library, uses fzf multi-selection, clears the existing queue, queues the choices, and starts playback. Borrow multi-select rather than a one-song-only picker. Its queue replacement is deliberate, so adapt that behavior if you want to append. The saved-library path is from an older cmus layout.

### 9. pyratebeard: random albums and weekly listening summaries

[cmus files](https://git.pyratebeard.net/dotfiles/files.html) · [Random-album helper](https://git.pyratebeard.net/dotfiles/file/cmus/.local/bin/ara.html) · [Status logger](https://git.pyratebeard.net/dotfiles/file/cmus/.config/cmus/cmus-status-display.html) · [Weekly summary script](https://git.pyratebeard.net/dotfiles/file/cmus/.local/bin/wmt.html)

The setup logs album or playlist activity through the status hook and includes a helper adding a chosen number of random album directories. It also contains weekly music-summary experiments. Borrow a finite album session and a local listening journal. The Python summary rewrite in the same repo queries Navidrome and has posting work marked TODO, so it is not evidence of a finished cmus auto-posting system.

### 10. ATN34: let the playing album change the desktop

[Personal setup write-up](https://www.atn34.com/posts/cmus-album-art.html)

Uses beets to establish predictable album directories and cover images, then connects a cmus status script to feh so the desktop background follows the playing album. Borrow preparation of artwork once, followed by a small playback hook. The script depends on the author's directory conventions.

### 11. Aaron Bieber: cmus as part of a Mac working environment

[Personal Mac workflow](https://blog.aaronbieber.com/2013/04/06/c-music-player-is-my-new-best-friend.html)

An older but clear example combining tmux, iTerm2, Alfred shortcuts, and notifications. Borrow global control without constantly switching windows. The Growl-era notification components are historical; use current Mac controls from the main ecosystem guide when adapting the idea.

## Visual setups and creator demonstrations

### 12. ahloiscreamo: Rose Pine Moon with artwork and Cavalier

[Workflow showcase](https://www.reddit.com/r/unixporn/comments/10jmuni/) · [Actual rc](https://github.com/ahloiscreamo/Illit/blob/a2c4d98526df23988ce5bdbca11c308da261ee56/config/cmus/rc) · [cmus reference images](https://github.com/ahloiscreamo/Illit/tree/a2c4d98526df23988ce5bdbca11c308da261ee56/config/cmus/ref) · [Waybar helper](https://github.com/ahloiscreamo/Illit/blob/a2c4d98526df23988ce5bdbca11c308da261ee56/config/waybar/scripts/cmus.sh)

The showcase identifies cmus, cmusCoversSDL, Cavalier, and Polybar. The surviving repo has custom row formatting, an album-focused sorting shortcut, notification glue, and a later Waybar script. Borrow the coordinated composition and formatting. The current repository contains configurations from different periods, so the old screenshot is not a promise of a single current install.

### 13. GideonWolfe: documented terminal music with progress output

[Music screenshot](https://github.com/GideonWolfe/dots/blob/4321a33f8e3324c1909c0f81788dc70fdd81317a/screenshots/cmus.png) · [Progress helper](https://github.com/GideonWolfe/dots/blob/4321a33f8e3324c1909c0f81788dc70fdd81317a/dotfiles/scripts/cmus-progress.sh) · [Polybar helper](https://github.com/GideonWolfe/dots/blob/4321a33f8e3324c1909c0f81788dc70fdd81317a/dotfiles/config/polybar/scripts/player-cmus.sh) · [Full environment](https://github.com/GideonWolfe/dots)

The repository provides a specific cmus screenshot rather than just listing the player as installed. Its progress helper converts playback position and duration into a configurable-length bar. Borrow the surrounding presentation or the small output component; the progress helper depends on another command named progress.

### 14. at8i: one launch for lyrics, covers, and tagging

[Full setup and preview](https://github.com/at8i/cmus-setup)

A complete Ubuntu-oriented example combining a player, artwork fetching/display, saved lyrics, and tag editing. Borrow the orchestration and pane/window arrangement. Its dependencies and paths are dated, so use it as a blueprint rather than a universal installer.

### 15. Vizkid04: Kitty artwork, tmux, and CAVA

[README and preview](https://github.com/Vizkid04/cmus_cover_art)

A concrete demonstration of cmus plus a Rust artwork helper, Kitty graphics, tmux sections, and CAVA. Borrow the pane proportions and separation of artwork extraction from display. The installation notes contain author-specific paths that need adaptation.

### 16. roistaff: CAVA colors follow the cover

[Demo and scripts](https://github.com/roistaff/cmus-plugins)

Artwork and visualization are coordinated so that CAVA's colors follow the album image. Borrow color extraction as a shared input for multiple visual components. This is a creator demonstration with scripts, not a general desktop configuration framework.

### 17. S22F5: cover rendering through Sixel or Kitty

[Demo and implementation](https://github.com/S22F5/cmus_sixel)

A compact cover-art integration demonstrating two terminal graphics approaches. Borrow the rendering method if you want the cover near the player without a separate image window. The terminal must support the chosen protocol.

### 18. emp1r3: a small POSIX shell artwork setup

[Screenshots and script](https://github.com/emp1r3/cmus-sixel)

Shows artwork using FFmpeg and img2sixel with a small shell helper. Borrow this if you prefer an implementation you can inspect quickly. It can also show the current cover independently of the full layout.

### 19. Oliver Hofkens: local lyrics and art alongside cmus

[Side-by-side screenshot and companion](https://github.com/OliverHofkens/cmus-liner)

A companion pane reads embedded lyrics and cover files, with selectable image styles. Borrow the offline-friendly arrangement: prepare tags and covers with library tools, then keep the viewer simple.

### 20. index-null: synchronized lyrics as a dedicated TUI

[Screenshots and project](https://github.com/index-null/cmus-lyric)

Shows a dedicated lyrics interface with synchronized scrolling, local/embedded lyrics, online fetching, and cover support. Borrow this if reading lyrics is part of the listening session rather than a small status-bar decoration. This is a companion demonstration, not someone's full desktop dotfiles.

## Additional configs worth opening

### 21. mrdotx: compact UI details and a Polybar hook

[Actual rc](https://github.com/mrdotx/dotfiles/blob/e88ad5156cbc0d63143dc6fb652a85cbe4d469d8/.config/cmus/rc) · [klassiker theme](https://github.com/mrdotx/dotfiles/blob/e88ad5156cbc0d63143dc6fb652a85cbe4d469d8/.config/cmus/klassiker.theme) · [Desktop screenshot](https://github.com/mrdotx/dotfiles/blob/e88ad5156cbc0d63143dc6fb652a85cbe4d469d8/screenshot.png)

Disables automatic expansion, enables mouse and resume, shows bitrate and remaining time, and calls a Polybar status script. The theme distinguishes current and inactive selections. Borrow the small usability choices, not just the palette.

### 22. gerardbm: Atomic colors with a deliberately small rc

[Setup and screenshots](https://github.com/gerardbm/dotfiles) · [Actual rc](https://github.com/gerardbm/dotfiles/blob/100ed2a9297fcb856d014e8c877dbf78759d7201/cmus/.config/cmus/rc) · [Atomic theme suite](https://github.com/gerardbm/atomic)

The cmus rc itself is minimal and enables software volume, while the README describes coordinated Atomic theming and Stow management. Borrow a small, maintainable player config inside a consistent terminal environment.

### 23. FrenzyExists: Nord notifications with matching cover wallpaper

[Screenshots](https://github.com/FrenzyExists/Nord-dotfiles-i3) · [Actual music hook](https://github.com/FrenzyExists/Nord-dotfiles-i3/blob/1314b8b06b242e9e2452f8ce34e8ead25cb73b0e/config/cmus/cmus_notify.sh)

The hook looks for artwork using album-artist and artist paths, sends a notification with the cover, and sets the background with feh. Borrow the fallback between compilation-aware and ordinary artist directories. The folder structure is specific to this setup.

### 24. Cybersnake223: Catppuccin inside a Hyprland environment

[Full environment](https://github.com/Cybersnake223/Hypr) · [Actual cmus files](https://github.com/Cybersnake223/Hypr/tree/e835336d697ca61d29cd72bb19910fb53bc9983e/.config/cmus)

Contains a Catppuccin theme and a saved player configuration in a larger Wayland desktop. Useful for coordinated appearance. The inspected status-hook field was empty, so do not infer a complex cmus backend from the surrounding desktop alone.

### 25. Cadesius: Forgotten Sands grayscale and Cuneiform symbols

[Showcase](https://www.reddit.com/r/unixporn/comments/r93ebq/) · [Actual cmus theme](https://github.com/Cadesius/Forgotten-Sands-Theme/blob/8a4e9b16d9ec9416c09f103d0aba3980c7b4b8be/cmus/full-greyscale.theme) · [Waybar reader](https://github.com/Cadesius/Forgotten-Sands-Theme/blob/8a4e9b16d9ec9416c09f103d0aba3980c7b4b8be/waybar/scripts/cmusreader.sh)

An unusually distinct grayscale setup using Cuneiform symbols in its desktop presentation. Borrow the restrained contrast and custom status symbols. The bar reader contains debugging output, so inspect it before using it unchanged.

### 26. bardisty: a library-management setup around cmus

[Player rc](https://github.com/bardisty/dotfiles/blob/751187e8ad76935181120ffc9fa667c98ae3aa8b/cmus/.config/cmus/rc) · [beets config](https://github.com/bardisty/dotfiles/blob/751187e8ad76935181120ffc9fa667c98ae3aa8b/beets/.config/beets/config.yaml)

The beets config includes artwork, metadata, duplicate, and playback plugins, with separate paths for albums, compilations, and soundtracks. The cmus rc mainly applies yellow/transparent styling; many other lines are commented examples. Borrow the organization of the library rather than treating every comment as active configuration.

### 27. mimame: Catppuccin plus structured imports

[Theme](https://github.com/mimame/.dotfiles/blob/5352122940316f62237af4776d021511332342e9/cmus/catppuccin.theme) · [beets configuration](https://github.com/mimame/.dotfiles/blob/5352122940316f62237af4776d021511332342e9/beets/config.yaml) · [Repository](https://github.com/mimame/.dotfiles)

Contains a cmus theme beside a beets setup with genre-oriented paths, fingerprinting, filename inference, and lyrics. Borrow the relationship between preparation and presentation. These files do not by themselves establish an automatic beets-to-cmus import bridge.

### 28. monoira: newest-file-first listening

[Actual rc](https://github.com/monoira/.dotfiles/blob/1389b65568899aa826cd15c19258913b1ebca1be/cmus/.config/cmus/rc)

Starts in sorted view, sorts by descending file modification time, displays titles simply, resumes, and follows playback. Borrow the idea of making newly added music easy to find. It also repeats the current track, which is a personal preference, and includes an older shuffle value to check against your cmus version.

### 29. sergii-dudar: Gruvbox with event-triggered bar refresh

[Player rc](https://github.com/sergii-dudar/dotfiles/blob/694682345381469d58bb4ea4031dcb681895d6c7/cmus/.config/cmus/rc) · [Music change notifier](https://github.com/sergii-dudar/dotfiles/blob/694682345381469d58bb4ea4031dcb681895d6c7/scripts/dwm/musicup) · [Full environment](https://github.com/sergii-dudar/dotfiles)

The active rc selects Gruvbox; many elaborate format settings are commented. A separate helper follows playerctl metadata and signals the status bar on updates, with MPD handling alongside it. Borrow the event-triggered bar refresh instead of repeatedly launching many metadata queries.

### 30. ssh0: notifications and custom colors

[cmus directory](https://github.com/ssh0/dotfiles/tree/c0c3acf1c21ecb74487e9ad7937fc4f8257d1fc4/cmus) · [Player rc](https://github.com/ssh0/dotfiles/blob/c0c3acf1c21ecb74487e9ad7937fc4f8257d1fc4/cmus/rc) · [Notification script](https://github.com/ssh0/dotfiles/blob/c0c3acf1c21ecb74487e9ad7937fc4f8257d1fc4/cmus/cmus_desktop_notify.py)

A preserved setup containing a custom theme, rc, status wrapper, and desktop-notification implementation. Useful for studying how the pieces are laid out. The notification script is old Python code, so it is a historical adaptation reference.

### 31. JD154: Fedora i3 music and notification glue

[Setup overview](https://github.com/JD154/fedora-dotfiles) · [cmus files](https://github.com/JD154/fedora-dotfiles/tree/5dd642587e1a060cffdd6816d547ce7687fe1234/cmus/.cmus)

An i3/Polybar environment listing cmus and CAVA, with actual notification scripts under the older .cmus layout. Borrow the desktop composition and hook arrangement while updating old package names and paths.

### 32. isfanafely: simple Sway integration and a refresh helper

[Screenshot](https://github.com/isfanafely/dotfiles/blob/548186a8fe13c646c07f4ea3f97ad175d5e7d8b8/screenshot/screenshot.png) · [Player files](https://github.com/isfanafely/dotfiles/tree/548186a8fe13c646c07f4ea3f97ad175d5e7d8b8/.config/cmus) · [Refresh helper](https://github.com/isfanafely/dotfiles/blob/548186a8fe13c646c07f4ea3f97ad175d5e7d8b8/.config/cmus/update.sh)

Includes Catppuccin, saved player settings, and a small helper that clears a view, adds the music directory, and forces a cache refresh. Useful as a simple scripting example. A clear-and-readd workflow is not the same as incremental library monitoring.

### 33. guisilvano: saved filters for browsing a collection

[Actual rc](https://github.com/guisilvano/dotfiles/blob/0c14fe2a118416c76fdb67f4c3845e33b93f1868/cmus/rc)

Defines filters for decades, classical music, unheard tracks, missing tags, and formats alongside familiar bindings. Borrow named filters as reusable views of a collection rather than continually rewriting search expressions.

### 34. jmiziolek: a tiny explicit library refresh

[Refresh script](https://github.com/jmiziolek/dotfiles/blob/f9894d78e88ffc0b73d538806ca4d7ba7d8bf4a8/cmus-refresh.sh)

A three-command refresh around the author's music location. Worth inspecting because it illustrates a small custom utility rather than a large plugin. Adapt its target directory and clearing behavior; it is not a file watcher.

## More screenshot posts for visual inspiration

### 35. river: Down by the Riverside

[Author's showcase](https://www.reddit.com/r/unixporn/comments/1781pcv/)

The author lists cmus plus lyrics-in-terminal, foot/Kitty, Waybar, and Tokyo Night. Useful for seeing the player as part of a Wayland workspace. Treat the post as a documented visual combination, not a verified current install recipe.

### 36. Qtile: daily desktop with a space cowboy

[Author's showcase](https://www.reddit.com/r/unixporn/comments/12m2qis/)

Lists cmus, clyrics, CAVA, Alacritty, and Doom Emacs. A direct example of player, lyrics, visualization, and work tools sharing one desktop.

### 37. Sway: immutable Gruvbox

[Author's showcase](https://www.reddit.com/r/unixporn/comments/1950xt1/)

A Fedora Sericea example listing cmus, CAVA, tmux, foot, and Waybar. Useful if you want a restrained combination of standard components instead of a large custom frontend.

### 38. dwm: fell into the void

[Author's showcase and comments](https://www.reddit.com/r/unixporn/comments/yt3wjq/)

Lists cmus with cli-visualizer in st on Void Linux. A useful detail in the comments: the artwork is a separate image window, not proof of an integrated cmus cover feature. Borrow the composition without misidentifying the implementation.

### 39. i3: No gaps, no eyestrain, just Gruvbox

[Showcase](https://www.reddit.com/r/unixporn/comments/emkwcv/) · [Author's linked dotfiles branch](https://github.com/mxdevmanuel/dotfiles/tree/desktop)

Kitty, Polybar, Gruvbox, and cmus inside tmux. Useful inspiration for a compact working desktop. The dotfiles link comes from the historical post and was not revalidated as a complete current setup.

### 40. XFCE: Solace in Everforest

[Author's showcase](https://www.reddit.com/r/unixporn/comments/1drsb06/)

The author lists cmus and lyrics-in-terminal within an Everforest Linux Mint/XFCE desktop. Useful as a palette and composition reference. The post also lists another player, so not every music element should be attributed to cmus.

### 41. OpenBSD cwm: a terminal-focused desktop

[Author's showcase](https://www.reddit.com/r/unixporn/comments/vqvfwa/)

Lists cmus with xterm, tmux, and ksh under cwm. Useful inspiration for a small BSD environment without relying on Linux desktop services.

### 42. BSPWM: My simple rice

[Author's showcase and source link](https://www.reddit.com/r/unixporn/comments/mf5g1a/)

Lists cmus in a BSPWM/Polybar desktop. The original sheeblou dotfiles endpoint returned a move response during this research, so use the post for the historical screenshot rather than assuming the old repo URL is a maintained recipe.

### 43. Euroblitz: a gallery of older personal desktops

[Gallery and author commentary](https://euroblitz.github.io/dotfiles.html)

Several personal desktop iterations, including an i3-gaps setup with cmus. Useful for visual comparison and for seeing how a setup evolves. The author explicitly describes the dotfiles as old.

### 44. SeniorMars: the 2020 rice as historical inspiration

[Repository and older setup screenshots](https://github.com/SeniorMars/dotfiles)

The README preserves an older terminal-heavy setup listing cmus, while also discussing a later Mac environment. The current inspected tree did not contain a dedicated cmus configuration. Keep this as historical visual inspiration, not a confirmed current cmus bundle.

## Small focused examples

### 45. Madacol: desktop shortcuts without a large framework

[Personal setup notes](https://madacol.com/blog/Cmus%20setup%20and%20shortcuts.html)

A concise list of desktop commands for opening cmus, controlling playback, and seeking. Useful if your goal is simply to make the player accessible from global shortcuts.

### 46. gontoblez: a tiny floating music query window

[blayc README](https://github.com/gontoblez/blayc)

Documents a Kitty/i3 floating window for querying music and handing playback to cmus. Borrow the tiny launcher surface. The README also documents filename limitations despite a broader feature claim, so treat the implementation as something to inspect and improve.

### 47. elairavi: a custom green cmus theme in a BSPWM environment

[Actual theme](https://github.com/elairavi/dotfiles/blob/592719a4bb35950fc62baa28ab1874adf6414018/.config/cmus/green-custom.theme) · [Full environment](https://github.com/elairavi/dotfiles)

A direct theme file to inspect when you want a personal variation rather than another named palette. The presence of a theme alone does not establish additional playback features.

### 48. igemnace: a terminal entertainment session

[Setup README](https://github.com/igemnace/dotfiles) · [cmus highlight theme](https://github.com/igemnace/dotfiles/blob/59a22fa25ea41540fca88b56e0c4034cdf7d3630/cfg/.config/cmus/highlight.theme)

The README includes an entertainment-session example using cmus and cli-visualizer, with a small cmus theme in the tree. Useful inspiration for keeping entertainment in a separate terminal session.

## Ideas worth borrowing

These are my suggested adaptations of the inspected setups, not claims that every author uses the same combination.

- **A player that appears on demand:** combine the persistent-session idea from Waylon Walker with the fuzzy picker from itsjfx. Keep music running while the control window opens and closes.
- **Select several tracks at once:** use gotbletu's queue-building idea, but decide explicitly whether a selection should replace or append to the queue.
- **An album-first workflow:** borrow directory-aware selection from sagotsky or album previews from Thibault Marin. This suits people who listen to releases rather than an endless shuffled track list.
- **A controller behind the visualizer:** Maka8295's panel makes the bar useful for seeking and volume, rather than purely decorative.
- **React to events:** pgaskin's D-Bus integration and sergii-dudar's playerctl follower show ways to update displays when state changes.
- **Prepare artwork once:** ATN34's beets arrangement makes downstream notifications, wallpapers, and viewers simpler.
- **Use one palette in several places:** coordinate the player, artwork frame, lyrics, and visualizer rather than adding unrelated themes.
- **Make the library's newest files easy to find:** monoira's descending file-time sort is a useful alternate starting view.
- **Save a listening journal:** pyratebeard's logger shows that a status hook can support later summaries without a permanent online profile.
- **Keep custom configuration small:** gerardbm's minimal rc is a useful reminder that a coherent setup does not require hundreds of changed bindings.

For a Mac, I would first borrow **itsjfx's popup workflow**, **Waylon Walker's persistent session**, and **ATN34's library preparation idea**, then pair them with one current Mac media-key handler from the main note. Linux-specific desktop scripts need adaptation.

## Historical leads that need care

- **fortes/dotfiles:** the current inspected tree contains MPD/rmpc configuration rather than the older cmus setup advertised by some search results. [Current repository](https://github.com/fortes/dotfiles).
- **newmanls/dotfiles:** its cmus topic/tag was not enough to establish a current cmus config; no cmus-named file appeared in the inspected tree. [Repository](https://github.com/newmanls/dotfiles).
- **egel/dotfiles:** current cmus-named files were not found in the inspected tree, despite older cmus-related discovery results. Its separate Gruvbox theme remains relevant in the main catalog. [Repository](https://github.com/egel/dotfiles).
- **Old saved state:** borrow settings from someone's `autosave` selectively. Their caches, playlists, histories, absolute paths, and credentials are not a reusable setup specification.
- **Old source or service assumptions:** Python 2 scripts, old terminal APIs, and native TCP control deserve adaptation. In particular, upstream warns against exposing cmus's native TCP interface to the internet. [Upstream manual](https://github.com/cmus/cmus/blob/master/Doc/cmus.txt).

A good borrowing order is: inspect the screenshot, read the relevant rc or script, identify its helper programs and paths, then adapt one useful behavior at a time.
