import pdb

from models.mix import Mix
from models.dj import Dj
from models.genre import Genre
import repositories.dj_repository as dj_repository
import repositories.mix_repository as mix_repository
import repositories.genre_repository as genre_repository

mix_repository.delete_all()
dj_repository.delete_all()
genre_repository.delete_all()

mikayla = Dj("Ruling Planet", "Mikayla's bio")
dj_repository.save(mikayla)
max = Dj("Max Salty", "Max's bio")
dj_repository.save(max)
ari = Dj("Saffron", "Ari's bio")
dj_repository.save(ari)
radha = Dj("Radha", "Radha's bio")
dj_repository.save(radha)
zach = Dj("Zach", "Zach's bio")
dj_repository.save(zach)
guest = Dj("Guest", "Sometimes we have guests!")
dj_repository.save(guest)

mix_1 = Mix("001: after hours", 
"I'm glad you're home, baby. Here, let me take that for you. You've worked so hard all day... Why don't you go unwind by the fire and I'll pour us some of that red we've been saving? Welcome to the After Hours...",
"001.jpeg", 
"001tracks.jpeg",
"slow jams,smooth jazz,r&b,funk,soul",
"https://soundcloud.com/mmarz-mix/mmarz-001-max-salty-after-hours",
Genre("Slow Jams", "#710300"),
max)
mix_repository.save(mix_1)

mix_2 = Mix("002: organic glitch",
"A set of ambitiously blind selections all because I wanted to end this mix with a Sailorwave tune.",
"002.jpeg",
"002tracks.jpeg",
"electronic,experimental,house",
"https://soundcloud.com/mmarz-mix/mmarz-002-mikayla-organic-glitch",
Genre("Electronic", "#C86006"),
mikayla)
mix_repository.save(mix_2)

mix_3 = Mix("003: drips n blips",
"some sticky icky icky ((will make you want to take a shower))",
"003.jpeg",
"003tracks.jpeg",
"industrial,ebm,new wave,electropunk,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-003-saffron-drips-n-blips",
Genre("Industrial", "#581845"),
ari)
mix_repository.save(mix_3)

mix_4 = Mix("004: pleasure pond",
"welcome to the pleasure pond!\nit's a warm dip in the lake, a levitation through the trees, a sensual swirl in the sky, and down into a dark dreamy place.",
"004.webp",
"004tracks.webp",
"ambient,newage,hindustani,minimal techno,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-004-radha-pleasure-pond",
Genre("Ambient", "#135F3C"),
radha)
mix_repository.save(mix_4)

mix_5 = Mix("005: impossible scheme",
"To Whom It May Concern:\nAttached please find a selection of anxious dance music that will force your next existential crisis into tidy rows and columns.\nBest,\nZach",
"005.webp",
"005tracks.webp",
"electro,experimental,minimal,breaks",
"https://soundcloud.com/mmarz-mix/mmarz-005-zach-impossible-scheme",
Genre("Techno", "#008FB1"),
zach)
mix_repository.save(mix_5)

mix_6 = Mix("006: crush",
"Hey! I'm glad I caught you. So um, I've been wanting to say–- I mean you know how we've been hanging out a lot, and–– well–– I really like hanging with you and I uh, I hope this isn't weird but I made you this mix. Anyway, um–– see you at school :)",
"006.webp",
"006tracks.webp",
"80s,90s,synthpop,girlpop,r&b,new jack swing",
"https://soundcloud.com/mmarz-mix/mmarz-006-max-salty-crush",
Genre("Pop", "#F745F7"),
max)
mix_repository.save(mix_6)

mix_7 = Mix("007: accomplished woman",
"Look, I hate the $18.2 billion industry that is Valentine's Day just as much as anyone but I also watched the 2005 version of Pride & Prejudice four times in the last two months. The photo was taken by my friend Madeline Wilson (bit.ly/2SVhAbQ), who is Will's Valentine each year but will forever be mine. ♥︎",
"007.webp",
"007tracks.webp",
"electronic,techno,bass,eco grime",
"https://soundcloud.com/mmarz-mix/mmarz-007-mikayla-accomplished-woman",
Genre("Electronic", "#C86006"),
mikayla)
mix_repository.save(mix_7)

mix_8 = Mix("008: shut the door",
"step into this pillow-filled smoky tent that smells of roses (+ sweat) with dark dancey tunes best suited for late night listening 💋💋💋",
"008.webp",
"008tracks.webp",
"middle eastern,krautrock,electronic,acid,minimal wave",
"https://soundcloud.com/mmarz-mix/mmarz-008-saffron-shut-the-door",
Genre("Electronic", "#C86006"),
ari)
mix_repository.save(mix_8)

mix_9 = Mix("009: after the flood",
"float away with another mellow and moody mix from @radha_v you will feel heavy and light all at once!",
"009.jpeg",
"009tracks.jpeg",
"folk,classical,newage,ambient,jazz,world,ambient jazz",
"https://soundcloud.com/mmarz-mix/mmarz-009-radha-after-the-flood",
Genre("Ambient", "#135F3C"),
radha)
mix_repository.save(mix_9)

mix_10 = Mix("010: lounge lizards from spaceport proxima",
"You're flying out of Proxima? You HAVE to go check out the Lounge Lizards. There's a reason why everyone calls 'em the best lounge band in Alpha Centauri.",
"010.jpeg",
"010tracks.jpeg",
"boogie,jazz,downtempo,disco",
"https://soundcloud.com/mmarz-mix/mmarz-010-zach-lounge-lizards-from-spaceport-proxima",
Genre("R&B", "#D68F1E"),
zach)
mix_repository.save(mix_10)

