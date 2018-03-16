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
                    hetalert.alertConfirm({
                        'msg':'恭喜用例添加成功！',
                        'cancelText':'回到首页',
                        'confirmText':'继续上传压缩文件！',
                        'cancelCallback':function () {
                            window.location = '/';
                        },
                        'confirmCallback':function () {
                            window.location = '/upload/';

                        }

                    });
                }else{
                    hetalert.alertInfo(data['message']);
                }

            }

        });
    });
});