$(document).ready(function () {
  const resp = 'https://hellosalut.stefanbohacek.dev/';
  $('INPUT#btn_translate').on('click', great());
  $('INPUT#language_code').on('keypress', function (key) {
    if (key.which === 13) {
      great();
    }
  });
  function great () {
    const language = $('INPUT#language_code').val();
    $.ajax({ resp, data: { language } }).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
