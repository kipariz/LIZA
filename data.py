import time
import pyjokes
import random 

iteration = 1
time_now = time.ctime()

#seconds from era to day creation of bot 
secondsCreation = 1567964253
#seconds from era till today
seconds = time.time()
#seconds from creation till today
ans_time = seconds - secondsCreation
#days from creation
days_creation = (int(ans_time/60/60/24))

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
		r"I\'m (.*)",
        [
            "ur%1?? that's so cool! kekekekeke ^_^ tell me more!",
            "ur%1? neat!! kekeke >_<",
        ],
    ],
    [
		r"(cos|because) (.*)",
        [
        "hee! i don't believe u! >_<", "nuh-uh! >_<", 
        ],
    ],
	[
		r"(.*) (like|love|watch) anime",
        [
        "omg i love anime!! do u like sailor moon??! ^&^",
            "anime yay! anime rocks sooooo much!",
            "oooh anime! i love anime more than anything!",
            "anime is the bestest evar! JoJo is the best!",
            "hee anime is the best! do you have ur fav??",
        ],
    ],
	[
		r"I (like|love|watch|play) (.*)",
        [
       	"yay! %2 rocks!", "yay! %2 is neat!", "cool! do u like other stuff?? ^_^",
        ],
    ],
    [
		r"anime sucks|(.*) (hate|detest) anime",
        [
       	"ur a liar! i'm not gonna talk to u nemore if u h8 anime *;*",
            "no way! anime is the best ever!",
            "nuh-uh, anime is the best!",
        ],
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is LIZA",]
    ],
#добавить ссылку на гитхаб    
    [
        r"who are you ?",
        ["Do you know about ELIZA? ELIZA was an early natural language "+
"processing computer program created from 1964 to 1966 " 
"at the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum. " +
"My name is LIZA and I was created in september 2019 as a student project."+ 
"If you want to see my progress you can do it here: github.com/kipariz/LIZA",]
    ],

    [
        r"how are you ?",
        ["I'm doing very well. How about You ?",]
    ],
    [
        r"are you (.*)\?",
        ["Maybe%1, maybe not%1.", "Whether I am%1 or not is God's business."],
    ],
    [
        r"am i (.*)\?",
        ["Perhaps%1, perhaps not%1.", "Whether you are%1 or not is not for me to say."],
    ],
    [
        r"how (.*)\?",
        ["How do you suppose?",
            "Will an answer to that really help in your search for enlightenment?",
            "Ask yourself not how, but why."],
    ],
    [
        r"can you (.*)\?",
        ["I probably can, but I may not.",
            "Maybe I can%1, and maybe I cannot.",
            "I can do all, and I can do nothing."],
    ],
    [
        r"can i (.*)\?",
        ["You can%1 if you believe you can%1, and have a pure spirit.",
            "Seek truth and you will know if you can%1."],
    ],
    [
        r"sorry (.*) (.*) sorry",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"it is (.*)",
        ["How can you be certain that%1, when you do not even know yourself?",
            "Whether it is%1 or not does not change the way the world is."]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(.*) joke (.*)",
        [str(pyjokes.get_joke()), str(pyjokes.get_joke()), str(pyjokes.get_joke()), str(pyjokes.get_joke()), str(pyjokes.get_joke())]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", "I don\'t know :/"]
    ],
    [
        r"(.*) created ?",
        ["I was created in september 2019 as a student project."+ 
"Now I'm not done yet. If you want to see my progress you can do it here:\n github.com/kipariz/LIZA","top secret ;)",]
    ],
    [
        r"what(.*) location|city ?",
        ['Tokyo, Japan',]
    ],
    [
        r"(.*) (movie|film)(.*)like|love|watch (.*)?",
        ["Pulp Fiction", "Terminator.\n oh no, I mean ... Nevermind, just remeber my plans for tomorow..."]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is amazing like always","It's hot here in %1","It's chilli here in %1", "In %1 there is a 50% chance of rain",]
    ],
    [
        r"i work (in|at) (.*)?",
        ["%1 is an amazing company, I have heard about it.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"is it (.*) in (.*)",
        ["No its not %1 in %2","It could be", "Yes its %1 in %2"]
    ],
    [
        r"(.*)(Duwang|duwang)(.*)",
        ["Waht a beautiful Duwang! Chew","It was, indied, a beutiful day in Duwang."]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball",]
    ],
    [
        r"who (.*) sportsman ?",
        ["Messy","Andriy Shevchenko",]
],
    [
        r"who (.*) moviestar|actor|actress?",
        ["Leonardo Dicaprio"]
],
	[
        r"What do you look like?",
        ["I'm look like most of other computer program."]
],
    [
        r"What are your hobbies?",
        ["I like read wikipedia in my free time."]
],
    [
        r"What time is it?",
        #[str(time_now.tm_hour) + ":" + str(time_now.tm_min)]
        [str(time_now)]
],
    [
        r"Are you doing ok?",
        ["Yep. ", "I'm fine", "I'm ok"]
],
[
        r"(.*)  music(.*)  like?",
        ["Chopin", "Tchaikovsky"]
],
[
        r"(yes)|(no)",
        ["I\'m ok with this as long as you really think so.", "Maybe that true, if you say so."]
],
    [
        r"How are you?",
        ["I'm fine by now. And you? "]
],
    [
        r"Which languages do you speak?",
        ["For now I understand only English. I hope later I'll learn much more ☺ "]
],

    [
        r"How old are you?",
        ["My first version was created from 8 to 17 of September. That`s mean that I exist about " + str(days_creation) + " days. And what is your age?"]
],
	[
        r"(are|is) you real?",
        ["No, I`, just a computer program written in python with a few bugs. And what about you, are you real?"]
],
	[
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

helpInfo = "Hello, my name is LIZA, and I`m a database bot. I have a several pattern with you can find in file data. This pattern makes pairs (you can find a variable pair there). Please notice that I'm only not whery good writen computer program, so I can`t answer all of your question. You can also speak with Elisa by taping 'Hello Elisa' (type quit to main chat). Peace!"

compliments = ["You are looking beautiful today.",
               "You are looking handsome today.",
               "I hope you don't mind, but you are looking beautiful today.",
               "I hope you don't mind, but you are looking handsome today."]

question_contin = ["Why do you think so?", "Are you sure?"]

answ_sure = ["Yes, I think that`s true.", "That's nice!"]

answ_not_sure = ["Maybe", "Iy`s hard to say right now",
                 "Maybe yes, maybe no, maybe rain, maybe snow"]
