define j = Character("Jazi", color="#c84fc8")
define food_choice = None
define activity_choice = None

image bedroom = "images/backgrounds/bedroom.jpg"
image kitchen = "images/backgrounds/kitchen.jfif"
image blackhole = "images/backgrounds/blackhole.jpg"

image jazi neutral = "images/queenofzan/cd neutral.png"
image jazi concerned = "images/queenofzan/cd concerned.png"
image jazi embarrassed = "images/queenofzan/cd embarrassed.png"
image jazi annoyed = "images/queenofzan/cd annoyed.png"
image jazi happy = "images/queenofzan/cd happy.png"
image jazi know it all = "images/queenofzan/cd know it all.png"
image jazi sleeping = "images/queenofzan/jazi sleepingg.png"
image jazi surprised = "images/queenofzan/cd surprised.png"


#START OF THE GAME
label start:
    play music "audio/music2.mp3" fadein 0.5
    scene kitchen:
        xysize (1920, 1080)
    with fade
    with vpunch
    show jazi neutral with dissolve #cuz we don't have a jazi tired/stressed
    j "Ugh… {w=0.005}I've {w=0.005}had {w=0.005}a {w=0.05}long {w=0.1}long {w=0.1} day... "

    menu:
        "What did Jazi eat today?"
        "Deep-dish pizza!":
            $ food_choice = "pizza"
            call regardless
            call pizza_path

        "Boba at midnight!":
            $ food_choice = "boba"
            call regardless
            call boba_path
    
    jump part2


label regardless:
    scene bedroom:
        xysize (1920, 1080)
    with fade
    show jazi neutral with dissolve
    play sound "audio/snoringsound.mp3"
    j "zzzzz"

    stop music fadeout 1.0
    stop sound fadeout 2.0
    play music "audio/suspense.mp3" fadein 0.5
    scene blackhole with fade
    pause 3.0
    show blackhole at shrinkout
    return


label pizza_path:
    #run pizza game
    renpy.emscripten.run_script('swapDisplay("game")')
    renpy.emscripten.run_script('loadMinigame("pizza")')
    #..

    play music "audio/music2.mp3" fadein 0.5 #other background music
    scene bedroom:
        xysize (1920, 1080)
    with fade #CHANGE TO BEDROOM AFTER
    
    show jazi embarrassed with dissolve:
        xalign 0.5 yalign 1.0 zoom 1.0
        linear 0.5 zoom 1.2
    j "Pizza in my sleep?? I must have eaten too much!..."
    return


label boba_path:
    #run boba game
    renpy.emscripten.run_script('swapDisplay("game")')
    renpy.emscripten.run_script('loadMinigame("boba")')
    #..
    play music "audio/music2.mp3" fadein 0.5 #other background music
    scene bedroom:
        xysize (1920, 1080)
    with fade
    show jazi embarrassed with dissolve:
        xalign 0.5 yalign 1.0 zoom 1.0
        linear 0.5 zoom 1.2
    j "Dreaming of boba?? {w=0.5} Maybe, I shouldn't have had boba by 1.a.m in the morning... Like who does that??"
    return

transform shrinkout:
    zoom 1.0
    alpha 1.0
    ease 0.7 zoom 0.0 alpha 0.0



#NEXT PART
label part2:
    show jazi know it all with dissolve
    j "I'll just go back to sleep!"

    show jazi neutral with dissolve
    j "So tired... I hope I don't have another crazy dream again..."

    menu:
        "What did Jazi do during the day?"
        "Went to see the bean":
            $ activity_choice = "bean"
            call regardless
            call the_bean_path
        "Pulled up an all-nighter for a hackathon!":
            $ activity_choice = "hackathon"
            call regardless
            call hackathon_path
    jump ending

label the_bean_path:
    #run the bean game
    renpy.emscripten.run_script('swapDisplay("game")')
    renpy.emscripten.run_script('loadMinigame("bean")')
    #..
    play music "audio/music2.mp3" fadein 0.5 #other background music
    scene bedroom with fade
    show jazi concerned with dissolve:
        xalign 0.5 yalign 1.0 zoom 1.0
        linear 0.5 zoom 1.2
    j "Dreaming about the bean? What do you mean?"
    return

label hackathon_path:
    #run the hackathon game
    renpy.emscripten.run_script("swapDisplay("game")")
    renpy.emscripten.run_script("loadMinigame("hack")")
    #..
    play music "audio/music2.mp3" fadein 0.5 #other background music
    scene bedroom with fade
    show jazi annoyed with dissolve:
        xalign 0.5 yalign 1.0 zoom 1.0
        linear 0.5 zoom 1.2
    j "All-nighter hackathon is crazy, bruh!"
    return



# last parttttt
label ending:
    play music "audio/music2.mp3" fadein 0.5 #some music here
    show jazi know it all with dissolve
    
    if food_choice == "pizza":
        $ food_text = "eating pizza"
    elif food_choice == "boba":
        $ food_text = "drinking boba"
    else:
        $ food_text = " "

    if activity_choice == "bean":
        $ activity_text = "going to the bean"
    elif activity_choice == "hackathon":
        $ activity_text = "hacking all night"
    else:
        $ activity_text = " "

    
    j "Hmm! [food_text] and [activity_text]?? I had a long day at Sleepover!"

    show jazi neutral with dissolve
    j "All thanks to Reem! {w=0.5} Now, back to sleep!"
    return