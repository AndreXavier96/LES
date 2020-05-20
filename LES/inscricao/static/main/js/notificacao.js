function confirmacao_notificacao(id) {
    if (id === "confirmacao"){
    document.getElementById('popup_notificacao').style.display = ''
    }else if (id === "popup_cancel"){
        document.getElementById('popup_notificacao').style.display = 'none'
    }
}