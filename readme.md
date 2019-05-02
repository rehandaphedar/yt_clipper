# yt_clipper

## Screenshots

<img src="https://i.imgur.com/S2pWtEy.jpg" width="560">

## Hotkeys

### Marker Hotkeys

**ctrl+shift+A:** toggle hotkeys on/off.

**A:** Add marker at current time (start = green, end = yellow, selected = purple).

**Z:** Undo last marker (disabled if a marker pair is currently selected).

**shift+mouseover:** View marker pair info and edit a pair's crop or speed (output webm fps is **multiplied** by the speed factor).

- While a pair is selected use **shift+Q/shift+A** to move the start/end marker to current time.
  - Adjust marker position more precisely using the '<' and '>' keys to view YouTube videos frame by frame.
- While a pair is selected use **shift+Z** to delete the pair.

**W:**

1. Change default new marker speed or crop (output webm fps is **multiplied** by the speed factor).
2. Specify intended download resolution for correctly previewing crops (automatically scales any existing crops on change).
   - Note that you can mark up the video at any quality/resolution and simply change the intended download resolution before saving the clipper script.
3. Specify any concatenated (merged) webms you want to make from the clipped webms. The format is similar to that for print ranges: comma separated marker pair numbers or ranges (eg '1-3,5,7'). Use semicolons to separate merged webms (eg '1-3,5,7;4-6,9' will create two merged webms)
4. Specify short title that will be prefixed to output script and webms.

**shift+E/D:** Update all markers to default new marker speed(**E**)/crop(**D**).

**X:** When marker or defaults editor is open, begin drawing crop. **Shift+click** in the video to set the top left crop boundary and then **shift+click** again to set the bottom right. Any other click action (eg ctrl+click) will stop drawing.

**shift+X(v0.0.57+):** Like **X**, begin drawing a crop but set only the left and right boundaries on **shift+click**. Vertically fills the crop, that is, it sets the top to 0 and the bottom to the video height.

### Video Playback Hotkeys

**shift+G:** Toggle auto video playback speed adjustment based on markers. When outside of a marker pair the playback speed is set back to 1 (and cannot be changed without toggling off auto speed adjustment).

**alt+G(v0.0.60+):** Toggle auto looping of currently selected marker pair.

**Q:** Decrease video playback speed by 0.25. If the speed falls below 0 it will cycle back to 1.

### Save and Upload Hotkeys

**S:** Save generated python clipper script (save it beside input webm).

**shift+S:** Copy generated python clipper script to clipboard (useful if saving breaks).

**alt+S:** Save markers info to a file (.json).

**G:** Toggle markers .json file upload for reloading markers (must be from the same video).

**C:** Upload anonymously to gfycat (only supports slowdown through the gfycat url).

**alt+shift+S:** Save yt_clipper authorization server script (run it with python ./yt_clipper_auth.py, close it with ctrl+C).

**shift+C:** Open gfycat browser authentication and upload under account (auth server must be running).

## Values

Crop is given as x:y:w:h where x:y is the distance left:top from the top left corner and w:h defines the width:height of the output video. Each value is a positive integer in pixels. w and h can also be iw and ih respectively for the input width and input height.

## Useful YouTube Controls

1. Use [space_bar] or K to pause/play the video.
2. Use '<' and '>' to view a video frame by frame.

## Tips

1. If you're new to userscripts checkout <https://openuserjs.org/about/Userscript-Beginners-HOWTO> for instructions.
2. Checkout the companion script for copying gfy links from the gfycat upload results page as markdown at <https://openuserjs.org/scripts/elwm/gfy2md>.
3. The script can be slow to load sometimes, so wait a bit before adding markers.
4. Refresh the page if the script doesn't load and to clear markers when switching videos in the same window.
5. Videos can be marked up and the markers json or clipper script can be saved before higher quality levels are available, but the final generated webm quality depends on the quality formats available.
6. The clipper script skips regenerating any existing webms. This makes it easy to delete webms you want regenerated and by rerunning the script.

## Output Script Usage

```sh
python ./clip.py -h # Prints help. Details all options and arguments.

python ./clip.py ./filename.webm

python ./clip.py ./filename.webm --overlay ./overlay.png --gfycat

python ./clip.py ./filename.webm --format bestvideo+bestaudio # this is the default format

python ./clip.py --url https://www.youtube.com/watch?v=0vrdgDdPApQ --audio

python ./clip.py --json markers.json # automatically generate webms using markers json
```

## Dependencies

- ffmpeg must be in your path for the python script (<https://www.ffmpeg.org>).
- passing --url to the python script requires youtube-dl be in your path
  - `pip install youtube-dl`
- passing --gfycat requires the urllib3 python package.
  - `pip install urllib3`

## Changelog

- v0.0.65: Skip generating existing webm clips before executing ffmpeg for faster script reruns.
- v0.0.64: Add denoise, deinterlace and crf options in clipper script.
- v0.0.63: Add creating webms using markers json in python clipper script. Add concatenating (merging) clips.
- v0.0.62: Make short title input in defaults editor wider and improve YouTube video fps detection.
- v0.0.61: Fix cropping when not in theater mode on YouTube.
- v0.0.60: Add alt+G for auto looping currently selected marker pair.
- v0.0.59: Q key now decreases playback speed by 0.25, cycling back to 1 if speed becomes 0 or less.
- v0.0.58: Slowdown is now a speed multiplier rather than divider.
- v0.0.57: Add shift+X for cropping with top and bottom automatically set to 0 and video height respectively.
