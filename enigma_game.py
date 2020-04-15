
def split(text):
    # print(text.splitlines())
    for line in text.splitlines():
        print(line)
        if input() == "":
            continue

def multi_choice(question_dict):
    while True:
        split(question_dict["question"])
        print("Type your answer: ")
        answer = input()
        if answer == question_dict["right"]:
            split(question_dict["right_path"])
            break
        elif answer == "":
            pass
        else:
            split(question_dict["wrong_path"])
            continue

def print_textfile(textfile_dict):
    filename = textfile_dict["textfile"]
    textfile = open(filename,"r")
    diagram = textfile.read()
    print(diagram)

print_textfile({"textfile": "ascii_enigma.txt"})
welcome = "Welcome to the Enigma Game. Make sure your console is on fullscreen. Click enter to continue."
split(welcome)
print("Appendix:\n\t(0) Beginning\n\t(1) Enigma sent to Poland\n\t(2) Hans Thilo Schmidt leaks document\n\t(3) Rejewski works on Enigma\n\t(4) What is the Enigma?\n\t(5) Rejewski breaks the Enigma\n\t(7) Rejewski breaks Enigma\n\t(6) Double enciphered fingerprints\n\t(7) U-33\n\t(8) Bletchly park\n\t(9) Capture of krebs\n\t(10) Operation primrose")
print()
print("Pick up from where you left last time or start from the beginning")
print()
print("Where to:")
goto = input()
if goto == "":
    goto = "0"
print()
start_elsewhere = False 
if goto != "0":
    start_elsewhere = True 

#########################
# ENIGMA SENT TO POLAND
#########################
enigma_sent_to_poland = [
    """- - - . . . - - - ENIGMA SENT TO POLAND - - - . . . - - -\rJanuary 1929\r
An alert customs worker in Warsaw noticed a strange box had arrived all the way from Germany.\r
Strangely enough...  A German Embassy official was requesting that it should be returned to Germany immediately.\r
The package had been sent to Poland by accident.\r
Suspicions arose among the Polish.\r
Two engineers from the Polish General Staff's Cipher Bureau were summoned and the box was examined.\r""",
    
    {"question": """Should they:\r(A) Open the box    (B) Send it back to Germany""",
    "right": "A",
    "right_path": """And sitting neatly in the box, was a shiny commercial Enigma cipher machine. \r
The box was soon packed up and sent off to Germany. \r
The Germans never suspected the box to be tampered with, much less inspire the next generation of its own decipherment.\r""",
    "wrong": "B",
    "wrong_path": """Perhaps you should have opened the box.\r
It could have inspired a whole generation of code breaking.\r
Here's another chance."""}
]

####################################
# HANS THILO SCHMIDT LEAKS DOCUMENTS
####################################
hans_thilo_schmidt_leaks_documents = [
    """- - - . . . - - - HANS THILO SCHMIDT LEAKS DOCUMENTS - - - . . . - - -\rNovember 1931\r
Rodolphe Lemione, a triple agent from France's Military Intelligence Agency is sat in front of a German man named Hans Thilo Schmidt.\r
He claimed to have important documents about the Enigma machine.\r
A device used to encrypt messages in the German navy, air force and army.\r
Rodolphe wanted those documents.\r""",

    {
        "question": """What should Rodolphe say?\r
(A) I hear you have important documents I want, Mr. Schmidt. Tell me about that. 
(B) Tell me Mr. Schmidt, what brings you all the way out here? Knowing what you know""",
        "right": "B",
        "right_path": """ Hans Thilo Schmidt: Yes I have come a long way. Much at the expense of my own.\r
    Of course you'd know all about it, what Germany has become.\r
    The economic depression hasn't given anyone a good time... especially me.\r
    I have a big family.\r
A lightbulb moment hit Rodolphe.\r""",
        "wrong": "A",
        "wrong_path": """Hans Thilo Schmidt's body stiffened. He looked uncomfortable.\r
Hans Thilo Schmidt: If you're going to speak like that to me, there's no point in carrying on with this conversation.\r
Should you have taken a different approach?"""
    },

    {
        "question": "(A) I think I know how to help you, Mr. Schmidt.\r(B) What matters most is that you have important documents I want",
        "right": "A",
        "right_path": "Hans Thilo Schmidt: Really? How so?",
        "wrong": "B",
        "wrong_path": "Hans Thilo Schmidt: I don't think this deal will go on any further.\rShould you have taken a different approach?"
    },

    {
        "question": """(A) I can offer you the amount you need, to help your family. for the exchange of the documents you have on the Enigma.\r
(B) You must betray your country for us""",
        "right": "A",
        "right_path": "Hans Thilo Schmidt: I agree.",
        "wrong": "B",
        "wrong_path":"Hans Thilo Schmidt: Excuse me?\rShould you have taken a different approach?"
    },

    """Rodolphe Lemione walked away with the documents tucked under under his jacket.\r
The documents were taken straight to the cryptographers in Paris.\r
And it found itself on the desk belonging to Marian Rejewski."""
    
]

