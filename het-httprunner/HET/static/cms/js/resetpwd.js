/**
 * Created by denger on 2018/2/2.   $();相当于是jquery();
 */
$ (function () {
    $('#submit').click(function (event) {
        //event.preventDefault是为了阻止按钮默认提交表单的事件
        event.preventDefault();
        var oldpwdE = $('input[name=oldpwd]');
        var newpwdE = $('input[name=newpwd]');
        var newpwd2E = $('input[name=newpwd2]');

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        hetajax.post({
            'url':'/cms/resetpwd/',
            'data':{
                'oldpwd':oldpwd,
                'newpwd':newpwd,
                'newpwd2':newpwd2
            },
            'success':function (data) {
                if(data['code']== 200) {
                    hetalert.alertSuccessToast('恭喜！密码修改成功！');
                    oldpwdE.val('');
                    newpwdE.val('');
                    newpwd2E.val('');
                }else{
                    var message = data['message'];
                    hetalert.alertInfo(message);
                }
                
            },
            'fail':function (error) {
                hetalert.alertNetworkError();
                
            }
        });


    });


});