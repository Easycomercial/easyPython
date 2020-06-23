function validar() {

nombre = document.getElementById("nomcli").value;
fono = document.getElementById("telefonocli").value;

  if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
    alert('Tu nombre no puede estar vacio');
    return false;
  } else if (fono == null || fono.length == 0 || !/^([0-9])*$/.test(fono)) {
  	alert('Es obligatorio usar solo numeros');
  	return false;
  } else {
  	alert('Gracias por contactarte con nosotros')
  }

  return true;
}