(function () {
    let password = document.getElementById('id_password1');
    let passwordConfirm = document.getElementById('id_password2');
    let password_field = document.querySelectorAll('.password_field')

    password_field.forEach(item => {
        item.addEventListener('input', function() {
            if (password.value === passwordConfirm.value) {
                document.getElementById("signupBtn").disabled = false;
            } else {
                document.getElementById("signupBtn").disabled = true;
            }
        })
    })
} () );
