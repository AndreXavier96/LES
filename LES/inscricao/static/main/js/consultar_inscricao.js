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

function editarsessaoinscrita(id, tipo, numero_alunos, name) {
    let inscritos = document.getElementById('inscritos' + id)
    let novosinscritos = document.getElementById('novosinscritos' + id)
    let input_id = document.getElementById('inputinscritos' + id)
    let butao = document.getElementById('butao' + id)
    console.log(numero_alunos)
    if (tipo === 'editar') {
        inscritos.style.display = 'none'
        novosinscritos.style.display = ''
        input_id.style.display = ''
        input_id.value = numero_alunos
        butao.style.display = ''
        document.getElementById('type').value = 3
    } else if (tipo === 'concluir') {
        document.getElementById('popup_editar').value = id
        document.getElementById('edit').value = id
        document.getElementById('popup_editar_sessao').style.display = ''
        document.getElementById('content_editar_sessao').innerHTML = '<p>Tem a certeza que pretende alterar o numero de inscritos em ' + name + ' de ' + numero_alunos + ' para ' + input_id.value + ' ?</p>'
    } else if (tipo === 'change') {

    } else if (tipo === 'cancel') {
        document.getElementById('inscritos' + numero_alunos).style.display = ''
        document.getElementById('novosinscritos' + numero_alunos).style.display = 'none'
        document.getElementById('inputinscritos' + numero_alunos).style.display = 'none'
        document.getElementById('butao' + numero_alunos).style.display = 'none'
        document.getElementById(id).style.display = 'none'
        document.getElementById('type').value = 0
    }
}