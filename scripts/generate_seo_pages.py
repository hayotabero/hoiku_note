from pathlib import Path
from html import escape
from datetime import date

ROOT = Path('/home/ubuntu/hoiku-note/client/public')
BASE = 'https://hoikunote-rhueltws.manus.space'
TODAY = '2026-09-15'

articles = [
  {
    'slug':'pawahara-taisho', 'keyword':'保育士 パワハラ 対処法',
    'title':'保育士 パワハラ対処法｜記録と相談先を整理',
    'description':'保育士のパワハラ対処法を、よくある言動、記録の取り方、園内外の相談先、環境を変える判断まで同業者目線で整理します。',
    'category':'人間関係',
    'summary':['まずは日時・場所・発言を記録する','直属の上司以外も含めて相談先を持つ','改善しない場合は転職も選択肢に入れる'],
    'story':'20代・経験2年のAさんは、主任からみんなの前で何度も叱責され、出勤前に動悸がするようになりました。最初は自分の力不足と思っていましたが、日時と発言をメモして園長に相談。配置と指導方法が変わり、少しずつ落ち着きを取り戻しました。',
    'body':'パワハラかもしれない言動は、感情だけで抱えると状況が見えにくくなります。日時・場所・相手・言われた内容・同席者・仕事や体調への影響を、できるだけ具体的に残しましょう。メールやシフト表など、もともと自分が閲覧できる資料も整理します。園内では園長、法人本部、相談担当など、直属の相手以外の窓口を検討できます。園外なら自治体の相談窓口や労働局の総合労働相談コーナーなど、一般的な相談先もあります。個別の法的判断は専門窓口で確認しながら進めてください。',
    'faqs':[('何を記録すればいいですか？','日時、場所、相手、具体的な発言、見ていた人、その後の影響を分けて記録すると相談時に伝えやすくなります。'),('退職をすぐ決めるべきですか？','急いで結論を出す必要はありません。記録と相談を行い、改善の可能性や心身への影響を見ながら選択肢を比べましょう。')]
  },
  {
    'slug':'yukyu-torenai', 'keyword':'保育士 有給 取れない',
    'title':'保育士 有給が取れない｜伝え方と確認ポイント',
    'description':'保育士が有給を取れないと感じるときの確認ポイント、園側のよくある言い分、角が立ちにくい交渉の仕方、転職検討サインを解説します。',
    'category':'働き方',
    'summary':['有給は条件を満たせば法律上認められる休暇','希望日・引き継ぎ・代替案をセットで伝える','慢性的に取れない園は環境を見直すサイン'],
    'story':'30代・経験8年のBさんは、「人が足りないから今月は無理」と毎回言われ、有給残日数だけが増えていました。希望日を早めに伝え、引き継ぎ表を添えて申請する形に変えたところ、園との会話が具体的になりました。',
    'body':'有給休暇は、雇用形態など一定の要件を満たす場合に法律上認められる休暇です。園の業務運営上、取得時期の調整が行われることはありますが、「忙しいから一切取れない」が慢性化している場合は、労働条件通知書や就業規則を確認しましょう。伝えるときは「○月○日に取得したいです。書類は前日までに整え、○○さんへ引き継ぎます」のように、日付・準備・代替案をセットにすると話し合いやすくなります。個別の適用やトラブルは、労働局などの専門窓口で確認してください。',
    'faqs':[('忙しい時期は有給を取れませんか？','業務上の調整が必要な場合はありますが、年間を通じて一切取れない状態なら、就業規則や相談窓口を確認することをおすすめします。'),('パートでも有給はありますか？','勤務日数や継続勤務期間などの条件により異なります。雇用契約と給与明細を確認し、必要なら専門窓口へ相談しましょう。')]
  },
  {
    'slug':'tedori-20man', 'keyword':'保育士 手取り20万円',
    'title':'保育士 手取り20万円は普通？給与の見方と上げ方',
    'description':'保育士の手取り20万円は多いか少ないかを、経験年数・地域・手当の違いから整理。給与を上げやすい園の特徴も紹介します。',
    'category':'お金',
    'summary':['手取りは地域・経験年数・手当で大きく変わる','額面と手取り、処遇改善手当を分けて確認する','資格手当・役職・転職で上がる可能性がある'],
    'story':'20代・経験3年のCさんは手取り20万円。友人と比べて少ない気がしていましたが、額面・住宅手当・処遇改善手当を分けて見ると、比較すべき項目が見えてきました。求人票だけでなく、手当の支給条件を面接で聞くようになりました。',
    'body':'手取り20万円が多いか少ないかは、地域、経験年数、勤務時間、住宅手当や処遇改善手当の有無で変わります。まず給与明細で、基本給・固定手当・変動手当・控除を分けて確認しましょう。給与を上げる方法には、資格手当のある園を選ぶ、リーダーや主任など役割に応じた手当を確認する、経験を評価する園へ転職するなどがあります。金額だけでなく、残業時間、休みやすさ、業務量も合わせて比較すると、長く続けやすい条件を見つけやすくなります。',
    'faqs':[('手取り20万円は少ないですか？','一概には言えません。地域や経験、手当で差が大きいため、額面と手当の内訳を同じ条件の求人と比べてみましょう。'),('給与交渉はできますか？','可能な場合があります。希望額だけでなく、経験年数、担当業務、取得資格を具体的に伝え、条件を確認しましょう。')]
  },
  {
    'slug':'nendo-tochu-tenshoku', 'keyword':'保育士 年度途中 転職タイミング',
    'title':'保育士 年度途中の転職タイミング｜円満退職のコツ',
    'description':'保育士が年度途中に転職するときのメリット・デメリット、うまくいくケース、円満退職の伝え方、タイミングの見極め方を解説します。',
    'category':'キャリア',
    'summary':['年度途中でも採用ニーズが合えば動ける','引き継ぎ計画を早めに相談する','転職理由より次の働き方を具体的に伝える'],
    'story':'経験5年のDさんは、年度末まで我慢するつもりでしたが、体調が崩れ始めたため転職活動を開始。見学で職員配置や休みの取り方を確認し、退職時期と引き継ぎを早めに相談しました。',
    'body':'年度途中の転職には、すぐに人材を探している園と出会いやすいこと、今の環境を早く変えられることがあります。一方で、引き継ぎや子どもたちへの配慮が必要です。応募前に、希望入職日、担当業務、引き継ぎに必要な期間を整理しておきましょう。退職を伝えるときは、相手を責める言い方ではなく「○月末を目安に、引き継ぎ計画を相談したいです」と事実と希望を落ち着いて伝えます。体調や安全に関わる場合は、年度末を待つことだけを正解にしないでください。',
    'faqs':[('年度途中の転職は迷惑ですか？','引き継ぎへの配慮は必要ですが、年度途中の採用を行う園もあります。自分の安全や健康も含めて判断しましょう。'),('いつ退職を伝えればいいですか？','就業規則や雇用契約を確認し、必要な予告期間を見たうえで、引き継ぎに余裕を持って相談するのが一般的です。')]
  },
  {
    'slug':'ninshin-taishoku-trouble', 'keyword':'保育士 妊娠 退職トラブル',
    'title':'保育士 妊娠・退職トラブル｜伝え方と選択肢',
    'description':'保育士が妊娠を機に退職を考えるときの、よくある引き止めや圧力、制度の確認、円満に伝える方法を共感ベースで整理します。',
    'category':'体調・ライフイベント',
    'summary':['妊娠の報告と退職の判断は分けて考える','体調と安全を優先し、制度を確認する','一人で園と交渉せず相談先を持つ'],
    'story':'30代・経験10年のEさんは、妊娠を報告した際に「年度末までは続けられるよね」と言われ、嬉しさと不安が入り混じりました。まず主治医に働き方を確認し、園には体調と希望時期を分けて伝えることで、話し合いの焦点を整理できました。',
    'body':'妊娠はおめでたい出来事である一方、保育現場では人手不足や引き継ぎへの不安から、報告や退職の相談に気を遣うことがあります。まず妊娠の報告、体調・配慮の相談、退職や休業など今後の希望を分けて考えると、話し合いやすくなります。職場の制度や手続きは個別の雇用条件で異なるため、就業規則、自治体や勤務先の窓口、必要に応じて専門機関へ確認しましょう。体調や安全に関しては主治医の指示を優先してください。',
    'faqs':[('妊娠を理由に退職を迫られたら？','一人で判断せず、発言や日時を記録し、勤務先の相談窓口や自治体・専門相談窓口へ確認しましょう。'),('退職以外の選択肢はありますか？','休業、配置や勤務時間の相談、出産後の復職、別の園での再スタートなど、状況により複数の選択肢があります。')]
  },
  {
    'slug':'ningen-kankei-tsukareta', 'keyword':'保育士 人間関係 疲れた',
    'title':'保育士 人間関係に疲れた｜抱え込まない整理術',
    'description':'保育士の人間関係に疲れたときに、あるある事例から原因を整理。距離の取り方、相談、園の文化を見直す視点を紹介します。',
    'category':'人間関係',
    'summary':['苦手な人がいることと、園の文化は分けて考える','事実・感情・希望を整理して相談する','改善しないときは環境との相性を見直す'],
    'story':'20代・経験1年のFさんは、休憩室の空気が重く、質問するだけで緊張していました。40代・経験15年のGさんは、長年の役割固定に疲れていました。年齢や経験が違っても、「相談できない」「休めない」という構造的なつらさは共通しています。',
    'body':'人間関係に疲れたとき、相手の性格だけを変えようとすると消耗します。まず「いつ、どんな場面で、何が起きるとつらいのか」を整理し、距離を取れる場面と、相談が必要な場面を分けましょう。園長や主任が職員の話を聞く文化か、休憩や有給をお互いさまと考えられるか、ミスを責めるだけでなく振り返れるか。人間関係は園の文化によって大きく変わります。自分の努力だけで改善しないなら、環境を変える視点を持ってもよいのです。',
    'faqs':[('苦手な人とはどう距離を取ればいいですか？','業務上必要な連絡に絞り、記録や第三者を交えた相談を使いながら、一人で抱えないことが大切です。'),('転職すれば人間関係は解決しますか？','必ず解決するとは限りませんが、園の文化や相談体制を見学・面接で確認することで相性を見極めやすくなります。')]
  },
  {
    'slug':'tenshoku-timing-nendomatsu', 'keyword':'保育士 転職 タイミング 年度末',
    'title':'保育士 転職タイミングは年度末？動く時期の選び方',
    'description':'保育士の転職タイミングを年度末・年度途中で比較。求人の探し方、見学で確認したい項目、今から準備する順番を整理します。',
    'category':'キャリア',
    'summary':['年度末は引き継ぎしやすい一方、求人が集中する','年度途中は採用ニーズと条件が合えば動きやすい','時期よりも自分の体調と希望条件を優先する'],
    'story':'経験7年のHさんは年度末に絞って探していましたが、見学の予約が集中。翌年は秋から条件を整理し、求人が出た園を早めに見学することで、比較する時間を確保できました。',
    'body':'年度末は退職・入職の区切りをつけやすく、引き継ぎの説明もしやすい時期です。一方、応募が集中するため、条件の比較に時間がかかることがあります。年度途中は求人が少ない時期もありますが、欠員補充など採用ニーズが明確な園と出会える可能性があります。まず希望する勤務時間、給与、通勤、休みやすさ、職員配置を整理し、時期に縛られず情報収集を始めましょう。',
    'faqs':[('年度末まで待つべきですか？','体調や職場環境が安定しているなら準備期間にできますが、心身への負担が大きい場合は年度途中も選択肢です。')]
  },
  {
    'slug':'enman-taishoku-tsutaekata', 'keyword':'保育士 円満退職 伝え方',
    'title':'保育士 円満退職の伝え方｜引き止めへの備え',
    'description':'保育士が円満退職を目指すときの伝える順番、引き継ぎの準備、引き止めへの返答例を、無理のない範囲で整理します。',
    'category':'キャリア',
    'summary':['退職理由は簡潔に、希望日とセットで伝える','引き継ぎは見える化して相談する','引き止められても結論を急いで変えなくていい'],
    'story':'経験4年のIさんは、退職を切り出すだけで涙が出そうでした。「○月末を希望しています。引き継ぎ表を作るので相談させてください」と紙に書いてから話したことで、伝える内容を保てました。',
    'body':'円満退職を目指すなら、退職理由を長く説明して相手を説得しようとするより、退職希望日、引き継ぎ、必要な手続きを順番に伝えることが役立ちます。「一身上の都合で、○月末を希望しています。担当業務は一覧にして、引き継ぎの時間を相談したいです」と、事実と希望を簡潔に伝えましょう。引き止めに対しては「考えたうえでの決断です。引き継ぎについては協力します」と繰り返しても構いません。',
    'faqs':[('退職理由を詳しく話す必要はありますか？','すべてを説明する必要はありません。相手を責めず、希望時期と引き継ぎを具体的に伝えると話し合いやすくなります。')]
  },
  {
    'slug':'hoiku-en-miwake', 'keyword':'保育士 転職 失敗しない園の見分け方',
    'title':'保育士 転職で失敗しない園の見分け方',
    'description':'保育士が転職で失敗しないために、求人票だけでは分からない園の文化、休み、職員配置、面接・見学での質問をまとめます。',
    'category':'キャリア',
    'summary':['求人票と現場の説明を照らし合わせる','休み・残業・配置を具体的に質問する','見学では職員同士の声かけも観察する'],
    'story':'30代・経験9年のJさんは、給与だけで決めた園で業務量に悩みました。次の転職では、休憩の取り方、欠勤時のフォロー、入職後の研修を質問し、働くイメージを持てる園を選びました。',
    'body':'転職先を選ぶときは、給与や通勤だけでなく、日常の運営を具体的に確認しましょう。「有給はどのように申請しますか」「欠勤が出た日の配置はどうなりますか」「休憩はどこで取りますか」「入職後の研修はありますか」といった質問は、働き続ける準備として自然です。見学では、職員同士の声かけ、子どもへの接し方、室内の整理だけでなく、質問への答え方が具体的かも見ておきましょう。',
    'faqs':[('見学で何を見ればいいですか？','職員同士の声かけ、子どもへの接し方、休憩場所、質問への回答の具体性などを確認すると園の文化を感じやすくなります。')]
  },
]

