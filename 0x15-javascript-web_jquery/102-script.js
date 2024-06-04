$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const language = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, (response) => {
      $('DIV#hello').text(response.hello);
    }, 'json');
  });
});
