#####################################################################################################
# Chapter Two - Day One Dark ########################################################################
#####################################################################################################

label chapter_two:
    
    #################################################################################################
    # Intro #########################################################################################
    #################################################################################################
    
    scene bg chapter two with fade
    play music "music/neutral.ogg" fadein 2 fadeout 3
    $ renpy.pause(5.0, hard=True)
    scene black with fade
    stop sound
    scene bg ord mantell cave with dissolve
    $ renpy.pause(0.1, hard=True)
    scene black with dissolve
    $ renpy.pause(0.25, hard=True)
    scene bg ord mantell cave with dissolve
    $ renpy.pause(0.5, hard=True)
    
    #################################################################################################
    # Mira wakes up inside a cave ... ###############################################################
    #################################################################################################
    
    "I'm not dead."
    "That's the first thought when I wake up."
    nvnr "I open my eyes and I'm somewhere new -- a bed of dirt and rock barely cushioned by a few 
          rags underneath me. There's some small bit of light nearby, but I can't make much of it 
          out from where I am on my back. The room I'm in doesn't seem all that much bigger than 
          the corridor I remember waking up in last time, but the ceiling vanishes into darkness."
    nvnr "The way the air moves -- naturally, organically -- tells me I probably found my way to 
          some planet or moon somewhere. Mission accomplished?"
    nvnr "But how?"
    nvnr "I was pretty sure I'd be dead, and blacking out as soon as I landed in that
          escape pod hadn't increased my survival chances any. The crewman had gotten me that far
          and it was fairly obvious I wasn't in the pod anymore."
    nvnr "Did he survive?"
    nvnr "I don't think I woke up and crawled my way all the way in here."
    nvl clear
    "Wherever {b}here{/b} really is."
    nvnr "I lift my head, but it's an effort. Those wounds from the -- ship? -- remind me not so
          politely that they're still there."
    nvnr "I touch a hand to my face. There's a rag there, wound tight around my forehead. Another
          binds that hole in my stomach and I notice my other hand is trapped in a makeshift 
          splint. I'm pretty sure I didn't have the wherewithal to do all this while I was 
          unconscious."
    nvnr "Someone else survived then. Maybe more than one. That crewman must have made it down 
          with me, at least, and patched me up."
    nvl clear
    "Now where is he?"
    nvnr "I can't put any weight on my left hand so I'm left leaning right to look around the 
          room. And room is far too generous ..."
    nvnr "Walls that look like rock and a floor filled with dirt."
    nvnr "A cave, maybe."
    nvnr "I lift my broken hand and can feel a very slight breeze coming from 
          somewhere ahead. An opening, I think. A low-powered lamp sits on the ground nearby with 
          what look like emergency supplies scattered all around it. That's where the light is 
          coming from."
    nvnr "{i}Someone{/i} was here not too long ago."
    nvnr "I just have to wait then. Wait to find out what happened, and what's going to happen now."
    nvl clear
    nvnr "That crewman had said we were on a ship that was burning up. The escape pods made sense."
    nvnr "But what ship?"
    nvnr "And why was I even there?"
    nvnr "That I couldn't remember anything about a mission or even what had happened to put me
          there was worrisome. I tried. I racked my brain until it gave me a headache, but ..."
    nvnr "Nothing."
    nvl clear
    "I can't remember {i}anything{/i}."
    nvnr "That girder must have hit me hard on the way down. By all rights I should've been dead.
          That I'd woken up at all before that ship finally fell apart with me on it was some kind
          of miracle."
    nvnr "A lot of people probably hadn't been so lucky."
    nvl clear
    
    #################################################################################################
    # Carr returns to find Mira awake ... ###########################################################
    #################################################################################################
    
    "I think I'd been waiting there for maybe an hour or so before I finally heard something."
    "At first, I couldn't tell where it was coming from, but it sounded like something moving toward
     me."
    "I crawl the few meters to the lamp and grab it, then hold it up a little higher."
    "The light beats back those shadows and the cave walls come into view."
    player neutral "\"Hope you are who I think you are ...\""
    "And not some local predator or something ... because there're no weapons on the ground that I can
     see and I'm in no condition to fight ..."
    "I listen, but ..."
    "No."
    "Footsteps."
    carr alarmed "\"... You're awake.\""
    "A man in a tattered Republic uniform comes around a bend in the wall I didn't even see. He stops
     dead in his tracks when he finds me there. He has an armful of what look like scrap parts under
     one arm."
    "He's not that crewman I remember from the ship."
    "I don't know {i}who{/i} he is."
    show carr
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "He's a Republic soldier like the crewman who saved me. 
         I probably have him to thank for saving my life this time.":
            $ good += 1
            player neutral "\"I guess I have you to thank for saving me.\""
            "I motion with my broken hand at my bandages."
            "He nods, but looks suddenly ... wary?"
            "It's hard to put my finger on it, but the moment I opened my mouth his demeanor changed
             from pleasant surprise to looking like I was about to pull a trick on him. Maybe a 
             deadly one."
            "Either way, the throbbing pain in my side where that shard of durasteel stabbed me isn't
             getting any better leaning over like this to see him so I ease myself back down to the
             ground."
        "He's certainly let himself get dirty down here. Not that I'm judging, of course ...":
            $ gray += 1
            player neutral "\"You're almost out of uniform, soldier.\""
            carr awed "\"... What?\""
            player "\"I don't think you'll pass next inspection at the rate you're going.\""
            carr alarmed "..."
            carr annoyed "\"Is that supposed to be some kind of joke?\""
            player "\"... Of course not.\""
            "I sigh."
            "The throbbing pain in my side where that shard of durasteel stabbed me isn't
             getting any better leaning over like this to see him so I ease myself back down to the
             ground."
        "I don't know him or why he brought me here. He might have saved me for some ... other reason
         than because we wear the same uniform.":
            $ dark += 1
            player annoyed "\"Who are you?\""
            "He doesn't have any weapons -- as far as I can tell. At least not brandished at me.
             That might be a good sign. We'll see."
            carr scowling "\"... The one who pulled you out of that escape pod and made sure you 
                           didn't bleed to death.\""
            "You'd think I was holding a blaster instead of a lamp for that look he's giving me now."
            "... I wish I was."
            "There's a dull, throbbing pain in my side where that shard of durasteel had stabbed me."
            "I've been trying to ignore it, but leaning over like this is making it worse."
            "Still, I make sure I return that look of his for another good few moments with enough 
             warning in my eyes to make him think twice about me being \"easy prey\" before letting 
             myself ease back down to the ground."
    
    #################################################################################################
    # Carr is wary of Mira's accent ... #############################################################
    #################################################################################################
    
    "I hear the man put down the load he came back with slowly. 
     Then he makes his way over to where I lay."
    "He watches me for a few moments without saying anything 
     and that silence stretches on uncomfortably."
    player "I guess you don't talk much, do you?"
    if good > max(gray, dark):
        "It's a little unnerving, seeing as he {b}did{/b} go to the trouble of rescuing me."
    elif gray > max(good, dark):
        "A little weird. Just staring at me like that after bothering to keep me alive."
    elif dark > max(good, gray):
        "And I don't like it. The way he's looking at me is making me wish I had some kind of
         weapon on hand."
    else:
        "I'm not sure what to make of all this just staring at me he's doing."
    "I put a put my good hand gingerly to that wound in my stomach, feeling the ache start to
     gradually subside."
    carr annoyed "\"Your accent ...\""
    "I look at him questioningly."
    "Of all the things I could expect him to say to that ..."
    player awed "\"... Accent?\""
    carr "\"You're Imperial.\""
    "I notice then just what he's talking about. 
     He has the heavy consonants of a core-worlder when he speaks, 
     but it didn't surprised me since he {b}is{/b} wearing a Republic uniform."
    "I'm pretty sure I was jettisoned from a Republic ship after all
     and this is probably a Republic world, so ..."
    "He continues to study me and I get the distinct impression that he might not have been so eager
     to keep me alive if he'd heard me talk before now."
    carr "\"Well?\""
    player saddened "\"... Well what?\""
    carr "..."
    carr "\"Are you with the Empire?\""
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "I'm wearing the same uniform as you, aren't I? I'm pretty sure we're allies.":
            $ good += 1
            player saddened "\"I'm pretty sure I know what you're thinking and you're wrong.\""
            carr "\"Oh? And what's that?\""
            player "\"I'm not your enemy. At least, I don't think I am. I mean, I don't know.\""
        "I don't know ... what does this uniform tell you?":
            $ gray += 1
            player neutral "..."
            "I look pointedly down at my tattered remains of the same uniform that he, himself,
             is wearing and then look back up at him."
            player "\"I'm pretty sure I put this on myself, you know ...\""
            carr "\"And so would an Imperial spy.\""
            player "\"Would you believe me if I said I wasn't one?\""
            carr "\"Not unless you could prove it.\""
            player "..."
            player "\"What if I don't even know?\""
        "What kind of stupid question is that? Of course not!":
            $ dark += 1
            player annoyed "\"What kind of a stupid question is that? 
                            Of course I'm not with the Empire!\""
            carr "\"It's not a stupid question. You {b}sound{/b} like an Imperial.\""
            player "\"And you sound like an idiot, how about that?\""
            player "\"Not everyone from the Imperial worlds is with the Sith Empire. Not everyone
                    from the Republic worlds is in the Republic!\""
            player "\"Are {b}you{/b} with the Empire?\""
            carr "\"Of course not.\""
            player "\"Then don't insult me by presuming to know who and what I am when I don't even
                    really know.\""
    
    #################################################################################################
    # Mira admits to amnesia ... ####################################################################
    #################################################################################################
    
    carr "\"What do you mean you 'don't know'?\""
    player saddened "\"I {b}don't{/b} know.\""
    player "\"Republic, Empire ... I can't remember anything before waking up on that ship,
            which pretty soon after tried to explode with me still inside it.\""
    carr "..."
    carr meditative "\"That was the {i}Justiciar{/i}."
    player neutral "\"What was?\""
    "He sits down instead of answering me right away, looking tired from wherever he was and
     whatever he was doing there."
    "He leans back against the far wall of the cave, still keeping an eye on me."
    carr pout "\"The {i}Justiciar{/i}. A carrier in the escort fleet.\""
    player alarmed "\"Escort fleet?\""
    carr "\"Yeah.\""
    player "\"What was it {b}escorting{/b}\""
    "He hesitates. I can see the distrust still in his eyes."
    carr "\"Munitions.\""
    carr "\"A few dignitaries.\""
    carr "\"We were headed for Ord Mantell ...\""
    "Ord Mantell ...?"
    "No."
    "Nothing."
    "I can't remember anything about any mission to Ord Mantell."
    player "\"Is that where we are now?\""
    "He nods slowly."
    carr "\"Seems so.\""
    carr "\"I've scouted around and the local wildlife and geography seems about right.\""
    carr "\"We were close by when we were attacked.\""
    "Attacked?"
    
    #################################################################################################
    # Carr and Mira talk about the attack ... #######################################################
    #################################################################################################
    
    player "\"Attacked by who?\""
    "Again, that mistrustful look."
    if good > max(gray, dark):
        "It's not helping, and I need to know what's going on if I want to help."
    elif gray > max(good, dark):
        "It's a little irritating. What damage could I possibly do right now knowing the truth?"
    elif dark > max(good, gray):
        "It's annoying. My life is on the line here too and he shouldn't be keeping secrets."
    else:
        "I don't know if he's right or wrong about me, but he's all I've got right now."
    "Whatever might have happened before, I can't remember it now. So does it even matter?"
    carr "\"Not the Empire, or we'd be having a very different conversation right now."
    player awed "\"You think I had something to do with it?\""
    carr "\"I didn't say that.\""
    carr frustrated "\"I don't know what to think. Did you?\""
    player alarmed "\"I told you I don't know.\""
    "He scowls, obviously frustrated with that answer again."
    player annoyed "\"Look.\""
    player "\"I can't remember anything.\""
    player "\"I {b}don't{/b} know what was going on on that ship, 
            and I {b}don't{/b} know anything about who attacked.\""
    player "\"I {b}do{/b} know that I was inside when it was, 
            and you saw how well that worked out for me ...\""
    "I gestured at the bandage work he had done on my head and stomach.
     That should've been fairly convincing, but ..."
    "Who knows what that \"escort fleet\" was really doing or why I was even there."
    
    #################################################################################################
    # Mira can't remember her name ... ##############################################################
    #################################################################################################
    
    carr pout "\"You remember your name?\""
    "He asks me that abruptly and I frown at the sudden turn away from those other suspicions."
    player "\"Yeah, of course I do, it's --\""
    "I open my mouth ... "
    "But the words don't come."
    "It shocks me for a moment, and for a moment all I can do is stare at him with my mouth agape."
    player alarmed "\"It's ...\""
    "Panic starts to set in."
    "Why can't I remember it?"
    "Why can't I remember my own name?"
    player disdained "{i}Because you can't remember {b}anything{/b}{i}."
    "That ... doesn't reassure me at {b}all{/b}."
    "I grasp desperately for the memory anyways, but it's like something slippery that just keeps
     sliding out of reach."
    "A dozen other names all come to mind -- none of them {b}mine{/b}."
    "And, somehow, that terrifies me more than anything else I can't remember right now."
    "I didn't notice that man had moved until he was kneeling down over me, trying to press fingers
     to my skull."
    "I flinch, and he gives me a disapproving look only a mother or a doctor could manage."
    carr "\"I did my best to patch you up, but I'm no field surgeon -- just a bridge officer.\""
    "He's just checking the wound."
    "I tell myself that 
     and try to settle down so he can take a look under those bandages on my head."
    "It hurts, but not like that stab wound in my guts."
    "I eye him warily the whole while, feeling far more out-of-sorts and somehow vulnerable now
     despite things not having changed at all."
    "Now I just {b}knew{/b}. Knew that I {b}didn't{/b} know -- my own name."
    carr "\"You took a bad shot to the head, 
          so I'm not sure what kind of brain damage you might've-\""
    player awed "\"{b}Brain{/b} damage?!\""
    carr "\"I don't know.\""
    carr "\"But I'm not a doctor, like I said.\""
    carr "\"It might explain your memory loss.\""
    "I just stare at him, trying to process that for a few seconds and suddenly paranoid about
     whether I even {b}can{/b} still \"process\" anything right."
    "I mean, I don't {b}feel{/b} like anything's loose or messed up inside my head ..."
    "Other than not being able to remember my own name or anything else about who I was, of course."
    "But how was brain damage {b}supposed{/b} to feel?"
    "Would I even know?"
    
    #################################################################################################
    # Carr tells her her name ... ###################################################################
    #################################################################################################
    
    carr "\"The name on the inside of your uniform said 'Mira'.\""
    carr "\"No idea about a family name -- it was pretty beat up when I found you.\""
    player alarmed "\"Mira ...\""
    $ player_name = "Mira"
    carr "\"That's right.\""
    carr "\"The uniform means you could be one of ours.\""
    carr frustrated "..."
    carr "\"I guess it doesn't really matter right now.\""
    carr pout "\"I'm Lieutenant Carr, junior grade.\""
    $ carr_name = "Lt. Carr"
    player saddened "\"Lieutenant?\""
    carr "\"Yeah.\""
    "He finishes inspecting my head and gives me a look that seems much less guarded now."
    "Apparently not knowing who I am or where I really came from makes me far less dangerous
     than just being crippled."
    player "\"You pulled me out of that escape pod?\""
    carr "\"One from the {i}Justiciar{/i} by the markings, yeah.\""
    "I think about that crewman who'd saved my life by actually helping me get there."
    "I'd been falling apart then too much to have ever done it alone."
    "I know that now."
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "Did you ... find anyone else?":
            $ good += 1
            player "\"There was another crewman with me, he ... he saved my life ...\""
            "But Carr just shakes his head."
            carr "\"Sorry. I didn't find anyone else. Just you in there.\""
            "That ..."
            "Hurts."
            "That poor man would have survived if he hadn't stopped for me."
        "I don't suppose you found anyone else who didn't need so much reassembly ...":
            $ gray += 1
            player "\"There was someone else with me who shouldn't have been falling apart quite
                    so much ...\""
            carr "\"Sorry. I didn't find anyone else. Just you in there.\""
            "That's ..."
            "Unfortunate."
        "That crewman obviously didn't make it or else he'd be here instead of this officer.":
            $ dark += 1
            player "\"What about other survivors? We can't be the only ones ...\""
    
    carr "\"I've been looking for others.\""
    carr "\"Your pod's the only other one I could get a fix on anywhere nearby.\""
    carr "\"Something fried your beacon on the way down just like mine -- maybe just like anyone
          else's.\""
    carr "\"I've been stuck tracking on foot the past couple days without any luck.\""
    carr "\"As far as I can tell, we're in the middle of nowhere on this planet.\""
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "That's ... a little disheartening.":
            $ good += 1
        "That's ... I've heard better news.":
            $ gray += 1
        "That's ... so I'm stuck out here with you.":
            $ dark += 1
            player disdained "\"I guess we're stuck with each other for a while then ...\""
            carr "\"Not exactly my preference either.\""
    
    #################################################################################################
    # Carr and Mira ponder situation ... ############################################################
    #################################################################################################
    
    "It doesn't seem like I'm still in danger of dying anymore, but being so far from civilization 
     without a beacon means that rescue parties have no way of finding us."
    player saddened "\"Food? Water?\""
    carr "\"Just the emergency rations from our pods.\""
    carr "\"Should last us a couple weeks if we're careful.\""
    player neutral "\"{b}Us{/b} ...\""
    "There's a rueful smirk on my face at the thought considering how this whole conversation
     started out."
    player "\"So ... no plans to get rid of me or leave me here to die then?\""
    carr "\"No.\""
    carr "\"Not yet, anyways.\""
    "He takes out a knife and points it at me."
    carr "\"Not unless you want to give me a reason too.\""
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "No need for that.":
            $ good += 1
            player saddened "\"We're on the same side, remember?\""
            carr "\"Yeah. I'll try to keep that in mind ...\""
        "No. Thanks for the offer, though.":
            $ gray += 1
            player neutral "\"No. Thank you.\""
            player "\"Not yet, anyways.\""
            "His lips twitch into the ghost of a smile."
            carr cheery "I didn't think so."
        "Don't threaten me.":
            $ dark += 1
            player annoyed "\"Don't wave that thing at me unless you're going to use it.\""
            carr "\"How do you know I won't?\""
            player "\"Because you haven't yet.\""
            carr "\"We'll see, I guess.\""
            
    #################################################################################################
    # Carr and Mira eat ... #########################################################################
    #################################################################################################
    
    "Carr cuts open one of the emergency ration packets he must have gotten from our pods
     and starts going about getting both of us something to eat."
    "I don't even realize how hungry I am until I'm clawing into some hermetically sealed \"food\"
     masquerading as a real meal and failing miserably."
    player disdained "\"Never thought I'd actually have to {b}eat{/b} one of these ...\""
    "Carr doesn't seem too much more pleased, but he is already half done."
    "Enough so to pause and give me a nugget of wisdom."
    carr pout "\"The quicker you eat it the quicker you'll forget the taste.\""
    carr "\"That's the first food you've gotten in you in days.\""
    player "\"How long have I been out?\""
    carr "\"Going on three days until today.\""
    player "\"Hm.\""
    "I finish that \"food\" and wash it down with a generous amount of water -- also from the
     emergency supplies."
    "The lieutenant watched me eat the whole time while pretending not to."
    "He also tried to hide where he slipped that knife back to when he thought I wasn't paying
     attention."
    player neutral "\"You look tired.\""
    carr "\"I'll manage.\""
    "I raise an eyebrow at him."
    player "\"Afraid I'll cut your throat in your sleep?\""
    carr "\"Among other things.\""
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "Don't be.":
            $ good += 1
            player "\"Don't be.\""
            "He just grunts at that."
            player saddened "\"And, for what it's worth ... thank you.\""
            carr "\"For what?\""
            player saddened "\"For not leaving me to die out there.\""
        "I guess we'll find out ...":
            $ gray += 1
            player "\"I guess we'll find out then, won't we?\""
            "He just grunts at that."
            player "\"It'll take me a little while -- what with the broken hand and all.\""
            player "\"But I'll try not to disappoint too much.\""
        "Maybe you should be.":
            $ dark += 1
            player "Maybe you should be."
            "He just grunts at that."
            
    "And with that I settle back in and try to make myself comfortable on the dirt floor again."
    "I don't realize how tired I am by now, and sleep comes on quickly once I'm down."
    
    scene black with fade
    
    #################################################################################################
    # End ###########################################################################################
    #################################################################################################
    
    jump chapter_three