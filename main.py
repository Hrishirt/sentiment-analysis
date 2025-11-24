from transformers import pipeline

classifier = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
)

print(classifier("حمار"))
