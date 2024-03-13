extensions = ["nbsphinx"]

templates_path = []
exclude_patterns = []
html_static_path = []

project = "YiJingFramework.Annotating.Zhouyi"
language = 'zh_CN'

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/YiJingFramework/Annotating.Zhouyi.git",
    "use_repository_button": True,
    "extra_footer": "这里是 YiJingFramework.Annotating.Zhouyi 的文档。前往 "
                    "<a href=\"https://yjfwk.yueyinqiu.top/\">https://yjfwk.yueyinqiu.top/</a> "
                    "查看更多项目。",
}
# html_logo = "taiji32.png"
html_title = "YiJingFramework. Annotating. Zhouyi"

nbsphinx_codecell_lexer = "csharp"
pygments_style = "vs"
nbsphinx_execute = "never"
