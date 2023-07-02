python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 5001

cd ./stable-diffusion-webui
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh) -f --listen --xformers --enable-insecure-extension-access --theme dark --api 

