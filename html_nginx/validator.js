function InvalidMsg(textbox) {
	if(textbox.validity.patternMismatch){
		textbox.setCustomValidity('Please enter 5 characters. Also the login must start with a letter');
	}       
	else {
		textbox.setCustomValidity('');
	}
	return true;
}
function InvalidMsgEmail(textbox) {
	if(textbox.validity.patternMismatch){
		textbox.setCustomValidity('This email is invalid');
	}       
	else {
		textbox.setCustomValidity('');
	}
	return true;
}

var password = document.getElementById("password"), confirm_password = document.getElementById("confirm_password");

function validatePassword(){
	if(password.value != confirm_password.value) {
		confirm_password.setCustomValidity("Passwords Don't Match");
	} else {
		confirm_password.setCustomValidity('');
	}
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
