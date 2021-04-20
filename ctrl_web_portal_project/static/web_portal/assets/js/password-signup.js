(function () {
    var password = document.getElementById('id_password1');
    var passwordConfirm = document.getElementById('id_password2');

    passwordConfirm.addEventListener('input', function() {
        if (password.value === passwordConfirm.value) {
            document.getElementById("signupBtn").disabled = false;
        } else {
            document.getElementById("signupBtn").disabled = true;
        }
    })
} () );
