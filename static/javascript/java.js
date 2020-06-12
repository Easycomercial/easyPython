function validacion() {

nombre = document.getElementById("nombre").value;
correo = document.getElementById("correo").value;
telefono = document.getElementById("telefono").value;
dudas = document.getElementById("dudas").value;

  if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
    alert('Tu nombre no puede estar vacio');
    return false;
  }
  else if (dudas == null || dudas.length == 0 || /^\s+$/.test(dudas)) {
    alert('Tus dudas no pueden estar vacios');
    return false;
  } else {
  	alert('Gracias por contactarte con nosotros')
  }

  return true;
}
