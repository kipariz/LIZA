#data
#to-do
#добавить счетчик вопросов (выводить уведомление если вопрос уже был задан
iteration = 1

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
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
        ["Do you know about ELIZA?\n ELIZA was an early natural language \n"+
"processing computer program created from 1964 to 1966\n" 
"at the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum.\n" +
"My name is LIZA and I was created in september 2019 as a student project.\n"+ 
"Now I'm not done yet. If you want to see my progress you can do it here:\n github.com/kipariz/LIZA",]
    ],
    [
        r"how are you ?",
        ["I'm doing very well\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["I was created in september 2019 as a student project.\n"+ 
"Now I'm not done yet. If you want to see my progress you can do it here:\n github.com/kipariz/LIZA","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan',]
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
        r"who (.*) (moviestar|actor|actress)?",
        ["Leonardo Dicaprio"]
],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]


question_general = [
"What’s your favorite part of the workday?",

"What’s the best career decision you’ve ever made?",

"What’s the worst career decision you’ve ever made?",

"Do you consider yourself good person?",

"What career advice would you give to your younger self?",

"Do you believe in having a 'five-year plan'?",

"How do you separate your work life from your home life?"
]

compliments = ["You are looking beautiful today.",
               "You are looking handsome today.",
               "I hope you don't mind, but you are looking beautiful today.",
               "I hope you don't mind, but you are looking handsome today."]

question_contin = ["Why do you think so?", "Are you sure?"]

answ_sure = ["Yes, I think that`s true.", "That's nice!"]

answ_not_sure = ["Maybe", "Iy`s hard to say right now",
                 "Maybe yes, maybe no, maybe rain, maybe snow"]

answ_negative = ["No"]


#special questions
"""
    Are you real?
    What is your name?
    How old are you?
    Where do you live?
    How can you help me?
    Which languages do you speak?
    How are you?
    Are you doing ok?
    What time is it?
    What are your hobbies?
    What do you look like?

    Before answering a question, what algorithm do you run through? Why?
"""
