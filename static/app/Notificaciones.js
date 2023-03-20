const notificacion = (mensaje, alerta) => {
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
    if(alerta =='success'){
        toastr.success(mensaje, "Notificación")
    }
    if(alerta =='error'){
        toastr.error(mensaje, "Notificación")
    }
    if(alerta =='info'){
        toastr.info(mensaje, "Notificación")
    }
}
