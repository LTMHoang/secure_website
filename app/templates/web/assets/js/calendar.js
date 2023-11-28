function closeForm(obj) {
    let overplayClose = document.getElementsByClassName('cal_overplay')[0];
    let formSignupClose = document.getElementsByClassName('form_signup')[0];
    if(confirm('Bạn có chắc chắn muốn hủy đăng ký khóa học?') == true){
        overplayClose.classList.remove('cal_active');
        formSignupClose.classList.remove('cal_active');
    }
}

window.onload = function() {
    //Mở form
    let btnSub = document.querySelectorAll('.calendar_accept');
    let overplayOpen = document.querySelector('.cal_overplay');
    let formSignupOpen = document.querySelector('.form_signup');

    for(let o of btnSub) {
        o.addEventListener('click', function() {
            overplayOpen.classList.add('cal_active');
            formSignupOpen.classList.add('cal_active');
        })
    }

    //Đóng form
    let btnClose = document.querySelector('.cal_close');
    let btnOverlay = document.querySelector('.cal_overplay');

    btnClose.addEventListener('click', function() {
        closeForm(this);
    })

    btnOverlay.addEventListener('click', function() {
        closeForm(this);
    })
}

$(document).ready(function() {
    let name = document.getElementById('name');
    let dob = document.getElementById('dob');
    let email = document.getElementById('email');
    let phoneN = document.getElementById('phone_number');
    let address = document.getElementById('address');

    $('.form_signup > input').click(function() {
        if(name.value == "" || dob.value == "" || email.value == "" || phoneN.value == "" || address.value == ""){
            alert('Bạn chưa điền đầy đủ thông tin!!!');
        }

        else{
            alert('CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH VIỆC ĐĂNG KÝ KHÓA HỌC'
                    + '\n\n'
                    + 'Đây là mã khóa học ' + (Math.random()*100000).toFixed(0)
                    + '\n\n'
                    + 'HẸN GẶP LẠI BẠN SỚM NHẤT CÓ THỂ'
                );
            $('.cal_overplay, .form_signup').removeClass('cal_active');
        }
    })
});