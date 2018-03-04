/**
 * Created by denger on 2018/2/23.
 */
$(function () {
    var ue = UE.getEditor("editor",{
        "serverUrl":'/ueditor/upload/'
    });
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var titleInput = $("input[name='title']");
        var boardSelect = $("select[name='board_id']");

        var title = titleInput.val();
        var board_id = boardSelect.val();
        var content = ue.getContent();

        hetajax.post({
            'url':'/apost/',
            'data':{
                'title':title,
                'content':content,
                'board_id':board_id
            },
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertConfirm({
                        'msg':'恭喜帖子发表成功！',
                        'cancelText':'回到首页',
                        'confirmText':'在发一篇',
                        'cancelCallback':function () {
                            window.location = '/';
                        },
                        'confirmCallback':function () {
                            titleInput.val('');
                            ue.setContent('');
                            
                        }

                    });
                }else{
                    hetalert.alertInfo(data['message']);
                }
                
            }

        });

    });
});