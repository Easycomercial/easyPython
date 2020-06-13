function validacionpl(){

nombreclie = document.getElementById("nombreclie").value;
emailclie = document.getElementById("emailclie").value;
telefonoclie = document.getElementById("telefonoclie").value;
planclie = document.getElementById("planclie").value;
	
 if (nombreclie == null || nombreclie.length == 0 || /^\s+$/.test(nombreclie)) {
 	alert('campo vacio');
 	return false;
 }
 else if (emailclie== null || emailclie.length == 0 || /^\s+$/.test(emailclie)) {
 	alert('campo vacio');
 	return false;
 	}else{
 		alert('Gracias por contactarse')
 	}

   
 return true;
}

function validacion() {

nombre = document.getElementById("nombre").value;
correo = document.getElementById("correo").value;
telefono = document.getElementById("telefono").value;
dudas = document.getElementById("dudas").value;

  if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
    alert('campo vacio');
    return false;
  }
  else if (dudas == null || dudas.length == 0 || /^\s+$/.test(dudas)) {
    alert('campo vacio');
    return false;
  } else {
  	alert('Gracias por contactarse')
  }

  return true;
}
