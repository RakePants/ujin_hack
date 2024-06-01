# Кейс "Доступ на территорию" | Хакатон Ujin Forum Зданий 
Команда AI_кабанчики.
## Описание решения
Сервис, способный отправлять уведомления в управляющую компанию в случае обнаружения посторонних лиц в некоторых помещениях.  

Целевая аудитория – управляющие компании. Они ежедневно сталкиваются с задачами управления и обеспечения безопасности в зданиях. С помощью нашего решения они смогут мгновенно получать уведомления о проникновении и быстро принимать меры.

Функционал системы начинается с интеграции с API Macroscop, который обеспечивает распознавание лиц и их учет. Как только Macroscop идентифицирует лицо, он автоматически отправляет уведомление нашему приложению, которое в свою очередь создает тикет в BMS Ujin или выдает лицу пропуск на объект.

Важный элемент продукта – веб-интерфейс, который позволяет пользователям просматривать детальные логи каждого события. В логах можно увидеть изображение лица, его уникальный ID, полные ФИО, точную дату и время обнаружения, а также статус и срок действия пропуска.
## Стек технологий
- React, Typescript 
- FastAPI, вебхуки, вебсокеты
- Микросервисная архитектура, паттерн Domain-Driven Design (DDD)
- MongoDB, объектное хранилище для фотографий
- Docker, nginx
## Инструкция по развертыванию
1. Клонировать репозиторий
2. Создать и заполнить .env-конфигурации в соответствии с файлами `.env.example`
3. Перейти в корневую папку проекта и выполнить команду `docker compose up --build` в терминале
