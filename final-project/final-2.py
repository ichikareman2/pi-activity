from flask import Flask

def main():
  CAMERA_FOLDER_PATH = "/home/pi/Camera"
  LOG_FOLDER_PATH = "/home/pi/Camera"
  LOG_FILE_PATH = LOG_FOLDER_PATH + "/" + "capture_log.txt"

  app = Flask(__name__, static_url_path=CAMERA_FOLDER_PATH, static_folder=CAMERA_FOLDER_PATH)

  @app.route("/")
  def index():
    return "Hello"

  @app.route("/check-movement")
  def check_movement():
    last_line = None
    with open(LOG_FILE_PATH, "r") as f:
      for line in f:
        pass
      last_line = line
    if last_line is None:
      return "No logs"
    with open("./templates/check_movement_template.html", "r") as f:
      template = f.read()
      readyhtml = template.replace("{{file_path}}", last_line)
      return readyhtml

  app.run(host="0.0.0.0", port=8080)

main()