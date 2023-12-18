###Для запуска тестов и просмотра отчетов скачать репозиторий, в папке с проектом выполнить команды:
###Windows
`python -m venv venv`  
`venv\Script\activate`  
`pip install -r requirements.txt`  
`pytest .`  
`allure serve allure-results`

##nix & macOS
`python -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  
`pytest .`  
`allure serve ./allure-results`
