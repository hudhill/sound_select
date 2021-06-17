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

mikayla = Dj("Ruling Planet", "mikayla.webp")
dj_repository.save(mikayla)
max = Dj("Max Salty", "max.webp")
dj_repository.save(max)
ari = Dj("Saffron", "ari.webp")
dj_repository.save(ari)
radha = Dj("Radha", "radha.webp")
dj_repository.save(radha)
zach = Dj("Zach", "zach.webp")
dj_repository.save(zach)

mix_1 = Mix("001: after hours", 
"I'm glad you're home, baby. Here, let me take that for you. You've worked so hard all day... Why don't you go unwind by the fire and I'll pour us some of that red we've been saving? Welcome to the After Hours...",
"001.jpeg", 
"001tracks.jpeg",
"slow jams,smooth jazz,r&b,funk,soul",
"https://soundcloud.com/mmarz-mix/mmarz-001-max-salty-after-hours",
Genre("Slow Jams", "#330000"),
max)
mix_repository.save(mix_1)

mix_2 = Mix("002: organic glitch",
"A set of ambitiously blind selections all because I wanted to end this mix with a Sailorwave tune.",
"002.jpeg",
"002tracks.jpeg",
"electronic,experimental,house",
"https://soundcloud.com/mmarz-mix/mmarz-002-mikayla-organic-glitch",
Genre("Electronic", "#FF34B3"),
mikayla)
mix_repository.save(mix_2)

mix_3 = Mix("003: drips n blips",
"some sticky icky icky ((will make you want to take a shower))",
"003.jpeg",
"003tracks.jpeg",
"industrial,ebm,new wave,electropunk,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-003-saffron-drips-n-blips",
Genre("Industrial", "#0BB5FF"),
ari)
mix_repository.save(mix_3)

mix_4 = Mix("004: pleasure pond",
"welcome to the pleasure pond!\nit's a warm dip in the lake, a levitation through the trees, a sensual swirl in the sky, and down into a dark dreamy place.",
"004.webp",
"004tracks.webp",
"ambient,newage,hindustani,minimal techno,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-004-radha-pleasure-pond",
Genre("Ambient", "#00FF66"),
radha)
mix_repository.save(mix_4)

mix_5 = Mix("005: impossible scheme",
"To Whom It May Concern:\nAttached please find a selection of anxious dance music that will force your next existential crisis into tidy rows and columns.\nBest,\nZach",
"005.webp",
"005tracks.webp",
"electro,experimental,minimal,breaks",
"https://soundcloud.com/mmarz-mix/mmarz-005-zach-impossible-scheme",
Genre("Techno", "#FF6103"),
zach)
mix_repository.save(mix_5)

mix_6 = Mix("006: crush",
"Hey! I'm glad I caught you. So um, I've been wanting to say–- I mean you know how we've been hanging out a lot, and–– well–– I really like hanging with you and I uh, I hope this isn't weird but I made you this mix. Anyway, um–– see you at school :)",
"006.webp",
"006tracks.webp",
"80s,90s,synthpop,girlpop,r&b,new jack swing",
"https://soundcloud.com/mmarz-mix/mmarz-006-max-salty-crush",
Genre("Pop", "#800080"),
max)
mix_repository.save(mix_6)

mix_7 = Mix("007: accomplished woman",
"Look, I hate the $18.2 billion industry that is Valentine's Day just as much as anyone but I also watched the 2005 version of Pride & Prejudice four times in the last two months. The photo was taken by my friend Madeline Wilson (bit.ly/2SVhAbQ), who is Will's Valentine each year but will forever be mine. ♥︎",
"007.webp",
"007tracks.webp",
"electronic,techno,bass,eco grime",
"https://soundcloud.com/mmarz-mix/mmarz-007-mikayla-accomplished-woman",
Genre("Electronic", "#FF34B3"),
mikayla)
mix_repository.save(mix_7)

mix_8 = Mix("008: shut the door",
"step into this pillow-filled smoky tent that smells of roses (+ sweat) with dark dancey tunes best suited for late night listening 💋💋💋",
"008.webp",
"008tracks.webp",
"middle eastern,krautrock,electronic,acid,minimal wave",
"https://soundcloud.com/mmarz-mix/mmarz-008-saffron-shut-the-door",
Genre("Electronic", "#FF34B3"),
ari)
mix_repository.save(mix_8)

mix_9 = Mix("009: after the flood",
"float away with another mellow and moody mix from @radha_v you will feel heavy and light all at once!",
"009.jpeg",
"009tracks.jpeg",
"folk,classical,newage,ambient,jazz,world,ambient jazz",
"https://soundcloud.com/mmarz-mix/mmarz-009-radha-after-the-flood",
Genre("Ambient", "#00FF66"),
radha)
mix_repository.save(mix_9)

