$(document).ready(function(){
    $('.file-upload').change(function() {
        var file = $(this)[0].files[0].name;
        $(this).next('p').text(file);
        console.log(file);
    });
});