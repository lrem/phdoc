$(document).ready(function() {
    $('.fold').each(function(index, fd) {
        $(fd).before('<a class="toggle" href="#">Show/Hide</a>');
        $(fd).hide();
    });
    $('a.toggle').click(function(ev) {
        $(ev.target).next().toggle('fold', {}, 300);
        ev.preventDefault();
    });
});
