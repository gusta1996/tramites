const registromunicipal = (id) => {
    $.get(`/return_registro_municipal?id=${id}`, function (data) {
        console.log(data)
        let datos = JSON.parse(data)
        console.log(datos.map(dato => {
            if (dato.fields.no_adeudar) {
                $("#btnno_adeudar").hide()
                $("#no_adeudar").hide()
                $("#ck1").removeClass('text-danger fa fa-close')
                $("#ck1").addClass('text-primary fa fa-check')
                $("#ad1").attr('href', '/media/' + dato.fields.no_adeudar)
                $("#ad1").show()
            } else {
                $("#btnno_adeudar").show()
                $("#no_adeudar").show()
                $("#ck1").addClass('text-danger fa fa-close')
                $("#ad1").hide()
                $("#enviar").hide()
            }
            if (dato.fields.escritura) {
                $("#btnescritura").hide()
                $("#escritura").hide()
                $("#ck2").removeClass('text-danger fa fa-close')
                $("#ck2").addClass('text-primary fa fa-check')
                $("#ad2").attr('href', '/media/' + dato.fields.escritura)
                $("#ad2").show()
            } else {
                $("#btnescritura").show()
                $("#escritura").show()
                $("#ck2").addClass('text-danger fa fa-close')
                $("#ad2").hide()
                $("#enviar").hide()
            }
        }))
    })
}