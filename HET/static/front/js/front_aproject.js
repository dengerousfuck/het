/**
 * Created by denger on 2018/2/27.
 */
$(function () {
    $("#save-project-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#project-dialog");
        var app_idInput = $("input[name='app_id']");
        var nameInput = $("input[name='name']");
        var interface_nameInput = $("input[name='interface_name']");
        var interface_urlInput = $("input[name='interface_url']");
        var parameter_keyInput = $("input[name='parameter_key']");
        var parameter_valueInput = $("input[name='parameter_value']");
        var typedInput = $("input[name='typed']");
        var methodInput = $("input[name='method']");
        var expected_codeInput = $("input[name='expected_code']");
        var signInput = $("input[name='sign']");
        var domainInput = $("input[name='domain']");
        var have_headersInput = $("input[name='have_headers']");

        var app_id = app_idInput.val();
        var name = nameInput.val();
        var interface_name = interface_nameInput.val();
        var interface_url = interface_urlInput.val();
        var parameter_key = parameter_keyInput.val();
        var parameter_value = parameter_valueInput.val();
        var typed = typedInput.val();
        var method = methodInput.val();
        var sign = signInput.val();
        var domain = domainInput.val();
        var expected_code = expected_codeInput.val();
        var have_headers = have_headersInput.val();

        // var submitType = self.attr('data-type');
        // var projectId = self.attr('data-id');

        if(!name || !app_id || !interface_name || !interface_url
        || !parameter_key || !parameter_value || !typed || !method
         || !sign || !domain || !expected_code || !have_headers){
            hetalert.alertInfoToast('请输入完整的项目接口信息！');
            return;
        }
        var url = '/aproject/';
        // var url = '';
        //
        // if(submitType == 'update'){
        //     url = '/cms/ubanner/';
        // }else {
        //     url = '/cms/abanner/';
        // }
        hetajax.post({
            'url':url,
            'data':{
                'name':name,
                'app_id':app_id,
                'interface_name':interface_name,
                'interface_url':interface_url,
                'parameter_key':parameter_key,
                'parameter_value':parameter_value,
                'typed':typed,
                'method':method,
                'sign':sign,
                'domain':domain,
                'expected_code':expected_code,
                'have_headers':have_headers
            },
            'success':function (data) {
                dialog.modal("hide");
                if(data['code']==200){
                    //重新加载当前页面
                    hetalert.alertInfoToast('接口录入成功！')
                    window.location.reload();
                }else{
                    hetalert.alertInfo(data['message']);
                }
            },
            'fail':function () {
                hetalert.alertNetworkError();

            }

        });

    })
});