#####################################################################################################
# Chapter One - Retrograde ##########################################################################
#####################################################################################################

label chapter_one:
    
    #################################################################################################
    # Intro #########################################################################################
    #################################################################################################
    
    scene bg chapter one with fade
    play music "music/tension.ogg" fadein 2 fadeout 1
    $ renpy.pause(5, hard=True)
    play sound "sfx/klaxons.ogg"
    scene black with fade
    
    #################################################################################################
    # Mira wakes up and panics ... ##################################################################
    #################################################################################################
    
    scene bg chapter one with fade
    play music "music/tension.ogg" fadein 2 fadeout 1
    $ renpy.pause(5, hard=True)
    play sound "sfx/klaxons.ogg"
    scene black with fade
    "Klaxons."
    player frustrated "\"Mmmph ...\""
    "There's something heavy on my back."
    scene bg justiciar corridor dead with dissolve
    $ renpy.pause(0.1, hard=True)
    scene black with dissolve
    $ renpy.pause(0.25, hard=True)
    scene bg justiciar corridor dead with dissolve
    $ renpy.pause(0.5, hard=True)
    "I blink my eyes open and see blood in front of my face dripping from clumps of hair."
    player alarmed "{i}That's ... {/i}"
    player alarmed "{i}... not good.{/i}"
    "I try to move a hand to my head but realize I'm pinned down by that thing on top of me."
    "It's digging into my back and making my muscles go numb all over."
    "Suddenly, I feel like I'm suffocating." 
    "I'm crushed down on the floor beneath something heavy and metal and I can't move or breathe."
    "I thrash around, trying to move something -- {b}anything{/b} ..."
    "... Everything hurts."
    "Why does everything hurt?"
    "I'm dying."
    "I'm trapped and broken and I'm dying and nobody is going to help me."
    player frustrated "{i}Focus.{/i}"
    
    #################################################################################################
    # Mira gets some perspective on her situation ... ###############################################
    #################################################################################################
    
    nvnr "I hold my breath and count to five. It helps. 
          It makes me stop thinking about having all the life crushed out of me so much 
          and actually look around at where I am."
    nvnr "Those warning sirens are still blaring. What happened? 
          I'm in some kind of corridor made of metal, but the whole place is falling apart. 
          Ceiling falling down, durasteel walls burst apart 
          and fires licking up and down panels and corpses."
    nvnr "Corpses."
    nvnr "I'm alone and there are dead bodies all around me in the corridor. 
          At least -- they look dead. 
          Most of them seemed blasted or burned ... like this whole place exploded or ..."
    play sound "sfx/explosion.wav"
    with Shake((0, 0, 0, 0), 3.0, dist=30)
    nvl clear
    nvnr "The ground shakes."
    nvnr "Another explosion."
    nvnr "It feels dull, like it's coming from somewhere far away 
          but still close enough to have done this kind of damage."
    nvnr "But all of this doesn't change the fact that I'm wounded and maybe dying 
          and still have a couple hundred pounds of durasteel crushing me into the floor."
    nvl clear
    
    #################################################################################################
    # Mira tries to move ... ########################################################################
    #################################################################################################
    
    $ renpy.pause(0.25, hard=True)
    player neutral "{i}Right.{/i}"
    "I put pressure on both my hands, pushing." 
    "A sharp jolt of pain lances through my whole arm."
    player frustrated "{i}!!!{/i}"
    "My left hand is crushed beneath me."
    player frustrated "{i}Just ... {b}perfect{/b}{/i}."
    "I'm pretty sure it's broken."
    "The right hand hurts, but, thankfully, still seems to work."
    "My legs too, as far as I can tell, flexing them."
    player alarmed "{i}Push.{/i}"
    player frustrated "\"Nngggg!\""
    play sound "sfx/metal_creak.wav"
    with Shake((0, 0, 0, 0), 1.0, dist=15)
    stop sound
    "With all three of the limbs I have left trying to force me away from the floor -- 
     I feel that weight digging into my spine shift just the slightest bit."
    "Then I collapse."
    play sound "sfx/door_slam.wav"
    with Shake((0, 0, 0, 0), 0.5, dist=10)
    "I'm breathing hard with one cheek squashed flat against the metal floor littered 
     with ash and debris."
    "... I could just ... lie here ... for a little while ..."
    
    #################################################################################################
    # Mira tries again ... ##########################################################################
    #################################################################################################
    
    player alarmed "{i}No ...{/i}"
    "No."
    player frustrated "{i} Come on ...{/i}"
    player frustrated "{i} ... just one more time.{/i}"
    "A few more breaths and I push with everything I've got left all over again."
    play sound "sfx/metal_creak.wav"
    with Shake((0, 0, 0, 0), 0.5, dist=10)
    "It isn't much."
    player frustrated "\"... mmmmh ...!\""
    "My legs start to buckle at the knee."
    "They're at a bad angle and it's hard to make them work right."
    "I end up kicking at the floor, just trying to keep enough of a grip to push."
    "..."
    play sound "sfx/metal_creak.wav"
    with Shake((0, 0, 0, 0), 0.5, dist=10)
    stop sound
    "Just a little more ..."
    play sound "sfx/metal_creak.wav"
    with Shake((0, 0, 0, 0), 0.5, dist=10)
    "..."
    with Shake((0, 0, 0, 0), 0.5, dist=10)
    play sound "sfx/door_slam.wav"
    player alarmed "\"... aaah!\""
    
    #################################################################################################
    # Mira gets free ... ############################################################################
    #################################################################################################
    
    nvnr "The thing shifts just enough for me to start squeezing myself out from underneath. 
          My whole body wants to shut down -- drained and breathing hard 
          and probably too messed up to even stand -- 
          but I ride that momentum out a few more seconds. 
          I just manage to claw my way out from beneath that thing and then flop over onto my back."
    nvnr "It hurts. For a few seconds  my lungs are working so hard 
          and my heart beating so fast that I'm sure they'll both explode right out of my chest. 
          Those seconds stretch on like minutes."
    play sound "sfx/explosion.wav"
    with Shake((0, 0, 0, 0), 3.0, dist=30)
    stop sound
    nvl clear
    nvnr "The ground shakes again."
    nvnr "I'm starting to think I might not be somewhere entirely stable."
    nvnr "I blink around the corridor again, not wanting to move anymore right now, 
          but I can't see much more than I could before. One of those dead bodies is next to me, 
          but I'm too tired to move away or do anything else."
    nvnr "I get a good look at that thing that was crushing me and it looks like a girder had stabbed 
          it's way down through the ceiling. 
          There's a mess of ripped wiring trailing like snakes all around it. 
          It looks heavier than it felt. It looks like it should've killed me."
    nvnr "My head still hurts and I think that girder must have hit me on the way down."
    nvl clear
    "I have to get moving."
    play sound "sfx/explosion.wav"
    with Shake((0, 0, 0, 0), 3.0, dist=50)
    stop sound
    play sound "sfx/klaxons.ogg"
    "Almost as if to agree with me, the corridor groans and there's another explosion somewhere 
     -- louder and much, much closer this time."
    "Those klaxons."
    "... the explosions ..."
    "... the ground ... shaking?"
    "It dawns on me that I might actually be onboard a ship under attack."
    "That or maybe a bunker."
    play music "music/chase.ogg" fadein 1 fadeout 2
    "Under attack and {b}losing{/b} by the sounds of it."
    "I have to get moving. I {b}have{/b} to get away from here."
    "Now."
    nvnr "I suck in a few more breaths now that my lungs aren't trying to explode and I try my legs. 
          They still work enough to use with my one good hand to push up off the floor. 
          Slowly. My left hand I cradle to my stomach and just try not to move at all. 
          Just the effort of getting out from under that girder made me never want to move it again."
    nvnr "Pushing, pushing, pushing, and ... I'm on my knees now, feeling light-headed 
          and looking down the corridor at a much improved altitude. 
          The motion makes me feel sick, though, blood rushing out of my skull. 
          Some trickles down into my left eye and I remember the small puddle that had been in my 
          face on waking. I go to touch a hand to my forehead but almost throw up. 
          I nearly black out too, but end up just losing my balance instead."
    nvl clear
    
    #################################################################################################
    # Mira gets injured ... #########################################################################
    #################################################################################################
    
    $ renpy.pause(0.25, hard=True)
    player meditative "..."
    player frustrated "!!!"
    play sound "sfx/squish.wav"
    "The next thing I know something is sticking right into my side."
    player alarmed "{b}Mmmph!{/b}"
    nvnr "I glance down, wide-eyed with an overwhelming pain that pushes through all that numbness 
          and threatens to make me pass out again right there. 
          I'm at an angle and on top of that girder that had trapped me against the floor. 
          I can't see what happened, but I can {b}feel{/b} it. My blood is painting the durasteel."
    play sound "sfx/explosion.wav"
    with Shake((0, 0, 0, 0), 3.0, dist=30)
    stop sound
    nvl clear
    nvnr "The corridor's shaking."
    nvnr "It shakes the girder and that thing stabbing my guts and I cry out, shoving myself away. 
          I land against the side of the wall instead, that blackened corpse underneath me, 
          and stare at the bloody shard of durasteel sticking out of the side of the girder that 
          had punctured my side. My hand is clutching the spot where it was and I look down, 
          pulling away. My palm fills with more blood."
    nvl clear
    $ renpy.pause(0.25, hard=True)
    player alarmed "{i}... Perfect!{/i}"
    
    #################################################################################################
    # Mira gets help ... ############################################################################
    #################################################################################################
    
    nvnr "Have to keep moving."
    nvnr "Have to keep moving ..."
    nvnr "That mantra in my head is the only thing I focus on. A new desperation gets me up off the 
          floor and stumbling forward. My legs aren't as good as I thought they were, and I have to 
          hold onto the wall to my right for support as I start pulling myself toward the end of 
          the corridor."
    nvnr "The lights flicker -- or was it my vision? I feel like I'm going to pass out or collapse 
          and survival instinct is the only thing keeping me on my feet while my stomach bleeds 
          out into my hand."
    nvnr "Then someone comes rushing past the end of the corridor."
    nvl clear
    $ renpy.pause(0.25, hard=True)
    play sound "sfx/klaxons.ogg"
    player alarmed "\"... {b}Hey!{/b}\""
    "I manage to gasp out on reflex and instantly regret it, nearly losing my feet again." 
    "I hug the wall, squeezing my eyes shut and put my good hand back on that 
     bleeding wound in my side."
    crewman alarmed "\"You okay?\""
    "That someone heard me."
    "Good."
    "Great."
    "Fanastic ..."
    "Because I have no idea where I am, where I need to go to get out of here, or even {b}if{/b} I'll 
     still be alive when I get there."
    crewman alarmed "\"Ma'am? You gonna make it?\""
    "His hand is on my shoulder, trying to help steady me." 
    "I barely feel it, still clinging to the wall and bent nearly double."
    player frustrated "\"I ...\""
    player "\"I don't know.\""
    "I manage to shake my head."
    crewman alarmed "\"Just ...\""
    crewman neutral "\"Come on.\""
    show crewman
    crewman "\"The ship's breached and won't last much longer.\""
    crewman "\"We have to get to the escape pods.\""
    "I take another step, pushing off from the wall."
    "Pain erupts all up my injured side."
    "Sucking in air through teeth that feel like they're wired shut, I freeze there in midstep."
    player "\"I ...\""
    player "\"I'm not sure if I'm {b}going{/b} anywhere ...\""
    nvnr "He puts an arm around my shoulders and forces me into a hobble. The pain comes back with 
          each step, but I don't get a chance to stop. 
          He doesn't let me do anything but push through it, growling deep in my throat while I do."
    scene bg justiciar corridor console with fade
    nvnr "Other people join us in a mad rush as we stumble out into a bigger corridor. 
          They're charging the same way we turn, though much faster and in ragged, desperate packs. 
          All in uniform, I notice briefly, but the pain in my side forces most everything else out."
    nvl clear
    play sound "sfx/explosion.wav"
    with Shake((0, 0, 0, 0), 2.0, dist=50)
    stop sound
    nvnr "The deck rocks and people topple off their feet. We almost do too, 
          but that crewman keeps us upright somehow. 
          It occurs to me that I probably wouldn't make it very far on my own ... "
    nvnr "... But this crewman could. And much faster. 
          If he wasn't trying to drag me along with him."
    
    #################################################################################################
    ## THOUGHT OPTION ###############################################################################
    #################################################################################################
    
    menu:
        "I'm holding him back. I'm probably dead already.":
            $ good += 3
            nvnr "I'm as good as dead anyways with this wound bleeding me dry. I won't make it. 
                  And this poor man shouldn't die because of me."
            nvnr "I open my mouth to tell him to leave me behind, 
                  but I end up coughing up blood instead."
            nvnr "\"Come on!\" he yells in my ear over all the noise of warning sirens and explosions 
                  and people scrambling for safety too. \"Don't die on me yet!\""
        "I don't have any choice. I don't want to die.":
            $ gray += 3
            nvnr "A flash of all those dead people back in the corridor I woke up in is enough to 
                  keep me quiet, though. I'm too afraid to die here like that. 
                  And it hurts too much to say anything anyways."
        "I won't die here! I won't be left here to die!":
            nvnr "I bite my tongue from saying anything. I have to survive. 
                  I have to survive this no matter what."
            $ dark += 3
    
    #################################################################################################
    
    nvl clear
    nvnr "I start to flicker between seeing and not, trying to focus on just keeping one foot going 
          in front of the other -- one at a time. One at a time. On and on."
    nvnr "It doesn't end. I think that crewman might be saying something to me, 
          or maybe someone else, but I can't pay attention enough to hear it. 
          I wouldn't have made it on my own is certain. I'm barely making it {b}now{/b}."
    nvl clear
    
    #################################################################################################
    # Mira escapes ... ##############################################################################
    #################################################################################################
    
    play sound "sfx/klaxons.ogg"
    "I trip, and fall over."
    "No."
    "That crewman is trying to get me to climb up into something."
    "An escape pod."
    scene bg justiciar escape pods with fade
    nvnr "I force my eyes open and stop holding my bleeding stomach in long enough to help get me 
          into the pod. The explosions are all around us now, but I can barely feel them anymore. 
          Everything is collapsing down to a point inside my head and I just try to keep enough 
          sense to make my one good hand work."
    nvnr "I crawl."
    nvnr "I pull."
    nvnr "And ..."
    nvl clear
    $ renpy.pause(0.25, hard=True)
    "I'm inside."
    "I flop over into the small compartment and tumble into one of the sides."
    "I don't feel anything hit me, but ..."
    "I'm far too gone to care. I just lay there."
    "Then consciousness drifts quickly, and silently away."
    play sound "sfx/explosion2.wav"
    with Shake((0, 0, 0, 0), 2.0, dist=50)
    scene black with fade
    $ renpy.pause(1, hard=True)
    stop music
    $ renpy.pause(2, hard=True)
    
    #################################################################################################
    # End ###########################################################################################
    #################################################################################################
    
    jump chapter_two