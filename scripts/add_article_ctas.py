from pathlib import Path
import re

root = Path('/home/ubuntu/hoiku-note/client/public/articles')
line_url = 'https://hoiku.proreach.co.jp/rl/instagram_aya-7sqz'

cta_css = '''
.article-header-cta{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:8px 15px;border:0;border-radius:999px;background:#06C755;color:#fff!important;font-size:12px;font-weight:800;cursor:pointer}.article-header-cta:hover{background:#05b34b}.line-icon{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;margin-right:7px;border-radius:7px;background:#fff;color:#06C755;font-weight:900;font-size:12px}.mid-cta{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:38px 0;padding:19px 21px;border:1px solid #b9e8c9;border-radius:15px;background:#effbf3}.mid-cta strong{display:block;color:#246443;font-size:15px}.mid-cta p{margin:5px 0 0;color:#587467;font-size:12px}.line-button{display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:10px 17px;border:0;border-radius:999px;background:#06C755;color:#fff!important;font-size:12px;font-weight:800;white-space:nowrap;cursor:pointer}.line-button:hover{background:#05b34b}.bottom-cta{margin:50px 0 35px;padding:28px 25px;border-radius:18px;background:#e9f8ee;border:1px solid #aee4c0;text-align:center}.bottom-cta h2{margin:0 0 8px;border:0;padding:0;color:#246443;font-size:24px}.bottom-cta p{margin:0 auto 17px;max-width:520px;color:#587467;font-size:13px}.bottom-cta small{display:block;margin-top:10px;color:#6f927d;font-size:10px}.floating-cta{display:none}.modal-backdrop{position:fixed;inset:0;z-index:100;display:flex;align-items:center;justify-content:center;padding:18px;background:rgba(29,46,52,.48);backdrop-filter:blur(6px)}.line-modal{position:relative;width:min(100%,440px);padding:31px 27px 25px;border-radius:19px;background:#fffdfa;box-shadow:0 28px 70px rgba(21,43,50,.25)}.modal-close{position:absolute;top:13px;right:13px;width:34px;height:34px;border:0;border-radius:50%;background:#f3f0e9;color:#6f7c7b;font-size:18px;cursor:pointer}.modal-icon{display:flex;align-items:center;justify-content:center;width:45px;height:45px;margin-bottom:15px;border-radius:14px 14px 14px 5px;background:#06C755;color:#fff;font-weight:900}.line-modal h2{margin:10px 0;color:#304a54;font-size:22px;line-height:1.55}.line-modal p,.line-modal li{color:#657277;font-size:13px;line-height:1.9}.line-modal ul{margin:10px 0 18px;padding-left:20px}.line-modal small{display:block;margin-top:10px;color:#99a19d;font-size:10px}@media(max-width:700px){.mid-cta{align-items:flex-start;flex-direction:column}.mid-cta .line-button{width:100%}.floating-cta{position:fixed;right:12px;bottom:12px;left:12px;z-index:80;display:none;align-items:center;justify-content:space-between;gap:10px;padding:8px 9px 8px 15px;border:1px solid #a4e2b8;border-radius:14px;background:rgba(239,251,243,.97);box-shadow:0 10px 28px rgba(29,75,47,.18)}.floating-cta.visible{display:flex}.floating-cta span{color:#246443;font-size:12px;font-weight:800}.floating-cta button{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:8px 14px;border:0;border-radius:999px;background:#06C755;color:#fff;font-size:12px;font-weight:800}.floating-close{width:28px!important;min-height:28px!important;padding:0!important;background:transparent!important;color:#6f7c7b!important;font-size:16px!important}}
'''

