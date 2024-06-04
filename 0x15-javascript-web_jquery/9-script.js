const resp = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.ajax({ resp }).done(function (data) {
    $('DIV#hello').text(data.hello);
  });
});
