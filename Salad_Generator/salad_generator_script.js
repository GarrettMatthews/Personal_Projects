// Salad Generator
// Garrett Matthews


var sweet_list = ["Strawberries","Blueberries","Mangos","Raspberries","Cinnamon Almonds","Apple","Peaches","Grapes","Oranges"];
var savory_list = ["Chicken", "Bacon", "Cucumber", "Tomatos", "Corn", "Onion", "Carrots", "Heart of Palm"];
var dressing_list = ["Ranch","Italian", "Blackberry Balsamic", "Lemon Poppyseed", "Strawberry", "Mango", "Blueberry Basil", "Lemon and Salt", "BBQ Sauce"];

//Function to generate 3 random salads
function generateSalad(){
    sweet_item1 = sweet_list[Math.floor(Math.random()*sweet_list.length)];
    savory_item1 = savory_list[Math.floor(Math.random()*savory_list.length)];
    dressing_item1 = dressing_list[Math.floor(Math.random()*dressing_list.length)];
    sweet_item2 = sweet_list[Math.floor(Math.random()*sweet_list.length)];
    savory_item2 = savory_list[Math.floor(Math.random()*savory_list.length)];
    dressing_item2 = dressing_list[Math.floor(Math.random()*dressing_list.length)];
    sweet_item3 = sweet_list[Math.floor(Math.random()*sweet_list.length)];
    savory_item3 = savory_list[Math.floor(Math.random()*savory_list.length)];
    dressing_item3 = dressing_list[Math.floor(Math.random()*dressing_list.length)];
    sweet_item4 = sweet_list[Math.floor(Math.random()*sweet_list.length)];
    savory_item4 = savory_list[Math.floor(Math.random()*savory_list.length)];
    dressing_item4 = dressing_list[Math.floor(Math.random()*dressing_list.length)];
    sweet_item5 = sweet_list[Math.floor(Math.random()*sweet_list.length)];
    savory_item5 = savory_list[Math.floor(Math.random()*savory_list.length)];
    dressing_item5 = dressing_list[Math.floor(Math.random()*dressing_list.length)];
    html = "<tr><td class=\"blank\"></td><td class=\"sweet\">Sweet Item</td><td class=\"savory\">Savory Item</td><td class=\"dressing\">Dressing</td></tr>";
    html += "<tr><td class=\"saladNum1\">Salad 1</td><td class=\"grid1\">" + sweet_item1 + "</td><td class=\"grid2\">" + savory_item1 + "</td><td class=\"grid1\">" + dressing_item1 + "</td></tr>";
    html += "<tr><td class=\"saladNum2\">Salad 2</td><td class=\"grid2\">" + sweet_item2 + "</td><td class=\"grid1\">" + savory_item2 + "</td><td class=\"grid2\">" + dressing_item2 + "</td></tr>";
    html += "<tr><td class=\"saladNum1\">Salad 3</td><td class=\"grid1\">" + sweet_item3 + "</td><td class=\"grid2\">" + savory_item3 + "</td><td class=\"grid1\">" + dressing_item3 + "</td></tr>";
    html += "<tr><td class=\"saladNum2\">Salad 4</td><td class=\"grid2\">" + sweet_item4 + "</td><td class=\"grid1\">" + savory_item4 + "</td><td class=\"grid2\">" + dressing_item4 + "</td></tr>";
    html += "<tr><td class=\"saladNum1\">Salad 5</td><td class=\"grid1\">" + sweet_item5 + "</td><td class=\"grid2\">" + savory_item5 + "</td><td class=\"grid1\">" + dressing_item5 + "</td></tr>";
    var saladTable = document.getElementById("salad");
    saladTable.innerHTML = html;
}

function displaySalad(){
    var saladTable = document.getElementById("salad")
}

//Function to add items onto the end of the arrays
function addItems(form){
    if (form.elements["sweet"].value.length >= 1){
        sweet_list.push(form.elements["sweet"].value);
    }
    var savory = form.elements["savory"].value
    if (savory.length >= 1){
        savory_list.push(savory);
    }
    var dressing = form.elements["dressing"].value
    if (dressing.length >= 1){
        dressing_list.push(dressing);
    }
    form.reset();
}

function sweetList(){
    data = fs.readFile('sweet_list.txt', 'utf-8');
    sweet_list = Array.from(data);
}

function savoryList(){
    data = fs.readFile('savory_list.txt', 'utf-8');
    savory_list = Array.from(data);
}

function dressingList(){
    data = fs.readFile('dressing_list.txt', 'utf-8');
    dressing_list = Array.from(data);
}