########################################
# MARIAN REJEWSKI BREAKS THE ENIGMA CODE
######################################## 

rejewski_breaks_enigma_pre = [
    """- - - . . . - - - REJEWSKI WORKS ON THE ENIGMA - - - . . . - - -\rDecember 1932\rMarian Rejewski, a newly recruited mathematician in the Polish Cipher Bureau had been selected to work on decrypting the Enigma in secret.\r
Marian knew that if he were to break the code, he would need to construct a replica Enigma machine first.\r
Using the documents leaked form Hans Thilo Schmidt, which were Enigma manuals, Marian could piece together the machine."""
]
rejewski_breaks_enigma_post = [
    """- - - . . . - - - REJEWSKI BREAKS THE ENIGMA - - - . . . - - -\rRejewski worked out a formula to solve the enigma by figuring out the wiring inside each rotor.\r
The only mistake he made was assuming that the entry disk was an extra scrambling unit."""
]

###################
# EXPLAINING ENIGMA
###################
explaining_enigma = [
    """- - - . . . - - - WHAT IS THE ENIGMA - - - . . . - - -\rThe  Enigma machine was a device used to encrypt communication by Nazi Germany.\r
It was a simple box that looked like very much like a typewriter when opened up.\r
It was anything but.\r
On the surface, the Enigma comprised of the rotors, lampboard, keyboard and plugboard.""",

    {"textfile": "enigma_box_representation.txt"},

    """Clicking on one letter on the keyboard lights up a letter on the Lampboard.\r
Clicking the same letter twice lights up two different letters on the Lampboard.\r
This can be explained by the internal structure of the Enigma.\r
The Enigma operates by scrambling the path of an electric current during input, so that the output is a different letter.\r
There is a new path for each input.\r
The plugboard itself is a scrambler.\r
It maps each letter (when inputted on the keyboard) to a different letter.
""",

    {"textfile": "plugboard.txt"},

    """The electric current then goes through the entry disk. No scrambling happens here.\r
What comes after the entry disk are the rotors.\r
The rotors are where the real scrambling happens.\r
Each rotor has a scrambling property inside. It maps each letter to a different letter.\r
""",
    
    {"textfile": "entry_disk_and_rotors.txt"},

    """Running through all the possibilities would take far too long to decode.\r
However, there is an extra component to the scramblers.\r
A reflector was added to the end of the scramblers.\r
The job of the reflector is to redirect the electric current back into the scramblers and light a letter up on the lightboard. """,

    {"textfile": "reflector.txt"},

    {
        "question": "What letter lights up on the lightboard?\r(A) J   (B) K",
        "right": "B",
        "right_path": "Correct, K is the output.",
        "wrong": "A",
        "wrong_path": "Wrong, try again."
    },

    """Every keyboard press rotates left wheel one letter forward.\r
When the right wheel has a full rotation, the middle wheel rotates one letter forward.\r
""",

    {"textfile": "entry_disk_and_rotors_first_rotation.txt"},

    {"textfile": "scrambler_first_rotation.txt"},

    {
    "question": "What letter will be output?\r(A) H      (B) J",
    "right": "B",
    "right_path": "Correct, J is the output",
    "wrong": "A",
    "wrong_path": "Wrong, try again."
    },

    {"textfile": "scrambler_first_rotation_answer.txt"},

    """Clicking F twice gives two different outputs""",

    """Passing the electric current through three of these scramblers creates 26 * 26 * 26 scrambler possibilities.\r
Different rotor versions had different wiring inside.\r
In order to decrypt Enigma messages, the correct wiring for each rotor must be known.\r
And more, the correct position of each rotor must be known.""",

    {
    "question": "How many arrangements would 3 rotors give?",
    "right": "6",
    "right_path": "Correct, 3 * 2 * 1 gives 6 different arrangements",
    "wrong": "any_other_number",
    "wrong_path": "Wrong. Hint: (3!)"
    },

    {"textfile": "rotor_arrangements.txt"},

    """Captures of German U-boats allowed the Polish to get their hands on German codesheets.\r
These codesheets listed the settings a message needed to be deciphered.\r
The codesheets were released for each month, detailing the setting used for each day.\r
""",

    {"textfile": "german_code_sheets.txt"},

]

