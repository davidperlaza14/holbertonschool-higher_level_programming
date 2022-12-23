$.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data['results'], function (k, v) {
        let title = v['title'];
        $('UL#list_movies').append(`<li>${title}</li>`);
      });
    },
    dataType: 'json'
});