# by MinCiencia, based in https://realpython.com/twitter-bot-python-tweepy/#the-reply-to-mentions-bot

import tweepy
import logging
from config_bot import create_api
import time
import pandas as pd
import os
import numpy as np
import re
import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            comuna = tweet.text.replace('@min_ciencia_IA ', '')
            comuna = comuna.lower()
            if comuna in keywords:
                logger.info(f"Answering to {tweet.user.name}")
                df = pd.read_csv('../output/producto19/CasosActivosPorComuna.csv')
                dfT = pd.read_csv('../output/producto19/CasosActivosPorComuna_T.csv')
                df["Comuna"] = df["Comuna"].str.lower()
                n = df.index[df['Comuna'] == comuna]
                casos_ultimo_informe = int(pd.to_numeric(dfT.iloc[dfT.index.max()][n + 1]))
                casos_informe_anterior = int(pd.to_numeric(dfT.iloc[dfT.index.max() - 1][n + 1]))
                variacion = casos_ultimo_informe - casos_informe_anterior
                fecha = dfT.iloc[dfT.index.max()][0]
                if variacion > 0:
                    reply = "🤖Hola @" + tweet.user.screen_name + ". En " + comuna + " los casos activos de Covid19 son " + str(casos_ultimo_informe) + " según mis registros en base al último informe epidemiológico del @ministeriosalud (" + fecha + "), " + str(variacion) + " más que en el informe anterior."
                    api.update_status(status=reply, in_reply_to_status_id=tweet.id)
                else:
                    reply = "🤖Hola @" + tweet.user.screen_name + ". En " + comuna + " los casos activos de Covid19 son " + str(casos_ultimo_informe) + " según mis registros en base al último informe epidemiológico del @ministeriosalud (" + fecha + "), " + str((-1) * variacion) + " menos que en el informe anterior."
                    api.update_status(status=reply, in_reply_to_status_id=tweet.id)

            else:
                for word in tweet.text.lower().split():
                    if word in keywords:
                        logger.info(f"Answering to {tweet.user.name}")
                        df = pd.read_csv('../output/producto19/CasosActivosPorComuna.csv')
                        dfT = pd.read_csv('../output/producto19/CasosActivosPorComuna_T.csv')
                        df["Comuna"] = df["Comuna"].str.lower()
                        n = df.index[df['Comuna'] == word]
                        casos_ultimo_informe = int(pd.to_numeric(dfT.iloc[dfT.index.max()][n + 1]))
                        casos_informe_anterior = int(pd.to_numeric(dfT.iloc[dfT.index.max()-1][n + 1]))
                        variacion = casos_ultimo_informe - casos_informe_anterior
                        fecha = dfT.iloc[dfT.index.max()][0]
                        if variacion > 0:
                            reply = "🤖Hola @" + tweet.user.screen_name + ". En " + word + " los casos activos de Covid19 son " + str(casos_ultimo_informe) + " según mis registros en base al último informe epidemiológico del @ministeriosalud (" + fecha + "), " + str(variacion) + " más que en el informe anterior."
                            api.update_status(status=reply, in_reply_to_status_id=tweet.id)
                        else:
                            reply = "🤖Hola @" + tweet.user.screen_name + ". En " + word + " los casos activos de Covid19 son " + str(casos_ultimo_informe) + " según mis registros en base al último informe epidemiológico del @ministeriosalud (" + fecha + "), " + str((-1) * variacion) + " menos que en el informe anterior."
                            api.update_status(status=reply, in_reply_to_status_id=tweet.id)
    return new_since_id

def main(a,b,c,d):
    api = create_api(a,b,c,d)
    since_id = 1378712721517084680
    df = pd.read_csv('../output/producto19/CasosActivosPorComuna.csv')
    df.dropna(subset=['Codigo comuna'], inplace=True)
    keywords = df.Comuna.unique()
    a = np.array([x.lower() if isinstance(x, str) else x for x in keywords])
    keywords = a.tolist()
    while True:
        since_id = check_mentions(api, keywords, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    main(consumer_key,consumer_secret,access_token,access_token_secret)