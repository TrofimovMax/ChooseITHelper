```mermaid
%%{init: {"themeVariables": {"fontFamily": "Arial, sans-serif"}}}%%
graph LR;
    Q1["What is the primary goal of your project?"] --> O1["Website"]; %% Веб-сайт
    Q1 --> O2["Mobile Application"]; %% Мобильное приложение
    Q1 --> O3["Game"]; %% Игра
    Q1 --> O4["Enterprise System"]; %% Корпоративная система
    Q1 --> O5["E-commerce"]; %% Интернет-магазин
    Q1 --> O6["Educational Platform"]; %% Образовательная платформа
    Q1 --> O7["Project Management Software"]; %% Программное обеспечение для управления проектами
    Q1 --> O8["Social Network"]; %% Социальная сеть
    Q1 --> O9["Financial Application"]; %% Финансовое приложение
    Q1 --> O10["Data Analytics Platform"]; %% Платформа для аналитики данных
    Q1 --> O11["Health & Fitness Platform"]; %% Платформа для здоровья и фитнеса
    Q1 --> O12["Messenger"]; %% Мессенджер
    Q1 --> O13["Booking Platform"]; %% Платформа для бронирования
    Q1 --> O14["CRM System"]; %% CRM-система
    Q1 --> O15["Business Automation Software"]; %% Программное обеспечение для автоматизации бизнеса

    Q2["What key features do you need?"] --> O16["Chat"]; %% Чат
    Q2 --> O17["Gallery"]; %% Галерея
    Q2 --> O18["Feedback Form"]; %% Форма обратной связи
    Q2 --> O19["Advanced Search"]; %% Расширенный поиск
    Q2 --> O20["Admin Panel"]; %% Панель администратора
    Q2 --> O21["Recommendation System"]; %% Система рекомендаций
    Q2 --> O22["Authorization & Registration"]; %% Авторизация и регистрация
    Q2 --> O23["Subscriptions & Notifications"]; %% Подписки и уведомления
    Q2 --> O24["Online Payments"]; %% Онлайн-платежи
    Q2 --> O25["Analytics"]; %% Аналитика

    Q3["What additional features do you want in the chat?"] --> O26["Group Chat"]; %% Групповой чат
    Q3 --> O27["File Sharing"]; %% Отправка файлов
    Q3 --> O28["Video Calls"]; %% Видеозвонки
    Q3 --> O29["Chatbot"]; %% Чат-бот
    Q3 --> O30["Message History"]; %% История сообщений
    Q3 --> O31["Notifications"]; %% Уведомления
    Q3 --> O32["Encryption"]; %% Шифрование
    Q3 --> O33["Message Search"]; %% Поиск по сообщениям
    Q3 --> O34["Multilingual Chat Support"]; %% Поддержка мультиязычного интерфейса
    Q3 --> O35["Social Media Integration"]; %% Интеграция с социальными сетями

    Q4["What type of Chatbot functionality do you need?"] --> O36["AI-Powered Chatbot"]; %% Чат-бот с ИИ
    Q4 --> O37["Rule-Based Chatbot"]; %% Чат-бот на основе правил
    Q4 --> O38["Hybrid Chatbot (AI + Rules)"]; %% Гибридный чат-бот
    Q4 --> O39["Multilingual Chatbot"]; %% Мультиязычный чат-бот
    Q4 --> O40["Voice-Enabled Chatbot"]; %% Чат-бот с голосовой поддержкой
    
    Q5["What is the main goal of your Hybrid Chatbot?"] --> O41["Customer Support"]; %% Поддержка клиентов
    Q5 --> O42["Sales Assistance"]; %% Помощь в продажах
    Q5 --> O43["Technical Support"]; %% Техническая поддержка
    Q5 --> O44["User Engagement"]; %% Вовлечение пользователей
    Q5 --> O45["Feedback Collection"]; %% Сбор обратной связи

    %% Sequential Alternatives Questions
    O1 --> Q2; %% Mobile Application connected to Key Features
    O16 --> Q3; %% Chat connected to Additional Chat Features
    O26 --> Q3; %% Group Chat connected back to Additional Chat Features
    O29 --> Q4;
    O38 --> Q5;
