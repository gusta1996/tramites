const limpiar = (select) => {
    for (let i = select.options.length; i >= 0; i--) {
        select.remove(i);
    }
};