$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var password_input1=$("input[name='password1']");
        var password_input2=$("input[name='password2']");

        var password1 = password_input1.val();
        var password2 = password_input2.val();

        hetajax.post({
            'url':'/updatepwd/',
            'data':{
                'password1':password1,
                'password2':password2
            },
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertInfoToast('修改密码成功！');
                    window.location = '/signin/';
                }else{
                    hetalert.alertInfo(data['message']);
                }

            }
        });
    });
});
