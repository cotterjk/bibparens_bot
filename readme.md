# (Biblical Parentheticals)
[@bibparens_bot](https://twitter.com/bibparens_bot) on twitter

Tweeting every parenthetical section of biblical scripture (like this) and where it appears.

## Process

### Finding all parentheticals
I created **kjv_final.txt** by hacking up this [text file of the King James Bible](https://raw.githubusercontent.com/ErikSchierboom/sentencegenerator/master/samples/the-king-james-bible.txt). I used the python ['re' library](https://docs.python.org/3/library/re.html) for editor-crashing regex substitutions, and Atom's built in find-replace for small enough jobs.

### Tweeting them
**tweetlines.py** reads in **kjv_final.txt**, chooses a random line, tweets it, and deletes it from the source file. If the line is too long to tweet, it automatically replies to itself until the line is all tweeted. It runs via [cron job](https://en.wikipedia.org/wiki/Cron) on my laptop at 5pm every day.

## Why?
I think they're funny! And I wanted to relearn regular expressions, and run a twitterbot via cron.

## No actually, why?

Besides being written in ancient dialects of languages unrelated to English, original manuscripts of the Bible's components did not have grammar, case, or punctuation as modern English would recognize. To me, seeing parenthesis (which are sort of unspeakable anyway) most expose scripture as an ongoing act of (inspired) translation and rendering, rather than literal dictation (like the Quran).

“A set of parentheses is used whenever the translators identified a thought within a thought. Wherever parentheses are employed in your bible, it is possible to read the surrounding verse or verses without the words in parentheses and have it still make sense." [†](https://www.purecambridgetext.com/post/2018/02/06/the-use-of-parentheses)

They read as whispered asides, explanatory commas, technicalities, and clarifications—which I think add a conversational tone to scripture which can feel stern and impenetrable. After compiling the list, it felt appropriate to dole them out in the arena and format of today's clarifications, educational threads, context clues, and shitposting.


## Quick Facts
- 221 parentheticals total
- 15 books of the Bible have no parentheticals at all
- 70 verses starts with parenthesis
- 24 parentheticals span multiple verses
- The longest begins in Romans 5:13 and spans 5 entire verses
