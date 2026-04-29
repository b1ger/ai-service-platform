# Design Partner Log

## Partner
- **Brand**: Shower Pack (`showerpack.com.ua`)
- **Contact**: Kateryna (owner, family-run with father)
- **Segment**: Ukrainian DTC manufacturer of dry hygiene kits (military / medical / field-use)
- **Founded**: 2017 (pivoted to dry showers in 2022 after full-scale invasion)
- **Award**: Ukrainian Business Awards 2023 — Business Of The Year
- **Sales channels**: own e-commerce site (Horoshop), social messengers (Viber, Telegram, Instagram DM), email
- **Order volumes**: not yet quantified (low — Kateryna says inbound messaging is "not actually a pain")

## Discovery timeline

### 2026-04-29 — first Telegram exchange (initiating)
Operator's opening message (paraphrased): pitching curiosity-led discovery, not selling, asking permission to ask 8–10 questions in messenger over a week.

Partner response (verbatim):
> "З повідомленнями зараз не так актуально, бо пишуть небагато і замовляють одразу на сайті."
> "В нас вручну відправка повідомлення смс з інформацією про день відправки, це Іра робить, коли формує ТТН."
> "Іра обробляє вручну, але то швидко, там просто пару галочок поставити."
> "Чеки створюю теж через пару кліків, тобто не прям багато часу."
> "**Мій біль зараз це SEO, я з чатом жпт платним вже місяць роблю повний перепис сторінок на сайті з потрібними мені ключовими.**"
> "Але мені ще товарів 30 переписати треба, і загальних сторінок може 10–20."
> "+ згенерувати фото для цього всього"
> "Ми щодня пишемо 10–15 людям, які робили замовлення рівно місяць тому. ... в різних месенджерах."
> "Ще можна з імейл розсилкою щось придумати. ... ChatGPT-ик прописував, але дизайн вручну робили через сендпульс."

### 2026-04-29 — second exchange (quantification)
Partner verbatim:
> "По часу: я в робочий день, окрім інших задач, беру 2-3 товари і повністю їх пропрацювую. Якщо це товар з описом та штук 5 фото оброблених, то на кожен з них я по годині точно витрачаю. Тобто на 2-3 товари йде десь 3, навіть 4 години."
> "**Найважче — генерувати фото та просити ШІ їх обробити. Він регулярно робить помилки. Оце прям топ по складності.**"
> "Вносити на сайт мені ок. Трошки ще вичитую."
> "Ще треба посилання подавати в тексти, щоб були лінки усередині сайту на інші сторінки."
> "Іра пише... стандартне повідомлення, не адаптуємо під клієнтів... тому і не пишемо одразу великій кількості людей, щоб не було сприйнято за спам."
> "Думали над автоматизацією... але там або смс (мало читають), або лише Вайбер. Вайбер не у всіх і виходить невиправдано дорого. А Іра вручну шукає в кого який месенджер активний."
> "**Першою SEO, бо вона горить найбільше і це якраз моя задача, яку я маю проконтролювати і зробити добре.**"

### 2026-04-29 — third exchange (technical detail + ChatGPT chats)
Partner shared four ChatGPT share-links showing actual image-editing sessions, plus brief annotations:
- Chat 1: bundle photo "10 dry showers + sushkar gift" — count was wrong, AI invented a fictional product
- Chat 2: socks product introduction — multiple iterations, lost product fidelity
- Chat 3: towel material substitution — three rounds of spatial misidentification, AI changed wrong layers
- Chat 4: military trench use-case shot — mitt repeatedly placed incorrectly (worn as glove instead of held in hands), packaging text distorted

Partner answers to operator's clarifying questions:
- Platform: **Horoshop**
- Photo source: **mix** (real product photos from production + studio + situational; some need composing with AI-generated scenes)
- Most valuable component if forced to choose: **photos** ("текст я можу окремо згенерувати / підправити і посилання вручну швидко додаються")
- Ideal: "все разом — найкраще! Щоб вже була готова картка продукту і мені лишилось її заповнити просто."

## Discovery findings — ranked

### Top pain (validated)
**SEO product card preparation, image work specifically.** ~15–20 hours/week of personal owner time. ~50–70 hours of remaining work to clear current backlog (30 products + 10–20 pages). Owner is buyer and user. Already pays for AI tools (ChatGPT Plus). High measurable ROI (organic search position → traffic → sales, tracked in Google Analytics).

### Secondary pain (not yet productized)
**30-day re-engagement messaging.** Daily 10–15 messages across multiple messengers, manually routed by which messenger each customer used. Not selected for product focus, but interesting cross-messenger routing problem worth keeping in long-term backlog.

### Tertiary signal
**Email newsletter content.** ChatGPT writes content; design done manually in SendPulse; produces 1–5 orders per send per Google Analytics. Lower priority.

### Confirmed non-pains
- Order intake (CRM handles it well)
- Order processing (Ira handles in seconds)
- Invoice creation (few clicks)
- TTN / Nova Poshta dispatch (manual but fast)

## Product fit analysis
- The validated pain (SEO image work) is exactly what the Composer hypothesis addresses
- The four ChatGPT conversations provided are an unusually detailed technical brief for failure modes (see `FAILURE_MODES_OBSERVED.md`)
- Partner has explicitly named the architectural insight herself: *"Тобі НЕ треба генерити рукавицю взагалі — у тебе вже є ідеальний асет."*
- Partner is sophisticated enough to give meaningful feedback on prototypes
- Partner is the right ICP profile (Ukrainian DTC manufacturer, owner-operator, Horoshop seller)

## Open questions (to address on voice call)
1. Confirm Horoshop API access and willingness to test API-based upload
2. Reconfirm: which 5–7 of the standard e-com photo templates does she actually need first? (hero, use-case, components, compactness, comparison, scenarios, result)
3. What budget range is realistic for a tool like this once it works? (anchor: she pays for ChatGPT Plus, ~800 UAH/mo)
4. Willingness to share full asset library (real product photos) for prototype testing
5. Willingness to be a public reference / case study after first successful month
6. Comfortable with web-only (browser) MVP or does she need mobile?

## Design Partner Agreement — draft principles (to formalize in 1-page doc)
- Free use of Composer for first 6 months (or until 50 successful generations, whichever later)
- Partner provides: product asset library, real workflow data, weekly 15-minute feedback call during build phase
- Operator provides: prototype within 6–8 weeks, weekly progress updates, hands-on troubleshooting
- Public usage rights: operator can describe the partnership and use anonymized examples in marketing once Composer is publicly available (partner has approval rights on specifics)
- Graceful exit: either party can end the partnership with 2 weeks notice; nothing built becomes proprietary to either side
- No guarantees: this is a build-together arrangement, not a vendor relationship

## Next steps with partner
See `NEXT_STEPS.md`. Highest priority: schedule and conduct 25–30 minute voice call.
