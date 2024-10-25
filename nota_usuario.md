# CUANDO TRABAJAMOS CON MULTIPLES USUARIO

Siempre trata de revisar la configuracion con el siguiente comando:

$ git config -l

Aqui verificamos que era necesario el cambio de :
Ejemplo:

* url=https://MichaelDrogalis@github.com/derekerdmann/lunch_call.git

to:

* url=ssh://git@github.com/derekerdmann/lunch_call.git

Esto se puede cambiar con:


git remote set-url origin ssh://git@github.com/sebastianVP/git_22102024_test.git
