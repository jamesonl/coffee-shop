# This kills both the ecosystem and fiveharbors apis
python end_game.py
kill $(pgrep -f app.py)
