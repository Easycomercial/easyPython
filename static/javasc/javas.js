function click_de_boton(id){
            $('#tipo_de_plant').val(id)
            $('#Modal1').modal('show')
          }

function validacion(){

nombre = document.getElementById("nombre").value;
email = document.getElementById("email").value;
	
 if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
 	alert('campo vacio');
 	return false;
 }
 else if (email== null || email.length == 0 || /^\s+$/.test(email)) {
 	alert('campo vacio');
 	return false;

   }
 return true;
}