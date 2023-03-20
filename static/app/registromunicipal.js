const registromunicipal = (id) => {
    $.get(`/return_registro_municipal?id=${id}`, function (data) {
        console.log(data)
        let datos = JSON.parse(data)
        console.log(datos.map(dato => {
            if (dato.fields.cedula) {
                $("#btncedula").hide()
                $("#cedula").hide()
                $("#ck1").removeClass('text-danger fa fa-close')
                $("#ck1").addClass('fa fa-check')
                $("#ck1").addClass('text-primary')
                $("#ad1").attr('href', '/media/' + dato.fields.cedula)
                $("#ad1").show()
            } else {
                $("#btncedula").show()
                $("#cedula").show()
                $("#ck1").addClass('text-danger fa fa-close')
                $("#ad1").hide()
                $("#enviar").hide()
            }
            if (dato.fields.votacion) {
                $("#btnvotacion").hide()
                $("#votacion").hide()
                $("#ck2").removeClass('text-danger fa fa-close')
                $("#ck2").addClass('text-primary fa fa-check')
                $("#ad2").attr('href', '/media/' + dato.fields.votacion)
                $("#ad2").show()

            } else {
                $("#btnvotacion").show()
                $("#votacion").show()
                $("#ck2").addClass('text-danger fa fa-close')
                $("#ad2").hide()
                $("#enviar").hide()
            }
            if (dato.fields.no_adeudar) {
                $("#btnno_adeudar").hide()
                $("#no_adeudar").hide()
                $("#ck3").removeClass('text-danger fa fa-close')
                $("#ck3").addClass('text-primary fa fa-check')
                $("#ad3").attr('href', '/media/' + dato.fields.no_adeudar)
                $("#ad3").show()
            } else {
                $("#btnno_adeudar").show()
                $("#no_adeudar").show()
                $("#ck3").addClass('text-danger fa fa-close')
                $("#ad3").hide()
                $("#enviar").hide()
            }
            if (dato.fields.senescyt) {
                $("#btnsenescyt").hide()
                $("#senescyt").hide()
                $("#ck4").removeClass('text-danger fa fa-close')
                $("#ck4").addClass('text-primary fa fa-check')
                $("#add4").attr('href', '/media/' + dato.fields.senescyt)
                $("#add4").show()
            } else {
                $("#btnsenescyt").show()
                $("#senescyt").show()
                $("#ck4").addClass('text-danger fa fa-close')
                $("#add4").hide()
                $("#enviar").hide()
            }
            if (dato.fields.titulo) {
                $("#btntitulo").hide()
                $("#titulo").hide()
                $("#ck5").removeClass('text-danger fa fa-close')
                $("#ck5").addClass('text-primary fa fa-check')
                $("#ad5").attr('href', '/media/' + dato.fields.titulo)
                $("#ad5").show()

            } else {
                $("#btntitulo").show()
                $("#titulo").show()
                $("#ck5").addClass('text-danger fa fa-close')
                $("#ad5").hide()
                $("#enviar").hide()
            }

            if (dato.fields.registro_profesional) {
                $("#btn6").hide()
                $("#ck6").removeClass('text-danger fa fa-close')
                $("#ck6").addClass('text-primary fa fa-check')
                $("#n_senescyt").val(dato.fields.registro_profesional)
                $("#n_senescyt").attr('readonly','readonly')

            } else {
                $("#btn6").show()
                $("#ck6").addClass('text-danger fa fa-close')
                $("#ad6").hide()
                $("#enviar").hide()
            }
            if (dato.fields.profesion) {
                $("#btn7").hide()
                $("#ck7").removeClass('text-danger fa fa-close')
                $("#ck7").addClass('text-primary fa fa-check')
                $("#profesion").val(dato.fields.profesion)
                $("#profesion").attr('readonly','readonly')

            } else {
                $("#btn7").show()
                $("#ck7").addClass('text-danger fa fa-close')
                $("#ad7").hide()
                $("#enviar").hide()
            }

        }))
    })
}