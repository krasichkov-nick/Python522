"use strict";

/* let message; // let, const, var
message = "Hello";
console.log(message)

let a = 10
a = 3.5;

let b, c;
let d = 5, e = 2;

let firstName = "Irina";
console.log(firstName); */

// const week = 7;

/* let str = "Двойные кавычки";
let str2 = 'Одинарный кавычки';
let str3 = `Обратные ${5 + 2}
 кавычки`

console.log(str);
console.log(str2);
console.log(str3); */


/* let firstName = "Ivan";
alert(`"Hello, ${firstName}"`) */

/* let name1 = 365
let name2 = "Земля"
let name3 = "7 млрд"
let name4 = "Солнца"
alert(`Мы живем на планете ${name2}, она делает один оборот вокруг ${name4} за ${name1} дней. Население нашей планеты составляет примерно ${name3}. человек.`) */

/* let res = confirm("Знаете ли вы html?");
console.log(res);

if(res){alert("Пора учить ява скрипт")}
else {alert("Нужно выучить")} */

// Типы данных

/* let number = 13;
console.log(number, typeof number)
console.log(number, typeof(number))

let a = 23.56
console.log(a, typeof(a));

let b = "hello"
console.log(b, typeof(b));

let c = true
console.log(c, typeof(c));

let d = null
console.log(d, typeof(d))

let e = undefined;
console.log(e, typeof(e)); */

/* let res = prompt("Ваше имя:", "Значение по умолчанию");
console.log(res); */

/* let a = 12
let b = 8

console.log('+:', a + b);
console.log('-:', a - b);
console.log('*:', a * b);
console.log('/:', a / b);
console.log('%:', a % b);
console.log('**:', a ** b); */

/* let a = "23"
let b = "6a"
console.log(a - b) //NaN */

/* let a = +prompt("Введите первое число:", 5);
let b = +prompt("Введите второе число:", 3);
// a = parseInt(a);
// b = parseInt(b);
alert("Результат: " + (a + b)); */

/* console.log(parseInt("21.84"));
console.log(parseFloat("21.84"));
console.log(parseFloat("21.8454654").toFixed(2));
console.log(Number("21.84"));
console.log(+"21.84");
console.log(+true);
console.log(+false); */

/* let a = 0, b = 0;
a++;
b--;
console.log(a);
console.log(b); */

/* let a = 0, b = 0;
++a;
b++;

console.log(a);
console.log(b); */

/* let a = 0, b = 0;
let c = a++ + 2;
let d = ++b + 2;
console.log(a);
console.log(b);
console.log(c);
console.log(d); */

/* let a = 1;
let b = a++; //b=1, a=2
let c = b + 5 + a // c = 1 + 5 + 2
console.log(c) */

//a++ or a+=1 or a=a+1

// let a = 1;
// let b = ++a; //b=2, a=2
// let c = b + 5 + a // c = 2 + 5 + 2
// console.log(c) //9

/* let num = 10;

num += 5;
console.log(num);

num -= 7;
console.log(num); */

/* console.log(5>3);
console.log(5<3);
console.log(5<=3);
console.log(5>=3);
console.log(5=="5");
console.log(5==="5");
console.log(5!="5");
console.log(5!=="5"); */

// 7 > 3 ? alert("7"): alert("3");

/* let ch = prompt("Угадайте число от 1 до 10");
let num = 7;
(ch == num) ? alert("Угадали") : alert("Не угадали");
(ch == num) ? alert("Угадали") : (ch < num) ? alert("Загаданное число больше") : alert("Загаданное число меньше"); */

/* if (условие){
    блок истина
} else {
    блок ложь
} */

/* 
false => 0, 0.0, "", false, null, undefined, NaN
*/ 

/* a = 0;
if (a){
    console.log("TRUE")
} else {
    console.log("FALSE")
} */

/* let a = +prompt("Введите первое число:", 5);
let b = +prompt("Введите второе число:", 0);

if (b != 0)
    alert(a / b) //infinity
else
    alert("На ноль делить нельзя") */

// let a = 12;
// let b = 6;

/* if(a > b){
    alert(a + " > " + b);
}
if(a < b){
    alert(a + " < " + b)
}
if(a == b){
    alert(a + " == " + b)
} */

/* if(a > b){
    alert(a + " > " + b);
}
else if(a < b){
    alert(a + " < " + b)
}
else(a == b){
    alert(a + " == " + b)
} */

/* let login = prompt("Введите логин: ");
if(login){
    if(login == "admin"){
        let psw = prompt("Введите пароль: ")
        if(psw){
            if(psw == password){
                alert("Добро пожаловать")
            }
            else{
                alert("Пароль не верен")
            }
        } else{
            alert("Вход отменен")
        }
    } else
        alert("Я вас не знаю");
} else{
    alert("Вход отменен");
} */

/* if (5 == 5 && 5 > 2){
    console.log("TRUE")
} else {
    console.log("FALSE")
} */

/*     console.log(!9);
    console.log(!0);
    console.log(!!0);
    console.log(!!"hello");
    console.log(!!"");
     */

/*     let age = prompt("Введите возраст: ");
    if (age < 18 || age > 69){
        alert("Права не давать");
    } else {
        alert("Вы можете получать права");
    } */

/* switch (условие){
    case  значение_1:
        блок кода;
        break;
    case  значение_n:
        блок кода;
        break;
    default:
        блок кода
} */

/* let a = +prompt("Введите число: ")
switch(a){
    case 1:
        alert("Код 1");
        break;
    case 2:
        alert("Код 2");
        break;
    case 2:
        alert("Код 3");
        break;
    default:
        alert("Я таких значений не знаю");
} */

/* let a = +prompt("Введите результат '2 + 2': ")
switch(a){
    case 4:
        alert("Верно");
        break;
    case 3:
    case 5:
        alert("Не верно");
        break;
    default:
        alert("Я таких значений не знаю");
} */

/* let m = +prompt("Введите номер месяца: ");
let n;
switch(m){
    case 1: n="Январь"; break;
    case 2: n="Февраль"; break;
    case 3: n="Март"; break;
    case 4: n="Апрель"; break;
    case 5: n="Май"; break;
    case 6: n="Июнь"; break;
    case 7: n="Июль"; break;
    case 8: n="Август"; break;
    case 9: n="Сентябрь"; break;
    case 10: n="Октябрь"; break;
    case 11: n="Ноябрь"; break;
    case 12: n="Декабрь"; break;
    default: n="Неправильный номер месяца";
}
alert("Вы ввели: " + n); */

let a = +prompt("Введите стоимость покупки: ");
let n=0;
if (a >= 500 && a < 1000){n = 3};
if (a >= 1000){n = 5}
alert(`Стоимость покупки без скидки: ${a} руб\nСкидка: ${n}%\nИтоговая стоимость: ${(a * n / 100 + a)} руб`);
