# by MinCiencia, based in https://realpython.com/twitter-bot-python-tweepy/#the-reply-to-mentions-bot

import tweepy
import logging
from config_bot import create_api
import time
import pandas as pd
import numpy as np
import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            df = pd.read_csv('./output/producto19/CasosActivosPorComuna.csv')
            dfT = pd.read_csv('./output/producto19/CasosActivosPorComuna_T.csv')
            n = df.index[df['Comuna'] == keyword]
            casos_ultimo_informe = dfT.iloc[dfT.index.max()][n + 1]
            casos_informe_anterior = dfT.iloc[dfT.index.max()-1][n + 1]
            variacion = casos_ultimo_informe - casos_informe_anterior
            fecha = dfT.iloc[dfT.index.max()][0]
            if variacion > 0:
                api.update_status(
                    status="🤖En "+keyword+" los casos activos son "+casos_ultimo_informe+" de acuerdo al último informe epidemiológico del @ministeriosalud del "+fecha+", "+variacion+" casos activos más que en el informe anterior",
                    in_reply_to_status_id=tweet.id,
                )
            else:
                api.update_status(
                    status="🤖En "+keyword+" los casos activos son "+casos_ultimo_informe+" de acuerdo al último informe epidemiológico del @ministeriosalud del "+fecha+", "+variacion+" casos activos menos que en el informe anterior",
                    in_reply_to_status_id=tweet.id,
                )
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    df = pd.read_csv('./output/producto19/CasosActivosPorComuna.csv')
    df.dropna(subset=['Codigo comuna'], inplace=True)
    keywords = df.Comuna.unique()
    keywords = keywords.tolist()
    while True:
        since_id = check_mentions(api, keywords, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()