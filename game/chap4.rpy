#####################################################################################################
# Chapter Four - Sick Leave #########################################################################
#####################################################################################################

label chapter_four:
    
    #################################################################################################
    # Intro #########################################################################################
    #################################################################################################
    
    scene bg chapter four with fade
    play music "music/neutral3.ogg" fadein 2 fadeout 3
    $ renpy.pause(5.0, hard=True)
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene bg ord mantell cave with dissolve
    $ renpy.pause(0.5, hard=True)
    
    if ch3_stayed_behind:
        jump ch4_mira_stayed_behind
    
#####################################################################################################
# Mira Stays Behind Path ############################################################################
#####################################################################################################
    
label ch4_mira_stayed_behind:
    
    #################################################################################################
    # Mira waits for Carr ###########################################################################
    #################################################################################################
    
    if good > max(gray, dark):
        nvnr "As much as I hate to admit it, Lieutenant Carr is probably right. I feel better, stronger
              -- much stronger than I did after waking up from the crash -- but I would still just slow
              him down. There were predators out there and worse -- separatists. If he landed himself in
              a situation where he had to make a run for it, I would be a liability. It was the right
              decision."
    elif gray > max(good, dark):
        nvnr "As much as I'd like to get out of this cave and actually {b}do{/b} something ... I
              have to admit that I'm not so eager to trek all day and maybe night just to see some
              dirt farmers. Finding separatists could certainly make it more interesting, but I
              didn't care to try my luck at tangling with them without any weapons besides Carr's
              one knife. Really, though, the thought of all the work of hiking through that rocky
              Mantellian landscape was what did me in."
    elif dark > max(good, gray):
        nvnr "Carr might be right. Or not. Either way, I'm not going to take the chance of either
              jeopardizing our rescue by tagging along or risk myself out there before I'm strong
              enough either. Let Carr do it. That's what he's good for right now, and he's more
              than willing to at the moment too."
    else:
        "Maybe Carr is right. I guess I had no choice but to defer to him anyways."
    
    nvnr "Of course, realizing that doesn't make it any easier to get up the next morning only to
          find him already gone."
    
    if good > max(gray, dark):
        nvnr "At first, that stung. Did he really think I'd try to follow him or make him take me
              along? I already agreed to stay behind. It was bad enough to be the dead weight in this
              mission equation without being patronized for it too. What good was making the right
              decision if you were robbed of the chance to act on it?"
    elif gray > max(good, dark):
        nvnr "Which annoys me a little."
        nvnr "I already let him have his way and leave me behind. Stars,
              I even {b}agreed{/b} with him. But he just has to go and rob me of the chance to follow
              through on my promise anyways. You'd think he didn't trust me too much ..."
    elif dark > max(good, gray):
        nvnr "Which infuriates me."
        nvnr "I already let him get his way. I stayed behind. I told him I would. Did that mean
              nothing? Apparently not, because he wasn't going to give me a chance to change my
              mind."
    else:
        nvnr "Which annoys me a little. But what am I going to do? It doesn't change the situation."
    
    nvl clear
    nvnr "I spend the next hour or so bouncing back and forth between frustration at and acceptance
          of the situation. I pace around the cave until I get tired, rest, look outside at the rocky
          landscape, and rest again."
    nvnr "I'm not getting fatigued as quickly, though. Moving around {b}is{/b} helping."
    nvl clear
    
    #################################################################################################
    # Carr doesn't come back ########################################################################
    #################################################################################################
    
    nvnr "Carr doesn't get back before nightfall."
    nvnr "That's not too surprising, but it still leaves a hollow pit inside my stomach."
    nvnr "I sit outside and throw rocks at the night sky, waiting to see some sign of him on the
          bluffs. I start to inevitably wonder what I will have to do if he's gone or dead. But those
          thoughts are bleak. Eventually, I go to sleep, hoping he'll be back with some good news -- or
          even better, {b}help{/b} -- in the morning."
    nvl clear
    stop music
    play music "music/tension.ogg" fadein 2 fadeout 3
    $ renpy.pause(0.5, hard=True)
    player wincing "\"... mmmph ...\""
    "I awake with an even worse feeling than the one I had last night about Carr being dead."
    player alarmed "\"Lieutenant ...?\""
    "I jerk upwards and immediately regret it."
    "My side throbs at that sudden motion and I wince, cupping my almost-healed hand around my
     almost-healed wound."
    "The cave is empty."
    "I look around, sure that I felt something that woke me up."
    "No one's here, though -- certainly not the lieutenant -- so I gently lie myself back down."
    "Then I hear it."
    "Voices."
    "Voices ... outside ..."
    "I sit back up, not sure what to think at first."
    "There are more than one, and they're getting closer."
    "I stand up carefully and listen ..."
    "... but I don't hear Carr."
    "And that makes me suddenly wary."
    "Somehow I doubt he sent others back here to help me without coming himself."
    "Even if he had, I don't have to take that chance."
    "I've been stuck in here for days on end without anything much to do."
    "I know how deep the cave goes. I know each wall and corner and stalagmite like it was my home."
    "It has been -- a terrible, claustraphobic home."
    "So it's not so difficult to find a place to quickly hide before those voices get in here
     to find me."
    "I squeeze back behind an outcropping of rock that you'd barely notice had a space behind it
     from the cave proper and I could still see out without being easily seen myself."
    "Then I wait ..."
    "... until two men stomp inside, blasters in hand and ready to shoot."
    show sep1 at left
    show sep2 at right
    "..."
    "... ..."
    sep1 "\"Doesn't look like he had anyone else with him.\""
    sep2 "\"Unless whoever it was got away already ...\""
    sep1 "\"Lucky for them then.\""
    "Both those two men holster their blasters after checking around the cave."
    "They don't find me or even notice my hiding spot."
    "I watch them start digging through the emergency supplies we had left eagerly, starting to
     pick out the food and water and anything that looks even meagerly valuable."
    "I watch, unsure of what to do, but sure that they are going to leave me here to die without
     any provisions."
    "But I can't let that happen."
    "I can't."
    "I'm not just going to die here on this rock without doing anything."
    if good > max(gray, dark):
        "And Lieutenant Carr probably needs my help."
    elif gray > max(good, dark):
        "Besides, it's pretty obvious Carr found himself some trouble."
        "And who else was going to save him, if not me?"
    elif dark > max(good, gray):
        "And Carr is obviously in trouble."
        "I should've known better than to let him go off without me, no matter what he said."
    "But first ..."
    "I have to do something about these two ..."
    
    #################################################################################################
    # ACTION CHOICE #################################################################################
    #################################################################################################
    
    menu:
        "I don't want to kill them. I can sneak out and try to steal their vehicle without them
         noticing.":
            $ good += 5
            jump ch4_mira_evades_seps_in_cave
        "*NOT IMPLEMENTED* I hate to risk it, but ... these two have information I need. I'll try to subdue them first.":
            $ gray += 5
            jump ch4_mira_subdues_seps_in_cave
        "*NOT IMPLEMENTED* These two are obviously seps and wouldn't hesitate to kill me or worse. 
         So I'll kill them first ...":
            $ dark += 5

    #####################################################################################################
    ## Mira Evades Seps in Cave Action Path #############################################################
    #####################################################################################################