################################
# DOUBLE ENCIPHERED FINGERPRINTS
################################
double_enciphered_fingerprints = [
    """- - - . . . - - - DOUBLE ENCIPHERED FINGERPRINTS - - - . . . - - -\rThe German code experts had decided that the message setting should be enciphered twice.""",
    {
        "question": "Was this a bad move?\r(A) Yes      (B) No",
        "right": "A",
        "right_path": "Yes, in codebreaking, you should avoid repeating anything twice unless you need to.\rRepetition is the enemy of security.",
        "wrong": "B",
        "wrong_path": "Wrong. Try again."
    },
    """When sending messages, the sender would decide what message setting to use.\r
For example, RCM.\r
The sender would turn their rotor settings to the settings specified for that day.\r
For example, ABC""",
    {"textfile": "abc_rotor_setting.txt"},
    """They would then type RCM twice, outputting --> WQR CLT\r
These letters were called the indicator, indicating to the receiver what the message setting is.\r
The sender then turns their rotor setting to RCM and sends the message off to the receiver using morse code.""",
    {"textfile": "rcm_rotor_setting.txt"},
    """The receiver then sets their Enigma machine to the current days settings.\r
They then type the indicator code, WQR CLT, into their Enigma machine.""",
    {
        "question": "What will the output be?",
        "right": "RCM RCM",
        "right_path": "Correct, the receiver now uses this rotor setting to decrypt messages.",
        "wrong": "anything else",
        "wrong_path": "Wrong. Hint: Decrypting a message using the same settings will give the original message. R _ _   R _ M"
    },

    """Rejewski and his team exploited this weakness, looking for patterns to crack the Enigma.\r
Rejewski received a batch of encrypted messages each day.""",
    {"textfile": "double_encryption.txt"},
    """All these messages were encrypted with the same day setting, however different indicator codes\r
The first and fourth column are encrypted with the same key, same with the second and fourth and third and sixth.\r
Remember, the sender had to type the indicator code twice.\r
Knowing this, Rejewski could map relations between the words in the form of a table.\r
""",
    {"textfile": "rejewski_table.txt"},
    """Rejewski began looking for patterns in this relation and eventually formed chains.\r
Using the table, A maps to F, F maps to W, W maps back to A.\r
A -> F -> W -> A        3 links.\r
B -> Q -> Z -> K -> V -> E -> L -> R -> I -> B      9 links.\r
Rejewski would do this for each letter.\r
Eventually realising that the characteristics of the chains were a result of the day key.\r
Although the plugboard is an extra scrambling unit, the only thing that is wholly reliant on the rotor settings are the number of number of links in the chain.\r
The chains were call fingerprints.\r
Changing the day key or even the plug board settings will result in the same chains with the same rotor settings.\r
Rejewski asked himself, which of the 105,546 (6 * 26^3) possible settings as associated with a the number of links in a particular set of chains?\r
Rejewski and his team spent the following year using a replication of the Enigma to catalogue the chain lengths of each of the 105,456 arrangements.\r
They would build the chains and number of links for each corresponding letter, using his catalogue to find the particular chain and link number.\r
This lead him directly to finding the day key (the rotor settings).\r
Now that he had the rotor settings. He needed to find the plugboard settings.\r
Rejewski would remove all the plugs and decipher a message using the day key.\r
Sometimes a known phrase will be deciphered. Meaning the plugs for those letters were unattached.\r
The rest of the letters could be deduced by guessing the letters that weren't decrypted in the phrase.\r
Since there were 6 arrangements of the rotors, Rejewski's team built machines called the Bombes to run this process in parallel.\r
By 1938, the skills of the Polish Cipher Bureau reached its peak.\r
Germany released two extra rotors.\r
Repeating Rejewski's method for all possibilities with the new rotors will require too much power and resources.\r
In 1939, Germany invaded Poland.\r
Poland offered Britain and France each an Enigma machine and blueprints.\r
However, without knowing the wiring of the two rotors, the code could not be broken.\r
""",
]
#########
#U-33
#########
u_33 = [
    "- - - . . . - - - U-33 - - - . . . - - -\rFebruary 1940",
    """The British war ship, Gleaner, was on its nightly patrol.\r
Suddenly, something white and tubular had disappeared into the water.\r""",
    {
        "question": "(A) Investigate the object     (B) Ignore it, it was probably a trick of the eyes\r",
        "right": "A",
        "right_path": """Upon closer inspection, that white object was a periscope.\r
The most dangerous thing a periscope could be connected to was a German Submarine. A U-boat.\rThis was the U-33.""",
        "wrong": "B",
        "wrong_path": "The ship is rocked, it had been hit by a detonation.\rTry again."
    },
    {"textfile": "ascii_submarine.txt"},
    {
        "question": "Should the Gleamer:\r(A) Drop depth charges (detonation) on the U-boat      (B) Sail away\r",
        "right": "A",
        "right_path": "The explosion of the depth charges jarred the U-boat",
        "wrong": "B",
        "wrong_path": "Perhaps not. Maybe there could be something important to be recovered from the U-boat."
    },
    """The U-boat sank to the sea bed. Stuck.\r
The captain of the U-boat believed the only way to bring the boat back up to the surface was to blow the air out of the tanks""",
    {
        "question": "Should they blow the tanks up?\r(A) No     (B) Yes",
        "right": "B",
        "right_path": "The tanks were blown and the U-boat began to ascend towards the surface.",
        "wrong_path": "The boat stayed on the sea bed. The men were trapped. Try again."
    },
    """The order was to abandon ship.\r
German protocol was to detonate the ship and dispose of any traces of Enigma.\r
""",
    {
        "question": "How should the crewmen have disposed of the Enigma components?\r (A) Take it out and drop them into the ocean      (B) Leave it in the boat to be detonated",
        "right": "A", 
        "right_path": "Correct. The crewmen put the wheels into their pockets to drop them into the ocean, where it would sink.",
        "wrong_path": "Wrong. Often, the U-boats did not sink properly. This would put all the German documents and codebooks at risk.",
    },
    """All the crew members did as said. Except for Friedrich Kumpf.\r
After he was rescued, Kumpf turned to his officer.\r
    "Herr Oberleutnant, I forgot to throw the wheels away."
His officer found the pockets of his clothes empty.\r
The British had taken the wheels.""",
]


