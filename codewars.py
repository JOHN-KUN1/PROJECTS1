def like_or_dislike(lst):
    if len(lst) >=1 or lst[len(lst)-1] != lst[len(lst)-2]:
        return lst[len(lst)-1]
    else:
        return 'Nothing'


print(like_or_dislike(['dislike','dislike']))
