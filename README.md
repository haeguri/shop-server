## intro

#### Stack

- python 3.4
- django 1.7.6
- django-restframework
- django-allauth
- django-rest-auth

#### Project Structure

	- second
      ㄴ settings.py
      ㄴ custom_auth.py
      ㄴ middleware.py
      ㄴ urls.py
    - snippets
      ㄴ models.py
      ㄴ forms.py
      ㄴ admin.py
      ㄴ forms.py
      ㄴ serializers.py
      ㄴ urls.py
      ㄴ views.py
    - cart
      ㄴ models.py
      ㄴ serializer.py
      ㄴ urls.py
      ㄴ views.py

## URL Structure

#### snippets/urls.py

	/api/search
    /api/products/(?P<product_id>[0-9]+)
    /api/hashtags
    /api/channels
    /api/channels/(?P<channel_id>[0-9]+)
    /api/issues
    /api/issues/(?P<issue_id>[0-9]+)
    /api/brands/(?P<brand_id>[0-9]+
    )
    

#### cart/urls.py

	asdf
    asdf


##  Model Structure

#### snippets/models.py

![](https://lh3.googleusercontent.com/D7PCvXLHdBX6RNvrTNO2gWLkhIj633PwgR3MjkvanaBT2qiQWOnUELi8NLXFgdVX9NrHy_T1yncqc3xxWhIObIT7Dxc__lRYU-uTMSTb8q6RyvV5jo_USV_yyvYdNOwpd3-efySFM22hjv5NVcQSnQDVXWXiK1xEOwq5McIiCXVhyM3lcRSIzE5JbvPpegndH-7N23hZ8yhE56r_bqBGAkudp3Ek-eQ8qdCSQuwgqE4iinWIzfJSrK0kTrGRRUalQfLftaLBTkp6v-MpRo9-v1xVPrGXO81NL94K0SKqmeSuWzDsefwJOGrQmz25AO3IxxKoNb6bu37hFADbGCjZ3Mt3G8gIAEuBIth-x1lA6615Pc1jEEwDA0AbV89PrsI033WN9prQhzAAxFKMwMrWE4cbOI2xG7jdEQp6qCfXkzxhja28p7TG3JXrNGDuhg0g3zDqzsq2Ev6t-KgB6Hm7CMG9WypHLbu4f6-y95A3j8ddSju8hS71DpTewDQ9ETVl6eO5OsD4IS2UbQvvyYOtha9lTdyZAHoE1ml9D3ehhMAp0zDG8DxNCoWrCOeUd35KIl9QfhUXf5Lh61AC1Jb2F--xhvslJXOKpmJeu_TZh9Iji2aFrMT1=w1440-h656-no)

#### cart/models.py

![](https://lh3.googleusercontent.com/lQVQZO-GXEx6ka0XGuUpN2vWLCQ8sD1FoULdtKLQzKc0mU07c-XRTjt0_uZ4IEY4BceHxWikLFOVmbycvoXhBkOAGUFmsELJwzRjHn97vkwJV4T9ZQZD5od0PXciN95fsiA8vpAEVxy0ijiuAA3ZPp9pVoqG48M0wIbTDgLrYGwTvAtO7d4j7hzQlYVXMfVEIFzc4cn3CJY2738kCA6-hXePf6JuUsKzUMNMEObulIOwgtHtcITJ77UTddkqrhlysgSWcJhy1b1m99BzBZUHjw1-JK6p5xD_fbu-c8KeJTs0Hs2iddN-lCsM3JuHcE9w6Of1lDQc3VqeQ6_3JiRxWSAHrG6wTZFbP_VbTmsA8RsD8bzDkFEKkrxkyJWMNY81evfqCWKW2T5PSHFR799UuWwR-KkfGLTf0V2cGH_8MqhyV97acHUqGHiCg4f3igbO_Hmi5KEO6QVu7rzgpcWbPaxtYzTyXLsEL2rCzFYK9rHRdl-TQrwKo1ZgXIgjgqUBqG6DtPbVppINXpN3Wt5MtwO1GKfcnTHC8C2cQxZ3owBvnEibIfhwgN89YpLCv7_E75ltqQ4XmVkY-15y8I5nDthhfjI3GNVFiAvCDYxQWFrAmFpc=w1440-h980-no)