mix_10 = Mix("010: lounge lizards from spaceport proxima",
"You're flying out of Proxima? You HAVE to go check out the Lounge Lizards. There's a reason why everyone calls 'em the best lounge band in Alpha Centauri.",
"010.jpeg",
"010tracks.jpeg",
"boogie,jazz,downtempo,disco",
"https://soundcloud.com/mmarz-mix/mmarz-010-zach-lounge-lizards-from-spaceport-proxima",
Genre("R&B", "#C30000"),
zach)
mix_repository.save(mix_10)

mix_11 = Mix("011: lagoon",
"A glowing talisman of tunes to guide you through the dark rainforest, out onto the shore, and down, down to the bottom of the sea…",
"011.jpeg",
"011tracks.jpeg",
"balearic,downtempo,ambient,spa,lagoon",
"https://soundcloud.com/mmarz-mix/mmarz-011-max-salty-lagoon",
Genre("Balearic", "#B23AEE"),
max)
mix_repository.save(mix_11)

mix_12 = Mix("012: ragequit",
"Took a break from suffering an embarrassing number of Game Overs on my Switch to make this mix.",
"012.jpeg",
"012tracks.jpeg",
"electronic,acid,techno,electro,breakbeat,ragequit,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-012-mikayla-ragequit",
Genre("Techno", "#FF6103"),
mikayla)
mix_repository.save(mix_12)

mix_13 = Mix("013: tadig talayi",
"A mini spectrum of Persian funk, psych, rock, pop, bandari, and classical gems 🌹",
"013.jpeg",
"013tracks.jpeg",
"persian,middle eastern,funk,psych,rock,pop,bandari,classical",
"https://soundcloud.com/mmarz-mix/mmarz-013-saffron-tadig-talayi",
Genre("Persian", "#00EEEE"),
ari)
mix_repository.save(mix_13)

mix_14 = Mix("014: lightdreams",
"enjoy my psychedelic-soup.. with extra kraut ! ★彡",
"014.jpeg",
"014tracks.jpeg",
"krautrock,psych-funk,psych-rock,world,kosmische,prog-rock,psych-jazz,fusion",
"https://soundcloud.com/mmarz-mix/mmarz-014-radha-lightdreams",
Genre("Psychedelic", "#DC8909"),
radha)
mix_repository.save(mix_14)

mix_15 = Mix("015: my proper place",
"'In a chamber of my heart sits an accountant. He is frowning and waving red paper at me.' I recently discovered the Prefab Sprout album I Trawl the Megahertz thanks to a timely reissue by Sony. The title track is one of the most incredible pieces of music I have ever heard. 'I am telling myself the story of my life,' the narrator begins, and what follows is a sweeping tale of melancholy, regret, and longing. It's the kind of tune you put on late at night to think about the story of your own life. All 22 minutes of 'I Trawl the Megahertz' are included in this mix, because it's just that good. I am surrounding it with music that is equally patient, deliberate, and sensitive. There are only eight songs here, but all of them are very special to me. I hope you'll find something in them as well.",
"015.jpeg",
"015tracks.webp",
"chamber pop,jazz,ambient,MPB,art rock",
"https://soundcloud.com/mmarz-mix/mmarz-015-zach-my-proper-place",
Genre("Ambient", "#00FF66"),
max)
mix_repository.save(mix_15)

mix_16 = Mix("016: light show",
"Trance music is my truest guilty pleasure. This mix goes out to all the kandy kids and sewer tunnel ravers in the suburbs. Put on your bracelets, stay hydrated, and enjoy the light show.\nPLUR,\nMax Salty",
"016.jpeg",
"016tracks.jpeg",
"trance,vocal trance,progressive house,techno,ambient,2000s",
"https://soundcloud.com/mmarz-mix/mmarz-016-max-salty-light-show",
Genre("Trance", "#385894"),
max)
mix_repository.save(mix_16)

mix_17 = Mix("017: shrubland",
"Music that makes me think of being a teenager in my hometown even though I was too busy listening to MCR to know about this kind of music when I was a teenager in my hometown.",
"017.jpeg",
"017tracks.jpeg",
"experimental,ambient,musique concrète,electronic",
"https://soundcloud.com/mmarz-mix/mmarz-017-mikayla-shrubland",
Genre("Ambient", "#00FF66"),
mikayla)
mix_repository.save(mix_17)