################
# BLETCHLEY PARK
################
bletchly_park = [
    "- - - . . . - - - BLETCHLEY PARK - - - . . . - - -\rApril 1940",
    """Cryptographers at Bletchly park, central of code breaking in Britain, had familiarised themselves with Rejewski's work.\r
Particularly Alan Turing, a brillian mathematician recruited to break the Enigma.\r
The capture of U-33 provided the missing wiring needed to crack the Enigma.\r
Turing focused on cribs.\r
Cribs is a piece of plaintext that can be associated with a piece of ciphertext.\r""",
    {"textfile": "crib_example.txt"},
    """Exploiting the fact that the Enigma never encoded itself as a letter.\r
Turing would move the plaintext across the ciphertext to determine valid cribs.\r""",
    {"textfile": "valid_cribs.txt"},
    {
        "question": """Which of the above crib is a valid crib?\r(A) 4 & 5      (B) 4 & 6""",
        "right": "B",
        "right_path": "Correct, those cribs have no overlapping cipher and plaintext",
        "wrong_path": "Wrong. Try again"
    },
    {"textfile": "valid_cribs_answer.txt"},
    """The Germans would send out a weather report daily at 6am with an almost guarantee that the word 'wetter' would be in the message.\r
Turing could use cribs to determine the message key and then the day key.\r
The Enigma messages couldn't be broken without cribs. But there were no cribs if there were no broken Enigma messages.\r
Thousands of settings still must be checked, Turing's new machine, called the Bombe peformed this task.\r
The British Bombe consisted of a series of Enigma machines wired together and worked by ruling out incorrect settings.\r
It would find the daily wheel and plugboard settings.\r
Unlike the Polish decrypting method, the British Bombe didn't rely on the double encryption method.\r
The only other way to read messages from the Enigma was if the settings were captured from a submarine.\r
The success of breaking the Enigma machine was owed to multiple contributions and sea captures.\r
"""
] 
##################
# CAPTURE OF KREBS
##################
capture_of_krebs = [
    "- - - . . . - - - CAPTURE OF KREBS - - - . . . - - -\rMarch 1941",
    """German Army trawlers, fishing boats that are coverted to military assets, were operating alogn the Norwegian coast.\r
Operation Claymore was on the go.\r""",
    {"textfile": "ascii_boat.txt"},
"""If one German trawler was captured, there was a high chance that Enigma was being used on the ship.\r
A trawler ship called Krebs was sailing away from Svolvaer.\r
The British HMS Somali opened fire as the German ship came near.\r
One of the shots hit the Kreb directly in the wheelhouse, instantly killing the captain and some crew.\r
More shots fired from the Somali and soon smoke billowed from out the engine room of the Krebs.\r
The Somali sent a boarding party to the Krebs, among the boarding party was Lieutenant Sir Marshall Warmington.\r
Once on the boat, the crew found the remaing Krebs crew waving a white flag.\r""",
    {
        "question": "What should Warmington do?\r(A) Take the remaing Germans as a prisoner of war\r(B) March into the captain's cabin to find important information.",
        "right": "B",
        "right_path": "Inside the captains cabin, Warmington found a piles of paper and a locked drawer.",
        "wrong_path": "Why not take a look around and see what could be found? Try again."
    },
    {
        "question": "Should Warmington open the locked draw?\r(A) Yes       (B) No",
        "right": "A",
        "right_path": "Warmington aimed his pistol towards the locked and pulled the trigger.",
        "wrong_path": "The draw must be locked for a reason. To hide something important. Try again"
    },
    """"As he pushed the draw open, he found two discs, realsing it was used for a cipher machine.\r
Operation claymore provided the codebreakers with more wheels and documents that they desperately needed.\r
The documents contained the German code sheets that would be used to decrypt Enigma messages.\r
However, they were for the month of February.\r
Turing was able to use February's decrypted messages to form his algorithm for faster code breaking.\r"""
]

