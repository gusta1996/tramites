const registromunicipal = (id) => {
    $.get(`/return_registro_municipal?id=${id}`, function (data) {
        let datos = JSON.parse(data)
        datos.map(dato => {
            console.log(dato)
            let pv=document.getElementById('primera_vez')
            if (dato.fields.primera_vez){
                pv.setAttribute('checked','cheked')
            }
            else{
                pv.removeAttribute('checked')
            }
            if (dato.fields.cedula) {
                $("#btn1").hide()
                $("#cedula").hide()
                $("#ck1").removeClass('text-danger fa fa-close')
                $("#ck1").addClass('fa fa-check')
                $("#ck1").addClass('text-primary')
                $("#ad1").attr('href', '/media/' + dato.fields.cedula)
                $("#ad1").show()
            } else {
                $("#btn1").show()
                $("#cedula").show()
                $("#ck1").addClass('text-danger fa fa-close')
                $("#ad1").hide()
                $("#enviar").hide()
            }
            if (dato.fields.votacion) {
                $("#btn2").hide()
                $("#votacion").hide()
                $("#ck2").removeClass('text-danger fa fa-close')
                $("#ck2").addClass('text-primary fa fa-check')
                $("#ad2").attr('href', '/media/' + dato.fields.votacion)
                $("#ad2").show()

            } else {
                $("#btn2").show()
                $("#votacion").show()
                $("#ck2").addClass('text-danger fa fa-close')
                $("#ad2").hide()
                $("#enviar").hide()
            }
            if (dato.fields.no_adeudar) {
                $("#btn3").hide()
                $("#no_adeudar").hide()
                $("#ck3").removeClass('text-danger fa fa-close')
                $("#ck3").addClass('text-primary fa fa-check')
                $("#ad3").attr('href', '/media/' + dato.fields.no_adeudar)
                $("#ad3").show()
            } else {
                $("#btn3").show()
                $("#no_adeudar").show()
                $("#ck3").addClass('text-danger fa fa-close')
                $("#ad3").hide()
                $("#enviar").hide()
            }
            if (dato.fields.no_adeudar_e) {
                $("#btn4").hide()
                $("#no_adeudar_e").hide()
                $("#ck4").removeClass('text-danger fa fa-close')
                $("#ck4").addClass('text-primary fa fa-check')
                $("#add4").attr('href', '/media/' + dato.fields.no_adeudar_e)
                $("#add4").show()
            } else {
                $("#btn4").show()
                $("#no_adeudar_e").show()
                $("#ck4").addClass('text-danger fa fa-close')
                $("#add4").hide()
                $("#enviar").hide()
            }
        })
    })
}