# python_recaptcha

* Repository: https://github.com/google/recaptcha
* Version: 0.1.0
* License: BSD

## Description

python_recaptcha is a (very) rough Python 3 port of Google's [recaptchalib.php](https://github.com/google/recaptcha/blob/1.0.0/php/recaptchalib.php) that I used in a Django project.

Please see the Google repository for setup details.

## Getting started

### Dependencies

urllib.parse, urllib.request, json

### Usage

from .recaptchalib import ReCaptcha

```python
from .recaptchalib import ReCaptcha

secret = RECAPTCHA SECRET
recaptcha = ReCaptcha(secret)

response = recaptcha.verifyResponse(
				request.META.get('REMOTE_ADDR'),
				request.POST['g-recaptcha-response'],)
				
if response is not None and response.success:
	# Do whatever it is you need to do
```

## Tests

Yeah ... there are none. I might have mentioned this was a rough port - just built to get me through a need. So tests did not make the agenda.

If you'd like to contribute testing code, that's be great.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Licence

This project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).

### Reference documents

[https://webdesign.tutsplus.com/tutorials/how-to-integrate-no-captcha-recaptcha-in-your-website--cms-23024]()

[https://github.com/google/recaptcha/blob/1.0.0/php/recaptchalib.php]()

