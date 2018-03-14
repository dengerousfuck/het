/**
 * Created by denger on 2018/3/14.
 */
$(function () {
    $("#excute-btn").click(function (event) {
        event.preventDefault();
        var fd = new FormData($('form')[0]);

        hetajax.post({
            'url':'/excute/',
            'types':'POST',
            'processData':false,
            'contentType':false,
            'data':fd,
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertInfo('文件上传成功！');
                    window.location = '/';
                }else{
                    hetalert.alertInfo(data['message']);
                }

            }
        });
    });
});