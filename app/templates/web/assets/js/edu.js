$(document).ready(function() {

//Thiết kế Website   
    $('#thiet_ke_website .course_list > div').click(function () {
        let idx = $(this).attr('rel');

        $('#thiet_ke_website .course_list > div').removeClass('addBorder');
        $(this).addClass('addBorder');
        
        $('#thiet_ke_website .course_subjects > div').removeClass('edu_active');
        $(`#thiet_ke_website .course_subjects > div:nth-child(${idx}`).addClass('edu_active');
    });

    $('#thiet_ke_website .course_subjects > div > div > div').click(function () {
        let idx = $(this).attr('rel');

        $('#thiet_ke_website .course_infomation > div').removeClass('edu_active');
        $(`#thiet_ke_website .course_infomation > div:nth-child(${idx}`).addClass('edu_active');
    });

//Lập trình di động
    $('#lap_trinh_di_dong .course_list > div').click(function () {
        let idx = $(this).attr('rel');

        $('#lap_trinh_di_dong .course_list > div').removeClass('addBorder');
        $(this).addClass('addBorder');
        
        $('#lap_trinh_di_dong .course_subjects > div').removeClass('edu_active');
        $(`#lap_trinh_di_dong .course_subjects > div:nth-child(${idx}`).addClass('edu_active');
    });

    $('#lap_trinh_di_dong .course_subjects > div > div > div').click(function () {
        let idx = $(this).attr('rel');

        $('#lap_trinh_di_dong .course_infomation > div').removeClass('edu_active');
        $(`#lap_trinh_di_dong .course_infomation > div:nth-child(${idx}`).addClass('edu_active');
    });

//Tin học văn phòng
    $('#tin_hoc_van_phong .course_list > div').click(function () {
        let idx = $(this).attr('rel');

        $('#tin_hoc_van_phong .course_list > div').removeClass('addBorder');
        $(this).addClass('addBorder');
        
        $('#tin_hoc_van_phong .course_subjects > div').removeClass('edu_active');
        $(`#tin_hoc_van_phong .course_subjects > div:nth-child(${idx}`).addClass('edu_active');
    });

    $('#tin_hoc_van_phong .course_subjects > div > div > div').click(function () {
        let idx = $(this).attr('rel');

        $('#tin_hoc_van_phong .course_infomation > div').removeClass('edu_active');
        $(`#tin_hoc_van_phong .course_infomation > div:nth-child(${idx}`).addClass('edu_active');
    });

//Tin học văn phòng MOS
    $('#tin_hoc_van_phong_mos .course_list > div').click(function () {
        let idx = $(this).attr('rel');

        $('#tin_hoc_van_phong_mos .course_list > div').removeClass('addBorder');
        $(this).addClass('addBorder');
        
        $('#tin_hoc_van_phong_mos .course_subjects > div').removeClass('edu_active');
        $(`#tin_hoc_van_phong_mos .course_subjects > div:nth-child(${idx}`).addClass('edu_active');
    });

    $('#tin_hoc_van_phong_mos .course_subjects > div > div > div').click(function () {
        let idx = $(this).attr('rel');

        $('#tin_hoc_van_phong_mos .course_infomation > div').removeClass('edu_active');
        $(`#tin_hoc_van_phong_mos .course_infomation > div:nth-child(${idx}`).addClass('edu_active');
    });

//Mạng máy tính
    $('#mang_may_tinh .course_list > div').click(function () {
        let idx = $(this).attr('rel');

        $('#mang_may_tinh .course_list > div').removeClass('addBorder');
        $(this).addClass('addBorder');
        
        $('#mang_may_tinh .course_subjects > div').removeClass('edu_active');
        $(`#mang_may_tinh .course_subjects > div:nth-child(${idx}`).addClass('edu_active');
    });

    $('#mang_may_tinh .course_subjects > div > div > div').click(function () {
        let idx = $(this).attr('rel');

        $('#mang_may_tinh .course_infomation > div').removeClass('edu_active');
        $(`#mang_may_tinh .course_infomation > div:nth-child(${idx}`).addClass('edu_active');
    });
});