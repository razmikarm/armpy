from armpy.hy import *

տպել()
տպել('Հայերեն', 'տարբերակի', 'ստուգում', բաժանիչ=' ~ ', վերջ='!\n')
տպել()
թիվ1 = մուտքագրել("Գրեք թիվ 1֊ը: ")
թիվ2 = մուտքագրել("Գրեք թիվ 2-ը: ")
թիվ1 = ամբողջ(թիվ1)
թիվ2 = ամբողջ(թիվ2)
պատասխան = թիվ1 / թիվ2
տպել("Գումար:", թիվ1 + թիվ2)
տպել("Բաժանում:", պատասխան)
տպել("Կլորացված:", կլոր(պատասխան))