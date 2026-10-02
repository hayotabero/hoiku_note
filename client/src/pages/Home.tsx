import { useMemo, useState } from "react";
import {
  ArrowRight,
  Baby,
  BookOpen,
  BriefcaseBusiness,
  CalendarDays,
  Check,
  ChevronDown,
  CircleHelp,
  Clock3,
  HeartHandshake,
  Menu,
  MessageCircle,
  PenLine,
  Search,
  ShieldAlert,
  Sparkles,
  X,
} from "lucide-react";

const topics = [
  {
    label: "ハラスメント",
    slug: "pawahara-taisho",
    title: "保育士 パワハラ 対処法",
    text: "まずは身を守るために。記録の取り方と相談先を、落ち着いて整理します。",
    icon: ShieldAlert,
    tone: "coral",
  },
  {
    label: "働き方",
    slug: "yukyu-torenai",
    title: "保育士 有給 取れない",
    text: "言い出しづらさの背景と、角が立ちにくい伝え方を一緒に考えます。",
    icon: CalendarDays,
    tone: "sage",
  },
  {
    label: "お金",
    slug: "tedori-20man",
    title: "保育士 手取り20万円",
    text: "経験年数や地域でどう変わる？給与明細を見るときのポイントも紹介。",
    icon: BriefcaseBusiness,
    tone: "blue",
  },
  {
    label: "転職",
    slug: "nendo-tochu-tenshoku",
    title: "保育士 年度途中 転職タイミング",
    text: "年度途中でも動けるケース、円満に話す順番、見極めの軸をまとめました。",
    icon: Clock3,
    tone: "lavender",
  },
  {
    label: "ライフイベント",
    slug: "ninshin-taishoku-trouble",
    title: "保育士 妊娠 退職トラブル",
    text: "おめでたいことなのに気を遣ってしまう。制度と気持ちを分けて整理します。",
    icon: HeartHandshake,
    tone: "peach",
  },
  {
    label: "人間関係",
    slug: "ningen-kankei-tsukareta",
    title: "保育士 人間関係 疲れた",
    text: "苦手な人がいるだけで、毎日が重くなる。園の文化を変える視点も。",
    icon: MessageCircle,
    tone: "mint",
  },
];

const categories = ["すべて", "お金", "人間関係", "体調・ライフイベント", "キャリア", "働き方"];

const salaryRows = [
  ["1〜3年目", "18〜21万円", "手取り20万円は地域によって十分あり得る水準"],
  ["4〜7年目", "20〜24万円", "役職・処遇改善手当の有無で差が出やすい"],
  ["主任クラス", "24〜30万円", "業務量とのバランスも必ず確認したい"],
];

function scrollToId(id: string) {
  document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
}

const LINE_URL = "https://hoiku.proreach.co.jp/rl/instagram_aya-7sqz";

function trackEvent(name: string, params: Record<string, string>) {
  const gtag = (window as Window & { gtag?: (...args: unknown[]) => void }).gtag;
  gtag?.("event", name, params);
}

