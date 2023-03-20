const registromunicipal = (id) => {
    $.get(`/return_registro_municipal?id=${id}`, function (data) {
        console.log(data)
        let datos = JSON.parse(data)
        console.log(datos.map(dato => {
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
            if (dato.fields.no_adeudar) {
                $("#btn2").hide()
                $("#no_adeudar").hide()
                $("#ck2").removeClass('text-danger fa fa-close')
                $("#ck2").addClass('text-primary fa fa-check')
                $("#ad2").attr('href', '/media/' + dato.fields.no_adeudar)
                $("#ad2").show()

            } else {
                $("#btn2").show()
                $("#no_adeudar").show()
                $("#ck2").addClass('text-danger fa fa-close')
                $("#ad2").hide()
                $("#enviar").hide()
            }
            if (dato.fields.no_adeudar_e) {
                $("#btn3").hide()
                $("#no_adeudar_e").hide()
                $("#ck3").removeClass('text-danger fa fa-close')
                $("#ck3").addClass('text-primary fa fa-check')
                $("#ad3").attr('href', '/media/' + dato.fields.no_adeudar_e)
                $("#ad3").show()
            } else {
                $("#btn3").show()
                $("#no_adeudar_e").show()
                $("#ck3").addClass('text-danger fa fa-close')
                $("#ad3").hide()
                $("#enviar").hide()
            }
        }))
    })
}