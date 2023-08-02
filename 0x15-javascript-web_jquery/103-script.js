$(function() {
    function fetchTranslation() {
      const languageCode = $('#language_code').val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`;

      $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
          const translation = data.hello;
          $('#hello').text(translation);
        },
        error: function() {
          $('#hello').text('Translation not available.');
        }
      });
    }

    $('#btn_translate').on('click', fetchTranslation);

    $('#language_code').on('keypress', function(event) {
      if (event.which === 13) {
        fetchTranslation();
     }
   });
});
