!(function (doc, win) {
    var el = doc.documentElement;
    //resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize';

    function setSize() {
        var w = el.clientWidth;
        if (!w) return;
        w=w>480?480:w;
        w=w<320?320:w;
        el.style.fontSize = (100 * (w / 1080)).toFixed(3) + 'px';
    }
    if (!doc.addEventListener) return;
    setSize();
    win.addEventListener('resize', setSize, false);
    win.addEventListener('pageshow', function(e) {
         if (e.persisted) {
            setSize();
         }
    }, false);
})(document, window);

