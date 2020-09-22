import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tags')

cartoes = {
    '1971212171110' : 'teste1',
    '1971212171111' : 'teste2',
    '1971212171112' : 'teste3'
}

for id, usuario in cartoes.items():
    table.put_item(
        Item={
            'id': id,
            'usuario': usuario
        }
    )
    print(id, ': ', usuario)