"""A program for an adventure game."""


print("Welcome to the Adventure Game!\n Welcome to the Isle of the Forgotten.")
print("After a violent storm at sea,\
you awake on the beach of a strange island shrouded in mist and mystery.\n Your only goal is to survive—and uncover the secrets hidden deep\
within the island's ancient ruins, eerie jungles, and long-abandoned villages.")
print("You wake up on the beach, soaked and bruised.\
The wreckage of your ship is scattered around.\n You see something glinting in the sand nearby and hear distant animal calls\
coming from the jungle.\n You must act quickly before night falls.\n")

choice1 = input(
    "Do you SEARCH the wreckage for supplies, HEAD into the jungle,\
 INVESTIGATE the glinting object? ").strip().lower()

if choice1 == "search":
    print("\nYou find a compass, a broken flare gun, and a journal with strange symbols.\
 You gain important tools for navigation.")
    choice2 = input(
        "Do you EXAMINE the journal, LIGHT the flare gun,\
 or CONTINUE into the jungle with the compass? ").strip().lower()

    if choice2 == "examine":
        print("\nThe journal contains cryptic notes about\
 the island's history and warnings about its dangers.\
 You gain little knowledge and get the code to deciper the notes.")
        choice3 = input(
            "Do you DECIPHER the notes, IGNORE them, or CONTINUE into the jungle? ").strip().lower()

        if choice3 == "decipher":
            print("\nYou spend time deciphering the notes.\
 They reveal the island's ancient civilization and\
 hint at a hidden treasure guarded by a mythical beast.\
 You gain valuable information.")
        elif choice3 == "ignore":
            print("\nYou decide the notes are too cryptic and ignore them.\
 You gain nothing but lose time.")
        elif choice3 == "continue":
            print("\nYou continue to wander the forest and eventually\
 get lost and stranded on the island forever")
        else:
            print(
                "That’s not a valid choice. The forest rejects\
 your indecision. You vanish into the mist.")
    elif choice2 == "light":
        print("\nYou light the flare gun to signal for help.")
        choice3 = input(
            "Do you shoot the flare into the SKY, towards the FOREST,\
 or into the OCEAN? ").strip().lower()

        if choice3 == "sky":
            print("\nThe flare shoots into the sky, illuminating the island.\
 You see a distant ship approaching! You gain hope and rescue.")
        elif choice3 == "forest":
            print(
                "\nYou set the forest on fire attracting\
 the attention of wild animals on the island")
        elif choice3 == "ocean":
            print("\nA wave crashes, extinguishing the flare.\
 You are left stranded with no hope of rescue.")
        else:
            print("That is not a valid choice. The forest swallows\
 you making you forfiet your life and adventure")
    elif choice2 == "continue":
        print("\nYou decide to continue into the jungle with the compass.")
        choice3 = input(
            "Do you CLIMB a tree to get a better view,\
 FOLLOW a river deeper into the jungle,\
 or BUILD a shelter for the night? ").strip().lower()

        if choice3 == "climb":
            print("\nYou climb a tree and spot a village in the distance.\
 You gain a vantage point and plan your next move.")
        elif choice3 == "follow":
            print("\nYou follow the river deeper into the jungle.\
 You find fresh water but also dangerous wildlife.")
        elif choice3 == "build":
            print("\nYou build a shelter for the night.\
 You gain safety but lose time exploring.")
        else:
            print("That is not a valid choice. The forest rejects your indecision.")
    else:
        print("That is not a valid choice. The ocean becomes hostile, and you drowns you.")
