from flask import Flask, request
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

app = Flask(__name__)

WECHAT_TOKEN = 'your_token_here'

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')

    try:
        check_signature(WECHAT_TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        return "Invalid signature", 403

    if request.method == 'GET':
        echostr = request.args.get('echostr', '')
        return echostr

    # POST请求处理用户消息
    msg = parse_message(request.data)
    if msg.type == 'text':
        reply = create_reply(f'您发送的消息是: {msg.content}', msg)
    else:
        reply = create_reply('暂时只支持文本消息', msg)
    return reply.render()

if __name__ == '__main__':
    app.run(port=80)
