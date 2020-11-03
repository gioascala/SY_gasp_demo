import os

#funzione che esegue il file vbs che a sua volta si occupa di avviare il file .bat che si occupa di ricercare il PID dei processi che interrogano la porta 8080
#per salvare su file l'output del .bat aggiungere al contenuto di porta.bat > "pathsalvataggio/salva.txt"
os.system(r'"porta.vbs"')
print("eseguito")