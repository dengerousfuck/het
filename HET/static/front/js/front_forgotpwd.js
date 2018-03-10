
$(function () {
    $("#sms-captcha-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var telephone = $("input[name='telephone']").val();
        if (!(/^1[354879]\d{9}$/.test(telephone))){
            hetalert.alertInfoToast('请输入正确的手机号码');
            return;
        }
        var timestamp = (new Date).getTime();
        var sign = md5(timestamp+telephone+"fdsafdsafd432432");
        hetajax.post({
            'url':'/c/sms_captcha/',
            'data':{
                'telephone':telephone,
                'timestamp':timestamp,
                'sign':sign
            },
            'success':function (data) {
                if (data['code']==200){
                    hetalert.alertSuccessToast('短信验证码发送成功！');
                    self.attr("disabled","disabled");
                    var timeCount = 60;
                    var timer = setInterval(function () {
                        timeCount--;
                        self.text(timeCount);
                        if(timeCount<=0){
                            self.removeAttr('disabled');
                            clearInterval(timer);
                            self.text('发送验证码');
                        }
                    },1000);
                }else {
                    hetalert.alertInfoToast(data['message']);
                }

            }

        });

    });
});



$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var telephone_input = $("input[name='telephone']");
        var sms_captcha_input = $("input[name='sms_captcha']");

        var telephone = telephone_input.val();
        var sms_captcha = sms_captcha_input.val();

        hetajax.post({
            'url':'/forgotpwd/',
            'data':{
                'telephone':telephone,
                'sms_captcha':sms_captcha
            },
            'success':function (data) {
                if(data['code'] == 200){
                    window.location = '/updatepwd/';

                }else{
                    hetalert.alertInfo(data['message']);
                }
            },
            'fail':function () {
                hetalert.alertNetworkError();
            }
        });

    });
});

