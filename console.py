import pdb

from models.mix import Mix
from models.dj import Dj
import repositories.dj_repository as dj_repository
import repositories.mix_repository as mix_repository

mix_repository.delete_all()
dj_repository.delete_all()

dj_1 = Dj("Ruling Planet")
dj_repository.save(dj_1)
dj_2 = Dj("Max Salty")
dj_repository.save(dj_2)
dj_3 = Dj("Saffron")
dj_repository.save(dj_3)
dj_4 = Dj("Radha")
dj_repository.save(dj_4)
dj_5 = Dj("Zach")
dj_repository.save(dj_5)

mix_1 = Mix("after hours", 
"I'm glad you're home, baby. Here, let me take that for you. You've worked so hard all day... Why don't you go unwind by the fire and I'll pour us some of that red we've been saving? Welcome to the After Hours...",
dj_2)
mix_repository.save(mix_1)

mix_2 = Mix("organic glitch",
"A set of ambitiously blind selections all because I wanted to end this mix with a Sailorwave tune.",
dj_1)
mix_repository.save(mix_2)

mix_3 = Mix("drips n blips",
"some sticky icky icky ((will make you want to take a shower))",
dj_3)
mix_repository.save(mix_3)

mix_4 = Mix("pleasure pond",
"welcome to the pleasure pond",
dj_4)
mix_repository.save(mix_4)

mix_5 = Mix("impossible scheme",
"To Whom It May Concern:\n Attached please find a selection of anxious dance music that will force your next existential crisis into tidy rows and columns.\n Best,\n Zach",
dj_5)
mix_repository.save(mix_5)

mix_6 = Mix("crush",
"Hey! I'm glad I caught you. So um, I've been wanting to say–- I mean you know how we've been hanging out a lot, and–– well–– I really like hanging with you and I uh, I hope this isn't weird but I made you this mix. Anyway, um–– see you at school :)",
dj_2)
mix_repository.save(mix_6)

mix_7 = Mix("accomplished woman",
"Look, I hate the $18.2 billion industry that is Valentine's Day just as much as anyone but I also watched the 2005 version of Pride & Prejudice four times in the last two months. The photo was taken by my friend Madeline Wilson (bit.ly/2SVhAbQ), who is Will's Valentine each year but will forever be mine. ♥︎",
dj_1)
mix_repository.save(mix_7)

mix_8 = Mix("shut the door",
"step into this pillow-filled smoky tent that smells of roses (+ sweat) with dark dancey tunes best suited for late night listening 💋💋💋",
dj_3)
mix_repository.save(mix_8)

mix_9 = Mix("after the flood",
"float away with another mellow and moody mix from @radha_v you will feel heavy and light all at once!",
dj_4)
mix_repository.save(mix_9)

mix_10 = Mix("lounge lizards from spaceport proxima",
"You're flying out of Proxima? You HAVE to go check out the Lounge Lizards. There's a reason why everyone calls 'em the best lounge band in Alpha Centauri.",
dj_5)
mix_repository.save(mix_10)

pdb.set_trace()