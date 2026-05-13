
# Python 生成高颜值博客首页
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>xiaok的个人博客</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Microsoft YaHei", sans-serif;
        }
        body {
            background-color: #f7f9fc;
            color: #333;
            line-height: 1.7;
            padding: 40px 20px;
        }
        .container {
            max-width: 700px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }
        .header {
            text-align: center;
            margin-bottom: 35px;
            border-bottom: 1px solid #eee;
            padding-bottom: 25px;
        }
        h1 {
            font-size: 28px;
            color: #222;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #777;
            font-size: 15px;
        }
        .post {
            margin: 25px 0;
            padding: 20px;
            background: #fafbfd;
            border-radius: 12px;
            transition: 0.2s;
        }
        .post:hover {
            background: #f1f4f9;
        }
        .post h2 {
            font-size: 18px;
            margin-bottom: 8px;
            color: #2d3748;
        }
        .post p {
            color: #555;
            font-size: 14px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #999;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>我的个人博客</h1>
            <div class="subtitle">记录生活 · 分享日常 · 随笔日记</div>
        </div>

        <div class="post">
            <h2>第一篇博客 · 网站上线啦</h2>
            <p>今天用 GitHub + Vercel 搭建了自己的免费博客，不用服务器，不用花钱，随时可以更新内容。</p>
        </div>

        <div class="post">
            <h2>关于这个小站</h2>
            <p>这里用来记录日常、学习笔记、生活感悟，一个属于自己的安静小角落。</p>
        </div>

        <div class="footer">
            Powered by GitHub & Vercel
        </div>
    </div>
</body>
</html>'''

# 写入文件
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ 博客网页 index.html 生成成功！")
