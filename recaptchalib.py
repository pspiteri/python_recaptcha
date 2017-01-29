from urllib import parse, request
import json


class ReCaptchaResponse:
    success = None
    error_codes = None


class ReCaptcha:
    SIGNUPURL = "https://www.google.com/recaptcha/admin"
    SITEVERIFYURL = "https://www.google.com/recaptcha/api/siteverify?"
    VERSION = "python_3.4"
    secret = None

    def __init__(self, secret):
        if secret == None or secret == "":
            raise ValueError('Secret is None or blank')

        self.secret = secret

    def encodeQS(self, data):
        req = ""

        for key, value in data.items():
            value_to_append = key + "=" + parse.quote_plus(value) + "&"
            req = req + value_to_append

        # Cut the last '&'
        req = req[:-1]

        return req

    def submitHTTPGet(self, path, data):
        req = self.encodeQS(data)
        response = request.urlopen(path + req).read(1000)

        return response

    def verifyResponse(self, remote_ip, response):

        if response == None or len(response) == 0:
            recaptcha_response = ReCaptchaResponse()
            recaptcha_response.success = False
            recaptcha_response.error_codes = 'missing input'

            return recaptcha_response

        data = {
            'secret': self.secret,
            'remoteip': remote_ip,
            'v': self.VERSION,
            'response': response,
        }

        get_response = self.submitHTTPGet(self.SITEVERIFYURL, data)

        answers = json.loads(get_response.decode())
        recaptcha_response = ReCaptchaResponse()

        print('ANSWERS')
        print(answers)

        if answers['success'] == True:
            recaptcha_response.success = True
        else:
            recaptcha_response.success = False
            if 'error-codes' not in answers:
                recaptcha_response.error_codes = None
            else:
                recaptcha_response.error_codes = answers['error-codes']  # error-codes are optional

        return recaptcha_response
