from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from yt_dlp import YoutubeDL as y
def videocatch_new(videoid, getcomments=True):
    with y({"getcomments": getcomments, "quiet" : True, "cachedir":False}) as ydl:
      results = {}
      vr = ydl.extract_info("https://www.youtube.com/watch?v=" + videoid, download=False)
      results['v'] = vr['requested_formats'][0]["url"]
      results['a'] = vr['requested_formats'][1]["url"]
      results["title"] = vr['title']
      results['description'] = vr["description"].replace("\n", "<br>\n")
      commentsoutput = "";
      try:
          if (len(vr["comments"]) != 0):
            lines = 0
            for a in vr["comments"]:
              if (lines >= 100):
                break
              outputbuffer = ""
              if ("." in a["id"]):
                outputbuffer += "<br>\n┗"
                outputbuffer += a["text"].replace("\n", "<br>\n┗")
                commentsoutput += outputbuffer
              else :
                outputbuffer += "<hr>\n" + a["text"].replace("\n", "<br>\n")
                commentsoutput += outputbuffer
              lines += 1
          commentsoutput += "<hr>"
          results["comment"] = commentsoutput
          return results
      except KeyError:
          results["comment"] = ""
          return results


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/resources", StaticFiles(directory="../resources"), name="static")
template = Jinja2Templates(directory="templates").TemplateResponse

@app.get("/", response_class=HTMLResponse)
async def ytview(request: Request, vid:str ,comment:bool=True):
   m = videocatch_new(vid, comment)
   return template("main.html", {
       "title":m["title"],
       "description":m["description"],
       "v":m["v"],
       "a":m['a'],
       "comment":m['comment'],
       "request": request
   })

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
