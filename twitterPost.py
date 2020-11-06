import random 

part1 = ["Robin","Max","Pankaj","Fake News", "Ankit","Rohit"]
part2 = ["no talent,","on the way down,","really poor numbers,","nasty tone,","looking like a fool,","bad hombre,","is out of control,"]
part3 = ["got destroyed by my ratings.","rigged the election.","had a much smaller crowd.","will pay for the wall.","a big Problem."]
part4 = ["So sad","Apologize","So true","Media won't report","Big trouble","Fantastic job","Stay tuned"]


twitterPost = [part1,part2,part3,part4]

combinePost = []

for post in twitterPost:
  randomPost = random.randint(0,len(post)-1)
  combinePost.append(post[randomPost])

print(" ".join(combinePost))