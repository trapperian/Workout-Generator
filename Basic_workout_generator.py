# this is a basic workout generator, input according to requests and it will give you a recommended workout for the day.

while (
    True
):  # since it seems that Al Sweigart recommends this for starting all of his programs
    print(
        'Did you do a workout of some sort or other yesterday? (Please use "yes" or "no")'
    )
    prior_wkt = input()
    if prior_wkt == "yes":
        print("Go for a walk for at least half an hour.")
        print(
            "Workout is done for the day, go home, eat your vegetables, drink water, get 8 hours of sleep."
        )
    elif prior_wkt == "no":
        print(
            "This workout recommendation is for an absolute beginner, it's pretty hard to get hurt on this one but standard disclaimers apply of getting doctor approval and  you assume all liability for damages.  This is a coding project, not a fitness recommendation."
        )
        print(
            """
        First and foremost, breathing, you're going to spend 2 minutes doing what is called, \"Crocodile Breathing\" lay on your stomach, put your forehead on your hands and breathe, focusing on your stomach/below the ribcage doing the work of breathing.  Further information: https://www.functionalmovement.com/Exercises/823/crocodile_breathing_with_ankle_weights \n
        Second, roll over onto your back, put your feet up on a wall or chair so that your knees are at roughly a 90 degree angle, 2 more minutes of breathing, focusing on the same action as before.  This is how important breathing is.
        Third, that rolling motion you did to go from prone to supine, do that back and forth, across both sides leading with arms and/or legs for 2 minutes, tomorrow your obliques will want to have a discussion with you.
        Fourth, crawl on your hands and knees for two minutes, this is where the fun really begins. Focus on looking at the horizon and moving opposite arm and legs so left arm, right leg move together, etc.
        Fifth, army crawl for two minutes same focus as before, eyes on horizon, opposite limbs working together
        Sixth, bear crawl, focus on getting your butt as high in the air as possible, 2 minutes still
        Seventh, crab crawl for two minutes.
        After a brief rest, do 'get back ups.' Lie on the floor and then stand up, repeat following positions and rules here: https://www.youtube.com/watch?v=o0_DoicHg2E
        Finally, go take a half hour walk.  That is a total of an hourish of a workout, you've improved your breathing, mobility, neural connections, basic strength, cardio and worked on some of the major killers of U.S. adults daily.
        Go home, drink water, eat vegetables and get 8 hours of sleep.  Continue this workout until you are feeling pretty sure of yourself and feeling 'well put together.' """
        )
    else:
        print("Please use the specific word's 'yes' or 'no'.")
