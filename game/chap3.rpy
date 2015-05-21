#####################################################################################################
# Chapter Three - Enemy of my Enemy #################################################################
#####################################################################################################

label chapter_three:
    
    #################################################################################################
    # Intro #########################################################################################
    #################################################################################################
    
    scene bg chapter three with fade
    play music "music/neutral2.ogg" fadein 2 fadeout 3
    $ renpy.pause(5.0, hard=True)
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    
    #################################################################################################
    # Mira gets her stim and kolto treatment ########################################################
    #################################################################################################
    
    carr pout "\"Hold still.\""
    player wincing "..."
    "I feel anesthetics rush through my arm right before the stimulants kick in, getting my blood 
     pumping faster."
    "There's a light-headedness that makes me dizzy even as I feel my heart race like I've been
     running for hours."
    "I don't realize I'm toppling over until I feel Carr's hand on my back, steadying me."
    "My eyes blink back open."
    scene bg ord mantell cave with dissolve
    $ renpy.pause(0.5, hard=True)
    carr "\"Alright?\""
    player normal "\"... Fine.\""
    "Carr waits until I'm steady enough again before leaving me to it."
    "This has become a ritual of ours over the past few days -- giving me a mix of stim and kolto 
     treatments from the emergency medical supplies to get me back on my feet as fast as possible."
    "Already, the fracture in my my hand is doing a lot better. 
     It feels more like a sprain than a break now."
    "The hole in my stomach is closing, even if it manages to look angry and discolored while doing
     it."
    "And my head ..."
    "Well ..."
    "... I still can't remember anything."
    nvnr "I'm stronger than I was, and can move around now." 
    nvnr "Not enough to leave the cave, of course, 
         but I make sure to move around enough to keep from being bedridden anymore than I already 
         have been."
    if good > max(gray, dark):
        nvnr "I want to help. Lieutenant Carr goes out everyday looking for other survivors or signs
             of civilization nearby and I want to be out there with him. Maybe that crewman who saved
             me got in another pod. Maybe there are other people who need our help."
        nvnr "At the very least, it's uncomfortable letting the lieutenant take all the risks on his
             own while I just sit and wait."
    elif gray > max(good, dark):
        nvnr "I need to get out there. See what's going on. I'm going stir crazy cooped up in here all
             by myself all day long. It makes me almost look forward to that dour look on Carr's face
             when he eventually drags himself back in at the end of each day. I've even taken to 
             tracking the progress of dirt and sweat on his uniform to convince myself that time
             isn't just standing still with me trapped in here."
    elif dark > max(good, gray):
        nvnr "I need to get out of here. I can't stay here forever, and I don't trust Carr to tell me
             about everything that he finds. How do I even know he's doing what he says he is? Oh
             sure, he {b}seems{/b} honest enough about it. But he still gives me those calculating
             looks of mistrust. He might not be lying when he tells me what he does know, but
             I know he's not telling me everything. I know it."
    else:
        nvnr "I'm tired of being cooped up in here. I'm tired of not knowing what's going on and
              what we should be doing about it. But I still need to heal."
    nvnr "So I wait. I pace, and I idle, and I think, think, think about the situation between
         frustrated attempts to dig up some memory of what came before. Most of the time, I just
         get a headache for all my trouble."
    nvl clear
    $ renpy.pause(0.25, hard=True)
    
    #################################################################################################
    # Mira and Carr discuss the ones who attacked the fleet #########################################
    #################################################################################################
    
    player frowning "\"So who do you really think attacked us?\""
    "I ask him that question again one day after he comes back and we're sharing another meager 
     dinner of emergency rations."
    "His answer isn't any different than before at first."
    carr frowning "\"Don't know.\""
    carr "\"Captain might have, but I saw her get shredded by a ruptured nav console when we were
          evacuating the bridge of my ship.\""
    carr "\"No colors, that's all I can remember.\""
    player "\"So not Empire th-\""
    carr "\"Not {b}openly{/b} Empire.\""
    player disdainful "\"Could just as easily be Republic by that logic.\""
    carr "\"I doubt it.\""
    carr "\"Why fire on our own ships?\""
    if good > max(gray, dark):
        player "\"It's not the first time it would've happened ...\""
    elif gray > max(good, dark):
        player smiling "\"Oh so many, many reasons to choose from ...\""
        player "\"... Especially if politicians are involved.\""
    elif dark > max(good, gray):
        player annoyed "\"High-ranking people always {b}find{/b} a reason.\""
        player "\"Or don't.\""
        player "\"They don't always need one.\""
    "The lieutenant doesn't say anything to that, just looks thoughtful."
    carr  "\"Whatever the case, it's a little coincidential that both our beacons were fried before 
           landing.\""
    carr "\"Too coincidential.\""
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "You're probably right.": 
            $ good += 1
            player frowning "\"You're probably right.\""
            player "\"So. You think someone did it on purpose?\""
            player "\"The same someone who attacked us?\""
        "And here I was hoping we were just really unlucky ...": 
            $ gray += 1
            player smiling "\"And here I was hoping we were just really unlucky ...\""
            player smiling "\"So. Who do we have to thank for this wonderful vacation from food,
                            facilities, and fun then?\""
        "Someone's going to pay for all this.": 
            $ dark += 1
            player scowling "\"I don't believe in coincidences.\""
            player "\"And I don't appreciate people trying to kill me.\""
            player "\"Whoever they are, they're going to pay for all this.\""
            player "\"One way, or another.\""
    
    #################################################################################################
    
    carr "\"My bet's on the separatists being behind it.\""
    carr "\"I don't know where they got the money -- that attack fleet was probably mercenary
          -- but I wouldn't be surprised.\""
    carr "\"They're the ones who benefit most from stopping those supplies coming into the fighting
          here.\""
    nvnr "I remember the separatists -- the ones the Republic forces are struggling with here.
         They didn't like the way things went with the Treaty of Coruscant or the war and now they 
         wanted independence."
    nvnr "I remember things like that, at least. General information."
    nvnr "So I'm not completely hopeless."
    nvl clear
    
    #################################################################################################
    # Carr discovers signs of a village #############################################################
    #################################################################################################
    
    nvnr "Carr continues to go out. I continue to inject and heal in frustrated impatience. And the
         galaxy continues on without us. For a week or so."
    nvnr "Then Carr comes back with some news."
    nvl clear
    $ renpy.pause(0.25, hard=True)
    carr "\"They {b}are{/b} farms. I'm sure now.\""
    carr "\"And that means a village -- probably somewhere south and maybe somewhere east of us.\""
    nvnr "It was poor luck that he'd finally found something in the direction that ended up feeling
         like the last one he could try. We'd been assuming there might be people to the north, or
         west -- based on some scans we'd intercepted with our emergency equipment and Carr's
         limited memory of local geography. But the receiver barely worked and it could have been 
         malfunctioning. And Carr was ..."
    nvnr "Well, it's not like the lieutenant had ever {b}been{/b} on this planet before crashing 
          right into it."
    nvnr "He had finally seen what he thought were farmsteads to the south then, after we'd given
         up on those signals. But those farmsteads had been so far along that he hadn't been able to 
         investigate then and still make it back to the cave before nightfall. Today, he had 
         confirmed it and gotten back late."
    nvl clear
    $ renpy.pause(0.25, hard=True)
    player normal "\"Friendly?\""
    "Carr shakes his head."
    carr neutral "\"No idea.\""
    carr "\"Didn't want to risk getting that close without warning you first.\""
    carr "\"In case they {b}are{/b} separatists or sympathizers.\""
    
    #################################################################################################
    ## DIALOG OPTION ################################################################################
    #################################################################################################
    
    menu:
        "It's good he recognizes his duty as an officer to a fellow soldier." if good > max(gray, dark): 
            $ good += 1
            $ carrAffection += 1
            player neutral "\"Thank you, Lieutenant -- for that.\""
            carr neutral "\"You don't have to thank me, Mira.\""
            carr "\"I'm not going to leave a wounded soldier behind.\""
            carr "\"Even if she sounds like an Imp, 
                  she was wearing the right colors when I found her.\""
            player "\"Let's hope you're right about me then.\""
        "I'm glad he finally sees us as a team.": 
            $ good += 1
            player neutral "\"Thanks, LT.\""
            carr neutral "\"You might sound like an Imp and not have the memory to say otherwise, but ...\""
            carr "\"We're still in this together, Mira.\""
            carr "\"For now, at least.\""
            player "\"I'll try not to disappoint.\""
        "It's nice to know he worries about me at least." if good > max(gray, dark): 
            $ good += 1
            $ carrAffection += 1
            player "\"I ... \""
            player saddened "\"Thank you. Lieutenant.\""
            player saddened "\"It means something to me that you'd come back.\""
            carr alarmed "\"...\""
            carr neutral "\"... I wouldn't just leave you behind out here, Mira.\""
            player smiling "\"I know.\""
        
        "And I was worried he'd end up being one of those officers who left wounded troopers 
         behind ..." if gray > max(good, dark): 
            $ gray += 1
            player smiling "\"So your duty to a wounded soldier {b}didn't{/b} conflict with
                            your duty to hate anyone with an Imperial accent?\""
            carr amused "Not this time, no."
            player "\"Oh well ...\""
            player "\"Here's hoping my luck holds out then, I guess.\""
            carr neutral "\"I'm not going to leave you behind out here, Mira.\""
            player "\"I might hold you to that promise, Lieutenant Carr.\""
        "Well at least he hasn't given up hope for me being useful yet.": 
            $ gray += 1
            player smiling "\"So I'm not useless enough to just leave behind, huh?\""
            carr neutral "\"I'm not going to just leave you behind out here, Mira.\""
            carr neutral "\"Even if you sound like just another Imp.\""
            player "\"Keep this up and I might even try to sound less like one.\""
        "If I didn't know any better, I'd think he was actually starting to like me." if gray > max(good, dark): 
            $ gray += 1
            $ carrAffection += 1
            player smiling "\"Careful, Lieutenant Carr.\""
            player "\"If I didn't know any better I'd think you were actually starting to {b}like{/b}
                    this maybe-Imperial spy ...\""
            carr alarmed "\"...\""
            carr "\"Let's ... \""
            carr "\"... hope that's not the case.\""
            player "\"What?\""
            player "\"Me being an Imperial spy or you starting to like me?\""
            carr alarmed "\"...\""
            carr alarmed "\"Either ...?\""
            carr neutral "\"Either way, Mira, I wouldn't just leave you behind.\""
        
        "Yeah. Good thing he wasn't thinking about leaving a wounded soldier behind." if dark > max(good, gray): 
            $ dark += 1
            $ carrAffection -= 1
            player disdained "\"At least you're not one of those officers who leaves wounded 
                               soldiers behind.\""
            carr annoyed "\"Of course not.\""
            carr "\"Until I know otherwise, you're a fellow Republic soldier and I'm not leaving you
                  here to die, Mira.\""
            player "\"Good.\""
        "He's only getting off this planet alive if we work together anyways.": 
            $ dark += 1
            player disdained "\"Good.\""
            player "\"Because we're getting off this planet together, or not at all.\""
            carr frowning "\"I hope that's not a threat, Mira ...\""
            player "\"No.\""
            player "\"Just the truth.\""
            carr "\"... Well.\""
        "He's worried about me. Good. I can use that." if dark > max(good, gray): 
            $ dark += 1
            $ carrAffection += 2
            player smiling "\"Oh, you came back for {b}me{/b} ...\""
            carr frowning "\"Of course, I did.\""
            carr "\"I'm not just going to leave you out here, Mira.\""
            player "\"I certainly hope not.\""
            player "\"I'd be pretty hurt if you didn't come back to me.\""
            carr alarmed "..."
            carr "\"... What?\""
            player normal "\"I said I'd be pretty worried if you didn't come back.\""
            carr frowning "\"... Oh.\""
            carr "\"Don't have to worry about that.\""
            player smiling "\"Okay, I won't.\""
            carr "..."
    
    #################################################################################################
    
    carr neutral "\"I'm going to try to talk to one of the farmers tomorrow if I can find them.\""
    carr "\"Find out where they get their supplies.\""
    carr "\"There has to be at least a small village somewhere nearby by the looks of them.\""
    
    #################################################################################################
    # Mira and Carr argue about her going with him ##################################################
    #################################################################################################
    
    player normal "\"I'm going with you.\""
    carr neutral "\"...\""
    carr "\"No.\""
    carr "\"You stay here.\""
    if good > max(gray, dark):
        player saddened "\"You can't just keep leaving me here.\""
        player "\"I can keep up.\""
        carr "\"No.\""
    elif gray > max(good, dark):
        player alarmed "\"What?\""
        player smiling "\"... You afraid you'll end up having to carry me?\""
        carr annoyed "..."
        carr "\"Franky ...\""
        carr "\"... yes.\""
    elif dark > max(good, gray):
        player annoyed "\"You can't just give me orders.\""
        carr annoyed "\"It's not an order, its ...\""
        player "\"I c-\""
        "I open my mouth again to argue with him but he breaks in right on top of me."
    player annoyed "..."
    carr neutral "\"You'd only slow me down and I need to be back here by tomorrow morning -- with
                  or without help.\""
    player disdained "\"I've been doing nothing but resting and healing for a week.\""
    player "\"I can make it.\""
    carr "\"In another day or two, maybe. Maybe you could keep up with me.\""
    carr "\"But I {b}don't{/b} want to be caught out there with you moving slow after nightfall.\""
    player "\"I can handle myself.\""
    "He doesn't immediately respond to that."
    "A second later, though, he reaches out and snatches my left hand without saying a word."
    "He just squeezes hard."
    "Pain shoots instantly up my arm."
    player frustrated "\"... {b}mmph{/b}!\""
    "I stopped feeling like I needed the splint two days ago, but that didn't mean it was ready
     for that kind of intentional abuse yet."
    "That pain is enough to paralyze my whole arm up past the elbow."
    "I grimace, sucking in ragged breaths."
    carr annoyed "\"See?\""
    carr "\"The terrain is too rocky along the way and we don't even have a blaster you could use.\""
    carr "\"That wound in your side could tear open again too.\""
    carr "\"Sorry, Mira.\""
    player wincing "..."
    if good > max(gray, dark):
        player "\"That was ...\""
        player "\"... uncalled for.\""
        carr "\"But you understand now.\""
        player scowling "\"...\""
    elif gray > max(good, dark):
        player angered "\"Blast it, then why don't you just punch me in the stomach wound next time 
                       you want to make a point!\""
        player wincing "\"{b}Stars{/b}, that ... \""
        player "\"{b}hurt{/b} ...!\""
        carr "\"But you understand now.\""
        player annoyed "\"Give me another lesson -- {b}please{/b}!\""
        player "\"Just think how many times you could try and trip me into the dirt if you take me 
                with you!\""
        carr "\"I'm not taking you with me, Mira.\""
        carr "\"Not this time, at least. 
              And hopefully we won't have to worry about it after tomorrrow.\""
    elif dark > max(good, gray):
        player wincing "\Try that ... again ...\""
        player angered "\"... I {b}dare{/b} you.\""
        carr "\"I'm not going to do that again, Mira.\""
        carr "\"But you understand now.\""
        player "\"I understand you just gave me a pretty good reason to shove my boot down your
                throat!\""
        carr saddened "\"I'm sorry, Mira.\""
        carr neutral "\"But you understand why I had to do that.\""
        player "\"If you think you're little 'lesson' is going to keep me from going out there with
                you, you're sadly mistaken.\""
        
    "I argue some more, but he is adamant about me staying here for at least another day or so."
    "And by then he's hoping he'd have already made contact with some Republic-friendly civilians."
    "But I'm not just going to stay here, am I?"
    "I'm not just going to do what he says, I'm going to ..."
    
    #################################################################################################
    # ACTION CHOICE #################################################################################
    #################################################################################################
    
    menu:
        "Nevermind. I'll stay put.":
            $ good += 5
            $ ch3_stayed_behind = True
            "... do nothing."
            "I sigh, and slump."
            "I guess I'll do what Lieutenant Carr wants and just ... stay put."
            "Yes, that's what I'll do ..."
            "Just ... stay put and wait ..."
        "[N/A] Follow him. Quietly.":
            $ gray += 5
            $ ch3_followed_carr = True
            "... Follow him?"
            "Yes, I could follow him."
            "Quietly."
            "It's not like I really {b}need{/b} his permission or approval."
            "I just have to make sure I sneak out after he leaves and follow him until we're too
             far along to turn back ..."
        "[N/A] Force him to take me with him.":
            $ dark += 5
            $ ch3_forced_carr = True
            "... {b}make{/b} him take me with him."
            "Now, how to do that ...?"
    