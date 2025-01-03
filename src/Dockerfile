FROM public.ecr.aws/lambda/python:3.11

COPY . ./
RUN python3.11 -m pip install -r requirements.txt -t .
RUN chmod -R 755 .

CMD ["app.lambda_handler"]
