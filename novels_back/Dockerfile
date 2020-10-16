FROM python:3.7.3

WORKDIR /usr/src/app

COPY . ./
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

CMD /bin/bash ./run.sh
