# Notes

## 2022/12/28

I had `SystemError: initialization of _psycopg raised unreported exception` error when I was running `docker-compose up -d` So I was trying to fixing it with migrating to python 3.9 in backend/Dockerfile
I want to setup order and checkout process, and adding paypal as payment gateway.

## 2022/12/20

I was trying to setup order and checkout process
Need a payment gateway, Searched for best ones. I want to have Paypal and Stripe.
Paypal just supports Django 2.2, I'm deciding to go with Django 3.2 or 2.2
Seems like doesn't matter, because Django 3.2 is backward compatible with 2.2 so whenever I want to upgrade to 3.2, It's easy and ready.
