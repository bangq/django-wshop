/*tab切换*/
(function ($) {
  $.fn.zTab=function(options) {
   var dft={
      tabnav:'.tabnav',
      tabcon:'.tabcon',
      trigger:'mouseenter',
      curName:'current',
      removeMod:null,
      cur:0,
      delay:0,
      auto:null,
      callback : null ,
      load:null
    };

    var ops=$.extend(dft,options);
    return this.each(function () {
      var self=$(this),
      nav=self.find(ops.tabnav),
      con=self.find(ops.tabcon),
      navBtn=nav.children(),
      num=navBtn.length,
      timer=null,
      timer2=null,
      isInit=false;

      //初始化执行
      init();

      navBtn.on(ops.trigger,function () {
        ops.cur=$(this).index();
        clearTimeout(timer);
        clearTimeout(timer2);
        timer=setTimeout(run,ops.delay);
        return false;
      });

      navBtn.on('mouseleave',function () {
        clearTimeout(timer);
        if (ops.auto) {
          timer2=setInterval(auto,ops.auto.interval);
        }
      });
      //
      function init () {
        ops.trigger=='click'?ops.trigger='click':ops.trigger='mouseenter'; //导航触发方式判定
        run();
        if (ops.auto) {
          timer2=setInterval(auto,ops.auto.interval);
        }
        else {
          run();
        }

        if(ops.load){
          ops.load(self,ops.cur,num);
        }

        isInit=true;
      }
      //
      function run () {
        if (ops.removeMod) {
          navBtn.addClass(ops.curName).eq(ops.cur).removeClass(ops.curName); //
        }
        else {
          navBtn.removeClass(ops.curName).eq(ops.cur).addClass(ops.curName); //
        }

          con.hide().eq(ops.cur).show(); //

         if(ops.callback&&isInit){
          ops.callback(ops.cur,ops);
        }
      }
      //
      function auto () {
        ops.cur+=1;
        if (ops.cur==num) {ops.cur=0;}
        run();
      }

    });
}
})(jQuery);

var zAction = function () {
  //namespace
  var action = {}

  var SELECTOR = '[data-action]'
  var _actionList = {}

  //util
  function _getActionName($elem) {
    var result = $elem.data('action') || ''
    if (!result) {
      var href = $.trim($elem.attr('href'))
      if (href && href.indexOf('#') === 0) result = href
    }
    return _formatActionName(result)
  }
  function _formatActionName(s) {
    return s ? $.trim(String(s).replace(/^[#!\s]+/, '')) : ''
  }

  function _init() {
    var $wrapper = $(document.body || document.documentElement)
    $wrapper.on('click', SELECTOR, function (ev) {
      //notice: default click behavior will be prevented.
      ev.preventDefault()

      var $elem = $(this)
      var actionName = _getActionName($elem)
      _handle(actionName, this)
    })
  }
  function _handle(actionName, context) {
    if (!actionName) {
      /** DEBUG_INFO_START **/
      console.warn('[Action] Empty action. Do nothing.')
      /** DEBUG_INFO_END **/
      return
    }
    var fn = _actionList[actionName]
    if (fn && $.isFunction(fn)) {
      /** DEBUG_INFO_START **/
      // console.log('[Action] Executing action `%s`.', actionName)
      /** DEBUG_INFO_END **/
      return fn.call(context || window)
    } else {
      /** DEBUG_INFO_START **/
      console.error('[Action] Not found action `%s`.', actionName)
      /** DEBUG_INFO_END **/
    }
  }

  //api
  action.add = function (actionSet) {
    if ($.isPlainObject(actionSet)) {
      $.each(actionSet, function (key, value) {
        var actionName = _formatActionName(key)
        if (actionName) {
          if ($.isFunction(value)) {
            /** DEBUG_INFO_START **/
            if (_actionList[actionName]) {
              console.warn('[Action] The existed action `%s` has been overridden.', actionName)
            }
            /** DEBUG_INFO_END **/

            _actionList[actionName] = value
          } else {
            /** DEBUG_INFO_START **/
            console.error('[Action] The function for action `%s` is invalid.', actionName)
            /** DEBUG_INFO_END **/
          }
        } else {
          /** DEBUG_INFO_START **/
          console.error('[Action] The action name `%s` is invalid.', key)
          /** DEBUG_INFO_END **/
        }
      })
    } else {
      /** DEBUG_INFO_START **/
      console.warn('[Action] Param must be a plain object.')
      /** DEBUG_INFO_END **/
    }
  }
  action.trigger = function (actionName, context) {
    return _handle(_formatActionName(actionName), context)
  }

  //init
  _init()

  /** DEBUG_INFO_START **/
  //exports for unit test
  action.__actionList = _actionList
  action.__getActionName = _getActionName
  action.__formatActionName = _formatActionName
  /** DEBUG_INFO_END **/

  //exports
  return action
}()

//运行
$(function () {
    FastClick.attach(document.body);

    //
    $(document.body).on('click','.ui-fullmask',function (e) {
        var target  = $(e.target);
        if (target.closest('.popfilter').length==0) { //ui-fullmask 内部的组件类名
          $('html,body').removeClass('holding');
          $(this).removeClass('show');
        }
    });

    //商品筛选下拉
  zAction.add({
    'filter-toggle':function () {
      var row=$(this).parents('.filter-row');
      row.toggleClass('on');
    },

  });
});