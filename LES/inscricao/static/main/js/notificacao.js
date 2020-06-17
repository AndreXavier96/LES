function confirmacao_notificacao(id) {
    if (id === "confirmacao"){
    document.getElementById('popup_notificacao').style.display = ''
    }
    else if (id === "popup_cancel"){
        document.getElementById('popup_notificacao').style.display = 'none'
    }
}

function incremental(type, id) {
    let value = document.getElementById(id).getAttribute('value')
    if (type === 'add') {
        document.getElementById(id).stepUp(1)
    } else if (type === 'minus') {
        document.getElementById(id).stepDown(1)
    }
    document.getElementById(id).setAttribute('value', value)
}