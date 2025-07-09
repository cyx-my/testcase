import difflib

def calculate_similarity(state1, state2):
    """
    使用 difflib 计算两个状态的相似度
    """
    # 将状态字符串分割为标签列表
    tags1 = state1.split()
    tags2 = state2.split()
    
    # 计算相似度
    similarity = difflib.SequenceMatcher(None, tags1, tags2).ratio()
    return similarity

def select_most_similar_state(given_state, statelist):
    """
    从状态列表中选择与给定状态最相似的状态
    """
    max_similarity = 0
    most_similar_state = None
    
    for state in statelist:
        similarity = calculate_similarity(given_state, state)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_state = state
    
    return most_similar_state, max_similarity


template_lines = [
    "<s*****a /><Gothic Long Lace Lace-up Half Finger Gloves /><Jun-18/2023 /><Color:BLACK /><Gave 4/5 because I just haven’t used them yet they for a music festival I have coming up. TBEY look just like the pics and I will b testing them out next month lol /><View All Reviews /><You May Also Like /><3,96€ /><5,09€ /><No More Data /><4 /><ls** bought this item 26 minutes ago /><Add 3.79€ of items to enjoy free shipping. /><More /><ADD TO BAG />",
    "<m*****r /><Steampunk Victorian Goggles /><Jul-20/2023 /><Color:BROWN /><Gave 5/5 because these goggles are perfect for my cosplay event. They fit well and look exactly like the pictures. Highly recommended! /><View All Reviews /><You May Also Like /><4,50€ /><6,19€ /><No More Data /><3 /><rs** bought this item 45 minutes ago /><Add 4.29€ of items to enjoy free shipping. /><More /><ADD TO BAG />",
    "<l*****y /><Retro Aviator Sunglasses /><Aug-05/2023 /><Color:BLACK /><Gave 3/5 because the sunglasses are okay, but the frames are a bit too big for my face. The color is accurate though. /><View All Reviews /><You May Also Like /><2,99€ /><3,99€ /><No More Data /><2 /><jk** bought this item 1 hour ago /><Add 5.00€ of items to enjoy free shipping. /><More /><ADD TO BAG />",
    "<a*****n /><Bohemian Maxi Dress /><Sep-12/2023 /><Color:RED /><Gave 5/5 because the dress is beautiful and fits perfectly. I got so many compliments at the party! /><View All Reviews /><You May Also Like /><19,99€ /><24,99€ /><No More Data /><5 /><mn** bought this item 30 minutes ago /><Add 2.00€ of items to enjoy free shipping. /><More /><ADD TO BAG />",
    "<p*****t /><Vintage Fedora Hat /><Oct-25/2023 /><Color:GRAY /><Gave 4/5 because the hat is stylish and well-made. It arrived a bit later than expected, but it was worth the wait. /><View All Reviews /><You May Also Like /><7,99€ /><9,99€ /><No More Data /><1 /><gh** bought this item 15 minutes ago /><Add 6.00€ of items to enjoy free shipping. /><More /><ADD TO BAG />"
]

# 给定状态
given_state = "<these are absolutely perfect for an outfit I already have from here, they fit well, and aren't itchy like some I've had in the past. Takes a little bit to put on, but are worth it. they are beautiful! /><s*****a /><Gothic Long Lace Lace-upHalf Finger gloves /><Jun-18/2023 /><Color: BLACK /><Gave 4/5 because I just haven’t used them yet they for a music festival I have coming up. TBEY look just like the pics and I will btesting them out next month lol /><View All Reviews /><You May Also Like /><3,96€ /><5,09EU /><No More Data /><3 /><tp** currently viewing this item /><Add 3.79EU of items to enjoy free shipping. /><More /><ADD TO BAG />"

# 选择最相似的状态
most_similar_state, similarity = select_most_similar_state(given_state, template_lines)

print("Most similar state:")
print(most_similar_state)
print(f"Similarity: {similarity:.2f}")