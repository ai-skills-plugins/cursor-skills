---
name: macos-hdmi-external-monitor
description: >-
  Diagnose and fix Apple Silicon MacBook Pro (14"/16" with built-in HDMI) when
  an external monitor is not detected. Use when HDMI/external display missing,
  WindowServer display plist wipe fails, HDMI_HPD-Debounced stuck at 0, LG/FHD
  monitor black or absent from System Settings Displays, or macOS Tahoe display
  handshake failures.
---

# macOS HDMI external monitor (Apple Silicon)

## Scope

- 14"/16" MacBook Pro with **built-in HDMI** (e.g. M1 Pro `MacBookPro18,3`)
- Symptom: external monitor not in Displays / `system_profiler SPDisplaysDataType`
- Prior fix `sudo rm /Library/Preferences/com.apple.windowserver.displays.plist` alone may **not** be enough

## Diagnose first

```bash
system_profiler SPDisplaysDataType
ioreg -l -w0 | grep -E 'HDMI_HPD|"ProductName" = '
```

| Finding | Meaning |
|---------|---------|
| Only built-in Online; `HDMI_HPD` = No | Cable/monitor/power/input — physical path |
| `HDMI_HPD` = Yes, ProductName present, `HDMI_HPD-Debounced` = **0** | Hotplug stuck — use **Fix (proven)** below |
| Debounced = 1 but still not Online | Prefs/WindowServer — wipe plists + kill WindowServer |
| Nothing on Thunderbolt buses and no HDMI port on model | Wrong assumption — needs USB-C adapter (13" Air/Pro) |

Do **not** conclude “no HDMI” on 14"/16" M-series Pro/Max — they have a dedicated HDMI port.

## Fix (proven) — Debounced stuck / plist wipe insufficient

Order matters. Needs sudo password.

1. **Unplug HDMI** from Mac. Unplug **power** from the monitor (not standby only).
2. Clear display prefs + display crossbar NVRAM:

```bash
sudo mv /Library/Preferences/com.apple.windowserver.displays.plist \
  /Library/Preferences/com.apple.windowserver.displays.plist.bak-cold

# zsh: nomatch-safe (active ByHost file may already be absent)
setopt NULL_GLOB
rm -f ~/Library/Preferences/ByHost/com.apple.windowserver.displays.*.plist
# leave .bak / .disabled / .pre-* alone unless restoring deliberately

sudo nvram -d display-crossbar0
```

3. **Shut Down** (Apple menu → Shut Down — not Restart). Wait **≥60s**.
4. Power on Mac with **HDMI disconnected**. Log in.
5. Power on monitor, select correct HDMI input, **then** plug HDMI into Mac.

### Verify

```bash
ioreg -l -w0 | grep -E 'HDMI_HPD|"ProductName" = '
system_profiler SPDisplaysDataType | grep -E 'Resolution|Online|Connection|LG|Display Type'
```

Success: `HDMI_HPD-Debounced` ≠ 0 (or display Online with external resolution). Prefer **60 Hz** if 100 Hz configs caused past issues (this machine had `pre-60hz-fix` backups).

## Weaker fixes (try only if Debounced already 1, or as first cheap attempt)

- Wipe system + ByHost windowserver displays plists → `sudo killall WindowServer` (logs out)
- System Settings → Displays → hold **Option** → Detect Displays
- Display sleep/wake alone does **not** clear Debounced = 0

## If Fix (proven) fails

- Different short Premium HDMI cable
- Other monitor HDMI input
- Bypass built-in HDMI: USB-C → HDMI adapter on a left USB-C port
- Fresh user account / Safe Mode to rule out login-item interference

## Agent notes

- ByHost glob `…displays.*.plist` errors with `no matches found` under zsh when already deleted — that is OK; continue.
- System plist regenerates quickly after login; wipe again immediately before cold shutdown if it reappeared.
- Do not require Thunderbolt device presence for built-in HDMI diagnosis.
