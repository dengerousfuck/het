/**
 * Created by denger on 2018/2/25.
 */
$(function () {
    $(".highlight-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr('data-id');
        var highlight = parseInt(tr.attr('data-highlight'));
        var url = '';
        if(highlight){
            url = '/cms/uhpost/';
        }else{
            url = '/cms/hpost/';
        }
        hetajax.post({
            'url':url,
            'data':{
                'post_id':post_id
            },
            'success':function (data) {
                if(data['code'] == 200){
                    hetalert.alertSuccess('操作成功！');
                    setTimeout(function () {
                        window.location.reload();
                    },500);
                }else{
                    hetalert.alertInfo(data['message']);
                }
            }
        });
    })
});

// $(function () {
//     $(".delete-btn").click(function (event) {
//         event.preventDefault();
//
//
//     })
// });