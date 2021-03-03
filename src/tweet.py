import sys
import tweepy
import pandas as pd



def tweeting(consumer_key, consumer_secret, my_access_token, my_access_token_secret, carrier):

    # Authentication
    my_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    my_auth.set_access_token(my_access_token, my_access_token_secret)
    my_api = tweepy.API(my_auth)


    # tweet
    if carrier == 'reportediario':
        my_mediamovil = pd.read_csv('../output/producto75/MediaMovil_casos_nuevos_T.csv')
        mediamovil_nacional = int(pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]))
        variacion_nacional = float(100*(pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]) - pd.to_numeric(
            my_mediamovil.iloc[my_mediamovil.index.max() - 7][17]))/pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]))
        variacion_nacional = ("%.2f" % variacion_nacional)
        # create update elements
        tweet_text = '🤖Actualicé los datos del reporte diario del @ministeriosalud de hoy 💫, gracias a los equipos de la Subsecretaría de Salud Pública y Redes Asistenciales. La media móvil semanal de casos nuevos para hoy es '+str(mediamovil_nacional)+'Mira qué actualicé en las imágenes y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_A_g1.png')
        media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        if variacion_nacional >= 0:
            reply1_text = '🤖La variación porcentual de la media móvil semanal de casos nuevos respecto de la semana pasada aumentó en un '+str(variacion_nacional)+'%. :(. Mira más detalles en https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75'
        else:
            reply1_text = '🤖La variación porcentual de la media móvil semanal respecto de la semana pasada disminuyó en un '+str(variacion_nacional)+'%. :). Mira más detalles en https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75'

        # Generate text tweet with media (image)
        tweet = my_api.update_status(status=tweet_text, media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])
        my_api.update_status(status=reply1_text, in_reply_to_status_id=tweet.id)

    elif carrier == 'mmamp':
        # create update elements
        tweet_text = '🤖Actualicé los datos de calidad del aire en todo el territorio nacional, desde las estaciones del SINCA del @MMAChile 💫. Mira específicamente qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        # media1= my_api.media_upload('./img/Datos covid_Bot_A_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text)
                             # media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])

    elif carrier == 'informeepi':
        # create update elements
        tweet_text = '🤖Actualicé los datos del Informe Epidemiológico publicado por @ministeriosalud de hoy 💫, gracias a su equipo de especialistas en epidemiología. Mira qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_B_g1.png')
        media2= my_api.media_upload('./img/Datos covid_Bot_B_g2.png')
        media3= my_api.media_upload('./img/Datos covid_Bot_B_g3.png')
        media4= my_api.media_upload('./img/Datos covid_Bot_B_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])

    elif carrier == 'vacunacion':
        my_vacunacion = pd.read_csv('../output/producto76/vacunacion_t.csv')
        vacunados = int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()][1]))
        # create update elements
        tweet_text = '🤖Actualicé los datos que muestran el avance en la campaña de vacunación #YoMeVacuno de hoy 💫, gracias a APS y DIPLAS, @ministeriosalud. Van '+str(vacunados)+' vacunados en 🇨🇱. Mira específicamente qué actualicé en la imagen y clona el github https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_C_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id
                                                           # media2.media_id,
                                                           # media3.media_id,
                                                           # media4.media_id
                                                           ])

if __name__ == '__main__':

    if len(sys.argv) == 6:
        consumer_key = sys.argv[1]
        consumer_secret_key = sys.argv[2]
        my_access_token = sys.argv[3]
        my_access_token_secret = sys.argv[4]
        carrier = sys.argv[5]

        tweeting(consumer_key, consumer_secret_key, my_access_token, my_access_token_secret, carrier)
