/**
 *
 *
 * Created by denger on 2018/2/4.
 */

$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name='email']").val();
        if (!email){
            hetalert.alertInfoToast('请输入邮箱');
            return;
        }
        hetajax.get({
            'url':'/cms/email_captcha/',
            'data':{
                'email':email
            },
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertSuccessToast('邮件发送成功，请注意查收!');
                }else{
                    hetalert.alertInfo(data['message']);
                }
                
            },
            'fail':function (error) {
                hetajax.alertNetworkError();
                
            }
        });
        
    });
    
});


$(function () {
    $("#submit").click(function(event) {
        event.preventDefault();
        var emailE = $("input[name='email']");
        var captchaE = $("input[name='captcha']");

        var email = emailE.val();
        var captcha = captchaE.val();

        hetajax.post({
            'url':'/cms/resetemail/',
            'data':{
                'email':email,
                'captcha':captcha
            },
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertSuccessToast('恭喜！邮箱修改成功！');
                }else{
                    hetalert.alertInfo(data['message']);
                }

                
            },
            'fail':function (error) {
                hetalert.alertNetworkError();
                
            }
        });
        
    });
    
});