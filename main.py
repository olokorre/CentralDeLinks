from app import app
from decouple import config

if __name__ == "__main__":
	app.run(debug=config('DEBUG') == 'true', host='0.0.0.0', port=config('PORT'))
