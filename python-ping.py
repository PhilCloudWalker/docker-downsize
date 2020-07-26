import urllib3

    # TODO: Change to XCOMM
bucket = "bayer-image-car"
input_image_path = "1_input/foto2.jpg"
output_image_path = "2_downsizing/new.jpg"# + input_image_path.split("/")[-1]

    # TODO: change url for docker

def task():
    url = "http://0.0.0.0:8080/image-resize"


        # TODO: DO NOT TOUCH
    data = {
        "bucket": bucket,
        "input_image_path": input_image_path,
        "output_image_path": output_image_path,
        "side":300
    }

    http = urllib3.PoolManager()
    r = http.request(
        'POST',
        url,
        fields=data)

    # TODO: GET NEW PATH OF DOWNSIZED FILE --> XCOMM
print(r.data)