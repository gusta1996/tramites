const registromunicipal = (id) => {
    $.get(`/return_registro_municipal?id=${id}`, function (data) {
        console.log(data)
        let datos = JSON.parse(data)
        console.log(datos.map(dato => {
            if (dato.fields.no_adeudar) {
                $("#btn1").hide()
                $("#no_adeudar").hide()
                $("#ck1").removeClass('text-danger fa fa-close')
                $("#ck1").addClass('text-primary fa fa-check')
                $("#ad1").attr('href', '/media/' + dato.fields.no_adeudar)
                $("#ad1").show()
            } else {
                $("#btn1").show()
                $("#no_adeudar").show()
                $("#ck1").addClass('text-danger fa fa-close')
                $("#ad1").hide()
                $("#enviar").hide()
            }
            if (dato.fields.cedula) {
                $("#btn2").hide()
                $("#cedula").hide()
                $("#ck2").removeClass('text-danger fa fa-close')
                $("#ck2").addClass('text-primary fa fa-check')
                $("#ad2").attr('href', '/media/' + dato.fields.cedula)
                $("#ad2").show()
            } else {
                $("#btn2").show()
                $("#cedula").show()
                $("#ck2").addClass('text-danger fa fa-close')
                $("#ad2").hide()
                $("#enviar").hide()
            }
            if (dato.fields.votacion) {
                $("#btn3").hide()
                $("#votacion").hide()
                $("#ck3").removeClass('text-danger fa fa-close')
                $("#ck3").addClass('text-primary fa fa-check')
                $("#ad3").attr('href', '/media/' + dato.fields.votacion)
                $("#ad3").show()
            } else {
                $("#btn3").show()
                $("#votacion").show()
                $("#ck3").addClass('text-danger fa fa-close')
                $("#ad3").hide()
                $("#enviar").hide()
            }
            if (dato.fields.declaracion_juramentada) {
                $("#btn4").hide()
                $("#declaracion_juramentada").hide()
                $("#ck4").removeClass('text-danger fa fa-close')
                $("#ck4").addClass('text-primary fa fa-check')
                $("#add4").attr('href', '/media/' + dato.fields.declaracion_juramentada)
                $("#add4").show()
            } else {
                $("#btn4").show()
                $("#declaracion_juramentada").show()
                $("#ck4").addClass('text-danger fa fa-close')
                $("#add4").hide()
                $("#enviar").hide()
            }
            if (dato.fields.planos) {
                $("#btn5").hide()
                $("#planos").hide()
                $("#ck5").removeClass('text-danger fa fa-close')
                $("#ck5").addClass('text-primary fa fa-check')
                $("#ad5").attr('href', '/media/' + dato.fields.planos)
                $("#ad5").show()
            } else {
                $("#btn5").show()
                $("#declaracion_juramentada").show()
                $("#ck5").addClass('text-danger fa fa-close')
                $("#ad5").hide()
                $("#enviar").hide()
            }
        }))
    })
}