#####################
# OPERATION PRIMROSE
#####################
operation_primrose = [
    "- - - . . . - - - OPERATION PRIMROSE - - - . . . - - -\rMay 1941",
    """The day before the documents from Operation Claymore reached the codebreakers at Bletchly Park, another convoy was being stalked by a U-boat.\r
This was the U-110.\r
The British HMS ship, Broadway, dropped two depth charges, forcing the crew to abandon ship and jump into the sea.\r
The boat was supposed to sink in a matter of minutes but it failed to sink.\r
The captain of the submarine, Fritz-Julius Lemp decided swim back to sink the ship and discard all the secret material on the it.\r
That was the last time Lemp was seen.\r
9 men from the Broadway quickly rowed to the abandoned ship.\r
A human chain was formed in the ship to pass all documents and equipment out of the ship.\r
One of them spotted a machine resembling a typewriter screwed to a the table in the radio room.
""",
    {
        "question": "Should they take the device?\r(A) Yes\r(B) No, The men are on a sinking submarine, the device is heavy and will take too long to remove",
        "right": "A",
        "right_path": "Yes, the device was an Enigma.",
        "wrong_path": "Does the device ring a bell? Perhaps its worth the risk."
    },
    """The men took out their screwdrivers and took the Enigma with them.\r
The papers collected by the men were German code sheets for June.\r
The codebreakers in Bletchly were able to read current Enigma messages for the first time.\r"""

]
###################
# END
###################
end= [
    """During August-December 1940, The amount of convoys seen and reported by U-boats before the Enigma was broken was 36%.\r
During January-May 1941, that number dropped down to 23%.\r
After the Enigma was broken during September-December 1941, that figure fell down to 4%.\r
Cracking the Enigma allowed the British to shorten the war by two years, having the upper hand in strategy as they could peek into German Intelligence.
A number of contributions and raids from numerous people and countries allowed the Enigma to be broken.
Thank you for playing the Enigma.""",
    {"textfile": "ascii_submarine2.txt"}
]

# for elem in explaining_enigma:
#     if isinstance(elem, dict):
#         if "textfile" in elem:
#             print_textfile(elem)
#         else:
#             multi_choice(elem)
#     else:
#         split(elem)


complete_storyline = [enigma_sent_to_poland, 
                    hans_thilo_schmidt_leaks_documents, 
                    rejewski_breaks_enigma_pre, 
                    explaining_enigma,
                    rejewski_breaks_enigma_post,
                    double_enciphered_fingerprints,
                    u_33,
                    bletchly_park, 
                    capture_of_krebs,
                    operation_primrose,
                    end]

def play_a_script(script):
    for elem in script:
        if isinstance(elem, dict):
            if "textfile" in elem:
                print_textfile(elem)
            else:
                multi_choice(elem)
        else:
            split(elem)

if start_elsewhere:
    truncated_storyline = complete_storyline[int(goto)-1:]
    for storyline in truncated_storyline:
        play_a_script(storyline)

for storyline in complete_storyline:
    play_a_script(storyline)
    # for elem in storyline:
    #     if isinstance(elem, dict):
    #         if "textfile" in elem:
    #             print_textfile(elem)
    #         else:
    #             multi_choice(elem)
    #     else:
    #         split(elem)

"""
{
    "question": ,
    "right": ,
    "right_path": ,
    "wrong": ,
    "wrong_path":
}
"""
