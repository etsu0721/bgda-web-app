# Import application from __init__.py
from app import app

# Run application
if __name__ == '__main__':
    app.run(debug=True) # Enable dev server to show changes without having to restart
      