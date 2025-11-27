from src.flask_app import flask_app


def test_home():
  ## app from falsk app, test_client is funcation, get is for home page come
  responce=app.test_client().get("/")
  assert responce.status_code==200
  assert responce.data== b"Hello Word, This is test Flask application!!"
