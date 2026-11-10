/* Cozy Comfort Insulation chat box. One file, works on the static site and the live WordPress site.
   Language: <html lang="es"> = Spanish, anything else = English. Posts to the lead handler -> GHL. */
(function () {
  if (window.__cozyChat) return; window.__cozyChat = 1;
  var ENDPOINT = "https://cozy-lead.5-223-88-156.sslip.io/lead";
  var es = (document.documentElement.lang || "en").toLowerCase().indexOf("es") === 0;
  var T = es ? {
    btn: "Cotización gratis", title: "Cozy Comfort Insulation", sub: "Le llamamos para su cotización gratis",
    hi: "¡Hola! Le haré unas preguntas rápidas y uno de nuestros asesores le llamará. ¿Cuál es su nombre?",
    phone: "Gracias, {n}. ¿Cuál es su número de teléfono?", email: "¿Cuál es su correo electrónico?",
    zip: "¿Cuál es su código postal?", service: "¿Qué servicio le interesa?", time: "¿Cuándo prefiere que le llamemos?",
    done: "¡Listo, {n}! Recibimos sus datos. Le llamaremos {t}. Si es urgente, llame al (818) 927-7494.",
    err: "No se pudo enviar. Por favor llámenos al (818) 927-7494.", send: "Enviar", ph: "Escriba aquí",
    bad: { name: "Escriba su nombre.", phone: "Escriba un teléfono de 10 dígitos.", email: "Escriba un correo válido.", zip: "Escriba un código postal de 5 dígitos." },
    sv: [["attic", "Aislamiento de ático"], ["blown-in", "Aislamiento soplado"], ["spray-foam", "Espuma en aerosol"], ["crawl-space", "Espacio de acceso (crawl space)"], ["removal", "Retiro y reemplazo"], ["radiant-barrier", "Barrera radiante"], ["other", "No estoy seguro / otro"]],
    tm: [["Lo antes posible", "lo antes posible"], ["Mañana (8 am – 12 pm)", "por la mañana (8 am – 12 pm)"], ["Tarde (12 – 5 pm)", "por la tarde (12 – 5 pm)"], ["Noche (5 – 8 pm)", "por la noche (5 – 8 pm)"]],
    close: "Cerrar"
  } : {
    btn: "Free quote", title: "Cozy Comfort Insulation", sub: "We'll call you with your free quote",
    hi: "Hi! I'll ask a few quick questions and one of our advisors will call you. What's your name?",
    phone: "Thanks, {n}. What's the best phone number?", email: "What's your email address?",
    zip: "What's your zip code?", service: "Which service are you interested in?", time: "When should we call you?",
    done: "All set, {n}! We got your details and will call you {t}. If it's urgent, call (818) 927-7494.",
    err: "That didn't go through. Please call us at (818) 927-7494.", send: "Send", ph: "Type here",
    bad: { name: "Please enter your name.", phone: "Please enter a 10-digit phone number.", email: "Please enter a valid email.", zip: "Please enter a 5-digit zip code." },
    sv: [["attic", "Attic insulation"], ["blown-in", "Blown-in insulation"], ["spray-foam", "Spray foam"], ["crawl-space", "Crawl space"], ["removal", "Removal & replacement"], ["radiant-barrier", "Radiant barrier"], ["other", "Not sure / other"]],
    tm: [["As soon as possible", "as soon as possible"], ["Morning (8am-12pm)", "in the morning (8am-12pm)"], ["Afternoon (12-5pm)", "in the afternoon (12-5pm)"], ["Evening (5-8pm)", "in the evening (5-8pm)"]],
    close: "Close"
  };
  var css = ".cc-b{position:fixed;right:18px;bottom:18px;z-index:2147483000;background:#f4a030;color:#1b2a3a;border:0;border-radius:999px;padding:14px 22px;font:700 16px/1 system-ui,Arial,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.28);cursor:pointer}" +
    ".cc-p{position:fixed;right:18px;bottom:18px;z-index:2147483001;width:360px;max-width:calc(100vw - 24px);height:520px;max-height:calc(100vh - 24px);background:#fff;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,.35);display:none;flex-direction:column;overflow:hidden;font:15px/1.4 system-ui,Arial,sans-serif;color:#1b2a3a}" +
    ".cc-p.o{display:flex}.cc-h{background:#2f7fc1;color:#fff;padding:12px 14px;display:flex;align-items:center;gap:10px}.cc-h b{display:block;font-size:15px}.cc-h span{font-size:12px;opacity:.9}.cc-h button{margin-left:auto;background:none;border:0;color:#fff;font-size:24px;cursor:pointer;line-height:1}" +
    ".cc-m{flex:1;overflow:auto;padding:14px;background:#f5f8fb;display:flex;flex-direction:column;gap:8px}.cc-m div{max-width:85%;padding:9px 12px;border-radius:14px;word-wrap:break-word}.cc-m .a{background:#fff;border:1px solid #dfe7ee;align-self:flex-start}.cc-m .u{background:#2f7fc1;color:#fff;align-self:flex-end}.cc-m .e{color:#b3261e;font-size:13px;align-self:flex-start;padding:0 4px}" +
    ".cc-c{display:flex;flex-wrap:wrap;gap:6px;padding:0 14px 10px;background:#f5f8fb}.cc-c button{background:#fff;border:1.5px solid #2f7fc1;color:#2f7fc1;border-radius:999px;padding:8px 12px;font:600 14px system-ui,Arial,sans-serif;cursor:pointer}" +
    ".cc-f{display:flex;gap:8px;padding:10px;border-top:1px solid #e3e9ef;background:#fff}.cc-f input{flex:1;border:1.5px solid #c9d5df;border-radius:10px;padding:10px;font-size:16px;min-width:0}.cc-f button{background:#2f7fc1;color:#fff;border:0;border-radius:10px;padding:0 16px;font:700 15px system-ui,Arial,sans-serif;cursor:pointer}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  var btn = document.createElement("button"); btn.className = "cc-b"; btn.type = "button"; btn.textContent = T.btn; btn.setAttribute("aria-label", T.btn);
  var p = document.createElement("div"); p.className = "cc-p"; p.setAttribute("role", "dialog"); p.setAttribute("aria-label", T.title);
  p.innerHTML = '<div class="cc-h"><div><b></b><span></span></div><button type="button" aria-label=""></button></div><div class="cc-m" aria-live="polite"></div><div class="cc-c"></div><form class="cc-f"><input name="v" autocomplete="off"><button type="submit"></button></form>';
  document.body.appendChild(btn); document.body.appendChild(p);
  var $ = function (s) { return p.querySelector(s); };
  $(".cc-h b").textContent = T.title; $(".cc-h span").textContent = T.sub; $(".cc-h button").innerHTML = "&times;"; $(".cc-h button").setAttribute("aria-label", T.close);
  $(".cc-f button").textContent = T.send; $(".cc-f input").placeholder = T.ph;
  var M = $(".cc-m"), C = $(".cc-c"), F = $(".cc-f"), I = F.v, d = {}, step = 0, started = false, busy = false;
  var EN_SV = ["Attic insulation", "Blown-in insulation", "Spray foam", "Crawl space", "Removal & replacement", "Radiant barrier", "Not sure / other"];
  var EN_TM = ["As soon as possible", "Morning (8am-12pm)", "Afternoon (12-5pm)", "Evening (5-8pm)"];
  var steps = ["name", "phone", "email", "zip", "service", "time"];
  function say(t, cls) { var e = document.createElement("div"); e.className = cls; e.textContent = t; M.appendChild(e); M.scrollTop = M.scrollHeight; }
  function ask() {
    C.innerHTML = ""; var k = steps[step];
    var q = { name: T.hi, phone: T.phone, email: T.email, zip: T.zip, service: T.service, time: T.time }[k].replace("{n}", (d.name || "").split(" ")[0]);
    say(q, "a");
    var chips = k === "service" ? T.sv : k === "time" ? T.tm : null;
    F.style.display = chips ? "none" : "flex";
    if (chips) chips.forEach(function (o) { var b = document.createElement("button"); b.type = "button"; b.textContent = o[0]; b.onclick = function () { answer(k, o); }; C.appendChild(b); });
    else { I.type = k === "email" ? "email" : k === "phone" ? "tel" : "text"; I.inputMode = k === "zip" ? "numeric" : ""; I.value = ""; I.focus(); }
  }
  function answer(k, o) {
    if (busy) return;
    if (k === "service") { d.service_key = T.sv.indexOf(o); say(o[1], "u"); }
    else { d.time_key = T.tm.indexOf(o); d.time_say = o[1]; say(o[0], "u"); }
    next();
  }
  function next() { step++; if (step < steps.length) ask(); else submit(); }
  F.onsubmit = function (e) {
    e.preventDefault(); var k = steps[step], v = I.value.trim(), bad = null;
    if (k === "name" && v.length < 2) bad = T.bad.name;
    if (k === "phone") { var n = v.replace(/\D/g, ""); if (n.length === 11 && n[0] === "1") n = n.slice(1); if (n.length !== 10) bad = T.bad.phone; v = n; }
    if (k === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) bad = T.bad.email;
    if (k === "zip" && !/^\d{5}$/.test(v)) bad = T.bad.zip;
    if (bad) { say(bad, "e"); return; }
    d[k] = v; say(k === "phone" ? v.replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3") : v, "u"); next();
  };
  function submit() {
    busy = true; C.innerHTML = ""; F.style.display = "none";
    var keys = ["attic", "blown-in", "spray-foam", "crawl-space", "removal", "radiant-barrier", "other"];
    var body = { name: d.name, phone: d.phone, email: d.email, zip: d.zip, service: keys[d.service_key],
      service_label: EN_SV[d.service_key], time_label: EN_TM[d.time_key], lang: es ? "es" : "en",
      source: location.hostname.indexOf("github.io") > -1 ? "preview-site" : "live-site", website: "" };
    var x = new XMLHttpRequest(); x.open("POST", ENDPOINT); x.setRequestHeader("Content-Type", "application/json");
    x.onload = function () { var ok = false; try { ok = JSON.parse(x.responseText).ok; } catch (e) {} busy = false;
      say(ok ? T.done.replace("{n}", d.name.split(" ")[0]).replace("{t}", d.time_say) : T.err, ok ? "a" : "e"); };
    x.onerror = function () { busy = false; say(T.err, "e"); };
    x.send(JSON.stringify(body));
  }
  function open() { p.classList.add("o"); btn.style.display = "none"; if (!started) { started = true; ask(); } }
  btn.onclick = open;
  $(".cc-h button").onclick = function () { p.classList.remove("o"); btn.style.display = ""; };
  document.addEventListener("click", function (e) { var a = e.target.closest && e.target.closest("[data-cozy-chat]"); if (a) { e.preventDefault(); open(); } });
})();
