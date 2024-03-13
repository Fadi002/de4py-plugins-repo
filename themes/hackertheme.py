# screenshot:
# https://prnt.sc/j44WjiYNJtn7

from plugins.plugins import ThemePlugin

class Hacker_Theme(ThemePlugin):
    def __init__(self):
        super().__init__(
            plugin_name="hacker theme",
            creator="Fadi002",
            link="https://github.com/Fadi002/de4py-plugins-repo/blob/main/themes/hackertheme.py",
            css="""html{overflow:hidden}*{font-family:"Share Tech Mono",monospace;color:#ffffffaa}h1,h2,h3,h4,h5,h6,p,span,a,ul,li,#clock,label{color:#0f2}body{width:100wh;height:100vh;background-color:#000;background-size:cover;background-position:center;background-repeat:no-repeat;cursor:crosshair}.navbar{position:fixed;height:100vh;width:200px;z-index:99;background-color:rgba(0,255,0,0.1);top:0;border-right:2px solid #0f2;box-shadow:0 4px 6px rgba(0,0,0,0.1),0 0 10px #0f2;transition-duration:.1s;cursor:pointer;backdrop-filter:blur(5px);display:flex;flex-direction:column;align-items:flex-end;padding-top:20px}.btn{width:97%;color:#00ff22aa;text-align:center;padding-top:10px;padding-bottom:10px;font-size:large;margin-bottom:10px;transition-duration:.2s}.btn:hover{background-color:rgba(0,255,0,0.2);width:100%}.menulol-container{position:fixed;top:20px;z-index:100;background-color:rgba(0,255,0,0.1);width:50px;height:50px;border-radius:50%;display:flex;justify-content:center;user-select:none;cursor:pointer;align-items:center}.menulol{font-size:24px;color:#0f2}.sebtn{border-left:2px solid #0f2}section.hidden{display:none}section.active{display:block}.content-container{left:210px;right:20px;bottom:20px;overflow-y:auto;display:flex}.center{padding:20px;margin:auto;display:flex;flex-direction:column;justify-content:center;align-items:center;height:100%}.frame{border:2px solid #0f2;background-color:#1f1f1f;border-radius:10px;padding:20px;box-shadow:0 4px 6px rgba(0,0,0,0.1),0 0 10px #0f2}.about-info{margin-top:20px;text-align:center}.about-info p{margin:10px 0;font-size:18px}.about-info a{color:#0f2;text-decoration:none;transition:color .2s}.about-info a:hover{color:#555}.scroll-box{max-height:300px;overflow-y:auto;background-color:#1f1f1f}.plugin-frame{border:2px solid #0f2;box-shadow:0 4px 6px rgba(0,0,0,0.1),0 0 10px #0f2}.scroll-box::-webkit-scrollbar{width:8px}.scroll-box::-webkit-scrollbar-thumb{background-color:#0f2;border-radius:4px}.notification-bar{color:#0f2;border-radius:10px;border:2px solid #0f2;box-shadow:0 4px 6px rgba(0,0,0,0.1),0 0 10px #0f2}.notification-progress{color:#0f2}.btn{width:97%;color:#00ff22aa;text-align:center;padding-top:10px;padding-bottom:10px;font-size:large;margin-bottom:10px;transition-duration:.2s}.btn:hover{background-color:rgba(0,255,0,0.2);width:100%}.btns{background-color:#0f2;box-shadow:0 4px 6px rgba(0,0,0,0.1),0 0 10px #0f2}.btns:hover{background-color:#222;color:#0f2;box-shadow:0 4px 6px rgba(0,0,0,0.1),0 0 10px #0f2}.plugin-info{color:#0f2}""")
