#!/usr/bin/env python
# coding: utf-8

# In[25]:


from textblob import TextBlob

# Function to perform sentiment analysis on a given text
def analyze_text_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get the sentiment
    sentiment = blob.sentiment

    # Print the sentiment analysis results
    print("Sentiment Analysis:")
    print(f"Polarity: {sentiment.polarity}")  # Polarity ranges from -1 (negative) to 1 (positive)
    print(f"Subjectivity: {sentiment.subjectivity}")  # Subjectivity ranges from 0 (objective) to 1 (subjective)

# Example usage
article_text = """ ‘Women’s leadership’ has become the new buzzword in workplaces all around the world—from conferences, reports, surveys, and awards to leadership development programmes, everything talks about the need and relevance of women in leadership. As a leader, I am wholly committed to endorsing this agenda of increasing women's participation in the workforce and supporting their journey towards leadership.
However, when leadership is viewed through a gendered lens, the conversations surrounding women leaders' achievements often only emphasise their resilience in fighting against the odds to get to the top. While these stories are inspiring and must certainly be celebrated, this outlook can unintentionally reinforce the notion that women leaders are an exception and that their leadership qualities are characteristically different from those of men. Moreover, they can inadvertently support the stereotype that women must prove themselves in ways men do not. This sets different expectations for women and overlooks the diverse paths men and women take to leadership. Also, when it comes to the choice of words used for leaders, men can be inspiring, emotional, empathetic, resilient, and kind, just as women can be ambitious, authoritative, assertive, practical and decisive. Therefore, we need to reset how we talk about leadership beyond gender labels to focus on the core qualities and effectiveness of leaders, irrespective of gender.
How often do we use the term ‘male leaders’ compared to ‘women leaders’? The answer stems from the historical and stereotypical association of leadership with masculine traits such as authority, assertiveness, decisiveness, and strength, implicitly suggesting that male leadership is the norm while female leadership is a variation. Unknowingly, this distinction perpetuates the idea that leadership is an inherently male domain and that most women do not have what it takes to become a leader or that women must overcome hurdles to be a part of the club.

A lot of this has got to do with the societal roles that have historically burdened women with most of the household responsibilities and family care necessitating that they navigate and struggle to balance these demands alongside their professional aspirations. Men often do not have to deal with this duality, or at least not to the extent of women. While celebrating women who overcome these challenges to take on leadership roles is commendable, we must also normalise crediting the women behind successful male leaders and talking about the need for men to equally participate in household and family responsibilities to support workforce equality. To that end, Kerala showcasing gender-neutral images in school textbooks to promote equality, challenging traditional gender stereotypes by showing men working in the kitchen or some of our cricketers like Virat Kohli crediting his wife Anushka Sharma for the T20 World Cup win are promising signs of progress.
The starting point to shift the narrative is to address the language we use. Terms like women leaders should be used judiciously, ensuring they do not imply that women are exceptions to the rule. A subtle change in communications placing emphasis on the leader's accomplishments rather than their gender can make a huge difference. For example, we have all been in rooms where a successful leader has been introduced by saying, "She is a remarkable or inspiring woman leader." When the introduction could have very well been that "She has led her organisation to achieve remarkable success." This is the only way to normalize the presence of women in leadership roles and reduce the implicit predisposition that they are different from their male counterparts.
It is absolutely critical to note that this shift in narrative and communications does not mean we should ignore the enormous gender gap in leadership positions. Given the current underrepresentation of women in leadership roles across various fields, bridging this gap is non-negotiable. Representation matters immensely. Seeing women in top leadership positions can help normalise their presence and create a powerful cascade for other women in workplaces and communities.

The key point is that leadership should be discussed in terms of outcomes and the ability to inspire and manage teams rather than gendered attributes. Leadership styles and qualities can vary between women and men. These often overlap, indicating that successful leadership is not confined to a single gender. A leader’s effectiveness is not determined by their gender but by how well they can contribute to the needs and growth of the organisation and its people.
"""
analyze_text_sentiment(article_text)