export default function Home() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState("すべて");
  const [openFaq, setOpenFaq] = useState<number | null>(0);
  const [lineModal, setLineModal] = useState<{ position: "top" | "mid" | "bottom" } | null>(null);

  const openLineModal = (position: "top" | "mid" | "bottom") => {
    setLineModal({ position });
    trackEvent("line_cta_click", { article: "home", position, step: "modal_open" });
  };

  const filteredTopics = useMemo(
    () =>
      topics.filter((topic) => {
        const matchesQuery = `${topic.label}${topic.title}${topic.text}`.toLowerCase().includes(query.toLowerCase());
        const matchesCategory = activeCategory === "すべて" || topic.label === activeCategory || (activeCategory === "体調・ライフイベント" && topic.label === "ライフイベント");
        return matchesQuery && matchesCategory;
      }),
    [query, activeCategory],
  );

  return (
    <div className="min-h-screen bg-[#fbfaf7] text-[#24313b]">
      <div className="topline" />
      <header className="sticky top-0 z-50 border-b border-[#e8e4dc]/80 bg-[#fbfaf7]/90 backdrop-blur-xl">
        <div className="container flex h-[74px] items-center justify-between gap-6">
          <button className="brand flex items-center gap-3" onClick={() => scrollToId("top")} aria-label="保育ノート トップへ">
            <span className="brand-mark"><Baby size={19} strokeWidth={2.4} /></span>
            <span className="text-left leading-none">
              <span className="block font-display text-[19px] font-bold tracking-[-0.04em] text-[#263b49]">保育ノート</span>
              <span className="mt-1 block text-[9px] font-bold tracking-[0.2em] text-[#8b938f]">HOIKU NOTE</span>
            </span>
          </button>

          <nav className="hidden items-center gap-7 md:flex" aria-label="メインナビゲーション">
            <button onClick={() => scrollToId("topics")} className="nav-link">悩みから探す</button>
            <button onClick={() => scrollToId("article")} className="nav-link">読みもの</button>
            <button onClick={() => scrollToId("about")} className="nav-link">保育ノートについて</button>
          </nav>

          <div className="hidden items-center gap-3 sm:flex">
            <button onClick={() => scrollToId("search")} className="icon-button" aria-label="記事を探す"><Search size={18} /></button>
            <button onClick={() => openLineModal("top")} className="header-cta"><MessageCircle size={16} />無料相談</button>
          </div>
          <button className="flex h-10 w-10 items-center justify-center rounded-full border border-[#e3e0d9] md:hidden" onClick={() => setMenuOpen((v) => !v)} aria-label="メニュー">
            {menuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
        {menuOpen && (
          <div className="mobile-menu md:hidden">
            <button onClick={() => { scrollToId("topics"); setMenuOpen(false); }}>悩みから探す <ArrowRight size={15} /></button>
            <button onClick={() => { scrollToId("article"); setMenuOpen(false); }}>読みもの <ArrowRight size={15} /></button>
            <button onClick={() => { scrollToId("line-cta"); setMenuOpen(false); }}>無料相談 <ArrowRight size={15} /></button>
          </div>
        )}
      </header>

      <main id="top">
        <section className="hero-section">
          <div className="container grid items-center gap-12 py-14 md:grid-cols-[1.05fr_.95fr] md:py-20 lg:gap-20 lg:py-24">
            <div className="relative z-10 animate-rise">
              <div className="eyebrow"><Sparkles size={14} />保育士のための、仕事と暮らしのノート</div>
              <h1 className="mt-6 max-w-[680px] font-display text-[clamp(2.5rem,6vw,5.45rem)] font-bold leading-[1.03] tracking-[-0.075em] text-[#273f50]">
                しんどい日も、<br /><span className="text-[#e7826b]">ひとりにしない。</span>
              </h1>
              <p className="mt-7 max-w-[560px] text-[15px] leading-[2] text-[#66727a] md:text-[17px]">
                パワハラ、有給、人間関係、給与、転職。<br className="hidden sm:block" />
                「これって私だけ？」と思ったときに、同じ仕事をする人の目線で、考える材料を届けます。
              </p>
              <div className="mt-9 flex flex-wrap items-center gap-3">
                <button className="primary-button" onClick={() => scrollToId("topics")}>悩みから記事を探す <ArrowRight size={17} /></button>
                <button className="text-button" onClick={() => scrollToId("article")}>まずは読んでみる <span>↘</span></button>
              </div>
              <div className="mt-10 flex items-center gap-4 text-[11px] font-bold tracking-[0.12em] text-[#8b938f]">
                <span className="flex items-center gap-2"><span className="dot dot-coral" />同業者目線</span>
                <span className="flex items-center gap-2"><span className="dot dot-sage" />押し売りなし</span>
                <span className="flex items-center gap-2"><span className="dot dot-blue" />匿名で相談OK</span>
              </div>
            </div>

            <div className="hero-art-wrap animate-float" aria-label="保育士を応援するイラスト">
              <img className="hero-art-image" src="/manus-storage/hoiku-note-hero-compressed_ad8b7881.jpg" alt="ノートと植物、朝の光を描いたイラスト" loading="lazy" decoding="async" />
              <div className="hero-art-bg" />
              <div className="sun-disc" />
              <div className="hero-note-card note-main">
                <div className="note-top"><span>今日の気持ち</span><span>2026.09.15</span></div>
                <div className="note-face">(´･ω･`)</div>
                <p>ちゃんと頑張ってる。<br /><strong>まずは深呼吸。</strong></p>
                <div className="note-line" /><div className="note-line short" />
              </div>
              <div className="hero-note-card note-small">
                <span className="mini-icon"><HeartHandshake size={16} /></span>
                <div><strong>相談していい</strong><small>ひとりで抱えなくて大丈夫</small></div>
              </div>
              <div className="plant plant-left"><span className="leaf leaf-a" /><span className="leaf leaf-b" /><span className="stem" /></div>
              <div className="plant plant-right"><span className="leaf leaf-a" /><span className="leaf leaf-b" /><span className="stem" /></div>
              <div className="art-caption"><PenLine size={13} /> 気持ちを言葉にすると、少し見える。</div>
            </div>
          </div>
          <div className="hero-bottom-label container"><span>SCROLL TO READ</span><span className="scroll-line" /></div>
        </section>

        <section id="topics" className="topics-section section-pad">
          <div className="container">
            <div className="section-heading-row">
              <div>
                <div className="section-kicker">悩みから探す</div>
                <h2 className="section-title">今、いちばん近い悩みは？</h2>
              </div>
              <p className="section-lead">答えを急がず、まずは<br className="hidden sm:block" />状況を整理するところから。</p>
            </div>
            <div id="search" className="search-box mt-8">
              <Search size={19} /><input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="キーワードで記事を探す（例：有給、転職）" aria-label="記事を検索" />
              {query && <button onClick={() => setQuery("")} aria-label="検索をクリア"><X size={16} /></button>}
            </div>
            <div className="category-tabs" role="tablist" aria-label="カテゴリで絞り込む">{categories.map((category) => <button key={category} role="tab" aria-selected={activeCategory === category} className={activeCategory === category ? "active" : ""} onClick={() => setActiveCategory(category)}>{category}</button>)}</div>
            <div className="topic-grid mt-6">
              {filteredTopics.map((topic, index) => {
                const Icon = topic.icon;
                return (
                  <a key={topic.title} href={`/articles/${topic.slug}/index.html`} className={`topic-card topic-${topic.tone}`} style={{ animationDelay: `${index * 45}ms` }}>
                    <div className="topic-card-top"><span className="topic-label">{topic.label}</span><Icon size={22} strokeWidth={1.8} /></div>
                    <h3>{topic.title}</h3><p>{topic.text}</p><span className="card-arrow"><ArrowRight size={16} /></span>
                  </a>
                );
              })}
              {filteredTopics.length === 0 && <div className="empty-search">「{query}」に近い記事はまだありません。言葉を変えて探してみてください。</div>}
            </div>
          </div>
        </section>

        <section id="article" className="article-section section-pad">
          <div className="container grid gap-12 lg:grid-cols-[minmax(0,1fr)_300px] lg:gap-20">
            <article className="article-copy">
              <div className="article-meta"><span className="article-category">特集</span><span>2026.09.15</span><span>読了目安 8分</span></div>
              <h2 className="article-title">保育士の悩みを、<br className="sm:hidden" />ひとつずつ整える。</h2>
              <p className="article-intro">「辞めたい」と思うほど頑張っている人へ。ここでは、よくある悩みをいったん分解して、今日からできる小さな対処法と、環境を変えるときの見極め方をまとめます。</p>

              <div className="callout quote-callout"><span className="quote-mark">“</span><p>つらさを感じるのは、あなたの我慢が足りないからではありません。職場の仕組みや文化が合っていないこともあります。</p></div>

              <div className="article-h2"><span>01</span><h3>結論・共感導入</h3></div>
              <h4>こんな悩みありませんか？</h4>
              <p>「先輩の機嫌を毎日うかがってしまう」「有給を取りたいと言うと、誰かに負担がかかる気がする」「手取り20万円。頑張っているのに、この先が見えない」——。保育の仕事が好きだからこそ、簡単には離れられず、気づかないうちに心身がすり減ってしまうことがあります。</p>
              <p>年度途中の転職や、妊娠をきっかけにした退職も、周囲の反応が気になって迷いますよね。まず知っておきたいのは、悩みを言葉にすることは、園への裏切りではないということ。自分の働き方を守るための、まっとうな準備です。</p>

              <div className="article-h2"><span>02</span><h3>具体的な原因・実態</h3></div>
              <p>保育士の悩みは、個人の性格だけでなく「人手不足」「閉じた人間関係」「園ごとの慣習」が重なって起こりがちです。たとえば、次のような“あるある”があります。</p>
              <ul className="check-list">
                <li><Check size={17} /><span>園長や主任から、みんなの前で繰り返し叱責される。人格を否定するような言葉が続く。</span></li>
                <li><Check size={17} /><span>「この日しか休めない」と伝えても、代替の人員調整を理由に有給の相談が流れてしまう。</span></li>
                <li><Check size={17} /><span>給与明細を見て手取り20万円前後。処遇改善手当や資格手当の説明がないまま働いている。</span></li>
                <li><Check size={17} /><span>妊娠を報告したら「年度末までは無理だよね」と圧を感じる。退職の相談をすると引き止められる。</span></li>
              </ul>
              <p>有給休暇は、雇用形態など一定の要件を満たす場合に法律上認められる休暇です。取得時期の調整が必要な場合はありますが、「忙しいから一切取れない」が慢性化しているなら、一般論として労働条件通知書や就業規則を確認し、必要に応じて労働局の総合労働相談コーナーなど外部窓口へ相談する方法もあります。制度の適用は個別事情で変わるため、断定せず確認しながら進めましょう。</p>

              <div className="salary-box">
                <div className="salary-head"><div><span className="mini-kicker">CHECK YOUR PAY</span><h4>手取り20万円は多い？少ない？</h4></div><BriefcaseBusiness size={24} /></div>
                <p>地域・経験年数・手当で幅があります。まずは額面と手取りを分けて、自分の条件を見てみましょう。</p>
                <div className="salary-table-wrap"><table><thead><tr><th>目安</th><th>手取りの相場感</th><th>見ておきたいこと</th></tr></thead><tbody>{salaryRows.map((row) => <tr key={row[0]}>{row.map((cell) => <td key={cell}>{cell}</td>)}</tr>)}</tbody></table></div>
              </div>

              <div className="article-h2"><span>03</span><h3>今すぐできる対処法</h3></div>
              <div className="step-list">
                <div className="step-item"><div className="step-number">01</div><div><h4>事実と気持ちを分けて記録する</h4><p>パワハラかもしれない言動は、日時・場所・相手・言われた内容・見ていた人・その後の影響を、できるだけ具体的にメモ。感情を書くのも大切ですが、まずは事実を分けて残すと相談しやすくなります。メールやシフト表など、もともと自分がアクセスできる資料も整理しておきましょう。</p></div></div>
                <div className="step-item"><div className="step-number">02</div><div><h4>希望を「お願い」ではなく具体的に伝える</h4><p>有給なら「○月○日と○日を取得したいです。引き継ぎは△△にまとめます」と、日付・理由・代替案をセットに。年度途中の転職なら「○月末を目安に、引き継ぎ計画を相談したいです」と早めに切り出すと、感情的なぶつかりを減らせます。</p></div></div>
                <div className="step-item"><div className="step-number">03</div><div><h4>一人で抱えず、相談先を二つ持つ</h4><p>園内なら直属の上司以外の管理者・法人本部・相談窓口。園外なら自治体の保育担当、労働局の総合労働相談コーナー、家族や信頼できる友人など。妊娠や体調に関わる場合は、主治医や自治体の相談先に確認しながら進めてください。相談先を分散すると、判断を急がずに済みます。</p></div></div>
                <div className="step-item"><div className="step-number">04</div><div><h4>「変わる可能性」を期限つきで見てみる</h4><p>改善を求めたあと、2〜4週間だけ様子を見るなど、自分なりの期限を決めます。話し合いの結果、配置や休みの取り方が変わったか。逆に、相談したことで不利益な扱いが増えたか。環境を見極める材料を集めましょう。</p></div></div>
              </div>

              <div className="inline-cta"><div className="inline-cta-icon"><CircleHelp size={22} /></div><div><strong>対処法はある。でも、相性の問題かもしれません。</strong><p>工夫しても毎日が苦しいなら、あなたの努力不足ではなく、園の文化との相性が合っていない可能性も。転職情報を見るだけでも、選択肢は増やせます。</p></div><button onClick={() => scrollToId("line-cta")}><ArrowRight size={18} /></button></div>

              <div className="article-h2"><span>04</span><h3>それでも改善しない場合の選択肢</h3></div>
              <p>人間関係は、個人の頑張りだけでは変えにくいものです。園長が職員の意見を聞く文化か、休憩や有給を「お互いさま」と考えられるか、給与や手当を説明してくれるか。求人票だけでなく、面接や見学で確かめられる部分があります。</p>
              <p>年度途中の転職は、引き継ぎや子どもたちへの配慮が必要な一方、採用側と条件が合えば早く環境を変えられるメリットもあります。妊娠・出産後の働き方も、退職だけでなく休業や復職、別の園での再スタートなど選択肢は一つではありません。大切なのは、今の園に残ることを“義務”にしないことです。</p>
              <div className="soft-panel"><span className="soft-panel-icon">◎</span><div><strong>見学で聞いていい質問</strong><p>「有給はどのように申請していますか？」「職員の相談窓口はありますか？」「産休・育休からの復職実績はありますか？」——働き続ける前提で確認することは、失礼ではありません。</p></div></div>

              <div className="article-h2"><span>05</span><h3>まとめ</h3></div>
              <p>保育士の悩みは、我慢で解決するものばかりではありません。記録する、具体的に伝える、相談先を持つ、期限を決めて見極める。小さく動くと、残る・休む・転職するという選択肢を、自分で比べられるようになります。</p>
            </article>

            <aside className="article-aside">
              <div className="aside-sticky">
                <div className="aside-card about-card" id="about"><div className="aside-avatar"><Baby size={24} /></div><span className="mini-kicker">ABOUT HOIKU NOTE</span><h3>保育士の毎日に、<br />考える余白を。</h3><p>同じ現場を知る編集チームが、仕事のモヤモヤを整理する記事を届けています。</p><button onClick={() => openLineModal("mid")} className="aside-link">LINEで話を聞く <ArrowRight size={15} /></button></div>
                <div className="aside-card toc-card"><span className="mini-kicker">IN THIS ARTICLE</span><button onClick={() => scrollToId("article")}>01　結論・共感導入</button><button onClick={() => scrollToId("article")}>02　具体的な原因・実態</button><button onClick={() => scrollToId("article")}>03　今すぐできる対処法</button><button onClick={() => scrollToId("article")}>04　改善しない場合の選択肢</button><button onClick={() => scrollToId("line-cta")}>05　まとめ</button></div>
                <div className="aside-note"><BookOpen size={17} /><span>制度や法律は個別事情で変わります。記事は情報整理のためにご活用ください。</span></div>
              </div>
            </aside>
          </div>
        </section>

        <section id="line-cta" className="line-cta-section">
          <div className="container">
            <div className="line-cta-box">
              <div className="line-cta-copy"><div className="eyebrow eyebrow-light"><MessageCircle size={14} /> INFORMATION & SUPPORT</div><h2>一人で抱え込まず、<br /><span>まずは話を聞いてほしい。</span></h2><p>まとまっていなくても大丈夫です。今の状況を話しながら、次にできることを一緒に整理します。</p><button className="line-button" onClick={() => openLineModal("bottom")}>LINEで無料相談する <ArrowRight size={17} /></button><small>※相談は無料。無理な勧誘はありません。</small></div>
              <div className="line-cta-art"><div className="cta-circle cta-circle-one" /><div className="cta-circle cta-circle-two" /><div className="chat-bubble bubble-one">話していいよ</div><div className="chat-bubble bubble-two">大丈夫、急がなくていい</div><div className="cta-heart">♡</div></div>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer"><div className="container flex flex-col justify-between gap-5 py-8 sm:flex-row sm:items-center"><div><div className="footer-brand">保育ノート</div><p>保育士の悩みに寄り添う、仕事と暮らしのメディア</p></div><div className="footer-links"><button onClick={() => scrollToId("topics")}>悩みから探す</button><button onClick={() => scrollToId("about")}>運営について</button><span>© 2026 Hoiku Note</span></div></div></footer>
      {lineModal && <div className="modal-backdrop" role="presentation" onClick={() => setLineModal(null)}><div className="line-modal" role="dialog" aria-modal="true" aria-labelledby="line-modal-title" onClick={(event) => event.stopPropagation()}><button className="modal-close" onClick={() => setLineModal(null)} aria-label="閉じる"><X size={18} /></button><div className="modal-icon"><MessageCircle size={22} /></div><span className="mini-kicker">LINE FREE CONSULTATION</span><h2 id="line-modal-title">相談内容は、まとまっていなくて大丈夫です。</h2><p>たとえば、こんなことから話せます。</p><ul><li>職場の人間関係やパワハラがつらい</li><li>有給・給与・転職のことを聞きたい</li><li>妊娠や退職について誰かに相談したい</li></ul><a className="line-button modal-button" href={LINE_URL} target="_blank" rel="noreferrer" onClick={() => trackEvent("line_cta_click", { article: "home", position: lineModal.position, step: "line_redirect" })}>LINEで無料相談をはじめる <ArrowRight size={17} /></a><small>外部のLINE相談ページへ移動します。無理な勧誘はありません。</small></div></div>}
    </div>
  );
}
