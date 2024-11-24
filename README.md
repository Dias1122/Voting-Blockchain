# Система электронного голосования на основе блокчейна
<br><br>
Что такое блокчейн?
<https://www.youtube.com/watch?v=ksZ6YhrErOk>
<br><br>
Система голосования на основе блокчейна была разработана как обучающее программное обеспечение для изучения блокчейна и его свойств, некоторые из функций, использованных в этом проекте:

- **Python**.
- **Blockchain**.
- **Cryptography**.
- **PyCrypto [pycryptodome]**.
- **Криптографический хэш SHA256**.
- **Асимметричный алгоритм шифрования с закрытым и открытым ключом RSA**.
- **Асимметричные цифровые подписи RSASSA-PKCS1-v1_5**.

Блокчейн — это общий неизменяемый реестр, который упрощает процесс записи транзакций и отслеживания активов в бизнес-сети.

Актив может быть:
- Материальным (дом, машина, наличные, земля)
- Нематериальным (интеллектуальная собственность, патенты, авторские права, брендинг).

Практически все, что имеет ценность, можно отслеживать и продавать в сети блокчейнов, что снижает риск и сокращает расходы для всех участников.

Блокчейн — это децентрализованный, распределенный и часто публичный цифровой реестр, состоящий из записей, называемых блоками, который используется для записи транзакций на многих компьютерах, так что любой задействованный блок не может быть изменен задним числом без изменения всех последующих блоков. Это позволяет участникам проверять и проверять транзакции независимо и относительно недорого.

.

- Он подтверждает, что каждая единица стоимости была передана только один раз, решая давнюю проблему двойных расходов.

- Блокчейн был описан как протокол обмена ценностями.

- Блокчейн может поддерживать права собственности, поскольку при правильной настройке для детализации соглашения об обмене он предоставляет запись, которая обязывает к предложению и принятию.

## Блоки

Блоки содержат пакеты действительных транзакций, которые хэшируются и кодируются в дереве Меркла. Каждый блок включает криптографический хэш предыдущего блока в блокчейне, связывая их. Связанные блоки образуют цепочку. Этот итеративный процесс подтверждает целостность предыдущего блока, вплоть до исходного блока генезиса.

## Конфиденциальность и блокчейн *`[5]`*

Блокчейн — это общая база данных, которая записывает транзакции между двумя сторонами в неизменяемом реестре. Блокчейны документируют и подтверждают псевдонимное владение всеми существующими монетами в экосистеме криптовалюты в любой момент времени с помощью криптографии.

> После того, как транзакция проверена и криптографически проверена другими участниками или узлами в сети, она превращается в «блок» в блокчейне.

Блок содержит информацию о времени совершения транзакции, предыдущих транзакциях и сведениях о транзакции. После записи в виде блока транзакции упорядочиваются в хронологическом порядке и не могут быть изменены

## Закрытые и открытые ключи

- Ключевым аспектом конфиденциальности в блокчейнах является использование закрытых и открытых ключей. Системы блокчейнов используют асимметричную криптографию для защиты транзакций между пользователями. В этих системах у каждого пользователя есть открытый и закрытый ключ.

- Эти ключи представляют собой случайные строки чисел и криптографически связаны. Математически невозможно, чтобы пользователь угадывал закрытый ключ другого пользователя по его открытому ключу. Это обеспечивает повышение безопасности и защищает от хакеров.

> Открытые ключи могут быть переданы другим пользователям в сети, поскольку они не раскрывают никаких персональных данных. У каждого пользователя есть адрес, который выводится из открытого ключа с помощью хэш-функции.

- Эти адреса используются для отправки и получения активов в блокчейне, таких как криптовалюта. Поскольку сети блокчейнов являются общими для всех участников, пользователи могут просматривать прошлые транзакции и активность, которая происходила в блокчейне.

- Отправители и получатели прошлых транзакций представлены и обозначены их адресами; личности пользователей не раскрываются. Открытые адреса не раскрывают личную информацию или идентификацию; скорее, они действуют как псевдонимные личности.

> Рекомендуется, чтобы пользователи не использовали открытый адрес более одного раза; эта тактика исключает возможность отслеживания прошлых транзакций определенного адреса злоумышленником в попытке раскрыть информацию. Закрытые ключи используются для защиты личности и безопасности пользователя с помощью цифровых подписей.

- Закрытые ключи используются для доступа к средствам и личным кошелькам в блокчейне; они добавляют уровень аутентификации личности.

```Когда люди хотят отправить деньги другим пользователям, они должны предоставить цифровую подпись, которая создается при предоставлении закрытого ключа. Этот процесс защищает от кражи средств.```

## PyCrypto 

### Генерация случайных чисел

Вот текущий список известных проблем/ошибок генерации случайных чисел, которые были обнаружены в предыдущих версиях PyCrypto:

- ```В версиях до v2.6.1 Crypto.Random был небезопасен при использовании fork() в некоторых случаях. См. рекомендации по CVE-2013-1445 для получения дополнительной информации. Пользователям рекомендуется обновиться до PyCrypto v2.6.1 или более поздней версии.```

- ```В версиях до v2.1.0 Crypto.Util.randpool.RandomPool был небезопасен в обычном использовании. Он вообще не был потокобезопасным или fork-безопасным, и не всегда правильно заполнялся энтропией. Это было задумано, но большинство разработчиков приложений просто считывали его, не задумываясь, что приводило к небезопасным приложениям. См. эту ветку для получения дополнительной информации. Теперь он устарел и будет удален в будущем выпуске; используйте вместо него Crypto.Random или os.urandom.```

> Хранение пула энтропии в программе пользовательского пространства — сложная задача, которая может привести к ошибкам. Особенно сложно сделать это надежно в универсальной криптографической библиотеке, и ошибки случаются довольно часто. Будем надеяться, что однажды операционные системы предоставят средства генерации случайных чисел, которые будут достаточно быстрыми, надежными и заслуживающими доверия, чтобы полностью заменить множество генераторов случайных чисел пользовательского пространства, которые в настоящее время досаждают нашему программному обеспечению.

| Пакет PyCrypto | Модуль | Описание |
|-------------------------------------------|--------------------------|---------------------------|
| **Crypto.Hash** | Модуль SHA256 | - Криптографический хэш-алгоритм SHA-256. <br> - SHA-256 принадлежит к семейству криптографических хэшей SHA-2. Он создает 256-битный дайджест сообщения. |
| **Crypto.PublicKey** | Модуль RSA | - Алгоритм криптографии с открытым ключом RSA (подпись и шифрование). <br> - RSA является наиболее распространенным и используемым алгоритмом криптографии с открытым ключом. |
| **Crypto.Signature** | Модуль PKCS1_v1_5 | - Протокол цифровой подписи RSA в соответствии с PKCS#1 v1.5 <br> - Эту схему правильнее называть RSASSA-PKCS1-v1_5. |

> **Примечание**: При использовании шифрования RSA с дополнением PKCS1_AOEP выдаются предупреждения об устаревании. Предварительные условия: закрытый ключ RSA в mykey.pem

> **Примечание**: библиотека PyCrypto устарела, и следует перейти на pycryptodome для API-совместимой, обновленной библиотеки или на cryptographyio для более современного API.
