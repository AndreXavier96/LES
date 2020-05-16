$(function () {
    $("#table_atividades").tablesorter();
});
$(function () {
    $('.tablesorter-childRow td').hide();

    $(".tablesorter")
        .tablesorter({
            theme: 'blue',
            cssChildRow: "tablesorter-childRow"
        })

    $('.tablesorter').delegate('.toggle', 'click', function () {
        $(this).closest('tr').nextUntil('tr:not(.tablesorter-childRow)').find('td').toggle();
        return false;
    });
});

function expandAtividade(id) {
    let icon = document.getElementById('icon_' + id)
    if (icon.classList.contains('is-expanded')) {
        icon.classList.remove('is-expanded')
    } else {
        icon.classList.add('is-expanded')
    }
}

function deleteInscricao(val) {
    let x = document.getElementById(val).className
    if (x === "Grupo")
        document.getElementById('content_delete_inscricao').innerHTML = '<p>Tem a certeza que pretende apagar a inscrição Grupo' + val + ' no Dia Aberto?</p>'
    else if (x === "Individual")
        document.getElementById('content_delete_inscricao').innerHTML = '<p>Tem a certeza que pretende apagar a inscrição Individual' + val + ' no Dia Aberto?</p>'
    document.getElementById('del').value = val
    document.getElementById('type').value = 1
    document.getElementById('popup_eliminar_inscricao').style.display = ''
}

function deleteSessao(val, name) {
    console.log(val)
    console.log(name)
    document.getElementById('content_delete_sessao').innerHTML = '<p>Tem a certeza que pretende apagar a inscrição na sessão ' + name + ' no Dia Aberto?</p>'
    document.getElementById('del2').value = val
    document.getElementById('type').value = 2
    document.getElementById('popup_eliminar_sessao').style.display = ''
}


function canceldelete(id) {
    document.getElementById(id).style.display = 'none'
    document.getElementById('type').value = 0
}