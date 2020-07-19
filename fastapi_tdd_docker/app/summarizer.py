import asyncio

import nltk
from newspaper import Article

from fastapi_tdd_docker.app.models.tortoise import TextSummary


async def generate_summary(summary_id: int, url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    summary = article.summary

    await TextSummary.filter(id=summary_id).update(summary=summary)
