# Frank Wang's Blog

基于 [Hugo](https://gohugo.io/) 的个人静态博客，主题为 `even`，支持中英文双语站点。  
A personal static blog built with [Hugo](https://gohugo.io/) using the `even` theme, with Chinese/English bilingual support.

## Site Overview | 站点说明

- 默认语言是中文（`/`），英文站点在 `/en/`。
- The default language is Chinese (`/`), and the English site is available at `/en/`.
- 主配置文件是 `config.toml`，文章目录是 `content/post`。
- Main config is `config.toml`, and posts are under `content/post`.

## Local Development | 本地开发

1. 安装 Hugo（建议 extended 版本）  
   Install Hugo (extended version recommended)
```bash
brew install hugo
```

2. 启动本地预览  
   Start local preview server
```bash
hugo server --bind 127.0.0.1 --port 1313 --disableFastRender --cacheDir /tmp/hugo_cache
```

3. 访问地址  
   Access URLs
- 中文首页 / Chinese home: `http://localhost:1313/`
- 英文首页 / English home: `http://localhost:1313/en/`

## Build | 构建发布

```bash
hugo --minify --cacheDir /tmp/hugo_cache
```

构建产物输出到 `public/`。  
Build output is generated in `public/`.

## Content Structure | 内容结构

- 中文文章 / Chinese post: `content/post/<name>.md`
- 英文文章 / English post: `content/post/<name>.en.md`

## English Processing Scripts | 英文处理脚本

项目内提供 3 个脚本（位于 `scripts/`）。  
The project includes 3 helper scripts in `scripts/`.

- `translate_posts.py`  
  批量生成或覆盖英文正文（机器翻译）  
  Batch-generate or overwrite English post bodies (machine translation)
- `clean_en_chinese.py`  
  清理英文稿中的中文残留  
  Remove remaining Chinese text from English posts
- `polish_en_md.py`  
  统一术语并润色常见英文表达  
  Normalize terminology and polish common English phrasing

### Script Usage | 脚本使用

建议先创建虚拟环境。  
A virtual environment is recommended.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install deep-translator
```

执行顺序如下。  
Run in this order.

```bash
.venv/bin/python scripts/translate_posts.py
.venv/bin/python scripts/clean_en_chinese.py
.venv/bin/python scripts/polish_en_md.py
```

## References | 参考

- Hugo docs: https://gohugo.io/documentation/
- Hugo Even theme: https://github.com/olOwOlo/hugo-theme-even
