
jQuery.noConflict();
jQuery(function ($) {
    $("#id_cpf").mask("999.999.999-99");
    $("#id_cep").mask("99999-999");
    $("#id_telefone").mask("99-9999-9999");
    $("#id_celular").mask("99-99999-9999");
    $("#id_cep").focusout(function () {
        cep = $(this).val().replace(/\D/g, '');
        if (cep != "") {
            var validacep = /^[0-9]{8}$/;
            if (validacep.test(cep)) {
                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
                    if (!("erro" in dados)) {
                        $('#id_endereco').val(dados.logradouro);
                        $('#id_bairro').val(dados.bairro);
                        $('#id_cidade').val(dados.localidade);
                        $('#id_uf').val(dados.uf);

                        $("#id_endereco").attr({"readonly":"True"});
                        $("#id_bairro").attr({"readonly":"True"});
                        $("#id_cidade").attr({"readonly":"True"});
                        $("#id_uf").attr({"readonly":"True"});
                    }
                    else{
                        $("#id_endereco").removeAttr("readonly");
                        $("#id_bairro").removeAttr("readonly");
                        $("#id_cidade").removeAttr("readonly");
                        $("#id_uf").removeAttr("readonly");
                    }
                });
            }
        }
    });
});
