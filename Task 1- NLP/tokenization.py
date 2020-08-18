# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nltk


para="""I am delighted to be here at the Indian Institute of Technology Madras and address the members of this renowned place of learning and other guests present here. My greetings to you all.

Friends, before I begin my address I want to share a thought with all the youth present here. I have met, so far, 11 million youth like you in a decade?s time, in India and abroad. I have seen their hopes, experienced their pains, walked with their aspirations and heard through their despair. All this experience made me learn something about them, which I would like to share with you:

I learnt, every youth wants to be unique, that is, YOU! But the world all around you, is doing its best, day and night, to make you just "everybody else".
Being like everybody else is convenient at the first glance, but not satisfying in the long vision.

The challenge, therefore, my young friends, is that you have to fight the hardest battle, which any human being can ever imagine to fight; and never stop fighting until you arrive at your destined place, that is, a UNIQUE YOU!

Being unique will require excellence, let us understand what is excellence in more detail.
Excellence is a self-imposed self-directed life-long process
Excellence is not by accident. It is a process, where an individual, organization or nation, continuously strives to better oneself. The performance standards are set by themselves, they work on their dreams with focus and are prepared to take calculated risks and do not get deterred by failures as they move towards their dreams. Then they step up their dreams as they tend to reach the original targets. They strive to work to their potential, in the process, they increase their performance thereby multiplying further their potential and this is an unending life cycle phenomenon. They are not in competition with anyone else, but themselves. That is the culture of excellence. Let me share an important experience from the life of the father of the nation.

To learn, reflect and give

Through 79 years of my life, I have been part of pre-independent India, jubilation of independence and the post-independence era. Let me recall, one incident which took place on the eve of Indian Independence. At the stroke of midnight of 14 ? 15 August 1947, the first Prime Minister of India Pt Jawaharlal Nehru was declaring the independence to 300 million Indians from foreign rule. There was rejoicing all around the country. At that time, there was a sudden question from a stray corner, where is the Father of Nation Mahatma Gandhiji? To the surprise of the entire audience, Mahatma Gandhi was in Calcutta wiping the tears of those who were affected due to the social disharmony. Mahatma Gandhiji's diary records his advice to a group of students who came to meet him Calcutta:

"Students ought to think and think well. They should do no wrong?.. Students should do everything to build-up a new state of India which would be everybody's pride".

These actions of the champion of non-violence at the time of independence made me feel proud by being led an inspirational leader.

Friends, while in the company of many young inspired students of IIT Madras, I would like to give my perspective on the topic "Evolution of a Unique YOU". In this context, I will talk to you about four important aspects in life with my experiences ? Aim in life, Acquiring Knowledge, Working Hard towards your dream even in the times of difficulty and then finally, how to manage failures and success in life."""


sen=nltk.sent_tokenize(para)

wo=nltk.word_tokenize(para)
