import praw
import random

random_answer = ['Monkey Tennis\n\n^im ^a ^bot', 'Alan Attack! Like the Cook Report, but with a more slapstick approach.\n\n^im ^a ^bot', 'Shoestring, Taggart, Spender, Bergerac, Morse. What does that say to you about regional detective series?\n\n^im ^a ^bot', 'God is a gas… but not a small gas like Calor Gas\n\n^im ^a ^bot', 'In my mind God made Adam and Eve, he didn’t make Adam and Steve.\n\n^im ^a ^bot', 'Actually the best thing I did, was to get thrown out by my wife. She’s living with a fitness instructor. He drinks that yellow stuff in tins. He’s an idiot.\n\n^im ^a ^bot', 'You make pigs smoke!\n\n^im ^a ^bot', 'Bucktoothed simpletons with eyebrows on their cheeks\n\n^im ^a ^bot', 'I don’t like big feet. It reminds me of gammon.\n\n^im ^a ^bot', 'I find it amazing how many people still think the petrol cap on a Ford Focus is offside rear.\n\n^im ^a ^bot', 'Quick tip for yourself: if you’re ever doing an after-dinner speech, you say "My Lords, Ladies and Gentlemen, sorry Im late, I just popped to the toilet. And while I was there, I saw some graffiti and it said I used to be indecisive, but now Im not so sure. Straight away you’ve got them by the jaffas.\n\n^im ^a ^bot', 'Earlier on I put in a pound of mashed up Dundee cake, let’s take a look… not a trace!\n\n^im ^a ^bot', 'Which, again, to me is a bonus.\n\n^im ^a ^bot', 'Do you know what this bathroom says to me? Aqua\n\n^im ^a ^bot', 'I’m sorry Mr Hawk, your pardon has been turned down. You have been found guilty of… premeditated homicide of a mouse\n\n^im ^a ^bot', 'The temperature inside this apple turnover is over 1,000 degrees. If I squeeze it, a jet of molten bramley apple will squirt out. Could go your way; could go mine. Either way, one of us is going down.\n\n^im ^a ^bot', 'smell my cheese you mother\n\n^im ^a ^bot', 'No offence, Lynn, but your life is technically not worth insuring.\n\n^im ^a ^bot', 'You ought to have a basic grasp of Latin if you’re working in Curry’s\n\n^im ^a ^bot','Kiss my Face\n\n^im ^a ^bot', 'He nearly Soiled himself\n\n^im ^a ^bot', 'Dan Dan Dan\n\n^im ^a ^bot', 'Does that mean there will be noise or wont be noise?\n\n^im ^a ^bot']
QUESTIONS = ["!randompartridge"]
partridge_item = random.choice(random_answer)

def main():
    reddit = praw.Reddit(
        user_agent="",
        client_id="",
        client_secret="",
        username="",
        password="",
    )

    subreddit = reddit.subreddit("AlanPartridge")
    for comment in subreddit.stream.comments(skip_existing=True):
            process_comment(comment)



def process_comment(comment):
    for question_phrase in QUESTIONS:
        if question_phrase in comment.body.lower():
         comment.reply (random.choice(random_answer))

        break


if __name__ == "__main__":
    main()
