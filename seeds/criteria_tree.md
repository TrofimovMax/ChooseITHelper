```mermaid
%%{init: {"themeVariables": {"fontFamily": "Arial, sans-serif"}}}%%
graph TD;
    Q6["What is your budget for implementing the Hybrid Chatbot?"] --> O51["Low Cost"]; %% Низкая стоимость
    Q6 --> O52["Moderate Cost"]; %% Средняя стоимость
    Q6 --> O53["High Cost"]; %% Высокая стоимость

    Q7["How important is security for your Hybrid Chatbot?"] --> O54["Basic Security"]; %% Базовая безопасность
    Q7 --> O55["Standard Security"]; %% Стандартная безопасность
    Q7 --> O56["Advanced Security"]; %% Продвинутая безопасность

    Q8["What level of scalability do you require for your Hybrid Chatbot?"] --> O57["Small Scale"]; %% Малый масштаб
    Q8 --> O58["Moderate Scale"]; %% Средний масштаб
    Q8 --> O59["Enterprise Scale"]; %% Корпоративный масштаб

    Q9["How important is ease of integration with existing systems?"] --> O60["Low Priority"]; %% Низкий приоритет
    Q9 --> O61["Moderate Priority"]; %% Средний приоритет
    Q9 --> O62["High Priority"]; %% Высокий приоритет

    Q10["What is the desired level of chatbot customization?"] --> O63["Basic Customization"]; %% Базовая настройка
    Q10 --> O64["Moderate Customization"]; %% Средняя настройка
    Q10 --> O65["Full Customization"]; %% Полная настройка

    %% Sequential Criteria Questions
    O51 --> Q7; %% From budget to security
    O52 --> Q7;
    O53 --> Q7;

    O54 --> Q8; %% From security to scalability
    O55 --> Q8;
    O56 --> Q8;

    O57 --> Q9; %% From scalability to integration
    O58 --> Q9;
    O59 --> Q9;

    O60 --> Q10; %% From integration to customization
    O61 --> Q10;
    O62 --> Q10;