css = '''body{margin:0;background:#fbfaf7;color:#2c414d;font-family:Arial,"Noto Sans JP",sans-serif;line-height:1.9}a{color:#d87360;text-decoration:none}.wrap{max-width:860px;margin:auto;padding:28px 22px 80px}.site{border-top:5px solid #e7826b;border-bottom:1px solid #e8e3da;padding:15px 22px;background:#fffdfa}.site-inner{max-width:1180px;margin:auto;display:flex;justify-content:space-between;align-items:center}.brand{font-weight:800;color:#2c414d}.brand small{display:block;color:#8a9692;font-size:9px;letter-spacing:.15em}.nav{display:flex;gap:18px;font-size:12px}.crumb{margin:24px 0;color:#89938f;font-size:12px}.crumb a{color:#738b82}.label{display:inline-block;color:#d87360;font-size:11px;font-weight:700;letter-spacing:.12em}.summary{margin:25px 0;padding:20px 24px;border-radius:14px;background:#fff0e8;border-left:4px solid #e7826b}.summary strong{display:block;margin-bottom:8px;color:#bd6655}.summary ul{margin:0;padding-left:20px}.story{padding:18px 21px;background:#edf3ef;border-radius:12px;color:#5e7070}.check{padding:19px 22px;background:#fff;border:1px solid #e6e0d8;border-radius:12px}.check li{margin:5px 0}.article h1{font-size:clamp(28px,5vw,50px);line-height:1.3;letter-spacing:-.05em;margin:18px 0;color:#293e4a}.article h2{font-size:24px;margin:50px 0 14px;border-bottom:1px solid #e7e1d8;padding-bottom:10px}.article h3{font-size:18px}.article p{color:#5f6e73}.related{display:grid;gap:10px;margin-top:20px}.related a{display:block;padding:12px 16px;background:#fff;border:1px solid #e6e0d8;border-radius:9px;color:#49676a}.author{margin-top:50px;padding:22px;background:#e9f1ed;border-radius:14px}.faq{margin-top:45px}.faq details{padding:14px 0;border-bottom:1px solid #e5e0d8}.faq summary{cursor:pointer;font-weight:700;color:#455d62}.footer{margin-top:60px;padding-top:20px;border-top:1px solid #e8e3da;color:#8a9591;font-size:12px}@media(max-width:600px){.nav{display:none}.wrap{padding:18px 17px 55px}.article h2{font-size:21px}}'''

