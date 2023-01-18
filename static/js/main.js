function initEditBookPage() {
    $('a.book-edit-form-link').click(function (event) {
        event.preventDefault();
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function (data, status, xhr) {
                // check if we got successful response from the server
                if (status != 'success') {
                    alert('Помилка на сервері. Спробуйте, будь ласка, пізніше.');
                    return false;
                }
                // update modal window with arrived content from the server
                var modal = $('#myModal'),
                    html = $(data), form = html.find('#content-column form');
                modal.find('.modal-body').html(form);
                // setup and show modal window finally
                modal.modal('show');
            },
            'error': function () {
                alert('Помилка на сервері. Спробуйте, будь ласка, пізніше.');
                return false;
            }
        });
        return false;
    });
}

// $(document).ready(function () {
//     initEditBookPage();
// });
