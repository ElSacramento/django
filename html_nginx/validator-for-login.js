var login = document.getElementById("login"), login_password = document.getElementById("login_password"), form = document.getElementById("formLogIn");

function validateLogIn(){
	if(login.value == "admin") {
		formLogIn.setCustomValidity("Login or password is wrong");
	} else {
		formLogIn.setCustomValidity('');
	}
}

login.onchange = validateLogIn;
login_password.onchange = validateLogIn;