mix_11 = Mix("011: lagoon",
"A glowing talisman of tunes to guide you through the dark rainforest, out onto the shore, and down, down to the bottom of the sea…",
"011.jpeg",
"011tracks.jpeg",
"balearic,downtempo,ambient,spa,lagoon",
"https://soundcloud.com/mmarz-mix/mmarz-011-max-salty-lagoon",
Genre("Balearic", "#0F20A4"),
max)
mix_repository.save(mix_11)

mix_12 = Mix("012: ragequit",
"Took a break from suffering an embarrassing number of Game Overs on my Switch to make this mix.",
"012.jpeg",
"012tracks.jpeg",
"electronic,acid,techno,electro,breakbeat,ragequit,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-012-mikayla-ragequit",
Genre("Techno", "#008FB1"),
mikayla)
mix_repository.save(mix_12)

mix_13 = Mix("013: tadig talayi",
"A mini spectrum of Persian funk, psych, rock, pop, bandari, and classical gems 🌹",
"013.jpeg",
"013tracks.jpeg",
"persian,middle eastern,funk,psych,rock,pop,bandari,classical",
"https://soundcloud.com/mmarz-mix/mmarz-013-saffron-tadig-talayi",
Genre("Persian", "#FF5733"),
ari)
mix_repository.save(mix_13)

mix_14 = Mix("014: lightdreams",
"enjoy my psychedelic-soup.. with extra kraut ! ★彡",
"014.jpeg",
"014tracks.jpeg",
"krautrock,psych-funk,psych-rock,world,kosmische,prog-rock,psych-jazz,fusion",
"https://soundcloud.com/mmarz-mix/mmarz-014-radha-lightdreams",
Genre("Psychedelic", "#CB117F"),
radha)
mix_repository.save(mix_14)

mix_15 = Mix("015: my proper place",
"'In a chamber of my heart sits an accountant. He is frowning and waving red paper at me.' I recently discovered the Prefab Sprout album I Trawl the Megahertz thanks to a timely reissue by Sony. The title track is one of the most incredible pieces of music I have ever heard. 'I am telling myself the story of my life,' the narrator begins, and what follows is a sweeping tale of melancholy, regret, and longing. It's the kind of tune you put on late at night to think about the story of your own life. All 22 minutes of 'I Trawl the Megahertz' are included in this mix, because it's just that good. I am surrounding it with music that is equally patient, deliberate, and sensitive. There are only eight songs here, but all of them are very special to me. I hope you'll find something in them as well.",
"015.jpeg",
"015tracks.webp",
"chamber pop,jazz,ambient,MPB,art rock",
"https://soundcloud.com/mmarz-mix/mmarz-015-zach-my-proper-place",
Genre("Ambient", "#135F3C"),
max)
mix_repository.save(mix_15)

mix_16 = Mix("016: light show",
"Trance music is my truest guilty pleasure. This mix goes out to all the kandy kids and sewer tunnel ravers in the suburbs. Put on your bracelets, stay hydrated, and enjoy the light show.\nPLUR,\nMax Salty",
"016.jpeg",
"016tracks.jpeg",
"trance,vocal trance,progressive house,techno,ambient,2000s",
"https://soundcloud.com/mmarz-mix/mmarz-016-max-salty-light-show",
Genre("Trance", "#18C306"),
max)
mix_repository.save(mix_16)

mix_17 = Mix("017: shrubland",
"Music that makes me think of being a teenager in my hometown even though I was too busy listening to MCR to know about this kind of music when I was a teenager in my hometown.",
"017.jpeg",
"017tracks.jpeg",
"experimental,ambient,musique concrète,electronic",
"https://soundcloud.com/mmarz-mix/mmarz-017-mikayla-shrubland",
Genre("Ambient", "#135F3C"),
mikayla)
mix_repository.save(mix_17)

mix_18 = Mix("018: murda",
"An hour-long collection of some of my favorite early memphis rap. Turn up the bass, pull out the Tanqueray, and get comfyyyyyyyyy.",
"018.jpeg",
"018tracks.jpeg",
"hip-hop,rap,memphis,90s",
"https://soundcloud.com/mmarz-mix/mmarz-018",
Genre("Hip-Hop", "#470261"),
ari)
mix_repository.save(mix_18)

mix_19 = Mix("019: driftwood",
"This week we're so happy to have our dear friend Sam Schulte contribute a mix for our series. I met Sam in college and we immediately connected over music. He's actually the gateway / reason I got into college radio and therefore found my way into this amazing community. Over the years we've shared tons of music/playlists with each other- so I'm very excited to have him as our first guest on mmarz :) - radha. Destress and drift out with this plaintive, mellow mix of songs near and dear to Sam.",
"019.jpeg",
"019tracks.jpeg",
"world,folk,jazz,classical,soul",
"https://soundcloud.com/mmarz-mix/mmarz-019-sam-driftwood",
Genre("Ambient", "#135F3C"),
guest)
mix_repository.save(mix_19)

mix_20 = Mix("020: sun kissed",
"I had a dream the other night that I was laying in warm sand, and a wave washed over me like a cozy duvet blanket. I woke up feeling like I was kissed by the sun! This week's mix is to slow ya down, make you feel warm, serene, & ready for the summer.",
"020.jpeg",
"020tracks.jpeg",
"easy listening,soul-jazz,lounge,funk,disco,psych-funk",
"https://soundcloud.com/mmarz-mix/mmarz-020-radha-sun-kissed",
Genre("Soul-Jazz", "#F67307"),
radha)
mix_repository.save(mix_20)

pdb.set_trace()