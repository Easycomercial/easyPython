function click_de_boton(id){
            $('#Modal1').modal('show')
    var input = document.getElementById("plan");
    if(id==1){
    input.value = "Contabilidad";
    }else if(id==2){
    input.value = "RRHH";
    }else if(id==3){
    input.value = "Contabilidad+RRHH";
    }else if(id==4){
    input.value = "ERP+FE";
 }
 }
