$(document).ready(function() {

//Để làm slider teacher mobile
    let headT = $('.teacher_slider-inner a:first-child');
    let tailT = $('.teacher_slider-inner a:last-child');

    $('.teacher_next').on('click', function () {

        let current = $('.teacher_active');
        let next = current.next();

        if(current.attr('rel') == tailT.attr('rel'))
            next = headT;

        current.removeClass('teacher_active');
        next.addClass('teacher_active').css('animation', 'sliderLtR 1.5s 1');;
    });

    $('.teacher_prev').on('click', function () {

        let current = $('.teacher_active');
        let prev = current.prev();

        if(current.attr('rel') == headT.attr('rel'))
            prev = tailT;

        current.removeClass('teacher_active');
        prev.addClass('teacher_active').css('animation', 'sliderRtL 1.5s 1');;
    });
    

//Để làm slider comment
    let head = $('.slider-inner a:first-child');
    let tail = $('.slider-inner a:last-child');

    $('.next').on('click', function () {

        let current = $('.active');
        let next = current.next();

        if(current.attr('rel') == tail.attr('rel'))
            next = head;

        current.removeClass('active');
        next.addClass('active').css('animation', 'sliderLtR 1.5s 1');;
    });

    $('.prev').on('click', function () {

        let current = $('.active');
        let prev = current.prev();

        if(current.attr('rel') == head.attr('rel'))
            prev = tail;

        current.removeClass('active');
        prev.addClass('active').css('animation', 'sliderRtL 1.5s 1');;
    });




//Làm slider tự động
    setInterval(function () {

        let current = $('.active');
        let next = current.next();


        if(current.attr('rel') == tail.attr('rel'))
            next = head;

        current.removeClass('active');
        next.addClass('active').css('animation', 'sliderLtR 1.5s 1');

    }, 5000);   
    
    setInterval(function () {

        let currentT = $('.teacher_active');
        let nextT = currentT.next();


        if(currentT.attr('rel') == tailT.attr('rel'))
            nextT = headT;

        currentT.removeClass('teacher_active');
        nextT.addClass('teacher_active').css('animation', 'sliderLtR 1.5s 1');

    }, 5000);   
})