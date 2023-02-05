last_user = 'Что-то'

function VvodName(){
    let name_user = prompt("Все таки нажал.\nИ как твое имя:", "имя")
    alert(name_user)
    Zamena(name_user)
}

function Zamena(name_user){
    document.body.innerHTML = document.body.innerHTML.replace(new RegExp(last_user, 'g'), name_user);
    last_user = name_user
}