mix_18 = Mix("018: murda",
"An hour-long collection of some of my favorite early memphis rap. Turn up the bass, pull out the Tanqueray, and get comfyyyyyyyyy.",
"018.jpeg",
"018tracks.jpeg",
"hip-hop,rap,memphis,90s",
"https://soundcloud.com/mmarz-mix/mmarz-018",
Genre("Hip-Hop", "#FFCC11"),
ari)
mix_repository.save(mix_18)

mix_20 = Mix("020: sun kissed",
"I had a dream the other night that I was laying in warm sand, and a wave washed over me like a cozy duvet blanket. I woke up feeling like I was kissed by the sun! This week's mix is to slow ya down, make you feel warm, serene, & ready for the summer.",
"020.jpeg",
"020tracks.jpeg",
"easy listening,soul-jazz,lounge,funk,disco,psych-funk",
"https://soundcloud.com/mmarz-mix/mmarz-020-radha-sun-kissed",
Genre("Soul-Jazz", "#9ACD32"),
radha)
mix_repository.save(mix_20)

mix_21 = Mix("021: club rosewood",
"My favorite kind of DJ has always been the one who keeps you guessing. Though I have a deep appreciation for those who lock into a hypnotizing groove for hours, I am usually most impressed by those who turn heads with curveball selections, drawing unexpected connections between disparate genres and eras.This mix is my imitation of that. After a few mixes with a fair amount of pretense involved, I wanted to get back to the feeling I had when I started buying up records in the first place. The tracklist includes some new favorites alongside a lot of tunes that I've been holding on to for the right moment, which only seems to happen at Club Rosewood, my favorite club in LA. I recorded this direct from vinyl in just a few takes. The mixing is far from perfect, but I also have a deep affinity for those cracks in the veneer, the moments where you can tell that it really is a human trying their best to keep things on the rails. I think this one's really good - hope you agree. ",
"021.jpeg",
"021tracks.jpeg",
"disco,house,funk,techno,soca",
"https://soundcloud.com/mmarz-mix/mmarz-021-zach-club-rosewood",
Genre("Disco", "#6600FF"),
zach)
mix_repository.save(mix_21)

mix_22 = Mix("022: toy factory",
"Welcome to the Toy Factory! Watch as the cogs spin, the hammers strike, the machinery whirs and ploinks and steams... all to create shiny pop toys just for you... :)-max salty",
"022.jpeg",
"022tracks.jpeg",
"synthpop,80s,new wave,sophistipop,experimental,avant garde,art of noise,beatbox",
"https://soundcloud.com/mmarz-mix/mmarz-022-max-salty-toy-factory",
Genre("Synthpop", "#238E68"),
max)
mix_repository.save(mix_22)

mix_23 = Mix("023: extremely lost",
"Haven't slept in seemingly eons. My skin is a mess. I've forgotten how to make a decent pot of coffee.",
"023.jpeg",
"023tracks.jpeg",
"techno,experimental electronic,ambient,minimal,noise",
"https://soundcloud.com/mmarz-mix/mmarz-023-mikayla-extremely-lost",
Genre("Techno", "#FF6103"),
mikayla)
mix_repository.save(mix_23)

mix_24 = Mix("024: black hole",
"Come fall into a weird, grimy spiral of drug-addled post punk, gothic rock, and synth pop (⌐■_■)",
"024.jpeg",
"024tracks.jpeg",
"post punk,goth rock,synth pop,industrial",
"https://soundcloud.com/mmarz-mix/mmarz-024",
Genre("Post Punk", "#0000FF"),
ari)
mix_repository.save(mix_24)

mix_25 = Mix("025: june gloom",
"june gloom? this one's for you...",
"025.jpeg",
"025tracks.jpeg",
"ambient,4th world,experimental,world,classical,new wave",
"https://soundcloud.com/mmarz-mix/mmarz-025-radha-june-gloom",
Genre("Ambient", "#00FF66"),
radha)
mix_repository.save(mix_25)

mix_27 = Mix("027: microdose summer",
"Summertime, and the livin' is TRIPPY! Feel free to throw this one on at your next poolside cookout - just be sure to stay away from the grill if some sneaky dosed you too heavy. If you're zooted to the freakin' moon, maybe go looking for a different recipe. This one is for the heads taking a dip, soakin' up the sun Sheryl Crow style and enjoying the view, maybe with a teensy bit of lysergic accompaniment on board.What am I saying? Who knows. Here, have some of this punch.",
"027.jpeg",
"027tracks.webp",
"chillout,balearic,new age,house,psychedelic",
"https://soundcloud.com/mmarz-mix/mmarz-027-zach-microdose-summer",
Genre("Chillout", "#E29578"),
zach)
mix_repository.save(mix_27)