label ch4_mira_evades_seps_in_cave:
    if good > max(gray, dark):
        "I don't want to kill these men."
        "Maybe I can just sneak past them ..."
    elif gray > max(good, dark):
        "As much as I'd love to hang around and watch these fascinating locals steal our equipment ..."
        "Maybe it'd be best if I made a hasty exit while they were distracted ..."
    elif dark > max(good, gray):
        "I wish I could take both of these fools down right now -- maybe force some answers out of them
         -- but I'm not stupid. They're armed, I'm not. Best to make a break for it while they're busy
         raiding our things."
    else:
        "I have to get past these two."
    "They had to have come here in some kind of vehicle."
    "I doubt they just walked here, or stumbled across this cave and happened to know to look inside."
    "No, it was pretty obvious that Carr had been intercepted, maybe even captured or killed."
    "And these two had probably followed his trail back."
    "It's not like he would have bothered hiding it."
    "So I wait. I wait until both men are rummaging through our emergency med kits with their backs to me
     and the entrance."
    "Then I move."
    sep2 "\"A lot of kolto missing for a guy that didn't look too banged up ...\""
    sep1 "\"Hm.\""
    "I creep around the rock face, painfully aware of how exposed I am until I'm through the entryway."
    "A good blaster shot at this range would cut this whole thing short real quick."
    "I try not to think about that, though -- just focus on stepping lightly and carefully and not
     making any noise loud enough to be heard over those two stealing our things ..."
    "..."
    "Surprisingly, I make it out of sight without incident."
    hide sep1
    hide sep2
    "The twisting rockface of the entrance swallows me whole and the probably-seps don't notice a thing."
    "... Too bad there's a third one waiting with their landspeeders outside."
    scene bg ord mantell speeders with dissolve
    show sep3
    stop music
    play music "music/combat2.ogg" fadein 2 fadeout 3
    sep3 "\"What the--\""
    
    #####################################################################################################
    ### Mira Defeats Separatists ########################################################################
    #####################################################################################################
    
    "My feet are moving before I can even fully process that situation I just blundered into, carrying me
     forward."
    "Then I'm charging at that man standing beside their speeders."
    "He reaches for his blaster on the hood, but I'm on top of him before he can shoot."
    sep3 "\"Gah!\""
    "Instinct takes over and continues carrying me along with it."
    "My good hand swings down on his arm with the blaster, just above the wrist."
    "He misfires, and a bolt fizzles into the dirt."
    "I'm moving again before he can recover, my right hand slicing back up instantly, gouging him in the 
     throat."
    sep3 "\"Gggng!\""
    "I push him since he's already stumbling back, and he topples over, hitting the back of his head hard
     on the wing of his speeder."
    "He stays down after that."
    hide sep3
    player alarmed "..."
    "I suck in a deep, steadying breath -- not realizing how much sudden force I'd actually put into that
     whole attack after so long idling in the cave."
    player "\"So much for sneaking out quietly ...\""
    "I stare at that man's body for a second before snatching his blaster up out of the dirt."
    "I can already hear the other two rushing out of the cave, shouting for the guy on the ground."
    "They're not ready for my ambush, though, and I crouch down behind the landspeeder."
    "Switching the blaster to stun, I fire as soon as I see both of those other two come out."
    "They're down, unconscious and in a heap, before they even realize what's happening."
    stop music
    
    #####################################################################################################
    ### Mira Escapes ####################################################################################
    #####################################################################################################
    
    play music "music/tension2.ogg" fadein 2 fadeout 3
    player awed "..."
    player "\"Stars ...\""
    "I had no idea I had those kind of reflexes when I tried to escape the cave unnoticed, but they'd
     saved my life."
    "I've obviously had some training -- those weren't the combat skills of a regular deck hand for a
     naval vessel."
    "The question was, of course, from {b}who{/b} ...?"
    player scowling "{i}Does it really matter right now{/i}?"
    "No."
    "Now that I stop and think about it, though, I realize I know exactly how I disabled that guy before
     he could even fire his gun. It wasn't just reflex."
    "The knowledge is in my head now that I'm aware of it."
    "Those shots too -- near-perfect aim."
    "Well, good enough anyways."
    "I know how to shoot, and I'm pretty confident I could hold my own against a few of these locals
     now that I'm properly armed."
    "Which is ... good, I guess."
    player "\"Stars, I must have been a marine or something.\""
    "I mutter that out loud as I grab the backpacks full of our supplies from the two stunned men on
     the ground and toss them in one of the speeders."
    "Or something ..."
    "Maybe Carr was right? Maybe I {b}am{/b} some kind of Imperial spy?"
    "Who knows ..."
    "That doesn't matter right now."
    "What matters is figuring out what happened to Carr and doing something about it."
    
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    
    #####################################################################################################
    ## Mira Subdues Seps in Cave Action Path ############################################################
    #####################################################################################################
    
label ch4_mira_subdues_seps_in_cave:

    if good > max(gray, dark):
        "I'm not getting out of here without dealing with these two, and I'm not just going to watch them
         leave with all my supplies."
        "That, and they probably know where Carr is."