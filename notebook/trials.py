from transformers import pipeline 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
pipe = pipeline("summarization",model="Ripesh08/news_summarization")
#load model 
tokenizer  =AutoTokenizer.from_pretrained("Ripesh08/news_summarization")
model =AutoModelForSeq2SeqLM.from_pretrained("Ripesh08/news_summarization")
text = '''The Demon Slayer: Kimetsu no Yaiba franchise continues its reign of success with the recent World Tour preview screenings of 'To the Hashira Training' captivating audiences worldwide. Opening to overwhelming enthusiasm and packed theatres, the event proved to be a significant milestone in the franchise's journey.
The tour kicked off in Tokyo on February 2-3, setting the stage for a spectacular journey across continents. From New York to Seoul, Berlin to São Paulo, fans eagerly gathered to witness the latest instalment of the beloved anime series. The palpable excitement and sold-out screenings underscored the global appeal of Demon Slayer: Kimetsu no Yaiba.
Record-Breaking Success in Japan
Upon its debut in Tokyo, 'To the Hashira Training' soared to the top of the Japanese box office charts, solidifying its position as a cultural phenomenon. With over 1.03 million tickets sold and approximately 1.4 billion yen in revenue, the film's success surpassed expectations, further cementing Demon Slayer's status as an anime powerhouse.
Anticipation Builds for North American Premiere
Following the World Tour's triumphant conclusion, all eyes are now on North America as fans eagerly await the theatrical premiere of 'To the Hashira Training.' Set to screen in IMAX and premium large formats, the North American release promises to deliver an immersive viewing experience for audiences across the continent.
Demon Slayer: Kimetsu no Yaiba's journey from manga to screen has been nothing short of extraordinary. With each adaptation garnering widespread acclaim and a dedicated fanbase, the franchise continues to captivate audiences worldwide. From its humble beginnings in print to its stunning visual spectacle on the silver screen, Demon Slayer's evolution is a testament to the power of storytelling.
As fans eagerly await the premiere of the Hashira Training Arc anime in spring, anticipation for what lies ahead continues to mount. With the franchise's unwavering popularity and a dedicated fanbase spanning the globe, the future looks brighter than ever for Demon Slayer: Kimetsu no Yaiba.'''
print(pipe(text)).