for path in sorted(root.glob('*/index.html')):
    slug = path.parent.name
    text = path.read_text()
    if 'data-cta-version="1"' in text:
        continue

    # Unify the header CTA with the same modal flow.
    text = text.replace(
        f'<a href="{line_url}" target="_blank" rel="noreferrer">無料相談</a>',
        '<button class="article-header-cta" data-line-position="header"><span class="line-icon">吹</span>無料相談</button>'
    )

    mid = '''<div class="mid-cta" data-cta-version="1"><div><strong>少しでも気になったら、話してみませんか？</strong><p>対処法を試してもつらいときは、状況を整理するだけでも大丈夫です。</p></div><button class="line-button" data-line-position="mid"><span class="line-icon">吹</span>今すぐLINEで相談する</button></div>'''
    text = text.replace('<h2>関連する記事</h2>', mid + '<h2>関連する記事</h2>', 1)

    bottom = '''<div class="bottom-cta" data-cta-version="1"><h2>一人で抱え込まず、今すぐLINEで相談する</h2><p>相談内容はまとまっていなくて大丈夫です。今の状況を話しながら、次にできることを一緒に整理します。</p><button class="line-button" data-line-position="bottom"><span class="line-icon">吹</span>今すぐLINEで相談する</button><small>相談無料・しつこい連絡はしません</small></div>'''
    text = text.replace('</section><div class="author">', '</section>' + bottom + '<div class="author">', 1)

    floating = '''<div class="floating-cta" id="floating-cta"><span>悩みを一人で抱えないで</span><button data-line-position="floating"><span class="line-icon">吹</span>LINEで相談</button><button class="floating-close" id="floating-close" aria-label="閉じる">×</button></div>'''
    modal = f'''<div class="modal-backdrop" id="line-modal" hidden><div class="line-modal" role="dialog" aria-modal="true" aria-labelledby="line-modal-title"><button class="modal-close" id="modal-close" aria-label="閉じる">×</button><div class="modal-icon">吹</div><span class="label">LINE FREE CONSULTATION</span><h2 id="line-modal-title">相談内容は、まとまっていなくて大丈夫です。</h2><p>たとえば、こんなことから話せます。</p><ul><li>職場の人間関係やパワハラがつらい</li><li>有給・給与・転職のことを聞きたい</li><li>妊娠や退職について誰かに相談したい</li></ul><a class="line-button" id="line-redirect" href="{line_url}" target="_blank" rel="noreferrer">今すぐLINEで相談する</a><small>相談無料・しつこい連絡はしません。</small></div></div>'''
    js = f'''<script>const CTA_CONFIG={{lineUrl:"{line_url}",copy:"今すぐLINEで相談する",color:"#06C755",article:"{slug}"}};const trackCta=(position,step)=>{{if(typeof window.gtag==="function")window.gtag("event","line_cta_click",{{article:CTA_CONFIG.article,position,step}})}};const modal=document.getElementById("line-modal");let activePosition="header";function openLineModal(position){{activePosition=position;modal.hidden=false;modal.style.display="flex";trackCta(position,"modal_open")}}function closeLineModal(){{modal.hidden=true;modal.style.display="none"}}document.querySelectorAll("[data-line-position]").forEach((el)=>el.addEventListener("click",()=>openLineModal(el.dataset.linePosition)));document.getElementById("modal-close").addEventListener("click",closeLineModal);modal.addEventListener("click",(e)=>{{if(e.target===modal)closeLineModal()}});document.getElementById("line-redirect").addEventListener("click",()=>trackCta(activePosition,"line_redirect"));const floating=document.getElementById("floating-cta");let floatingDismissed=false;window.addEventListener("scroll",()=>{{const max=document.documentElement.scrollHeight-window.innerHeight;const passed=max>0&&window.scrollY/max>=.5;if(passed&&!floatingDismissed)floating.classList.add("visible")}});document.getElementById("floating-close").addEventListener("click",()=>{{floatingDismissed=true;floating.classList.remove("visible")}});</script>'''
    text = text.replace('</style>', cta_css + '</style>', 1)
    text = text.replace('</body>', floating + modal + js + '</body>', 1)
    path.write_text(text)
print('CTA-enhanced articles:', len(list(root.glob('*/index.html'))))
''