# In[31]:


import matplotlib.pyplot as plt
from textblob import TextBlob

# Your LinkedIn post text
post = """ ‘Women’s leadership’ has become the new buzzword in workplaces all around the world—from conferences, reports, surveys, and awards to leadership development programmes, everything talks about the need and relevance of women in leadership. As a leader, I am wholly committed to endorsing this agenda of increasing women's participation in the workforce and supporting their journey towards leadership.
However, when leadership is viewed through a gendered lens, the conversations surrounding women leaders' achievements often only emphasise their resilience in fighting against the odds to get to the top. While these stories are inspiring and must certainly be celebrated, this outlook can unintentionally reinforce the notion that women leaders are an exception and that their leadership qualities are characteristically different from those of men. Moreover, they can inadvertently support the stereotype that women must prove themselves in ways men do not. This sets different expectations for women and overlooks the diverse paths men and women take to leadership. Also, when it comes to the choice of words used for leaders, men can be inspiring, emotional, empathetic, resilient, and kind, just as women can be ambitious, authoritative, assertive, practical and decisive. Therefore, we need to reset how we talk about leadership beyond gender labels to focus on the core qualities and effectiveness of leaders, irrespective of gender.
How often do we use the term ‘male leaders’ compared to ‘women leaders’? The answer stems from the historical and stereotypical association of leadership with masculine traits such as authority, assertiveness, decisiveness, and strength, implicitly suggesting that male leadership is the norm while female leadership is a variation. Unknowingly, this distinction perpetuates the idea that leadership is an inherently male domain and that most women do not have what it takes to become a leader or that women must overcome hurdles to be a part of the club.

A lot of this has got to do with the societal roles that have historically burdened women with most of the household responsibilities and family care necessitating that they navigate and struggle to balance these demands alongside their professional aspirations. Men often do not have to deal with this duality, or at least not to the extent of women. While celebrating women who overcome these challenges to take on leadership roles is commendable, we must also normalise crediting the women behind successful male leaders and talking about the need for men to equally participate in household and family responsibilities to support workforce equality. To that end, Kerala showcasing gender-neutral images in school textbooks to promote equality, challenging traditional gender stereotypes by showing men working in the kitchen or some of our cricketers like Virat Kohli crediting his wife Anushka Sharma for the T20 World Cup win are promising signs of progress.
The starting point to shift the narrative is to address the language we use. Terms like women leaders should be used judiciously, ensuring they do not imply that women are exceptions to the rule. A subtle change in communications placing emphasis on the leader's accomplishments rather than their gender can make a huge difference. For example, we have all been in rooms where a successful leader has been introduced by saying, "She is a remarkable or inspiring woman leader." When the introduction could have very well been that "She has led her organisation to achieve remarkable success." This is the only way to normalize the presence of women in leadership roles and reduce the implicit predisposition that they are different from their male counterparts.
It is absolutely critical to note that this shift in narrative and communications does not mean we should ignore the enormous gender gap in leadership positions. Given the current underrepresentation of women in leadership roles across various fields, bridging this gap is non-negotiable. Representation matters immensely. Seeing women in top leadership positions can help normalise their presence and create a powerful cascade for other women in workplaces and communities.

The key point is that leadership should be discussed in terms of outcomes and the ability to inspire and manage teams rather than gendered attributes. Leadership styles and qualities can vary between women and men. These often overlap, indicating that successful leadership is not confined to a single gender. A leader’s effectiveness is not determined by their gender but by how well they can contribute to the needs and growth of the organisation and its people.
"""

# Perform sentiment analysis
blob = TextBlob(post)
sentences = blob.sentences
sentiments = [sentence.sentiment.polarity for sentence in sentences]

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(sentiments, marker='o', linestyle='-', color='b')
plt.title('Sentiment Analysis of Newspaper Article')
plt.xlabel('Sentence Index')
plt.ylabel('Sentiment Polarity')
plt.grid(True)
plt.show()


