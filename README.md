# littlelemon

## Browsable
- [/](http://127.0.0.1:8000/)
- [/about/](http://127.0.0.1:8000/about/)
- [/menu/](http://127.0.0.1:8000/menu/)
- [/menu/\<int:pk\>/](http://127.0.0.1:8000/menu/1/)
- [/book/](http://127.0.0.1:8000/book/)
- [/reservations/](http://127.0.0.1:8000/reservations/)
- [/login/](http://127.0.0.1:8000/login/)


## API

### Djoser
- [/auth/users/](http://127.0.0.1:8000/auth/users/)
- [/auth/users/me/](http://127.0.0.1:8000/auth/users/me/)
- [/auth/users/confirm/](http://127.0.0.1:8000/auth/users/confirm/)
- [/auth/users/resend_activation/](http://127.0.0.1:8000/auth/users/resend_activation/)
- [/auth/users/set_password/](http://127.0.0.1:8000/auth/users/set_password/)
- [/auth/users/reset_password/](http://127.0.0.1:8000/auth/users/reset_password/)
- [/auth/users/reset_password_confirm//](http://127.0.0.1:8000/auth/users/reset_password_confirm/)
- [/auth/users/set_username/](http://127.0.0.1:8000/auth/users/set_username/)
- [/auth/users/reset_username/](http://127.0.0.1:8000/auth/users/reset_username/)
- [/auth/users/reset_username_confirm//](http://127.0.0.1:8000/auth/users/reset_username_confirm/)
- [/auth/token/login/](http://127.0.0.1:8000/auth/token/login/)
- [/auth/token/logout/](http://127.0.0.1:8000/auth/token/logout/)

### Others
- [/menu/](http://127.0.0.1:8000/menu/)    **get** _returns all menu items_ 
- [/menu/\<int:pk\>/](http://127.0.0.1:8000/menu/1/)    **get** _returns single menu item_ 
- [/booking/?date=YYYY-MM-DD](http://127.0.0.1:8000/booking/?date=2023-04-26)    **get** _returns all reservation by all users on given date_ 
- [/booking/](http://127.0.0.1:8000/booking/)    **post** _makes a reservation(called by user)_  __payload:__ _reservation_date, reservation_slot_ 
- [/menu/](http://127.0.0.1:8000/reservations/)    **get** _return all reservations made by user*s (for superuser)_ 