mix_28 = Mix("028: need ice riddim",
"It's so hot. You need ice. There is no ice. There is only hot hot dancehall courtesy of max salty.",
"028.jpeg",
"028tracks.jpeg",
"dancehall,reggae fusion,ragga,r&b,90s",
"https://soundcloud.com/mmarz-mix/mmarz-028-max-salty-need-ice-riddim",
Genre("Dancehall", "#FFD60A"),
max)
mix_repository.save(mix_28)

mix_29 = Mix("029: hyperextension",
"If you can get through the first 53 seconds of this mix, you can get through anything.",
"029.jpeg",
"029tracks.jpeg",
"electro,techno,industrial,acid",
"https://soundcloud.com/mmarz-mix/mmarz-029-mikayla-hyperextension",
Genre("Electronic", "#FF34B3"),
mikayla)
mix_repository.save(mix_29)

mix_31 = Mix("031: daydream",
"A tripped out, spaaaaced out mix of stoned downbeats you can flip on when it's that time of day to stare out the window ☁️☁️☁️",
"031.jpeg",
"031tracks.webp",
"trip hop,dub,downtempo,illbient,electronic",
"https://soundcloud.com/mmarz-mix/mmarz-031",
Genre("Trip Hop", "#10002B"),
ari)
mix_repository.save(mix_31)

mix_32 = Mix("032: make some room",
"some slappers for ya",
"032.jpeg",
"032tracks.jpeg",
"electronic,house,acid,techno",
"https://soundcloud.com/mmarz-mix/mmarz-032-radha-make-some-room",
Genre("Electronic", "#FF34B3"),
radha)
mix_repository.save(mix_32)

mix_33 = Mix("033: tunneling",
"You are traveling through a tunnel that stretches to infinity. A light at the end drifts further and further away. It is the only thing you can see, so you keep moving towards it.",
"033.jpeg",
"033tracks.jpeg",
"minimal techno,dream house,dub techno,glitch,bass music",
"https://soundcloud.com/mmarz-mix/mmarz-033-zach-tunneling",
Genre("Minimal", "#1D84A0"),
zach)
mix_repository.save(mix_33)

mix_35 = Mix("035: air",
"To kick off mmarz’s elements series, max salty brings you a lush, dreamy mix featuring female vocalists, sensual synths, and deep dreampop pleasures, inspired by the only element you can feel but cannot see. This one is an ode to the natural hypnosis of nighttime, like getting lost in the mist.",
"035.jpeg",
"035tracks.jpeg",
"dreampop,downtempo,electronic,ambient,new age,ASMR",
"https://soundcloud.com/mmarz-mix/mmarz-035-max-salty-air",
Genre("Dreampop", "#CB00FF"),
max)
mix_repository.save(mix_35)

mix_36 = Mix("036: e🅐𝙧ፕ𝖍",
"It's Virgo season!!! Time for some acid-ridden electro, breaks, and a poem about mountains.",
"036.jpeg",
"036tracks.jpeg",
"abstract,acid,ambient,bass,breaks,electro,experimental",
"https://soundcloud.com/mmarz-mix/mmarz-036-mikayla-earth",
Genre("Acid", "#D4D902"),
mikayla)
mix_repository.save(mix_36)

mix_37 = Mix("037: fire",
"A demonic, depraved, and debaucherous mix for the hottest club in hell ???",
"037.jpeg",
"037tracks.jpeg",
"demonic,darkwave,industrial,rock,ebm,electronic",
"https://soundcloud.com/mmarz-mix/mmarz-037",
Genre("Satanic", "#FF0000"),
ari)
mix_repository.save(mix_37)

mix_38 = Mix("038: water",
"fourth in the mmarz 'element' series: ~ water ~ ride the wave...float away...dive in...drink up // bathe in this hour long mix",
"038.jpeg",
"038tracks.jpeg",
"ambient,synth-pop,electronic",
"https://soundcloud.com/mmarz-mix/mmarz-030-radha-water",
Genre("Ambient", "#00FF66"),
radha)
mix_repository.save(mix_38)

mix_39 = Mix("039: m.e.t.a.l.",
"'That's METAL!' What's metal? The clean precision of the Miracle Blade? A rusted-out sedan decomposing in the backyard? A musician pushing the soul entire through their horn? Maybe all of the above. Please consult your doctor before listening to minutes 40-51 of this mix.",
"039.jpeg",
"039tracks.jpeg",
"acid techno,free jazz,electro,noise,psych rock",
"https://soundcloud.com/mmarz-mix/mmarz-039-zach-metal",
Genre("Experimental", "#C0C0C0"),
zach)
mix_repository.save(mix_39)

pdb.set_trace()