# import nocsmtranslator
# print(nocsmtranslator.translateForMe("en","th","chicken eat a huge cat"))
# print(nocsmtranslator.translateForMe("th","en","ไก่จิกเด็กตายบนปากโอ่ง"))

# -*- coding: utf-8 -*-

import http.client, urllib.parse, uuid, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = '75a648040ae949f594acc7b25221a622'

host = 'api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

# Translate to German and Italian.
params = "&to=en";

text = 'สวัสดีครับ'

def translate (content):

    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    conn = http.client.HTTPSConnection(host)
    conn.request ("POST", path + params, content, headers)
    response = conn.getresponse ()
    return response.read ()

requestBody = [{
    'Text' : text,
}]
content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
result = translate (content)

# Note: We convert result, which is JSON, to and from an object so we can pretty-print it.
# We want to avoid escaping any Unicode characters that result contains. See:
# https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
output = json.dumps(json.loads(result), indent=4, ensure_ascii=False)

print (output)