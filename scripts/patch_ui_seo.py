from pathlib import Path
p=Path('/home/ubuntu/hoiku-note/client/src/pages/Home.tsx')
s=p.read_text()
s=s.replace('const salaryRows = [','const categories = ["すべて", "お金", "人間関係", "体調・ライフイベント", "キャリア", "働き方"];\n\nconst salaryRows = [')
s=s.replace('  const [query, setQuery] = useState("");','  const [query, setQuery] = useState("");\n  const [activeCategory, setActiveCategory] = useState("すべて");')
s=s.replace('''      topics.filter((topic) =>
        `${topic.label}${topic.title}${topic.text}`.toLowerCase().includes(query.toLowerCase()),
      ),''','''      topics.filter((topic) => {
        const matchesQuery = `${topic.label}${topic.title}${topic.text}`.toLowerCase().includes(query.toLowerCase());
        const matchesCategory = activeCategory === "すべて" || topic.label === activeCategory || (activeCategory === "体調・ライフイベント" && topic.label === "ライフイベント");
        return matchesQuery && matchesCategory;
      }),''')
s=s.replace('''    [query],
  );''','''    [query, activeCategory],
  );''',1)
needle='''            <div id="search" className="search-box mt-8">
              <Search size={19} /><input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="キーワードで記事を探す（例：有給、転職）" aria-label="記事を検索" />
              {query && <button onClick={() => setQuery("")} aria-label="検索をクリア"><X size={16} /></button>}
            </div>'''
replacement=needle+'''\n            <div className="category-tabs" role="tablist" aria-label="カテゴリで絞り込む">{categories.map((category) => <button key={category} role="tab" aria-selected={activeCategory === category} className={activeCategory === category ? "active" : ""} onClick={() => setActiveCategory(category)}>{category}</button>)}</div>'''
if needle not in s: raise SystemExit('search needle not found')
s=s.replace(needle,replacement)
p.write_text(s)

css=Path('/home/ubuntu/hoiku-note/client/src/index.css')
c=css.read_text()
c += '''\n.topic-card { display:block; color:inherit; text-decoration:none; }\n.category-tabs { display:flex; gap:7px; flex-wrap:wrap; margin-top:14px; }.category-tabs button { padding:8px 13px; border:1px solid #e2ded5; border-radius:999px; background:#fbfaf7; color:#7b8581; font-size:11px; font-weight:700; transition:all .2s ease; }.category-tabs button:hover,.category-tabs button.active { border-color:#e7826b; background:#f9e5df; color:#bd6655; }\n.modal-backdrop { position:fixed; inset:0; z-index:100; display:flex; align-items:center; justify-content:center; padding:20px; background:rgba(29,46,52,.48); backdrop-filter:blur(6px); }.line-modal { position:relative; width:min(100%,460px); padding:35px 32px 29px; border-radius:20px; background:#fffdfa; box-shadow:0 28px 70px rgba(21,43,50,.25); }.modal-close { position:absolute; top:15px; right:15px; display:flex; align-items:center; justify-content:center; width:32px; height:32px; border-radius:50%; background:#f3f0e9; color:#6f7c7b; }.modal-icon { display:flex; align-items:center; justify-content:center; width:46px; height:46px; margin-bottom:18px; border-radius:14px 14px 14px 5px; background:#e7826b; color:#fff; }.line-modal h2 { margin:12px 0 12px; color:#304a54; font-family:'Zen Maru Gothic',sans-serif; font-size:22px; line-height:1.55; letter-spacing:-.06em; }.line-modal p,.line-modal li { color:#657277; font-size:13px; line-height:1.9; }.line-modal ul { margin:12px 0 18px; padding-left:20px; }.modal-button { text-decoration:none; }.line-modal small { display:block; margin-top:11px; color:#99a19d; font-size:10px; }\n'''
css.write_text(c)
print('patched category tabs and modal styles')
''
