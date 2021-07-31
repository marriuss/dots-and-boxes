The aim of this project was to implement Q-learning algorithm in multi-agent game.
Chosen game is classic version of board game "Dots and boxes" (https://en.wikipedia.org/wiki/Dots_and_Boxes).

### How to run the application
<ol>
<li>

Clone the repository: `git clone https://github.com/marriuss/dots-and-boxes.git` \
(Or just download it)
</li>
<li>

Make sure you have all the requirements: `dots_and_boxes\ pip install -r requirements.txt`
</li>
<li>

Run the app: `dots_and_boxes\ python run.py` \
(Or just run the file)
</li>
</ol>

### Project features

##### Features implemented:
<ul>
<li>More then 2 players allowed.</li>
<li>Two types of players: Bot and Agent.</li>
</ul>

##### To-do list:
<ul>
<li>Some refactoring.</li>
<li>New type of players: human!</li>
<li>Documentation.</li>
<li>Tests.</li>
<li>Serialization.</li>
</ul>

### Settings
_Text is not available..._

### Types of players

##### Bot
Common type of player. It's strategy is stupidly simple: it chooses one of currently available edges on field completely randomly.  

##### Agent
It's strategy is based on Q-learning algorithm. To learn more you can visit this page: https://en.wikipedia.org/wiki/Q-learning.

### Known bugs
"Win" text can be shown incorrectly.

P.S. There are can be misspelling or another types of mistakes in the text above. Text, that is "not available", will be written soon... maybe.
