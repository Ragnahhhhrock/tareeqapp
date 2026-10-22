import sys
from playwright.sync_api import sync_playwright
jobs=[("file:///home/claude/tareeqapp/social/og.html","og-image.png",1200,630),
      ("file:///home/claude/tareeqapp/social/twitter.html","twitter-card.png",1200,600)]
svg=open("/home/claude/tareeqapp/assets/brand/tareeq-mark.svg").read().replace("<svg ","<svg width=\"100%\" height=\"100%\" ",1)
with sync_playwright() as p:
    b=p.chromium.launch()
    for url,out,w,h in jobs:
        pg=b.new_page(viewport={"width":w,"height":h},device_scale_factor=1)
        pg.goto(url); pg.wait_for_timeout(600); pg.evaluate("document.fonts.ready")
        pg.screenshot(path="/home/claude/tareeqapp/"+out); pg.close()
    for size,out in [(32,"favicon-32.png"),(180,"apple-touch-icon.png"),(192,"icon-192.png"),(512,"icon-512.png")]:
        pg=b.new_page(viewport={"width":size,"height":size})
        bg="#4a5a2b" if size==180 else "transparent"
        pg.set_content(f'<body style="margin:0;background:{bg}"><div style="width:{size}px;height:{size}px">{svg}</div>')
        pg.wait_for_timeout(200); pg.screenshot(path="/home/claude/tareeqapp/"+out,omit_background=True); pg.close()
    b.close()
