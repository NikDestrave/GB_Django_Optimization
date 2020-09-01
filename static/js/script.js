var sum = 0,
    countItems = 0;

function init() { //Функция формирования товаров
    var button = document.getElementsByClassName("button_buy"),
        img = document.getElementsByClassName("product");
        button.onclick = clickFunction;
        img.onclick = clickImg;
}

function clickFunction(event) { //Функция формирования корзины и расчета стоимости
    var table = document.getElementById("shop_items"),
        tr = document.createElement('tr'),
        td = document.createElement('td'),
        id = event.target.id.split("_");
    if (shop_items[id[2]].count === 0) {
        table.appendChild(tr);
        td.textContent = ++countItems;
        tr.appendChild(td);

        td = document.createElement('td');
        td.textContent = shop_items[id[2]].name;
        tr.appendChild(td);

        td = document.createElement('td');
        td.id = "id_count_" + event.target.id;
        td.textContent = 1;
        tr.appendChild(td);

        td = document.createElement('td');
        td.textContent = shop_items[id[2]].cost;
        tr.appendChild(td);

        shop_items[id[2]].count++;
    }
    else {
        shop_items[id[2]].count++;
        var x = document.getElementById("id_count_" + event.target.id);
        x.innerText = shop_items[id[2]].count;
    }

    for (i=0; i<shop_items.length;i++) {
        sum += shop_items[i].count * shop_items[i].cost;
    }

    var y = document.getElementById('result');
    y.innerText = sum;
    sum = 0;
}

function clickImg(event) {
    var div = document.getElementById("big_img"),
        id = event.target.id.split("_");
    div.setAttribute("style", "text-align: center;");
    if (shop_items[id[2]].big_img == "") {
        div.textContent = "Фотографии не найдено!";
    } else {
        div.textContent = "";
        div.setAttribute("style", "background: url(" + shop_items[id[2]].big_img + ") no-repeat; height: 450px; background-size: contain; background-position:center;");
    }
}

window.onload = init;