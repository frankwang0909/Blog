+++
categories = ["frontend"]
tags = ["JavaScript"]
title = "两个Safari浏览器不兼容的坑"
keywords = ["iOS系统", "Safari浏览器", "new Date()日期转换", "事件不兼容"]
description = "苹果手机的Safari浏览器不兼容new Date()日期转换格式的坑, Safari在iOS5及以下对YYYY-MM-DD格式的日期不支持，所以需要转换日期的格式为YYYY/MM/DD。苹果手机的Safari浏览器不支持 keydown, keypress, keyup, change等事件的坑,在iOS的Safari中。 keydown、keypress、 keyup、change等事件都无效，考虑监听input和propertychange事件作为代替"
date = "2017-06-01T07:35:15+08:00"
url = "/safari-not-support.html"
+++


## 一、 苹果手机的Safari浏览器不兼容  new Date()日期转换格式的坑

做Web项目的开发，`倒计时`是个很常见的需求。我的需求是做一个演唱会门票开售时间的倒计时。

### 思路如下：

取到 `开售时间`和`服务器上现在的时间`，用`开售时间`减去`现在的时间`，得出一个时间毫秒数，然后再转换成xx天xx小时xx分xx秒。

跟后台技术小哥简单沟通了一下，后台会将`开售时间`和`现在的时间`传到页面上，放在`隐藏域`里，这样我用JavaScript就能取到时间了。so easy! 然后我就开始写代码了。

一开始我是这样写的：

```javascript
function preSellCount(){
    // 如果没有设置开售时间，则取演出时间，取到的时间格式为2017-06-01 10:00
    var preSt = $('#preSellTime').val() || $('#showTime').val();  

    var nowTime = $('#nowTime').val();

    // 如果没有设置开售时间，也没有设置演出的时间，则倒计时处显示“开售时间待定”
    if (!preSt) {
        $('#preSellCount').text("开售时间待定");
    }else{

        //取到的开售时间是一个字符串，先转换成毫秒数，
        var sellTime = new Date(preSt).getTime();

        //现在的毫秒数
        var now = new Date(nowTime).getTime();

        var count, d, h, min, sec, timeStr, timer;

        count = now > sellTime ? 0 : Math.floor((sellTime-now)/1000);

        //进来页面的时间不为零，才执行定时器
        if(count!==0){
            // 定时器
            timer = setInterval(function() {
                if (count === 0) {
                    clearInterval(timer);

                    // 倒计时为零时，自动刷新页面
                    window.location.reload();
                }else{
                    
                    // 天数
                    d = Math.floor(count/86400); 

                    // 小时数
                    h = Math.floor(count%86400/3600); 

                    // 分钟数
                    min = Math.floor(count%86400%3600/60); 

                    // 秒钟数
                    sec = Math.floor(count%86400%3600%60);

                    // 小于10的时候，前面补一个‘0’。
                    if (min < 10) {
                        min = '0' + min;
                    }
                    if (sec < 10 ) {
                        sec = '0' + sec;
                    }

                    if (d == 0) {
                        timeStr =  h + "小时" + min + "分" + s + "秒";
                    }else{
                        timeStr = d + "天" + h + "小时" + min + "分" + s + "秒";
                    }
                    // 得到倒计时的时间字符串
                    timeStr = d + "天" + h + "小时" + min + "分" + sec + "秒";

                    // 将字倒计时显示到页面上
                    $('#preSellCount').text(timeStr);

                    count -= 1;
                }
            }, 1000);
        }
    }
}

```

用 Chrome 模拟各种手机调试都是一切正常。发布到本地测试环境，然后用自己的安卓手机访问，也一切正常。再用同事的苹果手机测试，倒计时不显示。WTF?

想想哪里可能会有兼容性问题呢？

从头检查一遍代码。获取开售时间没有问题。取到的开售时间是一个字符串的日期，用`new Date(preSt).getTime()`转换成毫秒数，有没有问题呢？Google一下`new Date() iOS`。
果然发现有不少相关文章提到iOS下日期转换问题。由于Safari在iOS5及以下对`YYYY-MM-DD`格式的日期不支持，所以需要转换格式。

最简单的是用`正则表达式`把日期转换成 `YYYY/MM/DD`格式。

```javascript

    preSt.replace(/-/g, "/")

```

最终的代码是这样的：

```javascript

function preSellCount(){
    // 如果没有设置开售时间，则取演出时间，取到的时间格式为2017-06-01 10:00
    var preSt = $('#preSellTime').val() || $('#showTime').val();  
    var nowTime = $('#nowTime').val();
    // 如果没有设置开售时间，也没有设置演出的时间，则倒计时处显示“开售时间待定”
    if (!preSt) {
        $('#preSellCount').text("开售时间待定");
    }else{

        //取到的开售时间是一个字符串，先转换成毫秒数，
        var sellTime = new Date(preSt.replace(/-/g, "/")).getTime();

        //现在的毫秒数
        var now = new Date(nowTime.replace(/-/g, "/")).getTime();

        var count, d, h, min, sec, timeStr, timer;

        count = now > sellTime ? 0 : Math.floor((sellTime-now)/1000);

        //进来页面的时间不为零，才执行定时器
        if(count!==0){
            // 定时器
            timer = setInterval(function() {
                if (count === 0) {
                    clearInterval(timer);

                    // 倒计时为零时，自动刷新页面
                    window.location.reload();
                }else{
                    
                    // 天数
                    d = Math.floor(count/86400); 

                    // 小时数
                    h = Math.floor(count%86400/3600); 

                    // 分钟数
                    min = Math.floor(count%86400%3600/60); 

                    // 秒钟数
                    sec = Math.floor(count%86400%3600%60);

                    // 小于10的时候，前面补一个‘0’。
                    if (min < 10) {
                        min = '0' + min;
                    }
                    if (sec < 10 ) {
                        sec = '0' + sec;
                    }

                    if (d == 0) {
                        timeStr =  h + "小时" + min + "分" + s + "秒";
                    }else{
                        timeStr = d + "天" + h + "小时" + min + "分" + s + "秒";
                    }
                    // 得到倒计时的时间字符串
                    timeStr = d + "天" + h + "小时" + min + "分" + sec + "秒";

                    // 将字倒计时显示到页面上
                    $('#preSellCount').text(timeStr);

                    count -= 1;
                }
            }, 1000);
        }
    }
}

```


## 二、苹果手机的Safari浏览器不支持  keydown, keypress, keyup, change等事件的坑。

需求:在输入框中输入内容时，输入框后边显示清除按钮，点击可以清除输入框中的所有内容

```javascript
var keyword = $("#search-keyword");
var clear = $('.clear');

keyword.on('keyup', function(event) {
    if($(this).val().length>0){

        //显示清空输入框的小图标
        clear.show();

    }else{

        // 隐藏清空输入框的小图标
        clear.hide();
    }
});

```

但是在 iOS 的 Safari 中, keydown、keypress、 keyup、change等事件都无效，考虑监听 input 和 propertychange 事件作为代替。

```javascript
var keyword = $("#search-keyword");
var clear = $('.clear');

keyword.on('input propertychange', function(event) {
    if($(this).val().length>0){
        //显示清空输入框的小图标
        clear.show();
    }else{
        // 隐藏清空输入框的小图标
        clear.hide();
    }
});

```