# In[27]:


for i, sentence in enumerate(sentences):
    print(f"Sentence {i}: {sentence}")


# In[30]:


article = """ ‘Women’s leadership’ has become the new buzzword in workplaces all around the world—from conferences, reports, surveys, and awards to leadership development programmes, everything talks about the need and relevance of women in leadership. As a leader, I am wholly committed to endorsing this agenda of increasing women's participation in the workforce and supporting their journey towards leadership.
However, when leadership is viewed through a gendered lens, the conversations surrounding women leaders' achievements often only emphasise their resilience in fighting against the odds to get to the top. While these stories are inspiring and must certainly be celebrated, this outlook can unintentionally reinforce the notion that women leaders are an exception and that their leadership qualities are characteristically different from those of men. Moreover, they can inadvertently support the stereotype that women must prove themselves in ways men do not. This sets different expectations for women and overlooks the diverse paths men and women take to leadership. Also, when it comes to the choice of words used for leaders, men can be inspiring, emotional, empathetic, resilient, and kind, just as women can be ambitious, authoritative, assertive, practical and decisive. Therefore, we need to reset how we talk about leadership beyond gender labels to focus on the core qualities and effectiveness of leaders, irrespective of gender.
How often do we use the term ‘male leaders’ compared to ‘women leaders’? The answer stems from the historical and stereotypical association of leadership with masculine traits such as authority, assertiveness, decisiveness, and strength, implicitly suggesting that male leadership is the norm while female leadership is a variation. Unknowingly, this distinction perpetuates the idea that leadership is an inherently male domain and that most women do not have what it takes to become a leader or that women must overcome hurdles to be a part of the club.

A lot of this has got to do with the societal roles that have historically burdened women with most of the household responsibilities and family care necessitating that they navigate and struggle to balance these demands alongside their professional aspirations. Men often do not have to deal with this duality, or at least not to the extent of women. While celebrating women who overcome these challenges to take on leadership roles is commendable, we must also normalise crediting the women behind successful male leaders and talking about the need for men to equally participate in household and family responsibilities to support workforce equality. To that end, Kerala showcasing gender-neutral images in school textbooks to promote equality, challenging traditional gender stereotypes by showing men working in the kitchen or some of our cricketers like Virat Kohli crediting his wife Anushka Sharma for the T20 World Cup win are promising signs of progress.
The starting point to shift the narrative is to address the language we use. Terms like women leaders should be used judiciously, ensuring they do not imply that women are exceptions to the rule. A subtle change in communications placing emphasis on the leader's accomplishments rather than their gender can make a huge difference. For example, we have all been in rooms where a successful leader has been introduced by saying, "She is a remarkable or inspiring woman leader." When the introduction could have very well been that "She has led her organisation to achieve remarkable success." This is the only way to normalize the presence of women in leadership roles and reduce the implicit predisposition that they are different from their male counterparts.
It is absolutely critical to note that this shift in narrative and communications does not mean we should ignore the enormous gender gap in leadership positions. Given the current underrepresentation of women in leadership roles across various fields, bridging this gap is non-negotiable. Representation matters immensely. Seeing women in top leadership positions can help normalise their presence and create a powerful cascade for other women in workplaces and communities.

The key point is that leadership should be discussed in terms of outcomes and the ability to inspire and manage teams rather than gendered attributes. Leadership styles and qualities can vary between women and men. These often overlap, indicating that successful leadership is not confined to a single gender. A leader’s effectiveness is not determined by their gender but by how well they can contribute to the needs and growth of the organisation and its people.
"""

# Count occurrences of the term 'women leader'
count = article.lower().count('women leaders')
print(f"The term 'women leaders' appears {count} times in the article.")


# In[ ]:




