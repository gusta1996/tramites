const registromunicipal = (id) => {
    $.get(`/return_registro_municipal?id=${id}`, function (data) {
        let datos = JSON.parse(data)
        datos.map(dato => {
            console.log(dato)
            if (parseFloat(dato.fields.x.replace(",","."))>0) {
                $("#ck6").removeClass('text-danger fa fa-close')
                $("#ck6").addClass('text-primary fa fa-check')
            }
            else{
                $("#ck6").addClass('text-danger fa fa-close')
                 $("#enviar").hide()
            }
            if (dato.fields.direccion_local) {
                $("#ck7").removeClass('text-danger fa fa-close')
                $("#ck7").addClass('text-primary fa fa-check')
            }
            else{
                $("#ck7").addClass('text-danger fa fa-close')
                 $("#enviar").hide()
            }
            if (parseFloat(dato.fields.y.replace(",","."))>0) {
                $("#ck6").removeClass('text-danger fa fa-close')
                $("#ck6").addClass('text-primary fa fa-check')
            }
            else{
                $("#ck6").addClass('text-danger fa fa-close')
                 $("#enviar").hide()
            }
            $("#x").val(dato.fields.x)
            $("#y").val(dato.fields.y)
            $("#direccion").val(dato.fields.direccion_local)
            $("#local").val(dato.fields.nombre_negocio)
            console.log(dato.fields.estado===true)
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
            if (dato.fields.ruc) {
                $("#btnruc").hide()
                $("#ruc").hide()
                $("#ck4").removeClass('text-danger fa fa-close')
                $("#ck4").addClass('text-primary fa fa-check')
                $("#add4").attr('href', '/media/' + dato.fields.ruc)
                $("#add4").show()
            } else {
                $("#btnruc").show()
                $("#ruc").show()
                $("#ck4").addClass('text-danger fa fa-close')
                $("#add4").hide()
                $("#enviar").hide()
            }
            if (dato.fields.disenio) {
                $("#btndisenio").hide()
                $("#disenio").hide()
                $("#ck8").removeClass('text-danger fa fa-close')
                $("#ck8").addClass('text-primary fa fa-check')
                $("#ad8").attr('href', '/media/' + dato.fields.disenio)
                $("#ad8").show()
            } else {
                $("#btndisenio").show()
                $("#disenio").show()
                $("#ck8").addClass('text-danger fa fa-close')
                $("#ad8").hide()
                $("#enviar").hide()
            }


            if (dato.fields.nombre_negocio) {
                $("#ck5").removeClass('text-danger fa fa-close')
                $("#ck5").addClass('text-primary fa fa-check')
                $("#ad5").attr('href', '/media/' + dato.fields.nombre_negocio)
                $("#ad5").show()

            } else {
                $("#ck5").addClass('text-danger fa fa-close')
                $("#enviar").hide()
            }

            if(dato.fields.estado===true){
                console.log('en revision')
                let x=document.getElementById('x')
                let y= document.getElementById('y')
                let direccion=document.getElementById('direccion')
                let local= document.getElementById('local')
                x.setAttribute('readonly','readonly')
                y.setAttribute('readonly','readonly')
                direccion.setAttribute('readonly','readonly')
                local.setAttribute('readonly','readonly')

            }

        })
    })
}