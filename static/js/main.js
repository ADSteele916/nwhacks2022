$(document).ready(function(){
    $('.file-upload').change(function() {
        var file = $(this)[0].files[0].name;
        $(this).next('p').text(file);
        pre_child = $(this).siblings('pre');
        var fileReader = new FileReader();
        fileReader.onload = function(fileLoadedEvent){
            var textFromFileLoaded = fileLoadedEvent.target.result;
            pre_child.text(textFromFileLoaded);
        };

        fileReader.readAsText($(this)[0].files[0], "UTF-8");
    });
});