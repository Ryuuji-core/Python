print('Hello World')
value = 2

if value == 1:
    print unicode("valueの値は2です")
elif value == 2:
    print unicode("valueの値は2です")
elif value == 3:
    print unicode("valueの値は3です")
else:
    print unicode("値はありません。");
#上のIF文の仕組みについて。
#ifで　valueの値をして・・・でも違う
#それでelifに処理を飛ばす  elifとはC言語やC++で言うelse ifです。
#今回は一致したのでOK
#それでもダメならelseに処理を飛ばす。elseでは値を指定しなくても処理される。
