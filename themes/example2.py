from plugins.plugins import ThemePlugin

class LightThemeExample(ThemePlugin):
    def __init__(self):
        super().__init__(
            plugin_name="Light theme example plugin",
            creator="Fadi002",
            link="https://github.com/Fadi002/de4py-plugins-repo/themes/example2.py",
            css="""
body {
    background-color: lightpink;
}
h1, h2, h3, h4, h5, h6, p, span, a, ul, li, #clock, label {
    color: darkred;
}
.frame {
    border: 2px solid #4ba3e2;
    background-color: #f8f9fa;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 0 10px #4ba3e2;
}
.btn {
    color: darkred;
}
#changeLog, #outputanalyzer, #outputwinapihooks, #outputDEOBF, .scroll-box, textarea {
    background-color: #f8f9fa;
    color: darkred;
}
.custom-input {
    background-color: #9e9e9e;
    color: #333;
}

.custom-input:hover {
    background-color: #e1ecf4;
}

.custom-input:focus {
    background-color: #d0e5f5;
}

""")
