$(document).ready(function() {
    
//Để làm scrollTop

    $(window).scroll(function() {
        if($(this).scrollTop() > 100){
            $('#back-home').fadeIn();
        } else{
            $('#back-home').fadeOut();
        }
    });


    $('#back-home').click(function() {
        $('html, body').animate( {
            scrollTop: 0
        }, 1000);
    });

//Làm hỗ trợ nhanh
    $('#quickIcon').click(function() {
        $('#quickIcon').hide('slow');

        $('#quickMess').css('transform', 'translateY(0)');
        $('#quickMess').css('transition', 'transform 0.7s linear');
    });   
    
    $('#quickClose').click(function() {
        $('#quickIcon').show('slow');

        $('#quickMess').css('transform', 'translateY(100%)');
        $('#quickMess').css('transition', 'transform 0.7s linear');
    });
});