from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings

import re

class CustomSessionMiddleware(SessionMiddleware):

    def process_response(self, request, response):
        response = super(CustomSessionMiddleware, self).process_response(request, response)
        #You have access to request.user in this method
        try:
            path_info = request.path
            pattern = re.compile("(admin)", re.IGNORECASE)
            if not pattern.search(path_info):
                del response.cookies[settings.SESSION_COOKIE_NAME]
        except:
            pass
        return response