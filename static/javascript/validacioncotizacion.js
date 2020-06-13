function validar() {

nombre = document.getElementById("nomcli").value;

  if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
    alert('Tu nombre no puede estar vacio');
    return false;
  } else {
  	alert('Gracias por contactarte con nosotros')
  }

  return true;
}