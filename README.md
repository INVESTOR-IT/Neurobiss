<h1 align="center"> Тест Neurobiss </h1>

**Deploy:**<br>
`docker build -t neurobiss .`<br>
`docker run -p 8000:8000 neurobiss`<br>

---

**ENV**<br>
Копируем из `.env.example` название и подставляем свои значения<br>
Что бы получить `CHAT_ID`, запускам `python3 app/telebot/telebot.py`, переходим к боту `@NeurobissTest_Bot`, запускам бота.<br>
В логах получам `CHAT_ID` и прописываем в `.env`

---

**Эндпоинты**<br>
`http://localhost:8000/health` - проверка, жив ли сервис<br>
`http://localhost:8000/amocrm_webhook` - получает с вебхука, обрабатывает, отправляет в телеграм бот<br>

---

**Эндпоинты**<br>
Создавая и меняя задачи в amoCRM, бот будет сообщать об изменениях