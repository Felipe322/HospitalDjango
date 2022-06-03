$("#id_estado").change(function(e) {
    var token = $('[name="csrfmiddlewaretoken"]').val();
    var url = '/pacientes/busca-municipio/';
    $.ajax({
           type: "POST",
           url: url,
           data: {'id':this.value,'csrfmiddlewaretoken':token},
           success: function(data)
           {
                var html='';
                $.each(data, function(llave,valor){
                    html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                });
                $('#id_municipio').html(html);
           },
           error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
          }
      });
  }); 
  