def page(a):
    url = f'{BASE}/articles/{a["slug"]}/index.html'
    breadcrumb = [{'@type':'ListItem','position':1,'name':'保育ノート','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'記事一覧','item':BASE+'/#topics'},{'@type':'ListItem','position':3,'name':a['keyword'],'item':url}]
    faq = [{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':ans}} for q,ans in a['faqs']]
    related = [x for x in articles if x['slug'] != a['slug']][:3]
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(a['title'])}</title><meta name="description" content="{escape(a['description'])}"><link rel="canonical" href="{url}"><style>{css}</style><script type="application/ld+json">{__import__('json').dumps({'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':breadcrumb},ensure_ascii=False)}</script><script type="application/ld+json">{__import__('json').dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':faq},ensure_ascii=False)}</script></head><body><header class="site"><div class="site-inner"><a class="brand" href="{BASE}/">保育ノート<small>HOIKU NOTE</small></a><nav class="nav"><a href="{BASE}/#topics">悩みから探す</a><a href="{BASE}/#article">読みもの</a><a href="https://hoiku.proreach.co.jp/rl/instagram_aya-7sqz" target="_blank" rel="noreferrer">無料相談</a></nav></div></header><main class="wrap article"><nav class="crumb" aria-label="パンくず"><a href="{BASE}/">トップ</a>　&gt;　<a href="{BASE}/#topics">記事一覧</a>　&gt;　{escape(a['keyword'])}</nav><span class="label">{escape(a['category'])}　/　2026.09.15</span><h1>{escape(a['title'])}</h1><div class="summary"><strong>この記事の結論</strong><ul>{''.join(f'<li>{escape(x)}</li>' for x in a['summary'])}</ul></div><p>{escape(a['story'])}</p><h2>こんな悩みありませんか？</h2><p>{escape(a['body'])}</p><div class="check"><strong>セルフチェック</strong><ul><li>職場で相談できる人がいない</li><li>休みや給与の条件を説明されていない</li><li>出勤前から気持ちが重い日が続く</li></ul><p>3つ以上当てはまる場合は、記事の対処法を試しながら、外部相談や環境を変える選択肢も検討してみてください。</p></div><h2>今日からできる対処法</h2><p>{escape(a['body'])}</p><h2>関連する記事</h2><div class="related">{''.join(f'<a href="{BASE}/articles/{x["slug"]}/index.html">{escape(x["keyword"])}</a>' for x in related)}</div><section class="faq"><h2>よくある質問</h2>{''.join(f'<details><summary>{escape(q)}</summary><p>{escape(ans)}</p></details>' for q,ans in a['faqs'])}</section><div class="author"><strong>執筆・編集：保育ノート編集部</strong><p>保育現場での勤務経験者と、保育士の転職・働き方を取材してきた編集メンバーが、制度や職場選びの情報を整理しています。個別の法律・医療判断は専門窓口へご確認ください。</p></div><footer class="footer"><a href="{BASE}/">保育ノート トップへ戻る</a></footer></main></body></html>'''

for a in articles:
    path = ROOT / 'articles' / a['slug'] / 'index.html'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page(a), encoding='utf-8')

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',f'<url><loc>{BASE}/</loc><lastmod>{TODAY}</lastmod><priority>1.0</priority></url>']
for a in articles:
    sitemap.append(f'<url><loc>{BASE}/articles/{a["slug"]}/index.html</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>')
sitemap.append('</urlset>')
(ROOT/'sitemap.xml').write_text('\n'.join(sitemap), encoding='utf-8')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n', encoding='utf-8')
print(f'generated {len(articles)} article pages')
print('sitemap', ROOT/'sitemap.xml')
print('robots', ROOT/'robots.txt')
