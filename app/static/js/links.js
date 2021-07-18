function delete_link(id) {
    Swal.fire({
        title: 'Tem certeza?',
        text: "Quer deletar esse link?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sim, deletar!',
        cancelButtonText: 'Cancelar',
        background: '#303030',
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.showLoading();
            $.ajax({
                url: '/links/' + id,
                type: 'DELETE',
                success: () => {
                    Swal.fire({
                        title: 'Deletado',
                        text: 'Link deletado!',
                        icon: 'success',
                        background: '#303030',
                    }).then((result) => {
                        location.reload();
                    });
                },
                error: () => {
                    Swal.fire({
                        title: 'Algo deu errado :(',
                        text: 'Link não foi deletado!',
                        icon: 'error',
                        background: '#303030',
                    });
                }
            });
        }
    });
}

function share_link(id) {
    Swal.fire({
        title: 'Compartilhar link',
        html: '<p>Informe o nome do usuário</p><input required id="destinatario" />',
        background: '#303030',
        confirmButtonText: 'Enviar',
    }).then((result) => {
        if ($('#destinatario').val()) {
            Swal.showLoading();
            $.ajax({
                url: '/share/' + id,
                type: 'POST',
                data: {
                    'destinatario': $('#destinatario').val(),
                },
                success: (result) => {
                    Swal.fire({
                        title: 'Enviado',
                        text: result.messange,
                        icon: 'success',
                        background: '#303030',
                    })
                },
                error: (result) => {
                    console.log(result);
                    Swal.fire({
                        title: 'Algo deu errado :(',
                        text: result.responseJSON.messange,
                        icon: 'error',
                        background: '#303030',
                    });
                }
            });
        }
    });
}