


<!-- ABOUT THE PROJECT -->
## About The Project

It's a Telegram Bot application. The project contains 3 buttons that are "Stupid", "Fat", "Dump". When we clicking a button, appropriate message showed on our Telegram channel. The project contain Login and Registration option, and count the message click event of each user and display the count result of each user.


---
**NOTE**

For the security purpose, I have hidden the Bot token. if you want to continue with this. you can create the ".env" file add this 


   ```sh
   TOKEN=Your Token
   ```
   
   - also add your Channel Name in settings.py
   - add chat_id in views.py



---

<!-- GETTING STARTED -->
## Getting Started

If you would love to run this project on your local env, I will walk you through:


### Installation

1. Create virutal environment
   ```sh
   virtualenv venv
   ```
2. Activate virtualenv
   ```sh
   windows: venv\Script\activate
   Linux : source venv/bin/activate  
   ```
3. Clone the repo
   ```sh
   git clone https://github.com/abdullakn/impress.ai.git
   ```
4. Install requirements.txt
   ```sh
   pip install -r requirments.txt
   ```
5. Create DB and add into settings.py
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```   
6. Run Project: <br>
   go to the project folder where manage.py file is present
   ```JS
   python manage.py runserver
   ```
