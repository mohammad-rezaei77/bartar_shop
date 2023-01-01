<!DOCTYPE html>
<html lang="fa" dir="rtl">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="csrf-token" content="KBza1aLRXA8kNhca6OFH12VUDQ8Lu0DMNf3Kt9xV">

        <title>Laravel</title>

        <link rel="stylesheet" href="/css/app.css">

        <script>
            window.csrf = 'KBza1aLRXA8kNhca6OFH12VUDQ8Lu0DMNf3Kt9xV'
        </script>
    </head>
    <body>
        <div id="app" class="rtl wrapper">
            <router-view :key="$route.fullPath"></router-view>

            <notify :data='null' />
        </div>
        <script src="/js/app.js"></script>
    </body>
</html>
