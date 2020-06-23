function validacion() {

nombre = document.getElementById("nombre").value;
dudas = document.getElementById("dudas").value;
fono = document.getElementById("telefono").value;

  if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
    alert('Tu nombre no puede estar vacio');
    return false;
  }
  else if (dudas == null || dudas.length == 0 || /^\s+$/.test(dudas)) {
    alert('Tus dudas no pueden estar vacios');
    return false;
  } else if (fono == null || fono.length == 0 || !/^([0-9])*$/.test(fono)) {
    alert('Es obligatorio usar solo numeros');
    return false;

  } else {
  	alert('Gracias por contactarte con nosotros')
  }

  return true;
}
