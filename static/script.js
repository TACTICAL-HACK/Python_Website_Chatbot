let path = [];

function renderOptions(options) {
    const area = $('#chatArea');
    area.empty();
    options.forEach(option => {
        const btn = $('<button>').text(option);
        btn.click(() => {
            path.push(option);
            fetchOptions();
        });
        area.append(btn).append('<br>');
    });
}

function renderResponse(lines) {
    const area = $('#chatArea');
    area.empty();
    lines.forEach(line => {
        area.append(`<p>${line}</p>`);
    });
    area.append('<br><button onclick="restart()">Start Over</button>');
}

function fetchOptions() {
    $.post('/get_options', JSON.stringify({ path: path }), function(data) {
        if (data.type === 'options') {
            renderOptions(data.data);
        } else {
            renderResponse(data.data);
        }
    }, 'json');
}

function restart() {
    path = [];
    renderOptions(Object.keys(window.initialCategories));
}

$(document).ready(function() {
    $('#startBtn').click(() => {
        path = [];
        $.get('/get_root', function(data) {
            renderOptions(data);
        });
    });
});
