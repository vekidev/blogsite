from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)
blogs = []
with open("./api/templates/blogs/metadata.txt","r") as f:
    blogmetaraw = f.read().split('\n')
    f.close()

blogmeta = {}
for i in blogmetaraw:
    line = i.split("`")
    blogmeta[line[0]] = line[1:]

print(blogmeta)

for ind, blog in enumerate(os.listdir("./api/templates/blogs")):
    if blog.endswith(".html"):
        blogs.append([blog.removesuffix(".html"),"/blog/"+blog.removesuffix(".html"),blogmeta.get(blog,["unknown",blog.removesuffix('.html')])])

@app.route("/")
def root():
    return render_template("index.html")

@app.route(f"/blog/<blogid>")
def blogpage(blogid):
    try:
        return render_template(f"blogs/{blogid}.html",id=blogid)
    except:
        return "oh well..."

@app.route("/blog")
def blogmain():
    return render_template("blogpage.html",blogs=blogs)
