const llenarCombo = (uri, selectDestino) => {
    $.get(uri, function (data) {
        let o = JSON.parse(data);
        console.log(o)
        o.map(element => {
            console.log(element.pk, element.fields.nombre)
            let opcion = document.createElement('option');
            opcion.value = element.pk;
            opcion.text = element.fields.nombre.toUpperCase();
            selectDestino.appendChild(opcion);
        })
    })
}


const selectElement = (id, valueToSelect) => {
    let element = document.getElementById(id);
    element.setAttribute("disabled", "disabled");
    setTimeout(function () {
        element.value = valueToSelect;
        element.removeAttribute("disabled");
    }, 1000)
}
