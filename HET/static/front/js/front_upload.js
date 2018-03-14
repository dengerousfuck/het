$(function () {
    $("#upload").click(function (event) {
        event.preventDefault();
        var fd = new FormData($('form')[0]);

        hetajax.post({
            'url':'/upload/',
            'types':'POST',
            'processData':false,
            'contentType':false,
            'data':fd,
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertInfoToast('文件上传成功！');
                    window.location.reload();
                }else{
                    hetalert.alertInfo(data['message']);
                }

            }
        });
    });
});