elif choice1 == "head":
    print("After braving the thick jungle, you find a fork in the trail.\
 One leads toward a smoky mountain, the other to a ruined stone\n temple partly overtaken by vines. A third path\
 heads toward the sounds of rushing water.")
    choice2 = input("Do you choose to GO to the smokey mountain,\
 EXPLORE the stone temple, or FOLLOW the sound of the water? ").strip().lower()

    if choice2 == "go":
        print("You reach a dormant volcano with signs of\
 recent activity.\nSmoke seeps from cracks in the rock.\
 You spot strange footprints leading into a nearby cave.")
        choice3 = input("Do you choose to LEAVE the area,\
 ENTER the cave, or INVESTIGATE the strange footprints").strip().lower()

        if choice3 == "leave":
            print("You escape whatever was coming, but the you were never seen again.")
        elif choice3 == "enter":
            print("You bravely enter the cave,\
 finding it dark and damp.\nStrange echoes fill the air as you venture deeper.")
        elif choice3 == "investigate":
            print("You follow the footprints, leading you\
 to a hidden clearing with ancient carvings on the rocks.")
        else:
            print("That is not a valid choice. The volcano erupts, burying you in ash.")
    elif choice2 == "explore":
        print("You enter the stone temple, finding it filled with ancient artifacts and murals.\
 The air is thick with dust and mystery.")
        choice3 = input("Do you EXAMINE the murals,\
 SEARCH for hidden passages, or LEAVE the temple? ").strip().lower()

        if choice3 == "examine":
            print("You study the murals, revealing secrets about the island's past.\
 You gain knowledge but also attract unwanted attention.")
        elif choice3 == "search":
            print(
                "You search for hidden passages, finding a secret room filled with treasures.")
        elif choice3 == "leave":
            print("You leave the temple, deciding to explore elsewhere.")
        else:
            print(
                "That is not a valid choice. The temple collapses, trapping you inside.")
    elif choice2 == "follow":
        print("You follow the sound of rushing water, leading you to a beautiful waterfall.\
 The water sparkles in the sunlight, creating a serene atmosphere.")
        choice3 = input("Do you DRINK from the waterfall,\
 SWIM in the pool below, or CLIMB behind the waterfall? ").strip().lower()

        if choice3 == "drink":
            print("You drink from the waterfall, feeling rejuvenated and refreshed.")
        elif choice3 == "swim":
            print("You swim in the pool, enjoying the cool water and tranquility.")
        elif choice3 == "climb":
            print(
                "You climb behind the waterfall, discovering a hidden cave with ancient relics.")
        else:
            print(
                "That is not a valid choice. The waterfall sweeps you away into the unknown.")
    else:
        print("That is not a valid choice. The jungle becomes hostile, and you are lost forever.")
elif choice1 == "investigate":
    print("You approach the glinting object, revealing it to be a strange artifact.\
 It hums with energy and seems to pulse with a life of its own.")
    choice2 = input("Do you TOUCH the artifact,\
 STUDY it from a distance, or LEAVE it alone? ").strip().lower()

    if choice2 == "touch":
        print("You touch the artifact, feeling a surge of energy.\
 Your mind is flooded with visions of the island's history.")
        choice3 = input("Do you EMBRACE the visions,\
 FIGHT against them, or RUN away from the artifact? ").strip().lower()

        if choice3 == "embrace":
            print("You embrace the visions, gaining profound knowledge about the island's secrets.\
 You become one with the island's history.")
        elif choice3 == "fight":
            print("You fight against the visions, causing the artifact to explode.\
 You are thrown back, losing consciousness.")
        elif choice3 == "run":
            print("You run away from the artifact, escaping its power.\
 You feel a sense of relief but also a lingering curiosity.")
        else:
            print("That is not a valid choice. The artifact reacts violently,\
 and you are consumed by its power.")
    elif choice2 == "study":
        print("You study the artifact from a distance,\
 noting its intricate designs and mysterious symbols.")
        choice3 = input("Do you RECORD your observations,\
 IGNORE the artifact, or TRY to decipher its symbols? ").strip().lower()

        if choice3 == "record":
            print("You record your observations,\
 gaining valuable insights into the artifact's purpose.\
 You feel a sense of accomplishment.")
        elif choice3 == "ignore":
            print("You ignore the artifact, deciding it is too dangerous to interact with.\
 You gain nothing but avoid potential harm.")
        elif choice3 == "try":
            print("You try to decipher the symbols,\
 revealing a map of the island's hidden locations.\
 You gain valuable knowledge for your journey.")
        else:
            print("That is not a valid choice. The artifact reacts violently,\
 and you are consumed by its power.")
    elif choice2 == "leave":
        print("You decide to leave the artifact alone, respecting its mystery.")
        choice3 = input("Do you RETURN to the beach,\
 CONTINUE exploring the jungle, or SEEK help from the villagers? ").strip().lower()

        if choice3 == "return":
            print("You return to the beach, finding your shipwrecked crew.\
 You gain companionship and a chance to escape the island but\
 have feeling you lost something valuable.")
        elif choice3 == "continue":
            print(
                "You continue exploring the jungle, uncovering new paths and hidden treasures.")
        elif choice3 == "seek":
            print(
                "You seek help from the villagers, gaining allies and resources for your journey.")
        else:
            print("That is not a valid choice. The jungle becomes hostile,\
 and you are lost forever.")
    else:
        print("That is not a valid choice. The artifact reacts violently,\
 and you are consumed by its power.")
else:
    print("That is not a valid choice. The island rejects your indecision,\
 and you are lost forever.")
