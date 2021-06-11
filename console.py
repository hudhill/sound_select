import pdb

from models.mix import Mix
from models.dj import Dj
import repositories.dj_repository as dj_repository
import repositories.mix_repository as mix_repository

mix_repository.delete_all()
dj_repository.delete_all()

dj_1 = Dj("Ruling Planet", "Mikayla's bio")
dj_repository.save(dj_1)
dj_2 = Dj("Max Salty", "Max's bio")
dj_repository.save(dj_2)
dj_3 = Dj("Saffron", "Ari's bio")
dj_repository.save(dj_3)
dj_4 = Dj("Radha", "Radha's bio")
dj_repository.save(dj_4)
dj_5 = Dj("Zach", "Zach's bio")
dj_repository.save(dj_5)

mix_1 = Mix("001: after hours", 
"I'm glad you're home, baby. Here, let me take that for you. You've worked so hard all day... Why don't you go unwind by the fire and I'll pour us some of that red we've been saving? Welcome to the After Hours...",
"001.jpeg", 
"001tracks.jpeg",
"slow jams,smooth jazz,r&b,funk,soul",
dj_2)
mix_repository.save(mix_1)

mix_2 = Mix("002: organic glitch",
"A set of ambitiously blind selections all because I wanted to end this mix with a Sailorwave tune.",
"002.jpeg",
"002tracks.jpeg",
"electronic,experimental,house",
dj_1)
mix_repository.save(mix_2)

mix_3 = Mix("003: drips n blips",
"some sticky icky icky ((will make you want to take a shower))",
"003.jpeg",
"003tracks.jpeg",
"industrial,ebm,new wave,electropunk,experimental",
dj_3)
mix_repository.save(mix_3)

mix_4 = Mix("004: pleasure pond",
"welcome to the pleasure pond!\nit's a warm dip in the lake, a levitation through the trees, a sensual swirl in the sky, and down into a dark dreamy place.",
"004.webp",
"004tracks.webp",
"ambient,newage,hindustani,minimal techno,experimental",
dj_4)
mix_repository.save(mix_4)

mix_5 = Mix("005: impossible scheme",
"To Whom It May Concern:\nAttached please find a selection of anxious dance music that will force your next existential crisis into tidy rows and columns.\nBest,\nZach",
"005.webp",
"005tracks.webp",
"electro,experimental,minimal,breaks",
dj_5)
mix_repository.save(mix_5)

mix_6 = Mix("006: crush",
"Hey! I'm glad I caught you. So um, I've been wanting to say–- I mean you know how we've been hanging out a lot, and–– well–– I really like hanging with you and I uh, I hope this isn't weird but I made you this mix. Anyway, um–– see you at school :)",
"006.webp",
"006tracks.webp",
"80s,90s,synthpop,girlpop,r&b,new jack swing",
dj_2)
mix_repository.save(mix_6)

mix_7 = Mix("007: accomplished woman",
"Look, I hate the $18.2 billion industry that is Valentine's Day just as much as anyone but I also watched the 2005 version of Pride & Prejudice four times in the last two months. The photo was taken by my friend Madeline Wilson (bit.ly/2SVhAbQ), who is Will's Valentine each year but will forever be mine. ♥︎",
"007.webp",
"007tracks.webp",
"electronic,techno,bass,eco grime",
dj_1)
mix_repository.save(mix_7)

mix_8 = Mix("008: shut the door",
"step into this pillow-filled smoky tent that smells of roses (+ sweat) with dark dancey tunes best suited for late night listening 💋💋💋",
"008.webp",
"008tracks.webp",
"middle eastern,krautrock,electronic,acid,minimal wave",
dj_3)
mix_repository.save(mix_8)

mix_9 = Mix("009: after the flood",
"float away with another mellow and moody mix from @radha_v you will feel heavy and light all at once!",
"009.jpeg",
"009tracks.jpeg",
"folk,classical,newage,ambient,jazz,world,ambient jazz",
dj_4)
mix_repository.save(mix_9)

mix_10 = Mix("010: lounge lizards from spaceport proxima",
"You're flying out of Proxima? You HAVE to go check out the Lounge Lizards. There's a reason why everyone calls 'em the best lounge band in Alpha Centauri.",
"010.jpeg",
"010tracks.jpeg",
"boogie,jazz,downtempo,disco",
dj_5)
mix_repository.save(mix_10)

pdb.set_trace()