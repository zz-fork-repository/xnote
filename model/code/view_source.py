from BaseHandler import *
from web.tornado.escape import xhtml_escape

class ViewSourceHandler(BaseHandler):

    def default_request(self):
        path = self.get_argument("path", "")
        key  = self.get_argument("key", "")
        if path == "":
            self.render("code/view-source.html", error = "path is empty")
        else:
            try:
                content = fsutil.readfile(path)
                if key != "":
                    content = xhtml_escape(content)
                    key     = xhtml_escape(key)
                    content = textutil.replace(content, key, htmlutil.span("?", "search-key"), ignore_case=True, use_template=True)
                self.render("code/view-source.html", content = content)
            except Exception as e:
                self.render("code/view-source.html", error = e)

handler = ViewSourceHandler