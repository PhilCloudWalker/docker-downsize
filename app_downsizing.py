from flask import request, Flask
from flask import jsonify
from PIL import Image
import boto3, os

app = Flask(__name__)
s3 = boto3.client('s3',
                  aws_access_key_id="AKIAYGBZKVH3JKDRLX42",
                  aws_secret_access_key="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")


@app.route("/image-resize", methods=["POST", "GET"])
def resize():
    if request.method == "GET":
        resp = jsonify(success=True)
        return resp

    elif request.method == "POST":
        bucket = request.form.get("bucket")
        input_image_path = request.form.get("input_image_path")
        output_image_path = request.form.get("output_image_path")
        side = request.form.get("side")

        print("--- Body Parameter ----")
        print(bucket)
        print(input_image_path)
        print(output_image_path)

        #run model
        print('--- Run anonymizer ----')
        side = int(side)
        size = (side, side)

        #---main ---#
        image = get_image(bucket, input_image_path, s3)
        image.thumbnail(size, Image.ANTIALIAS)
        save_image(image, bucket, output_image_path, s3)

        #TODO: return path of new file
        resp = jsonify(success=True)
        return resp
    else:
        resp = jsonify(success=False)
        return resp

#TODO: Change to lokal
def get_image(bucket, input_image_path, s3):

    s3.download_file(bucket, input_image_path, 'tmp/input.jpg')
    image = Image.open('tmp/input.jpg').convert('RGB')
    os.remove('tmp/input.jpg')
    return image

#TODO: Change to lokal
def save_image(image, bucket, output_image_path, s3):
    image.save('tmp/output.jpg')
    s3.upload_file('tmp/output.jpg', bucket, output_image_path)
    os.remove('tmp/output.jpg')

if __name__ == '__main__':
    #bucket
    #get_image()

    app.run(host='0.0.0.0', debug=False, threaded=False, port=80)