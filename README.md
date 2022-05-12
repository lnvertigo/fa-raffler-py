# FurAffinity Raffler
Reads the list of followers from the static ` "../watchlist/to/[username]/#" ` URL and uses Python's shuffle method to determine a winner.

## Usage
---
**Enter the username of the followers list you want to import into the top field** and press the button below the field.

You can **manually enter a name** (not strictly a username) with the second field and button combo.

**Shuffle using the shuffle button**, and the list window will shuffle, and the winner (the first user in the shuffled list) will appear on the main control panel.

## Mysteries to Solve
---
- When loading a page of 200+ followers, opening the URL in Firefox will show all followers instead of splitting into 2 pages of 200. **The code will still treat the list as 2 pages despite this.**
- Similarly, how does FA determine to split the list to "Next 1000" and "Next 200" in browser?
- What causes Current Bug #1?

## Current Bugs
---
- When entering specific usernames, instead of the watchers list, the *main page* is parsed.

	List of users it doesn't work with:
	- amazinarts
	- seyorrol

	Both have 15k+ watchers and some have characters such as `-` and `.` . However, the user `---` (3 dashes) functions just fine (has 3k followers).

