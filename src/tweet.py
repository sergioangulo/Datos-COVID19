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
        my_positividad = pd.read_csv('../output/producto49/Positividad_Diaria_Media_T.csv')
        my_mediamovil = pd.read_csv('../output/producto75/MediaMovil_casos_nuevos_T.csv')
        mediamovil_nacional = int(pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]))
        variacion_nacional = float(100*(pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]) - pd.to_numeric(
            my_mediamovil.iloc[my_mediamovil.index.max() - 7][17]))/pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]))
        positividad_nacional = float(100*pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][4]))
        variacion_positividad = float(100*(pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][4]) - pd.to_numeric(
            my_positividad.iloc[my_positividad.index.max() - 7][4]))/pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][4]))
        positividad_nacional = ("%.2f" % positividad_nacional)

        # create update elements
        tweet_text = '🤖Actualicé el reporte diario del @ministeriosalud de hoy 💫, gracias a la Subsecretaría de Salud Pública y de Redes Asistenciales. Hay '+str(mediamovil_nacional)+' casos nuevos promedio en los últimos 7 días, con positividad de '+str(positividad_nacional)+'%. Más detalles en los productos en la imagen.  https://github.com/MinCiencia/Datos-COVID19'


        if variacion_nacional >= 0 and variacion_positividad >= 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos creció en '+str(variacion_nacional)+'% y la positividad en '+str(variacion_positividad)+'% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        elif variacion_nacional >= 0 and variacion_positividad < 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos creció en '+str(variacion_nacional)+'% y la positividad bajó en '+str(variacion_positividad)+'% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        elif variacion_nacional < 0 and variacion_positividad < 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos creció en '+str(variacion_nacional)+'% y la positividad en '+str(variacion_positividad)+'% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        elif variacion_nacional < 0 and variacion_positividad >= 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos bajó en ' + str(
                variacion_nacional) + '% y la positividad aumentó en ' + str(
                variacion_positividad) + '% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        # Generate text tweet with media (image)
        media1= my_api.media_upload('./img/Datos covid_Bot_A_g1.png')
        media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')
        tweet = my_api.update_status(status=tweet_text, media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])
        my_api.update_status(status=reply1_text, in_reply_to_status_id=tweet.id)

    elif carrier == 'mmamp':
        # create update elements
        tweet_text = '🤖Actualicé los datos de calidad del aire en todo el territorio nacional, desde las estaciones del SINCA del @MMAChile 💫. Mira específicamente qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_G_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id])

    elif carrier == 'informeepi':
        my_epi= pd.read_csv('../output/producto1/Covid-19_T.csv')
        fecha_informe = my_epi.iloc[my_epi.index.max()-1][0]


        # create update elements
        tweet_text = '🤖Actualicé los datos del Informe Epidemiológico publicado por @ministeriosalud de hoy 💫, con los datos correspondientes al '+fecha_informe+'. Gracias al equipo de especialistas en epidemiología. Mira qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_B_g1.png')
        media2= my_api.media_upload('./img/Datos covid_Bot_B_g2.png')
        media3= my_api.media_upload('./img/Datos covid_Bot_B_g3.png')
        media4= my_api.media_upload('./img/Datos covid_Bot_B_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])

    elif carrier == 'vacunacion':
        my_vacunacion = pd.read_csv('../output/producto76/vacunacion_t.csv')
        vacunados = int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()][1]))
        vacunados_pauta_completa = int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()][2]))
        my_vacunacion_avance = vacunados/15000000
        my_vacunacion_avance_pauta_completa = vacunados_pauta_completa/15000000
        my_vacunacion_avance = ("%.2f" % my_vacunacion_avance)
        my_vacunacion_avance_pauta_completa = ("%.2f" % my_vacunacion_avance_pauta_completa)

        # create update elements
        tweet_text = '🤖Actualicé los datos que muestran el avance en la campaña de vacunación #YoMeVacuno de hoy 💫, gracias a APS y DIPLAS, @ministeriosalud. Van '+str(vacunados)+' vacunados con primera dosis en 🇨🇱. Mira específicamente qué actualicé en la imagen y clona el github https://github.com/MinCiencia/Datos-COVID19'
        reply1_text = '🤖Además, un total de ' + str(vacunados_pauta_completa) + ' personas tienen pauta completa. En 🇨🇱, un ' + my_vacunacion_avance + '% tiene al menos una dosis, y un ' + my_vacunacion_avance_pauta_completa + '% completó su pauta de vacunación. Detalles en https://github.com/MinCiencia/Datos-COVID19'

        media1= my_api.media_upload('./img/Datos covid_Bot_C_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        tweet = my_api.update_status(status=tweet_text, media_ids=[media1.media_id])
        my_api.update_status(status=reply1_text, in_reply_to_status_id=tweet.id)


    elif carrier == 'testeo':
        tweet_text = "Actualicé los datos del informe de testeo y trazabilidad del @ministeriosalud de hoy 💫, ¡gracias @FunCienciayVida! Mira específicamente qué actualicé en la imagen, y clónate el github https://github.com/MinCiencia/Datos-COVID19"
        media1 = my_api.media_upload('./src/img/Datos covid_Bot_D_g1.png')
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
