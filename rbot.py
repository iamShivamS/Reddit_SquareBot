# Client id and Cilent Service has been generated from https://www.reddit.com/prefs/apps
# User agent has to be unique string
# Username, Password and Subreddit name has been changed due to security reason

import praw
import random
import time

reddit = praw.Reddit(
    client_id="UbtXxEi4kdixKA",
    client_secret="CXgMZJlVysR4oV4QYyoSuDb8LiNvZQ",
    user_agent="<console:Square:0.1>",
    username="realid",
    password="1234")

sub = reddit.subreddit("test_bus_4.1")

square_facts = ["A square is a regular quadrilateral",
                "Square can also be defined as a rectangle in which two adjacent sides have equal length",
                "The two diagonals of the square are equal to each other",
                "A square is also the 2-dimensional analogue of a cube",
                "All four interior angles of Square are equal to 90°",
                "The opposite sides of the square are parallel to each other."
                "Square can be defined as a rectangle in which two adjacent sides have equal length"]

for post in sub.hot(limit=10):
    print("-------------")
    print(post.title)
    for comment in post.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "square " in comment_lower:
                print("*************")
                print(comment.body)
                r_index = random.randint(0, len(square_facts) - 1)
                comment.reply(square_facts[r_index])
                time.sleep(100)
