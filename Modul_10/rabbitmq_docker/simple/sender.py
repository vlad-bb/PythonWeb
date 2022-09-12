import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

msg = input('>>> ')
channel.basic_publish(exchange='', routing_key='hello', body=msg.encode())
print(f"[x] Sent: {msg}")
connection.close()
