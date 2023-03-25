# Text-Analysis-Project
 
## Part 4: Project Writeup and Reflection

Write a summary of your project and your reflections on it in [`README.md`](README.md), using [Markdown format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). There is no need to use fancy words or ChatGPT. The [`README.md`](README.md) file should consist of the following sections:

**1. Project Overview** (~1 paragraph)

What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?

    I used Gutenberg to access my first book and I downloaded other two books and convereted them into txt file to get access to it. I used three books written by Agatha Christie. The first book was written in the start of her career the other in the middle and book 3 at the last. I did some basic text analysis, summarize the text to look at the frequency of all three books. I also analyzed the sentiment of the different books. Apart from sentiment analysis. I looked at the similarity and the clustering for the rest of the texts. 

**2. Implementation** (~1-2 paragraphs + screenshots)

Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use screenshots to describe how you used ChatGPT to help you or learn new things.

    I mostly followed the instructions to complete the project. But one of the decision that I made on the architecture level was deciding if I wanted to analyze a single book first using verious metrics or if I should run the single analysis on all the books one at a time. I chose to do so because it allowed me to clearly compare the data between the various texts in a single output. 

    I needed decoding for my text files so I used Chatgpt to help me understand how that worked. 
    image.png

    TF-IDF was a new concept to I used Chatgpt to help me understand that in an easy language. 

**3. Results** (~2-3 paragraphs + figures/examples)

Present what you accomplished in your project:

    Text analysis of the three books gave some basic insights, but there wasn't anything particularly interesting about the frequency of the words. They were mostly neutral, and the positive sentiments were higher than the negative sentiments, which was very intresting because most of the books are based around crime and more negative elements, so I was expecting it to give a negative sentiment report. Apart from that, I also looked at the similarity between those three books. The rangewas from 72-79, which was understandable given the books were from the same author and was the same genre. I also did stext clustering and looked the unique words in all three books. 
    I remember reading about Agatha Christie that as she grew old her mental health worsened and that was reflected in her work. So I ran an analysis to see the the major difference between the books from different time in her career however I there we not a lot of differences in the sentiment and the similarity of the book. However the number of unique words in those books were progressively decreasing: 
    Number of unique words in Book1:  13612
    Number of unique words in Book2:  12443
    Number of unique words in Book3:  8467
    Around the end of her career her book had 5 thousand less unique words which was very intresting. It was speculated that she suffered from dissociative amnesia. Which might have reflected in her work as well. 


- If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
- If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

**4. Reflection** (~1-2 paragraphs)

From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

    I think my interest in the topic and what I wanted to do really helped me planed the project ahead of time. I liked how the project gave a lot of independence, allowing us to pick what we could work on. I still dealt with a lot of libraries and concepts that were very new so I had to install them and use intenet and chatgpt to come up with answers. 

    Chatgpt was really helpful in explaining new commands and libraries, also finding out how to download them. A lot of time the code seemed correct but was not giving the correct output, chatgpt really helped to debug my code. I also used it to help me understand the code given in the instructions to better understand them while putting it in the program. 
    