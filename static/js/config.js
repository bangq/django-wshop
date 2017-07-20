/**
 * Created by sanli on 2017/7/20.
 */

KindEditor.ready(function (K) {
    window.editor = K.create('#id_details', {
        uploadJson: '/admin/upload/kindeditor',
        // 指定大小
        width: '800px',
        height: '200px'
    });
});