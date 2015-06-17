from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings

import re

class CustomSessionMiddleware(SessionMiddleware):

    def process_response(self, request, response):
        response = super(CustomSessionMiddleware, self).process_response(request, response)
        #You have access to request.user in this method
        print("CustomSessionMiddleware")
        try:
            path_info = request.path
            pattern = re.compile("(admin)", re.IGNORECASE)
            if not pattern.search(path_info):
                del response.cookies[settings.SESSION_COOKIE_NAME]
        except:
            pass
        return response

# 소셜계정으로 로그인하는 사용자는 패스워드가 존재하지 않는다.
# 만약 소셜계정 사용자가 비밀번호 리셋을 시도한다면 불가능함을 알린다.
class UserTypeFilterMiddleware(object):
    def process_request(self, request):
        print("Before Process!!")