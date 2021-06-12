1. Erstelle und aktiviere ein 'virtual environment'
    -> https://docs.python.org/3/tutorial/venv.html

2. Installieren von der Datei 'requirements.txt'

3. Erstelle in google workspace for developers: 'credentials.json' und füge sie dem Verzeichniss Hinzu.
   Wenn die .json Datei einen anderen Namen hat muss sie in 'credentials.json' umbenannt werden.
    -> https://developers.google.com/workspace/guides/create-project
    -> https://developers.google.com/workspace/guides/create-credentials   (Google Drive API)

4. Führe die Datei 'main.py' aus und melde dich über den Browser mit deinem Google account an.
   Dies fügt dem Verzeichniss die Datei 'token.json' hinzu.

5. Fülle die Variablen in der Datei 'email_configuration' mit den Anmeldedaten und Einstellungen der Emailadresse über die du eine Email 
   versenden möchtest.
    
6. Gebe am Ende der Datei 'main.py' in dem Funktionsaufruf: send_mail_with_pdf.sendMail(<recipient-email-adress>, 'temp.pdf', document_infos[0]['name')
   anstelle des Platzhalters die Emailadresse, an die du senden möchtest, als String ein.

7. Nun sollte beim Ausführen der Datei 'main.py' eine Email versendet werden mit dem ersten Document aus 'document_infos'.
   Zudem werden im Terminal die Metainformationen aller Documente ausgedruckt.

Viel Spaß