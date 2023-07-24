"""
Project structure:

my_project/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── account_controller.py
│   │   ├── agent_controller.py
│   │   └── home_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── account/
│       │   └── add_agent.html
│       │   └── register.html
│       ├── agent/
│       │   └── show.html
│       └── home/
│           └── index.html
├── requirements.txt
└── run.py
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()