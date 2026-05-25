# TODO - Crowd Heatmap & Alerts Fix

- [x] Update `app.py`:
  - [x] Add `/heatmap_feed` route streaming live heatmap frames (multipart JPEG)
  - [x] Add `/get_stats` route returning JSON with real person count (and optional density)
  - [x] Ensure heatmap generation is actually used inside the streaming loop


- [ ] Update `templates/dashboard.html`:
  - [x] Replace heatmap placeholder image with `<img>` pointing to `/heatmap_feed`

- [ ] Update `static/js/script.js`:
  - [x] Remove random simulated count
  - [x] Poll `/get_stats` and update `#num`
  - [x] Toggle alarm based on real count threshold (e.g., > 30)

- [ ] Run and verify manually:
  - [ ] Login -> Dashboard shows both video and live heatmap
  - [ ] `Current Person Count` updates continuously
  - [ ] Alarm triggers only when threshold exceeded


