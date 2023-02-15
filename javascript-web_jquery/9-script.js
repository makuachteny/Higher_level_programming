$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const helloMessage = data.hello;
    $('div#hello').text(helloMessage);
  });
});
